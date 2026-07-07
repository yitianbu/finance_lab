from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass, replace
from datetime import datetime
from pathlib import Path
from typing import Any

from long_term_hold_strategy import LongTermHoldConfig
from scripts.stock_strategy.backtest_long_term_hold_all_a import (
    DEFAULT_STOCK_NAME_OVERRIDES,
    MarketTrendGateConfig,
    PortfolioBacktestConfig,
    _benchmark_return,
    _float_value,
    _write_csv,
    apply_stock_names,
    build_benchmark_trend_gate,
    generate_all_a_events,
    load_stock_name_map,
    simulate_portfolio,
)
from stock_range_trader import DEFAULT_BASE_DIR, load_bars_from_json


@dataclass(frozen=True)
class PeriodCase:
    case: str
    period_start: str
    period_end: str
    benchmark_return: float


@dataclass(frozen=True)
class ParameterCase:
    case: str
    min_rank_score: float
    max_positions: int
    target_weight: float
    max_new_entries_per_day: int


def apply_extra_round_trip_cost(rows: list[dict[str, Any]], extra_round_trip_cost: float) -> list[dict[str, Any]]:
    stressed: list[dict[str, Any]] = []
    for row in rows:
        output = dict(row)
        output["net_return"] = _float_value(output, "net_return") - extra_round_trip_cost
        output["excess_return"] = _float_value(output, "excess_return") - extra_round_trip_cost
        output["extra_round_trip_cost"] = extra_round_trip_cost
        stressed.append(output)
    return stressed


def _summary_row(case: str, summary: dict[str, Any], extra: dict[str, Any] | None = None) -> dict[str, Any]:
    row = {
        "case": case,
        "period_start": summary["period_start"],
        "period_end": summary["period_end"],
        "portfolio_return": summary["portfolio_return"],
        "benchmark_return": summary["benchmark_return"],
        "excess_vs_benchmark": summary["excess_vs_benchmark"],
        "selected_trades": summary["selected_trades"],
        "avg_trade_return": summary["avg_trade_return"],
        "win_rate": summary["win_rate"],
        "profit_factor": summary["profit_factor"],
        "avg_holding_days": summary["avg_holding_days"],
        "capital_time_units": summary["capital_time_units"],
        "capital_time_pnl": summary["capital_time_pnl"],
        "pnl_per_capital_time_unit": summary["pnl_per_capital_time_unit"],
        "annualized_pnl_per_capital_time": summary["annualized_pnl_per_capital_time"],
        "max_drawdown_realized_cost_curve": summary["max_drawdown_realized_cost_curve"],
        "min_rank_score": summary["min_rank_score"],
        "max_positions": summary["max_positions"],
        "target_weight": summary["target_weight"],
        "max_new_entries_per_day": summary["max_new_entries_per_day"],
        "market_gate_blocked_entries": summary.get("market_gate_blocked_entries", 0),
    }
    if extra:
        row.update(extra)
    return row


def run_period_cases(
    events: list[dict[str, Any]],
    base_config: PortfolioBacktestConfig,
    periods: list[PeriodCase],
    extra_round_trip_cost: float = 0.0,
    market_gate: dict[str, bool] | None = None,
) -> list[dict[str, Any]]:
    stressed_events = apply_extra_round_trip_cost(events, extra_round_trip_cost) if extra_round_trip_cost else events
    rows: list[dict[str, Any]] = []
    for period in periods:
        config = replace(base_config, period_start=period.period_start, period_end=period.period_end)
        summary, _selected, _curve = simulate_portfolio(
            stressed_events,
            config,
            benchmark_return=period.benchmark_return,
            market_gate=market_gate,
        )
        rows.append(_summary_row(
            period.case,
            summary,
            {"extra_round_trip_cost": extra_round_trip_cost},
        ))
    return rows


def run_parameter_grid(
    events: list[dict[str, Any]],
    base_config: PortfolioBacktestConfig,
    cases: list[ParameterCase],
    benchmark_return: float,
    extra_round_trip_cost: float = 0.0,
    market_gate: dict[str, bool] | None = None,
) -> list[dict[str, Any]]:
    stressed_events = apply_extra_round_trip_cost(events, extra_round_trip_cost) if extra_round_trip_cost else events
    rows: list[dict[str, Any]] = []
    for case in cases:
        config = replace(
            base_config,
            min_rank_score=case.min_rank_score,
            max_positions=case.max_positions,
            target_weight=case.target_weight,
            max_new_entries_per_day=case.max_new_entries_per_day,
        )
        summary, _selected, _curve = simulate_portfolio(
            stressed_events,
            config,
            benchmark_return=benchmark_return,
            market_gate=market_gate,
        )
        rows.append(_summary_row(
            case.case,
            summary,
            {"extra_round_trip_cost": extra_round_trip_cost},
        ))
    return rows


def default_parameter_cases(
    rank_scores: list[float],
    max_positions_values: list[int],
    target_weights: list[float],
    max_new_entries_values: list[int],
) -> list[ParameterCase]:
    cases: list[ParameterCase] = []
    for min_rank_score in rank_scores:
        for max_positions in max_positions_values:
            for target_weight in target_weights:
                for max_new_entries_per_day in max_new_entries_values:
                    label = (
                        f"rank{min_rank_score:g}_pos{max_positions}_"
                        f"weight{target_weight:g}_new{max_new_entries_per_day}"
                    )
                    cases.append(ParameterCase(
                        case=label,
                        min_rank_score=min_rank_score,
                        max_positions=max_positions,
                        target_weight=target_weight,
                        max_new_entries_per_day=max_new_entries_per_day,
                    ))
    return cases


def build_default_periods(
    period_start: str,
    period_end: str,
    benchmark_bars: list,
) -> list[PeriodCase]:
    cutoffs = [
        ("2024H2", "2024-07-01", "2025-01-01"),
        ("2025H1", "2025-01-01", "2025-07-01"),
        ("2025H2", "2025-07-01", "2026-01-01"),
        ("2026YTD", "2026-01-01", period_end),
        ("1Y_2024_2025", "2024-07-01", "2025-07-01"),
        ("1Y_2025_2026", "2025-07-01", period_end),
        ("full", period_start, period_end),
    ]
    periods: list[PeriodCase] = []
    for label, start, end in cutoffs:
        if start < period_start or end > period_end or start >= end:
            continue
        periods.append(PeriodCase(label, start, end, _benchmark_return(benchmark_bars, start, end)))
    return periods


def run_friction_cases(
    events: list[dict[str, Any]],
    base_config: PortfolioBacktestConfig,
    benchmark_return: float,
    costs: list[float],
    market_gate: dict[str, bool] | None = None,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for cost in costs:
        label = f"extra_cost_{cost:g}"
        rows.extend(run_parameter_grid(
            events,
            base_config,
            [ParameterCase(
                case=label,
                min_rank_score=base_config.min_rank_score,
                max_positions=base_config.max_positions,
                target_weight=base_config.target_weight,
                max_new_entries_per_day=base_config.max_new_entries_per_day,
            )],
            benchmark_return,
            extra_round_trip_cost=cost,
            market_gate=market_gate,
        ))
    return rows


def read_events_csv(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _parse_float_list(raw: str) -> list[float]:
    return [float(item) for item in raw.split(",") if item.strip()]


def _parse_int_list(raw: str) -> list[int]:
    return [int(item) for item in raw.split(",") if item.strip()]


def write_robustness_outputs(
    output_dir: Path,
    summary: dict[str, Any],
    period_rows: list[dict[str, Any]],
    grid_rows: list[dict[str, Any]],
    friction_rows: list[dict[str, Any]],
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(output_dir / "period_summary.csv", period_rows)
    _write_csv(output_dir / "parameter_grid.csv", grid_rows)
    _write_csv(output_dir / "friction_summary.csv", friction_rows)
    (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), "utf-8")

    best_grid = sorted(grid_rows, key=lambda row: _float_value(row, "excess_vs_benchmark"), reverse=True)[:10]
    lines = [
        "# 长期持有策略稳健性验证",
        "",
        f"- Period: {summary['period_start']} to {summary['period_end']}",
        f"- Events: {summary['events']}; period cases: {len(period_rows)}; parameter cases: {len(grid_rows)}; friction cases: {len(friction_rows)}",
        f"- Benchmark return: {summary['benchmark_return']:.2%}",
        f"- Market gate: {summary.get('market_gate', 'off')}",
        "",
        "## Period Cases",
        "",
        "| Case | Period | Return | Benchmark | Excess | Trades | Win Rate | Max DD | Blocked |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in period_rows:
        lines.append(
            f"| {row['case']} | {row['period_start']} to {row['period_end']} | "
            f"{_float_value(row, 'portfolio_return'):.2%} | {_float_value(row, 'benchmark_return'):.2%} | "
            f"{_float_value(row, 'excess_vs_benchmark'):.2%} | {int(_float_value(row, 'selected_trades'))} | "
            f"{_float_value(row, 'win_rate'):.2%} | {_float_value(row, 'max_drawdown_realized_cost_curve'):.2%} | "
            f"{int(_float_value(row, 'market_gate_blocked_entries'))} |"
        )

    lines.extend([
        "",
        "## Top Parameter Cases",
        "",
        "| Case | Return | Excess | Capital-Time Ann. | Trades | Win Rate | Rank | Positions | Weight | New/Day | Cost | Blocked |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ])
    for row in best_grid:
        lines.append(
            f"| {row['case']} | {_float_value(row, 'portfolio_return'):.2%} | "
            f"{_float_value(row, 'excess_vs_benchmark'):.2%} | "
            f"{_float_value(row, 'annualized_pnl_per_capital_time'):.2%} | "
            f"{int(_float_value(row, 'selected_trades'))} | "
            f"{_float_value(row, 'win_rate'):.2%} | {_float_value(row, 'min_rank_score'):.2f} | "
            f"{int(_float_value(row, 'max_positions'))} | {_float_value(row, 'target_weight'):.2%} | "
            f"{int(_float_value(row, 'max_new_entries_per_day'))} | {_float_value(row, 'extra_round_trip_cost'):.2%} | "
            f"{int(_float_value(row, 'market_gate_blocked_entries'))} |"
        )

    lines.extend([
        "",
        "## Friction Cases",
        "",
        "| Extra Round-Trip Cost | Return | Excess | Trades | Win Rate |",
        "|---:|---:|---:|---:|---:|",
    ])
    for row in friction_rows:
        lines.append(
            f"| {_float_value(row, 'extra_round_trip_cost'):.2%} | {_float_value(row, 'portfolio_return'):.2%} | "
            f"{_float_value(row, 'excess_vs_benchmark'):.2%} | {int(_float_value(row, 'selected_trades'))} | "
            f"{_float_value(row, 'win_rate'):.2%} |"
        )
    (output_dir / "robustness_report.md").write_text("\n".join(lines) + "\n", "utf-8")


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate long-term hold all-A robustness across periods, parameters, and costs")
    parser.add_argument("--base-dir", default=str(DEFAULT_BASE_DIR))
    parser.add_argument("--kline-dir", default="data/hold5_tail_proxy/klines")
    parser.add_argument("--benchmark-json", default="data/announcement_backtest/klines/000300.SH.json")
    parser.add_argument("--events-csv", default="")
    parser.add_argument("--period-start", default="2024-07-01")
    parser.add_argument("--period-end", default="")
    parser.add_argument("--max-positions", type=int, default=5)
    parser.add_argument("--max-new-entries-per-day", type=int, default=1)
    parser.add_argument("--target-weight", type=float, default=0.20)
    parser.add_argument("--min-rank-score", type=float, default=102.0)
    parser.add_argument("--initial-capital", type=float, default=1.0)
    parser.add_argument("--rank-scores", default="101,102,103")
    parser.add_argument("--max-positions-grid", default="3,5")
    parser.add_argument("--target-weights", default="0.15,0.20")
    parser.add_argument("--max-new-entries-grid", default="1,2")
    parser.add_argument("--extra-round-trip-costs", default="0,0.001,0.003,0.005")
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
    strategy_config = LongTermHoldConfig()
    benchmark_bars = load_bars_from_json(base_dir / args.benchmark_json, strategy_config.benchmark_code)
    period_end = args.period_end or benchmark_bars[-1].trade_date
    output_dir = Path(args.output_dir) if args.output_dir else (
        base_dir / "reports" / "long_term_hold" / "robustness" / datetime.now().strftime("%Y%m%d_%H%M%S")
    )
    base_config = PortfolioBacktestConfig(
        period_start=args.period_start,
        period_end=period_end,
        max_positions=args.max_positions,
        max_new_entries_per_day=args.max_new_entries_per_day,
        target_weight=args.target_weight,
        min_rank_score=args.min_rank_score,
        initial_capital=args.initial_capital,
    )

    stock_names = dict(DEFAULT_STOCK_NAME_OVERRIDES)
    if args.stock_name_csv:
        stock_names.update(load_stock_name_map(base_dir / args.stock_name_csv))

    if args.events_csv:
        events = read_events_csv(base_dir / args.events_csv)
        stats = {"events_source": args.events_csv}
    else:
        events, stats = generate_all_a_events(base_dir / args.kline_dir, benchmark_bars, strategy_config, base_config)
    events = apply_stock_names(events, stock_names)

    benchmark_return = _benchmark_return(benchmark_bars, base_config.period_start, base_config.period_end)
    market_gate_config = MarketTrendGateConfig(
        ma_length=args.market_gate_ma,
        return_lookback=args.market_gate_return_lookback,
        min_return=args.market_gate_min_return,
    )
    market_gate = build_benchmark_trend_gate(benchmark_bars, market_gate_config) if args.market_gate else None
    periods = build_default_periods(base_config.period_start, base_config.period_end, benchmark_bars)
    period_rows = run_period_cases(events, base_config, periods, market_gate=market_gate)

    parameter_cases = default_parameter_cases(
        rank_scores=_parse_float_list(args.rank_scores),
        max_positions_values=_parse_int_list(args.max_positions_grid),
        target_weights=_parse_float_list(args.target_weights),
        max_new_entries_values=_parse_int_list(args.max_new_entries_grid),
    )
    grid_rows = run_parameter_grid(events, base_config, parameter_cases, benchmark_return, market_gate=market_gate)
    friction_rows = run_friction_cases(
        events,
        base_config,
        benchmark_return,
        _parse_float_list(args.extra_round_trip_costs),
        market_gate=market_gate,
    )

    summary = {
        "period_start": base_config.period_start,
        "period_end": base_config.period_end,
        "benchmark_code": strategy_config.benchmark_code,
        "benchmark_return": benchmark_return,
        "events": len(events),
        "output_dir": str(output_dir),
        "base_config": asdict(base_config),
        "stats": stats,
        "market_gate": (
            f"benchmark close > MA{args.market_gate_ma} and "
            f"{args.market_gate_return_lookback}d return >= {args.market_gate_min_return:.2%}"
            if args.market_gate else "off"
        ),
        "market_gate_config": asdict(market_gate_config),
        "market_gate_allowed_days": sum(1 for allowed in (market_gate or {}).values() if allowed),
    }
    write_robustness_outputs(output_dir, summary, period_rows, grid_rows, friction_rows)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
