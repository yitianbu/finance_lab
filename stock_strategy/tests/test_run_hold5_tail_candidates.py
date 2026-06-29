import unittest

from scripts.stock_strategy.run_hold5_tail_candidates import (
    Quote,
    apply_attack_mode_preference,
    apply_strategy_switch,
    candidate_quality_score,
    classify_risk_tier,
    evaluate_attack_mode,
    evaluate_strategy_switch,
    recheck_top_rows,
)


def make_quote(code: str, price: float, low: float, high: float, open_: float | None = None) -> Quote:
    market = 1 if code.startswith("6") else 0
    return Quote(
        secucode=f"{code}.{'SH' if market == 1 else 'SZ'}",
        code=code,
        name="测试",
        market=market,
        price=price,
        pct=0.01,
        change=0.1,
        volume=100000,
        amount=500000000,
        high=high,
        low=low,
        open=open_ if open_ is not None else price,
        prev_close=price / 1.01,
        turnover=3.2,
        volume_ratio=1.1,
        main_net=1000000,
        main_net_pct=0.002,
        industry="测试行业",
        timestamp="2026-06-29T14:50:00",
    )


def make_row(idx: int, formal: bool = True) -> dict:
    code = f"300{idx:03d}.SZ"
    return {
        "secucode": code,
        "name": f"测试{idx}",
        "industry": "测试行业",
        "quote_time": "2026-06-29T14:49:00",
        "latest_date": "2026-06-29",
        "price": 10.0 + idx,
        "pct": 0.01,
        "amount": 500000000,
        "turnover": 3.0,
        "volume_ratio": 1.0,
        "main_net": 1000000,
        "industry_avg_pct": 0.02,
        "industry_adv_ratio": 0.8,
        "industry_amount": 1000000000,
        "close_pos": 0.8,
        "upper_shadow": 0.1,
        "samples": 120,
        "win_rate": 0.6,
        "avg_return": 0.03,
        "median_return": 0.02,
        "profit_factor": 2.0,
        "max_drawdown": -0.1,
        "worst_return": -0.08,
        "worst_sample_date": "2026-01-01",
        "worst_hold_drawdown": -0.1,
        "stop_loss": 9.5,
        "stop_risk": 0.05,
        "target_low": 10.2 + idx,
        "target_high": 10.5 + idx,
        "reward_risk": 1.5,
        "buy_low": (10.0 + idx) * 0.997,
        "buy_high": (10.0 + idx) * 1.003,
        "formal": formal,
        "reject_reason": "",
        "score": 100 - idx,
    }


def make_switch_meta(
    adv_ratio: float = 0.58,
    sh_pct: float = 0.01,
    sz_pct: float = 0.01,
    cy_pct: float = -0.002,
) -> dict:
    return {
        "adv_ratio": adv_ratio,
        "sh_pct": sh_pct,
        "sz_pct": sz_pct,
        "cy_pct": cy_pct,
    }


class Hold5TailCandidateRecheckTests(unittest.TestCase):
    def test_recheck_fetches_only_top_ten_rows(self):
        rows = [make_row(idx) for idx in range(12)]
        requested: list[str] = []

        def fetcher(secucodes: list[str]) -> dict[str, Quote]:
            requested.extend(secucodes)
            return {code: make_quote(code.split(".")[0], 20.0, 19.0, 21.0) for code in secucodes}

        rechecked, errors = recheck_top_rows(rows, fetcher, top_n=10)

        self.assertEqual(errors, [])
        self.assertEqual(requested, [row["secucode"] for row in rows[:10]])
        self.assertEqual(sum(row["rechecked"] for row in rechecked), 10)
        self.assertFalse(rechecked[10]["rechecked"])
        self.assertEqual(rechecked[10]["recheck_reject_reason"], "")

    def test_recheck_downgrades_candidate_when_tail_position_turns_weak(self):
        rows = [make_row(1)]

        def fetcher(secucodes: list[str]) -> dict[str, Quote]:
            return {secucodes[0]: make_quote("300001", 10.1, 10.0, 12.0, open_=11.8)}

        rechecked, errors = recheck_top_rows(rows, fetcher, top_n=10)

        self.assertEqual(errors, [])
        row = rechecked[0]
        self.assertFalse(row["formal"])
        self.assertIn("recheck_weak_tail_position", row["reject_reason"])
        self.assertEqual(row["recheck_price"], 10.1)
        self.assertAlmostEqual(row["buy_low"], 10.1 * 0.997)
        self.assertLess(row["close_pos"], 0.5)


class Hold5StrategySwitchTests(unittest.TestCase):
    def test_candidate_quality_score_penalizes_left_tail_even_with_same_average(self):
        safer = candidate_quality_score(
            win_rate=0.60,
            avg_return=0.03,
            median_return=0.025,
            profit_factor=2.0,
            reward_risk=1.4,
            worst_return=-0.08,
            worst_hold_drawdown=-0.10,
            sample_max_drawdown=-0.20,
            close_pos=0.75,
            amount=500000000,
            industry_avg_pct=0.01,
            industry_adv_ratio=0.70,
            ret5=0.06,
            dist_ma20=0.08,
            vol_ratio_log=0.50,
        )
        fragile = candidate_quality_score(
            win_rate=0.60,
            avg_return=0.03,
            median_return=0.025,
            profit_factor=2.0,
            reward_risk=1.4,
            worst_return=-0.20,
            worst_hold_drawdown=-0.24,
            sample_max_drawdown=-0.45,
            close_pos=0.75,
            amount=500000000,
            industry_avg_pct=0.01,
            industry_adv_ratio=0.70,
            ret5=0.06,
            dist_ma20=0.08,
            vol_ratio_log=0.50,
        )

        self.assertGreater(safer, fragile)

    def test_classifies_core_candidate_when_left_tail_is_clean(self):
        row = make_row(1)

        self.assertEqual(classify_risk_tier(row), "核心")

    def test_red_switch_downgrades_all_candidates_when_recent_strategy_is_losing(self):
        rows = [make_row(1), make_row(2), make_row(3)]
        meta = make_switch_meta()
        recent = {
            "avg_return": -0.01,
            "win_rate": 0.45,
            "worst_return": -0.08,
            "excess_return": -0.02,
        }

        decision = evaluate_strategy_switch(meta, rows, recent)
        switched = apply_strategy_switch(rows, decision)

        self.assertEqual(decision["state"], "红色")
        self.assertIn("recent_loss_regime", decision["reasons"])
        self.assertTrue(all(not row["formal"] for row in switched))
        self.assertTrue(all("strategy_switch_red" in row["reject_reason"] for row in switched))

    def test_yellow_switch_keeps_aggressive_names_as_research_only(self):
        rows = [make_row(1), make_row(2), make_row(3)]
        for row in rows:
            row["reward_risk"] = 1.0

        decision = evaluate_strategy_switch(make_switch_meta(), rows, None)
        switched = apply_strategy_switch(rows, decision)

        self.assertEqual(decision["state"], "黄色")
        self.assertTrue(all(row["risk_tier"] == "进取" for row in switched[:3]))
        self.assertTrue(all(row["action_tier"] == "进取研究" for row in switched[:3]))
        self.assertTrue(all(not row["formal"] for row in switched[:3]))

    def test_no_core_left_tail_cluster_is_warning_when_recent_regime_is_healthy(self):
        rows = [make_row(1), make_row(2), make_row(3)]
        for row in rows:
            row["worst_return"] = -0.16
            row["worst_hold_drawdown"] = -0.20
            row["max_drawdown"] = -0.30

        recent = {
            "avg_return": 0.02,
            "win_rate": 0.60,
            "worst_return": -0.08,
            "excess_return": 0.01,
            "medium_avg_return": 0.03,
            "medium_win_rate": 0.65,
            "medium_excess_return": 0.02,
        }
        decision = evaluate_strategy_switch(make_switch_meta(), rows, recent)
        switched = apply_strategy_switch(rows, decision)

        self.assertEqual(decision["state"], "黄色")
        self.assertIn("no_core_left_tail_warning", decision["reasons"])
        self.assertTrue(all(row["action_tier"] == "进取研究" for row in switched[:3]))

    def test_no_core_left_tail_cluster_blocks_when_loss_regime_is_confirmed(self):
        rows = [make_row(1), make_row(2), make_row(3)]
        for row in rows:
            row["worst_return"] = -0.16
            row["worst_hold_drawdown"] = -0.20
            row["max_drawdown"] = -0.30
        recent = {
            "avg_return": -0.03,
            "win_rate": 0.35,
            "worst_return": -0.15,
            "excess_return": -0.04,
            "medium_avg_return": -0.04,
            "medium_win_rate": 0.35,
            "medium_excess_return": -0.04,
        }

        decision = evaluate_strategy_switch(make_switch_meta(), rows, recent)
        switched = apply_strategy_switch(rows, decision)

        self.assertEqual(decision["state"], "红色")
        self.assertIn("confirmed_loss_regime", decision["reasons"])
        self.assertIn("confirmed_loss_regime_with_left_tail", decision["reasons"])
        self.assertTrue(all(row["action_tier"] == "观察" for row in switched[:3]))

    def test_good_reward_risk_does_not_override_losing_recent_backtest(self):
        rows = [make_row(1), make_row(2), make_row(3)]
        for row in rows:
            row["reward_risk"] = 1.6
            row["worst_return"] = -0.16
            row["worst_hold_drawdown"] = -0.20
        recent = {
            "avg_return": -0.0348,
            "win_rate": 0.31,
            "worst_return": -0.2663,
            "excess_return": -0.04,
            "medium_avg_return": -0.03,
            "medium_win_rate": 0.35,
            "medium_excess_return": -0.04,
        }

        decision = evaluate_strategy_switch(make_switch_meta(), rows, recent)
        switched = apply_strategy_switch(rows, decision)

        self.assertEqual(decision["state"], "红色")
        self.assertIn("confirmed_loss_regime", decision["reasons"])
        self.assertTrue(all(row["action_tier"] == "观察" for row in switched[:3]))

    def test_short_term_loss_does_not_block_when_medium_regime_is_healthy(self):
        rows = [make_row(1), make_row(2), make_row(3)]
        for row in rows:
            row["reward_risk"] = 1.6
            row["worst_return"] = -0.16
            row["worst_hold_drawdown"] = -0.20
        recent = {
            "avg_return": -0.01,
            "win_rate": 0.40,
            "worst_return": -0.13,
            "excess_return": 0.002,
            "consecutive_loss_days": 4,
            "medium_avg_return": 0.014,
            "medium_win_rate": 0.65,
            "medium_excess_return": 0.026,
        }

        decision = evaluate_strategy_switch(make_switch_meta(), rows, recent)
        switched = apply_strategy_switch(rows, decision)

        self.assertEqual(decision["state"], "黄色")
        self.assertNotIn("confirmed_loss_regime", decision["reasons"])
        self.assertTrue(all(row["action_tier"] == "进取研究" for row in switched[:3]))

    def test_medium_absolute_loss_with_positive_excess_does_not_confirm_loss_regime(self):
        rows = [make_row(1), make_row(2), make_row(3)]
        for row in rows:
            row["reward_risk"] = 1.6
            row["worst_return"] = -0.16
            row["worst_hold_drawdown"] = -0.20
        recent = {
            "avg_return": -0.03,
            "win_rate": 0.30,
            "worst_return": -0.13,
            "excess_return": -0.02,
            "consecutive_loss_days": 3,
            "medium_avg_return": -0.003,
            "medium_win_rate": 0.55,
            "medium_excess_return": 0.008,
        }

        decision = evaluate_strategy_switch(make_switch_meta(), rows, recent)

        self.assertEqual(decision["state"], "黄色")
        self.assertNotIn("confirmed_loss_regime", decision["reasons"])

    def test_benchmark_gate_blocks_when_medium_strategy_cannot_beat_index(self):
        rows = [make_row(1), make_row(2), make_row(3)]
        recent = {
            "avg_return": 0.01,
            "win_rate": 0.55,
            "worst_return": -0.08,
            "excess_return": 0.002,
            "medium_sample_days": 30,
            "medium_avg_return": 0.007,
            "medium_win_rate": 0.55,
            "medium_excess_return": 0.001,
            "medium_excess_best_return": -0.010,
            "medium_max_drawdown": -0.40,
        }

        decision = evaluate_strategy_switch(make_switch_meta(), rows, recent)
        switched = apply_strategy_switch(rows, decision)

        self.assertEqual(decision["state"], "红色")
        self.assertIn("benchmark_gate_underperforming", decision["reasons"])
        self.assertTrue(all(row["action_tier"] == "观察" for row in switched[:3]))

    def test_benchmark_gate_allows_recent_profit_regime(self):
        rows = [make_row(1), make_row(2), make_row(3)]
        for row in rows:
            row["reward_risk"] = 1.6
            row["worst_return"] = -0.16
            row["worst_hold_drawdown"] = -0.20
        recent = {
            "avg_return": 0.06,
            "win_rate": 0.70,
            "worst_return": -0.05,
            "excess_return": 0.04,
            "medium_sample_days": 30,
            "medium_avg_return": 0.009,
            "medium_win_rate": 0.50,
            "medium_excess_return": 0.04,
            "medium_excess_best_return": -0.020,
            "medium_max_drawdown": -0.60,
        }

        decision = evaluate_strategy_switch(make_switch_meta(), rows, recent)

        self.assertEqual(decision["state"], "黄色")
        self.assertNotIn("benchmark_gate_underperforming", decision["reasons"])

    def test_legacy_medium_metrics_do_not_evaluate_optimized_benchmark_gate(self):
        rows = [make_row(1), make_row(2), make_row(3)]
        recent = {
            "avg_return": 0.06,
            "win_rate": 0.70,
            "worst_return": -0.05,
            "excess_return": 0.04,
            "medium_sample_days": 30,
            "medium_avg_return": 0.009,
            "medium_win_rate": 0.50,
            "medium_excess_return": 0.04,
        }

        decision = evaluate_strategy_switch(make_switch_meta(), rows, recent)

        self.assertFalse(decision["benchmark_gate_evaluated"])
        self.assertNotIn("benchmark_gate_underperforming", decision["reasons"])

    def test_green_switch_allows_core_formal_candidates(self):
        rows = [make_row(1), make_row(2), make_row(3)]

        decision = evaluate_strategy_switch(make_switch_meta(), rows, {"avg_return": 0.02, "win_rate": 0.6, "worst_return": -0.08, "excess_return": 0.01})
        switched = apply_strategy_switch(rows, decision)

        self.assertEqual(decision["state"], "绿色")
        self.assertTrue(all(row["risk_tier"] == "核心" for row in switched[:3]))
        self.assertTrue(all(row["action_tier"] == "正式核心" for row in switched[:3]))
        self.assertTrue(all(row["formal"] for row in switched[:3]))


class Hold5AttackModeTests(unittest.TestCase):
    def test_attack_mode_promotes_risk_focused_candidate_in_strong_regime(self):
        rows = [make_row(idx) for idx in range(1, 11)]
        for row in rows[:3]:
            row["avg_return"] = 0.04
            row["win_rate"] = 0.62
            row["profit_factor"] = 2.0
            row["reward_risk"] = 1.2
            row["worst_return"] = -0.10
            row["worst_hold_drawdown"] = -0.12
        rows[7]["avg_return"] = 0.08
        rows[7]["win_rate"] = 0.76
        rows[7]["profit_factor"] = 6.0
        rows[7]["reward_risk"] = 2.2
        rows[7]["worst_return"] = -0.08
        rows[7]["worst_hold_drawdown"] = -0.10
        recent = {
            "medium_sample_days": 30,
            "medium_avg_return": 0.07,
            "medium_win_rate": 0.70,
            "medium_excess_best_return": 0.01,
            "medium_max_drawdown": -0.20,
        }

        decision = evaluate_attack_mode(rows, recent)
        preferred = apply_attack_mode_preference(rows, decision)

        self.assertTrue(decision["enabled"])
        self.assertEqual(decision["preferred_secucode"], rows[7]["secucode"])
        self.assertTrue(preferred[7]["attack_mode_preferred"])
        self.assertIn("attack_mode_preferred", preferred[7]["attack_mode_reason"])

    def test_attack_mode_stays_off_when_recent_regime_is_not_strong(self):
        rows = [make_row(idx) for idx in range(1, 11)]
        recent = {
            "medium_sample_days": 30,
            "medium_avg_return": 0.02,
            "medium_win_rate": 0.70,
            "medium_excess_best_return": 0.01,
            "medium_max_drawdown": -0.20,
        }

        decision = evaluate_attack_mode(rows, recent)
        preferred = apply_attack_mode_preference(rows, decision)

        self.assertFalse(decision["enabled"])
        self.assertTrue(all(not row["attack_mode_preferred"] for row in preferred))


if __name__ == "__main__":
    unittest.main()
