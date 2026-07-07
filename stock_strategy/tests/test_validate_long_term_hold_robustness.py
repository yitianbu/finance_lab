import unittest

from scripts.stock_strategy.backtest_long_term_hold_all_a import PortfolioBacktestConfig
from scripts.stock_strategy.validate_long_term_hold_robustness import (
    ParameterCase,
    PeriodCase,
    apply_extra_round_trip_cost,
    build_arg_parser,
    run_parameter_grid,
    run_period_cases,
)


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
        "name": secucode,
        "signal_date": entry_date,
        "entry_date": entry_date,
        "exit_date": exit_date,
        "entry_price": 10.0,
        "exit_price": 10.0 * (1.0 + net_return),
        "gross_return": net_return + 0.0013,
        "net_return": net_return,
        "benchmark_return": 0.0,
        "excess_return": net_return,
        "exit_reason": "test",
        "holding_days": 5,
        "rank_score": rank_score,
        "excess_return_120d": excess_return_120d,
        "excess_return_240d": excess_return_240d,
        "stock_return_120d": 0.20,
        "drawdown_120d": -0.05,
        "volatility_120d": 0.25,
    }


class ValidateLongTermHoldRobustnessTests(unittest.TestCase):
    def test_apply_extra_round_trip_cost_reduces_returns_without_mutating_input(self):
        rows = [event("600001.SH", "2026-01-02", "2026-01-10", 0.10, 102.0)]

        stressed = apply_extra_round_trip_cost(rows, 0.003)

        self.assertEqual(rows[0]["net_return"], 0.10)
        self.assertAlmostEqual(stressed[0]["net_return"], 0.097)
        self.assertAlmostEqual(stressed[0]["excess_return"], 0.097)
        self.assertEqual(stressed[0]["extra_round_trip_cost"], 0.003)

    def test_run_period_cases_returns_one_summary_per_period(self):
        events = [
            event("600001.SH", "2025-01-02", "2025-01-10", 0.10, 102.5),
            event("600002.SH", "2026-01-02", "2026-01-10", 0.20, 102.5),
        ]
        config = PortfolioBacktestConfig(period_start="2025-01-01", period_end="2026-12-31")
        periods = [
            PeriodCase("2025", "2025-01-01", "2025-12-31", 0.05),
            PeriodCase("2026", "2026-01-01", "2026-12-31", -0.02),
        ]

        rows = run_period_cases(events, config, periods)

        self.assertEqual([row["case"] for row in rows], ["2025", "2026"])
        self.assertEqual([row["selected_trades"] for row in rows], [1, 1])
        self.assertAlmostEqual(rows[0]["benchmark_return"], 0.05)
        self.assertAlmostEqual(rows[1]["benchmark_return"], -0.02)

    def test_run_period_cases_can_apply_market_gate(self):
        events = [
            event("600001.SH", "2025-01-02", "2025-01-10", 0.10, 102.5),
            event("600002.SH", "2025-01-03", "2025-01-10", 0.20, 102.5),
        ]
        config = PortfolioBacktestConfig(period_start="2025-01-01", period_end="2025-12-31")
        periods = [PeriodCase("2025", "2025-01-01", "2025-12-31", 0.0)]

        rows = run_period_cases(
            events,
            config,
            periods,
            market_gate={"2025-01-02": False, "2025-01-03": True},
        )

        self.assertEqual(rows[0]["selected_trades"], 1)
        self.assertEqual(rows[0]["market_gate_blocked_entries"], 1)

    def test_run_parameter_grid_returns_each_config_with_friction_label(self):
        events = [
            event("600001.SH", "2026-01-02", "2026-01-10", 0.10, 101.5),
            event("600002.SH", "2026-01-03", "2026-01-10", 0.20, 102.5),
        ]
        config = PortfolioBacktestConfig(period_start="2026-01-01", period_end="2026-12-31")
        cases = [
            ParameterCase("loose", min_rank_score=101.0, max_positions=5, target_weight=0.2, max_new_entries_per_day=1),
            ParameterCase("strict", min_rank_score=102.0, max_positions=5, target_weight=0.2, max_new_entries_per_day=1),
        ]

        rows = run_parameter_grid(events, config, cases, benchmark_return=0.0, extra_round_trip_cost=0.002)

        self.assertEqual([row["case"] for row in rows], ["loose", "strict"])
        self.assertEqual([row["extra_round_trip_cost"] for row in rows], [0.002, 0.002])
        self.assertEqual([row["selected_trades"] for row in rows], [2, 1])
        self.assertGreater(rows[0]["portfolio_return"], rows[1]["portfolio_return"])

    def test_run_parameter_grid_includes_capital_time_efficiency(self):
        events = [event("600001.SH", "2026-01-02", "2026-01-10", 0.10, 102.5)]
        config = PortfolioBacktestConfig(period_start="2026-01-01", period_end="2026-12-31")
        cases = [
            ParameterCase("base", min_rank_score=102.0, max_positions=5, target_weight=0.2, max_new_entries_per_day=1),
        ]

        rows = run_parameter_grid(events, config, cases, benchmark_return=0.0)

        self.assertAlmostEqual(rows[0]["capital_time_units"], 1.0)
        self.assertAlmostEqual(rows[0]["capital_time_pnl"], 0.02)
        self.assertAlmostEqual(rows[0]["pnl_per_capital_time_unit"], 0.02)
        self.assertAlmostEqual(rows[0]["annualized_pnl_per_capital_time"], 4.88)

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


if __name__ == "__main__":
    unittest.main()
