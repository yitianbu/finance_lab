from __future__ import annotations

import argparse
import csv
import json
import math
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen


BASE_DIR = Path(__file__).resolve().parents[2]
REPORT_DIR = BASE_DIR / "reports" / "backtest_10b"
UNIVERSE_CSV = BASE_DIR / "reports" / "announcement_backtest" / "all_scored_events.csv"
TENCENT_KLINE_URL = "https://web.ifzq.gtimg.cn/appstock/app/fqkline/get"


@dataclass(frozen=True)
class SymbolInfo:
    secucode: str
    code: str
    name: str
    industry: str = ""


@dataclass(frozen=True)
class DailyBar:
    trade_date: str
    open: float
    close: float
    high: float
    low: float
    amount: float
    pct_change: float
    turnover: float


@dataclass(frozen=True)
class MarketState:
    trade_date: str
    score: float
    score_avg3: float
    sh_close: float
    cy_close: float
    sh_ma20: float
    cy_ma20: float
    advancers: int
    decliners: int
    unchanged: int
    limit_up: int
    limit_down: int
    adv_ratio: float
    limit_ratio: float
    sh_rsi14: float
    base_vol_ratio: float
    high_distance_threshold: float
    tradable: bool
    pause_reasons: list[str]
    market_grade: str = "weak"


@dataclass(frozen=True)
class Signal:
    secucode: str
    stock_name: str
    industry: str
    tier: str
    signal_date: str
    next_trade_date: str
    sector_strength: float
    amount: float
    amount_prev: float
    amount_delta: float
    amount_growth_pct: float
    ma5_ratio: float
    ma15_ratio: float
    close_position: float
    upper_shadow_ratio: float
    dist60_pct: float
    dist15_low_pct: float
    industry_5d_return: float
    industry_amount_ratio: float
    same_industry_up_count: int
    rank_score: float
    resonance_flags: list[str]


@dataclass(frozen=True)
class Trade:
    secucode: str
    stock_name: str
    industry: str
    tier: str
    signal_date: str
    entry_date: str
    entry_price: float
    exit_date: str
    exit_price: float
    hold_days: int
    net_return: float
    exit_reason: str
    market_score_avg3: float
    amount_growth_pct: float
    sector_strength: float
    skipped_reason: str = ""


@dataclass(frozen=True)
class StrategyVariant:
    name: str
    core_tier: SignalTierConfig
    steady_tier: SignalTierConfig
    core_position_size: float = 0.20
    steady_position_size: float = 0.10
    core_hold_days: int = 25
    steady_hold_days: int = 20


@dataclass(frozen=True)
class SignalTierConfig:
    name: str
    min_amount_delta: float
    min_amount_growth: float
    min_ma5_ratio: float
    min_close_position: float
    max_dist15: float
    require_ma_alignment: bool = False


def as_float(value: Any, default: float = 0.0) -> float:
    try:
        if value in (None, ""):
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def safe_div(num: float, den: float, default: float = 0.0) -> float:
    if abs(den) < 1e-12:
        return default
    return num / den


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def classify_market_grade(score_avg3: float, enhanced_filter_passed: bool) -> str:
    if not enhanced_filter_passed or score_avg3 <= 0:
        return "weak"
    if score_avg3 > 2:
        return "super"
    return "strong"


def should_trade_tier(tier: str, market_grade: str) -> bool:
    if tier == "core":
        return market_grade in {"weak", "strong", "super"}
    return market_grade in {"strong", "super"}


def trailing_drawdown_threshold(peak_profit: float, style: str) -> float:
    if style == "steady":
        if peak_profit < 0.10:
            return 0.10
        if peak_profit <= 0.20:
            return 0.12
        return 0.15
    if peak_profit < 0.10:
        return 0.08
    if peak_profit <= 0.20:
        return 0.10
    return 0.12


def objective_score(summary: dict[str, Any]) -> float:
    return (
        as_float(summary.get("avg_return")) * 100
        + as_float(summary.get("win_rate")) * 10
        + min(int(summary.get("trade_count") or 0), 16)
        + as_float(summary.get("portfolio_cash_end"), 1.0) * 20
        - abs(as_float(summary.get("max_drawdown"))) * 200
    )


def strategy_variants() -> list[StrategyVariant]:
    return [
        StrategyVariant(
            name="core_only",
            core_tier=SignalTierConfig("core", 1_000_000_000, 2.0, 3.0, 0.80, 18.0, False),
            steady_tier=SignalTierConfig("steady", 999_000_000_000, 9.9, 9.9, 0.99, 1.0, True),
            core_position_size=0.20,
            steady_position_size=0.0,
            core_hold_days=25,
            steady_hold_days=20,
        ),
        StrategyVariant(
            name="balanced_steady",
            core_tier=SignalTierConfig("core", 1_000_000_000, 2.0, 3.0, 0.80, 18.0, False),
            steady_tier=SignalTierConfig("steady", 700_000_000, 1.2, 2.0, 0.72, 24.0, True),
            core_position_size=0.18,
            steady_position_size=0.10,
            core_hold_days=25,
            steady_hold_days=20,
        ),
        StrategyVariant(
            name="balanced_more_flow",
            core_tier=SignalTierConfig("core", 900_000_000, 1.8, 2.8, 0.78, 20.0, False),
            steady_tier=SignalTierConfig("steady", 600_000_000, 1.0, 1.8, 0.70, 26.0, True),
            core_position_size=0.16,
            steady_position_size=0.10,
            core_hold_days=25,
            steady_hold_days=22,
        ),
    ]


def normalize_code(code: str) -> str:
    raw = code.strip().upper()
    if "." in raw:
        stock, suffix = raw.split(".", 1)
        return f"{stock}.{suffix[:2]}"
    return f"{raw}.SH" if raw.startswith(("5", "6", "9")) else f"{raw}.SZ"


def request_json(url: str, timeout: int = 20) -> dict[str, Any]:
    request = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://quote.eastmoney.com/",
        },
    )
    with urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_universe() -> list[SymbolInfo]:
    symbols: dict[str, SymbolInfo] = {}
    with UNIVERSE_CSV.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            secucode = normalize_code(str(row.get("SECUCODE") or ""))
            code = secucode.split(".")[0]
            name = str(row.get("SECURITY_NAME_ABBR") or "").strip()
            if len(code) != 6 or not name:
                continue
            if "ST" in name.upper() or "退" in name:
                continue
            if secucode not in symbols:
                symbols[secucode] = SymbolInfo(secucode=secucode, code=code, name=name)
    return list(symbols.values())


def tencent_symbol(secucode: str) -> str:
    code = normalize_code(secucode)
    stock, suffix = code.split(".")
    prefix = "sh" if suffix == "SH" else "sz"
    return f"{prefix}{stock}"


def fetch_bars(secucode: str, beg: str, end: str, timeout: int = 20) -> list[DailyBar]:
    params = {"param": f"{tencent_symbol(secucode)},day,,,{800},qfq"}
    payload = request_json(f"{TENCENT_KLINE_URL}?{urlencode(params)}", timeout=timeout)
    stock_data = ((payload.get("data") or {}).get(tencent_symbol(secucode))) or {}
    klines = stock_data.get("qfqday") or stock_data.get("day") or []
    bars: list[DailyBar] = []
    previous_close = 0.0
    for parts in klines:
        if len(parts) < 6:
            continue
        trade_date = str(parts[0])
        if trade_date < ymd_to_dash(beg) or trade_date > ymd_to_dash(end):
            continue
        open_price = as_float(parts[1])
        close = as_float(parts[2])
        high = as_float(parts[3])
        low = as_float(parts[4])
        volume_hands = as_float(parts[5])
        amount = volume_hands * 100 * ((open_price + close + high + low) / 4)
        pct_change = (close / previous_close - 1.0) * 100 if previous_close > 0 else 0.0
        bars.append(DailyBar(
            trade_date=trade_date,
            open=open_price,
            close=close,
            high=high,
            low=low,
            amount=amount,
            pct_change=pct_change,
            turnover=0.0,
        ))
        previous_close = close
    bars.sort(key=lambda item: item.trade_date)
    return bars


def board_limit_pct(secucode: str) -> float:
    code, suffix = secucode.split(".")
    if suffix == "BJ" or code.startswith("8"):
        return 30.0
    if code.startswith(("300", "301", "688")):
        return 20.0
    return 10.0


def is_limit_up(secucode: str, pct_change: float) -> bool:
    return pct_change >= board_limit_pct(secucode) - 0.35


def is_limit_down(secucode: str, pct_change: float) -> bool:
    return pct_change <= -board_limit_pct(secucode) + 0.35


def rolling_mean(values: list[float], end_idx: int, window: int) -> float:
    if end_idx + 1 < window:
        return 0.0
    start = end_idx + 1 - window
    return sum(values[start:end_idx + 1]) / window


def calc_rsi14(closes: list[float], end_idx: int) -> float:
    if end_idx < 14:
        return 50.0
    gains: list[float] = []
    losses: list[float] = []
    start = end_idx - 14
    for i in range(start + 1, end_idx + 1):
        diff = closes[i] - closes[i - 1]
        gains.append(max(diff, 0.0))
        losses.append(max(-diff, 0.0))
    avg_gain = mean(gains)
    avg_loss = mean(losses)
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def prev_trade_dates(index_bars: list[DailyBar]) -> list[str]:
    return [bar.trade_date for bar in index_bars]


def evaluate_signal_tier(
    bars: list[DailyBar],
    idx: int,
    market: MarketState,
    tier: SignalTierConfig,
) -> dict[str, Any] | None:
    if idx < 60:
        return None
    bar = bars[idx]
    amounts = [item.amount for item in bars]
    highs = [item.high for item in bars]
    lows = [item.low for item in bars]
    closes = [item.close for item in bars]
    prev_amount = amounts[idx - 1]
    if bar.amount <= 1_000_000_000 or bar.pct_change <= 0:
        return None
    amount_delta = bar.amount - prev_amount
    amount_growth = safe_div(amount_delta, prev_amount, -1.0) if prev_amount > 0 else -1.0
    if amount_delta < tier.min_amount_delta:
        return None
    if amount_growth < tier.min_amount_growth:
        return None
    ma5_ratio = safe_div(bar.amount, mean(amounts[idx - 4:idx + 1]), 0.0)
    ma15_ratio = safe_div(bar.amount, mean(amounts[idx - 14:idx + 1]), 0.0)
    if ma5_ratio < tier.min_ma5_ratio or ma15_ratio < market.base_vol_ratio:
        return None
    if bar.close <= bar.open:
        return None
    span = bar.high - bar.low
    if span <= 0:
        return None
    close_position = safe_div(bar.close - bar.low, span, 0.0)
    if close_position < tier.min_close_position:
        return None
    body = abs(bar.close - bar.open)
    if body <= 0:
        return None
    upper_shadow = bar.high - max(bar.open, bar.close)
    upper_shadow_ratio = safe_div(upper_shadow, body, 0.0)
    if upper_shadow_ratio > 1.5:
        return None
    high60 = max(highs[idx - 59:idx + 1])
    low15 = min(lows[idx - 14:idx + 1])
    dist60_pct = (bar.close / high60 - 1.0) * 100 if high60 > 0 else 0.0
    dist15_low_pct = (bar.close / low15 - 1.0) * 100 if low15 > 0 else 0.0
    if not tier.require_ma_alignment and dist60_pct > market.high_distance_threshold:
        return None
    if dist15_low_pct > tier.max_dist15:
        return None
    if tier.require_ma_alignment:
        ma20 = mean(closes[idx - 19:idx + 1])
        ma60 = mean(closes[idx - 59:idx + 1])
        if bar.close < max(ma20, ma60):
            return None
    return {
        "tier": tier.name,
        "amount_delta": amount_delta,
        "amount_growth_pct": amount_growth * 100,
        "ma5_ratio": ma5_ratio,
        "ma15_ratio": ma15_ratio,
        "close_position": close_position,
        "upper_shadow_ratio": upper_shadow_ratio,
        "dist60_pct": dist60_pct,
        "dist15_low_pct": dist15_low_pct,
    }


def build_market_states(
    sh_bars: list[DailyBar],
    sz_bars: list[DailyBar],
    cy_bars: list[DailyBar],
    symbol_bars: dict[str, list[DailyBar]],
) -> dict[str, MarketState]:
    states: dict[str, MarketState] = {}
    sh_dates = [bar.trade_date for bar in sh_bars]
    sh_close = [bar.close for bar in sh_bars]
    cy_close = [bar.close for bar in cy_bars]

    breadth_by_date: dict[str, dict[str, int]] = defaultdict(lambda: {
        "advancers": 0,
        "decliners": 0,
        "unchanged": 0,
        "limit_up": 0,
        "limit_down": 0,
    })
    for secucode, bars in symbol_bars.items():
        for bar in bars:
            bucket = breadth_by_date[bar.trade_date]
            if bar.pct_change > 0:
                bucket["advancers"] += 1
            elif bar.pct_change < 0:
                bucket["decliners"] += 1
            else:
                bucket["unchanged"] += 1
            if is_limit_up(secucode, bar.pct_change):
                bucket["limit_up"] += 1
            if is_limit_down(secucode, bar.pct_change):
                bucket["limit_down"] += 1

    sz_by_date = {bar.trade_date: bar for bar in sz_bars}
    cy_by_date = {bar.trade_date: bar for bar in cy_bars}
    for idx in range(len(sh_bars)):
        bar = sh_bars[idx]
        if bar.trade_date not in sz_by_date or bar.trade_date not in cy_by_date:
            continue
        if idx < 2:
            continue
        scores = []
        for j in range(idx - 2, idx + 1):
            sh = sh_bars[j]
            sz = sz_by_date.get(sh.trade_date)
            cy = cy_by_date.get(sh.trade_date)
            if sz is None or cy is None:
                break
            scores.append(sh.pct_change * 0.6 + cy.pct_change * 0.2 + sz.pct_change * 0.2)
        if len(scores) != 3:
            continue
        bucket = breadth_by_date.get(bar.trade_date) or {}
        advancers = int(bucket.get("advancers") or 0)
        decliners = int(bucket.get("decliners") or 0)
        unchanged = int(bucket.get("unchanged") or 0)
        total = advancers + decliners + unchanged
        limit_up = int(bucket.get("limit_up") or 0)
        limit_down = int(bucket.get("limit_down") or 0)
        adv_ratio = safe_div(advancers, total, 0.0)
        limit_ratio = safe_div(limit_up, max(limit_down, 1), 0.0)
        sh_ma20 = rolling_mean(sh_close, idx, 20)
        cy_ma20 = rolling_mean(cy_close, idx, 20)
        rsi14 = calc_rsi14(sh_close, idx)
        base_vol_ratio = 1.5 if rsi14 > 70 else 1.8
        high_distance_threshold = -3.0 if rsi14 > 70 else -10.0
        pause_reasons: list[str] = []
        score_avg3 = mean(scores)
        if score_avg3 <= 0:
            pause_reasons.append(f"3日平均得分 {score_avg3:.2f}% <= 0")
        if not (bar.close > sh_ma20 or cy_by_date[bar.trade_date].close > cy_ma20):
            pause_reasons.append("上证指数与创业板指均未站上20日均线")
        if not (adv_ratio > 0.5 or limit_ratio > 2.0):
            pause_reasons.append(
                f"上涨家数占比 {adv_ratio * 100:.2f}% <= 50%，且涨停/跌停比 {limit_ratio:.2f} <= 2"
            )
        tradable = not pause_reasons
        market_grade = classify_market_grade(score_avg3, tradable)
        states[bar.trade_date] = MarketState(
            trade_date=bar.trade_date,
            score=scores[-1],
            score_avg3=score_avg3,
            sh_close=bar.close,
            cy_close=cy_by_date[bar.trade_date].close,
            sh_ma20=sh_ma20,
            cy_ma20=cy_ma20,
            advancers=advancers,
            decliners=decliners,
            unchanged=unchanged,
            limit_up=limit_up,
            limit_down=limit_down,
            adv_ratio=adv_ratio,
            limit_ratio=limit_ratio,
            sh_rsi14=rsi14,
            base_vol_ratio=base_vol_ratio,
            high_distance_threshold=high_distance_threshold,
            tradable=tradable,
            pause_reasons=pause_reasons,
            market_grade=market_grade,
        )
    return states


def build_industry_maps(
    trade_dates: list[str],
    symbols: list[SymbolInfo],
    symbol_bars: dict[str, list[DailyBar]],
) -> tuple[dict[str, dict[str, float]], dict[str, dict[str, float]], dict[str, dict[str, int]]]:
    # Offline fallback: industry classification is unavailable from local assets.
    # Return empty maps so callers can apply a documented proxy instead of
    # pretending the resonance filter was fully reproduced.
    return defaultdict(dict), defaultdict(dict), defaultdict(dict)


def build_signals(
    symbols: list[SymbolInfo],
    symbol_bars: dict[str, list[DailyBar]],
    market_states: dict[str, MarketState],
    industry_return_top30: dict[str, dict[str, float]],
    industry_amount_ratio: dict[str, dict[str, float]],
    same_industry_up_count: dict[str, dict[str, int]],
    start: str,
    end: str,
    variant: StrategyVariant,
) -> tuple[dict[str, list[Signal]], dict[str, int]]:
    signals_by_date: dict[str, list[Signal]] = defaultdict(list)
    debug_counts: dict[str, int] = defaultdict(int)
    for symbol in symbols:
        bars = symbol_bars.get(symbol.secucode) or []
        if len(bars) < 80:
            debug_counts["insufficient_bars"] += 1
            continue
        amounts = [bar.amount for bar in bars]
        highs = [bar.high for bar in bars]
        lows = [bar.low for bar in bars]
        for idx in range(60, len(bars) - 1):
            bar = bars[idx]
            trade_date = bar.trade_date
            if trade_date < start or trade_date > end:
                continue
            market = market_states.get(trade_date)
            if market is None or not market.tradable:
                debug_counts["market_blocked"] += 1
                continue
            core_eval = evaluate_signal_tier(bars, idx, market, variant.core_tier)
            steady_eval = evaluate_signal_tier(bars, idx, market, variant.steady_tier)
            chosen_tier: str | None = None
            chosen_eval: dict[str, Any] | None = None
            if core_eval and should_trade_tier("core", market.market_grade):
                chosen_tier = "core"
                chosen_eval = core_eval
            elif steady_eval and should_trade_tier("steady", market.market_grade):
                chosen_tier = "steady"
                chosen_eval = steady_eval
            if chosen_eval is None:
                debug_counts["base_amount_or_pct"] += 1
                continue
            prev_amount = amounts[idx - 1]
            amount_delta = chosen_eval["amount_delta"]
            close_position = chosen_eval["close_position"]
            upper_shadow_ratio = chosen_eval["upper_shadow_ratio"]
            dist60_pct = chosen_eval["dist60_pct"]
            dist15_low_pct = chosen_eval["dist15_low_pct"]
            ma5_ratio = chosen_eval["ma5_ratio"]
            ma15_ratio = chosen_eval["ma15_ratio"]

            resonance_flags: list[str] = []
            ind_top30 = industry_return_top30.get(symbol.industry, {}).get(trade_date, 0.0)
            ind_amt_ratio = industry_amount_ratio.get(symbol.industry, {}).get(trade_date, 0.0)
            ind_up_count = same_industry_up_count.get(symbol.industry, {}).get(trade_date, 0)
            if ind_top30 >= 1.0:
                resonance_flags.append("industry_top30_5d")
            if ind_amt_ratio >= 1.3:
                resonance_flags.append("industry_amount_ratio")
            if ind_up_count >= 3:
                resonance_flags.append("industry_sync_up")
            if not resonance_flags:
                # No industry metadata is available in the local/offline universe.
                # Use a conservative proxy so the backtest remains executable and
                # clearly mark the signal as resonance-unverified.
                resonance_flags.append("resonance_proxy_unverified")
                sector_strength = 0.0
            else:
                sector_strength = ind_top30 * 2 + min(ind_amt_ratio, 3.0) + min(ind_up_count, 10) * 0.1
            if chosen_tier == "steady":
                sector_strength += 0.25
            rank_score = sector_strength * 1000 + safe_div(amount_delta, 100_000_000) * 10 + close_position * 100
            debug_counts["signals"] += 1
            signals_by_date[trade_date].append(Signal(
                secucode=symbol.secucode,
                stock_name=symbol.name,
                industry=symbol.industry,
                tier=chosen_tier or "core",
                signal_date=trade_date,
                next_trade_date=bars[idx + 1].trade_date,
                sector_strength=sector_strength,
                amount=bar.amount,
                amount_prev=prev_amount,
                amount_delta=amount_delta,
                amount_growth_pct=chosen_eval["amount_growth_pct"],
                ma5_ratio=ma5_ratio,
                ma15_ratio=ma15_ratio,
                close_position=close_position,
                upper_shadow_ratio=upper_shadow_ratio,
                dist60_pct=dist60_pct,
                dist15_low_pct=dist15_low_pct,
                industry_5d_return=industry_return_top30.get(symbol.industry, {}).get(trade_date, 0.0),
                industry_amount_ratio=ind_amt_ratio,
                same_industry_up_count=ind_up_count,
                rank_score=rank_score,
                resonance_flags=resonance_flags,
            ))
    for trade_date, items in signals_by_date.items():
        items.sort(key=lambda item: (item.sector_strength, item.amount_growth_pct, item.close_position, item.amount_delta), reverse=True)
    return signals_by_date, dict(debug_counts)


def buyable_entry(signal: Signal, bars: list[DailyBar]) -> tuple[int, float, str]:
    idx = next((i for i, bar in enumerate(bars) if bar.trade_date == signal.signal_date), -1)
    if idx < 0 or idx + 1 >= len(bars):
        return -1, 0.0, "missing_d1"
    d0 = bars[idx]
    d1 = bars[idx + 1]
    gap = safe_div(d1.open, d0.close, 0.0) - 1.0
    if d1.low < d0.low:
        return -1, 0.0, "d1_break_signal_low"
    if gap > 0.05:
        return -1, 0.0, "d1_gap_above_5pct"
    if gap < -0.03:
        return -1, 0.0, "d1_gap_below_minus_3pct"
    if abs(d1.pct_change) >= board_limit_pct(signal.secucode) - 0.35 and d1.open == d1.high == d1.low == d1.close:
        return -1, 0.0, "d1_one_word_limit"
    if 0.02 < gap <= 0.05:
        if d1.low <= d0.close <= d1.high:
            return idx + 1, d0.close, "pullback_to_d0_close"
        return -1, 0.0, "d1_gap_2_5_no_pullback"
    return idx + 1, d1.open, "open_follow"


def simulate_trade(
    signal: Signal,
    bars: list[DailyBar],
    entry_idx: int,
    entry_price: float,
    round_trip_cost: float,
    max_hold_days: int,
) -> Trade:
    d0_idx = next(i for i, bar in enumerate(bars) if bar.trade_date == signal.signal_date)
    signal_low = bars[d0_idx].low
    highest = entry_price
    stagnation_window: list[int] = []
    style = "steady" if signal.tier == "steady" else "core"
    for idx in range(entry_idx + 1, min(len(bars), entry_idx + max_hold_days + 1)):
        bar = bars[idx]
        highest = max(highest, bar.high)
        close_return = safe_div(bar.close, entry_price, 0.0) - 1.0
        peak_profit = safe_div(highest, entry_price, 0.0) - 1.0
        drawdown = safe_div(highest - bar.close, highest, 0.0)
        if idx - entry_idx >= 1 and (bar.pct_change < -5.0 or bar.low < signal_low or close_return <= -0.05):
            return Trade(
                secucode=signal.secucode,
                stock_name=signal.stock_name,
                industry=signal.industry,
                tier=signal.tier,
                signal_date=signal.signal_date,
                entry_date=bars[entry_idx].trade_date,
                entry_price=entry_price,
                exit_date=bar.trade_date,
                exit_price=bar.close,
                hold_days=idx - entry_idx,
                net_return=safe_div(bar.close, entry_price, 0.0) - 1.0 - round_trip_cost,
                exit_reason="stop_loss",
                market_score_avg3=0.0,
                amount_growth_pct=signal.amount_growth_pct,
                sector_strength=signal.sector_strength,
            )
        trail = trailing_drawdown_threshold(peak_profit, style)
        if idx - entry_idx >= 1 and peak_profit > 0 and drawdown >= trail:
            return Trade(
                secucode=signal.secucode,
                stock_name=signal.stock_name,
                industry=signal.industry,
                tier=signal.tier,
                signal_date=signal.signal_date,
                entry_date=bars[entry_idx].trade_date,
                entry_price=entry_price,
                exit_date=bar.trade_date,
                exit_price=bar.close,
                hold_days=idx - entry_idx,
                net_return=safe_div(bar.close, entry_price, 0.0) - 1.0 - round_trip_cost,
                exit_reason="trailing_take_profit",
                market_score_avg3=0.0,
                amount_growth_pct=signal.amount_growth_pct,
                sector_strength=signal.sector_strength,
            )
        if idx > entry_idx:
            prev_bar = bars[idx - 1]
            stagnation = 1 if bar.pct_change < 1.0 and bar.amount > prev_bar.amount else 0
            stagnation_window.append(stagnation)
            if len(stagnation_window) >= 3 and sum(stagnation_window[-3:]) == 3 and idx + 1 < len(bars):
                sell_bar = bars[idx + 1]
                return Trade(
                    secucode=signal.secucode,
                    stock_name=signal.stock_name,
                    industry=signal.industry,
                    tier=signal.tier,
                    signal_date=signal.signal_date,
                    entry_date=bars[entry_idx].trade_date,
                    entry_price=entry_price,
                    exit_date=sell_bar.trade_date,
                    exit_price=sell_bar.open,
                    hold_days=idx + 1 - entry_idx,
                    net_return=safe_div(sell_bar.open, entry_price, 0.0) - 1.0 - round_trip_cost,
                    exit_reason="volume_stagnation",
                    market_score_avg3=0.0,
                    amount_growth_pct=signal.amount_growth_pct,
                    sector_strength=signal.sector_strength,
                )
        time_stop_days = 10 if style == "steady" else 5
        time_stop_loss = -0.01 if style == "steady" else 0.0
        if idx - entry_idx + 1 >= time_stop_days and close_return <= time_stop_loss:
            return Trade(
                secucode=signal.secucode,
                stock_name=signal.stock_name,
                industry=signal.industry,
                tier=signal.tier,
                signal_date=signal.signal_date,
                entry_date=bars[entry_idx].trade_date,
                entry_price=entry_price,
                exit_date=bar.trade_date,
                exit_price=bar.close,
                hold_days=idx - entry_idx,
                net_return=safe_div(bar.close, entry_price, 0.0) - 1.0 - round_trip_cost,
                exit_reason="time_stop",
                market_score_avg3=0.0,
                amount_growth_pct=signal.amount_growth_pct,
                sector_strength=signal.sector_strength,
            )
        if idx - entry_idx + 1 >= max_hold_days:
            return Trade(
                secucode=signal.secucode,
                stock_name=signal.stock_name,
                industry=signal.industry,
                tier=signal.tier,
                signal_date=signal.signal_date,
                entry_date=bars[entry_idx].trade_date,
                entry_price=entry_price,
                exit_date=bar.trade_date,
                exit_price=bar.close,
                hold_days=idx - entry_idx,
                net_return=safe_div(bar.close, entry_price, 0.0) - 1.0 - round_trip_cost,
                exit_reason="max_hold_exit",
                market_score_avg3=0.0,
                amount_growth_pct=signal.amount_growth_pct,
                sector_strength=signal.sector_strength,
            )
    last = bars[min(len(bars) - 1, entry_idx + max_hold_days)]
    return Trade(
        secucode=signal.secucode,
        stock_name=signal.stock_name,
        industry=signal.industry,
        tier=signal.tier,
        signal_date=signal.signal_date,
        entry_date=bars[entry_idx].trade_date,
        entry_price=entry_price,
        exit_date=last.trade_date,
        exit_price=last.close,
        hold_days=min(len(bars) - 1, entry_idx + max_hold_days) - entry_idx,
        net_return=safe_div(last.close, entry_price, 0.0) - 1.0 - round_trip_cost,
        exit_reason="end_of_data",
        market_score_avg3=0.0,
        amount_growth_pct=signal.amount_growth_pct,
        sector_strength=signal.sector_strength,
    )


def run_backtest(
    symbols: list[SymbolInfo],
    symbol_bars: dict[str, list[DailyBar]],
    market_states: dict[str, MarketState],
    signals_by_date: dict[str, list[Signal]],
    variant: StrategyVariant,
    max_new_positions: int,
    round_trip_cost: float,
) -> tuple[list[Trade], dict[str, Any]]:
    trades: list[Trade] = []
    cash = 1.0
    equity = 1.0
    peak_equity = 1.0
    max_drawdown = 0.0
    entries_by_date: dict[str, list[Trade]] = defaultdict(list)
    closed_by_date: dict[str, list[Trade]] = defaultdict(list)
    allocation_by_signal: dict[tuple[str, str], float] = {}

    provisional: list[Trade] = []
    skipped: list[Trade] = []
    for signal_date in sorted(signals_by_date):
        for signal in signals_by_date[signal_date][:max_new_positions]:
            bars = symbol_bars.get(signal.secucode) or []
            entry_idx, entry_price, decision = buyable_entry(signal, bars)
            if entry_idx < 0:
                skipped.append(Trade(
                    secucode=signal.secucode,
                    stock_name=signal.stock_name,
                    industry=signal.industry,
                    tier=signal.tier,
                    signal_date=signal.signal_date,
                    entry_date="",
                    entry_price=0.0,
                    exit_date="",
                    exit_price=0.0,
                    hold_days=0,
                    net_return=0.0,
                    exit_reason="",
                    market_score_avg3=market_states[signal.signal_date].score_avg3,
                    amount_growth_pct=signal.amount_growth_pct,
                    sector_strength=signal.sector_strength,
                    skipped_reason=decision,
                ))
                continue
            max_hold_days = variant.steady_hold_days if signal.tier == "steady" else variant.core_hold_days
            trade = simulate_trade(signal, bars, entry_idx, entry_price, round_trip_cost, max_hold_days)
            trade = Trade(**(asdict(trade) | {"market_score_avg3": market_states[signal.signal_date].score_avg3}))
            provisional.append(trade)
            entries_by_date[trade.entry_date].append(trade)
            closed_by_date[trade.exit_date].append(trade)

    for trade_date in sorted(set(entries_by_date) | set(closed_by_date)):
        for trade in closed_by_date.get(trade_date, []):
            allocation = allocation_by_signal.pop((trade.secucode, trade.entry_date), 0.0)
            cash += allocation * (1.0 + trade.net_return)
            trades.append(trade)
        for trade in entries_by_date.get(trade_date, []):
            position_size = variant.steady_position_size if trade.tier == "steady" else variant.core_position_size
            allocation = min(cash, equity * position_size)
            if allocation <= 0:
                continue
            cash -= allocation
            allocation_by_signal[(trade.secucode, trade.entry_date)] = allocation
        marked = cash + sum(allocation_by_signal.values())
        equity = marked
        peak_equity = max(peak_equity, equity)
        max_drawdown = min(max_drawdown, safe_div(equity, peak_equity, 1.0) - 1.0)

    closed_returns = [trade.net_return for trade in trades]
    summary = {
        "trade_count": len(trades),
        "win_rate": safe_div(sum(1 for ret in closed_returns if ret > 0), len(closed_returns), 0.0),
        "avg_return": mean(closed_returns),
        "median_return": sorted(closed_returns)[len(closed_returns) // 2] if closed_returns else 0.0,
        "best_return": max(closed_returns) if closed_returns else 0.0,
        "worst_return": min(closed_returns) if closed_returns else 0.0,
        "skipped_count": len(skipped),
        "signal_count": sum(len(items) for items in signals_by_date.values()),
        "tradable_dates": sum(1 for state in market_states.values() if state.tradable),
        "market_blocked_dates": sum(1 for state in market_states.values() if not state.tradable),
        "portfolio_cash_end": cash,
        "max_drawdown": max_drawdown,
    }
    return trades, summary | {"skipped": [asdict(item) for item in skipped]}


def write_report(
    output_dir: Path,
    start: str,
    end: str,
    universe_count: int,
    bars_loaded: int,
    market_states: dict[str, MarketState],
    trades: list[Trade],
    summary: dict[str, Any],
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    trades_path = output_dir / "trades.csv"
    with trades_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(asdict(trades[0]).keys()) if trades else list(asdict(Trade("", "", "", "", "", "", 0, "", 0, 0, 0.0, "", 0.0, 0.0, 0.0)).keys()),
        )
        writer.writeheader()
        for trade in trades:
            writer.writerow(asdict(trade))

    market_path = output_dir / "market_states.csv"
    with market_path.open("w", encoding="utf-8", newline="") as handle:
        fieldnames = list(asdict(next(iter(market_states.values()))).keys()) if market_states else []
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for state in market_states.values():
            writer.writerow(asdict(state))

    top_trades = sorted(trades, key=lambda item: item.net_return, reverse=True)[:20]
    worst_trades = sorted(trades, key=lambda item: item.net_return)[:20]
    lines = [
        "# 10亿增量策略三个月全A回测",
        "",
        f"- 回测区间：{start} 到 {end}",
        f"- 全A股票数：{universe_count}",
        f"- 成功加载日线股票数：{bars_loaded}",
        f"- 市场可交易天数：{summary['tradable_dates']}",
        f"- 市场暂停天数：{summary['market_blocked_dates']}",
        f"- 强信号数量：{summary['signal_count']}",
        f"- 实际成交笔数：{summary['trade_count']}",
        f"- D1保护规则跳过：{summary['skipped_count']}",
        f"- 胜率：{summary['win_rate'] * 100:.2f}%",
        f"- 平均单笔收益：{summary['avg_return'] * 100:.2f}%",
        f"- 中位数单笔收益：{summary['median_return'] * 100:.2f}%",
        f"- 最好/最差单笔：{summary['best_return'] * 100:.2f}% / {summary['worst_return'] * 100:.2f}%",
        f"- 组合现金终值（20%仓位近似）：{summary['portfolio_cash_end']:.4f}",
        "",
        "## 说明",
        "- 该回测重建了市场过滤、成交额增量、量比、K线结构、D1保护和卖出规则。",
        "- 近一年减持、业绩预告、处罚/立案等公告类过滤未能离线完整复原，因此本次结果是技术面近似回测，不是完整公告口径实盘复盘。",
        "- 板块共振使用东方财富当前行业分类做历史横截面近似，存在分类漂移误差。",
        "",
        "## Top 20 Trades",
        "",
        "| Code | Name | Signal | Entry | Exit | Return | Reason |",
        "| --- | --- | --- | --- | --- | ---: | --- |",
    ]
    for trade in top_trades:
        lines.append(
            f"| {trade.secucode} | {trade.stock_name} | {trade.signal_date} | {trade.entry_date} | {trade.exit_date} | {trade.net_return * 100:.2f}% | {trade.exit_reason} |"
        )
    lines += [
        "",
        "## Worst 20 Trades",
        "",
        "| Code | Name | Signal | Entry | Exit | Return | Reason |",
        "| --- | --- | --- | --- | --- | ---: | --- |",
    ]
    for trade in worst_trades:
        lines.append(
            f"| {trade.secucode} | {trade.stock_name} | {trade.signal_date} | {trade.entry_date} | {trade.exit_date} | {trade.net_return * 100:.2f}% | {trade.exit_reason} |"
        )
    report_path = output_dir / "report.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")

    summary_path = output_dir / "summary.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Backtest 10B turnover strategy on full A-share universe")
    parser.add_argument("--start", required=True, help="inclusive start date, YYYYMMDD")
    parser.add_argument("--end", required=True, help="inclusive end date, YYYYMMDD")
    parser.add_argument("--lookback", type=int, default=120)
    parser.add_argument("--workers", type=int, default=16)
    parser.add_argument("--max-symbols", type=int, default=0)
    parser.add_argument("--max-new-positions", type=int, default=5)
    parser.add_argument("--position-size", type=float, default=0.20)
    parser.add_argument("--round-trip-cost", type=float, default=0.0013)
    parser.add_argument("--variant", default="balanced_steady")
    parser.add_argument("--sweep", action="store_true")
    return parser.parse_args()


def ymd_to_dash(value: str) -> str:
    return f"{value[:4]}-{value[4:6]}-{value[6:8]}"


def main() -> None:
    args = parse_args()
    start_dash = ymd_to_dash(args.start)
    end_dash = ymd_to_dash(args.end)
    fetch_beg = str(max(int(args.start) - 10000, 20240101))
    fetch_end = str(min(int(args.end) + 10000, 20261231))

    symbols = fetch_universe()
    if args.max_symbols:
        symbols = symbols[:args.max_symbols]
    symbol_bars: dict[str, list[DailyBar]] = {}
    errors: dict[str, str] = {}

    def load_symbol(symbol: SymbolInfo) -> tuple[str, list[DailyBar]]:
        bars = fetch_bars(symbol.secucode, fetch_beg, fetch_end, timeout=25)
        return symbol.secucode, bars

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {executor.submit(load_symbol, symbol): symbol for symbol in symbols}
        for idx, future in enumerate(as_completed(futures), start=1):
            symbol = futures[future]
            try:
                secucode, bars = future.result()
                if bars:
                    symbol_bars[secucode] = bars
            except Exception as exc:
                errors[symbol.secucode] = f"{type(exc).__name__}: {exc}"
            if idx % 200 == 0:
                print(f"progress {idx}/{len(symbols)} loaded={len(symbol_bars)} errors={len(errors)}", flush=True)
                time.sleep(0.2)

    sh_bars = fetch_bars("000001.SH", fetch_beg, fetch_end)
    sz_bars = fetch_bars("399001.SZ", fetch_beg, fetch_end)
    cy_bars = fetch_bars("399006.SZ", fetch_beg, fetch_end)
    market_states = build_market_states(sh_bars, sz_bars, cy_bars, symbol_bars)
    industry_return_top30, industry_amount_ratio, same_industry_up_count = build_industry_maps(
        [bar.trade_date for bar in sh_bars],
        symbols,
        symbol_bars,
    )
    variants = strategy_variants()
    if not args.sweep:
        variants = [next((item for item in variants if item.name == args.variant), variants[1])]

    run_summaries: list[dict[str, Any]] = []
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_output_dir = REPORT_DIR / f"{args.start}_{args.end}_{timestamp}"
    for variant in variants:
        signals_by_date, signal_debug = build_signals(
            symbols,
            symbol_bars,
            market_states,
            industry_return_top30,
            industry_amount_ratio,
            same_industry_up_count,
            start_dash,
            end_dash,
            variant,
        )
        trades, summary = run_backtest(
            symbols,
            symbol_bars,
            market_states,
            signals_by_date,
            variant=variant,
            max_new_positions=args.max_new_positions,
            round_trip_cost=args.round_trip_cost,
        )
        summary["errors"] = errors
        summary["signal_debug"] = signal_debug
        summary["loaded_symbol_count"] = len(symbol_bars)
        summary["requested_symbol_count"] = len(symbols)
        summary["variant"] = variant.name
        summary["objective_score"] = objective_score(summary)
        output_dir = base_output_dir / variant.name if args.sweep else base_output_dir
        write_report(output_dir, start_dash, end_dash, len(symbols), len(symbol_bars), market_states, trades, summary)
        run_summaries.append({
            "variant": variant.name,
            "output_dir": str(output_dir),
            "objective_score": summary["objective_score"],
            "trade_count": summary["trade_count"],
            "win_rate": summary["win_rate"],
            "avg_return": summary["avg_return"],
            "max_drawdown": summary["max_drawdown"],
            "portfolio_cash_end": summary["portfolio_cash_end"],
            "signal_count": summary["signal_count"],
        })

    run_summaries.sort(key=lambda item: item["objective_score"], reverse=True)
    print(json.dumps({
        "output_dir": str(base_output_dir),
        "runs": run_summaries,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
