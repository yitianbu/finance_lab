from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import asdict, dataclass, replace
from datetime import date, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen


DEFAULT_BASE_DIR = Path(__file__).resolve().parents[1]
EASTMONEY_KLINE_URL = "https://push2his.eastmoney.com/api/qt/stock/kline/get"
TENCENT_KLINE_URL = "https://web.ifzq.gtimg.cn/appstock/app/fqkline/get"


@dataclass(frozen=True)
class DailyBar:
    trade_date: str
    open: float
    close: float
    high: float
    low: float
    volume: float
    amount: float
    pct_change: float
    turnover: float


@dataclass(frozen=True)
class PredictionConfig:
    history_window: int = 90
    similar_count: int = 15
    atr_period: int = 14
    target_coverage: float = 0.80
    atr_multiplier_candidates: tuple[float, ...] = (0.75, 1.0, 1.25, 1.5, 1.75)
    min_reward_risk: float = 1.8
    base_position_size: float = 0.20
    round_trip_cost: float = 0.0013
    max_hold_days: int = 5


@dataclass(frozen=True)
class RangePrediction:
    signal_date: str
    next_trade_date: str
    signal_close: float
    predicted_high: float
    predicted_low: float
    band_high: float
    band_low: float
    expected_close_return: float
    atr: float
    atr_pct: float
    score: float
    similar_count: int


@dataclass(frozen=True)
class CalibrationResult:
    multiplier: float
    coverage: float
    avg_width_pct: float
    candidates: list[dict[str, float]]


@dataclass(frozen=True)
class TradePlan:
    action: str
    buy_zone_low: float
    buy_zone_high: float
    stop_loss: float
    take_profit: float
    reward_risk: float
    position_hint: float
    reason: str


@dataclass(frozen=True)
class TradeExecution:
    entered: bool
    entry_price: float
    exit_price: float
    gross_return: float
    net_return: float
    exit_reason: str
    entry_date: str = ""
    exit_date: str = ""
    holding_days: int = 0


def as_float(value: Any, default: float = 0.0) -> float:
    try:
        if value is None or value == "":
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def safe_div(numerator: float, denominator: float, default: float = 0.0) -> float:
    if abs(denominator) < 1e-12:
        return default
    return numerator / denominator


def normalize_code(raw_code: str) -> str:
    value = raw_code.strip().upper()
    if not value:
        raise ValueError("stock code is required")

    if "." in value:
        code, suffix = value.split(".", 1)
    elif value.startswith(("SH", "SZ")):
        suffix, code = value[:2], value[2:]
    else:
        code = value
        suffix = "SH" if value.startswith(("5", "6", "9")) else "SZ"

    code = "".join(ch for ch in code if ch.isdigit())
    suffix = suffix[:2]
    if len(code) != 6:
        raise ValueError(f"invalid stock code: {raw_code}")
    if suffix not in {"SH", "SZ"}:
        suffix = "SH" if code.startswith(("5", "6", "9")) else "SZ"
    return f"{code}.{suffix}"


def eastmoney_secid(raw_code: str) -> str:
    code = normalize_code(raw_code)
    stock_code, suffix = code.split(".")
    market = "1" if suffix == "SH" else "0"
    return f"{market}.{stock_code}"


def eastmoney_url(raw_code: str, beg: str, end: str) -> str:
    params = {
        "secid": eastmoney_secid(raw_code),
        "fields1": "f1,f2,f3,f4,f5,f6",
        "fields2": "f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61",
        "klt": "101",
        "fqt": "1",
        "beg": beg,
        "end": end,
    }
    return f"{EASTMONEY_KLINE_URL}?{urlencode(params)}"


def tencent_symbol(raw_code: str) -> str:
    code = normalize_code(raw_code)
    stock_code, suffix = code.split(".")
    prefix = "sh" if suffix == "SH" else "sz"
    return f"{prefix}{stock_code}"


def tencent_url(raw_code: str, count: int = 500) -> str:
    params = {"param": f"{tencent_symbol(raw_code)},day,,,{count},qfq"}
    return f"{TENCENT_KLINE_URL}?{urlencode(params)}"


def fetch_eastmoney_payload(raw_code: str, beg: str, end: str, timeout: int = 20) -> dict[str, Any]:
    request = Request(
        eastmoney_url(raw_code, beg, end),
        headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://quote.eastmoney.com/",
        },
    )
    with urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_tencent_payload(raw_code: str, count: int = 500, timeout: int = 20) -> dict[str, Any]:
    request = Request(
        tencent_url(raw_code, count),
        headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://gu.qq.com/",
        },
    )
    with urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def parse_eastmoney_payload(payload: dict[str, Any]) -> list[DailyBar]:
    data = payload.get("data") or {}
    klines = data.get("klines") or []
    bars: list[DailyBar] = []
    for line in klines:
        parts = str(line).split(",")
        if len(parts) < 11:
            continue
        bars.append(DailyBar(
            trade_date=parts[0],
            open=as_float(parts[1]),
            close=as_float(parts[2]),
            high=as_float(parts[3]),
            low=as_float(parts[4]),
            volume=as_float(parts[5]),
            amount=as_float(parts[6]),
            pct_change=as_float(parts[8]),
            turnover=as_float(parts[10]),
        ))
    bars.sort(key=lambda item: item.trade_date)
    return bars


def parse_tencent_payload(raw_code: str, payload: dict[str, Any]) -> list[DailyBar]:
    data = payload.get("data") or {}
    symbol = tencent_symbol(raw_code)
    stock_data = data.get(symbol) or {}
    rows = stock_data.get("qfqday") or stock_data.get("day") or []
    bars: list[DailyBar] = []
    previous_close = 0.0
    for row in rows:
        if len(row) < 6:
            continue
        trade_date = str(row[0])
        open_price = as_float(row[1])
        close = as_float(row[2])
        high = as_float(row[3])
        low = as_float(row[4])
        volume = as_float(row[5])
        pct_change = 0.0
        if previous_close > 0:
            pct_change = (close / previous_close - 1.0) * 100
        bars.append(DailyBar(
            trade_date=trade_date,
            open=open_price,
            close=close,
            high=high,
            low=low,
            volume=volume,
            amount=0.0,
            pct_change=pct_change,
            turnover=0.0,
        ))
        previous_close = close
    bars.sort(key=lambda item: item.trade_date)
    return bars


def parse_daily_payload(raw_code: str, payload: dict[str, Any]) -> list[DailyBar]:
    data = payload.get("data") or {}
    if isinstance(data, dict) and data.get("klines"):
        return parse_eastmoney_payload(payload)
    bars = parse_tencent_payload(raw_code, payload)
    if bars:
        return bars
    return parse_eastmoney_payload(payload)


def load_bars_from_json(path: Path, raw_code: str = "") -> list[DailyBar]:
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return parse_daily_payload(raw_code or "000001.SZ", payload)


def load_daily_bars(
    raw_code: str,
    beg: str,
    end: str,
    input_json: Path | None = None,
    data_source: str = "auto",
) -> list[DailyBar]:
    if input_json is not None:
        return load_bars_from_json(input_json, raw_code)

    if data_source not in {"auto", "eastmoney", "tencent"}:
        raise ValueError(f"unsupported data source: {data_source}")
    if data_source in {"auto", "eastmoney"}:
        try:
            bars = parse_eastmoney_payload(fetch_eastmoney_payload(raw_code, beg, end))
            if bars or data_source == "eastmoney":
                return bars
        except Exception:
            if data_source == "eastmoney":
                raise
    return parse_tencent_payload(raw_code, fetch_tencent_payload(raw_code))


def true_range(bars: list[DailyBar], idx: int) -> float:
    bar = bars[idx]
    if idx <= 0:
        return max(0.0, bar.high - bar.low)
    prev_close = bars[idx - 1].close
    return max(bar.high - bar.low, abs(bar.high - prev_close), abs(bar.low - prev_close))


def atr_at(bars: list[DailyBar], idx: int, period: int = 14) -> float:
    if idx < 0:
        return 0.0
    start = max(0, idx - period + 1)
    return mean([true_range(bars, item_idx) for item_idx in range(start, idx + 1)])


def close_return(bars: list[DailyBar], start_idx: int, end_idx: int) -> float:
    if start_idx < 0 or end_idx < 0 or start_idx >= len(bars) or end_idx >= len(bars):
        return 0.0
    return safe_div(bars[end_idx].close, bars[start_idx].close, 1.0) - 1.0


def feature_vector(bars: list[DailyBar], idx: int, config: PredictionConfig) -> dict[str, float]:
    bar = bars[idx]
    prev = bars[idx - 1] if idx > 0 else bar
    ma20_start = max(0, idx - 19)
    volume_start = max(0, idx - 19)
    ma20 = mean([item.close for item in bars[ma20_start: idx + 1]]) or bar.close
    avg_volume = mean([item.volume for item in bars[volume_start: idx + 1]]) or bar.volume
    day_range = max(bar.high - bar.low, 1e-9)
    atr = atr_at(bars, idx, config.atr_period)
    prev_close = prev.close or bar.close
    volume_ratio = safe_div(bar.volume, avg_volume, 1.0)
    return {
        "pct_change": bar.pct_change / 100.0,
        "prev_pct": prev.pct_change / 100.0,
        "ret_3": close_return(bars, max(0, idx - 3), idx),
        "ret_5": close_return(bars, max(0, idx - 5), idx),
        "amplitude": safe_div(bar.high - bar.low, prev_close),
        "close_pos": safe_div(bar.close - bar.low, day_range, 0.5),
        "dist_ma20": safe_div(bar.close, ma20, 1.0) - 1.0,
        "atr_pct": safe_div(atr, bar.close),
        "gap": safe_div(bar.open, prev_close, 1.0) - 1.0,
        "volume_ratio_log": math.log(max(volume_ratio, 1e-6)),
    }


FEATURE_WEIGHTS = {
    "pct_change": 1.4,
    "prev_pct": 0.8,
    "ret_3": 0.8,
    "ret_5": 0.6,
    "amplitude": 0.8,
    "close_pos": 0.6,
    "dist_ma20": 0.9,
    "atr_pct": 0.7,
    "gap": 0.5,
    "volume_ratio_log": 0.5,
}


def feature_distance(left: dict[str, float], right: dict[str, float]) -> float:
    total = 0.0
    for key, weight in FEATURE_WEIGHTS.items():
        total += weight * abs(left.get(key, 0.0) - right.get(key, 0.0))
    return total


def weighted_average(items: list[tuple[float, float]]) -> float:
    total_weight = sum(weight for _, weight in items)
    if total_weight <= 0:
        return mean([value for value, _ in items])
    return sum(value * weight for value, weight in items) / total_weight


def predict_next_range(
    bars: list[DailyBar],
    signal_idx: int,
    config: PredictionConfig,
    next_trade_date: str = "NEXT",
) -> RangePrediction:
    if signal_idx >= len(bars):
        raise ValueError("signal_idx is outside bars")
    if signal_idx < max(30, config.atr_period + 5):
        raise ValueError("not enough history to predict next range")

    current_bar = bars[signal_idx]
    current_features = feature_vector(bars, signal_idx, config)
    start_idx = max(20, signal_idx - config.history_window)
    candidates: list[tuple[float, int]] = []

    for candidate_idx in range(start_idx, signal_idx):
        if candidate_idx + 1 > signal_idx:
            continue
        candidate_features = feature_vector(bars, candidate_idx, config)
        candidates.append((feature_distance(current_features, candidate_features), candidate_idx))

    if not candidates:
        raise ValueError("no historical similar days available")

    selected = sorted(candidates, key=lambda item: item[0])[: config.similar_count]
    high_items: list[tuple[float, float]] = []
    low_items: list[tuple[float, float]] = []
    close_items: list[tuple[float, float]] = []
    for distance, candidate_idx in selected:
        candidate = bars[candidate_idx]
        next_bar = bars[candidate_idx + 1]
        weight = 1.0 / (0.08 + distance)
        high_items.append((safe_div(next_bar.high, candidate.close, 1.0) - 1.0, weight))
        low_items.append((safe_div(next_bar.low, candidate.close, 1.0) - 1.0, weight))
        close_items.append((safe_div(next_bar.close, candidate.close, 1.0) - 1.0, weight))

    predicted_high_ret = weighted_average(high_items)
    predicted_low_ret = weighted_average(low_items)
    expected_close_return = weighted_average(close_items)
    atr = atr_at(bars, signal_idx, config.atr_period)
    atr_pct = safe_div(atr, current_bar.close)

    predicted_high = current_bar.close * (1.0 + predicted_high_ret)
    predicted_low = current_bar.close * (1.0 + predicted_low_ret)
    if predicted_low > predicted_high:
        predicted_low, predicted_high = predicted_high, predicted_low

    # Keep the point forecast plausible when similar days are too compressed.
    min_width = max(atr * 0.35, current_bar.close * 0.005)
    if predicted_high - predicted_low < min_width:
        middle = (predicted_high + predicted_low) / 2.0
        predicted_high = middle + min_width / 2.0
        predicted_low = middle - min_width / 2.0

    band_high = current_bar.close + atr
    band_low = current_bar.close - atr
    avg_distance = mean([distance for distance, _ in selected])
    score = safe_div(expected_close_return, max(atr_pct, 0.005)) - avg_distance

    return RangePrediction(
        signal_date=current_bar.trade_date,
        next_trade_date=next_trade_date,
        signal_close=round(current_bar.close, 4),
        predicted_high=round(predicted_high, 4),
        predicted_low=round(predicted_low, 4),
        band_high=round(band_high, 4),
        band_low=round(band_low, 4),
        expected_close_return=expected_close_return,
        atr=round(atr, 4),
        atr_pct=atr_pct,
        score=score,
        similar_count=len(selected),
    )


def calibrated_band(prediction: RangePrediction, calibration: CalibrationResult) -> RangePrediction:
    band_high = prediction.signal_close + prediction.atr * calibration.multiplier
    band_low = prediction.signal_close - prediction.atr * calibration.multiplier
    return replace(prediction, band_high=round(band_high, 4), band_low=round(band_low, 4))


def calibrate_atr_multiplier(
    bars: list[DailyBar],
    end_signal_idx: int,
    config: PredictionConfig,
    target_count: int = 90,
) -> CalibrationResult:
    if end_signal_idx <= 1:
        raise ValueError("not enough bars to calibrate")

    start_target_idx = max(1, end_signal_idx - target_count + 1)
    target_indices = list(range(start_target_idx, end_signal_idx + 1))
    candidate_results: list[dict[str, float]] = []

    for multiplier in config.atr_multiplier_candidates:
        hits = 0
        widths: list[float] = []
        for target_idx in target_indices:
            signal_idx = target_idx - 1
            signal = bars[signal_idx]
            actual = bars[target_idx]
            atr = atr_at(bars, signal_idx, config.atr_period)
            band_high = signal.close + multiplier * atr
            band_low = signal.close - multiplier * atr
            if actual.high <= band_high and actual.low >= band_low:
                hits += 1
            widths.append(safe_div((band_high - band_low), signal.close))

        samples = len(target_indices)
        candidate_results.append({
            "multiplier": float(multiplier),
            "coverage": safe_div(hits, samples),
            "avg_width_pct": mean(widths),
        })

    selected = candidate_results[-1]
    for item in candidate_results:
        if item["coverage"] >= config.target_coverage:
            selected = item
            break

    return CalibrationResult(
        multiplier=selected["multiplier"],
        coverage=selected["coverage"],
        avg_width_pct=selected["avg_width_pct"],
        candidates=candidate_results,
    )


def make_trade_plan(
    prediction: RangePrediction,
    calibration: CalibrationResult,
    config: PredictionConfig,
) -> TradePlan:
    atr = max(prediction.atr, prediction.signal_close * 0.005)
    buy_zone_low = max(prediction.predicted_low, prediction.band_low)
    buy_zone_high = min(prediction.signal_close, buy_zone_low + 0.35 * atr)
    if buy_zone_high < buy_zone_low:
        buy_zone_high = buy_zone_low

    stop_loss = buy_zone_low - 0.25 * atr
    take_profit = min(prediction.predicted_high, prediction.band_high)
    if take_profit <= buy_zone_high:
        take_profit = prediction.predicted_high

    risk = max(buy_zone_high - stop_loss, 1e-9)
    reward = take_profit - buy_zone_high
    reward_risk = reward / risk

    action = "BUY_ZONE"
    reason_parts: list[str] = []
    if prediction.expected_close_return <= 0:
        action = "WATCH"
        reason_parts.append("expected return is not positive")
    if reward_risk < config.min_reward_risk:
        action = "WATCH"
        reason_parts.append("reward/risk below threshold")
    if prediction.similar_count < max(5, config.similar_count // 2):
        action = "WATCH"
        reason_parts.append("too few similar days")
    if not reason_parts:
        reason_parts.append("positive similar-day expectation with acceptable reward/risk")

    return TradePlan(
        action=action,
        buy_zone_low=round(buy_zone_low, 4),
        buy_zone_high=round(buy_zone_high, 4),
        stop_loss=round(stop_loss, 4),
        take_profit=round(take_profit, 4),
        reward_risk=round(reward_risk, 4),
        position_hint=config.base_position_size if action == "BUY_ZONE" else 0.0,
        reason="; ".join(reason_parts),
    )


def simulate_trade(plan: TradePlan, actual: DailyBar, cost_rate: float = 0.0013) -> TradeExecution:
    if plan.action != "BUY_ZONE":
        return TradeExecution(False, 0.0, 0.0, 0.0, 0.0, "no_signal")
    if actual.open < plan.buy_zone_low:
        return TradeExecution(False, 0.0, 0.0, 0.0, 0.0, "open_below_buy_zone")
    if actual.low > plan.buy_zone_high:
        return TradeExecution(False, 0.0, 0.0, 0.0, 0.0, "not_filled")

    entry_price = plan.buy_zone_high
    if actual.open <= plan.buy_zone_high:
        entry_price = min(max(actual.open, plan.buy_zone_low), plan.buy_zone_high)

    exit_price = actual.close
    if actual.low <= plan.stop_loss:
        exit_reason = "t1_locked_stop_alert"
    elif actual.high >= plan.take_profit:
        exit_reason = "t1_locked_take_profit_alert"
    else:
        exit_reason = "t1_locked_close"

    gross_return = safe_div(exit_price, entry_price, 1.0) - 1.0
    net_return = gross_return
    return TradeExecution(
        entered=True,
        entry_price=round(entry_price, 4),
        exit_price=round(exit_price, 4),
        gross_return=gross_return,
        net_return=net_return,
        exit_reason=exit_reason,
        entry_date=actual.trade_date,
        exit_date=actual.trade_date,
        holding_days=0,
    )


def simulate_t1_position_trade(
    plan: TradePlan,
    bars: list[DailyBar],
    entry_idx: int,
    max_hold_days: int = 5,
    cost_rate: float = 0.0013,
) -> TradeExecution:
    if plan.action != "BUY_ZONE":
        return TradeExecution(False, 0.0, 0.0, 0.0, 0.0, "no_signal")
    if entry_idx < 0 or entry_idx >= len(bars):
        return TradeExecution(False, 0.0, 0.0, 0.0, 0.0, "invalid_entry_idx")

    entry_bar = bars[entry_idx]
    if entry_bar.open < plan.buy_zone_low:
        return TradeExecution(False, 0.0, 0.0, 0.0, 0.0, "open_below_buy_zone")
    if entry_bar.low > plan.buy_zone_high:
        return TradeExecution(False, 0.0, 0.0, 0.0, 0.0, "not_filled")
    if entry_bar.low <= plan.stop_loss:
        return TradeExecution(False, 0.0, 0.0, 0.0, 0.0, "entry_day_stop_breached")

    entry_price = plan.buy_zone_high
    if entry_bar.open <= plan.buy_zone_high:
        entry_price = min(max(entry_bar.open, plan.buy_zone_low), plan.buy_zone_high)

    if entry_idx + 1 >= len(bars):
        return TradeExecution(
            True,
            round(entry_price, 4),
            round(entry_bar.close, 4),
            safe_div(entry_bar.close, entry_price, 1.0) - 1.0,
            safe_div(entry_bar.close, entry_price, 1.0) - 1.0,
            "no_t1_bar_mark_to_market",
            entry_bar.trade_date,
            entry_bar.trade_date,
            0,
        )

    exit_idx = min(len(bars) - 1, entry_idx + max(1, max_hold_days))
    exit_bar = bars[exit_idx]
    exit_price = exit_bar.close
    exit_reason = "max_hold_close"

    for idx in range(entry_idx + 1, exit_idx + 1):
        bar = bars[idx]
        if bar.open <= plan.stop_loss:
            exit_idx = idx
            exit_bar = bar
            exit_price = bar.open
            exit_reason = "t1_stop_gap"
            break
        if bar.open >= plan.take_profit:
            exit_idx = idx
            exit_bar = bar
            exit_price = bar.open
            exit_reason = "t1_take_profit_gap"
            break
        if bar.low <= plan.stop_loss:
            exit_idx = idx
            exit_bar = bar
            exit_price = plan.stop_loss
            exit_reason = "t1_stop_loss"
            break
        if bar.high >= plan.take_profit:
            exit_idx = idx
            exit_bar = bar
            exit_price = plan.take_profit
            exit_reason = "t1_take_profit"
            break

    gross_return = safe_div(exit_price, entry_price, 1.0) - 1.0
    net_return = gross_return
    return TradeExecution(
        entered=True,
        entry_price=round(entry_price, 4),
        exit_price=round(exit_price, 4),
        gross_return=gross_return,
        net_return=net_return,
        exit_reason=exit_reason,
        entry_date=entry_bar.trade_date,
        exit_date=exit_bar.trade_date,
        holding_days=exit_idx - entry_idx,
    )


def max_drawdown(returns: list[float]) -> float:
    equity = 1.0
    peak = 1.0
    worst = 0.0
    for item in returns:
        equity *= 1.0 + item
        peak = max(peak, equity)
        worst = min(worst, safe_div(equity, peak, 1.0) - 1.0)
    return worst


def backtest_predictions(
    bars: list[DailyBar],
    config: PredictionConfig,
    target_count: int = 90,
) -> tuple[dict[str, float], list[dict[str, Any]]]:
    if len(bars) < 40:
        raise ValueError("not enough bars to backtest")

    start_target_idx = max(31, len(bars) - target_count)
    rows: list[dict[str, Any]] = []
    for target_idx in range(start_target_idx, len(bars)):
        signal_idx = target_idx - 1
        try:
            prediction = predict_next_range(bars[: signal_idx + 1], signal_idx, config, bars[target_idx].trade_date)
            calibration = calibrate_atr_multiplier(bars[: signal_idx + 1], signal_idx, config, target_count)
            prediction = calibrated_band(prediction, calibration)
        except ValueError:
            continue

        actual = bars[target_idx]
        signal_close = bars[signal_idx].close
        high_abs_error = abs(actual.high - prediction.predicted_high)
        low_abs_error = abs(actual.low - prediction.predicted_low)
        high_error_pct = safe_div(high_abs_error, signal_close)
        low_error_pct = safe_div(low_abs_error, signal_close)
        band_hit = actual.high <= prediction.band_high and actual.low >= prediction.band_low
        direction_hit = (prediction.expected_close_return >= 0) == (actual.close >= signal_close)
        rows.append({
            "target_date": actual.trade_date,
            "signal_date": prediction.signal_date,
            "signal_close": round(signal_close, 4),
            "actual_high": round(actual.high, 4),
            "actual_low": round(actual.low, 4),
            "predicted_high": prediction.predicted_high,
            "predicted_low": prediction.predicted_low,
            "band_high": prediction.band_high,
            "band_low": prediction.band_low,
            "high_abs_error": round(high_abs_error, 4),
            "low_abs_error": round(low_abs_error, 4),
            "high_error_pct": high_error_pct,
            "low_error_pct": low_error_pct,
            "high_within_1pct": high_error_pct <= 0.01,
            "low_within_1pct": low_error_pct <= 0.01,
            "high_within_2pct": high_error_pct <= 0.02,
            "low_within_2pct": low_error_pct <= 0.02,
            "band_hit": band_hit,
            "direction_hit": direction_hit,
            "band_width_pct": safe_div(prediction.band_high - prediction.band_low, signal_close),
        })

    samples = len(rows)
    metrics = {
        "samples": samples,
        "high_mae": mean([row["high_abs_error"] for row in rows]),
        "low_mae": mean([row["low_abs_error"] for row in rows]),
        "high_error_pct": mean([row["high_error_pct"] for row in rows]),
        "low_error_pct": mean([row["low_error_pct"] for row in rows]),
        "high_within_1pct": safe_div(sum(bool(row["high_within_1pct"]) for row in rows), samples),
        "low_within_1pct": safe_div(sum(bool(row["low_within_1pct"]) for row in rows), samples),
        "both_within_1pct": safe_div(
            sum(bool(row["high_within_1pct"] and row["low_within_1pct"]) for row in rows),
            samples,
        ),
        "high_within_2pct": safe_div(sum(bool(row["high_within_2pct"]) for row in rows), samples),
        "low_within_2pct": safe_div(sum(bool(row["low_within_2pct"]) for row in rows), samples),
        "both_within_2pct": safe_div(
            sum(bool(row["high_within_2pct"] and row["low_within_2pct"]) for row in rows),
            samples,
        ),
        "band_coverage": safe_div(sum(bool(row["band_hit"]) for row in rows), samples),
        "direction_hit": safe_div(sum(bool(row["direction_hit"]) for row in rows), samples),
        "avg_band_width_pct": mean([row["band_width_pct"] for row in rows]),
    }
    return metrics, rows


def backtest_trade_rules(
    bars: list[DailyBar],
    config: PredictionConfig,
    target_count: int = 90,
) -> tuple[dict[str, float], list[dict[str, Any]]]:
    if len(bars) < 40:
        raise ValueError("not enough bars to backtest trades")

    max_hold_days = max(1, config.max_hold_days)
    end_target_idx = max(31, len(bars) - max_hold_days)
    start_target_idx = max(31, end_target_idx - target_count)
    rows: list[dict[str, Any]] = []
    returns: list[float] = []
    for target_idx in range(start_target_idx, end_target_idx):
        signal_idx = target_idx - 1
        try:
            prediction = predict_next_range(bars[: signal_idx + 1], signal_idx, config, bars[target_idx].trade_date)
            calibration = calibrate_atr_multiplier(bars[: signal_idx + 1], signal_idx, config, target_count)
            prediction = calibrated_band(prediction, calibration)
        except ValueError:
            continue

        plan = make_trade_plan(prediction, calibration, config)
        execution = simulate_t1_position_trade(plan, bars, target_idx, max_hold_days, config.round_trip_cost)
        if execution.entered:
            returns.append(execution.net_return)
        rows.append({
            "target_date": bars[target_idx].trade_date,
            "signal_date": prediction.signal_date,
            "action": plan.action,
            "buy_zone_low": plan.buy_zone_low,
            "buy_zone_high": plan.buy_zone_high,
            "stop_loss": plan.stop_loss,
            "take_profit": plan.take_profit,
            "reward_risk": plan.reward_risk,
            "entered": execution.entered,
            "entry_date": execution.entry_date,
            "entry_price": execution.entry_price,
            "exit_date": execution.exit_date,
            "exit_price": execution.exit_price,
            "exit_reason": execution.exit_reason,
            "holding_days": execution.holding_days,
            "net_return": execution.net_return,
            "expected_close_return": prediction.expected_close_return,
        })

    trade_count = len(returns)
    wins = [item for item in returns if item > 0]
    losses = [item for item in returns if item < 0]
    total_return = math.prod([1.0 + item for item in returns]) - 1.0 if returns else 0.0
    profit_factor = safe_div(sum(wins), abs(sum(losses))) if losses else (999.0 if wins else 0.0)
    metrics = {
        "signals": sum(1 for row in rows if row["action"] == "BUY_ZONE"),
        "trades": trade_count,
        "total_return": total_return,
        "avg_return": mean(returns),
        "win_rate": safe_div(len(wins), trade_count),
        "profit_factor": profit_factor,
        "max_drawdown": max_drawdown(returns),
        "max_hold_days": max_hold_days,
    }
    return metrics, rows


def round_metrics(metrics: dict[str, float]) -> dict[str, float]:
    return {key: round(value, 6) if isinstance(value, float) else value for key, value in metrics.items()}


def write_dicts_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def format_pct(value: float) -> str:
    return f"{value * 100:.2f}%"


def write_report(
    output_dir: Path,
    code: str,
    latest_bar: DailyBar,
    prediction: RangePrediction,
    calibration: CalibrationResult,
    plan: TradePlan,
    prediction_metrics: dict[str, float],
    trade_metrics: dict[str, float],
) -> None:
    lines = [
        f"# {code} Range Trader Report",
        "",
        f"- Generated at: {datetime.now().isoformat(timespec='seconds')}",
        f"- Latest bar: {latest_bar.trade_date} close {latest_bar.close:.2f}, high {latest_bar.high:.2f}, low {latest_bar.low:.2f}, pct {latest_bar.pct_change:.2f}%",
        "",
        "## Next Session",
        "",
        f"- Action: {plan.action}",
        f"- Predicted high/low: {prediction.predicted_high:.2f} / {prediction.predicted_low:.2f}",
        f"- Calibrated ATR band: {prediction.band_high:.2f} / {prediction.band_low:.2f}",
        f"- Buy zone: {plan.buy_zone_low:.2f} - {plan.buy_zone_high:.2f}",
        f"- Stop / take profit: {plan.stop_loss:.2f} / {plan.take_profit:.2f}",
        f"- Reward/risk: {plan.reward_risk:.2f}",
        f"- Position hint: {format_pct(plan.position_hint)}",
        f"- Reason: {plan.reason}",
        "",
        "## 90-Target Prediction Backtest",
        "",
        f"- Samples: {int(prediction_metrics['samples'])}",
        f"- High MAE: {prediction_metrics['high_mae']:.2f}",
        f"- Low MAE: {prediction_metrics['low_mae']:.2f}",
        f"- High error pct: {format_pct(prediction_metrics['high_error_pct'])}",
        f"- Low error pct: {format_pct(prediction_metrics['low_error_pct'])}",
        f"- Both within 2 pct: {format_pct(prediction_metrics['both_within_2pct'])}",
        f"- Band coverage: {format_pct(prediction_metrics['band_coverage'])}",
        f"- Direction hit: {format_pct(prediction_metrics['direction_hit'])}",
        "",
        "## 90-Target T+1 Exit Backtest",
        "",
        f"- Signals: {int(trade_metrics['signals'])}",
        f"- Trades: {int(trade_metrics['trades'])}",
        f"- Total return: {format_pct(trade_metrics['total_return'])}",
        f"- Win rate: {format_pct(trade_metrics['win_rate'])}",
        f"- Profit factor: {trade_metrics['profit_factor']:.2f}",
        f"- Max drawdown: {format_pct(trade_metrics['max_drawdown'])}",
        f"- Max hold days: {int(trade_metrics['max_hold_days'])}",
        "- Entry-day stop/take hits are not exit fills; exits start from the next trading day.",
        "",
        "This is a paper-trading research report, not a guaranteed trading instruction.",
    ]
    (output_dir / "range_trader_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def analyze_stock(
    raw_code: str,
    bars: list[DailyBar],
    config: PredictionConfig,
    base_dir: Path,
    target_count: int = 90,
) -> dict[str, Any]:
    if len(bars) < 60:
        raise ValueError("not enough daily bars")
    code = normalize_code(raw_code)
    latest_idx = len(bars) - 1
    latest_bar = bars[latest_idx]
    prediction = predict_next_range(bars, latest_idx, config)
    calibration = calibrate_atr_multiplier(bars, latest_idx, config, target_count)
    prediction = calibrated_band(prediction, calibration)
    plan = make_trade_plan(prediction, calibration, config)
    prediction_metrics, prediction_rows = backtest_predictions(bars, config, target_count)
    trade_metrics, trade_rows = backtest_trade_rules(bars, config, target_count)

    output_dir = base_dir / "reports" / "range_trader" / f"{code.replace('.', '_')}_{latest_bar.trade_date}"
    output_dir.mkdir(parents=True, exist_ok=True)
    write_dicts_csv(output_dir / "prediction_backtest.csv", prediction_rows)
    write_dicts_csv(output_dir / "trade_backtest.csv", trade_rows)

    summary = {
        "code": code,
        "latest_bar": asdict(latest_bar),
        "prediction": asdict(prediction),
        "calibration": asdict(calibration),
        "trade_plan": asdict(plan),
        "prediction_metrics": round_metrics(prediction_metrics),
        "trade_metrics": round_metrics(trade_metrics),
        "output_dir": str(output_dir),
    }
    with (output_dir / "prediction_summary.json").open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, ensure_ascii=False, indent=2)
    write_report(
        output_dir,
        code,
        latest_bar,
        prediction,
        calibration,
        plan,
        prediction_metrics,
        trade_metrics,
    )
    return summary


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="A-share next-day range trader")
    parser.add_argument("--code", required=True, help="Stock code, for example 300450 or 300450.SZ")
    parser.add_argument("--base-dir", default=str(DEFAULT_BASE_DIR))
    parser.add_argument("--input-json", type=Path, default=None, help="Eastmoney K-line JSON file")
    parser.add_argument("--beg", default="20240101")
    parser.add_argument("--end", default=date.today().strftime("%Y%m%d"))
    parser.add_argument("--target-count", type=int, default=90)
    parser.add_argument("--history-window", type=int, default=90)
    parser.add_argument("--similar-count", type=int, default=15)
    parser.add_argument("--target-coverage", type=float, default=0.80)
    parser.add_argument("--min-reward-risk", type=float, default=1.8)
    return parser


def main() -> None:
    args = build_arg_parser().parse_args()
    config = PredictionConfig(
        history_window=args.history_window,
        similar_count=args.similar_count,
        target_coverage=args.target_coverage,
        min_reward_risk=args.min_reward_risk,
    )
    bars = load_daily_bars(args.code, args.beg, args.end, args.input_json)
    summary = analyze_stock(args.code, bars, config, Path(args.base_dir), args.target_count)
    printable = {
        "code": summary["code"],
        "latest_date": summary["latest_bar"]["trade_date"],
        "action": summary["trade_plan"]["action"],
        "predicted_high": summary["prediction"]["predicted_high"],
        "predicted_low": summary["prediction"]["predicted_low"],
        "band_high": summary["prediction"]["band_high"],
        "band_low": summary["prediction"]["band_low"],
        "prediction_metrics": summary["prediction_metrics"],
        "trade_metrics": summary["trade_metrics"],
        "output_dir": summary["output_dir"],
    }
    print(json.dumps(printable, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
