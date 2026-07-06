import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.stock_strategy.backtest_long_term_hold_all_a import (
    MarketTrendGateConfig,
    PortfolioBacktestConfig,
    apply_stock_names,
    build_arg_parser,
    build_benchmark_trend_gate,
    is_a_share_stock_code,
    simulate_portfolio,
    write_outputs,
)
from stock_range_trader import DailyBar


def event(
    secucode: str,
    entry_date: str,
    exit_date: str,
    net_return: float,
    rank_score: float,
    excess_return_120d: float = 0.20,
    excess_return_240d: float = 0.30,
) -> dict:
    return {
        "secucode": secucode,
        "signal_date": entry_date,
        "entry_date": entry_date,
        "exit_date": exit_date,
        "entry_price": 10.0,
        "exit_price": 10.0 * (1.0 + net_return),
        "net_return": net_return,
        "benchmark_return": 0.0,
        "excess_return": net_return,
        "exit_reason": "test",
        "holding_days": 5,
        "rank_score": rank_score,
        "excess_return_120d": excess_return_120d,
        "excess_return_240d": excess_return_240d,
    }


def bar(trade_date: str, close: float) -> DailyBar:
    return DailyBar(
        trade_date=trade_date,
        open=close,
        close=close,
        high=close,
        low=close,
        volume=1_000_000,
        amount=10_000_000,
        pct_change=0.0,
        turnover=1.0,
    )


class BacktestLongTermHoldAllATests(unittest.TestCase):
    def test_a_share_filter_excludes_indexes_and_non_stock_codes(self):
        self.assertTrue(is_a_share_stock_code("600268.SH"))
        self.assertTrue(is_a_share_stock_code("002817.SZ"))
        self.assertTrue(is_a_share_stock_code("301512.SZ"))

        self.assertFalse(is_a_share_stock_code("399001.SZ"))
        self.assertFalse(is_a_share_stock_code("399006.SZ"))
        self.assertFalse(is_a_share_stock_code("000300.SH"))
        self.assertFalse(is_a_share_stock_code("510300.SH"))

    def test_simulation_takes_only_highest_ranked_signal_per_day(self):
        config = PortfolioBacktestConfig(
            period_start="2026-01-01",
            period_end="2026-02-01",
            max_positions=5,
            max_new_entries_per_day=1,
            target_weight=0.20,
            min_rank_score=0.0,
        )
        events = [
            event("600001.SH", "2026-01-02", "2026-01-10", 0.10, 99.0),
            event("600002.SH", "2026-01-02", "2026-01-10", 0.30, 103.0),
            event("600003.SH", "2026-01-03", "2026-01-10", 0.20, 100.0),
        ]

        summary, selected, _curve = simulate_portfolio(events, config)

        self.assertEqual([row["secucode"] for row in selected], ["600002.SH", "600003.SH"])
        self.assertEqual(summary["selected_trades"], 2)
        self.assertGreater(summary["portfolio_return"], 0.0)

    def test_simulation_applies_high_conviction_rank_floor(self):
        config = PortfolioBacktestConfig(
            period_start="2026-01-01",
            period_end="2026-02-01",
            max_positions=5,
            max_new_entries_per_day=1,
            target_weight=0.20,
            min_rank_score=102.0,
        )
        events = [
            event("600001.SH", "2026-01-02", "2026-01-10", 0.40, 101.9),
            event("600002.SH", "2026-01-03", "2026-01-10", 0.10, 102.1),
        ]

        summary, selected, _curve = simulate_portfolio(events, config)

        self.assertEqual([row["secucode"] for row in selected], ["600002.SH"])
        self.assertEqual(summary["selected_trades"], 1)

    def test_simulation_reports_capital_time_efficiency(self):
        config = PortfolioBacktestConfig(
            period_start="2026-01-01",
            period_end="2026-02-01",
            max_positions=5,
            max_new_entries_per_day=1,
            target_weight=0.20,
            min_rank_score=0.0,
        )
        events = [event("600001.SH", "2026-01-02", "2026-01-10", 0.10, 103.0)]

        summary, selected, _curve = simulate_portfolio(events, config)

        self.assertEqual(len(selected), 1)
        self.assertAlmostEqual(summary["capital_time_units"], 1.0)
        self.assertAlmostEqual(summary["capital_time_pnl"], 0.02)
        self.assertAlmostEqual(summary["pnl_per_capital_time_unit"], 0.02)
        self.assertAlmostEqual(summary["annualized_pnl_per_capital_time"], 4.88)

    def test_simulation_blocks_new_entries_when_market_gate_is_closed(self):
        config = PortfolioBacktestConfig(
            period_start="2026-01-01",
            period_end="2026-02-01",
            max_positions=5,
            max_new_entries_per_day=1,
            target_weight=0.20,
            min_rank_score=0.0,
        )
        events = [
            event("600001.SH", "2026-01-02", "2026-01-10", 0.10, 103.0),
            event("600002.SH", "2026-01-03", "2026-01-10", 0.20, 103.0),
        ]

        summary, selected, _curve = simulate_portfolio(
            events,
            config,
            market_gate={"2026-01-02": False, "2026-01-03": True},
        )

        self.assertEqual([row["secucode"] for row in selected], ["600002.SH"])
        self.assertEqual(summary["selected_trades"], 1)
        self.assertEqual(summary["market_gate_blocked_entries"], 1)

    def test_simulation_can_use_dynamic_position_tiers(self):
        config = PortfolioBacktestConfig(
            period_start="2026-01-01",
            period_end="2026-02-01",
            max_positions=5,
            max_new_entries_per_day=3,
            target_weight=0.20,
            min_rank_score=102.5,
            dynamic_position_sizing=True,
        )
        events = [
            event("600001.SH", "2026-01-02", "2026-01-10", 0.10, 102.6),
            event("600002.SH", "2026-01-03", "2026-01-10", 0.10, 103.2),
            {
                **event("600003.SH", "2026-01-04", "2026-01-10", 0.10, 104.2),
                "volatility_120d": 0.30,
                "drawdown_120d": -0.03,
            },
        ]

        _summary, selected, _curve = simulate_portfolio(events, config)

        notionals = {row["secucode"]: row["notional"] for row in selected}
        self.assertAlmostEqual(notionals["600001.SH"], 0.20)
        self.assertAlmostEqual(notionals["600002.SH"], 0.25)
        self.assertAlmostEqual(notionals["600003.SH"], 0.30)

    def test_parser_defaults_to_low_risk_high_return_profile(self):
        args = build_arg_parser().parse_args([])

        self.assertTrue(args.market_gate)
        self.assertEqual(args.market_gate_min_return, 0.02)
        self.assertEqual(args.min_rank_score, 102.5)
        self.assertEqual(args.max_positions, 5)
        self.assertEqual(args.max_new_entries_per_day, 2)
        self.assertEqual(args.target_weight, 0.20)
        self.assertTrue(args.dynamic_position_sizing)

    def test_benchmark_trend_gate_requires_price_above_ma_and_positive_return(self):
        bars = [
            bar("2026-01-01", 10.0),
            bar("2026-01-02", 10.5),
            bar("2026-01-03", 11.0),
            bar("2026-01-04", 10.2),
            bar("2026-01-05", 9.5),
            bar("2026-01-06", 12.0),
        ]
        gate_config = MarketTrendGateConfig(ma_length=3, return_lookback=2, min_return=0.0)

        gate = build_benchmark_trend_gate(bars, gate_config)

        self.assertFalse(gate["2026-01-03"])
        self.assertFalse(gate["2026-01-05"])
        self.assertTrue(gate["2026-01-06"])

    def test_parser_accepts_market_gate_options(self):
        args = build_arg_parser().parse_args([
            "--market-gate",
            "--market-gate-ma",
            "120",
            "--market-gate-return-lookback",
            "60",
            "--market-gate-min-return",
            "0.01",
        ])

        self.assertTrue(args.market_gate)
        self.assertEqual(args.market_gate_ma, 120)
        self.assertEqual(args.market_gate_return_lookback, 60)
        self.assertEqual(args.market_gate_min_return, 0.01)

    def test_outputs_include_stock_names_when_name_map_is_available(self):
        rows = [event("600268.SH", "2026-01-02", "2026-01-10", 0.10, 102.5)]
        annotated = apply_stock_names(rows, {"600268.SH": "国电南自"})

        self.assertEqual(annotated[0]["name"], "国电南自")
        self.assertNotIn("name", rows[0])

        summary = {
            "period_start": "2026-01-01",
            "period_end": "2026-02-01",
            "a_share_files": 1,
            "loaded_stocks": 1,
            "eligible_history_stocks": 1,
            "raw_signals": 1,
            "entry_valid_events": 1,
            "selected_trades": 1,
            "portfolio_return": 0.02,
            "benchmark_return": 0.01,
            "excess_vs_benchmark": 0.01,
            "avg_trade_return": 0.10,
            "win_rate": 1.0,
            "profit_factor": "inf",
            "max_new_entries_per_day": 1,
            "max_positions": 5,
            "min_rank_score": 102.0,
        }
        with TemporaryDirectory() as tmp_dir:
            output_dir = Path(tmp_dir)
            write_outputs(output_dir, summary, annotated, annotated, [])

            report = (output_dir / "report.md").read_text("utf-8")
            trades_csv = (output_dir / "all_a_stock_long_term_hold_trades.csv").read_text("utf-8")

        self.assertIn("| Code | Name | Entry |", report)
        self.assertIn("600268.SH | 国电南自", report)
        self.assertIn("name", trades_csv.splitlines()[0])
        self.assertIn("国电南自", trades_csv)


if __name__ == "__main__":
    unittest.main()
