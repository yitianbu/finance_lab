import csv
import json
import tempfile
import unittest
from pathlib import Path

from stock_pool_scanner import (
    PoolCandidate,
    PoolScanConfig,
    evaluate_summary,
    find_kline_cache,
    load_announcement_pool,
    load_codes_file,
    scan_candidates,
    write_pool_outputs,
)


def summary(
    code: str = "300450.SZ",
    action: str = "BUY_ZONE",
    trades: int = 8,
    total_return: float = 0.12,
    max_drawdown: float = -0.03,
    band_coverage: float = 0.86,
    reward_risk: float = 2.2,
) -> dict:
    return {
        "code": code,
        "latest_bar": {"trade_date": "2026-06-09", "close": 10.0},
        "prediction": {
            "predicted_high": 10.8,
            "predicted_low": 9.7,
            "band_high": 11.0,
            "band_low": 9.0,
            "expected_close_return": 0.02,
        },
        "trade_plan": {
            "action": action,
            "buy_zone_low": 9.7,
            "buy_zone_high": 10.0,
            "stop_loss": 9.4,
            "take_profit": 10.8,
            "reward_risk": reward_risk,
            "reason": "test",
        },
        "prediction_metrics": {"band_coverage": band_coverage, "direction_hit": 0.55},
        "trade_metrics": {
            "signals": trades,
            "trades": trades,
            "total_return": total_return,
            "win_rate": 0.55,
            "profit_factor": 1.8,
            "max_drawdown": max_drawdown,
        },
        "output_dir": "/tmp/detail",
    }


class StockPoolScannerTests(unittest.TestCase):
    def test_load_codes_file_accepts_plain_lines_and_csv(self):
        with tempfile.TemporaryDirectory() as tmp:
            plain = Path(tmp) / "codes.txt"
            plain.write_text("300450\n600955.SH\n# comment\n", encoding="utf-8")
            csv_path = Path(tmp) / "codes.csv"
            with csv_path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=["secucode", "name"])
                writer.writeheader()
                writer.writerow({"secucode": "000603.SZ", "name": "盛达资源"})

            plain_candidates = load_codes_file(plain)
            csv_candidates = load_codes_file(csv_path)

            self.assertEqual([item.secucode for item in plain_candidates], ["300450.SZ", "600955.SH"])
            self.assertEqual(csv_candidates[0].secucode, "000603.SZ")
            self.assertEqual(csv_candidates[0].name, "盛达资源")

    def test_load_announcement_pool_filters_dedupes_and_sorts_recent_scores(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "events.csv"
            fieldnames = ["SECUCODE", "SECURITY_NAME_ABBR", "NOTICE_DATE", "EVENT_SCORE", "PREDICT_TYPE"]
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({"SECUCODE": "300001.SZ", "SECURITY_NAME_ABBR": "旧记录", "NOTICE_DATE": "2026-01-01", "EVENT_SCORE": "96", "PREDICT_TYPE": "预增"})
                writer.writerow({"SECUCODE": "300001.SZ", "SECURITY_NAME_ABBR": "新记录", "NOTICE_DATE": "2026-04-01", "EVENT_SCORE": "96", "PREDICT_TYPE": "预增"})
                writer.writerow({"SECUCODE": "600001.SH", "SECURITY_NAME_ABBR": "低分", "NOTICE_DATE": "2026-05-01", "EVENT_SCORE": "80", "PREDICT_TYPE": "预增"})
                writer.writerow({"SECUCODE": "920001.BJ", "SECURITY_NAME_ABBR": "北交所", "NOTICE_DATE": "2026-06-01", "EVENT_SCORE": "96", "PREDICT_TYPE": "预增"})

            candidates = load_announcement_pool(path, min_score=96, limit=10)

            self.assertEqual(len(candidates), 1)
            self.assertEqual(candidates[0].secucode, "300001.SZ")
            self.assertEqual(candidates[0].name, "新记录")
            self.assertEqual(candidates[0].source_date, "2026-04-01")

    def test_evaluate_summary_requires_action_trades_return_drawdown_and_coverage(self):
        config = PoolScanConfig(min_trades=6, min_total_return=0.03, max_drawdown=-0.08, min_band_coverage=0.8)

        accepted = evaluate_summary(PoolCandidate("300450.SZ"), summary(), config)
        rejected = evaluate_summary(
            PoolCandidate("300451.SZ"),
            summary(action="WATCH", trades=2, total_return=-0.01, max_drawdown=-0.20, band_coverage=0.6),
            config,
        )

        self.assertTrue(accepted.tradable)
        self.assertEqual(accepted.reject_reason, "")
        self.assertFalse(rejected.tradable)
        self.assertIn("not BUY_ZONE", rejected.reject_reason)
        self.assertIn("trades 2 < 6", rejected.reject_reason)
        self.assertGreater(accepted.rank_score, rejected.rank_score)

    def test_scan_candidates_sorts_tradable_first_and_records_errors(self):
        candidates = [PoolCandidate("000001.SZ"), PoolCandidate("000002.SZ"), PoolCandidate("000003.SZ")]

        def analyzer(candidate: PoolCandidate) -> dict:
            if candidate.secucode == "000003.SZ":
                raise ValueError("no data")
            if candidate.secucode == "000002.SZ":
                return summary(code=candidate.secucode, action="WATCH")
            return summary(code=candidate.secucode, total_return=0.2)

        results = scan_candidates(candidates, analyzer, PoolScanConfig())

        self.assertEqual(results[0].secucode, "000001.SZ")
        self.assertTrue(results[0].tradable)
        self.assertEqual(results[-1].status, "error")
        self.assertIn("no data", results[-1].reject_reason)

    def test_find_kline_cache_accepts_normalized_filenames(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache_dir = Path(tmp)
            expected = cache_dir / "300450_SZ.json"
            expected.write_text("{}", encoding="utf-8")

            self.assertEqual(find_kline_cache(cache_dir, "300450.SZ"), expected)
            self.assertIsNone(find_kline_cache(cache_dir, "600000.SH"))

    def test_write_pool_outputs_creates_report_csv_and_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            results = scan_candidates(
                [PoolCandidate("000001.SZ", name="测试")],
                lambda candidate: summary(code=candidate.secucode),
                PoolScanConfig(),
            )

            write_pool_outputs(Path(tmp), results, PoolScanConfig())

            self.assertTrue((Path(tmp) / "pool_scan.csv").exists())
            self.assertTrue((Path(tmp) / "pool_scan.json").exists())
            report = (Path(tmp) / "pool_scan_report.md").read_text("utf-8")
            payload = json.loads((Path(tmp) / "pool_scan.json").read_text("utf-8"))
            self.assertIn("股票池区间策略扫描", report)
            self.assertEqual(payload["results"][0]["secucode"], "000001.SZ")


if __name__ == "__main__":
    unittest.main()
