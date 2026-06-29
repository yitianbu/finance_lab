from unittest import TestCase

from scripts.stock_strategy.backtest_10b_tencent import DailyBar, MarketState


class Backtest10BTests(TestCase):
    def make_bar(self, trade_date: str, open_: float, close: float, high: float, low: float, amount: float) -> DailyBar:
        return DailyBar(
            trade_date=trade_date,
            open=open_,
            close=close,
            high=high,
            low=low,
            amount=amount,
            pct_change=((close / open_) - 1.0) * 100 if open_ else 0.0,
            turnover=0.0,
        )

    def make_market(self) -> MarketState:
        return MarketState(
            trade_date="2026-04-21",
            score=1.2,
            score_avg3=0.8,
            sh_close=3500,
            cy_close=2200,
            sh_ma20=3400,
            cy_ma20=2100,
            advancers=3000,
            decliners=1800,
            unchanged=100,
            limit_up=90,
            limit_down=20,
            adv_ratio=0.62,
            limit_ratio=4.5,
            sh_rsi14=58,
            base_vol_ratio=1.8,
            high_distance_threshold=-10.0,
            tradable=True,
            pause_reasons=[],
        )

    def test_classify_market_grade(self):
        from scripts.stock_strategy.backtest_10b_tencent import classify_market_grade

        self.assertEqual(classify_market_grade(2.1, True), "super")
        self.assertEqual(classify_market_grade(0.6, True), "strong")
        self.assertEqual(classify_market_grade(-0.1, True), "weak")
        self.assertEqual(classify_market_grade(1.2, False), "weak")

    def test_secondary_tier_can_pass_when_core_fails(self):
        from scripts.stock_strategy.backtest_10b_tencent import SignalTierConfig, evaluate_signal_tier

        bars = [
            self.make_bar(f"2026-04-{day:02d}", 10.0, 10.0 + day * 0.02, 10.2 + day * 0.02, 9.8 + day * 0.02, 4e8)
            for day in range(1, 61)
        ]
        bars.append(self.make_bar("2026-06-21", 11.0, 11.4, 11.5, 10.95, 1.45e9))
        market = self.make_market()
        core = SignalTierConfig(
            name="core",
            min_amount_delta=1e9,
            min_amount_growth=2.0,
            min_ma5_ratio=3.0,
            min_close_position=0.8,
            max_dist15=18.0,
            require_ma_alignment=False,
        )
        steady = SignalTierConfig(
            name="steady",
            min_amount_delta=7e8,
            min_amount_growth=1.2,
            min_ma5_ratio=2.0,
            min_close_position=0.72,
            max_dist15=24.0,
            require_ma_alignment=True,
        )

        self.assertIsNone(evaluate_signal_tier(bars, len(bars) - 1, market, core))
        self.assertIsNotNone(evaluate_signal_tier(bars, len(bars) - 1, market, steady))

    def test_signal_tier_name_is_preserved(self):
        from scripts.stock_strategy.backtest_10b_tencent import SignalTierConfig, evaluate_signal_tier

        bars = [
            self.make_bar(f"2026-05-{day:02d}", 10.0, 10.1 + day * 0.02, 10.2 + day * 0.02, 9.95 + day * 0.02, 5e8)
            for day in range(1, 61)
        ]
        bars.append(self.make_bar("2026-07-21", 11.0, 11.35, 11.40, 10.98, 1.6e9))
        market = self.make_market()
        tier = SignalTierConfig(
            name="steady",
            min_amount_delta=7e8,
            min_amount_growth=1.0,
            min_ma5_ratio=2.0,
            min_close_position=0.72,
            max_dist15=24.0,
            require_ma_alignment=True,
        )

        signal = evaluate_signal_tier(bars, len(bars) - 1, market, tier)
        self.assertEqual(signal["tier"], "steady")

    def test_trailing_drawdown_threshold_is_wider_for_steady_style(self):
        from scripts.stock_strategy.backtest_10b_tencent import trailing_drawdown_threshold

        self.assertEqual(trailing_drawdown_threshold(0.05, "steady"), 0.10)
        self.assertEqual(trailing_drawdown_threshold(0.15, "steady"), 0.12)
        self.assertEqual(trailing_drawdown_threshold(0.25, "steady"), 0.15)

    def test_market_grade_controls_tier_participation(self):
        from scripts.stock_strategy.backtest_10b_tencent import should_trade_tier

        self.assertFalse(should_trade_tier("steady", "weak"))
        self.assertTrue(should_trade_tier("core", "weak"))
        self.assertTrue(should_trade_tier("steady", "super"))
        self.assertTrue(should_trade_tier("core", "super"))

    def test_objective_penalizes_low_sample_and_drawdown(self):
        from scripts.stock_strategy.backtest_10b_tencent import objective_score

        weak = objective_score({"trade_count": 2, "avg_return": 0.03, "max_drawdown": -0.18, "win_rate": 1.0, "portfolio_cash_end": 1.02})
        stable = objective_score({"trade_count": 12, "avg_return": 0.015, "max_drawdown": -0.05, "win_rate": 0.58, "portfolio_cash_end": 1.08})
        self.assertGreater(stable, weak)
