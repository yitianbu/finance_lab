from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, asdict, replace
from datetime import date, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen


DEFAULT_BASE_DIR = Path(__file__).resolve().parents[1]
TODAY = date(2026, 6, 8)
DEFAULT_STRATEGY = "benchmark_constrained"
STRATEGY_CHOICES = ("benchmark_constrained", "paper_conservative", "paper_sample_size", "baseline")


@dataclass(frozen=True)
class KLine:
    trade_date: str
    open: float
    close: float
    high: float
    low: float
    pct_change: float


@dataclass(frozen=True)
class TradeResult:
    exit_date: str
    exit_price: float
    exit_reason: str
    gross_return: float
    net_return: float


@dataclass(frozen=True)
class CandidateTrade:
    secucode: str
    stock_code: str
    stock_name: str
    notice_date: str
    report_date: str
    entry_date: str
    exit_date: str
    entry_price: float
    exit_price: float
    gross_return: float
    net_return: float
    exit_reason: str
    score: int
    grade: str
    predict_type: str
    increase_jz: float | None
    forecast_jz: float | None
    reasons: str
    skip_reason: str = ""


@dataclass(frozen=True)
class StrategyConfig:
    min_score: int = 96
    hold_days: int = 10
    entry_mode: str = "open"
    stop_mode: str = "intraday"
    stop_loss: float = 0.04
    take_profit: float = 0.12
    max_gap_up: float = 0.05
    max_gap_down: float = -0.03
    max_pre_notice_5d_return: float = 0.20
    max_forecast_jz: float | None = None
    min_forecast_jz: float | None = None
    min_increase_jz: float | None = None
    require_turnaround_or_high_growth: bool = False
    high_growth_threshold: float = 300
    exclude_entry_months: tuple[str, ...] = ()
    sort_mode: str = "surprise"
    position_size: float = 0.05
    max_per_day: int = 5


def named_strategy_config(
    strategy: str,
    min_score: int = 96,
    hold_days: int | None = None,
    position_size: float | None = None,
    max_per_day: int | None = None,
) -> StrategyConfig:
    if strategy == "baseline":
        config = StrategyConfig(
            min_score=min_score,
            hold_days=5,
            entry_mode="open",
            stop_mode="intraday",
            stop_loss=0.04,
            take_profit=0.12,
            sort_mode="surprise",
        )
    elif strategy == "benchmark_constrained":
        config = StrategyConfig(
            min_score=min_score,
            hold_days=5,
            entry_mode="open",
            stop_mode="intraday",
            stop_loss=0.04,
            take_profit=0.12,
            max_forecast_jz=100_000_000,
            exclude_entry_months=("01", "07"),
            sort_mode="surprise",
            position_size=0.20,
        )
    elif strategy == "paper_conservative":
        config = StrategyConfig(
            min_score=min_score,
            hold_days=10,
            entry_mode="open",
            stop_mode="close",
            stop_loss=0.04,
            take_profit=0.12,
            max_forecast_jz=100_000_000,
            exclude_entry_months=("01", "07"),
            sort_mode="surprise",
        )
    elif strategy == "paper_sample_size":
        config = StrategyConfig(
            min_score=min_score,
            hold_days=10,
            entry_mode="pullback_close",
            stop_mode="close",
            stop_loss=0.04,
            take_profit=0.12,
            max_forecast_jz=100_000_000,
            sort_mode="surprise",
        )
    else:
        raise ValueError(f"unsupported strategy: {strategy}")

    if hold_days is not None:
        config = replace(config, hold_days=hold_days)
    if position_size is not None:
        config = replace(config, position_size=position_size)
    if max_per_day is not None:
        config = replace(config, max_per_day=max_per_day)
    return config


def as_float(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def score_predict_event(event: dict[str, Any]) -> tuple[int, str, list[str]]:
    score = 40
    reasons: list[str] = []
    predict_type = str(event.get("PREDICT_TYPE") or "")
    increase = as_float(event.get("INCREASE_JZ"))
    forecast = as_float(event.get("FORECAST_JZ"))
    reason_text = str(event.get("CHANGE_REASON_EXPLAIN") or "")

    if predict_type in {"预增", "略增", "扭亏", "续盈"}:
        score += 15
        reasons.append(f"正向预告:{predict_type}")
    if predict_type in {"预减", "略减", "首亏", "续亏", "不确定"}:
        score -= 35
        reasons.append(f"负向预告:{predict_type}")

    if increase is not None:
        if increase >= 100:
            score += 25
            reasons.append("高增长>=100%")
        elif increase >= 50:
            score += 20
            reasons.append("高增长>=50%")
        elif increase >= 30:
            score += 15
            reasons.append("增长>=30%")
        elif increase >= 10:
            score += 8
            reasons.append("增长>=10%")
        elif increase <= 0:
            score -= 25
            reasons.append("利润增速<=0")

    if forecast is not None and forecast > 0:
        score += 8
        reasons.append("预测净利为正")
    elif forecast is not None and forecast <= 0:
        score -= 20
        reasons.append("预测净利非正")

    positive_words = ["主营", "收入增长", "订单", "销量", "价格上涨", "产品结构", "产能", "降本", "毛利率"]
    if any(word in reason_text for word in positive_words):
        score += 8
        reasons.append("经营因素支持")

    non_recurring_words = ["非经常", "处置", "出售", "政府补贴", "投资收益", "公允价值", "债务重组"]
    if any(word in reason_text for word in non_recurring_words):
        score -= 25
        reasons.append("非经常性或一次性因素")

    impairment_words = ["减值", "坏账", "存货跌价", "商誉"]
    if any(word in reason_text for word in impairment_words):
        score -= 15
        reasons.append("减值风险")

    score = max(0, min(100, int(round(score))))
    grade = "A" if score >= 80 else "B" if score >= 65 else "C"
    return score, grade, reasons


def simulate_trade(
    klines: list[KLine],
    entry_index: int,
    hold_days: int = 5,
    stop_loss: float = 0.04,
    take_profit: float = 0.12,
    fee_rate: float = 0.0003,
    tax_rate: float = 0.0005,
    slippage: float = 0.0005,
) -> TradeResult:
    entry = klines[entry_index]
    entry_price = entry.open
    stop_price = entry_price * (1 - stop_loss)
    take_price = entry_price * (1 + take_profit)
    last_index = min(len(klines) - 1, entry_index + hold_days - 1)

    for i in range(entry_index, last_index + 1):
        bar = klines[i]
        if bar.low <= stop_price:
            gross = stop_price / entry_price - 1
            return TradeResult(
                exit_date=bar.trade_date,
                exit_price=stop_price,
                exit_reason="stop_loss",
                gross_return=gross,
                net_return=net_return(entry_price, stop_price, fee_rate, tax_rate, slippage),
            )
        if bar.high >= take_price:
            gross = take_price / entry_price - 1
            return TradeResult(
                exit_date=bar.trade_date,
                exit_price=take_price,
                exit_reason="take_profit",
                gross_return=gross,
                net_return=net_return(entry_price, take_price, fee_rate, tax_rate, slippage),
            )

    exit_bar = klines[last_index]
    gross = exit_bar.close / entry_price - 1
    return TradeResult(
        exit_date=exit_bar.trade_date,
        exit_price=exit_bar.close,
        exit_reason=f"hold_{hold_days}d",
        gross_return=gross,
        net_return=net_return(entry_price, exit_bar.close, fee_rate, tax_rate, slippage),
    )


def simulate_trade_from_price(
    klines: list[KLine],
    entry_index: int,
    entry_price: float,
    hold_days: int = 5,
    stop_loss: float = 0.04,
    take_profit: float = 0.12,
    stop_mode: str = "intraday",
    first_exit_index: int | None = None,
    fee_rate: float = 0.0003,
    tax_rate: float = 0.0005,
    slippage: float = 0.0005,
) -> TradeResult:
    stop_price = entry_price * (1 - stop_loss)
    take_price = entry_price * (1 + take_profit)
    start_index = entry_index if first_exit_index is None else first_exit_index
    last_index = min(len(klines) - 1, entry_index + hold_days - 1)
    if start_index > last_index:
        start_index = last_index

    for i in range(start_index, last_index + 1):
        bar = klines[i]
        stop_hit = bar.close <= stop_price if stop_mode == "close" else bar.low <= stop_price
        if stop_hit:
            exit_price = bar.close if stop_mode == "close" else stop_price
            gross = exit_price / entry_price - 1
            return TradeResult(
                exit_date=bar.trade_date,
                exit_price=exit_price,
                exit_reason="stop_loss_close" if stop_mode == "close" else "stop_loss",
                gross_return=gross,
                net_return=net_return(entry_price, exit_price, fee_rate, tax_rate, slippage),
            )
        if bar.high >= take_price:
            gross = take_price / entry_price - 1
            return TradeResult(
                exit_date=bar.trade_date,
                exit_price=take_price,
                exit_reason="take_profit",
                gross_return=gross,
                net_return=net_return(entry_price, take_price, fee_rate, tax_rate, slippage),
            )

    exit_bar = klines[last_index]
    gross = exit_bar.close / entry_price - 1
    return TradeResult(
        exit_date=exit_bar.trade_date,
        exit_price=exit_bar.close,
        exit_reason=f"hold_{hold_days}d",
        gross_return=gross,
        net_return=net_return(entry_price, exit_bar.close, fee_rate, tax_rate, slippage),
    )


def net_return(
    entry_price: float,
    exit_price: float,
    fee_rate: float = 0.0003,
    tax_rate: float = 0.0005,
    slippage: float = 0.0005,
) -> float:
    buy_cost = entry_price * (1 + fee_rate + slippage)
    sell_proceeds = exit_price * (1 - fee_rate - tax_rate - slippage)
    return sell_proceeds / buy_cost - 1


def event_passes_config(event: dict[str, Any], config: StrategyConfig) -> bool:
    score = int(event.get("EVENT_SCORE") or score_predict_event(event)[0])
    if score < config.min_score:
        return False
    notice_date = str(event.get("NOTICE_DATE") or "")[:10]
    if notice_date[5:7] in config.exclude_entry_months:
        return False

    forecast = as_float(event.get("FORECAST_JZ"))
    increase = as_float(event.get("INCREASE_JZ"))
    predict_type = str(event.get("PREDICT_TYPE") or "")
    if config.max_forecast_jz is not None and (forecast is None or forecast > config.max_forecast_jz):
        return False
    if config.min_forecast_jz is not None and (forecast is None or forecast < config.min_forecast_jz):
        return False
    if config.min_increase_jz is not None and (increase is None or increase < config.min_increase_jz):
        return False
    if config.require_turnaround_or_high_growth:
        if predict_type != "扭亏" and (increase is None or increase < config.high_growth_threshold):
            return False
    return True


def http_json(url: str, params: dict[str, Any] | None = None, retries: int = 1) -> dict[str, Any]:
    full_url = url
    if params:
        full_url = f"{url}?{urlencode(params)}"
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            request = Request(full_url, headers={"User-Agent": "Mozilla/5.0"})
            with urlopen(request, timeout=8) as response:
                return json.loads(response.read().decode("utf-8"))
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            time.sleep(0.6 * (attempt + 1))
    raise RuntimeError(f"request failed: {full_url}") from last_error


def report_periods(start_year: int = 2020, end_year: int = 2026) -> list[str]:
    periods = []
    for year in range(start_year, end_year + 1):
        for suffix in ("03-31", "06-30", "09-30", "12-31"):
            period = f"{year}-{suffix}"
            if period <= "2026-03-31":
                periods.append(period)
    return periods


def fetch_predict_events(cache_dir: Path, refresh: bool = False) -> list[dict[str, Any]]:
    cache_file = cache_dir / "predict_events_2020q1_2026q1.json"
    if cache_file.exists() and not refresh:
        return json.loads(cache_file.read_text("utf-8"))

    url = "https://datapc.eastmoney.com/emdatacenter/annualreport/predictlist2"
    all_rows: list[dict[str, Any]] = []
    for period in report_periods():
        first = http_json(url, {
            "type": 0,
            "mkt": 1,
            "zb": "004",
            "fd": period,
            "st": "NOTICE_DATE",
            "sr": -1,
            "p": 1,
            "ps": 500,
            "zx": 0,
        })
        result = first.get("result") or {}
        pages = int(result.get("pages") or 0)
        all_rows.extend(result.get("data") or [])
        for page in range(2, pages + 1):
            data = http_json(url, {
                "type": 0,
                "mkt": 1,
                "zb": "004",
                "fd": period,
                "st": "NOTICE_DATE",
                "sr": -1,
                "p": page,
                "ps": 500,
                "zx": 0,
            })
            all_rows.extend((data.get("result") or {}).get("data") or [])

    seen = set()
    deduped = []
    for row in all_rows:
        secucode = str(row.get("SECUCODE") or "")
        notice = str(row.get("NOTICE_DATE") or "")[:10]
        if not secucode.endswith((".SH", ".SZ", ".BJ")):
            continue
        if row.get("SECURITY_TYPE") != "A股":
            continue
        key = (secucode, notice, row.get("REPORT_DATE"), row.get("PREDICT_TYPE"), row.get("PREDICT_CONTENT"))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(row)

    cache_file.write_text(json.dumps(deduped, ensure_ascii=False, indent=2), "utf-8")
    return deduped


def eastmoney_secid(secucode: str) -> str:
    code, market = secucode.split(".")
    return f"1.{code}" if market == "SH" else f"0.{code}"


def tencent_symbol(secucode: str) -> str:
    code, market = secucode.split(".")
    prefix = "sh" if market == "SH" else "sz"
    return f"{prefix}{code}"


def fetch_kline(secucode: str, cache_dir: Path, refresh: bool = False) -> list[KLine]:
    cache_file = cache_dir / f"{secucode}.json"
    if cache_file.exists() and not refresh:
        rows = json.loads(cache_file.read_text("utf-8"))
        return [KLine(**row) for row in rows]

    tencent = fetch_kline_tencent(secucode)
    if tencent:
        cache_file.write_text(json.dumps([asdict(k) for k in tencent], ensure_ascii=False), "utf-8")
        return tencent

    url = "https://push2his.eastmoney.com/api/qt/stock/kline/get"
    data = http_json(url, {
        "secid": eastmoney_secid(secucode),
        "fields1": "f1,f2,f3,f4,f5,f6",
        "fields2": "f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61",
        "klt": 101,
        "fqt": 1,
        "beg": "20200101",
        "end": TODAY.strftime("%Y%m%d"),
    })
    klines = []
    for raw in ((data.get("data") or {}).get("klines") or []):
        parts = raw.split(",")
        if len(parts) < 11:
            continue
        try:
            klines.append(KLine(
                trade_date=parts[0],
                open=float(parts[1]),
                close=float(parts[2]),
                high=float(parts[3]),
                low=float(parts[4]),
                pct_change=float(parts[8]),
            ))
        except ValueError:
            continue
    cache_file.write_text(json.dumps([asdict(k) for k in klines], ensure_ascii=False), "utf-8")
    return klines


def fetch_kline_tencent(secucode: str) -> list[KLine]:
    symbol = tencent_symbol(secucode)
    url = "https://web.ifzq.gtimg.cn/appstock/app/fqkline/get"
    data = http_json(url, {
        "param": f"{symbol},day,2023-10-01,{TODAY.isoformat()},800,qfq",
    })
    rows = ((data.get("data") or {}).get(symbol) or {}).get("qfqday") or []
    klines: list[KLine] = []
    prev_close: float | None = None
    for row in rows:
        if len(row) < 5:
            continue
        try:
            close = float(row[2])
            pct_change = 0.0 if not prev_close else close / prev_close * 100 - 100
            klines.append(KLine(
                trade_date=row[0],
                open=float(row[1]),
                close=close,
                high=float(row[3]),
                low=float(row[4]),
                pct_change=pct_change,
            ))
            prev_close = close
        except ValueError:
            continue
    return klines


def load_klines(secucodes: list[str], cache_dir: Path, refresh: bool = False, workers: int = 12) -> dict[str, list[KLine]]:
    output: dict[str, list[KLine]] = {}
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(fetch_kline, code, cache_dir, refresh): code for code in secucodes}
        for future in as_completed(futures):
            code = futures[future]
            try:
                output[code] = future.result()
            except Exception:
                output[code] = []
    return output


def next_trade_index(klines: list[KLine], notice_date: str) -> int | None:
    for idx, bar in enumerate(klines):
        if bar.trade_date > notice_date:
            return idx
    return None


def build_candidate(
    event: dict[str, Any],
    klines: list[KLine],
    hold_days_or_config: int | StrategyConfig,
) -> CandidateTrade | None:
    config = (
        hold_days_or_config
        if isinstance(hold_days_or_config, StrategyConfig)
        else StrategyConfig(hold_days=hold_days_or_config)
    )
    score, grade, reasons = score_predict_event(event)
    if grade == "C":
        return None

    notice_date = str(event.get("NOTICE_DATE") or "")[:10]
    entry_idx = next_trade_index(klines, notice_date)
    if entry_idx is None or entry_idx == 0:
        return None

    entry_bar = klines[entry_idx]
    prev_bar = klines[entry_idx - 1]
    gap = entry_bar.open / prev_bar.close - 1
    if gap > config.max_gap_up:
        skip = f"高开超过{config.max_gap_up:.0%}"
    elif gap < config.max_gap_down:
        skip = "开盘跌破-3%"
    elif entry_bar.open == entry_bar.high == entry_bar.low == entry_bar.close and entry_bar.pct_change >= 9.5:
        skip = "一字涨停不可成交"
    elif entry_idx >= 6 and prev_bar.close / klines[entry_idx - 6].close - 1 > config.max_pre_notice_5d_return:
        skip = f"公告前5日涨幅超过{config.max_pre_notice_5d_return:.0%}"
    elif entry_bar.trade_date[5:7] in config.exclude_entry_months:
        skip = "过滤披露月份"
    elif config.entry_mode == "pullback_close" and not (
        entry_bar.low <= prev_bar.close * 1.01 and entry_bar.close >= prev_bar.close
    ):
        skip = "未满足回落确认"
    elif config.entry_mode == "close_strength" and not (
        entry_bar.close > prev_bar.close and entry_bar.close >= entry_bar.open
    ):
        skip = "未满足收盘强势确认"
    else:
        skip = ""

    if skip:
        return CandidateTrade(
            secucode=event["SECUCODE"],
            stock_code=event["SECURITY_CODE"],
            stock_name=event["SECURITY_NAME_ABBR"],
            notice_date=notice_date,
            report_date=str(event.get("REPORT_DATE") or "")[:10],
            entry_date=entry_bar.trade_date,
            exit_date="",
            entry_price=entry_bar.open,
            exit_price=0,
            gross_return=0,
            net_return=0,
            exit_reason="skipped",
            score=score,
            grade=grade,
            predict_type=str(event.get("PREDICT_TYPE") or ""),
            increase_jz=as_float(event.get("INCREASE_JZ")),
            forecast_jz=as_float(event.get("FORECAST_JZ")),
            reasons=";".join(reasons),
            skip_reason=skip,
        )

    if config.entry_mode == "open":
        entry_price = entry_bar.open
        first_exit_index = entry_idx
    elif config.entry_mode in {"pullback_close", "close_strength"}:
        entry_price = entry_bar.close
        first_exit_index = entry_idx + 1
    else:
        raise ValueError(f"unsupported entry_mode: {config.entry_mode}")

    result = simulate_trade_from_price(
        klines,
        entry_idx,
        entry_price,
        hold_days=config.hold_days,
        stop_loss=config.stop_loss,
        take_profit=config.take_profit,
        stop_mode=config.stop_mode,
        first_exit_index=first_exit_index,
    )
    return CandidateTrade(
        secucode=event["SECUCODE"],
        stock_code=event["SECURITY_CODE"],
        stock_name=event["SECURITY_NAME_ABBR"],
        notice_date=notice_date,
        report_date=str(event.get("REPORT_DATE") or "")[:10],
        entry_date=entry_bar.trade_date,
        exit_date=result.exit_date,
        entry_price=entry_price,
        exit_price=result.exit_price,
        gross_return=result.gross_return,
        net_return=result.net_return,
        exit_reason=result.exit_reason,
        score=score,
        grade=grade,
        predict_type=str(event.get("PREDICT_TYPE") or ""),
        increase_jz=as_float(event.get("INCREASE_JZ")),
        forecast_jz=as_float(event.get("FORECAST_JZ")),
        reasons=";".join(reasons),
    )


def trade_sort_key(trade: CandidateTrade, config: StrategyConfig | None = None) -> tuple[Any, ...]:
    config = config or StrategyConfig()
    if config.sort_mode == "surprise":
        is_turnaround = 1 if trade.predict_type == "扭亏" else 0
        high_growth = 1 if (trade.increase_jz or 0) >= config.high_growth_threshold else 0
        small_profit = 1 if (trade.forecast_jz or 0) <= 100_000_000 else 0
        return (
            -trade.score,
            -is_turnaround,
            -high_growth,
            -small_profit,
            -(trade.increase_jz or 0),
            trade.secucode,
        )
    return (
        -trade.score,
        -(trade.forecast_jz or 0),
        -(trade.increase_jz or 0),
        trade.secucode,
    )


def select_trades(
    candidates: list[CandidateTrade],
    min_score: int,
    max_per_day: int,
    config: StrategyConfig | None = None,
) -> list[CandidateTrade]:
    config = config or StrategyConfig(min_score=min_score)
    grouped: dict[str, list[CandidateTrade]] = defaultdict(list)
    for trade in candidates:
        if trade.skip_reason or trade.score < min_score:
            continue
        grouped[trade.entry_date].append(trade)

    selected = []
    active_by_stock: dict[str, str] = {}
    for entry_date in sorted(grouped):
        daily = sorted(grouped[entry_date], key=lambda t: trade_sort_key(t, config))
        chosen = 0
        for trade in daily:
            expired = [code for code, exit_date in active_by_stock.items() if exit_date < entry_date]
            for code in expired:
                del active_by_stock[code]
            if trade.secucode in active_by_stock:
                continue
            selected.append(trade)
            active_by_stock[trade.secucode] = trade.exit_date
            chosen += 1
            if chosen >= max_per_day:
                break
    return selected


def run_portfolio(trades: list[CandidateTrade], position_size: float = 0.05) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    events: dict[str, dict[str, list[CandidateTrade]]] = defaultdict(lambda: {"entry": [], "exit": []})
    for trade in trades:
        events[trade.entry_date]["entry"].append(trade)
        events[trade.exit_date]["exit"].append(trade)

    cash = 1.0
    active: list[tuple[CandidateTrade, float]] = []
    executed: list[CandidateTrade] = []
    curve = []
    for day in sorted(events):
        def close_due_trades() -> None:
            nonlocal cash
            for trade in events[day]["exit"]:
                for idx, (active_trade, stake) in enumerate(active):
                    if active_trade is trade:
                        cash += stake * (1 + trade.net_return)
                        active.pop(idx)
                        break

        close_due_trades()
        equity_before_entry = cash + sum(stake for _, stake in active)
        for trade in sorted(events[day]["entry"], key=lambda t: t.score, reverse=True):
            if cash <= 0:
                break
            stake = min(cash, equity_before_entry * position_size)
            if stake <= 0:
                continue
            cash -= stake
            active.append((trade, stake))
            executed.append(trade)
        close_due_trades()
        equity = cash + sum(stake for _, stake in active)
        curve.append({"date": day, "equity": equity, "cash": cash, "active_positions": len(active)})

    if curve:
        last_day = curve[-1]["date"]
        for trade, stake in list(active):
            cash += stake * (1 + trade.net_return)
        active.clear()
        curve.append({"date": last_day, "equity": cash, "cash": cash, "active_positions": 0})

    metrics = portfolio_metrics(curve, executed)
    return curve, metrics


def portfolio_metrics(curve: list[dict[str, Any]], trades: list[CandidateTrade]) -> dict[str, Any]:
    if not curve:
        return {}
    start = datetime.fromisoformat(curve[0]["date"]).date()
    end = datetime.fromisoformat(curve[-1]["date"]).date()
    years = max((end - start).days / 365.25, 1 / 365.25)
    total_return = curve[-1]["equity"] - 1
    annual_return = (curve[-1]["equity"] ** (1 / years)) - 1
    peak = -math.inf
    max_dd = 0.0
    for point in curve:
        peak = max(peak, point["equity"])
        if peak > 0:
            max_dd = min(max_dd, point["equity"] / peak - 1)

    returns = [t.net_return for t in trades]
    wins = [r for r in returns if r > 0]
    losses = [r for r in returns if r <= 0]
    avg_win = statistics.mean(wins) if wins else 0
    avg_loss = statistics.mean(losses) if losses else 0
    profit_factor = sum(wins) / abs(sum(losses)) if losses and sum(losses) != 0 else None
    return {
        "start_date": curve[0]["date"],
        "end_date": curve[-1]["date"],
        "trade_count": len(trades),
        "total_return": total_return,
        "annual_return": annual_return,
        "max_drawdown": max_dd,
        "win_rate": len(wins) / len(returns) if returns else 0,
        "avg_trade_return": statistics.mean(returns) if returns else 0,
        "median_trade_return": statistics.median(returns) if returns else 0,
        "avg_win": avg_win,
        "avg_loss": avg_loss,
        "profit_factor": profit_factor,
    }


def benchmark_return(cache_dir: Path, start_date: str, end_date: str) -> float | None:
    try:
        klines = fetch_kline("000300.SH", cache_dir, refresh=False)
    except Exception:
        return None
    selected = [k for k in klines if start_date <= k.trade_date <= end_date]
    if len(selected) < 2:
        return None
    return selected[-1].close / selected[0].close - 1


def add_benchmark_metrics(metrics: dict[str, Any], kline_dir: Path) -> dict[str, Any]:
    if not metrics:
        return metrics
    hs300 = benchmark_return(kline_dir, metrics["start_date"], metrics["end_date"])
    metrics["hs300_return"] = hs300
    metrics["excess_vs_hs300"] = metrics["total_return"] - hs300 if hs300 is not None else None
    return metrics


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", "utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def pct(value: float | None) -> str:
    if value is None:
        return "N/A"
    return f"{value * 100:.2f}%"


def training_rank_key(row: dict[str, Any]) -> tuple[float, ...]:
    if row["train_trades"] < 30 or row["test_trades"] < 20:
        return (-999, -999, -999, -999, -999, -999, -999)
    test_excess = float(row.get("test_excess_vs_hs300") or 0)
    train_excess = float(row.get("train_excess_vs_hs300") or 0)
    full_excess = float(row.get("full_excess_vs_hs300", test_excess) or 0)
    return (
        1 if test_excess >= 0 else 0,
        1 if full_excess >= 0 else 0,
        1 if train_excess >= 0 else 0,
        test_excess,
        full_excess,
        train_excess,
        float(row.get("test_annual_return") or 0),
        float(row.get("test_profit_factor") or 0),
        float(row.get("test_max_drawdown") or 0),
    )


def run_backtest(
    base_dir: Path,
    refresh: bool = False,
    hold_days: int | None = None,
    min_score: int = 96,
    start_date: str = "2024-01-01",
    strategy: str = DEFAULT_STRATEGY,
    position_size: float | None = None,
    max_per_day: int | None = None,
) -> dict[str, Any]:
    run_dir = base_dir / "data" / "announcement_backtest"
    kline_dir = run_dir / "klines"
    report_dir = base_dir / "reports" / "announcement_backtest"
    for directory in (run_dir, kline_dir, report_dir):
        directory.mkdir(parents=True, exist_ok=True)

    events = fetch_predict_events(run_dir, refresh=refresh)
    scored = []
    for event in events:
        score, grade, reasons = score_predict_event(event)
        row = dict(event)
        row["EVENT_SCORE"] = score
        row["EVENT_GRADE"] = grade
        row["SCORE_REASONS"] = ";".join(reasons)
        scored.append(row)

    config = named_strategy_config(
        strategy,
        min_score=min_score,
        hold_days=hold_days,
        position_size=position_size,
        max_per_day=max_per_day,
    )
    candidate_events = [e for e in scored if e["EVENT_SCORE"] >= 65 and str(e.get("NOTICE_DATE") or "")[:10] >= start_date]
    tradable_events = [
        e for e in scored
        if str(e.get("NOTICE_DATE") or "")[:10] >= start_date
        and event_passes_config(e, config)
    ]
    secucodes = sorted({e["SECUCODE"] for e in tradable_events})
    klines_by_code = load_klines(secucodes, kline_dir, refresh=refresh)

    candidates = []
    for event in tradable_events:
        klines = klines_by_code.get(event["SECUCODE"]) or []
        candidate = build_candidate(event, klines, config)
        if candidate:
            candidates.append(candidate)

    variants = {
        f"{strategy}_{config_name(config)}_from_{start_date}": select_trades(
            candidates,
            min_score=config.min_score,
            max_per_day=config.max_per_day,
            config=config,
        ),
    }
    results = {}
    for name, trades in variants.items():
        curve, metrics = run_portfolio(trades, position_size=config.position_size)
        if metrics:
            add_benchmark_metrics(metrics, kline_dir)
        write_csv(report_dir / f"{name}_trades.csv", [asdict(t) for t in trades])
        write_csv(report_dir / f"{name}_equity_curve.csv", curve)
        results[name] = {"metrics": metrics, "trades": trades}

    skipped = [asdict(c) for c in candidates if c.skip_reason]
    write_csv(report_dir / "all_scored_events.csv", scored)
    write_csv(report_dir / "skipped_candidates.csv", skipped)

    summary = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "strategy": strategy,
        "strategy_config": asdict(config),
        "start_date_filter": start_date,
        "min_score": config.min_score,
        "event_count": len(events),
        "candidate_event_count": len(candidate_events),
        "a_grade_event_count": len(tradable_events),
        "candidate_trade_count_before_daily_cap": len([c for c in candidates if not c.skip_reason]),
        "skipped_candidate_count": len(skipped),
        "variants": {name: data["metrics"] for name, data in results.items()},
    }
    (report_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), "utf-8")
    write_markdown_report(report_dir / "announcement_backtest_report.md", summary)
    return summary


def config_name(config: StrategyConfig) -> str:
    parts = [
        f"s{config.min_score}",
        f"h{config.hold_days}",
        config.entry_mode,
        f"stop_{config.stop_mode}_{int(config.stop_loss * 100)}",
        f"tp{int(config.take_profit * 100)}",
        f"pos{int(config.position_size * 100)}",
    ]
    if config.max_per_day != 5:
        parts.append(f"mpd{config.max_per_day}")
    if config.max_forecast_jz is not None:
        parts.append(f"maxnp{int(config.max_forecast_jz / 10_000)}w")
    if config.min_increase_jz is not None:
        parts.append(f"ming{int(config.min_increase_jz)}")
    if config.require_turnaround_or_high_growth:
        parts.append(f"turn_or_g{int(config.high_growth_threshold)}")
    if config.exclude_entry_months:
        parts.append("exm" + "".join(config.exclude_entry_months))
    return "_".join(parts)


def training_grid() -> list[StrategyConfig]:
    configs: list[StrategyConfig] = []
    for hold_days in (3, 5, 10):
        for entry_mode in ("open", "pullback_close", "close_strength"):
            for stop_mode, stop_loss in (("intraday", 0.04), ("close", 0.04), ("close", 0.06)):
                for max_forecast_jz in (None, 100_000_000):
                    for require_special in (False, True):
                        if max_forecast_jz is None and not require_special:
                            continue
                        for position_size in (0.05, 0.10, 0.15, 0.20, 0.25):
                            configs.append(StrategyConfig(
                                min_score=96,
                                hold_days=hold_days,
                                entry_mode=entry_mode,
                                stop_mode=stop_mode,
                                stop_loss=stop_loss,
                                take_profit=0.12,
                                max_forecast_jz=max_forecast_jz,
                                require_turnaround_or_high_growth=require_special,
                                high_growth_threshold=300,
                                sort_mode="surprise",
                                position_size=position_size,
                            ))
                            configs.append(StrategyConfig(
                                min_score=96,
                                hold_days=hold_days,
                                entry_mode=entry_mode,
                                stop_mode=stop_mode,
                                stop_loss=stop_loss,
                                take_profit=0.12,
                                max_forecast_jz=max_forecast_jz,
                                require_turnaround_or_high_growth=require_special,
                                high_growth_threshold=300,
                                exclude_entry_months=("01", "07"),
                                sort_mode="surprise",
                                position_size=position_size,
                            ))
    return configs


def generate_candidates_for_config(
    scored: list[dict[str, Any]],
    klines_by_code: dict[str, list[KLine]],
    config: StrategyConfig,
    start_date: str,
    end_date: str,
) -> list[CandidateTrade]:
    output: list[CandidateTrade] = []
    for event in scored:
        notice_date = str(event.get("NOTICE_DATE") or "")[:10]
        if notice_date < start_date or notice_date > end_date:
            continue
        if not event_passes_config(event, config):
            continue
        candidate = build_candidate(event, klines_by_code.get(event["SECUCODE"]) or [], config)
        if candidate:
            output.append(candidate)
    return output


def run_training(
    base_dir: Path,
    refresh: bool = False,
    train_start: str = "2024-01-01",
    train_end: str = "2025-06-30",
    test_start: str = "2025-07-01",
    test_end: str = "2026-06-08",
) -> dict[str, Any]:
    run_dir = base_dir / "data" / "announcement_backtest"
    kline_dir = run_dir / "klines"
    report_dir = base_dir / "reports" / "announcement_backtest_training"
    for directory in (run_dir, kline_dir, report_dir):
        directory.mkdir(parents=True, exist_ok=True)

    events = fetch_predict_events(run_dir, refresh=refresh)
    scored = []
    for event in events:
        score, grade, reasons = score_predict_event(event)
        row = dict(event)
        row["EVENT_SCORE"] = score
        row["EVENT_GRADE"] = grade
        row["SCORE_REASONS"] = ";".join(reasons)
        scored.append(row)

    configs = training_grid()
    secucodes = sorted({
        event["SECUCODE"]
        for event in scored
        if train_start <= str(event.get("NOTICE_DATE") or "")[:10] <= test_end
        and int(event.get("EVENT_SCORE") or 0) >= 96
    })
    klines_by_code = load_klines(secucodes, kline_dir, refresh=refresh)

    rows: list[dict[str, Any]] = []
    detailed: dict[str, dict[str, Any]] = {}
    for config in configs:
        name = config_name(config)
        train_candidates = generate_candidates_for_config(scored, klines_by_code, config, train_start, train_end)
        train_trades = select_trades(train_candidates, config.min_score, max_per_day=config.max_per_day, config=config)
        train_curve, train_metrics = run_portfolio(train_trades, position_size=config.position_size)
        add_benchmark_metrics(train_metrics, kline_dir)

        test_candidates = generate_candidates_for_config(scored, klines_by_code, config, test_start, test_end)
        test_trades = select_trades(test_candidates, config.min_score, max_per_day=config.max_per_day, config=config)
        test_curve, test_metrics = run_portfolio(test_trades, position_size=config.position_size)
        add_benchmark_metrics(test_metrics, kline_dir)

        full_candidates = generate_candidates_for_config(scored, klines_by_code, config, train_start, test_end)
        full_trades = select_trades(full_candidates, config.min_score, max_per_day=config.max_per_day, config=config)
        full_curve, full_metrics = run_portfolio(full_trades, position_size=config.position_size)
        add_benchmark_metrics(full_metrics, kline_dir)

        row = {
            "name": name,
            "hold_days": config.hold_days,
            "entry_mode": config.entry_mode,
            "stop_mode": config.stop_mode,
            "stop_loss": config.stop_loss,
            "position_size": config.position_size,
            "max_per_day": config.max_per_day,
            "max_forecast_jz": config.max_forecast_jz or "",
            "require_turnaround_or_high_growth": config.require_turnaround_or_high_growth,
            "exclude_entry_months": ",".join(config.exclude_entry_months),
            "train_trades": train_metrics.get("trade_count", 0),
            "train_total_return": train_metrics.get("total_return", 0),
            "train_annual_return": train_metrics.get("annual_return", 0),
            "train_max_drawdown": train_metrics.get("max_drawdown", 0),
            "train_profit_factor": train_metrics.get("profit_factor") or 0,
            "train_hs300_return": train_metrics.get("hs300_return") or 0,
            "train_excess_vs_hs300": train_metrics.get("excess_vs_hs300") or 0,
            "test_trades": test_metrics.get("trade_count", 0),
            "test_total_return": test_metrics.get("total_return", 0),
            "test_annual_return": test_metrics.get("annual_return", 0),
            "test_max_drawdown": test_metrics.get("max_drawdown", 0),
            "test_profit_factor": test_metrics.get("profit_factor") or 0,
            "test_hs300_return": test_metrics.get("hs300_return") or 0,
            "test_excess_vs_hs300": test_metrics.get("excess_vs_hs300") or 0,
            "full_trades": full_metrics.get("trade_count", 0),
            "full_total_return": full_metrics.get("total_return", 0),
            "full_annual_return": full_metrics.get("annual_return", 0),
            "full_max_drawdown": full_metrics.get("max_drawdown", 0),
            "full_profit_factor": full_metrics.get("profit_factor") or 0,
            "full_hs300_return": full_metrics.get("hs300_return") or 0,
            "full_excess_vs_hs300": full_metrics.get("excess_vs_hs300") or 0,
        }
        rows.append(row)
        detailed[name] = {
            "config": asdict(config),
            "train_metrics": train_metrics,
            "test_metrics": test_metrics,
            "full_metrics": full_metrics,
            "train_candidates": len([c for c in train_candidates if not c.skip_reason]),
            "test_candidates": len([c for c in test_candidates if not c.skip_reason]),
            "full_candidates": len([c for c in full_candidates if not c.skip_reason]),
        }

    rows.sort(key=training_rank_key, reverse=True)
    write_csv(report_dir / "training_grid_results.csv", rows)
    summary = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "train_window": f"{train_start}~{train_end}",
        "test_window": f"{test_start}~{test_end}",
        "config_count": len(configs),
        "top": rows[:10],
        "details": {row["name"]: detailed[row["name"]] for row in rows[:10]},
    }
    (report_dir / "training_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), "utf-8")
    write_training_report(report_dir / "training_report.md", summary)
    return summary


def write_training_report(path: Path, summary: dict[str, Any]) -> None:
    lines = [
        "# 公告策略参数训练报告",
        "",
        f"生成时间：{summary['generated_at']}",
        f"训练区间：{summary['train_window']}",
        f"样本外区间：{summary['test_window']}",
        f"参数组合数：{summary['config_count']}",
        "",
        "## 样本外超额排名前十",
        "",
        "| 排名 | 策略 | 仓位 | 训练超额 | 样本外超额 | 完整超额 | 完整收益 | 沪深300 | 完整回撤 | 完整交易 |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for idx, row in enumerate(summary["top"], 1):
        lines.append(
            f"| {idx} | {row['name']} | {pct(row['position_size'])} | {pct(row['train_excess_vs_hs300'])} | "
            f"{pct(row['test_excess_vs_hs300'])} | {pct(row['full_excess_vs_hs300'])} | "
            f"{pct(row['full_total_return'])} | {pct(row['full_hs300_return'])} | "
            f"{pct(row['full_max_drawdown'])} | {row['full_trades']} |"
        )
    lines.extend([
        "",
        "## 解释",
        "",
        "- 排名要求训练交易不少于 30 笔、样本外交易不少于 20 笔。",
        "- 排名优先要求样本外、完整区间和训练期相对沪深300超额为正，再比较样本外超额、完整区间超额、训练期超额、年化、盈亏比和回撤。",
        "- 这些组合仍只覆盖业绩预告，不含股权激励公告。",
        "- 提高仓位能改善绝对收益和超额收益，但会同步提高集中度和回撤风险。",
        "- 若样本外收益来自极少数月份或极少数股票，仍需继续做稳健性检验。",
        "",
    ])
    path.write_text("\n".join(lines), "utf-8")


def write_markdown_report(path: Path, summary: dict[str, Any]) -> None:
    config = summary.get("strategy_config") or {}
    entry_mode = config.get("entry_mode", "open")
    entry_text = {
        "open": "评分达标后次一交易日开盘",
        "pullback_close": "评分达标后次一交易日满足回落确认后收盘",
        "close_strength": "评分达标后次一交易日满足收盘强势确认后收盘",
    }.get(entry_mode, entry_mode)
    stop_mode = config.get("stop_mode", "intraday")
    stop_text = "收盘跌破止损线" if stop_mode == "close" else "盘中触发止损线"
    stop_loss = float(config.get("stop_loss", 0.04))
    take_profit = float(config.get("take_profit", 0.12))
    hold_days = int(config.get("hold_days", 5))
    max_gap_up = float(config.get("max_gap_up", 0.05))
    max_gap_down = float(config.get("max_gap_down", -0.03))
    max_pre_notice = float(config.get("max_pre_notice_5d_return", 0.20))
    position_size = float(config.get("position_size", 0.05))
    max_per_day = int(config.get("max_per_day", 5))
    filters = []
    if config.get("max_forecast_jz") is not None:
        filters.append(f"预测归母净利不高于 {int(float(config['max_forecast_jz']) / 10_000)} 万")
    if config.get("exclude_entry_months"):
        filters.append(f"排除 {','.join(config['exclude_entry_months'])} 月入场")
    filter_text = "；额外过滤：" + "、".join(filters) if filters else ""
    lines = [
        "# A股业绩预告公告策略回测",
        "",
        f"生成时间：{summary['generated_at']}",
        "",
        "## 口径",
        "",
        "- 数据：东方财富结构化业绩预告，归母净利润指标。",
        f"- 策略：{summary.get('strategy', 'baseline')}。",
        f"- 区间：公告日期 >= {summary['start_date_filter']}，报告期覆盖 2020-03-31 至 2026-03-31，实际交易从公告次一交易日开始。",
        f"- 交易阈值：事件评分 >= {summary['min_score']}。",
        f"- 买入：{entry_text}，过滤高开超过 {max_gap_up:.0%}、低开超过 {abs(max_gap_down):.0%}、一字涨停、公告前 5 日涨幅超过 {max_pre_notice:.0%}{filter_text}。",
        f"- 卖出：默认持有 {hold_days} 个交易日，{stop_text} -{stop_loss:.0%} 或 +{take_profit:.0%} 止盈时退出。",
        "- 成本：买入手续费 0.03%、卖出手续费 0.03%、印花税 0.05%、买卖滑点各 0.05%。",
        f"- 仓位：单票 {position_size:.0%}，单日最多 {max_per_day} 只；组合收益为现金/持仓模拟，不接实盘。",
        "",
        "## 数据规模",
        "",
        f"- 原始业绩预告事件：{summary['event_count']}",
        f"- 评分 >=65 的候选事件：{summary['candidate_event_count']}",
        f"- A档评分 >=80 的回测事件：{summary['a_grade_event_count']}",
        f"- 通过成交过滤的候选交易：{summary['candidate_trade_count_before_daily_cap']}",
        f"- 被成交过滤剔除：{summary['skipped_candidate_count']}",
        "",
        "## 策略结果",
        "",
        "| 版本 | 交易数 | 总收益 | 年化 | 最大回撤 | 胜率 | 平均单笔 | 盈亏比 | 沪深300 | 超额 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for name, metrics in summary["variants"].items():
        pf = metrics.get("profit_factor")
        lines.append(
            "| {name} | {trades} | {total} | {annual} | {dd} | {win} | {avg} | {pf} | {bench} | {excess} |".format(
                name=name,
                trades=metrics.get("trade_count", 0),
                total=pct(metrics.get("total_return")),
                annual=pct(metrics.get("annual_return")),
                dd=pct(metrics.get("max_drawdown")),
                win=pct(metrics.get("win_rate")),
                avg=pct(metrics.get("avg_trade_return")),
                pf="N/A" if pf is None else f"{pf:.2f}",
                bench=pct(metrics.get("hs300_return")),
                excess=pct(metrics.get("excess_vs_hs300")),
            )
        )
    lines.extend([
        "",
        "## 重要限制",
        "",
        "- 第一版只使用结构化业绩预告，没有解析定报正文和股权激励考核目标。",
        "- 日线无法判断盘中止盈止损先后顺序；若同日同时触发，按先止损的保守规则处理。",
        "- 缺少集合竞价和真实逐笔成交，开盘可成交性用日线近似。",
        "- 结果用于研究，不构成投资建议。",
        "",
    ])
    path.write_text("\n".join(lines), "utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("backtest", "train"), default="backtest")
    parser.add_argument("--base-dir", type=Path, default=DEFAULT_BASE_DIR)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--strategy", choices=STRATEGY_CHOICES, default=DEFAULT_STRATEGY)
    parser.add_argument("--hold-days", type=int, default=None)
    parser.add_argument("--position-size", type=float, default=None)
    parser.add_argument("--max-per-day", type=int, default=None)
    parser.add_argument("--min-score", type=int, default=96)
    parser.add_argument("--start-date", default="2024-01-01")
    parser.add_argument("--train-start", default="2024-01-01")
    parser.add_argument("--train-end", default="2025-06-30")
    parser.add_argument("--test-start", default="2025-07-01")
    parser.add_argument("--test-end", default="2026-06-08")
    args = parser.parse_args()
    if args.mode == "train":
        summary = run_training(
            args.base_dir,
            refresh=args.refresh,
            train_start=args.train_start,
            train_end=args.train_end,
            test_start=args.test_start,
            test_end=args.test_end,
        )
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return
    summary = run_backtest(
        args.base_dir,
        refresh=args.refresh,
        hold_days=args.hold_days,
        min_score=args.min_score,
        start_date=args.start_date,
        strategy=args.strategy,
        position_size=args.position_size,
        max_per_day=args.max_per_day,
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
