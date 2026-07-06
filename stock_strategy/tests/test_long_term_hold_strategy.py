import tempfile
import unittest
from pathlib import Path

from long_term_hold_strategy import (
    LongTermHoldConfig,
    analyze_long_term_hold,
    backtest_long_term_hold,
    write_long_term_hold_outputs,
)
from stock_range_trader import DailyBar


def make_bar(day: int, close: float, volume: float = 1_200_000, open_price: float | None = None) -> DailyBar:
    open_value = open_price if open_price is not None else close * 0.998
    return DailyBar(
        trade_date=f"2026-01-{day:03d}",
        open=open_value,
        close=close,
        high=max(open_value, close) * 1.006,
        low=min(open_value, close) * 0.994,
        volume=volume,
        amount=volume * close,
        pct_change=0.0,
        turnover=1.8,
    )


def long_term_setup() -> tuple[list[DailyBar], list[DailyBar]]:
    stock_bars: list[DailyBar] = []
    benchmark_bars: list[DailyBar] = []
    stock_close = 10.0
    benchmark_close = 3000.0
    for day in range(1, 281):
        benchmark_close *= 1.00035
        stock_close *= 1.00075 if day < 140 else 1.00135
        stock_bars.append(make_bar(day, stock_close, 1_200_000))
        benchmark_bars.append(make_bar(day, benchmark_close, 8_000_000))
    return stock_bars, benchmark_bars


class LongTermHoldStrategyTests(unittest.TestCase):
    def test_accepts_long_term_relative_strength_candidate(self):
        stock_bars, benchmark_bars = long_term_setup()

        result = analyze_long_term_hold("300450.SZ", "长期强势", stock_bars, benchmark_bars)

        self.assertTrue(result.tradable)
        self.assertEqual(result.reject_reason, "")
        self.assertGreater(result.ma60, result.ma120)
        self.assertGreater(result.ma120, result.ma200)
        self.assertGreaterEqual(result.excess_return_120d, 0.06)
        self.assertGreaterEqual(result.excess_return_240d, 0.08)
        self.assertGreater(result.buy_zone_high, result.latest_close)
        self.assertLess(result.initial_stop_loss, result.latest_close)
        self.assertIn("long_term_hold", result.tags)

    def test_rejects_candidate_that_underperforms_benchmark(self):
        stock_bars, benchmark_bars = long_term_setup()
        stock_close = stock_bars[139].close
        benchmark_close = benchmark_bars[139].close
        for idx in range(140, 280):
            stock_close *= 1.00005
            benchmark_close *= 1.00090
            day = idx + 1
            stock_bars[idx] = make_bar(day, stock_close, 1_100_000)
            benchmark_bars[idx] = make_bar(day, benchmark_close, 8_000_000)

        result = analyze_long_term_hold("300451.SZ", "跑输样本", stock_bars, benchmark_bars)

        self.assertFalse(result.tradable)
        self.assertIn("excess_return_120d", result.reject_reason)

    def test_backtest_holds_for_weeks_and_exits_on_deterioration(self):
        stock_bars, benchmark_bars = long_term_setup()
        stock_close = stock_bars[-1].close
        benchmark_close = benchmark_bars[-1].close
        for day in range(281, 341):
            benchmark_close *= 1.0010
            stock_close *= 1.0010 if day < 300 else 0.9965
            stock_bars.append(make_bar(day, stock_close, 1_150_000))
            benchmark_bars.append(make_bar(day, benchmark_close, 8_000_000))

        config = LongTermHoldConfig(min_history_days=220, min_hold_days=10, relative_exit_lookback=20)
        metrics, trades = backtest_long_term_hold("300450.SZ", stock_bars, benchmark_bars, config)

        self.assertEqual(metrics["trades"], 1)
        self.assertLessEqual(metrics["trades_per_year"], 3.0)
        self.assertGreaterEqual(trades[0]["holding_days"], 10)
        self.assertIn(trades[0]["exit_reason"], {"relative_weakness", "trend_break", "trailing_stop"})

    def test_write_outputs_creates_report_files(self):
        stock_bars, benchmark_bars = long_term_setup()
        result = analyze_long_term_hold("300450.SZ", "长期强势", stock_bars, benchmark_bars)

        with tempfile.TemporaryDirectory() as tmp:
            write_long_term_hold_outputs(Path(tmp), [result], LongTermHoldConfig())

            self.assertTrue((Path(tmp) / "long_term_hold_scan.csv").exists())
            self.assertTrue((Path(tmp) / "long_term_hold_scan.json").exists())
            report = (Path(tmp) / "long_term_hold_scan_report.md").read_text("utf-8")
            self.assertIn("长期持有跑赢大盘策略扫描", report)
            self.assertIn("300450.SZ", report)


if __name__ == "__main__":
    unittest.main()
