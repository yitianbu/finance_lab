import tempfile
import unittest
from pathlib import Path

from scripts.stock_strategy.run_long_term_hold_candidates import load_candidates, scan_with_loader
from stock_range_trader import DailyBar


def make_bar(day: int, close: float, volume: float = 1_000_000) -> DailyBar:
    return DailyBar(
        trade_date=f"2026-02-{day:03d}",
        open=close * 0.998,
        close=close,
        high=close * 1.004,
        low=close * 0.994,
        volume=volume,
        amount=volume * close,
        pct_change=0.0,
        turnover=1.5,
    )


def long_term_bars() -> tuple[list[DailyBar], list[DailyBar]]:
    stock_bars: list[DailyBar] = []
    benchmark_bars: list[DailyBar] = []
    stock_close = 9.5
    benchmark_close = 3000.0
    for day in range(1, 281):
        benchmark_close *= 1.00035
        stock_close *= 1.00080 if day < 150 else 1.00130
        stock_bars.append(make_bar(day, stock_close, 1_100_000))
        benchmark_bars.append(make_bar(day, benchmark_close, 8_000_000))
    return stock_bars, benchmark_bars


class RunLongTermHoldCandidatesTests(unittest.TestCase):
    def test_load_candidates_dedupes_inline_and_file_codes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "codes.csv"
            path.write_text("secucode,name\n300450.SZ,长期强势\n600000.SH,样本\n", encoding="utf-8")

            candidates = load_candidates("300450,300450.SZ", str(path), limit=10)

            self.assertEqual([item.secucode for item in candidates], ["300450.SZ", "600000.SH"])

    def test_scan_with_loader_writes_outputs(self):
        candidates = load_candidates("300450,300451", "", limit=10)
        strong_bars, benchmark_bars = long_term_bars()

        def loader(secucode: str) -> list[DailyBar]:
            bars = list(strong_bars)
            if secucode == "300451.SZ":
                latest = bars[-1]
                bars[-1] = make_bar(280, latest.close * 0.92, 1_000_000)
            return bars

        with tempfile.TemporaryDirectory() as tmp:
            results = scan_with_loader(candidates, loader, benchmark_bars, Path(tmp))

            self.assertEqual(results[0].secucode, "300450.SZ")
            self.assertTrue(results[0].tradable)
            self.assertFalse(results[1].tradable)
            self.assertTrue((Path(tmp) / "long_term_hold_scan.csv").exists())
            self.assertTrue((Path(tmp) / "long_term_hold_scan_report.md").exists())


if __name__ == "__main__":
    unittest.main()
