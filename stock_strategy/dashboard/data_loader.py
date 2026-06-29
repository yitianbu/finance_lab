from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_BASE_DIR = Path(__file__).resolve().parents[2]
MAX_TABLE_ROWS = 200


class StrategyDashboardLoader:
    def __init__(self, base_dir: Path | str = DEFAULT_BASE_DIR) -> None:
        self.base_dir = Path(base_dir)
        self.reports_dir = self.base_dir / "reports"
        self.data_dir = self.base_dir / "data"
        self.notes: list[str] = []
        self.source_files: dict[str, str] = {}

    def load_dashboard(self) -> dict[str, Any]:
        self.notes = []
        self.source_files = {}

        automation_path = self._latest_by_name(self.reports_dir / "automation_10", "summary_*.json")
        automation = self._read_json(automation_path, "automation_summary") if automation_path else {}
        if not automation_path:
            self.notes.append("未找到最新自动化策略摘要")

        candidate_scan_path = self._latest_by_name(self.reports_dir, "automation_10_candidate_scan_*.json")
        candidate_scan = self._read_json(candidate_scan_path, "candidate_scan") if candidate_scan_path else {}

        backtest_summary_path = self._latest_by_mtime(self.reports_dir / "backtest_10b", "summary.json")
        backtest_summary = self._read_json(backtest_summary_path, "backtest_summary") if backtest_summary_path else {}
        if not backtest_summary_path:
            self.notes.append("未找到最新回测摘要")
            backtest_dir = None
        else:
            backtest_dir = backtest_summary_path.parent

        trades = self._read_csv(backtest_dir / "trades.csv", "backtest_trades") if backtest_dir else []
        market_states = self._read_csv(backtest_dir / "market_states.csv", "backtest_market_states") if backtest_dir else []

        user_positions_path = self.data_dir / "live_trading" / "user_positions.csv"
        user_positions = self._read_csv(user_positions_path, "user_positions")

        live_summary_path = self._latest_by_mtime(self.reports_dir / "live_trading", "summary.json")
        live_trading = self._read_json(live_summary_path, "live_trading_summary") if live_summary_path else {}

        hold5_summary_path = self._latest_by_mtime(self.reports_dir / "automation_5_14_50", "summary.json")
        hold5_summary = self._read_json(hold5_summary_path, "hold5_top3_summary") if hold5_summary_path else {}

        report_date = self._report_date(automation, automation_path)
        data_notes = list(automation.get("data_notes") or [])
        data_notes.extend(self.notes)

        return {
            "strategy_name": "10亿增量策略",
            "mode": "local",
            "report_date": report_date,
            "loaded_at": datetime.now(timezone.utc).isoformat(),
            "market": self._market(automation),
            "candidate_status": self._candidate_status(automation, candidate_scan),
            "t_plus_1": automation.get("t_plus_1") or {},
            "holdings_alerts": self._holdings_alerts(automation, user_positions),
            "user_positions": user_positions,
            "backtest_summary": backtest_summary,
            "trades": trades,
            "market_states": market_states,
            "live_trading": live_trading,
            "hold5_top3": self._hold5_top3(hold5_summary),
            "data_notes": data_notes,
            "source_files": self.source_files,
        }

    def _latest_by_name(self, directory: Path, pattern: str) -> Path | None:
        if not directory.exists():
            return None
        matches = sorted(directory.glob(pattern))
        return matches[-1] if matches else None

    def _latest_by_mtime(self, directory: Path, filename: str) -> Path | None:
        if not directory.exists():
            return None
        matches = [path for path in directory.rglob(filename) if path.is_file()]
        if not matches:
            return None
        return max(matches, key=lambda path: (path.stat().st_mtime, str(path)))

    def _read_json(self, path: Path | None, source_key: str) -> dict[str, Any]:
        if path is None or not path.exists():
            return {}
        try:
            payload = json.loads(path.read_text("utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            self.notes.append(f"{source_key} 读取失败：{exc}")
            return {}
        if isinstance(payload, dict):
            self._record_source(source_key, path)
            return payload
        self.notes.append(f"{source_key} 不是 JSON object")
        return {}

    def _read_csv(self, path: Path | None, source_key: str) -> list[dict[str, Any]]:
        if path is None or not path.exists():
            return []
        try:
            with path.open("r", encoding="utf-8", newline="") as handle:
                rows = [
                    {key: self._coerce(value) for key, value in row.items() if key is not None}
                    for row in csv.DictReader(handle)
                ]
        except OSError as exc:
            self.notes.append(f"{source_key} 读取失败：{exc}")
            return []
        self._record_source(source_key, path)
        return rows[:MAX_TABLE_ROWS]

    def _record_source(self, key: str, path: Path) -> None:
        try:
            self.source_files[key] = str(path.relative_to(self.base_dir))
        except ValueError:
            self.source_files[key] = path.name

    def _report_date(self, automation: dict[str, Any], automation_path: Path | None) -> str:
        for key in ("actual_signal_date", "requested_review_date", "trade_date"):
            value = automation.get(key)
            if value:
                return str(value)
        if automation_path:
            stem = automation_path.stem
            if stem.startswith("summary_"):
                return stem.removeprefix("summary_")
        return ""

    def _market(self, automation: dict[str, Any]) -> dict[str, Any]:
        market = automation.get("market")
        if not isinstance(market, dict):
            market = {}
        return {
            "grade": market.get("grade") or market.get("market_grade") or "unknown",
            "tradable": bool(market.get("tradable", False)),
            "score_avg3": market.get("score_avg3"),
            "advancers": market.get("advancers"),
            "decliners": market.get("decliners"),
            "adv_ratio": market.get("adv_ratio"),
            "limit_up": market.get("limit_up"),
            "limit_down": market.get("limit_down"),
            "limit_ratio": market.get("limit_ratio"),
            "sh_close": market.get("sh_close"),
            "cy_close": market.get("cy_close"),
            "pause_reasons": market.get("pause_reasons") or [],
            "scores": market.get("scores") or [],
        }

    def _candidate_status(self, automation: dict[str, Any], candidate_scan: dict[str, Any]) -> dict[str, Any]:
        formal_candidates = automation.get("formal_candidates") or []
        watchlist = automation.get("watchlist") or []
        scan_results = candidate_scan.get("results") or []
        block_reason = automation.get("candidate_block_reason") or ""
        if not formal_candidates and not block_reason:
            block_reason = "暂无正式候选。"
        return {
            "formal_count": len(formal_candidates),
            "watchlist_count": len(watchlist),
            "scan_initial_count": candidate_scan.get("initial_count") or automation.get("initial_count"),
            "scan_result_count": len(scan_results),
            "block_reason": block_reason,
            "formal_candidates": formal_candidates[:50],
            "watchlist": watchlist[:50],
            "scan_results": scan_results[:50],
        }

    def _holdings_alerts(self, automation: dict[str, Any], user_positions: list[dict[str, Any]]) -> list[dict[str, Any]]:
        quote_checks = automation.get("holding_quote_check") or []
        if quote_checks:
            return [
                {
                    "secucode": item.get("secucode", ""),
                    "name": item.get("name", ""),
                    "close": item.get("close"),
                    "pct_change": item.get("pct_change"),
                    "action": item.get("action") or item.get("status") or "暂无动作建议",
                    "missing": item.get("missing") or "",
                }
                for item in quote_checks
                if isinstance(item, dict)
            ]

        return [
            {
                "secucode": item.get("secucode", ""),
                "name": item.get("name", ""),
                "close": None,
                "pct_change": None,
                "action": item.get("notes") or "本地持仓，暂无当日行情校验。",
                "missing": "未找到持仓行情检查结果",
            }
            for item in user_positions
            if item.get("status") in ("holding", "")
        ]

    def _hold5_top3(self, summary: dict[str, Any]) -> dict[str, Any]:
        formal = summary.get("formal") or []
        watch = summary.get("watch") or []
        picks = [item for item in formal if isinstance(item, dict)][:3]
        return {
            "strategy_name": "5日盈利前三",
            "generated_at": summary.get("generated_at") or "",
            "latest_date": summary.get("latest_date") or "",
            "sell_date": summary.get("sell_date") or "",
            "eligible_count": summary.get("eligible_count"),
            "validated_count": summary.get("validated_count"),
            "adv_ratio": summary.get("adv_ratio"),
            "top_industries": summary.get("top_industries") or "",
            "formal_count": len(formal),
            "watch_count": len(watch),
            "picks": picks,
        }

    def _coerce(self, value: Any) -> Any:
        if value is None:
            return ""
        if not isinstance(value, str):
            return value
        text = value.strip()
        if text == "":
            return ""
        if text == "True":
            return True
        if text == "False":
            return False
        try:
            if "." not in text and "e" not in text.lower():
                return int(text)
            return float(text)
        except ValueError:
            return text
