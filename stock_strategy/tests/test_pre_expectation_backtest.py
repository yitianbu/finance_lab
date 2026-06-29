import unittest

from pre_expectation_backtest import (
    PreExpectationConfig,
    build_pre_event_candidate,
    is_excluded_stock_name,
    price_strength_signal,
    simulate_until_forced_exit,
)
from announcement_backtest import KLine


class PreExpectationBacktestTests(unittest.TestCase):
    def test_signal_does_not_change_when_future_bar_changes(self):
        klines = [
            KLine(f"2026-01-{day:02d}", 10 + day * 0.05, 10 + day * 0.05, 10 + day * 0.05, 10 + day * 0.05, 0)
            for day in range(1, 23)
        ]
        klines[20] = KLine("2026-01-21", 11.2, 11.6, 11.7, 11.1, 0)
        klines[21] = KLine("2026-01-22", 20.0, 20.0, 20.0, 20.0, 0)
        benchmark = {bar.trade_date: bar.close for bar in klines}
        config = PreExpectationConfig(min_pre_5d_return=0.02, min_pre_10d_excess=-0.20)

        first = price_strength_signal(klines, signal_idx=20, benchmark_by_date=benchmark, config=config)

        changed_future = list(klines)
        changed_future[21] = KLine("2026-01-22", 5.0, 5.0, 5.0, 5.0, 0)
        second = price_strength_signal(changed_future, signal_idx=20, benchmark_by_date=benchmark, config=config)

        self.assertEqual(first, second)

    def test_trade_respects_t1_even_if_entry_day_hits_stop(self):
        klines = [
            KLine("2026-01-01", 100, 100, 100, 100, 0),
            KLine("2026-01-02", 100, 100, 120, 90, 0),
            KLine("2026-01-05", 100, 112, 113, 99, 0),
        ]
        config = PreExpectationConfig(stop_loss=0.05, take_profit=0.10)

        result = simulate_until_forced_exit(
            klines,
            entry_idx=1,
            entry_price=100,
            forced_exit_idx=2,
            config=config,
        )

        self.assertEqual(result.exit_date, "2026-01-05")
        self.assertEqual(result.exit_reason, "take_profit")

    def test_pre_event_candidate_enters_before_announcement_reaction(self):
        event = {
            "SECUCODE": "000001.SZ",
            "SECURITY_CODE": "000001",
            "SECURITY_NAME_ABBR": "平安银行",
            "NOTICE_DATE": "2026-01-07 00:00:00",
            "REPORT_DATE": "2025-12-31 00:00:00",
            "PREDICT_TYPE": "预增",
            "INCREASE_JZ": 350,
            "FORECAST_JZ": 50_000_000,
            "CHANGE_REASON_EXPLAIN": "主营业务收入增长，订单增加。",
        }
        klines = [
            KLine("2026-01-01", 10.0, 10.0, 10.0, 10.0, 0),
            KLine("2026-01-02", 10.1, 10.1, 10.1, 10.1, 0),
            KLine("2026-01-05", 10.2, 10.2, 10.2, 10.2, 0),
            KLine("2026-01-06", 10.4, 10.6, 10.7, 10.3, 0),
            KLine("2026-01-08", 10.7, 11.4, 11.5, 10.7, 0),
            KLine("2026-01-09", 11.4, 11.3, 11.4, 11.2, 0),
        ]
        benchmark = {bar.trade_date: bar.close for bar in klines}
        config = PreExpectationConfig(
            pre_entry_days=1,
            exclude_notice_months=(),
            min_pre_5d_return=-1.0,
            min_pre_10d_excess=-1.0,
            max_pre_20d_return=10.0,
            min_history_days=0,
        )

        candidate = build_pre_event_candidate(event, klines, benchmark, config)

        self.assertIsNotNone(candidate)
        self.assertEqual(candidate.entry_date, "2026-01-06")
        self.assertEqual(candidate.notice_date, "2026-01-07")
        self.assertNotEqual(candidate.exit_date, candidate.entry_date)

    def test_excludes_st_and_delisting_risk_names(self):
        config = PreExpectationConfig()

        self.assertTrue(is_excluded_stock_name("*ST国华", config))
        self.assertTrue(is_excluded_stock_name("ST高鸿", config))
        self.assertTrue(is_excluded_stock_name("退市园城", config))
        self.assertFalse(is_excluded_stock_name("平安银行", config))


if __name__ == "__main__":
    unittest.main()
