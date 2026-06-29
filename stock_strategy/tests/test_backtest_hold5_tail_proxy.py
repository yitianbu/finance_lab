import unittest

from scripts.stock_strategy.backtest_hold5_tail_proxy import (
    ROUND_TRIP_COST,
    ProxyBar,
    build_analyzed_export_rows,
    select_trade_candidates,
    summarize_rolling_capital,
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

    def test_select_trade_candidates_excludes_watch_rows_from_buys(self):
        analyzed = [
            {"secucode": "688001.SH", "name": "高分观察", "tier": "观察", "score": 100.0},
            {"secucode": "300001.SZ", "name": "核心一", "tier": "核心", "score": 90.0},
            {"secucode": "300002.SZ", "name": "被拒进取", "tier": "进取", "score": 85.0, "reject_reason": "win_rate_lt_55"},
            {"secucode": "300004.SZ", "name": "进取一", "tier": "进取", "score": 80.0, "reject_reason": ""},
            {"secucode": "300003.SZ", "name": "观察二", "tier": "观察", "score": 70.0},
        ]

        selected = select_trade_candidates(analyzed, limit=3)

        self.assertEqual([row["secucode"] for row in selected], ["300001.SZ", "300004.SZ"])

    def test_summarize_rolling_capital_uses_complete_trades_only(self):
        rows = [
            {"rank": 1, "strategy_return": 0.10, "holding_complete": True},
            {"rank": 2, "strategy_return": -0.05, "holding_complete": True},
            {"rank": 3, "strategy_return": 0.20, "holding_complete": True},
            {"rank": 1, "strategy_return": 0.50, "holding_complete": False},
        ]

        top3 = summarize_rolling_capital(rows, rank1_only=False, daily_capital=3.0, hold_days=5)
        rank1 = summarize_rolling_capital(rows, rank1_only=True, daily_capital=3.0, hold_days=5)

        self.assertEqual(top3["completed_trades"], 3)
        self.assertAlmostEqual(top3["pnl_on_max_capital"], 0.25 / 15.0)
        self.assertEqual(rank1["completed_trades"], 1)
        self.assertAlmostEqual(rank1["pnl_on_max_capital"], 0.10 * 3.0 / 15.0)


if __name__ == "__main__":
    unittest.main()
