import unittest

from scripts.stock_strategy.backtest_hold5_tail_proxy import (
    ROUND_TRIP_COST,
    ProxyBar,
    build_analyzed_export_rows,
)


def make_bar(date: str, close: float) -> ProxyBar:
    return ProxyBar(
        date=date,
        open=close,
        close=close,
        high=close * 1.01,
        low=close * 0.99,
        volume=1000000,
        amount=500000000,
        amplitude=0.02,
        pct=0.01,
        change=0.1,
        turnover=3.0,
    )


class BacktestHold5TailProxyExportTests(unittest.TestCase):
    def test_build_analyzed_export_rows_keeps_rank_and_adds_forward_return(self):
        dates = [
            "2026-01-01",
            "2026-01-02",
            "2026-01-05",
            "2026-01-06",
            "2026-01-07",
            "2026-01-08",
            "2026-01-09",
        ]
        first_bars = [make_bar(date, close) for date, close in zip(dates, [10, 10, 11, 11, 12, 12, 13])]
        second_bars = [make_bar(date, close) for date, close in zip(dates, [20, 20, 19, 19, 18, 18, 17])]
        analyzed = [
            {"secucode": "300001.SZ", "name": "测试一", "score": 99.0},
            {"secucode": "300002.SZ", "name": "测试二", "score": 88.0},
            {"secucode": "300003.SZ", "name": "测试三", "score": 77.0},
        ]

        rows = build_analyzed_export_rows(
            analyzed,
            {
                "300001.SZ": first_bars,
                "300002.SZ": second_bars,
            },
            {
                "300001.SZ": {bar.date: idx for idx, bar in enumerate(first_bars)},
                "300002.SZ": {bar.date: idx for idx, bar in enumerate(second_bars)},
            },
            trade_date="2026-01-02",
            evaluation_date="2026-01-09",
            limit=2,
        )

        self.assertEqual([row["rank"] for row in rows], [1, 2])
        self.assertEqual([row["secucode"] for row in rows], ["300001.SZ", "300002.SZ"])
        self.assertEqual(rows[0]["evaluation_date"], "2026-01-09")
        self.assertAlmostEqual(rows[0]["strategy_return"], 13 / 10 - 1 - ROUND_TRIP_COST)
        self.assertAlmostEqual(rows[1]["strategy_return"], 17 / 20 - 1 - ROUND_TRIP_COST)


if __name__ == "__main__":
    unittest.main()
