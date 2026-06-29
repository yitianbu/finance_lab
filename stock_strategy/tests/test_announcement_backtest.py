import unittest

from announcement_backtest import (
    CandidateTrade,
    KLine,
    StrategyConfig,
    build_candidate,
    config_name,
    event_passes_config,
    named_strategy_config,
    run_portfolio,
    score_predict_event,
    select_trades,
    simulate_trade,
    training_rank_key,
)


class AnnouncementBacktestTests(unittest.TestCase):
    def test_score_rewards_high_quality_profit_growth(self):
        event = {
            "PREDICT_TYPE": "预增",
            "INCREASE_JZ": 120,
            "FORECAST_JZ": 100_000_000,
            "CHANGE_REASON_EXPLAIN": "主营业务收入增长，产品销量提升。",
        }

        score, grade, reasons = score_predict_event(event)

        self.assertGreaterEqual(score, 80)
        self.assertEqual(grade, "A")
        self.assertIn("高增长", ",".join(reasons))

    def test_score_rejects_non_recurring_profit_growth(self):
        event = {
            "PREDICT_TYPE": "预增",
            "INCREASE_JZ": 150,
            "FORECAST_JZ": 50_000_000,
            "CHANGE_REASON_EXPLAIN": "主要由于资产处置收益和政府补贴等非经常性损益。",
        }

        score, grade, reasons = score_predict_event(event)

        self.assertLess(score, 80)
        self.assertNotEqual(grade, "A")
        self.assertIn("非经常性", ",".join(reasons))

    def test_simulate_trade_uses_stop_loss_before_take_profit_conservatively(self):
        klines = [
            KLine("2026-01-02", 100, 100, 100, 100, 0),
            KLine("2026-01-05", 100, 110, 115, 95, 0),
            KLine("2026-01-06", 108, 108, 109, 107, 0),
        ]

        result = simulate_trade(klines, entry_index=1, hold_days=2)

        self.assertEqual(result.exit_reason, "stop_loss")
        self.assertAlmostEqual(result.gross_return, -0.04, places=6)

    def test_simulate_trade_takes_profit_when_reached(self):
        klines = [
            KLine("2026-01-02", 100, 100, 100, 100, 0),
            KLine("2026-01-05", 100, 112, 113, 99, 0),
            KLine("2026-01-06", 108, 108, 109, 107, 0),
        ]

        result = simulate_trade(klines, entry_index=1, hold_days=2)

        self.assertEqual(result.exit_reason, "take_profit")
        self.assertAlmostEqual(result.gross_return, 0.12, places=6)

    def test_portfolio_keeps_duplicate_equal_trades_as_separate_positions(self):
        trade = CandidateTrade(
            secucode="000001.SZ",
            stock_code="000001",
            stock_name="平安银行",
            notice_date="2026-01-01",
            report_date="2025-12-31",
            entry_date="2026-01-02",
            exit_date="2026-01-06",
            entry_price=10,
            exit_price=11,
            gross_return=0.10,
            net_return=0.10,
            exit_reason="hold_5d",
            score=96,
            grade="A",
            predict_type="预增",
            increase_jz=100,
            forecast_jz=1_000_000,
            reasons="高增长",
        )

        _curve, metrics = run_portfolio([trade, trade], position_size=0.05)

        self.assertGreater(metrics["total_return"], 0.009)

    def test_portfolio_releases_cash_for_same_day_exit(self):
        trade1 = CandidateTrade(
            secucode="000001.SZ",
            stock_code="000001",
            stock_name="平安银行",
            notice_date="2026-01-01",
            report_date="2025-12-31",
            entry_date="2026-01-02",
            exit_date="2026-01-02",
            entry_price=10,
            exit_price=11,
            gross_return=0.10,
            net_return=0.10,
            exit_reason="take_profit",
            score=96,
            grade="A",
            predict_type="预增",
            increase_jz=100,
            forecast_jz=1_000_000,
            reasons="高增长",
        )
        trade2 = CandidateTrade(
            secucode="000002.SZ",
            stock_code="000002",
            stock_name="万科A",
            notice_date="2026-01-02",
            report_date="2025-12-31",
            entry_date="2026-01-03",
            exit_date="2026-01-03",
            entry_price=10,
            exit_price=11,
            gross_return=0.10,
            net_return=0.10,
            exit_reason="take_profit",
            score=96,
            grade="A",
            predict_type="预增",
            increase_jz=100,
            forecast_jz=1_000_000,
            reasons="高增长",
        )

        curve, metrics = run_portfolio([trade1, trade2], position_size=1.0)

        self.assertEqual(curve[-1]["active_positions"], 0)
        self.assertEqual(metrics["trade_count"], 2)
        self.assertGreater(metrics["total_return"], 0.20)

    def test_select_trades_does_not_rank_by_future_return(self):
        low_future_return = CandidateTrade(
            secucode="000001.SZ",
            stock_code="000001",
            stock_name="平安银行",
            notice_date="2026-01-01",
            report_date="2025-12-31",
            entry_date="2026-01-02",
            exit_date="2026-01-06",
            entry_price=10,
            exit_price=9,
            gross_return=-0.10,
            net_return=-0.10,
            exit_reason="hold_5d",
            score=96,
            grade="A",
            predict_type="预增",
            increase_jz=100,
            forecast_jz=1_000_000,
            reasons="高增长",
        )
        high_future_return = CandidateTrade(
            secucode="000002.SZ",
            stock_code="000002",
            stock_name="万科A",
            notice_date="2026-01-01",
            report_date="2025-12-31",
            entry_date="2026-01-02",
            exit_date="2026-01-06",
            entry_price=10,
            exit_price=12,
            gross_return=0.20,
            net_return=0.20,
            exit_reason="hold_5d",
            score=96,
            grade="A",
            predict_type="预增",
            increase_jz=100,
            forecast_jz=1_000_000,
            reasons="高增长",
        )

        selected = select_trades([low_future_return, high_future_return], min_score=96, max_per_day=1)

        self.assertEqual(selected[0].secucode, "000001.SZ")

    def test_event_filter_keeps_small_profit_turnaround_or_super_growth(self):
        config = StrategyConfig(
            min_score=96,
            max_forecast_jz=100_000_000,
            require_turnaround_or_high_growth=True,
            high_growth_threshold=300,
        )
        small_turnaround = {
            "EVENT_SCORE": 96,
            "PREDICT_TYPE": "扭亏",
            "INCREASE_JZ": 120,
            "FORECAST_JZ": 50_000_000,
            "NOTICE_DATE": "2026-01-01 00:00:00",
        }
        large_plain_growth = {
            "EVENT_SCORE": 96,
            "PREDICT_TYPE": "预增",
            "INCREASE_JZ": 120,
            "FORECAST_JZ": 500_000_000,
            "NOTICE_DATE": "2026-01-01 00:00:00",
        }
        small_super_growth = {
            "EVENT_SCORE": 96,
            "PREDICT_TYPE": "预增",
            "INCREASE_JZ": 350,
            "FORECAST_JZ": 80_000_000,
            "NOTICE_DATE": "2026-01-01 00:00:00",
        }

        self.assertTrue(event_passes_config(small_turnaround, config))
        self.assertFalse(event_passes_config(large_plain_growth, config))
        self.assertTrue(event_passes_config(small_super_growth, config))

    def test_pullback_close_entry_uses_close_after_confirmation(self):
        event = {
            "SECUCODE": "000001.SZ",
            "SECURITY_CODE": "000001",
            "SECURITY_NAME_ABBR": "平安银行",
            "NOTICE_DATE": "2026-01-01 00:00:00",
            "REPORT_DATE": "2025-12-31 00:00:00",
            "PREDICT_TYPE": "预增",
            "INCREASE_JZ": 350,
            "FORECAST_JZ": 80_000_000,
            "CHANGE_REASON_EXPLAIN": "主营业务收入增长。",
        }
        klines = [
            KLine("2026-01-01", 10, 10, 10, 10, 0),
            KLine("2026-01-02", 10.3, 10.1, 10.4, 9.95, 1),
            KLine("2026-01-05", 10.2, 11.4, 11.5, 10.2, 12),
        ]
        config = StrategyConfig(entry_mode="pullback_close", hold_days=2)

        candidate = build_candidate(event, klines, config)

        self.assertIsNotNone(candidate)
        self.assertEqual(candidate.entry_date, "2026-01-02")
        self.assertAlmostEqual(candidate.entry_price, 10.1)
        self.assertEqual(candidate.exit_reason, "take_profit")

    def test_select_trades_prioritizes_turnaround_super_growth_and_small_profit(self):
        plain_large = CandidateTrade(
            secucode="000001.SZ",
            stock_code="000001",
            stock_name="平安银行",
            notice_date="2026-01-01",
            report_date="2025-12-31",
            entry_date="2026-01-02",
            exit_date="2026-01-06",
            entry_price=10,
            exit_price=11,
            gross_return=0.10,
            net_return=0.10,
            exit_reason="hold_5d",
            score=96,
            grade="A",
            predict_type="预增",
            increase_jz=120,
            forecast_jz=500_000_000,
            reasons="高增长",
        )
        turnaround_small = CandidateTrade(
            secucode="000002.SZ",
            stock_code="000002",
            stock_name="万科A",
            notice_date="2026-01-01",
            report_date="2025-12-31",
            entry_date="2026-01-02",
            exit_date="2026-01-06",
            entry_price=10,
            exit_price=9,
            gross_return=-0.10,
            net_return=-0.10,
            exit_reason="hold_5d",
            score=96,
            grade="A",
            predict_type="扭亏",
            increase_jz=120,
            forecast_jz=50_000_000,
            reasons="高增长",
        )
        config = StrategyConfig(sort_mode="surprise")

        selected = select_trades([plain_large, turnaround_small], min_score=96, max_per_day=1, config=config)

        self.assertEqual(selected[0].secucode, "000002.SZ")

    def test_paper_conservative_strategy_matches_training_choice(self):
        config = named_strategy_config("paper_conservative")

        self.assertEqual(config.hold_days, 10)
        self.assertEqual(config.entry_mode, "open")
        self.assertEqual(config.stop_mode, "close")
        self.assertAlmostEqual(config.stop_loss, 0.04)
        self.assertEqual(config.max_forecast_jz, 100_000_000)
        self.assertEqual(config.exclude_entry_months, ("01", "07"))

    def test_named_strategy_hold_days_can_be_overridden(self):
        config = named_strategy_config("paper_conservative", hold_days=5)

        self.assertEqual(config.hold_days, 5)
        self.assertEqual(config.stop_mode, "close")

    def test_benchmark_constrained_strategy_uses_trained_exposure(self):
        config = named_strategy_config("benchmark_constrained")

        self.assertEqual(config.hold_days, 5)
        self.assertEqual(config.entry_mode, "open")
        self.assertEqual(config.stop_mode, "intraday")
        self.assertAlmostEqual(config.stop_loss, 0.04)
        self.assertEqual(config.max_forecast_jz, 100_000_000)
        self.assertEqual(config.exclude_entry_months, ("01", "07"))
        self.assertAlmostEqual(config.position_size, 0.20)
        self.assertEqual(config.max_per_day, 5)

    def test_training_rank_prefers_positive_benchmark_excess(self):
        benchmark_loser = {
            "train_trades": 80,
            "test_trades": 80,
            "train_annual_return": 0.18,
            "test_annual_return": 0.30,
            "train_excess_vs_hs300": 0.02,
            "test_excess_vs_hs300": -0.02,
            "test_profit_factor": 3.0,
            "test_max_drawdown": -0.05,
        }
        benchmark_winner = {
            "train_trades": 80,
            "test_trades": 80,
            "train_annual_return": 0.12,
            "test_annual_return": 0.16,
            "train_excess_vs_hs300": 0.01,
            "test_excess_vs_hs300": 0.03,
            "test_profit_factor": 2.0,
            "test_max_drawdown": -0.08,
        }

        self.assertGreater(training_rank_key(benchmark_winner), training_rank_key(benchmark_loser))

    def test_training_rank_prefers_positive_full_period_excess(self):
        full_period_loser = {
            "train_trades": 80,
            "test_trades": 80,
            "train_annual_return": 0.18,
            "test_annual_return": 0.30,
            "train_excess_vs_hs300": 0.02,
            "test_excess_vs_hs300": 0.08,
            "full_excess_vs_hs300": -0.01,
            "test_profit_factor": 3.0,
            "test_max_drawdown": -0.05,
        }
        full_period_winner = {
            "train_trades": 80,
            "test_trades": 80,
            "train_annual_return": 0.12,
            "test_annual_return": 0.16,
            "train_excess_vs_hs300": 0.01,
            "test_excess_vs_hs300": 0.03,
            "full_excess_vs_hs300": 0.01,
            "test_profit_factor": 2.0,
            "test_max_drawdown": -0.08,
        }

        self.assertGreater(training_rank_key(full_period_winner), training_rank_key(full_period_loser))

    def test_training_rank_prefers_positive_train_excess(self):
        train_loser = {
            "train_trades": 80,
            "test_trades": 80,
            "train_annual_return": 0.05,
            "test_annual_return": 0.30,
            "train_excess_vs_hs300": -0.05,
            "test_excess_vs_hs300": 0.08,
            "full_excess_vs_hs300": 0.05,
            "test_profit_factor": 3.0,
            "test_max_drawdown": -0.05,
        }
        train_winner = {
            "train_trades": 80,
            "test_trades": 80,
            "train_annual_return": 0.12,
            "test_annual_return": 0.16,
            "train_excess_vs_hs300": 0.01,
            "test_excess_vs_hs300": 0.03,
            "full_excess_vs_hs300": 0.01,
            "test_profit_factor": 2.0,
            "test_max_drawdown": -0.08,
        }

        self.assertGreater(training_rank_key(train_winner), training_rank_key(train_loser))

    def test_config_name_includes_position_size(self):
        config = StrategyConfig(position_size=0.20)

        self.assertIn("pos20", config_name(config))


if __name__ == "__main__":
    unittest.main()
