import json
import tempfile
import threading
import unittest
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import urlopen

from stock_strategy.dashboard.server import create_server


class DashboardServerTests(unittest.TestCase):
    def test_api_dashboard_returns_json_payload(self):
        with tempfile.TemporaryDirectory() as tmp:
            base_dir = Path(tmp)
            summary_dir = base_dir / "reports" / "automation_10"
            summary_dir.mkdir(parents=True)
            (summary_dir / "summary_2026-06-24.json").write_text(
                json.dumps(
                    {
                        "actual_signal_date": "2026-06-24",
                        "market": {"grade": "strong", "tradable": True},
                        "formal_candidates": [],
                    },
                    ensure_ascii=False,
                ),
                "utf-8",
            )
            server = create_server("127.0.0.1", 0, base_dir)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                with urlopen(f"http://127.0.0.1:{server.server_port}/api/dashboard", timeout=3) as response:
                    self.assertEqual(response.status, 200)
                    self.assertEqual(response.headers.get_content_type(), "application/json")
                    payload = json.loads(response.read().decode("utf-8"))
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=3)

            self.assertEqual(payload["report_date"], "2026-06-24")
            self.assertIn("market", payload)
            self.assertIn("source_files", payload)

    def test_root_serves_static_dashboard_page(self):
        with tempfile.TemporaryDirectory() as tmp:
            base_dir = Path(tmp)
            (base_dir / "reports" / "automation_10").mkdir(parents=True)
            (base_dir / "reports" / "automation_10" / "summary_2026-06-24.json").write_text(
                '{"actual_signal_date":"2026-06-24"}',
                "utf-8",
            )
            server = create_server("127.0.0.1", 0, base_dir)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                with urlopen(f"http://127.0.0.1:{server.server_port}/", timeout=3) as response:
                    self.assertEqual(response.status, 200)
                    self.assertEqual(response.headers.get_content_type(), "text/html")
                    html = response.read().decode("utf-8")
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=3)

            self.assertIn("10亿增量策略控制台", html)
            self.assertIn("5日盈利前三", html)
            self.assertIn("/api/dashboard", html)

    def test_server_rejects_path_traversal(self):
        with tempfile.TemporaryDirectory() as tmp:
            base_dir = Path(tmp)
            (base_dir / "reports" / "automation_10").mkdir(parents=True)
            (base_dir / "reports" / "automation_10" / "summary_2026-06-24.json").write_text(
                '{"actual_signal_date":"2026-06-24"}',
                "utf-8",
            )
            server = create_server("127.0.0.1", 0, base_dir)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                with self.assertRaises(HTTPError) as raised:
                    urlopen(f"http://127.0.0.1:{server.server_port}/../data/live_trading/user_positions.csv", timeout=3)
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=3)

            raised.exception.close()
            self.assertIn(raised.exception.code, {400, 404})


if __name__ == "__main__":
    unittest.main()
