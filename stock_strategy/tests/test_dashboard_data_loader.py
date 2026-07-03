import csv
import json
import tempfile
import unittest
from pathlib import Path

from stock_strategy.dashboard.data_loader import StrategyDashboardLoader


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False), "utf-8")


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else ["secucode", "stock_name"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


class DashboardDataLoaderTests(unittest.TestCase):
    def test_load_dashboard_uses_latest_local_strategy_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            base_dir = Path(tmp)
            write_json(
                base_dir / "reports" / "automation_10" / "summary_2026-06-23.json",
                {
                    "actual_signal_date": "2026-06-23",
                    "market": {"grade": "weak", "tradable": False},
                    "formal_candidates": [{"secucode": "000001.SZ"}],
                },
            )
            write_json(
                base_dir / "reports" / "automation_10" / "summary_2026-06-24.json",
                {
                    "run_time": "2026-06-24 21:56:31 CST +0800",
                    "actual_signal_date": "2026-06-24",
                    "market": {
                        "grade": "strong",
                        "tradable": True,
                        "score_avg3": 0.12,
                        "adv_ratio": 0.27,
                        "limit_ratio": 8.25,
                        "pause_reasons": [],
                    },
                    "formal_candidates": [],
                    "watchlist": [],
                    "candidate_block_reason": "历史 K 线无法验证，按规则不编造正式候选。",
                    "t_plus_1": {
                        "d0_signal_date": "2026-06-24",
                        "d1_buy_date": "2026-06-25",
                        "earliest_sell_date": "2026-06-26",
                    },
                    "holding_quote_check": [
                        {
                            "secucode": "300450.SZ",
                            "name": "先导智能",
                            "action": "触发硬止损",
                            "missing": "信号日低点缺失",
                        }
                    ],
                    "data_notes": ["Tencent full-A backtest failed."],
                },
            )
            write_json(
                base_dir / "reports" / "automation_10_candidate_scan_20260623.json",
                {"initial_count": 211, "results": [{"secucode": "300204.SZ", "name": "舒泰神"}]},
            )
            write_json(
                base_dir / "reports" / "backtest_10b" / "20260201_20260618_20260618_171852" / "summary.json",
                {
                    "trade_count": 125,
                    "win_rate": 0.376,
                    "avg_return": 0.0187,
                    "max_drawdown": -0.063,
                    "portfolio_cash_end": 1.134,
                },
            )
            write_csv(
                base_dir / "reports" / "backtest_10b" / "20260201_20260618_20260618_171852" / "trades.csv",
                [
                    {
                        "secucode": "688501.SH",
                        "stock_name": "青达环保",
                        "tier": "steady",
                        "signal_date": "2026-02-09",
                        "net_return": "-0.083",
                    }
                ],
            )
            write_csv(
                base_dir / "reports" / "backtest_10b" / "20260201_20260618_20260618_171852" / "market_states.csv",
                [
                    {
                        "trade_date": "2026-06-24",
                        "score_avg3": "0.124",
                        "adv_ratio": "0.270",
                        "tradable": "True",
                        "market_grade": "strong",
                    }
                ],
            )
            write_csv(
                base_dir / "data" / "live_trading" / "user_positions.csv",
                [
                    {
                        "secucode": "300450.SZ",
                        "code": "300450",
                        "name": "先导智能",
                        "market": "SZ",
                        "status": "holding",
                        "source": "user",
                        "added_date": "2026-06-10",
                        "buy_date": "",
                        "buy_price": "54",
                        "quantity": "",
                        "weight": "",
                        "notes": "temporary cost basis",
                    }
                ],
            )
            write_json(
                base_dir / "reports" / "live_trading" / "2026-06-21" / "summary.json",
                {
                    "trade_date": "2026-06-21",
                    "cash": 1000000,
                    "market_value": 0,
                    "equity": 1000000,
                    "exposure": 0,
                    "planned_orders": 0,
                    "fills": 0,
                    "rejections": 0,
                },
            )

            dashboard = StrategyDashboardLoader(base_dir).load_dashboard()

            self.assertEqual(dashboard["report_date"], "2026-06-24")
            self.assertEqual(dashboard["market"]["grade"], "strong")
            self.assertTrue(dashboard["market"]["tradable"])
            self.assertEqual(dashboard["candidate_status"]["formal_count"], 0)
            self.assertIn("不编造正式候选", dashboard["candidate_status"]["block_reason"])
            self.assertEqual(dashboard["t_plus_1"]["d1_buy_date"], "2026-06-25")
            self.assertEqual(dashboard["backtest_summary"]["trade_count"], 125)
            self.assertEqual(len(dashboard["trades"]), 1)
            self.assertEqual(len(dashboard["market_states"]), 1)
            self.assertEqual(len(dashboard["holdings_alerts"]), 1)
            self.assertEqual(dashboard["holdings_alerts"][0]["secucode"], "300450.SZ")
            self.assertEqual(dashboard["live_trading"]["trade_date"], "2026-06-21")
            self.assertIn("automation_summary", dashboard["source_files"])
            self.assertGreaterEqual(len(dashboard["strategy_catalog"]), 6)
            self.assertIn("hold5-tail", {item["id"] for item in dashboard["strategy_catalog"]})
            self.assertIn("ten-billion-turnover", {item["id"] for item in dashboard["strategy_catalog"]})

    def test_load_dashboard_handles_missing_and_empty_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            base_dir = Path(tmp)
            write_json(
                base_dir / "reports" / "automation_10" / "summary_2026-06-24.json",
                {
                    "actual_signal_date": "2026-06-24",
                    "market": {},
                    "formal_candidates": [],
                    "candidate_block_reason": "",
                },
            )
            write_csv(base_dir / "reports" / "backtest_10b" / "run" / "trades.csv", [])

            dashboard = StrategyDashboardLoader(base_dir).load_dashboard()

            self.assertEqual(dashboard["report_date"], "2026-06-24")
            self.assertEqual(dashboard["candidate_status"]["block_reason"], "暂无正式候选。")
            self.assertEqual(dashboard["backtest_summary"], {})
            self.assertEqual(dashboard["trades"], [])
            self.assertEqual(dashboard["market_states"], [])
            self.assertEqual(dashboard["holdings_alerts"], [])
            self.assertIn("未找到最新回测摘要", dashboard["data_notes"])
            self.assertEqual(dashboard["strategy_catalog"][0]["name"], "14:50 尾盘5日持有")

    def test_load_dashboard_ignores_csv_extra_columns(self):
        with tempfile.TemporaryDirectory() as tmp:
            base_dir = Path(tmp)
            write_json(
                base_dir / "reports" / "automation_10" / "summary_2026-06-24.json",
                {"actual_signal_date": "2026-06-24", "formal_candidates": []},
            )
            positions = base_dir / "data" / "live_trading" / "user_positions.csv"
            positions.parent.mkdir(parents=True)
            positions.write_text(
                "secucode,name,status,notes\n"
                "300450.SZ,先导智能,holding,user note,extra unquoted field\n",
                "utf-8",
            )

            dashboard = StrategyDashboardLoader(base_dir).load_dashboard()

            self.assertEqual(len(dashboard["user_positions"]), 1)
            self.assertEqual(dashboard["user_positions"][0]["secucode"], "300450.SZ")
            self.assertNotIn(None, dashboard["user_positions"][0])

    def test_holdings_alerts_prefer_current_user_holdings_over_stale_quote_checks(self):
        with tempfile.TemporaryDirectory() as tmp:
            base_dir = Path(tmp)
            write_json(
                base_dir / "reports" / "automation_10" / "summary_2026-06-24.json",
                {
                    "actual_signal_date": "2026-06-24",
                    "formal_candidates": [],
                    "holding_quote_check": [
                        {
                            "secucode": "300450.SZ",
                            "name": "先导智能",
                            "action": "旧持仓检查",
                        }
                    ],
                },
            )
            write_csv(
                base_dir / "data" / "live_trading" / "user_positions.csv",
                [
                    {
                        "secucode": "300450.SZ",
                        "name": "先导智能",
                        "status": "closed",
                        "notes": "已清仓",
                    },
                    {
                        "secucode": "688002.SH",
                        "name": "睿创微纳",
                        "status": "holding",
                        "notes": "当前持仓",
                    },
                ],
            )

            dashboard = StrategyDashboardLoader(base_dir).load_dashboard()

            self.assertEqual(len(dashboard["holdings_alerts"]), 1)
            self.assertEqual(dashboard["holdings_alerts"][0]["secucode"], "688002.SH")
            self.assertEqual(dashboard["holdings_alerts"][0]["action"], "当前持仓")

    def test_load_dashboard_includes_latest_hold5_top3_strategy(self):
        with tempfile.TemporaryDirectory() as tmp:
            base_dir = Path(tmp)
            write_json(
                base_dir / "reports" / "automation_10" / "summary_2026-06-24.json",
                {"actual_signal_date": "2026-06-24", "formal_candidates": []},
            )
            write_json(
                base_dir / "reports" / "automation_5_14_50" / "20260625_145020" / "summary.json",
                {
                    "latest_date": "2026-06-25",
                    "sell_date": "2026-07-02",
                    "formal": [{"secucode": "000001.SZ", "name": "旧候选", "avg_return": 0.01}],
                },
            )
            write_json(
                base_dir / "reports" / "automation_5_14_50" / "20260626_145203" / "summary.json",
                {
                    "generated_at": "2026-06-26T14:52:03+08:00",
                    "latest_date": "2026-06-26",
                    "sell_date": "2026-07-03",
                    "eligible_count": 418,
                    "validated_count": 413,
                    "adv_ratio": 0.155,
                    "top_industries": "半导体(1.20%, 60%上涨)",
                    "formal": [
                        {"secucode": "603986.SH", "name": "兆易创新", "avg_return": 0.045, "score": 103},
                        {"secucode": "001309.SZ", "name": "德明利", "avg_return": 0.061, "score": 82},
                        {"secucode": "600176.SH", "name": "中国巨石", "avg_return": 0.052, "score": 81},
                        {"secucode": "000725.SZ", "name": "不应展示", "avg_return": 0.016, "score": 80},
                    ],
                    "watch": [{"secucode": "300975.SZ", "name": "商络电子"}],
                },
            )
            write_json(
                base_dir / "reports" / "automation_5_14_50" / "position_review_20260627_150000" / "summary.json",
                {
                    "latest_date": "2026-06-27",
                    "position_reviews": [{"secucode": "000001.SZ"}],
                },
            )

            dashboard = StrategyDashboardLoader(base_dir).load_dashboard()

            hold5 = dashboard["hold5_top3"]
            self.assertEqual(hold5["strategy_name"], "5日盈利前三")
            self.assertEqual(hold5["latest_date"], "2026-06-26")
            self.assertEqual(hold5["sell_date"], "2026-07-03")
            self.assertEqual(hold5["formal_count"], 4)
            self.assertEqual([item["name"] for item in hold5["picks"]], ["兆易创新", "德明利", "中国巨石"])
            self.assertEqual(hold5["watch_count"], 1)
            self.assertIn("hold5_top3_summary", dashboard["source_files"])
            hold5_strategy = next(item for item in dashboard["strategy_catalog"] if item["id"] == "hold5-tail")
            self.assertIn("20260626_145203/summary.json", hold5_strategy["reports"][0]["path"])


if __name__ == "__main__":
    unittest.main()
