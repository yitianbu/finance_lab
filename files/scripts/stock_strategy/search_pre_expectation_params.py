from __future__ import annotations

import json
from pathlib import Path

from pre_expectation_backtest import (
    DEFAULT_BASE_DIR,
    PreExpectationConfig,
    _names_by_code,
    _run_variant,
    build_calendar_proxy_candidates,
    close_by_date,
    load_cached_klines,
)
from announcement_backtest import fetch_predict_events


def main() -> None:
    base_dir = DEFAULT_BASE_DIR
    run_dir = base_dir / "data" / "announcement_backtest"
    kline_dir = run_dir / "klines"
    events = fetch_predict_events(run_dir, refresh=False)
    klines_by_code = load_cached_klines(kline_dir)
    benchmark_by_date = close_by_date(klines_by_code["000300.SH"])
    names_by_code = _names_by_code(events)

    rows = []
    for min5 in (0.02, 0.04, 0.06, 0.08):
        for excess10 in (0.00, 0.02, 0.04):
            for max20 in (0.15, 0.25):
                for stop in (0.04, 0.06):
                    for hold in (3, 5, 10):
                        config = PreExpectationConfig(
                            proxy_hold_days=hold,
                            stop_loss=stop,
                            min_pre_5d_return=min5,
                            min_pre_10d_excess=excess10,
                            max_pre_20d_return=max20,
                            position_size=0.10,
                            max_per_day=5,
                        )
                        candidates = build_calendar_proxy_candidates(
                            klines_by_code,
                            benchmark_by_date,
                            names_by_code,
                            config,
                            "2024-01-01",
                            "2026-06-08",
                        )
                        _selected, _executed, _curve, metrics = _run_variant(candidates, config, kline_dir)
                        if not metrics or metrics["trade_count"] < 80:
                            continue
                        rows.append({
                            "min5": min5,
                            "excess10": excess10,
                            "max20": max20,
                            "stop": stop,
                            "hold": hold,
                            "candidates": len(candidates),
                            **metrics,
                        })

    rows.sort(
        key=lambda row: (
            row.get("excess_vs_hs300") or -9,
            row["total_return"],
            row["max_drawdown"],
            row.get("profit_factor") or 0,
        ),
        reverse=True,
    )
    print(json.dumps(rows[:20], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
