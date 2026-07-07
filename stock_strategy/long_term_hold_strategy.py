from __future__ import annotations

import csv
import json
import math
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from stock_range_trader import DailyBar, close_return, normalize_code, safe_div


@dataclass(frozen=True)
class LongTermHoldConfig:
    benchmark_code: str = "000300.SH"
    min_history_days: int = 260
    ma_short: int = 60
    ma_mid: int = 120
    ma_long: int = 200
    relative_short_lookback: int = 120
    relative_long_lookback: int = 240
    min_stock_return_120d: float = 0.06
    min_excess_return_120d: float = 0.06
    min_excess_return_240d: float = 0.08
    max_drawdown_120d: float = -0.28
    max_volatility_120d: float = 0.42
    max_distance_ma200: float = 0.55
    min_turnover: float = 0.0
    max_entry_gap: float = 0.03
    buy_pullback_pct: float = 0.03
    max_initial_loss: float = 0.12
    ma200_exit_buffer: float = 0.03
    min_hold_days: int = 60
    relative_exit_lookback: int = 60
    max_relative_exit_underperformance: float = -0.06
    trail_start_pct: float = 0.25
    trailing_stop_pct: float = 0.15
    max_hold_days: int = 520
    cooldown_days: int = 20
    base_position_size: float = 0.20
    round_trip_cost: float = 0.0013


@dataclass(frozen=True)
class LongTermHoldResult:
    secucode: str
    name: str = ""
    tradable: bool = False
    status: str = "ok"
    reject_reason: str = ""
    rank_score: float = 0.0
    latest_date: str = ""
    latest_close: float = 0.0
    benchmark_code: str = "000300.SH"
    ma60: float = 0.0
    ma120: float = 0.0
    ma200: float = 0.0
    distance_ma200: float = 0.0
    stock_return_120d: float = 0.0
    benchmark_return_120d: float = 0.0
    excess_return_120d: float = 0.0
    stock_return_240d: float = 0.0
    benchmark_return_240d: float = 0.0
    excess_return_240d: float = 0.0
    drawdown_120d: float = 0.0
    volatility_120d: float = 0.0
    buy_zone_low: float = 0.0
    buy_zone_high: float = 0.0
    initial_stop_loss: float = 0.0
    trend_stop_price: float = 0.0
    relative_exit_excess: float = 0.0
    position_hint: float = 0.0
    tags: str = ""


@dataclass(frozen=True)
class LongTermHoldTrade:
    secucode: str
    signal_date: str
    entry_date: str
    exit_date: str
    entry_price: float
    exit_price: float
    gross_return: float
    net_return: float
    benchmark_return: float
    excess_return: float
    exit_reason: str
    holding_days: int
    signal_score: float


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def pct(value: float) -> str:
    return f"{value * 100:.2f}%"


def _window(bars: list[DailyBar], end_idx: int, length: int, include_end: bool = True) -> list[DailyBar]:
    stop = end_idx + 1 if include_end else end_idx
    start = max(0, stop - length)
    return bars[start:stop]


def _ma(bars: list[DailyBar], end_idx: int, length: int) -> float:
    return mean([bar.close for bar in _window(bars, end_idx, length)])


def _bar_on_or_before(bars: list[DailyBar], trade_date: str) -> DailyBar | None:
    selected: DailyBar | None = None
    for bar in bars:
        if bar.trade_date > trade_date:
            break
        selected = bar
    return selected


def _benchmark_return_between(benchmark_bars: list[DailyBar], start_date: str, end_date: str) -> float:
    start = _bar_on_or_before(benchmark_bars, start_date)
    end = _bar_on_or_before(benchmark_bars, end_date)
    if start is None or end is None or start.close <= 0:
        return 0.0
    return end.close / start.close - 1.0


def _benchmark_return_for_stock_window(
    stock_bars: list[DailyBar],
    benchmark_bars: list[DailyBar],
    end_idx: int,
    lookback: int,
) -> float:
    start_idx = end_idx - lookback
    if start_idx < 0:
        return 0.0
    return _benchmark_return_between(
        benchmark_bars,
        stock_bars[start_idx].trade_date,
        stock_bars[end_idx].trade_date,
    )


def _stock_return(bars: list[DailyBar], end_idx: int, lookback: int) -> float:
    start_idx = end_idx - lookback
    if start_idx < 0 or bars[start_idx].close <= 0:
        return 0.0
    return bars[end_idx].close / bars[start_idx].close - 1.0


def _drawdown_from_recent_high(bars: list[DailyBar], end_idx: int, length: int) -> float:
    values = _window(bars, end_idx, length)
    recent_high = max((bar.high for bar in values), default=0.0)
    if recent_high <= 0:
        return 0.0
    return bars[end_idx].close / recent_high - 1.0


def _annualized_volatility(bars: list[DailyBar], end_idx: int, length: int) -> float:
    values = _window(bars, end_idx, length)
    returns: list[float] = []
    for idx in range(1, len(values)):
        previous = values[idx - 1].close
        if previous > 0:
            returns.append(values[idx].close / previous - 1.0)
    if len(returns) < 2:
        return 0.0
    avg = mean(returns)
    variance = mean([(item - avg) ** 2 for item in returns])
    return math.sqrt(variance) * math.sqrt(244)


def _empty_result(
    secucode: str,
    name: str,
    reason: str,
    config: LongTermHoldConfig,
    status: str = "ok",
) -> LongTermHoldResult:
    return LongTermHoldResult(
        secucode=normalize_code(secucode),
        name=name,
        tradable=False,
        status=status,
        reject_reason=reason,
        benchmark_code=config.benchmark_code,
    )


def _rank_score(
    excess_return_120d: float,
    excess_return_240d: float,
    stock_return_120d: float,
    distance_ma200: float,
    drawdown_120d: float,
    volatility_120d: float,
    config: LongTermHoldConfig,
    tradable: bool,
) -> float:
    relative_120_score = min(max(excess_return_120d / max(config.min_excess_return_120d, 1e-9), 0.0), 2.0) / 2.0 * 22.0
    relative_240_score = min(max(excess_return_240d / max(config.min_excess_return_240d, 1e-9), 0.0), 2.0) / 2.0 * 18.0
    absolute_score = min(max(stock_return_120d / 0.24, 0.0), 1.0) * 12.0
    trend_score = max(0.0, 1.0 - abs(distance_ma200 - 0.12) / 0.35) * 10.0
    drawdown_score = max(0.0, 1.0 - abs(drawdown_120d) / max(abs(config.max_drawdown_120d), 1e-9)) * 10.0
    volatility_score = max(0.0, 1.0 - volatility_120d / max(config.max_volatility_120d, 1e-9)) * 8.0
    pass_bonus = 12.0 if tradable else 0.0
    return round(18.0 + relative_120_score + relative_240_score + absolute_score + trend_score + drawdown_score + volatility_score + pass_bonus, 6)


def analyze_long_term_hold(
    secucode: str,
    name: str,
    bars: list[DailyBar],
    benchmark_bars: list[DailyBar],
    config: LongTermHoldConfig = LongTermHoldConfig(),
) -> LongTermHoldResult:
    normalized = normalize_code(secucode)
    required = max(config.min_history_days, config.ma_long + 1, config.relative_long_lookback + 1)
    if len(bars) < required:
        return _empty_result(normalized, name, f"history_days {len(bars)} < {required}", config)
    if len(benchmark_bars) < max(config.relative_short_lookback + 1, config.relative_long_lookback + 1):
        return _empty_result(normalized, name, "benchmark_history_insufficient", config)

    latest_idx = len(bars) - 1
    latest = bars[latest_idx]
    if latest.close <= 0:
        return _empty_result(normalized, name, "invalid latest close", config)

    ma60 = _ma(bars, latest_idx, config.ma_short)
    ma120 = _ma(bars, latest_idx, config.ma_mid)
    ma200 = _ma(bars, latest_idx, config.ma_long)
    stock_return_120d = _stock_return(bars, latest_idx, config.relative_short_lookback)
    stock_return_240d = _stock_return(bars, latest_idx, config.relative_long_lookback)
    benchmark_return_120d = _benchmark_return_for_stock_window(
        bars,
        benchmark_bars,
        latest_idx,
        config.relative_short_lookback,
    )
    benchmark_return_240d = _benchmark_return_for_stock_window(
        bars,
        benchmark_bars,
        latest_idx,
        config.relative_long_lookback,
    )
    excess_return_120d = stock_return_120d - benchmark_return_120d
    excess_return_240d = stock_return_240d - benchmark_return_240d
    drawdown_120d = _drawdown_from_recent_high(bars, latest_idx, config.relative_short_lookback)
    volatility_120d = _annualized_volatility(bars, latest_idx, config.relative_short_lookback)
    distance_ma200 = safe_div(latest.close, ma200, 1.0) - 1.0
    trend_stop_price = ma200 * (1.0 - config.ma200_exit_buffer)
    initial_stop_loss = max(latest.close * (1.0 - config.max_initial_loss), trend_stop_price)

    reasons: list[str] = []
    if latest.close <= ma200:
        reasons.append("close_below_ma200")
    if ma60 <= ma120:
        reasons.append("ma60_not_above_ma120")
    if ma120 <= ma200:
        reasons.append("ma120_not_above_ma200")
    if stock_return_120d < config.min_stock_return_120d:
        reasons.append(f"stock_return_120d {pct(stock_return_120d)} < {pct(config.min_stock_return_120d)}")
    if excess_return_120d < config.min_excess_return_120d:
        reasons.append(f"excess_return_120d {pct(excess_return_120d)} < {pct(config.min_excess_return_120d)}")
    if excess_return_240d < config.min_excess_return_240d:
        reasons.append(f"excess_return_240d {pct(excess_return_240d)} < {pct(config.min_excess_return_240d)}")
    if drawdown_120d < config.max_drawdown_120d:
        reasons.append(f"drawdown_120d {pct(drawdown_120d)} < {pct(config.max_drawdown_120d)}")
    if volatility_120d > config.max_volatility_120d:
        reasons.append(f"volatility_120d {pct(volatility_120d)} > {pct(config.max_volatility_120d)}")
    if distance_ma200 > config.max_distance_ma200:
        reasons.append(f"distance_ma200 {pct(distance_ma200)} > {pct(config.max_distance_ma200)}")
    if latest.turnover > 0 and latest.turnover < config.min_turnover:
        reasons.append(f"turnover {latest.turnover:.2f} < {config.min_turnover:.2f}")

    tradable = not reasons
    rank_score = _rank_score(
        excess_return_120d=excess_return_120d,
        excess_return_240d=excess_return_240d,
        stock_return_120d=stock_return_120d,
        distance_ma200=distance_ma200,
        drawdown_120d=drawdown_120d,
        volatility_120d=volatility_120d,
        config=config,
        tradable=tradable,
    )
    tags = ["long_term_hold"]
    if excess_return_120d >= config.min_excess_return_120d * 1.5:
        tags.append("strong_relative")
    if drawdown_120d > config.max_drawdown_120d * 0.35:
        tags.append("shallow_drawdown")
    if volatility_120d <= config.max_volatility_120d * 0.55:
        tags.append("low_volatility")

    return LongTermHoldResult(
        secucode=normalized,
        name=name,
        tradable=tradable,
        status="ok",
        reject_reason="; ".join(reasons),
        rank_score=rank_score,
        latest_date=latest.trade_date,
        latest_close=latest.close,
        benchmark_code=config.benchmark_code,
        ma60=ma60,
        ma120=ma120,
        ma200=ma200,
        distance_ma200=distance_ma200,
        stock_return_120d=stock_return_120d,
        benchmark_return_120d=benchmark_return_120d,
        excess_return_120d=excess_return_120d,
        stock_return_240d=stock_return_240d,
        benchmark_return_240d=benchmark_return_240d,
        excess_return_240d=excess_return_240d,
        drawdown_120d=drawdown_120d,
        volatility_120d=volatility_120d,
        buy_zone_low=latest.close * (1.0 - config.buy_pullback_pct),
        buy_zone_high=latest.close * (1.0 + config.max_entry_gap),
        initial_stop_loss=initial_stop_loss,
        trend_stop_price=trend_stop_price,
        relative_exit_excess=config.max_relative_exit_underperformance,
        position_hint=config.base_position_size if tradable else 0.0,
        tags=",".join(tags),
    )


def _exit_trade(
    secucode: str,
    signal: LongTermHoldResult,
    bars: list[DailyBar],
    benchmark_bars: list[DailyBar],
    entry_idx: int,
    config: LongTermHoldConfig,
) -> LongTermHoldTrade | None:
    entry_bar = bars[entry_idx]
    if entry_bar.open > signal.buy_zone_high or entry_bar.open < signal.initial_stop_loss:
        return None

    entry_price = entry_bar.open
    last_idx = min(len(bars) - 1, entry_idx + config.max_hold_days - 1)
    exit_idx = last_idx
    exit_price = bars[last_idx].close
    exit_reason = "max_hold" if last_idx < len(bars) - 1 else "open_position_end"
    best_close = entry_bar.close

    for idx in range(entry_idx + 1, last_idx + 1):
        bar = bars[idx]
        best_close = max(best_close, bar.close)
        ma200 = _ma(bars, idx, config.ma_long) if idx + 1 >= config.ma_long else 0.0
        trend_stop = ma200 * (1.0 - config.ma200_exit_buffer) if ma200 > 0 else 0.0
        hard_stop = max(entry_price * (1.0 - config.max_initial_loss), trend_stop)

        if bar.open <= hard_stop:
            exit_idx = idx
            exit_price = bar.open
            exit_reason = "stop_gap"
            break
        if bar.low <= hard_stop:
            exit_idx = idx
            exit_price = hard_stop
            exit_reason = "stop_loss"
            break

        holding_days = idx - entry_idx + 1
        if holding_days < config.min_hold_days:
            continue

        if trend_stop > 0 and bar.close < trend_stop:
            exit_idx = idx
            exit_price = bar.close
            exit_reason = "trend_break"
            break

        peak_return = best_close / entry_price - 1.0
        if peak_return >= config.trail_start_pct and bar.close <= best_close * (1.0 - config.trailing_stop_pct):
            exit_idx = idx
            exit_price = bar.close
            exit_reason = "trailing_stop"
            break

        start_idx = idx - config.relative_exit_lookback
        if start_idx >= 0:
            stock_ret = close_return(bars, start_idx, idx)
            benchmark_ret = _benchmark_return_between(
                benchmark_bars,
                bars[start_idx].trade_date,
                bar.trade_date,
            )
            ma120 = _ma(bars, idx, config.ma_mid) if idx + 1 >= config.ma_mid else 0.0
            if stock_ret - benchmark_ret <= config.max_relative_exit_underperformance and ma120 > 0 and bar.close < ma120:
                exit_idx = idx
                exit_price = bar.close
                exit_reason = "relative_weakness"
                break

    gross_return = exit_price / entry_price - 1.0
    net_return = gross_return - config.round_trip_cost
    benchmark_return = _benchmark_return_between(
        benchmark_bars,
        entry_bar.trade_date,
        bars[exit_idx].trade_date,
    )
    return LongTermHoldTrade(
        secucode=secucode,
        signal_date=signal.latest_date,
        entry_date=entry_bar.trade_date,
        exit_date=bars[exit_idx].trade_date,
        entry_price=entry_price,
        exit_price=exit_price,
        gross_return=gross_return,
        net_return=net_return,
        benchmark_return=benchmark_return,
        excess_return=net_return - benchmark_return,
        exit_reason=exit_reason,
        holding_days=max(1, exit_idx - entry_idx + 1),
        signal_score=signal.rank_score,
    )


def _max_drawdown(returns: list[float]) -> float:
    equity = 1.0
    peak = 1.0
    worst = 0.0
    for item in returns:
        equity *= 1.0 + item
        peak = max(peak, equity)
        worst = min(worst, equity / peak - 1.0)
    return worst


def backtest_long_term_hold(
    secucode: str,
    bars: list[DailyBar],
    benchmark_bars: list[DailyBar],
    config: LongTermHoldConfig = LongTermHoldConfig(),
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    normalized = normalize_code(secucode)
    trades: list[LongTermHoldTrade] = []
    idx = max(config.min_history_days - 1, config.ma_long, config.relative_long_lookback)
    last_signal_idx = len(bars) - 2
    while idx <= last_signal_idx:
        signal = analyze_long_term_hold(normalized, "", bars[: idx + 1], benchmark_bars, config)
        if signal.tradable:
            trade = _exit_trade(normalized, signal, bars, benchmark_bars, idx + 1, config)
            if trade is not None:
                trades.append(trade)
                try:
                    exit_idx = next(item_idx for item_idx, bar in enumerate(bars) if bar.trade_date == trade.exit_date)
                except StopIteration:
                    exit_idx = idx + config.max_hold_days
                idx = max(idx + 1, exit_idx + config.cooldown_days)
                continue
        idx += 1

    returns = [trade.net_return for trade in trades]
    benchmark_returns = [trade.benchmark_return for trade in trades]
    wins = [item for item in returns if item > 0]
    losses = [item for item in returns if item <= 0]
    years = max(len(bars) / 244.0, 1e-9)
    total_return = math.prod([1.0 + item for item in returns]) - 1.0 if returns else 0.0
    benchmark_total_return = math.prod([1.0 + item for item in benchmark_returns]) - 1.0 if benchmark_returns else 0.0
    metrics = {
        "signals": len(trades),
        "trades": len(trades),
        "trades_per_year": safe_div(len(trades), years),
        "avg_return": mean(returns),
        "win_rate": safe_div(len(wins), len(returns)),
        "total_return": total_return,
        "benchmark_total_return": benchmark_total_return,
        "excess_total_return": total_return - benchmark_total_return,
        "best_return": max(returns) if returns else 0.0,
        "worst_return": min(returns) if returns else 0.0,
        "profit_factor": safe_div(sum(wins), abs(sum(losses)), float("inf")) if losses else (float("inf") if wins else 0.0),
        "max_drawdown": _max_drawdown(returns),
        "avg_holding_days": mean([trade.holding_days for trade in trades]),
    }
    return metrics, [asdict(trade) for trade in trades]


def _json_safe(value: Any) -> Any:
    if isinstance(value, float) and math.isinf(value):
        return "inf" if value > 0 else "-inf"
    if isinstance(value, dict):
        return {key: _json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    return value


def write_long_term_hold_outputs(
    output_dir: Path,
    results: list[LongTermHoldResult],
    config: LongTermHoldConfig,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = [asdict(item) for item in results]
    fieldnames = list(rows[0].keys()) if rows else list(LongTermHoldResult.__dataclass_fields__.keys())
    with (output_dir / "long_term_hold_scan.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "strategy": "long_term_hold_v1",
        "config": asdict(config),
        "results": rows,
    }
    (output_dir / "long_term_hold_scan.json").write_text(
        json.dumps(_json_safe(payload), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    tradable = [item for item in results if item.tradable]
    lines = [
        "# 长期持有跑赢大盘策略扫描",
        "",
        f"- Generated at: {payload['generated_at']}",
        f"- Benchmark: {config.benchmark_code}",
        f"- Scanned: {len(results)}",
        f"- Candidates: {len(tradable)}",
        f"- Target behavior: hold for months, trade rarely, stay only while relative strength is intact.",
        "",
        "## 买入规则",
        "",
        f"- 长期趋势：收盘价在 MA{config.ma_long} 上方，且 MA{config.ma_short} > MA{config.ma_mid} > MA{config.ma_long}",
        f"- 跑赢大盘：{config.relative_short_lookback} 日超额收益不低于 {pct(config.min_excess_return_120d)}，{config.relative_long_lookback} 日超额收益不低于 {pct(config.min_excess_return_240d)}",
        f"- 风险过滤：{config.relative_short_lookback} 日回撤不深于 {pct(config.max_drawdown_120d)}，年化波动不高于 {pct(config.max_volatility_120d)}",
        f"- 买点：信号收盘价下方 {pct(config.buy_pullback_pct)} 到上方 {pct(config.max_entry_gap)} 之间分批建仓",
        "",
        "## 卖出规则",
        "",
        f"- 初始止损：买入价下方 {pct(config.max_initial_loss)} 或 MA{config.ma_long} 下方 {pct(config.ma200_exit_buffer)}，取更高者",
        f"- 趋势卖点：持有满 {config.min_hold_days} 个交易日后，收盘跌破 MA{config.ma_long} 下方缓冲线",
        f"- 跑输卖点：{config.relative_exit_lookback} 日超额收益低于 {pct(config.max_relative_exit_underperformance)} 且收盘跌破 MA{config.ma_mid}",
        f"- 回撤卖点：浮盈超过 {pct(config.trail_start_pct)} 后，从最高收盘回撤 {pct(config.trailing_stop_pct)}",
        "",
        "## 通过候选",
        "",
    ]
    if tradable:
        lines.append("| Code | Name | Score | Close | Stock 120D | Benchmark 120D | Excess 120D | Buy Zone | Initial Stop | Trend Stop | Tags |")
        lines.append("|---|---|---:|---:|---:|---:|---:|---|---:|---:|---|")
        for item in tradable:
            lines.append(
                f"| {item.secucode} | {item.name} | {item.rank_score:.2f} | {item.latest_close:.2f} | "
                f"{pct(item.stock_return_120d)} | {pct(item.benchmark_return_120d)} | {pct(item.excess_return_120d)} | "
                f"{item.buy_zone_low:.2f}-{item.buy_zone_high:.2f} | {item.initial_stop_loss:.2f} | "
                f"{item.trend_stop_price:.2f} | {item.tags} |"
            )
    else:
        lines.append("No candidates passed all filters.")

    lines.extend(["", "## 观察/拒绝", ""])
    lines.append("| Code | Name | Status | Score | Reason |")
    lines.append("|---|---|---|---:|---|")
    for item in [row for row in results if not row.tradable]:
        lines.append(
            f"| {item.secucode} | {item.name} | {item.status} | {item.rank_score:.2f} | {item.reject_reason} |"
        )
    lines.append("")
    lines.append("This is a research scanner for paper trading. It does not place orders or guarantee returns.")
    (output_dir / "long_term_hold_scan_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
