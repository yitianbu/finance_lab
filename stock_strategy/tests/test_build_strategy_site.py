import json
import tempfile
import unittest
from pathlib import Path

from scripts.stock_strategy.build_strategy_site import build_static_site


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False), "utf-8")


class BuildStrategySiteTests(unittest.TestCase):
    def test_build_static_site_writes_publishable_assets_and_artifacts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_json(
                root / "reports" / "automation_10" / "summary_2026-06-24.json",
                {"actual_signal_date": "2026-06-24", "formal_candidates": []},
            )
            write_json(
                root / "reports" / "automation_5_14_50" / "20260626_145203" / "summary.json",
                {
                    "latest_date": "2026-06-26",
                    "sell_date": "2026-07-03",
                    "formal": [{"secucode": "000001.SZ", "name": "平安银行"}],
                },
            )
            report = root / "reports" / "automation_5_14_50" / "20260626_145203" / "report.md"
            report.write_text("# 候选报告\n", "utf-8")
            csv = root / "reports" / "automation_5_14_50" / "20260626_145203" / "hold5_candidates.csv"
            csv.write_text("secucode,name\n000001.SZ,平安银行\n", "utf-8")
            script = root / "scripts" / "stock_strategy" / "run_hold5_tail_candidates.py"
            script.parent.mkdir(parents=True)
            script.write_text("print('scan')\n", "utf-8")
            doc = root / "docs" / "hold5_tail_strategy_summary.md"
            doc.parent.mkdir(parents=True)
            doc.write_text("# 策略总结\n", "utf-8")

            output = root / "public"
            result = build_static_site(root, output, clean=True)

            self.assertEqual(result["strategy_count"], 8)
            self.assertGreaterEqual(result["copied_artifacts"], 4)
            self.assertTrue((output / "index.html").is_file())
            self.assertTrue((output / "app.js").is_file())
            self.assertTrue((output / "strategy_order.js").is_file())
            self.assertTrue((output / "styles.css").is_file())
            self.assertTrue((output / "dashboard.json").is_file())

            html = (output / "index.html").read_text("utf-8")
            self.assertIn('data-api="dashboard.json"', html)
            self.assertIn('data-file-base="files"', html)
            self.assertIn('href="styles.css?v=', html)
            self.assertIn('src="strategy_order.js?v=', html)
            self.assertIn('src="app.js?v=', html)

            payload = json.loads((output / "dashboard.json").read_text("utf-8"))
            self.assertEqual(payload["report_date"], "2026-06-24")
            self.assertTrue((output / "files" / "reports" / "automation_5_14_50" / "20260626_145203" / "summary.json").is_file())
            self.assertTrue((output / "files" / "scripts" / "stock_strategy" / "run_hold5_tail_candidates.py").is_file())


if __name__ == "__main__":
    unittest.main()
