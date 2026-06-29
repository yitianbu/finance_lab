import unittest

from stock_range_trader import (
    CalibrationResult,
    DailyBar,
    PredictionConfig,
    RangePrediction,
    TradePlan,
    backtest_predictions,
    calibrate_atr_multiplier,
    make_trade_plan,
    max_drawdown,
    parse_tencent_payload,
    predict_next_range,
    simulate_trade,
    simulate_t1_position_trade,
)


def make_bar(day: int, close: float, pct: float = 0.0, volume: float = 1_000_000) -> DailyBar:
    open_price = close * (1 - pct / 200)
    high = close * (1 + 0.015 + abs(pct) / 300)
    low = close * (1 - 0.015 - abs(pct) / 300)
    return DailyBar(
        trade_date=f"2026-01-{day:02d}",
        open=open_price,
        close=close,
        high=high,
        low=low,
        volume=volume,
        amount=volume * close,
        pct_change=pct,
        turnover=1.0,
    )


def synthetic_bars(count: int = 150) -> list[DailyBar]:
    bars: list[DailyBar] = []
    close = 20.0
    for idx in range(count):
        pct = ((idx % 9) - 4) * 0.35
        close *= 1 + pct / 100
        day = idx + 1
        bars.append(make_bar(day, close, pct=pct, volume=1_000_000 + idx * 1000))
    return bars


class StockRangeTraderTests(unittest.TestCase):
    def test_prediction_does_not_change_when_future_spike_is_appended(self):
        bars = synthetic_bars(130)
        signal_idx = 118
        config = PredictionConfig(history_window=70, similar_count=12)

        base_prediction = predict_next_range(bars[: signal_idx + 1], signal_idx, config)
        future_spike = DailyBar(
            trade_date="2026-06-01",
            open=60,
            close=75,
            high=90,
            low=58,
            volume=8_000_000,
            amount=600_000_000,
            pct_change=20,
            turnover=8.0,
        )
        appended_prediction = predict_next_range(bars[: signal_idx + 1] + [future_spike], signal_idx, config)

        self.assertAlmostEqual(base_prediction.predicted_high, appended_prediction.predicted_high, places=8)
        self.assertAlmostEqual(base_prediction.predicted_low, appended_prediction.predicted_low, places=8)
        self.assertEqual(base_prediction.next_trade_date, appended_prediction.next_trade_date)

    def test_calibration_selects_smallest_covering_multiplier(self):
        bars = synthetic_bars(150)
        config = PredictionConfig(history_window=70, target_coverage=0.55)

        result = calibrate_atr_multiplier(bars, end_signal_idx=140, config=config, target_count=40)

        self.assertIn(result.multiplier, config.atr_multiplier_candidates)
        self.assertGreaterEqual(result.coverage, 0.55)
        smaller = [item for item in result.candidates if item["multiplier"] < result.multiplier]
        self.assertTrue(all(item["coverage"] < 0.55 for item in smaller))

    def test_trade_plan_requires_positive_reward_risk(self):
        low_reward_prediction = RangePrediction(
            signal_date="2026-01-10",
            next_trade_date="2026-01-11",
            signal_close=10.0,
            predicted_high=10.2,
            predicted_low=9.8,
            band_high=10.3,
            band_low=9.7,
            expected_close_return=0.002,
            atr=0.6,
            atr_pct=0.06,
            score=0.2,
            similar_count=10,
        )
        calibration = CalibrationResult(multiplier=1.0, coverage=0.8, avg_width_pct=0.08, candidates=[])
        config = PredictionConfig(min_reward_risk=1.6)

        watch_plan = make_trade_plan(low_reward_prediction, calibration, config)
        self.assertEqual(watch_plan.action, "WATCH")

        high_reward_prediction = RangePrediction(
            signal_date="2026-01-10",
            next_trade_date="2026-01-11",
            signal_close=10.0,
            predicted_high=11.4,
            predicted_low=9.7,
            band_high=11.5,
            band_low=9.5,
            expected_close_return=0.02,
            atr=0.4,
            atr_pct=0.04,
            score=0.8,
            similar_count=10,
        )

        buy_plan = make_trade_plan(high_reward_prediction, calibration, config)
        self.assertEqual(buy_plan.action, "BUY_ZONE")
        self.assertGreaterEqual(buy_plan.reward_risk, config.min_reward_risk)

    def test_simulate_trade_marks_same_day_stop_as_t1_locked_alert(self):
        plan = TradePlan(
            action="BUY_ZONE",
            buy_zone_low=9.8,
            buy_zone_high=10.0,
            stop_loss=9.5,
            take_profit=10.8,
            reward_risk=2.0,
            position_hint=0.2,
            reason="test",
        )
        actual = DailyBar(
            trade_date="2026-01-12",
            open=10.0,
            close=10.4,
            high=10.9,
            low=9.4,
            volume=1_000_000,
            amount=10_000_000,
            pct_change=2.0,
            turnover=1.0,
        )

        result = simulate_trade(plan, actual)

        self.assertTrue(result.entered)
        self.assertEqual(result.exit_reason, "t1_locked_stop_alert")
        self.assertEqual(result.exit_price, actual.close)
        self.assertAlmostEqual(result.gross_return, 0.04, places=6)

    def test_simulate_trade_rejects_gap_below_buy_zone(self):
        plan = TradePlan(
            action="BUY_ZONE",
            buy_zone_low=9.8,
            buy_zone_high=10.0,
            stop_loss=9.5,
            take_profit=10.8,
            reward_risk=2.0,
            position_hint=0.2,
            reason="test",
        )
        actual = DailyBar(
            trade_date="2026-01-12",
            open=9.7,
            close=10.4,
            high=10.9,
            low=9.6,
            volume=1_000_000,
            amount=10_000_000,
            pct_change=-3.0,
            turnover=1.0,
        )

        result = simulate_trade(plan, actual)

        self.assertFalse(result.entered)
        self.assertEqual(result.exit_reason, "open_below_buy_zone")

    def test_t1_position_trade_exits_on_next_day_stop_gap(self):
        plan = TradePlan(
            action="BUY_ZONE",
            buy_zone_low=9.8,
            buy_zone_high=10.0,
            stop_loss=9.5,
            take_profit=10.8,
            reward_risk=2.0,
            position_hint=0.2,
            reason="test",
        )
        bars = [
            DailyBar("2026-01-12", 10.0, 10.4, 10.9, 9.7, 1_000_000, 10_000_000, 2.0, 1.0),
            DailyBar("2026-01-13", 9.3, 9.2, 9.4, 9.0, 1_100_000, 10_000_000, -10.0, 1.0),
        ]

        result = simulate_t1_position_trade(plan, bars, entry_idx=0, max_hold_days=5)

        self.assertTrue(result.entered)
        self.assertEqual(result.entry_price, 10.0)
        self.assertEqual(result.exit_price, 9.3)
        self.assertEqual(result.exit_reason, "t1_stop_gap")
        self.assertEqual(result.entry_date, "2026-01-12")
        self.assertEqual(result.exit_date, "2026-01-13")
        self.assertEqual(result.holding_days, 1)
        self.assertAlmostEqual(result.gross_return, -0.07, places=6)

    def test_t1_position_trade_rejects_entry_day_gap_below_buy_zone(self):
        plan = TradePlan(
            action="BUY_ZONE",
            buy_zone_low=9.8,
            buy_zone_high=10.0,
            stop_loss=9.5,
            take_profit=10.8,
            reward_risk=2.0,
            position_hint=0.2,
            reason="test",
        )
        bars = [
            DailyBar("2026-01-12", 9.7, 10.2, 10.4, 9.6, 1_000_000, 10_000_000, -3.0, 1.0),
            DailyBar("2026-01-13", 10.2, 10.3, 10.5, 10.0, 1_000_000, 10_000_000, 1.0, 1.0),
        ]

        result = simulate_t1_position_trade(plan, bars, entry_idx=0, max_hold_days=5)

        self.assertFalse(result.entered)
        self.assertEqual(result.exit_reason, "open_below_buy_zone")

    def test_t1_position_trade_rejects_entry_day_stop_breach(self):
        plan = TradePlan(
            action="BUY_ZONE",
            buy_zone_low=9.8,
            buy_zone_high=10.0,
            stop_loss=9.5,
            take_profit=10.8,
            reward_risk=2.0,
            position_hint=0.2,
            reason="test",
        )
        bars = [
            DailyBar("2026-01-12", 10.2, 10.1, 10.4, 9.4, 1_000_000, 10_000_000, -1.0, 1.0),
            DailyBar("2026-01-13", 10.1, 10.3, 10.5, 10.0, 1_000_000, 10_000_000, 2.0, 1.0),
        ]

        result = simulate_t1_position_trade(plan, bars, entry_idx=0, max_hold_days=5)

        self.assertFalse(result.entered)
        self.assertEqual(result.exit_reason, "entry_day_stop_breached")

    def test_t1_position_trade_enters_entry_day_pullback_that_stays_above_stop(self):
        plan = TradePlan(
            action="BUY_ZONE",
            buy_zone_low=9.8,
            buy_zone_high=10.0,
            stop_loss=9.5,
            take_profit=10.8,
            reward_risk=2.0,
            position_hint=0.2,
            reason="test",
        )
        bars = [
            DailyBar("2026-01-12", 10.2, 10.3, 10.4, 9.8, 1_000_000, 10_000_000, 1.0, 1.0),
            DailyBar("2026-01-13", 10.3, 10.9, 11.0, 10.2, 1_000_000, 10_000_000, 5.0, 1.0),
        ]

        result = simulate_t1_position_trade(plan, bars, entry_idx=0, max_hold_days=5)

        self.assertTrue(result.entered)
        self.assertEqual(result.entry_price, 10.0)
        self.assertEqual(result.exit_reason, "t1_take_profit")
        self.assertEqual(result.exit_price, 10.8)

    def test_t1_position_trade_exits_after_max_hold_when_no_level_hits(self):
        plan = TradePlan(
            action="BUY_ZONE",
            buy_zone_low=9.8,
            buy_zone_high=10.0,
            stop_loss=9.5,
            take_profit=10.8,
            reward_risk=2.0,
            position_hint=0.2,
            reason="test",
        )
        bars = [
            DailyBar("2026-01-12", 9.9, 10.0, 10.2, 9.7, 1_000_000, 10_000_000, 0.0, 1.0),
            DailyBar("2026-01-13", 10.1, 10.2, 10.4, 9.8, 1_000_000, 10_000_000, 2.0, 1.0),
            DailyBar("2026-01-14", 10.2, 10.3, 10.5, 9.9, 1_000_000, 10_000_000, 1.0, 1.0),
            DailyBar("2026-01-15", 10.3, 10.6, 10.7, 10.0, 1_000_000, 10_000_000, 3.0, 1.0),
        ]

        result = simulate_t1_position_trade(plan, bars, entry_idx=0, max_hold_days=3)

        self.assertTrue(result.entered)
        self.assertEqual(result.exit_price, 10.6)
        self.assertEqual(result.exit_reason, "max_hold_close")
        self.assertEqual(result.exit_date, "2026-01-15")
        self.assertEqual(result.holding_days, 3)

    def test_prediction_backtest_outputs_error_and_coverage_metrics(self):
        bars = synthetic_bars(145)
        metrics, rows = backtest_predictions(bars, PredictionConfig(history_window=70), target_count=30)

        self.assertEqual(metrics["samples"], 30)
        self.assertEqual(len(rows), 30)
        self.assertIn("high_mae", metrics)
        self.assertIn("band_coverage", metrics)
        self.assertGreaterEqual(metrics["band_coverage"], 0.0)

    def test_max_drawdown_compounded_curve(self):
        self.assertAlmostEqual(max_drawdown([0.10, -0.20, 0.05]), -0.20)

    def test_parse_tencent_payload_computes_pct_change_from_previous_close(self):
        payload = {
            "data": {
                "sz300450": {
                    "qfqday": [
                        ["2026-06-08", "45.90", "43.81", "46.10", "43.39", "593518"],
                        ["2026-06-09", "44.52", "44.22", "44.74", "43.56", "217332"],
                    ]
                }
            }
        }

        bars = parse_tencent_payload("300450.SZ", payload)

        self.assertEqual(len(bars), 2)
        self.assertEqual(bars[-1].trade_date, "2026-06-09")
        self.assertAlmostEqual(bars[-1].close, 44.22)
        self.assertAlmostEqual(bars[-1].pct_change, (44.22 / 43.81 - 1) * 100, places=6)


if __name__ == "__main__":
    unittest.main()
