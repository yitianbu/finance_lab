import csv
import tempfile
import unittest
from pathlib import Path

from stock_all_a_scanner import load_candidates_from_events


class StockAllAScannerTests(unittest.TestCase):
    def test_load_candidates_from_events_dedupes_and_excludes_st_bj(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "events.csv"
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=["SECUCODE", "SECURITY_NAME_ABBR"])
                writer.writeheader()
                writer.writerow({"SECUCODE": "000001.SZ", "SECURITY_NAME_ABBR": "平安银行"})
                writer.writerow({"SECUCODE": "000001.SZ", "SECURITY_NAME_ABBR": "平安银行"})
                writer.writerow({"SECUCODE": "600000.SH", "SECURITY_NAME_ABBR": "浦发银行"})
                writer.writerow({"SECUCODE": "920001.BJ", "SECURITY_NAME_ABBR": "北交所"})
                writer.writerow({"SECUCODE": "000002.SZ", "SECURITY_NAME_ABBR": "ST测试"})
                writer.writerow({"SECUCODE": "000003.SZ", "SECURITY_NAME_ABBR": "退市测试"})

            candidates = load_candidates_from_events(path)

            self.assertEqual([item.secucode for item in candidates], ["000001.SZ", "600000.SH"])
            self.assertEqual(candidates[0].name, "平安银行")


if __name__ == "__main__":
    unittest.main()
