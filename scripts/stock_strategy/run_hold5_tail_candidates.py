from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
import random
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen


BASE_DIR = Path(__file__).resolve().parents[2]
CLIST_URL = "https://push2.eastmoney.com/api/qt/clist/get"
ULIST_URL = "https://push2.eastmoney.com/api/qt/ulist.np/get"
KLINE_URL = "https://push2his.eastmoney.com/api/qt/stock/kline/get"
TENCENT_QUOTE_URL = "https://qt.gtimg.cn/q=sh000001,sz399001,sz399006"
ROUND_TRIP_COST = 0.0013
BENCHMARK_GATE_SAMPLE_DAYS = 30
BENCHMARK_GATE_MIN_SAMPLES = 12
BENCHMARK_GATE_MIN_AVG_RETURN = 0.008
BENCHMARK_GATE_MIN_WIN_RATE = 0.50
BENCHMARK_GATE_MIN_EXCESS_BEST_RETURN = -0.025
BENCHMARK_GATE_MIN_MAX_DRAWDOWN = -0.65
QUOTE_FIELDS = ",".join([
    "f2", "f3", "f4", "f5", "f6", "f8", "f10", "f12", "f13", "f14", "f15",
    "f16", "f17", "f18", "f62", "f86", "f100", "f184",
])


@dataclass(frozen=True)
class Quote:
    secucode: str
    code: str
    name: str
    market: int
    price: float
    pct: float
    change: float
    volume: float
    amount: float
    high: float
    low: float
    open: float
    prev_close: float
    turnover: float
    volume_ratio: float
    main_net: float
    main_net_pct: float
    industry: str
    timestamp: str


@dataclass(frozen=True)
class Bar:
    date: str
    open: float
    close: float
    high: float
    low: float
    volume: float
    amount: float
    amplitude: float
    pct: float
    change: float
    turnover: float


def as_float(value: Any, default: float = 0.0) -> float:
    try:
        if value in (None, "", "-"):
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def pct(value: float) -> str:
    return f"{value * 100:.2f}%"


def safe_div(num: float, den: float, default: float = 0.0) -> float:
    return num / den if abs(den) > 1e-12 else default


def candidate_quality_score(
    *,
    win_rate: float,
    avg_return: float,
    median_return: float,
    profit_factor: float,
    reward_risk: float,
    worst_return: float,
    worst_hold_drawdown: float,
    sample_max_drawdown: float,
    close_pos: float,
    amount: float,
    industry_avg_pct: float,
    industry_adv_ratio: float,
    ret5: float,
    dist_ma20: float,
    vol_ratio_log: float,
    main_net_ratio: float = 0.0,
) -> float:
    del median_return, reward_risk, worst_return, worst_hold_drawdown
    del industry_adv_ratio, ret5, dist_ma20, vol_ratio_log
    return (
        win_rate * 30
        + avg_return * 350
        + min(profit_factor, 8.0) * 4
        + close_pos * 10
        + safe_div(amount, 1_000_000_000) * 1.5
        + industry_avg_pct * 80
        + main_net_ratio * 10
        + max(sample_max_drawdown, -0.5) * 20
    )


def request_json(url: str, referer: str = "https://quote.eastmoney.com/", retries: int = 6) -> dict[str, Any]:
    last_exc: Exception | None = None
    for attempt in range(retries):
        try:
            req = Request(url, headers={"User-Agent": "Mozilla/5.0", "Referer": referer})
            with urlopen(req, timeout=15) as response:
                return json.loads(response.read().decode("utf-8"))
        except Exception as exc:  # noqa: BLE001 - network endpoints are flaky.
            last_exc = exc
            time.sleep(0.45 + attempt * 0.75 + random.random() * 0.25)
    raise RuntimeError(str(last_exc))


def secucode(code: str, market: int) -> str:
    return f"{code}.{'SH' if market == 1 else 'SZ'}"


def secid(code: str, market: int) -> str:
    return f"{market}.{code}"


def parse_quote_item(item: dict[str, Any]) -> Quote | None:
    code = str(item.get("f12") or "")
    market = int(as_float(item.get("f13"), -1))
    price = as_float(item.get("f2"))
    if not code or market not in {0, 1}:
        return None
    ts = int(as_float(item.get("f86")))
    if ts < 1_000_000_000:
        ts = 0
    timestamp = datetime.fromtimestamp(ts).isoformat(timespec="seconds") if ts > 0 else ""
    return Quote(
        secucode=secucode(code, market),
        code=code,
        name=str(item.get("f14") or ""),
        market=market,
        price=price,
        pct=as_float(item.get("f3")) / 100.0,
        change=as_float(item.get("f4")),
        volume=as_float(item.get("f5")),
        amount=as_float(item.get("f6")),
        high=as_float(item.get("f15")),
        low=as_float(item.get("f16")),
        open=as_float(item.get("f17")),
        prev_close=as_float(item.get("f18")),
        turnover=as_float(item.get("f8")),
        volume_ratio=as_float(item.get("f10")),
        main_net=as_float(item.get("f62")),
        main_net_pct=as_float(item.get("f184")) / 100.0,
        industry=str(item.get("f100") or ""),
        timestamp=timestamp,
    )


def fetch_clist() -> list[Quote]:
    rows: list[Quote] = []
    page = 1
    total = 0
    consecutive_errors = 0
    while True:
        params = {
            "pn": page,
            "pz": 100,
            "po": 1,
            "np": 1,
            "fltt": 2,
            "invt": 2,
            "fid": "f6",
            "fs": "m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23",
            "fields": QUOTE_FIELDS,
        }
        try:
            payload = request_json(f"{CLIST_URL}?{urlencode(params)}")
            consecutive_errors = 0
        except Exception as exc:  # noqa: BLE001
            consecutive_errors += 1
            print(f"WARN clist page {page} failed: {exc}", flush=True)
            if consecutive_errors >= 4 or (total and page > math.ceil(total / 100)):
                break
            page += 1
            continue
        data = payload.get("data") or {}
        total = int(data.get("total") or total or 0)
        diff = data.get("diff") or []
        if not diff:
            break
        for item in diff:
            quote = parse_quote_item(item)
            if quote is not None:
                rows.append(quote)
        if total and len(rows) >= total:
            break
        if total and page >= math.ceil(total / 100):
            break
        page += 1
    return rows


def market_from_secucode(value: str) -> tuple[str, int]:
    code, suffix = value.split(".", 1)
    return code, 1 if suffix.upper() == "SH" else 0


def fetch_light_quotes(secucodes: list[str]) -> dict[str, Quote]:
    if not secucodes:
        return {}
    secids = []
    for item in secucodes:
        code, market = market_from_secucode(item)
        secids.append(secid(code, market))
    params = {
        "fltt": 2,
        "invt": 2,
        "fields": QUOTE_FIELDS,
        "secids": ",".join(secids),
    }
    payload = request_json(f"{ULIST_URL}?{urlencode(params)}")
    rows: dict[str, Quote] = {}
    for item in ((payload.get("data") or {}).get("diff") or []):
        quote = parse_quote_item(item)
        if quote is not None:
            rows[quote.secucode] = quote
    return rows


def fetch_bars(quote: Quote, beg: str, end: str) -> list[Bar]:
    params = {
        "secid": secid(quote.code, quote.market),
        "fields1": "f1,f2,f3,f4,f5,f6",
        "fields2": "f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61",
        "klt": "101",
        "fqt": "1",
        "beg": beg,
        "end": end,
    }
    payload = request_json(f"{KLINE_URL}?{urlencode(params)}")
    lines = ((payload.get("data") or {}).get("klines") or [])
    bars: list[Bar] = []
    for line in lines:
        parts = str(line).split(",")
        if len(parts) < 11:
            continue
        bars.append(Bar(
            date=parts[0],
            open=as_float(parts[1]),
            close=as_float(parts[2]),
            high=as_float(parts[3]),
            low=as_float(parts[4]),
            volume=as_float(parts[5]),
            amount=as_float(parts[6]),
            amplitude=as_float(parts[7]) / 100.0,
            pct=as_float(parts[8]) / 100.0,
            change=as_float(parts[9]),
            turnover=as_float(parts[10]),
        ))
    bars.sort(key=lambda item: item.date)
    return bars


def fetch_indices() -> dict[str, tuple[float, float]]:
    req = Request(TENCENT_QUOTE_URL, headers={"User-Agent": "Mozilla/5.0", "Referer": "https://gu.qq.com/"})
    with urlopen(req, timeout=12) as response:
        text = response.read().decode("gbk", errors="ignore")
    result: dict[str, tuple[float, float]] = {}
    for chunk in text.split(";"):
        if "=" not in chunk:
            continue
        key, raw = chunk.split("=", 1)
        values = raw.strip().strip('"').split("~")
        if len(values) < 32:
            continue
        symbol = key.strip().replace("v_", "")
        result[symbol] = (as_float(values[3]), as_float(values[32]) / 100.0)
    return result


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def atr_pct(bars: list[Bar], idx: int, period: int = 14) -> float:
    values: list[float] = []
    for pos in range(max(1, idx - period + 1), idx + 1):
        prev = bars[pos - 1].close
        bar = bars[pos]
        tr = max(bar.high - bar.low, abs(bar.high - prev), abs(bar.low - prev))
        values.append(safe_div(tr, bar.close))
    return mean(values)


def close_return(bars: list[Bar], start: int, end: int) -> float:
    return safe_div(bars[end].close, bars[start].close, 1.0) - 1.0


def feature_vector(bars: list[Bar], idx: int) -> dict[str, float]:
    bar = bars[idx]
    prev = bars[idx - 1] if idx > 0 else bar
    ma5 = mean([item.close for item in bars[max(0, idx - 4): idx + 1]]) or bar.close
    ma20 = mean([item.close for item in bars[max(0, idx - 19): idx + 1]]) or bar.close
    vol20 = mean([item.volume for item in bars[max(0, idx - 19): idx + 1]]) or bar.volume
    day_range = max(bar.high - bar.low, 1e-9)
    return {
        "pct": bar.pct,
        "prev_pct": prev.pct,
        "ret3": close_return(bars, max(0, idx - 3), idx),
        "ret5": close_return(bars, max(0, idx - 5), idx),
        "amp": safe_div(bar.high - bar.low, prev.close),
        "close_pos": safe_div(bar.close - bar.low, day_range, 0.5),
        "dist_ma5": safe_div(bar.close, ma5, 1.0) - 1.0,
        "dist_ma20": safe_div(bar.close, ma20, 1.0) - 1.0,
        "atr_pct": atr_pct(bars, idx),
        "vol_ratio_log": math.log(max(safe_div(bar.volume, vol20, 1.0), 1e-6)),
    }


FEATURE_WEIGHTS = {
    "pct": 1.5,
    "prev_pct": 0.7,
    "ret3": 0.8,
    "ret5": 0.6,
    "amp": 0.7,
    "close_pos": 0.7,
    "dist_ma5": 0.8,
    "dist_ma20": 0.9,
    "atr_pct": 0.6,
    "vol_ratio_log": 0.3,
}


def distance(left: dict[str, float], right: dict[str, float]) -> float:
    return sum(FEATURE_WEIGHTS[key] * abs(left.get(key, 0.0) - right.get(key, 0.0)) for key in FEATURE_WEIGHTS)


def max_drawdown(returns: list[float]) -> float:
    equity = 1.0
    peak = 1.0
    worst = 0.0
    for value in returns:
        equity *= 1.0 + value
        peak = max(peak, equity)
        worst = min(worst, safe_div(equity, peak, 1.0) - 1.0)
    return worst


def is_near_one_price_limit(q: Quote) -> bool:
    if q.prev_close <= 0:
        return False
    amp = (q.high - q.low) / q.prev_close
    limit = 0.195 if q.code.startswith(("30", "68")) else 0.095
    return q.pct >= limit and amp <= 0.012


def analyze_quote(
    q: Quote,
    industry_stats: dict[str, dict[str, float]],
    latest_date: str,
    beg: str,
    end: str,
    analog_count: int,
) -> dict[str, Any]:
    bars = fetch_bars(q, beg, end)
    if len(bars) < 220:
        raise ValueError(f"not enough bars: {len(bars)}")
    if bars[-1].date != latest_date:
        raise ValueError(f"stale kline {bars[-1].date}")

    current_idx = len(bars) - 1
    current = bars[current_idx]
    current_features = feature_vector(bars, current_idx)
    start = max(60, current_idx - 185)
    end_idx = current_idx - 6
    analogs: list[tuple[float, int, float, float]] = []
    for idx in range(start, end_idx + 1):
        dist = distance(current_features, feature_vector(bars, idx))
        net = close_return(bars, idx, idx + 5) - ROUND_TRIP_COST
        trough = min(item.low for item in bars[idx + 1: idx + 6])
        hold_dd = safe_div(trough, bars[idx].close, 1.0) - 1.0
        analogs.append((dist, idx, net, hold_dd))

    selected = sorted(analogs, key=lambda item: item[0])[:analog_count]
    returns = [item[2] for item in selected]
    drawdowns = [item[3] for item in selected]
    wins = [item for item in returns if item > 0]
    losses = [item for item in returns if item < 0]
    pf = safe_div(sum(wins), abs(sum(losses)), 999.0 if wins else 0.0)
    avg = mean(returns)
    med = statistics.median(returns) if returns else 0.0
    p70 = sorted(returns)[int(0.70 * (len(returns) - 1))] if returns else 0.0
    worst = min(returns) if returns else 0.0
    worst_idx = min(selected, key=lambda item: item[2])[1] if selected else -1
    current_close_pos = safe_div(q.price - q.low, max(q.high - q.low, 1e-9), 0.5)
    upper_shadow = safe_div(q.high - q.price, max(q.high - q.low, 1e-9), 0.0)
    atr = atr_pct(bars, current_idx)
    stop_risk = min(0.065, max(0.025, 0.80 * atr))
    stop_loss = q.price * (1.0 - stop_risk)
    target_low = q.price * (1.0 + max(0.0, med))
    target_high = q.price * (1.0 + max(avg, p70, 0.0))
    reward_risk = safe_div(max(avg, p70, 0.0), stop_risk)
    stats = industry_stats.get(q.industry, {})

    reject: list[str] = []
    if len(selected) < 30:
        reject.append("sample_lt_30")
    if safe_div(len(wins), len(returns)) < 0.55:
        reject.append("win_rate_lt_55")
    if avg <= 0:
        reject.append("avg_return_not_positive")
    if pf < 1.2:
        reject.append("profit_factor_lt_1_2")
    if reward_risk < 1.0:
        reject.append("stop_risk_gt_expected_reward")
    if current_close_pos < 0.50:
        reject.append("weak_tail_position")
    if upper_shadow > 0.55 and q.price < q.open:
        reject.append("tail_selloff_proxy")
    if is_near_one_price_limit(q):
        reject.append("one_price_or_near_limit_up")

    sample_max_drawdown = max_drawdown(returns)
    worst_hold_drawdown = min(drawdowns) if drawdowns else 0.0
    score = candidate_quality_score(
        win_rate=safe_div(len(wins), len(returns)),
        avg_return=avg,
        median_return=med,
        profit_factor=pf,
        reward_risk=reward_risk,
        worst_return=worst,
        worst_hold_drawdown=worst_hold_drawdown,
        sample_max_drawdown=sample_max_drawdown,
        close_pos=current_close_pos,
        amount=q.amount,
        industry_avg_pct=stats.get("avg_pct", 0.0),
        industry_adv_ratio=stats.get("adv_ratio", 0.0),
        ret5=current_features.get("ret5", 0.0),
        dist_ma20=current_features.get("dist_ma20", 0.0),
        vol_ratio_log=current_features.get("vol_ratio_log", 0.0),
        main_net_ratio=safe_div(q.main_net, max(q.amount, 1.0)),
    )

    return {
        "secucode": q.secucode,
        "name": q.name,
        "industry": q.industry,
        "quote_time": q.timestamp,
        "latest_date": latest_date,
        "price": q.price,
        "pct": q.pct,
        "amount": q.amount,
        "turnover": q.turnover,
        "volume_ratio": q.volume_ratio,
        "main_net": q.main_net,
        "industry_avg_pct": stats.get("avg_pct", 0.0),
        "industry_adv_ratio": stats.get("adv_ratio", 0.0),
        "industry_amount": stats.get("amount", 0.0),
        "close_pos": current_close_pos,
        "upper_shadow": upper_shadow,
        "samples": len(selected),
        "win_rate": safe_div(len(wins), len(returns)),
        "avg_return": avg,
        "median_return": med,
        "profit_factor": pf,
        "max_drawdown": sample_max_drawdown,
        "worst_return": worst,
        "worst_sample_date": bars[worst_idx].date if worst_idx >= 0 else "",
        "worst_hold_drawdown": worst_hold_drawdown,
        "stop_loss": stop_loss,
        "stop_risk": stop_risk,
        "target_low": target_low,
        "target_high": target_high,
        "reward_risk": reward_risk,
        "buy_low": q.price * 0.997,
        "buy_high": q.price * 1.003,
        "formal": not reject,
        "reject_reason": ";".join(reject),
        "score": score,
    }


def row_float(row: dict[str, Any], key: str, default: float = 0.0) -> float:
    return as_float(row.get(key), default)


def append_reject_reason(row: dict[str, Any], reason: str) -> None:
    existing = [item for item in str(row.get("reject_reason") or "").split(";") if item]
    if reason not in existing:
        existing.append(reason)
    row["reject_reason"] = ";".join(existing)
    row["formal"] = False


def classify_risk_tier(row: dict[str, Any]) -> str:
    if not bool(row.get("formal")):
        return "观察"
    reward_risk = row_float(row, "reward_risk")
    worst_return = row_float(row, "worst_return")
    worst_hold_drawdown = row_float(row, "worst_hold_drawdown")
    sample_drawdown = row_float(row, "max_drawdown")
    close_pos = row_float(row, "close_pos")
    if (
        reward_risk >= 1.2
        and worst_return >= -0.12
        and worst_hold_drawdown >= -0.15
        and sample_drawdown >= -0.35
        and close_pos >= 0.55
    ):
        return "核心"
    if reward_risk >= 0.9 and worst_return >= -0.22 and sample_drawdown >= -0.45:
        return "进取"
    return "观察"


def evaluate_strategy_switch(
    meta: dict[str, Any],
    rows: list[dict[str, Any]],
    recent: dict[str, float] | None = None,
) -> dict[str, Any]:
    top_rows = rows[:3]
    positive_indices = sum(1 for key in ("sh_pct", "sz_pct", "cy_pct") if row_float(meta, key) > 0)
    adv_ratio = row_float(meta, "adv_ratio")
    market_red = adv_ratio < 0.45 or positive_indices <= 1
    market_green = adv_ratio >= 0.50 and positive_indices >= 2

    tiers = [classify_risk_tier(row) for row in top_rows]
    core_count = tiers.count("核心")
    aggressive_count = tiers.count("进取")
    watch_count = tiers.count("观察")
    left_tail_count = sum(
        1
        for row in top_rows
        if row_float(row, "worst_hold_drawdown") < -0.18 or row_float(row, "worst_return") < -0.18
    )
    avg_worst_return = mean([row_float(row, "worst_return") for row in top_rows])
    avg_worst_hold_drawdown = mean([row_float(row, "worst_hold_drawdown") for row in top_rows])

    reasons: list[str] = []
    def add_reason(reason: str) -> None:
        if reason not in reasons:
            reasons.append(reason)

    if market_red:
        add_reason("market_breadth_or_index_weak")
    elif not market_green:
        add_reason("market_not_green")
    if not top_rows or watch_count == len(top_rows):
        add_reason("top3_all_watch")
    if core_count == 0 and aggressive_count > 0:
        add_reason("no_core_only_aggressive")
    if left_tail_count >= 2:
        add_reason("top3_left_tail_cluster")

    no_core_left_tail_warning = (
        core_count == 0
        and top_rows
        and (
            left_tail_count >= 2
            or avg_worst_return < -0.14
            or avg_worst_hold_drawdown < -0.16
        )
    )
    no_core_watch_heavy_warning = core_count == 0 and watch_count >= 2 and bool(top_rows)
    if no_core_left_tail_warning:
        add_reason("no_core_left_tail_warning")
    if no_core_watch_heavy_warning:
        add_reason("no_core_watch_heavy_warning")

    short_recent_weak = False
    confirmed_loss_regime = False
    benchmark_gate_red = False
    benchmark_gate_evaluated = False
    if recent:
        if row_float(recent, "avg_return") <= 0:
            short_recent_weak = True
            add_reason("recent_avg_return_not_positive")
        if row_float(recent, "win_rate") < 0.50:
            short_recent_weak = True
            add_reason("recent_win_rate_lt_50")
        if row_float(recent, "worst_return") < -0.12:
            short_recent_weak = True
            add_reason("recent_worst_return_lt_minus_12")
        if "excess_return" in recent and row_float(recent, "excess_return") < 0:
            short_recent_weak = True
            add_reason("recent_underperforms_index")
        if row_float(recent, "consecutive_loss_days") >= 3:
            short_recent_weak = True
            add_reason("recent_consecutive_loss_days_gte_3")
        if short_recent_weak:
            add_reason("recent_loss_regime")

        medium_keys = {"medium_avg_return", "medium_win_rate", "medium_excess_return"}
        has_medium = any(key in recent for key in medium_keys)
        if has_medium:
            medium_avg = row_float(recent, "medium_avg_return")
            medium_win = row_float(recent, "medium_win_rate")
            medium_excess = row_float(recent, "medium_excess_return")
            medium_consecutive_loss = row_float(recent, "medium_consecutive_loss_days")
            medium_healthy = medium_avg > 0 and medium_win >= 0.55 and medium_excess >= 0
            medium_bad = (
                (medium_avg <= 0 and medium_excess < 0)
                or (medium_win < 0.45 and medium_excess < 0)
                or (medium_consecutive_loss >= 5 and medium_avg <= 0 and medium_excess < 0)
            )
            confirmed_loss_regime = short_recent_weak and medium_bad and not medium_healthy
        else:
            confirmed_loss_regime = short_recent_weak
        if confirmed_loss_regime:
            add_reason("confirmed_loss_regime")

        medium_sample_days = row_float(recent, "medium_sample_days")
        has_optimized_benchmark_metrics = {
            "medium_excess_best_return",
            "medium_max_drawdown",
        }.issubset(recent.keys())
        if medium_sample_days >= BENCHMARK_GATE_MIN_SAMPLES and has_optimized_benchmark_metrics:
            benchmark_gate_evaluated = True
            medium_avg = row_float(recent, "medium_avg_return")
            medium_win = row_float(recent, "medium_win_rate")
            medium_excess_best = row_float(recent, "medium_excess_best_return")
            medium_max_dd = row_float(recent, "medium_max_drawdown")
            benchmark_competitive = (
                medium_avg >= BENCHMARK_GATE_MIN_AVG_RETURN
                and medium_win >= BENCHMARK_GATE_MIN_WIN_RATE
                and medium_excess_best >= BENCHMARK_GATE_MIN_EXCESS_BEST_RETURN
                and medium_max_dd >= BENCHMARK_GATE_MIN_MAX_DRAWDOWN
            )
            if not benchmark_competitive:
                benchmark_gate_red = True
                add_reason("benchmark_gate_underperforming")

    candidate_warning = no_core_left_tail_warning or no_core_watch_heavy_warning
    if confirmed_loss_regime and no_core_left_tail_warning:
        add_reason("confirmed_loss_regime_with_left_tail")
    if market_red or confirmed_loss_regime or benchmark_gate_red or not top_rows or watch_count == len(top_rows):
        state = "红色"
    elif market_green and core_count > 0 and left_tail_count < 2 and not reasons:
        state = "绿色"
    elif market_green and core_count > 0 and all(reason == "top3_left_tail_cluster" for reason in reasons):
        state = "黄色"
    elif market_green and core_count > 0 and not any(reason.startswith("recent_") for reason in reasons):
        state = "绿色"
    elif candidate_warning:
        state = "黄色"
    else:
        state = "黄色"

    return {
        "state": state,
        "reasons": reasons,
        "core_count": core_count,
        "aggressive_count": aggressive_count,
        "watch_count": watch_count,
        "left_tail_count": left_tail_count,
        "avg_worst_return": avg_worst_return,
        "avg_worst_hold_drawdown": avg_worst_hold_drawdown,
        "confirmed_loss_regime": confirmed_loss_regime,
        "benchmark_gate_red": benchmark_gate_red,
        "benchmark_gate_evaluated": benchmark_gate_evaluated,
        "benchmark_gate_requires": {
            "sample_window": BENCHMARK_GATE_SAMPLE_DAYS,
            "min_samples": BENCHMARK_GATE_MIN_SAMPLES,
            "min_avg_return": BENCHMARK_GATE_MIN_AVG_RETURN,
            "min_win_rate": BENCHMARK_GATE_MIN_WIN_RATE,
            "min_excess_best_return": BENCHMARK_GATE_MIN_EXCESS_BEST_RETURN,
            "min_max_drawdown": BENCHMARK_GATE_MIN_MAX_DRAWDOWN,
        },
    }


def apply_strategy_switch(rows: list[dict[str, Any]], decision: dict[str, Any]) -> list[dict[str, Any]]:
    state = str(decision.get("state") or "黄色")
    for row in rows:
        risk_tier = classify_risk_tier(row)
        row["risk_tier"] = risk_tier
        if state == "红色":
            row["action_tier"] = "观察"
            append_reject_reason(row, "strategy_switch_red")
            continue
        if risk_tier == "核心":
            row["action_tier"] = "正式核心"
            row["formal"] = True
        elif risk_tier == "进取":
            row["action_tier"] = "进取研究"
            append_reject_reason(row, "strategy_switch_yellow" if state == "黄色" else "aggressive_research_only")
        else:
            row["action_tier"] = "观察"
            row["formal"] = False
    return rows


def action_priority(row: dict[str, Any]) -> int:
    return {"正式核心": 3, "进取研究": 2, "观察": 1}.get(str(row.get("action_tier") or ""), 0)


def load_recent_metrics(path: str | None) -> dict[str, float] | None:
    if not path:
        return None
    metrics_path = Path(path)
    if not metrics_path.exists():
        return None
    try:
        raw = json.loads(metrics_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None
    metrics = {
        "avg_return": row_float(raw, "avg_return"),
        "win_rate": row_float(raw, "win_rate"),
        "worst_return": row_float(raw, "worst_return"),
        "excess_return": row_float(raw, "excess_return"),
        "consecutive_loss_days": row_float(raw, "consecutive_loss_days"),
        "medium_sample_days": row_float(raw, "medium_sample_days"),
        "medium_avg_return": row_float(raw, "medium_avg_return"),
        "medium_win_rate": row_float(raw, "medium_win_rate"),
        "medium_excess_return": row_float(raw, "medium_excess_return"),
        "medium_consecutive_loss_days": row_float(raw, "medium_consecutive_loss_days"),
    }
    if "medium_excess_best_return" in raw:
        metrics["medium_excess_best_return"] = row_float(raw, "medium_excess_best_return")
    if "medium_max_drawdown" in raw:
        metrics["medium_max_drawdown"] = row_float(raw, "medium_max_drawdown")
    return metrics


def refresh_row_with_quote(row: dict[str, Any], quote: Quote) -> list[str]:
    old_price = row_float(row, "price")
    old_target_low = row_float(row, "target_low")
    old_target_high = row_float(row, "target_high")
    target_low_return = max(0.0, safe_div(old_target_low, old_price, 1.0) - 1.0) if old_price > 0 else 0.0
    target_high_return = max(0.0, safe_div(old_target_high, old_price, 1.0) - 1.0) if old_price > 0 else 0.0

    day_range = max(quote.high - quote.low, 1e-9)
    close_pos = safe_div(quote.price - quote.low, day_range, 0.5)
    upper_shadow = safe_div(quote.high - quote.price, day_range, 0.0)
    stop_risk = row_float(row, "stop_risk")

    row.update({
        "quote_time": quote.timestamp or row.get("quote_time", ""),
        "price": quote.price,
        "pct": quote.pct,
        "amount": quote.amount,
        "turnover": quote.turnover,
        "volume_ratio": quote.volume_ratio,
        "main_net": quote.main_net,
        "close_pos": close_pos,
        "upper_shadow": upper_shadow,
        "stop_loss": quote.price * (1.0 - stop_risk),
        "target_low": quote.price * (1.0 + target_low_return),
        "target_high": quote.price * (1.0 + target_high_return),
        "buy_low": quote.price * 0.997,
        "buy_high": quote.price * 1.003,
        "rechecked": True,
        "recheck_price": quote.price,
        "recheck_time": quote.timestamp,
    })

    reasons: list[str] = []
    if quote.price <= 0 or quote.prev_close <= 0:
        reasons.append("recheck_invalid_quote")
    if quote.pct <= -0.04:
        reasons.append("recheck_drop_lt_minus_4")
    if old_price > 0 and quote.price / old_price - 1.0 <= -0.02:
        reasons.append("recheck_price_drop_gt_2pct")
    if close_pos < 0.50:
        reasons.append("recheck_weak_tail_position")
    if upper_shadow > 0.55 and quote.price < quote.open:
        reasons.append("recheck_tail_selloff_proxy")
    if is_near_one_price_limit(quote):
        reasons.append("recheck_one_price_or_near_limit_up")
    return reasons


def recheck_top_rows(
    rows: list[dict[str, Any]],
    quote_fetcher: Any = fetch_light_quotes,
    top_n: int = 10,
) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    for row in rows:
        row.setdefault("rechecked", False)
        row.setdefault("recheck_price", 0.0)
        row.setdefault("recheck_time", "")
        row.setdefault("recheck_reject_reason", "")

    top_rows = rows[: max(0, top_n)]
    secucodes = [str(row.get("secucode") or "") for row in top_rows if row.get("secucode")]
    if not secucodes:
        return rows, []

    errors: list[dict[str, str]] = []
    try:
        quotes = quote_fetcher(secucodes)
    except Exception as exc:  # noqa: BLE001 - recheck is a conservative optional guard.
        return rows, [{"secucode": ",".join(secucodes), "name": "top_recheck", "error": str(exc)}]

    for row in top_rows:
        code = str(row.get("secucode") or "")
        quote = quotes.get(code)
        if quote is None:
            row["rechecked"] = False
            row["recheck_reject_reason"] = "recheck_quote_missing"
            append_reject_reason(row, "recheck_quote_missing")
            errors.append({"secucode": code, "name": str(row.get("name") or ""), "error": "recheck quote missing"})
            continue
        reasons = refresh_row_with_quote(row, quote)
        row["recheck_reject_reason"] = ";".join(reasons)
        for reason in reasons:
            append_reject_reason(row, reason)
    return rows, errors


def planned_sell_date(trade_date: str) -> str:
    # June 2026 has no A-share trading holiday in the current 5-session window; weekends excluded.
    day = datetime.strptime(trade_date, "%Y-%m-%d").date()
    sessions = 0
    while sessions < 5:
        day += timedelta(days=1)
        if day.weekday() < 5:
            sessions += 1
    return day.isoformat()


def write_outputs(output_dir: Path, rows: list[dict[str, Any]], errors: list[dict[str, str]], meta: dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0].keys()) if rows else [
        "secucode", "name", "industry", "latest_date", "price", "formal", "reject_reason",
    ]
    with (output_dir / "hold5_candidates.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    with (output_dir / "errors.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["secucode", "name", "error"])
        writer.writeheader()
        writer.writerows(errors)
    core_candidates = [row for row in rows if row.get("action_tier") == "正式核心"][:3]
    aggressive_candidates = [row for row in rows if row.get("action_tier") == "进取研究"][:3]
    watch_candidates = [row for row in rows if row.get("action_tier") == "观察"][:5]
    summary = {
        **meta,
        "formal": core_candidates,
        "aggressive": aggressive_candidates,
        "watch": watch_candidates,
        "errors": len(errors),
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    formal = core_candidates
    aggressive = aggressive_candidates
    watch = watch_candidates
    switch = meta.get("strategy_switch") or {}
    switch_state = str(switch.get("state") or "黄色")
    if switch_state == "红色":
        conclusion = "今日不建议新开仓；亏损规避开关红色，正式核心候选 0 只。"
    elif formal:
        conclusion = f"今日可研究新开仓；正式核心候选 {len(formal)} 只，进取研究候选 {len(aggressive)} 只。"
    elif aggressive:
        conclusion = f"无核心候选；可研究进取候选 {len(aggressive)} 只，不作为正式核心开仓。"
    else:
        conclusion = "今日不建议新开仓；无核心候选，进取候选不足。"
    positive_indices = sum(1 for key in ("sh_pct", "sz_pct", "cy_pct") if meta[key] > 0)
    if positive_indices == 3 and meta["adv_ratio"] >= 0.60:
        market_note = "结论：指数与市场宽度同步走强，成交额充足，但尾盘追高风险较高，仍需严格执行买入区间和止损。"
    elif positive_indices <= 1 or meta["adv_ratio"] < 0.45:
        market_note = "结论：指数或市场宽度偏弱，适合降低仓位和提高触发价纪律。"
    else:
        market_note = "结论：指数与市场宽度存在分化，适合只保留统计优势明确且风控空间足够的候选。"
    lines = [
        "# A股尾盘5交易日持有候选筛选",
        "",
        f"- 生成时间：{meta['generated_at']}",
        f"- 行情日期：{meta['latest_date']}",
        f"- 实时快照时间范围：{meta['quote_time_min']} 至 {meta['quote_time_max']}",
        f"- 候选池：东方财富全A实时快照 {meta['snapshot_count']} 只；硬过滤后 {meta['eligible_count']} 只；按成交额/尾盘位置/行业共振预筛验证 {meta['validated_count']} 只。",
        f"- Top候选轻量复核：复核 {meta.get('recheck_count', 0)} 只；复核剔除/降级 {meta.get('recheck_reject_count', 0)} 只；复核错误 {meta.get('recheck_error_count', 0)} 条。",
        "- 数据限制：使用14:50附近实时快照叠加日线历史验证；未取得逐笔或1分钟尾盘趋势，尾盘承接用当日价格位置做代理。",
        f"- 计划卖出日：{meta['sell_date']}（买入后第5个交易日）",
        "",
        "## 结论",
        conclusion,
        "",
        "## 亏损规避开关",
        f"- 状态：{switch_state}",
        f"- 原因：{'; '.join(switch.get('reasons') or ['无明显拦截原因'])}",
        f"- Top3风险层级：核心 {switch.get('core_count', 0)} 只、进取 {switch.get('aggressive_count', 0)} 只、观察 {switch.get('watch_count', 0)} 只；左尾集中 {switch.get('left_tail_count', 0)} 只。",
        f"- Top3左尾均值：最差5日样本 {switch.get('avg_worst_return', 0.0):.2%}，持有期最深回撤 {switch.get('avg_worst_hold_drawdown', 0.0):.2%}。",
        f"- 大盘竞争力门槛：{'未达标' if switch.get('benchmark_gate_red') else ('已达标' if switch.get('benchmark_gate_evaluated') else '未接入/样本不足')}。",
        f"- 近期策略统计：{meta.get('recent_metrics_note', '未接入')}",
        "",
        "## 市场环境",
        f"- 上证指数 {meta['sh_close']:.2f}（{meta['sh_pct']:.2%}），深证成指 {meta['sz_close']:.2f}（{meta['sz_pct']:.2%}），创业板指 {meta['cy_close']:.2f}（{meta['cy_pct']:.2%}）。",
        f"- 全A快照上涨 {meta['advancers']} 只、下跌 {meta['decliners']} 只，涨跌比 {meta['adv_ratio']:.2%}；样本合计成交额约 {meta['total_amount'] / 1e12:.2f} 万亿元。",
        f"- 板块共振靠前：{meta['top_industries']}",
        f"- {market_note}",
        "",
        "## 正式核心候选",
    ]
    if formal:
        lines.append("| 排名 | 代码 | 名称 | 建议买入区间/触发价 | 计划卖出日 | 止损位 | 5日目标区间 | 5日胜率 | 平均5日收益 | 利润因子 | 最大回撤 | 核心买入理由 | 主要风险 |")
        lines.append("|---:|---|---|---|---|---:|---|---:|---:|---:|---:|---|---|")
        for idx, row in enumerate(formal, 1):
            reason = (
                f"{row['samples']}个近似样本第5交易日退出胜率{row['win_rate']:.2%}、"
                f"均值{row['avg_return']:.2%}、中位数{row['median_return']:.2%}；"
                f"当前收在日内区间{row['close_pos']:.0%}位置，行业上涨占比{row['industry_adv_ratio']:.0%}。"
            )
            risk = (
                f"最差样本{row['worst_sample_date']} {row['worst_return']:.2%}，"
                f"样本持中最深回撤{row['worst_hold_drawdown']:.2%}；分钟级尾盘承接未验证。"
            )
            lines.append(
                f"| {idx} | {row['secucode']} | {row['name']} | "
                f"{row['buy_low']:.2f}-{row['buy_high']:.2f} | {meta['sell_date']} | "
                f"{row['stop_loss']:.2f} | {row['target_low']:.2f}-{row['target_high']:.2f} | "
                f"{row['win_rate']:.2%} | {row['avg_return']:.2%} | {row['profit_factor']:.2f} | "
                f"{row['max_drawdown']:.2%} | {reason} | {risk} |"
            )
    else:
        lines.append("无。没有标的同时满足核心风险层级与亏损规避开关。")

    lines.extend(["", "## 进取研究候选"])
    if aggressive:
        lines.append("| 排名 | 代码 | 名称 | 建议买入区间/触发价 | 计划卖出日 | 止损位 | 5日目标区间 | 5日胜率 | 平均5日收益 | 利润因子 | 最大回撤 | 研究理由 | 风险约束 |")
        lines.append("|---:|---|---|---|---|---:|---|---:|---:|---:|---:|---|---|")
        for idx, row in enumerate(aggressive, 1):
            reason = (
                f"{row['samples']}个近似样本胜率{row['win_rate']:.2%}、"
                f"均值{row['avg_return']:.2%}、PF {row['profit_factor']:.2f}；"
                f"当前日内位置{row['close_pos']:.0%}。"
            )
            risk = (
                f"非核心：最差样本{row['worst_return']:.2%}，"
                f"持中最深{row['worst_hold_drawdown']:.2%}，仅适合小仓位研究。"
            )
            lines.append(
                f"| {idx} | {row['secucode']} | {row['name']} | "
                f"{row['buy_low']:.2f}-{row['buy_high']:.2f} | {meta['sell_date']} | "
                f"{row['stop_loss']:.2f} | {row['target_low']:.2f}-{row['target_high']:.2f} | "
                f"{row['win_rate']:.2%} | {row['avg_return']:.2%} | {row['profit_factor']:.2f} | "
                f"{row['max_drawdown']:.2%} | {reason} | {risk} |"
            )
    else:
        lines.append("无。")

    lines.extend(["", "## 观察名单"])
    if watch:
        lines.append("| 排名 | 代码 | 名称 | 当前状态 | 需补齐条件才可买 | 5日胜率 | 平均5日收益 | 利润因子 | 缺口/风险 |")
        lines.append("|---:|---|---|---|---|---:|---:|---:|---|")
        for idx, row in enumerate(watch, 1):
            need = "修复：" + (row["reject_reason"] or "等待更好买点")
            lines.append(
                f"| {idx} | {row['secucode']} | {row['name']} | WATCH | {need} | "
                f"{row['win_rate']:.2%} | {row['avg_return']:.2%} | {row['profit_factor']:.2f} | "
                f"最差{row['worst_return']:.2%}，持中最深{row['worst_hold_drawdown']:.2%} |"
            )
    else:
        lines.append("无。")
    lines.extend([
        "",
        "## 方法与文件",
        f"- 本轮报告：{output_dir / 'report.md'}",
        f"- 本轮候选CSV：{output_dir / 'hold5_candidates.csv'}",
        f"- 本轮摘要JSON：{output_dir / 'summary.json'}",
        f"- 错误明细：{output_dir / 'errors.csv'}",
        "- 数据源/脚本：东方财富全A实时快照、Top候选轻量实时报价复核与前复权日K；`scripts/stock_strategy/run_hold5_tail_candidates.py`。",
        "- 风险提示：本报告只用于量化研究候选，不构成投资建议；未连接券商、未执行真实交易，需自行决策。",
    ])
    (output_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run A-share late-session hold-5 candidate screen")
    parser.add_argument("--base-dir", default=str(BASE_DIR))
    parser.add_argument("--latest-date", default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument("--beg", default="20240101")
    parser.add_argument("--max-validate", type=int, default=420)
    parser.add_argument("--workers", type=int, default=28)
    parser.add_argument("--analog-count", type=int, default=120)
    parser.add_argument("--recheck-top", type=int, default=10)
    parser.add_argument("--recent-metrics-json", default="")
    args = parser.parse_args()

    base_dir = Path(args.base_dir)
    latest_date = args.latest_date
    latest_compact = latest_date.replace("-", "")
    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")
    output_dir = base_dir / "reports" / "automation_5_14_50" / datetime.now().strftime("%Y%m%d_%H%M%S")

    quotes = fetch_clist()
    fresh_quotes = [q for q in quotes if q.price > 0]
    if not fresh_quotes:
        raise SystemExit("no fresh realtime quotes")

    industry_raw: dict[str, list[Quote]] = defaultdict(list)
    for q in fresh_quotes:
        industry_raw[q.industry].append(q)
    industry_stats: dict[str, dict[str, float]] = {}
    for industry, items in industry_raw.items():
        industry_stats[industry] = {
            "avg_pct": mean([q.pct for q in items]),
            "adv_ratio": safe_div(sum(1 for q in items if q.pct > 0), len(items)),
            "amount": sum(q.amount for q in items),
        }

    def eligible(q: Quote) -> bool:
        name_u = q.name.upper()
        if "ST" in name_u or "退" in q.name:
            return False
        if q.price < 2 or q.amount < 300_000_000 or q.prev_close <= 0:
            return False
        if q.pct <= -0.04 or q.pct >= (0.18 if q.code.startswith(("30", "68")) else 0.085):
            return False
        if is_near_one_price_limit(q):
            return False
        close_pos = safe_div(q.price - q.low, max(q.high - q.low, 1e-9), 0.5)
        if close_pos < 0.45:
            return False
        return True

    eligible_quotes = [q for q in fresh_quotes if eligible(q)]
    eligible_quotes.sort(
        key=lambda q: (
            safe_div(q.price - q.low, max(q.high - q.low, 1e-9), 0.5) * 30
            + min(q.amount / 1e9, 20) * 4
            + q.pct * 120
            + industry_stats.get(q.industry, {}).get("avg_pct", 0.0) * 100
            + safe_div(q.main_net, max(q.amount, 1.0)) * 8
        ),
        reverse=True,
    )
    selected = eligible_quotes[: args.max_validate]

    rows: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {
            executor.submit(analyze_quote, q, industry_stats, latest_date, args.beg, latest_compact, args.analog_count): q
            for q in selected
        }
        for future in as_completed(futures):
            q = futures[future]
            try:
                rows.append(future.result())
            except Exception as exc:  # noqa: BLE001
                errors.append({"secucode": q.secucode, "name": q.name, "error": str(exc)})

    rows.sort(key=lambda r: (r["formal"], r["score"]), reverse=True)
    rows, recheck_errors = recheck_top_rows(rows, fetch_light_quotes, args.recheck_top)
    errors.extend(recheck_errors)
    rows.sort(key=lambda r: (r["formal"], r["score"]), reverse=True)
    top_industries = sorted(industry_stats.items(), key=lambda item: (item[1]["avg_pct"], item[1]["amount"]), reverse=True)[:5]
    top_text = "、".join(f"{name}({stats['avg_pct']:.2%}, {stats['adv_ratio']:.0%}上涨)" for name, stats in top_industries if name)
    try:
        indices = fetch_indices()
    except Exception as exc:  # noqa: BLE001
        print(f"WARN indices failed: {exc}", flush=True)
        indices = {}
    meta = {
        "generated_at": generated_at,
        "latest_date": latest_date,
        "sell_date": planned_sell_date(latest_date),
        "snapshot_count": len(fresh_quotes),
        "eligible_count": len(eligible_quotes),
        "validated_count": len(rows),
        "recheck_count": sum(1 for row in rows if row.get("rechecked")),
        "recheck_reject_count": sum(1 for row in rows if row.get("recheck_reject_reason")),
        "recheck_error_count": len(recheck_errors),
        "quote_time_min": min([q.timestamp for q in fresh_quotes if q.timestamp] or [generated_at]),
        "quote_time_max": max([q.timestamp for q in fresh_quotes if q.timestamp] or [generated_at]),
        "total_amount": sum(q.amount for q in fresh_quotes),
        "advancers": sum(1 for q in fresh_quotes if q.pct > 0),
        "decliners": sum(1 for q in fresh_quotes if q.pct < 0),
        "adv_ratio": safe_div(sum(1 for q in fresh_quotes if q.pct > 0), len(fresh_quotes)),
        "top_industries": top_text,
        "sh_close": indices.get("sh000001", (0.0, 0.0))[0],
        "sh_pct": indices.get("sh000001", (0.0, 0.0))[1],
        "sz_close": indices.get("sz399001", (0.0, 0.0))[0],
        "sz_pct": indices.get("sz399001", (0.0, 0.0))[1],
        "cy_close": indices.get("sz399006", (0.0, 0.0))[0],
        "cy_pct": indices.get("sz399006", (0.0, 0.0))[1],
    }
    recent_metrics = load_recent_metrics(args.recent_metrics_json)
    strategy_switch = evaluate_strategy_switch(meta, rows, recent_metrics)
    rows = apply_strategy_switch(rows, strategy_switch)
    rows.sort(key=lambda r: (action_priority(r), r["score"]), reverse=True)
    meta["strategy_switch"] = strategy_switch
    if recent_metrics is None:
        meta["recent_metrics_note"] = "未接入最近已完成信号滚动统计，仅使用市场/候选/尾盘开关。"
    else:
        optimized_gate_note = ""
        if {"medium_excess_best_return", "medium_max_drawdown"}.issubset(recent_metrics.keys()):
            optimized_gate_note = (
                f"最强指数超额{recent_metrics['medium_excess_best_return']:.2%}、"
                f"中期回撤{recent_metrics['medium_max_drawdown']:.2%}；"
                f"强收益开关要求近{BENCHMARK_GATE_SAMPLE_DAYS}批中至少{BENCHMARK_GATE_MIN_SAMPLES}批、"
                f"均值>={BENCHMARK_GATE_MIN_AVG_RETURN:.2%}、"
                f"胜率>={BENCHMARK_GATE_MIN_WIN_RATE:.2%}、"
                f"相对最强指数超额>={BENCHMARK_GATE_MIN_EXCESS_BEST_RETURN:.2%}、"
                f"回撤>={BENCHMARK_GATE_MIN_MAX_DRAWDOWN:.2%}。"
            )
        else:
            optimized_gate_note = "强收益开关缺少最强指数超额/中期回撤字段，未评估。"
        meta["recent_metrics_note"] = (
            f"均值{recent_metrics['avg_return']:.2%}、胜率{recent_metrics['win_rate']:.2%}、"
            f"最差{recent_metrics['worst_return']:.2%}、超额{recent_metrics['excess_return']:.2%}、"
            f"连续亏损日{recent_metrics['consecutive_loss_days']:.0f}；"
            f"中期样本{recent_metrics['medium_sample_days']:.0f}批、"
            f"中期均值{recent_metrics['medium_avg_return']:.2%}、"
            f"中期胜率{recent_metrics['medium_win_rate']:.2%}、"
            f"中期超额{recent_metrics['medium_excess_return']:.2%}；"
            f"{optimized_gate_note}"
        )
    write_outputs(output_dir, rows, errors, meta)
    print(json.dumps({"output_dir": str(output_dir), "meta": meta, "formal": len([r for r in rows if r["formal"]]), "errors": len(errors)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
