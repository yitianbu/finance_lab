from __future__ import annotations

import csv
import json
import re
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

        hold5_summary_path = self._latest_hold5_candidate_path("summary.json")
        hold5_summary = self._read_json(hold5_summary_path, "hold5_top3_summary") if hold5_summary_path else {}
        long_term_scan_path = self._latest_by_mtime(self.reports_dir / "long_term_hold", "long_term_hold_scan.json")
        long_term_scan = self._read_json(long_term_scan_path, "long_term_hold_scan") if long_term_scan_path else {}
        long_term_daily_path = self._latest_long_term_daily_summary_path()
        long_term_daily = self._read_json(long_term_daily_path, "long_term_hold_daily") if long_term_daily_path else {}
        range_review_path = self._latest_by_mtime(self.reports_dir / "range_trader", "recommendation_review_*.csv")
        range_review = self._read_csv(range_review_path, "range_recommendation_review") if range_review_path else []
        crowding_path = self._latest_by_mtime(self.reports_dir / "crowding_warning", "crowding_warning_v2_current_*.json")
        crowding = self._read_json(crowding_path, "crowding_warning_summary") if crowding_path else {}

        report_date = self._report_date(automation, automation_path)
        data_notes = list(automation.get("data_notes") or [])
        data_notes.extend(self.notes)

        return {
            "strategy_name": "10亿增量策略",
            "mode": "local",
            "report_date": report_date,
            "loaded_at": datetime.now(timezone.utc).isoformat(),
            "strategy_catalog": self._strategy_catalog(
                hold5_summary,
                long_term_scan,
                long_term_daily,
                automation,
                candidate_scan,
                live_trading,
                range_review,
                crowding,
            ),
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
        active_positions = [
            item
            for item in user_positions
            if str(item.get("status") or "").strip() in ("", "holding")
        ]
        active_codes = {str(item.get("secucode") or "") for item in active_positions if item.get("secucode")}
        quote_checks = automation.get("holding_quote_check") or []
        if quote_checks:
            checks = [
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
            if active_codes:
                active_checks = [item for item in checks if item.get("secucode") in active_codes]
                if active_checks:
                    return active_checks
            elif checks:
                return checks

        return [
            {
                "secucode": item.get("secucode", ""),
                "name": item.get("name", ""),
                "close": None,
                "pct_change": None,
                "action": item.get("notes") or "本地持仓，暂无当日行情校验。",
                "missing": "未找到持仓行情检查结果",
            }
            for item in active_positions
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

    def _strategy_catalog(
        self,
        hold5_summary: dict[str, Any] | None = None,
        long_term_scan: dict[str, Any] | None = None,
        long_term_daily: dict[str, Any] | None = None,
        automation: dict[str, Any] | None = None,
        candidate_scan: dict[str, Any] | None = None,
        live_trading: dict[str, Any] | None = None,
        range_review: list[dict[str, Any]] | None = None,
        crowding: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        return [
            {
                "id": "hold5-tail",
                "name": "14:50 尾盘5日持有",
                "status": "生产保留",
                "tone": "good",
                "cadence": "交易日 14:50",
                "mode": "候选输出",
                "objective": "在尾盘用全A实时快照筛出可研究的5个交易日持有候选，并用策略状态拦截控制新开仓节奏。",
                "workflow": ["全A实时快照", "硬过滤", "相似样本验证", "Top10复核", "风险分层"],
                "workflow_notes": [
                    {"label": "全A实时快照", "description": "14:50 左右读取全市场实时快照，先得到当天可研究的真实候选池。"},
                    {"label": "硬过滤", "description": "剔除 ST、停牌、价格异常、流动性不足和一字板等不适合成交的标的。"},
                    {"label": "相似样本验证", "description": "按历史近似样本统计 5 日胜率、平均收益、利润因子、左尾和持有期回撤。"},
                    {"label": "Top10复核", "description": "对最终候选再拉轻量报价，尾盘价格恶化、回落或接近不可成交状态时降级。"},
                    {"label": "风险分层", "description": "输出正式核心、进取研究和观察名单；策略红灯时默认不建议新开仓。"},
                ],
                "detail_sections": self._hold5_detail_sections(hold5_summary or {}),
                "latest_advice": self._hold5_latest_advice(hold5_summary or {}),
                "signals": [
                    "旧底层排序：胜率、平均5日收益、利润因子、尾盘位置、成交额、板块共振和主力净额。",
                    "30样本强收益状态拦截：平均收益、胜率、相对最强指数超额和滚动最大回撤同时达标。",
                    "强行情攻击模式只调整同层级排序，不跳过红色策略状态。",
                ],
                "risk_controls": [
                    "剔除 ST、停牌、价格异常、流动性不足和明显无法成交的一字板。",
                    "最终候选 Top10 轻量实时报价复核，尾盘恶化时降级。",
                    "核心、进取、观察分层输出；策略红灯时默认不建议新开仓。",
                ],
                "outputs": ["Top3/Top10 候选", "买入区间与5日目标", "风险层级", "计划卖出日"],
                "limits": ["代理回测基于日线收盘，不是历史14:50盘口回放。", "候选只用于研究，不连接券商、不自动下单。"],
                "metrics": [
                    {"label": "强收益拦截窗口", "value": "30 批"},
                    {"label": "最低完成样本", "value": "12 批"},
                    {"label": "最低胜率", "value": "50%"},
                    {"label": "持有周期", "value": "5 日"},
                ],
                "scripts": [
                    self._artifact("候选扫描", "scripts/stock_strategy/run_hold5_tail_candidates.py"),
                    self._artifact("代理回测", "scripts/stock_strategy/backtest_hold5_tail_proxy.py"),
                    self._artifact("持仓跟踪", "scripts/stock_strategy/hold5_position_tracker.py"),
                    self._artifact("真实推荐复盘", "scripts/stock_strategy/replay_saved_recommendation_execution.py"),
                ],
                "docs": [
                    self._artifact("策略总结", "docs/hold5_tail_strategy_summary.md"),
                    self._artifact("动态执行设计", "docs/superpowers/specs/2026-06-30-hold5-dynamic-execution-design.md"),
                ],
                "reports": [
                    self._latest_hold5_candidate_artifact("最新候选摘要", "summary.json"),
                    self._latest_hold5_candidate_artifact("最新策略报告", "report.md"),
                    self._latest_hold5_candidate_artifact("最新候选CSV", "hold5_candidates.csv"),
                ],
            },
            {
                "id": "hold5-dynamic-execution",
                "name": "动态执行模式",
                "status": "执行增强",
                "tone": "good",
                "cadence": "14:50 信号后",
                "mode": "第一名 / Top3 切换",
                "objective": "在每日固定资金单位约束下，根据策略状态和第一名相对优势，在第一名集中买入与 Top3 等权之间切换。",
                "workflow": ["近期真实报告", "recent_metrics", "候选质量", "第一名优势判断", "执行模式建议"],
                "latest_advice": self._hold5_dynamic_latest_advice(hold5_summary or {}),
                "signals": [
                    "策略状态先行：红灯时不新开仓。",
                    "第一名在平均收益、胜率、利润因子、reward/risk 和左尾风险上显著不弱于 Top3 时集中。",
                    "候选分歧较大或单票风险较高时回到 Top3 等权。",
                ],
                "risk_controls": [
                    "攻击模式只能影响首选排序，不能放行红色状态。",
                    "资金占用按每天3份、持有5个交易日估算。",
                    "真实报告复盘、缺失日期补算和代理长期回测分开展示。",
                ],
                "outputs": ["第一名买3", "Top3等权", "不新开仓", "触发原因"],
                "limits": ["真实样本仍少，不能直接证明第一名长期优于 Top3。"],
                "metrics": [
                    {"label": "固定投入单位", "value": "3"},
                    {"label": "最大滚动占用", "value": "15"},
                    {"label": "默认持有", "value": "5 日"},
                ],
                "scripts": [
                    self._artifact("候选扫描", "scripts/stock_strategy/run_hold5_tail_candidates.py"),
                    self._artifact("复盘执行", "scripts/stock_strategy/replay_saved_recommendation_execution.py"),
                ],
                "docs": [
                    self._artifact("动态执行设计", "docs/superpowers/specs/2026-06-30-hold5-dynamic-execution-design.md"),
                    self._artifact("策略总结", "docs/hold5_tail_strategy_summary.md"),
                ],
                "reports": [
                    self._latest_artifact("动态执行代理", "reports/automation_5_14_50/dynamic_execution_one_year_proxy_20260630_from215123", "summary.json"),
                    self._latest_artifact("模式切换回测", "reports/automation_5_14_50/mode_switch_backtest_fast_20260629_214055", "summary.json"),
                    self._latest_artifact("近期推荐盈亏", "reports/automation_5_14_50/recent3_recommendation_pnl_asof_20260703", "report.md"),
                ],
            },
            {
                "id": "ten-billion-turnover",
                "name": "10亿增量策略",
                "status": "回测策略",
                "tone": "info",
                "cadence": "盘后/本地报告",
                "mode": "全A技术面近似",
                "objective": "寻找成交额增量、市场状态和风险收益结构较好的短线候选，并用市场状态曲线和回测结果审计。",
                "workflow": ["全A行情", "增量过滤", "市场状态门", "候选输出", "组合回测"],
                "latest_advice": self._ten_billion_latest_advice(automation or {}, candidate_scan or {}),
                "signals": [
                    "成交额增量和价格行为构成基础候选。",
                    "市场状态门使用上涨家数、涨跌停结构、指数状态等信息控制是否交易。",
                    "回测输出交易、市场状态曲线和组合权益指标。",
                ],
                "risk_controls": [
                    "市场不可交易时暂停。",
                    "公告、减持、处罚等过滤在离线回测中可能无法完整复原。",
                    "仅做本地研究，不直接接券商接口。",
                ],
                "outputs": ["自动化摘要", "候选扫描结果", "回测交易", "市场状态曲线"],
                "limits": ["当前回测是技术面近似，不等同完整公告口径实盘复盘。"],
                "metrics": [
                    {"label": "默认报告源", "value": "automation_10"},
                    {"label": "回测源", "value": "backtest_10b"},
                ],
                "scripts": [
                    self._artifact("10亿回测", "scripts/stock_strategy/backtest_10b_tencent.py"),
                    self._artifact("控制台服务", "scripts/stock_strategy/serve_strategy_dashboard.py"),
                ],
                "docs": [
                    self._artifact("优化设计", "docs/superpowers/specs/2026-06-10-10b-strategy-optimization-design.md"),
                    self._artifact("README", "README.md"),
                ],
                "reports": [
                    self._latest_artifact("最新自动化摘要", "reports/automation_10", "summary_*.json"),
                    self._latest_artifact("最新候选扫描", "reports", "automation_10_candidate_scan_*.json"),
                    self._latest_artifact("最新回测摘要", "reports/backtest_10b", "summary.json"),
                ],
            },
            {
                "id": "announcement-earnings",
                "name": "业绩预告公告策略",
                "status": "纸面前策略",
                "tone": "warn",
                "cadence": "公告披露后",
                "mode": "事件驱动",
                "objective": "根据业绩预告质量、公告前涨幅、缺口和风控约束，在公告次一交易日生成可回测交易。",
                "workflow": ["公告事件", "事件评分", "开盘过滤", "止盈止损", "现金组合模拟"],
                "latest_advice": self._announcement_latest_advice(),
                "signals": [
                    "默认 `benchmark_constrained`：分数高、预测净利上限、排除不稳定月份。",
                    "公告次一交易日开盘买入，默认持有5日。",
                    "用惊喜度排序，同日最多限定新开仓数量。",
                ],
                "risk_controls": [
                    "过滤过高/过低开盘缺口、一字涨停和公告前5日过度上涨。",
                    "默认4%止损、12%止盈，计入手续费、印花税和滑点。",
                    "单票仓位和单日数量受配置约束。",
                ],
                "outputs": ["回测报告", "候选交易", "训练参数报告", "公告推荐"],
                "limits": ["事件数据覆盖范围影响结果；历史公告收益不代表未来表现。"],
                "metrics": [
                    {"label": "默认策略", "value": "benchmark_constrained"},
                    {"label": "默认持有", "value": "5 日"},
                    {"label": "默认止损", "value": "4%"},
                    {"label": "默认止盈", "value": "12%"},
                ],
                "scripts": [
                    self._artifact("公告回测", "stock_strategy/announcement_backtest.py"),
                    self._artifact("全量公告推荐", "scripts/stock_strategy/review_all_a_range_candidates.py"),
                ],
                "docs": [
                    self._artifact("公告推荐设计", "docs/superpowers/specs/2026-06-15-full-announcement-recommendations-design.md"),
                    self._artifact("纸面实盘设计", "docs/superpowers/specs/2026-06-09-live-paper-trading-design.md"),
                ],
                "reports": [
                    self._latest_artifact("公告回测报告", "reports/announcement_backtest", "report.md"),
                    self._latest_artifact("训练报告", "reports/announcement_backtest_training", "report.md"),
                    self._latest_artifact("全量推荐", "reports/full_announcement_recommendations", "*.md"),
                ],
            },
            {
                "id": "range-trader",
                "name": "次日区间 / 股票池扫描",
                "status": "扫描工具",
                "tone": "info",
                "cadence": "按需运行",
                "mode": "单股区间预测 + 批量排名",
                "objective": "用相似历史窗口、ATR 校准和交易计划，为单股或候选池生成次日买入区间与风险收益排序。",
                "workflow": ["K线缓存", "相似窗口", "ATR区间", "交易计划", "池内排名"],
                "latest_advice": self._range_trader_latest_advice(range_review or []),
                "signals": [
                    "单股模型输出预测高低点、买入区间、止损止盈和 reward/risk。",
                    "股票池扫描只把 BUY_ZONE、交易样本足够、收益为正且回撤可控的标为可交易。",
                    "失败项保留拒绝原因，便于审计。",
                ],
                "risk_controls": [
                    "最小交易样本数、最大回撤、最小区间覆盖率共同约束。",
                    "不做分时盘口预测，不下真实订单。",
                ],
                "outputs": ["单股详细报告", "池扫描 Markdown", "CSV/JSON 审计文件"],
                "limits": ["依赖日线缓存质量；ATR 区间不是盘口成交保证。"],
                "metrics": [
                    {"label": "默认历史窗口", "value": "90 日"},
                    {"label": "默认相似样本", "value": "15"},
                    {"label": "目标覆盖率", "value": "80%"},
                ],
                "scripts": [
                    self._artifact("单股区间", "stock_strategy/stock_range_trader.py"),
                    self._artifact("股票池扫描", "stock_strategy/stock_pool_scanner.py"),
                ],
                "docs": [
                    self._artifact("池扫描设计", "docs/superpowers/specs/2026-06-09-stock-pool-range-scan-design.md"),
                    self._artifact("区间交易计划", "docs/superpowers/plans/2026-06-09-stock-range-trader.md"),
                ],
                "reports": [
                    self._latest_artifact("股票池扫描报告", "reports/range_trader", "pool_scan_report.md"),
                    self._latest_artifact("单股区间报告", "reports/range_trader", "range_report.md"),
                    self._latest_artifact("扫描摘要", "reports/range_trader", "summary.json"),
                ],
            },
            {
                "id": "live-paper-trading",
                "name": "公告策略纸面实盘",
                "status": "纸面运行",
                "tone": "warn",
                "cadence": "每日",
                "mode": "账户级审计",
                "objective": "把公告回测策略推进到实盘前流程，生成订单、成交、持仓、资金和风控日报，但不连接券商。",
                "workflow": ["信号生成", "风控过滤", "纸面订单", "账本更新", "每日报告"],
                "latest_advice": self._live_paper_latest_advice(live_trading or {}),
                "signals": [
                    "默认使用公告策略 `benchmark_constrained` 作为信号源。",
                    "账户资金、仓位、黑名单、ST/退市风险和行情新鲜度共同决定是否放行。",
                    "每日输出可复查 CSV 和 Markdown 报告。",
                ],
                "risk_controls": [
                    "默认资金 1,000,000 元，单票目标仓位20%，组合总仓位80%。",
                    "单日最多5笔新买入，单票最小成交金额10,000元。",
                    "行情缺失或日期不新鲜时拒绝实盘买入。",
                ],
                "outputs": ["orders.csv", "positions.csv", "fills.csv", "daily_report.md", "summary.json"],
                "limits": ["纸面成交使用计划价或日线近似，不等于真实交易可成交。"],
                "metrics": [
                    {"label": "默认资金", "value": "100万"},
                    {"label": "单票目标", "value": "20%"},
                    {"label": "组合上限", "value": "80%"},
                ],
                "scripts": [
                    self._artifact("纸面实盘", "stock_strategy/live_trader.py"),
                ],
                "docs": [
                    self._artifact("纸面实盘设计", "docs/superpowers/specs/2026-06-09-live-paper-trading-design.md"),
                ],
                "reports": [
                    self._latest_artifact("最新纸面摘要", "reports/live_trading", "summary.json"),
                    self._latest_artifact("最新纸面日报", "reports/live_trading", "daily_report.md"),
                ],
            },
            {
                "id": "long-term-hold",
                "name": "长期持有跑赢大盘",
                "status": "新增研究",
                "tone": "info",
                "cadence": "盘后/周度复核",
                "mode": "单股长期相对强势",
                "objective": "寻找长期趋势向上且持续跑赢基准的股票，尽量减少买卖，只在趋势或相对收益恶化时退出。",
                "workflow": ["日线K线", "长期均线", "相对基准", "低换手买点", "持仓卖点"],
                "latest_advice": self._long_term_hold_latest_advice(long_term_scan or {}, long_term_daily or {}),
                "signals": [
                    "收盘价在 MA200 上方，且 MA60 > MA120 > MA200。",
                    "120日和240日收益均要求跑赢基准，默认基准为沪深300 `000300.SH`。",
                    "回撤、波动率和距离 MA200 的偏离共同过滤过热或失控标的。",
                ],
                "risk_controls": [
                    "买点限制在信号收盘价下方3%到上方3%之间，避免追高。",
                    "初始止损取买入价下方12%与 MA200 下方3%中的更高者。",
                    "全A组合回测默认只买 rank >= 102 的高分候选，且每天最多新开1只，避免同日次优候选拖累。",
                    "持有满最短周期后，跌破长期趋势、60日明显跑输基准或浮盈回撤触发卖出。",
                ],
                "outputs": ["候选CSV/JSON", "买入区间", "初始止损", "趋势卖点", "相对收益卖点"],
                "limits": ["策略目标是用规则筛选长期相对强势，不保证一定盈利或一定跑赢大盘。"],
                "metrics": [
                    {"label": "默认基准", "value": "沪深300"},
                    {"label": "核心趋势", "value": "MA60/120/200"},
                    {"label": "组合高分门槛", "value": "rank >= 102"},
                    {"label": "每日新开", "value": "最多 1 只"},
                    {"label": "默认最短持有", "value": "60 日"},
                    {"label": "默认最大持有", "value": "520 日"},
                ],
                "scripts": [
                    self._artifact("长期持有策略", "stock_strategy/long_term_hold_strategy.py"),
                    self._artifact("候选扫描", "scripts/stock_strategy/run_long_term_hold_candidates.py"),
                    self._artifact("全A组合回测", "scripts/stock_strategy/backtest_long_term_hold_all_a.py"),
                ],
                "docs": [
                    self._artifact("README", "README.md"),
                ],
                "reports": [
                    self._latest_artifact("最新长期持有报告", "reports/long_term_hold", "long_term_hold_scan_report.md"),
                    self._latest_artifact("最新长期持有JSON", "reports/long_term_hold", "long_term_hold_scan.json"),
                    self._latest_artifact("最新长期持有CSV", "reports/long_term_hold", "long_term_hold_scan.csv"),
                ],
            },
            {
                "id": "crowding-warning",
                "name": "拥挤度预警",
                "status": "风险预警",
                "tone": "bad",
                "cadence": "按交易日复核",
                "mode": "热门篮子过热/回落监测",
                "objective": "监测强势股票篮子的趋势压力、量能、相关性和回落特征，为持仓和策略开关提供风险背景。",
                "workflow": ["全A股票池", "热门篮子", "趋势压力", "热度/相关性", "风险等级"],
                "latest_advice": self._crowding_latest_advice(crowding or {}),
                "workflow_notes": [
                    {"label": "全A股票池", "description": "先拉取全市场可交易标的，剔除样本不足、行情缺失或流动性太弱的股票。"},
                    {"label": "热门篮子", "description": "按近期涨幅、成交额和强势程度挑出市场最拥挤的一批股票，作为风险观察对象。"},
                    {"label": "趋势压力", "description": "看 60/120 日涨幅、相对指数超额、均线距离和回撤，判断趋势是否已经拉得过长。"},
                    {"label": "热度/相关性", "description": "看量能放大、波动率和股票之间的同步性；同步越强，说明交易越拥挤。"},
                    {"label": "风险等级", "description": "把前面指标合成正常、升温、过热观察、30日预警、高危等状态，供策略开关参考。"},
                ],
                "signals": [
                    "V1 关注20日收益、量能放大、回撤、波动和股票间相关性。",
                    "V2 增加60/120日相对指数表现、均线距离、宽基泡沫和低波白马过热识别。",
                    "输出正常、升温、过热观察、30日预警、高危等风险等级。",
                ],
                "risk_controls": [
                    "预警只作为风险背景，不直接替代具体策略信号。",
                    "样本不足或基准数据缺失时不强行给出结论。",
                ],
                "outputs": ["风险等级", "触发类型", "热门篮子指标", "历史验证"],
                "limits": ["风险预警不是择时保证；极端行情下需要结合策略自身风控。"],
                "metrics": [
                    {"label": "默认观察窗", "value": "20/60/120 日"},
                    {"label": "高危阈值", "value": "70+"},
                ],
                "scripts": [
                    self._artifact("拥挤度 V1", "scripts/stock_strategy/crowding_warning_v1.py"),
                    self._artifact("拥挤度 V2", "scripts/stock_strategy/crowding_warning_v2_current.py"),
                    self._artifact("历史验证", "scripts/stock_strategy/crowding_historical_validation.py"),
                ],
                "docs": [],
                "reports": [
                    self._latest_artifact("最新拥挤度报告", "reports/crowding_warning", "*.md"),
                    self._latest_artifact("最新拥挤度摘要", "reports/crowding_warning", "*.json"),
                ],
            },
        ]

    def _advice(self, title: str, body: str, tone: str = "warn", label: str = "最新购买建议") -> dict[str, str]:
        return {
            "label": label,
            "title": title,
            "body": body,
            "tone": tone,
        }

    def _hold5_latest_advice(self, summary: dict[str, Any]) -> dict[str, str]:
        latest_date = summary.get("latest_date") or "--"
        sell_date = summary.get("sell_date") or "--"
        formal = [item for item in summary.get("formal") or [] if isinstance(item, dict)]
        aggressive = [item for item in summary.get("aggressive") or [] if isinstance(item, dict)]
        watch = [item for item in summary.get("watch") or [] if isinstance(item, dict)]
        switch = summary.get("strategy_switch") if isinstance(summary.get("strategy_switch"), dict) else {}
        state = str(switch.get("state") or "")

        if formal:
            names = self._names_for_advice(formal)
            return {
                "label": "最新购买建议",
                "title": "建议研究买入",
                "body": f"{latest_date} 核心候选：{names}；第5个交易日 {sell_date} 复核。",
                "tone": "good",
            }
        if state == "红色":
            names = self._names_for_advice(aggressive or watch)
            suffix = f"；进取/观察：{names}" if names else ""
            return {
                "label": "最新购买建议",
                "title": "暂不新开仓",
                "body": f"{latest_date} 策略红灯，无正式候选{suffix}。",
                "tone": "bad",
            }
        if aggressive:
            names = self._names_for_advice(aggressive)
            return {
                "label": "最新购买建议",
                "title": "仅进取研究",
                "body": f"{latest_date} 无核心候选；可观察 {names}，不作为正式买入。",
                "tone": "warn",
            }
        return {
            "label": "最新购买建议",
            "title": "暂无买入建议",
            "body": f"{latest_date} 暂无正式候选。",
            "tone": "warn",
        }

    def _hold5_dynamic_latest_advice(self, summary: dict[str, Any]) -> dict[str, str]:
        latest_date = summary.get("latest_date") or "--"
        base_advice = self._hold5_latest_advice(summary)
        formal = [item for item in summary.get("formal") or [] if isinstance(item, dict)]
        candidates = formal or [item for item in summary.get("aggressive") or [] if isinstance(item, dict)]
        names = self._names_for_advice(candidates)

        if base_advice["title"] == "建议研究买入":
            suffix = f"；先复核 {names}" if names else ""
            return self._advice(
                "按动态模式复核",
                f"{latest_date} 有尾盘候选{suffix}，再判断第一名集中或 Top3 等权。",
                "good",
            )
        if base_advice["title"] == "暂不新开仓":
            return self._advice(
                "跟随尾盘策略暂停",
                f"{latest_date} 尾盘策略红灯，动态执行模式不放行新仓。",
                "bad",
            )
        return self._advice(
            "等待尾盘信号",
            f"{latest_date} 暂无可执行核心候选；有候选后再判断第一名集中或 Top3 等权。",
            "warn",
        )

    def _ten_billion_latest_advice(self, automation: dict[str, Any], candidate_scan: dict[str, Any]) -> dict[str, str]:
        signal_date = self._report_date(automation, None) or "--"
        market = self._market(automation)
        formal = [item for item in automation.get("formal_candidates") or [] if isinstance(item, dict)]
        watchlist = [item for item in automation.get("watchlist") or [] if isinstance(item, dict)]
        scan_results = [item for item in candidate_scan.get("results") or [] if isinstance(item, dict)]

        if formal:
            names = self._names_for_advice(formal)
            return self._advice(
                "可研究买入",
                f"{signal_date} 正式候选：{names}；按市场状态门和 T+1 节奏执行。",
                "good",
            )
        if market.get("grade") != "unknown" and not market.get("tradable"):
            reasons = "、".join(str(item) for item in market.get("pause_reasons") or [] if item)
            reason_text = f"；原因：{reasons}" if reasons else ""
            return self._advice("市场门暂停买入", f"{signal_date} 市场状态不可交易{reason_text}。", "bad")

        block_reason = automation.get("candidate_block_reason") or ""
        if block_reason:
            return self._advice("暂不新开仓", f"{signal_date} {block_reason}", "warn")
        if watchlist:
            names = self._names_for_advice(watchlist)
            return self._advice("仅观察候选", f"{signal_date} 无正式候选；观察名单：{names}。", "warn")
        if scan_results:
            names = self._names_for_advice(scan_results)
            return self._advice(
                "暂不新开仓",
                f"{signal_date} 扫描到 {len(scan_results)} 只初筛结果（{names}），但未形成正式买入名单。",
                "warn",
            )
        return self._advice("暂无买入建议", f"{signal_date} 暂无自动化正式候选。", "warn")

    def _announcement_latest_advice(self) -> dict[str, str]:
        path = self._latest_by_mtime(self.reports_dir / "full_announcement_recommendations", "*.md")
        report_date = self._date_from_path(path) if path else "--"
        if path:
            return self._advice(
                "暂无公告买入名单",
                f"{report_date} 最新产物是公告推荐/回测报告，尚未接入今日正式买入名单；需按开盘缺口、止损止盈复核。",
                "warn",
            )
        return self._advice(
            "等待公告推荐",
            "暂无最新公告推荐产物；需要先生成公告候选，再按事件评分和开盘过滤复核。",
            "warn",
        )

    def _range_trader_latest_advice(self, review_rows: list[dict[str, Any]]) -> dict[str, str]:
        if not review_rows:
            return self._advice(
                "等待区间扫描",
                "暂无最新区间复盘 CSV；先运行股票池扫描，再看买入区间、止损和 reward/risk。",
                "warn",
            )

        latest_report_date = max(str(row.get("report_date") or row.get("signal_latest_date") or "") for row in review_rows)
        latest_rows = [
            row
            for row in review_rows
            if str(row.get("report_date") or row.get("signal_latest_date") or "") == latest_report_date
        ]
        names = self._names_for_advice(latest_rows)
        current_date = max(str(row.get("current_date") or "") for row in review_rows) or latest_report_date or "--"
        names_text = f"；最近信号：{names}" if names else ""
        return self._advice(
            "按区间复核，不追价",
            f"最新复盘到 {current_date}{names_text}；只有触达买入区间后才按止损/止盈计划执行。",
            "info",
        )

    def _live_paper_latest_advice(self, live_trading: dict[str, Any]) -> dict[str, str]:
        trade_date = live_trading.get("trade_date") or "--"
        planned_orders = self._int_value(live_trading.get("planned_orders"))
        fills = self._int_value(live_trading.get("fills"))
        rejections = self._int_value(live_trading.get("rejections"))
        exposure = self._float_value(live_trading.get("exposure"))

        if planned_orders > 0:
            return self._advice(
                "纸面计划买入",
                f"{trade_date} 计划订单 {planned_orders} 笔，已成交 {fills} 笔，拒绝 {rejections} 笔；仅纸面执行。",
                "good",
            )
        return self._advice(
            "今日无纸面买入",
            f"{trade_date} 计划订单 0 笔，当前纸面仓位 {self._percent(exposure)}；继续等待公告信号。",
            "warn",
        )

    def _long_term_hold_latest_advice(self, scan: dict[str, Any], daily: dict[str, Any]) -> dict[str, str]:
        results = [item for item in scan.get("results") or [] if isinstance(item, dict)]
        formal_count = int(daily.get("formal_count") or 0)
        watch_count = int(daily.get("watch_count") or 0)
        signal_date = daily.get("signal_date") or (results[0].get("latest_date") if results else "") or "--"
        reason = daily.get("reason_no_formal") or ""
        formal = [item for item in results if self._float_value(item.get("rank_score")) >= 102]

        if formal_count > 0 or formal:
            names = self._names_for_advice(formal or results)
            return {
                "label": "最新购买建议",
                "title": "可研究买入",
                "body": f"{signal_date} 高分候选：{names}；按买入区间和长期止损执行。",
                "tone": "good",
            }

        watch_names = self._names_for_advice(results)
        reason_text = f"；原因：{reason}" if reason else ""
        watch_text = f"；观察 {watch_count} 只" if watch_count else ""
        names_text = f"：{watch_names}" if watch_names else ""
        return {
            "label": "最新购买建议",
            "title": "暂无正式买入",
            "body": f"{signal_date} 未触发正式买入{watch_text}{names_text}{reason_text}。",
            "tone": "warn",
        }

    def _crowding_latest_advice(self, crowding: dict[str, Any]) -> dict[str, str]:
        latest = crowding.get("latest") if isinstance(crowding.get("latest"), dict) else {}
        signal_date = latest.get("date") or crowding.get("latest_date") or "--"
        risk_level = str(latest.get("risk_level") or "未知")
        trigger = latest.get("trigger") or "未触发"
        score = latest.get("watch_score")
        if score is None and isinstance(latest.get("v2"), dict):
            score = latest["v2"].get("watch_score") or latest["v2"].get("blended_watch")
        score_text = f"，热度 {self._number(score, 1)}" if score is not None else ""

        if risk_level == "高危":
            return self._advice(
                "高危，暂停追涨",
                f"{signal_date} 拥挤度为高危，触发：{trigger}{score_text}；新买入需降频或暂停。",
                "bad",
            )
        if risk_level in {"30日预警", "过热观察", "升温"}:
            return self._advice(
                "风险升温，控制仓位",
                f"{signal_date} 拥挤度 {risk_level}，触发：{trigger}{score_text}；优先减小新仓。",
                "warn",
            )
        if risk_level != "未知":
            return self._advice(
                "风险背景可控",
                f"{signal_date} 拥挤度 {risk_level}，触发：{trigger}{score_text}；仍需结合具体策略信号。",
                "info",
            )
        return self._advice(
            "等待拥挤度更新",
            "暂无最新拥挤度摘要；先更新风险报告，再决定是否放行追涨类新仓。",
            "warn",
        )

    def _names_for_advice(self, rows: list[dict[str, Any]], limit: int = 3) -> str:
        names = [str(item.get("name") or item.get("secucode") or "").strip() for item in rows]
        return "、".join([name for name in names if name][:limit])

    def _float_value(self, value: Any) -> float:
        try:
            return float(value)
        except (TypeError, ValueError):
            return 0.0

    def _int_value(self, value: Any) -> int:
        try:
            return int(float(value))
        except (TypeError, ValueError):
            return 0

    def _percent(self, value: Any) -> str:
        return f"{self._float_value(value) * 100:.1f}%"

    def _number(self, value: Any, digits: int = 1) -> str:
        return f"{self._float_value(value):.{digits}f}"

    def _date_from_path(self, path: Path) -> str:
        text = str(path)
        match = re.search(r"(20\d{2})[-_]?(\d{2})[-_]?(\d{2})", text)
        if not match:
            return "--"
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"


    def _hold5_detail_sections(self, summary: dict[str, Any]) -> list[dict[str, Any]]:
        formal = [item for item in summary.get("formal") or [] if isinstance(item, dict)]
        watch = [item for item in summary.get("watch") or [] if isinstance(item, dict)]
        latest_items = [
            (
                f"最新信号日 {summary.get('latest_date') or '--'}；第5个交易日 "
                f"{summary.get('sell_date') or '--'} 做卖出确认，盈利且站上 MA5 时可继续持有。"
            ),
            (
                f"候选池硬过滤后 {self._display_count(summary.get('eligible_count'))} 只，"
                f"相似样本验证 {self._display_count(summary.get('validated_count'))} 只；"
                f"正式候选 {len(formal)} 只，观察 {len(watch)} 只。"
            ),
        ]
        if summary.get("top_industries"):
            latest_items.append(f"板块共振靠前：{summary['top_industries']}")
        if summary.get("recent_metrics_note"):
            latest_items.append(f"近期策略状态：{summary['recent_metrics_note']}")

        return [
            {
                "title": "保留口径",
                "items": [
                    "当前保留旧底层排序，不再使用两次手工新权重实验。",
                    "核心优化是 30 样本强收益状态拦截、Top10 轻量实时报价复核和强行情攻击模式排序。",
                    "风险层级只作为行动标签，不把低分核心强行排到高分进取前面。",
                ],
            },
            {
                "title": "运行流程",
                "items": [
                    "交易日 14:50 拉全A实时快照，先用可成交性、流动性、尾盘承接和异常价格做硬过滤。",
                    "对预筛股票找历史相似样本，计算 5 日胜率、平均收益、利润因子、最差样本和持有期回撤。",
                    "最终 Top10 再复核实时价格，若尾盘跌破、上影线明显或报价异常，会降级或剔除。",
                ],
            },
            {
                "title": "最新报告怎么看",
                "items": latest_items,
            },
            {
                "title": "输出层级",
                "items": [
                    "正式核心：收益、左尾、持有回撤和 reward/risk 相对干净，可作为主要研究对象。",
                    "进取研究：预期收益较强，但左尾或回撤不够干净，只适合小仓位研究。",
                    "观察名单：当前尾盘位置、风险或统计质量不足，需要修复条件后再考虑。",
                ],
            },
            {
                "title": "为什么不是实盘指令",
                "items": [
                    "历史验证主要是日线收盘代理，不是真实历史 14:50 分钟级盘口回放。",
                    "页面只发布研究候选和风控说明，不连接券商、不自动下单，也不构成投资建议。",
                ],
            },
        ]

    def _display_count(self, value: Any) -> str:
        return str(value) if value is not None and value != "" else "--"

    def _artifact(self, label: str, relative_path: str) -> dict[str, Any]:
        path = self.base_dir / relative_path
        return {
            "label": label,
            "path": relative_path,
            "exists": path.is_file(),
            "kind": path.suffix.lower().lstrip(".") or "file",
        }

    def _latest_artifact(self, label: str, relative_dir: str, pattern: str) -> dict[str, Any]:
        path = self._latest_by_mtime(self.base_dir / relative_dir, pattern)
        if path is None:
            return {"label": label, "path": "", "exists": False, "kind": "file"}
        return self._path_artifact(label, path)

    def _latest_hold5_candidate_artifact(self, label: str, filename: str) -> dict[str, Any]:
        path = self._latest_hold5_candidate_path(filename)
        if path is None:
            return {"label": label, "path": "", "exists": False, "kind": "file"}
        return self._path_artifact(label, path)

    def _latest_hold5_candidate_path(self, filename: str) -> Path | None:
        directory = self.reports_dir / "automation_5_14_50"
        if not directory.exists():
            return None
        paths = [
            path
            for path in directory.glob(f"20*/{filename}")
            if path.is_file()
            and path.parent.name[:8].isdigit()
            and not path.parent.name.startswith("2026-")
        ]
        if not paths:
            return None
        return max(paths, key=lambda path: (path.stat().st_mtime, str(path)))

    def _latest_long_term_daily_summary_path(self) -> Path | None:
        directory = self.reports_dir / "long_term_hold"
        if not directory.exists():
            return None
        paths = [path for path in directory.glob("automation_2_daily_*/summary.json") if path.is_file()]
        if not paths:
            return None
        return max(paths, key=lambda path: (path.stat().st_mtime, str(path)))

    def _path_artifact(self, label: str, path: Path) -> dict[str, Any]:
        try:
            relative_path = str(path.relative_to(self.base_dir))
        except ValueError:
            relative_path = str(path)
        return {
            "label": label,
            "path": relative_path,
            "exists": True,
            "kind": path.suffix.lower().lstrip(".") or "file",
        }
