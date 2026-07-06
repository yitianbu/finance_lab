from __future__ import annotations

import argparse
import csv
import json
import math
from bisect import bisect_right
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from long_term_hold_strategy import LongTermHoldConfig, _exit_trade, analyze_long_term_hold
from stock_range_trader import DEFAULT_BASE_DIR, DailyBar, load_bars_from_json, normalize_code


TRADING_DAYS_PER_YEAR = 244

A_SHARE_PREFIXES = {
    "SH": ("600", "601", "603", "605", "688"),
    "SZ": ("000", "001", "002", "003", "300", "301"),
}

DEFAULT_STOCK_NAME_OVERRIDES = {
    "000593.SZ": "德龙汇能",
    "000429.SZ": "粤高速A",
    "002293.SZ": "罗莱生活",
    "002440.SZ": "闰土股份",
    "002817.SZ": "黄山胶囊",
    "002895.SZ": "川恒股份",
    "003008.SZ": "开普检测",
    "300929.SZ": "华骐环保",
    "600039.SH": "四川路桥",
    "600268.SH": "国电南自",
    "600360.SH": "华微电子",
    "600377.SH": "宁沪高速",
    "601088.SH": "中国神华",
    "601991.SH": "大唐发电",
    "688367.SH": "工大高科",
}


@dataclass(frozen=True)
class PortfolioBacktestConfig:
    period_start: str
    period_end: str
    max_positions: int = 5
    max_new_entries_per_day: int = 1
    target_weight: float = 0.20
    min_rank_score: float = 102.0
    initial_capital: float = 1.0


@dataclass(frozen=True)
class MarketTrendGateConfig:
    ma_length: int = 120
    return_lookback: int = 60
    min_return: float = 0.0


def is_a_share_stock_code(raw_code: str) -> bool:
    try:
        code = normalize_code(raw_code)
    except ValueError:
        return False
    stock_code, suffix = code.split(".")
    return suffix in A_SHARE_PREFIXES and stock_code.startswith(A_SHARE_PREFIXES[suffix])


def _float_value(row: dict[str, Any], key: str, default: float = 0.0) -> float:
    try:
        return float(row.get(key, default))
    except (TypeError, ValueError):
        return default


def _int_value(row: dict[str, Any], key: str, default: int = 0) -> int:
    try:
        return int(float(row.get(key, default)))
    except (TypeError, ValueError):
        return default


def _typed_event(row: dict[str, Any]) -> dict[str, Any]:
    output = dict(row)
    for key in (
        "benchmark_return",
        "drawdown_120d",
        "entry_price",
        "excess_return",
        "excess_return_120d",
        "excess_return_240d",
        "exit_price",
        "gross_return",
        "net_return",
        "rank_score",
        "signal_score",
        "stock_return_120d",
        "volatility_120d",
    ):
        if key in output:
            output[key] = _float_value(output, key)
    output["holding_days"] = _int_value(output, "holding_days", 0)
    return output


def load_stock_name_map(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}

    names: dict[str, str] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            raw_code = (
                row.get("secucode")
                or row.get("SECUCODE")
                or row.get("code")
                or row.get("SECURITY_CODE")
                or ""
            )
            raw_name = row.get("name") or row.get("SECURITY_NAME_ABBR") or row.get("stock_name") or ""
            if not raw_code or not raw_name:
                continue
            try:
                names[normalize_code(raw_code)] = str(raw_name)
            except ValueError:
                continue
    return names


def apply_stock_names(rows: list[dict[str, Any]], stock_names: dict[str, str]) -> list[dict[str, Any]]:
    annotated: list[dict[str, Any]] = []
    for row in rows:
        output = dict(row)
        secucode = str(output.get("secucode") or "")
        output["name"] = str(output.get("name") or stock_names.get(secucode, ""))
        annotated.append(output)
    return annotated


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def build_benchmark_trend_gate(
    benchmark_bars: list[DailyBar],
    config: MarketTrendGateConfig,
) -> dict[str, bool]:
    closes = [bar.close for bar in benchmark_bars]
    prefix = [0.0]
    for close in closes:
        prefix.append(prefix[-1] + close)

    gate: dict[str, bool] = {}
    required = config.ma_length + config.return_lookback
    for idx, bar in enumerate(benchmark_bars):
        if idx + 1 < required or idx - config.return_lookback < 0:
            gate[bar.trade_date] = False
            continue
        ma = _ma(prefix, idx, config.ma_length)
        lookback_close = closes[idx - config.return_lookback]
        trailing_return = bar.close / lookback_close - 1.0 if lookback_close > 0 else 0.0
        gate[bar.trade_date] = ma > 0 and bar.close > ma and trailing_return >= config.min_return
    return gate


def _portfolio_summary(
    selected: list[dict[str, Any]],
    equity_curve: list[dict[str, Any]],
    final_equity: float,
    config: PortfolioBacktestConfig,
    benchmark_return: float = 0.0,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    returns = [_float_value(row, "net_return") for row in selected]
    weighted_pnl = [_float_value(row, "notional") * _float_value(row, "net_return") for row in selected]
    capital_time_units = sum(
        _float_value(row, "notional") * _float_value(row, "holding_days")
        for row in selected
    )
    capital_time_pnl = sum(weighted_pnl)
    pnl_per_capital_time_unit = (
        capital_time_pnl / capital_time_units if capital_time_units > 0 else 0.0
    )
    profit = sum(item for item in weighted_pnl if item > 0)
    loss = -sum(item for item in weighted_pnl if item < 0)
    profit_factor: float | str = profit / loss if loss > 0 else ("inf" if profit > 0 else 0.0)

    peak = config.initial_capital
    max_drawdown = 0.0
    for point in equity_curve:
        equity = _float_value(point, "equity_at_cost")
        peak = max(peak, equity)
        max_drawdown = min(max_drawdown, equity / peak - 1.0 if peak > 0 else 0.0)

    summary = {
        "period_start": config.period_start,
        "period_end": config.period_end,
        "selected_trades": len(selected),
        "initial_capital": config.initial_capital,
        "final_equity": final_equity,
        "portfolio_return": final_equity / config.initial_capital - 1.0 if config.initial_capital > 0 else 0.0,
        "benchmark_return": benchmark_return,
        "excess_vs_benchmark": (
            final_equity / config.initial_capital - 1.0 - benchmark_return if config.initial_capital > 0 else 0.0
        ),
        "avg_trade_return": _mean(returns),
        "win_rate": sum(1 for item in returns if item > 0) / len(returns) if returns else 0.0,
        "profit_factor": profit_factor,
        "avg_holding_days": _mean([_float_value(row, "holding_days") for row in selected]),
        "capital_time_units": capital_time_units,
        "capital_time_pnl": capital_time_pnl,
        "pnl_per_capital_time_unit": pnl_per_capital_time_unit,
        "annualized_pnl_per_capital_time": pnl_per_capital_time_unit * TRADING_DAYS_PER_YEAR,
        "max_drawdown_realized_cost_curve": max_drawdown,
        "max_positions": config.max_positions,
        "max_new_entries_per_day": config.max_new_entries_per_day,
        "target_weight": config.target_weight,
        "min_rank_score": config.min_rank_score,
    }
    if extra:
        summary.update(extra)
    return summary


def simulate_portfolio(
    events: list[dict[str, Any]],
    config: PortfolioBacktestConfig,
    benchmark_return: float = 0.0,
    extra_summary: dict[str, Any] | None = None,
    market_gate: dict[str, bool] | None = None,
) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]]]:
    filtered_events = [
        _typed_event(event)
        for event in events
        if config.period_start <= str(event.get("entry_date", "")) < config.period_end
        and _float_value(event, "rank_score") >= config.min_rank_score
    ]
    filtered_events.sort(
        key=lambda row: (
            str(row.get("entry_date", "")),
            -_float_value(row, "rank_score"),
            -_float_value(row, "excess_return_120d"),
            -_float_value(row, "excess_return_240d"),
            str(row.get("secucode", "")),
        )
    )

    entries_by_date: dict[str, list[dict[str, Any]]] = {}
    calendar = {config.period_start, config.period_end}
    for event in filtered_events:
        entries_by_date.setdefault(str(event["entry_date"]), []).append(event)
        calendar.add(str(event["entry_date"]))
        calendar.add(str(event["exit_date"]))

    cash = config.initial_capital
    open_positions: list[dict[str, Any]] = []
    selected: list[dict[str, Any]] = []
    equity_curve: list[dict[str, Any]] = []
    market_gate_blocked_entries = 0

    for current_date in sorted(calendar):
        remaining: list[dict[str, Any]] = []
        for position in open_positions:
            if str(position["exit_date"]) <= current_date:
                cash += _float_value(position, "notional") * (1.0 + _float_value(position, "net_return"))
                selected.append(position)
            else:
                remaining.append(position)
        open_positions = remaining

        todays_events = sorted(
            entries_by_date.get(current_date, []),
            key=lambda row: (
                -_float_value(row, "rank_score"),
                -_float_value(row, "excess_return_120d"),
                -_float_value(row, "excess_return_240d"),
                str(row.get("secucode", "")),
            ),
        )
        held_codes = {str(position.get("secucode", "")) for position in open_positions}
        new_count = 0
        if market_gate is not None and todays_events and not market_gate.get(current_date, False):
            market_gate_blocked_entries += len(todays_events)
            todays_events = []
        for event in todays_events:
            if new_count >= config.max_new_entries_per_day or len(open_positions) >= config.max_positions:
                break
            if str(event.get("secucode", "")) in held_codes:
                continue
            equity_now = cash + sum(_float_value(position, "notional") for position in open_positions)
            notional = min(cash, equity_now * config.target_weight)
            if notional <= 1e-12:
                break
            position = dict(event)
            position["notional"] = notional
            cash -= notional
            open_positions.append(position)
            held_codes.add(str(position.get("secucode", "")))
            new_count += 1

        equity_curve.append({
            "date": current_date,
            "cash": cash,
            "open_positions": len(open_positions),
            "equity_at_cost": cash + sum(_float_value(position, "notional") for position in open_positions),
        })

    for position in open_positions:
        cash += _float_value(position, "notional") * (1.0 + _float_value(position, "net_return"))
        selected.append(position)

    summary_extra = dict(extra_summary or {})
    summary_extra["market_gate_blocked_entries"] = market_gate_blocked_entries
    summary = _portfolio_summary(selected, equity_curve, cash, config, benchmark_return, summary_extra)
    return summary, selected, equity_curve


def _benchmark_close_on_or_before(benchmark_bars: list[DailyBar], trade_date: str) -> float:
    dates = [bar.trade_date for bar in benchmark_bars]
    idx = bisect_right(dates, trade_date) - 1
    return benchmark_bars[idx].close if idx >= 0 else 0.0


def _benchmark_return(benchmark_bars: list[DailyBar], start_date: str, end_date: str) -> float:
    start = _benchmark_close_on_or_before(benchmark_bars, start_date)
    end = _benchmark_close_on_or_before(benchmark_bars, end_date)
    return end / start - 1.0 if start > 0 and end > 0 else 0.0


def _stock_return(closes: list[float], idx: int, lookback: int) -> float:
    if idx - lookback < 0 or closes[idx - lookback] <= 0:
        return 0.0
    return closes[idx] / closes[idx - lookback] - 1.0


def _annualized_volatility(closes: list[float], idx: int, length: int) -> float:
    start = max(1, idx - length + 1)
    returns = [closes[item] / closes[item - 1] - 1.0 for item in range(start, idx + 1) if closes[item - 1] > 0]
    if len(returns) < 2:
        return 0.0
    avg = _mean(returns)
    return math.sqrt(_mean([(item - avg) ** 2 for item in returns])) * math.sqrt(244)


def _ma(prefix: list[float], idx: int, length: int) -> float:
    if idx + 1 < length:
        return 0.0
    return (prefix[idx + 1] - prefix[idx + 1 - length]) / length


def _quick_pass(
    bars: list[DailyBar],
    closes: list[float],
    highs: list[float],
    prefix: list[float],
    idx: int,
    benchmark_bars: list[DailyBar],
    strategy_config: LongTermHoldConfig,
) -> bool:
    latest = bars[idx]
    ma60 = _ma(prefix, idx, strategy_config.ma_short)
    ma120 = _ma(prefix, idx, strategy_config.ma_mid)
    ma200 = _ma(prefix, idx, strategy_config.ma_long)
    if ma200 <= 0 or latest.close <= ma200 or ma60 <= ma120 or ma120 <= ma200:
        return False

    return_120d = _stock_return(closes, idx, strategy_config.relative_short_lookback)
    return_240d = _stock_return(closes, idx, strategy_config.relative_long_lookback)
    if return_120d < strategy_config.min_stock_return_120d:
        return False

    excess_120d = return_120d - _benchmark_return(
        benchmark_bars,
        bars[idx - strategy_config.relative_short_lookback].trade_date,
        latest.trade_date,
    )
    excess_240d = return_240d - _benchmark_return(
        benchmark_bars,
        bars[idx - strategy_config.relative_long_lookback].trade_date,
        latest.trade_date,
    )
    if excess_120d < strategy_config.min_excess_return_120d or excess_240d < strategy_config.min_excess_return_240d:
        return False

    recent_high = max(highs[max(0, idx - strategy_config.relative_short_lookback + 1): idx + 1])
    drawdown = latest.close / recent_high - 1.0 if recent_high > 0 else 0.0
    if drawdown < strategy_config.max_drawdown_120d:
        return False
    if _annualized_volatility(closes, idx, strategy_config.relative_short_lookback) > strategy_config.max_volatility_120d:
        return False

    distance_ma200 = latest.close / ma200 - 1.0
    return distance_ma200 <= strategy_config.max_distance_ma200


def generate_all_a_events(
    kline_dir: Path,
    benchmark_bars: list[DailyBar],
    strategy_config: LongTermHoldConfig,
    portfolio_config: PortfolioBacktestConfig,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    required = max(
        strategy_config.min_history_days,
        strategy_config.ma_long + 1,
        strategy_config.relative_long_lookback + 1,
    )
    events: list[dict[str, Any]] = []
    stats = {
        "files": 0,
        "a_share_files": 0,
        "loaded_stocks": 0,
        "eligible_history_stocks": 0,
        "raw_signals": 0,
        "entry_valid_events": 0,
        "errors": 0,
    }

    for path in sorted(kline_dir.glob("*.json")):
        stats["files"] += 1
        raw_code = path.stem.replace("_", ".")
        if not is_a_share_stock_code(raw_code):
            continue
        stats["a_share_files"] += 1
        try:
            secucode = normalize_code(raw_code)
            bars = [bar for bar in load_bars_from_json(path, secucode) if bar.trade_date <= portfolio_config.period_end]
        except Exception:
            stats["errors"] += 1
            continue
        if len(bars) < required + 1:
            continue

        stats["loaded_stocks"] += 1
        dates = [bar.trade_date for bar in bars]
        closes = [bar.close for bar in bars]
        highs = [bar.high for bar in bars]
        prefix = [0.0]
        for close in closes:
            prefix.append(prefix[-1] + close)

        period_start_idx = max(0, bisect_right(dates, portfolio_config.period_start) - 1)
        signal_idx = max(required - 1, period_start_idx)
        end_idx = len(bars) - 1
        if signal_idx >= end_idx:
            continue
        stats["eligible_history_stocks"] += 1

        for idx in range(signal_idx, end_idx):
            entry_idx = idx + 1
            if bars[entry_idx].trade_date < portfolio_config.period_start or bars[entry_idx].trade_date >= portfolio_config.period_end:
                continue
            if not _quick_pass(bars, closes, highs, prefix, idx, benchmark_bars, strategy_config):
                continue
            signal = analyze_long_term_hold(secucode, "", bars[: idx + 1], benchmark_bars, strategy_config)
            if not signal.tradable:
                continue
            stats["raw_signals"] += 1
            trade = _exit_trade(secucode, signal, bars, benchmark_bars, entry_idx, strategy_config)
            if trade is None:
                continue
            row = asdict(trade)
            row.update({
                "rank_score": signal.rank_score,
                "excess_return_120d": signal.excess_return_120d,
                "excess_return_240d": signal.excess_return_240d,
                "stock_return_120d": signal.stock_return_120d,
                "drawdown_120d": signal.drawdown_120d,
                "volatility_120d": signal.volatility_120d,
            })
            events.append(row)
            stats["entry_valid_events"] += 1

    return events, stats


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = sorted(set().union(*(row.keys() for row in rows))) if rows else ["secucode"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_outputs(
    output_dir: Path,
    summary: dict[str, Any],
    events: list[dict[str, Any]],
    selected: list[dict[str, Any]],
    equity_curve: list[dict[str, Any]],
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(output_dir / "all_a_stock_long_term_hold_events.csv", events)
    _write_csv(output_dir / "all_a_stock_long_term_hold_trades.csv", selected)
    _write_csv(output_dir / "equity_curve.csv", equity_curve)
    (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), "utf-8")

    lines = [
        "# 全A股票长期持有跑赢大盘策略回测",
        "",
        f"- Period: {summary['period_start']} to {summary['period_end']}",
        f"- A-share stock files: {summary.get('a_share_files')}; loaded: {summary.get('loaded_stocks')}; eligible history: {summary.get('eligible_history_stocks')}",
        f"- Raw signals: {summary.get('raw_signals')}; entry-valid events: {summary.get('entry_valid_events')}; selected trades: {summary['selected_trades']}",
        f"- Portfolio return: {summary['portfolio_return']:.2%}; benchmark: {summary['benchmark_return']:.2%}; excess: {summary['excess_vs_benchmark']:.2%}",
        f"- Avg trade return: {summary['avg_trade_return']:.2%}; win rate: {summary['win_rate']:.2%}; profit factor: {summary['profit_factor']}",
        f"- Execution: max {summary['max_new_entries_per_day']} new entry per day, max {summary['max_positions']} positions, rank >= {summary['min_rank_score']:.2f}",
        f"- Market gate: {summary.get('market_gate', 'off')}; blocked entries: {int(_float_value(summary, 'market_gate_blocked_entries'))}",
    ]
    stock_names = [str(row.get("name") or row.get("secucode") or "") for row in selected]
    if stock_names:
        lines.append(f"- Stock names: {'、'.join(stock_names)}")
    lines.extend([
        "",
        "## Selected Trades",
        "",
        "| Code | Name | Entry | Exit | Net Return | Benchmark | Excess | Holding | Reason | Notional |",
        "|---|---|---|---|---:|---:|---:|---:|---|---:|",
    ])
    for row in selected:
        lines.append(
            f"| {row['secucode']} | {row.get('name', '')} | {row['entry_date']} @ {_float_value(row, 'entry_price'):.2f} | "
            f"{row['exit_date']} @ {_float_value(row, 'exit_price'):.2f} | {_float_value(row, 'net_return'):.2%} | "
            f"{_float_value(row, 'benchmark_return'):.2%} | {_float_value(row, 'excess_return'):.2%} | "
            f"{_int_value(row, 'holding_days')} | {row['exit_reason']} | {_float_value(row, 'notional'):.4f} |"
        )
    (output_dir / "report.md").write_text("\n".join(lines) + "\n", "utf-8")


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Backtest long-term hold strategy across cached A-share stocks")
    parser.add_argument("--base-dir", default=str(DEFAULT_BASE_DIR))
    parser.add_argument("--kline-dir", default="data/hold5_tail_proxy/klines")
    parser.add_argument("--benchmark-json", default="data/announcement_backtest/klines/000300.SH.json")
    parser.add_argument("--period-start", default="2025-07-02")
    parser.add_argument("--period-end", default="2026-07-01")
    parser.add_argument("--max-positions", type=int, default=5)
    parser.add_argument("--max-new-entries-per-day", type=int, default=1)
    parser.add_argument("--target-weight", type=float, default=0.20)
    parser.add_argument("--min-rank-score", type=float, default=102.0)
    parser.add_argument("--initial-capital", type=float, default=1.0)
    parser.add_argument("--market-gate", action="store_true")
    parser.add_argument("--market-gate-ma", type=int, default=120)
    parser.add_argument("--market-gate-return-lookback", type=int, default=60)
    parser.add_argument("--market-gate-min-return", type=float, default=0.0)
    parser.add_argument("--stock-name-csv", default="")
    parser.add_argument("--output-dir", default="")
    return parser


def main() -> None:
    args = build_arg_parser().parse_args()
    base_dir = Path(args.base_dir)
    output_dir = Path(args.output_dir) if args.output_dir else (
        base_dir / "reports" / "long_term_hold" / f"all_a_stock_backtest_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    )
    portfolio_config = PortfolioBacktestConfig(
        period_start=args.period_start,
        period_end=args.period_end,
        max_positions=args.max_positions,
        max_new_entries_per_day=args.max_new_entries_per_day,
        target_weight=args.target_weight,
        min_rank_score=args.min_rank_score,
        initial_capital=args.initial_capital,
    )
    strategy_config = LongTermHoldConfig()
    benchmark_bars = [
        bar
        for bar in load_bars_from_json(base_dir / args.benchmark_json, strategy_config.benchmark_code)
        if bar.trade_date <= portfolio_config.period_end
    ]
    stock_names = dict(DEFAULT_STOCK_NAME_OVERRIDES)
    if args.stock_name_csv:
        stock_names.update(load_stock_name_map(base_dir / args.stock_name_csv))

    events, stats = generate_all_a_events(base_dir / args.kline_dir, benchmark_bars, strategy_config, portfolio_config)
    events = apply_stock_names(events, stock_names)
    benchmark_return = _benchmark_return(benchmark_bars, portfolio_config.period_start, portfolio_config.period_end)
    market_gate_config = MarketTrendGateConfig(
        ma_length=args.market_gate_ma,
        return_lookback=args.market_gate_return_lookback,
        min_return=args.market_gate_min_return,
    )
    market_gate = build_benchmark_trend_gate(benchmark_bars, market_gate_config) if args.market_gate else None
    summary, selected, equity_curve = simulate_portfolio(
        events,
        portfolio_config,
        benchmark_return=benchmark_return,
        extra_summary=stats,
        market_gate=market_gate,
    )
    selected = apply_stock_names(selected, stock_names)
    summary["benchmark_code"] = strategy_config.benchmark_code
    summary["output_dir"] = str(output_dir)
    summary["market_gate"] = (
        f"benchmark close > MA{args.market_gate_ma} and "
        f"{args.market_gate_return_lookback}d return >= {args.market_gate_min_return:.2%}"
        if args.market_gate else "off"
    )
    summary["market_gate_config"] = asdict(market_gate_config)
    summary["market_gate_allowed_days"] = sum(1 for allowed in (market_gate or {}).values() if allowed)
    write_outputs(output_dir, summary, events, selected, equity_curve)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
