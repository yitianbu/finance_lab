import tempfile
import unittest
from pathlib import Path

from announcement_backtest import CandidateTrade
from live_trader import (
    LiveRiskConfig,
    PaperAccount,
    Position,
    apply_paper_fills,
    build_buy_plan,
    build_sell_plan,
    write_daily_outputs,
)


def candidate(secucode: str, stock_name: str = "测试股票", price: float = 10.0) -> CandidateTrade:
    code = secucode.split(".")[0]
    return CandidateTrade(
        secucode=secucode,
        stock_code=code,
        stock_name=stock_name,
        notice_date="2026-01-01",
        report_date="2025-12-31",
        entry_date="2026-01-02",
        exit_date="2026-01-08",
        entry_price=price,
        exit_price=price * 1.05,
        gross_return=0.05,
        net_return=0.048,
        exit_reason="hold_5d",
        score=96,
        grade="A",
        predict_type="预增",
        increase_jz=100,
        forecast_jz=50_000_000,
        reasons="高增长",
    )


class LiveTraderTests(unittest.TestCase):
    def test_buy_plan_rejects_blacklist_st_and_total_exposure_limit(self):
        config = LiveRiskConfig(
            position_size=0.20,
            max_total_exposure=0.40,
            blacklist=("000001.SZ",),
        )
        account = PaperAccount(
            cash=600_000,
            positions={
                "000099.SZ": Position("000099.SZ", "已有持仓", 20_000, 10.0, 10.0),
                "000100.SZ": Position("000100.SZ", "已有持仓2", 20_000, 10.0, 10.0),
            },
        )

        plan = build_buy_plan(
            [
                candidate("000001.SZ"),
                candidate("000002.SZ", stock_name="ST测试"),
                candidate("000003.SZ"),
            ],
            account,
            config,
            trade_date="2026-01-02",
        )

        self.assertEqual(len(plan.accepted_orders), 0)
        reasons = {item.secucode: item.reason for item in plan.rejected}
        self.assertIn("黑名单", reasons["000001.SZ"])
        self.assertIn("ST", reasons["000002.SZ"])
        self.assertIn("组合仓位", reasons["000003.SZ"])

    def test_buy_plan_caps_new_orders_per_day(self):
        config = LiveRiskConfig(position_size=0.10, max_total_exposure=1.0, max_new_positions=2)
        account = PaperAccount(cash=1_000_000)

        plan = build_buy_plan(
            [candidate(f"00000{i}.SZ") for i in range(1, 5)],
            account,
            config,
            trade_date="2026-01-02",
        )

        self.assertEqual(len(plan.accepted_orders), 2)
        self.assertEqual(len(plan.rejected), 2)
        self.assertTrue(all("单日买入上限" in item.reason for item in plan.rejected))

    def test_apply_paper_fills_reduces_cash_and_adds_position(self):
        account = PaperAccount(cash=1_000_000)
        plan = build_buy_plan(
            [candidate("000001.SZ", price=10.0)],
            account,
            LiveRiskConfig(position_size=0.20),
            trade_date="2026-01-02",
        )

        fills, updated = apply_paper_fills(plan.accepted_orders, account)

        self.assertEqual(len(fills), 1)
        self.assertLess(updated.cash, account.cash)
        self.assertIn("000001.SZ", updated.positions)
        self.assertGreater(updated.positions["000001.SZ"].quantity, 0)

    def test_sell_plan_exits_positions_on_planned_exit_date(self):
        account = PaperAccount(
            cash=800_000,
            positions={
                "000001.SZ": Position(
                    "000001.SZ",
                    "平安银行",
                    20_000,
                    10.0,
                    10.5,
                    entry_date="2026-01-02",
                    planned_exit_date="2026-01-08",
                )
            },
        )

        sell_orders = build_sell_plan(account, trade_date="2026-01-08")
        fills, updated = apply_paper_fills(sell_orders, account)

        self.assertEqual(len(sell_orders), 1)
        self.assertEqual(sell_orders[0].side, "SELL")
        self.assertEqual(len(fills), 1)
        self.assertNotIn("000001.SZ", updated.positions)
        self.assertGreater(updated.cash, account.cash)

    def test_write_daily_outputs_creates_audit_files(self):
        account = PaperAccount(cash=1_000_000)
        plan = build_buy_plan(
            [candidate("000001.SZ"), candidate("000002.SZ", stock_name="ST测试")],
            account,
            LiveRiskConfig(position_size=0.20),
            trade_date="2026-01-02",
        )
        fills, updated = apply_paper_fills(plan.accepted_orders, account)

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp)
            write_daily_outputs(output_dir, plan, fills, updated)

            self.assertTrue((output_dir / "orders.csv").exists())
            self.assertTrue((output_dir / "fills.csv").exists())
            self.assertTrue((output_dir / "positions.csv").exists())
            report = (output_dir / "daily_report.md").read_text("utf-8")
            self.assertIn("纸面实盘日报", report)
            self.assertIn("风控拒绝", report)


if __name__ == "__main__":
    unittest.main()
