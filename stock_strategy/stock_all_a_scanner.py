from __future__ import annotations

import argparse
import csv
import json
import math
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from stock_pool_scanner import PoolCandidate, PoolScanConfig, evaluate_summary, write_pool_outputs
from stock_range_trader import (
    DEFAULT_BASE_DIR,
    PredictionConfig,
    backtest_predictions,
    backtest_trade_rules,
    calibrated_band,
    calibrate_atr_multiplier,
    fetch_tencent_payload,
    make_trade_plan,
    parse_tencent_payload,
    predict_next_range,
)


DEFAULT_EVENTS_CSV = DEFAULT_BASE_DIR / "reports" / "announcement_backtest" / "all_scored_events.csv"


@dataclass(frozen=True)
class FullMarketScanStats:
    scanned_candidates: int
    ok_results: int
    errors: int
    tradable: int
    output_dir: str


def load_candidates_from_events(path: Path, limit: int | None = None) -> list[PoolCandidate]:
    seen: set[str] = set()
    candidates: list[PoolCandidate] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            secucode = str(row.get("SECUCODE") or row.get("secucode") or "")
            name = str(row.get("SECURITY_NAME_ABBR") or row.get("name") or "")
            if not secucode.endswith((".SZ", ".SH")):
                continue
            if secucode in seen:
                continue
            if "ST" in name.upper() or "退" in name:
                continue
            seen.add(secucode)
            candidates.append(PoolCandidate(secucode=secucode, name=name, source="all_a_events"))
            if limit and len(candidates) >= limit:
                break
    return candidates


def analyze_candidate(candidate: PoolCandidate, range_config: PredictionConfig, target_count: int) -> dict[str, Any]:
    bars = parse_tencent_payload(
        candidate.secucode,
        fetch_tencent_payload(candidate.secucode, count=520, timeout=20),
    )
    if len(bars) < max(180, range_config.history_window + target_count + 5):
        raise ValueError(f"not enough bars: {len(bars)}")

    latest_idx = len(bars) - 1
    latest_bar = bars[latest_idx]
    prediction = predict_next_range(bars, latest_idx, range_config)
    calibration = calibrate_atr_multiplier(bars, latest_idx, range_config, target_count)
    prediction = calibrated_band(prediction, calibration)
    plan = make_trade_plan(prediction, calibration, range_config)
    prediction_metrics, _ = backtest_predictions(bars, range_config, target_count)
    trade_metrics, _ = backtest_trade_rules(bars, range_config, target_count)

    return {
        "code": candidate.secucode,
        "latest_bar": asdict(latest_bar),
        "prediction": asdict(prediction),
        "calibration": asdict(calibration),
        "trade_plan": asdict(plan),
        "prediction_metrics": prediction_metrics,
        "trade_metrics": trade_metrics,
        "output_dir": "",
    }


def run_full_market_scan(
    candidates: list[PoolCandidate],
    output_dir: Path,
    range_config: PredictionConfig,
    scan_config: PoolScanConfig,
    target_count: int,
    workers: int,
) -> FullMarketScanStats:
    results = []
    errors = 0
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(analyze_candidate, candidate, range_config, target_count): candidate
            for candidate in candidates
        }
        for index, future in enumerate(as_completed(futures), start=1):
            candidate = futures[future]
            try:
                results.append(evaluate_summary(candidate, future.result(), scan_config))
            except Exception as exc:
                errors += 1
                if errors <= 20:
                    print("ERR", candidate.secucode, type(exc).__name__, str(exc)[:120])
            if index % 100 == 0:
                tradable = sum(1 for item in results if item.tradable)
                print(
                    "progress",
                    index,
                    "of",
                    len(candidates),
                    "ok",
                    len(results),
                    "tradable",
                    tradable,
                    "errors",
                    errors,
                    flush=True,
                )

    results.sort(key=lambda item: (item.tradable, item.rank_score, item.secucode), reverse=True)
    write_pool_outputs(output_dir, results, scan_config)
    stats = FullMarketScanStats(
        scanned_candidates=len(candidates),
        ok_results=len(results),
        errors=errors,
        tradable=sum(1 for item in results if item.tradable),
        output_dir=str(output_dir),
    )
    summary = {
        **asdict(stats),
        "top": [asdict(item) for item in results[:20]],
    }
    (output_dir / "full_market_scan_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return stats


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Full A-share next-day range scan")
    parser.add_argument("--base-dir", default=str(DEFAULT_BASE_DIR))
    parser.add_argument("--events-csv", default=str(DEFAULT_EVENTS_CSV))
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--workers", type=int, default=24)
    parser.add_argument("--target-count", type=int, default=90)
    parser.add_argument("--history-window", type=int, default=90)
    parser.add_argument("--similar-count", type=int, default=15)
    parser.add_argument("--target-coverage", type=float, default=0.80)
    parser.add_argument("--min-reward-risk", type=float, default=1.8)
    parser.add_argument("--min-trades", type=int, default=5)
    parser.add_argument("--min-total-return", type=float, default=0.0)
    parser.add_argument("--max-drawdown", type=float, default=-0.08)
    parser.add_argument("--min-band-coverage", type=float, default=0.75)
    return parser


def main() -> None:
    args = build_arg_parser().parse_args()
    base_dir = Path(args.base_dir)
    candidates = load_candidates_from_events(Path(args.events_csv), args.limit or None)
    if not candidates:
        raise SystemExit("no candidates loaded")

    range_config = PredictionConfig(
        history_window=args.history_window,
        similar_count=args.similar_count,
        target_coverage=args.target_coverage,
        min_reward_risk=args.min_reward_risk,
    )
    scan_config = PoolScanConfig(
        min_trades=args.min_trades,
        min_total_return=args.min_total_return,
        max_drawdown=args.max_drawdown,
        min_band_coverage=args.min_band_coverage,
        max_results=100,
    )
    output_dir = base_dir / "reports" / "range_trader" / "all_a_scan" / datetime.now().strftime("%Y%m%d_%H%M%S")
    run_full_market_scan(
        candidates=candidates,
        output_dir=output_dir,
        range_config=range_config,
        scan_config=scan_config,
        target_count=args.target_count,
        workers=max(1, args.workers),
    )


if __name__ == "__main__":
    main()
