from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from datetime import date, datetime
from pathlib import Path
from typing import Callable

from long_term_hold_strategy import (
    LongTermHoldConfig,
    LongTermHoldResult,
    analyze_long_term_hold,
    write_long_term_hold_outputs,
)
from stock_pool_scanner import PoolCandidate, candidate_from_code, find_kline_cache, load_codes_file
from stock_range_trader import DEFAULT_BASE_DIR, DailyBar, load_daily_bars


BarLoader = Callable[[str], list[DailyBar]]


def load_candidates(codes: str = "", codes_file: str = "", limit: int = 0) -> list[PoolCandidate]:
    candidates: list[PoolCandidate] = []
    if codes:
        candidates.extend(candidate_from_code(item.strip()) for item in codes.split(",") if item.strip())
    if codes_file:
        candidates.extend(load_codes_file(Path(codes_file)))

    deduped: dict[str, PoolCandidate] = {}
    for candidate in candidates:
        if candidate.secucode not in deduped:
            deduped[candidate.secucode] = candidate
    output = list(deduped.values())
    return output[:limit] if limit else output


def scan_with_loader(
    candidates: list[PoolCandidate],
    loader: BarLoader,
    benchmark_bars: list[DailyBar],
    output_dir: Path,
    config: LongTermHoldConfig = LongTermHoldConfig(),
) -> list[LongTermHoldResult]:
    results: list[LongTermHoldResult] = []
    for candidate in candidates:
        try:
            bars = loader(candidate.secucode)
            results.append(analyze_long_term_hold(candidate.secucode, candidate.name, bars, benchmark_bars, config))
        except Exception as exc:
            results.append(
                LongTermHoldResult(
                    secucode=candidate.secucode,
                    name=candidate.name,
                    tradable=False,
                    status="error",
                    reject_reason=f"{type(exc).__name__}: {exc}",
                    rank_score=float("-inf"),
                    benchmark_code=config.benchmark_code,
                )
            )
    results.sort(key=lambda item: (item.tradable, item.rank_score, item.excess_return_120d, item.secucode), reverse=True)
    write_long_term_hold_outputs(output_dir, results, config)
    return results


def build_loader(beg: str, end: str, kline_dir: str = "") -> BarLoader:
    cache_dir = Path(kline_dir) if kline_dir else None

    def loader(secucode: str) -> list[DailyBar]:
        cache_path = find_kline_cache(cache_dir, secucode)
        return load_daily_bars(secucode, beg, end, cache_path)

    return loader


def build_config(args: argparse.Namespace) -> LongTermHoldConfig:
    return LongTermHoldConfig(
        benchmark_code=args.benchmark_code,
        min_history_days=args.min_history_days,
        ma_short=args.ma_short,
        ma_mid=args.ma_mid,
        ma_long=args.ma_long,
        relative_short_lookback=args.relative_short_lookback,
        relative_long_lookback=args.relative_long_lookback,
        min_stock_return_120d=args.min_stock_return_120d,
        min_excess_return_120d=args.min_excess_return_120d,
        min_excess_return_240d=args.min_excess_return_240d,
        max_drawdown_120d=args.max_drawdown_120d,
        max_volatility_120d=args.max_volatility_120d,
        max_distance_ma200=args.max_distance_ma200,
        min_turnover=args.min_turnover,
        max_entry_gap=args.max_entry_gap,
        buy_pullback_pct=args.buy_pullback_pct,
        max_initial_loss=args.max_initial_loss,
        ma200_exit_buffer=args.ma200_exit_buffer,
        min_hold_days=args.min_hold_days,
        relative_exit_lookback=args.relative_exit_lookback,
        max_relative_exit_underperformance=args.max_relative_exit_underperformance,
        trail_start_pct=args.trail_start_pct,
        trailing_stop_pct=args.trailing_stop_pct,
        max_hold_days=args.max_hold_days,
        cooldown_days=args.cooldown_days,
        base_position_size=args.base_position_size,
        round_trip_cost=args.round_trip_cost,
    )


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Scan long-term hold candidates that seek to outperform a benchmark")
    parser.add_argument("--codes", default="", help="Comma separated stock codes")
    parser.add_argument("--codes-file", default="", help="Plain text or CSV stock code file")
    parser.add_argument("--base-dir", default=str(DEFAULT_BASE_DIR))
    parser.add_argument("--beg", default="20240101")
    parser.add_argument("--end", default=date.today().strftime("%Y%m%d"))
    parser.add_argument("--kline-dir", default="", help="Directory with cached K-line JSON files")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--benchmark-code", default="000300.SH")

    parser.add_argument("--min-history-days", type=int, default=260)
    parser.add_argument("--ma-short", type=int, default=60)
    parser.add_argument("--ma-mid", type=int, default=120)
    parser.add_argument("--ma-long", type=int, default=200)
    parser.add_argument("--relative-short-lookback", type=int, default=120)
    parser.add_argument("--relative-long-lookback", type=int, default=240)
    parser.add_argument("--min-stock-return-120d", type=float, default=0.06)
    parser.add_argument("--min-excess-return-120d", type=float, default=0.06)
    parser.add_argument("--min-excess-return-240d", type=float, default=0.08)
    parser.add_argument("--max-drawdown-120d", type=float, default=-0.28)
    parser.add_argument("--max-volatility-120d", type=float, default=0.42)
    parser.add_argument("--max-distance-ma200", type=float, default=0.55)
    parser.add_argument("--min-turnover", type=float, default=0.0)
    parser.add_argument("--max-entry-gap", type=float, default=0.03)
    parser.add_argument("--buy-pullback-pct", type=float, default=0.03)
    parser.add_argument("--max-initial-loss", type=float, default=0.12)
    parser.add_argument("--ma200-exit-buffer", type=float, default=0.03)
    parser.add_argument("--min-hold-days", type=int, default=60)
    parser.add_argument("--relative-exit-lookback", type=int, default=60)
    parser.add_argument("--max-relative-exit-underperformance", type=float, default=-0.06)
    parser.add_argument("--trail-start-pct", type=float, default=0.25)
    parser.add_argument("--trailing-stop-pct", type=float, default=0.15)
    parser.add_argument("--max-hold-days", type=int, default=520)
    parser.add_argument("--cooldown-days", type=int, default=20)
    parser.add_argument("--base-position-size", type=float, default=0.20)
    parser.add_argument("--round-trip-cost", type=float, default=0.0013)
    return parser


def main() -> None:
    args = build_arg_parser().parse_args()
    candidates = load_candidates(args.codes, args.codes_file, args.limit)
    if not candidates:
        raise SystemExit("no candidates provided")

    base_dir = Path(args.base_dir)
    output_dir = base_dir / "reports" / "long_term_hold" / datetime.now().strftime("%Y%m%d_%H%M%S")
    config = build_config(args)
    loader = build_loader(args.beg, args.end, args.kline_dir)
    benchmark_bars = loader(config.benchmark_code)
    results = scan_with_loader(candidates, loader, benchmark_bars, output_dir, config)
    summary = {
        "scanned": len(results),
        "candidates": sum(1 for item in results if item.tradable),
        "benchmark_code": config.benchmark_code,
        "output_dir": str(output_dir),
        "config": asdict(config),
        "top": [asdict(item) for item in results[: min(10, len(results))]],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
