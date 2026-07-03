from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import asdict, dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Callable

from stock_range_trader import (
    DEFAULT_BASE_DIR,
    PredictionConfig,
    analyze_stock,
    load_daily_bars,
    normalize_code,
)


@dataclass(frozen=True)
class PoolCandidate:
    secucode: str
    name: str = ""
    source: str = "manual"
    source_date: str = ""
    event_score: float = 0.0
    predict_type: str = ""


@dataclass(frozen=True)
class PoolScanConfig:
    min_trades: int = 5
    min_total_return: float = 0.0
    max_drawdown: float = -0.08
    min_band_coverage: float = 0.75
    max_results: int = 50


@dataclass(frozen=True)
class PoolScanResult:
    secucode: str
    name: str
    source: str
    source_date: str
    event_score: float
    action: str
    tradable: bool
    status: str
    reject_reason: str
    rank_score: float
    latest_date: str = ""
    latest_close: float = 0.0
    predicted_high: float = 0.0
    predicted_low: float = 0.0
    buy_zone_low: float = 0.0
    buy_zone_high: float = 0.0
    stop_loss: float = 0.0
    take_profit: float = 0.0
    reward_risk: float = 0.0
    signals: int = 0
    trades: int = 0
    total_return: float = 0.0
    win_rate: float = 0.0
    profit_factor: float = 0.0
    max_drawdown: float = 0.0
    band_coverage: float = 0.0
    direction_hit: float = 0.0
    detail_dir: str = ""


def as_float(value: Any, default: float = 0.0) -> float:
    try:
        if value is None or value == "":
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def format_pct(value: float) -> str:
    return f"{value * 100:.2f}%"


def candidate_from_code(raw_code: str, name: str = "", source: str = "manual") -> PoolCandidate:
    return PoolCandidate(secucode=normalize_code(raw_code), name=name, source=source)


def find_kline_cache(cache_dir: Path | None, secucode: str) -> Path | None:
    if cache_dir is None:
        return None
    normalized = normalize_code(secucode)
    stem = normalized.replace(".", "_")
    stock_code = normalized.split(".")[0]
    candidates = [
        cache_dir / f"{stem}.json",
        cache_dir / f"{normalized}.json",
        cache_dir / f"{stock_code}.json",
        cache_dir / f"{stock_code}_kline.json",
    ]
    for path in candidates:
        if path.exists():
            return path
    return None


def load_codes_file(path: Path) -> list[PoolCandidate]:
    text = path.read_text("utf-8-sig")
    stripped_lines = [line.strip() for line in text.splitlines() if line.strip() and not line.strip().startswith("#")]
    if not stripped_lines:
        return []

    if path.suffix.lower() == ".csv" or "," in stripped_lines[0]:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            candidates: list[PoolCandidate] = []
            for row in reader:
                raw_code = (
                    row.get("secucode")
                    or row.get("SECUCODE")
                    or row.get("code")
                    or row.get("SECURITY_CODE")
                    or ""
                )
                if not raw_code:
                    continue
                name = row.get("name") or row.get("SECURITY_NAME_ABBR") or row.get("stock_name") or ""
                candidates.append(candidate_from_code(raw_code, name=name, source="codes_file"))
            return candidates

    return [candidate_from_code(line.split()[0], source="codes_file") for line in stripped_lines]


def load_announcement_pool(
    path: Path,
    min_score: float = 96,
    limit: int = 30,
) -> list[PoolCandidate]:
    latest_by_code: dict[str, PoolCandidate] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            secucode = row.get("SECUCODE") or row.get("secucode") or ""
            if not secucode.endswith((".SZ", ".SH")):
                continue
            score = as_float(row.get("EVENT_SCORE"))
            if score < min_score:
                continue
            notice_date = str(row.get("NOTICE_DATE") or "")[:10]
            try:
                normalized = normalize_code(secucode)
            except ValueError:
                continue
            candidate = PoolCandidate(
                secucode=normalized,
                name=str(row.get("SECURITY_NAME_ABBR") or ""),
                source="announcement",
                source_date=notice_date,
                event_score=score,
                predict_type=str(row.get("PREDICT_TYPE") or ""),
            )
            previous = latest_by_code.get(normalized)
            if previous is None or (candidate.source_date, candidate.event_score) > (previous.source_date, previous.event_score):
                latest_by_code[normalized] = candidate

    candidates = list(latest_by_code.values())
    candidates.sort(key=lambda item: (item.source_date, item.event_score, item.secucode), reverse=True)
    return candidates[:limit]


def reject_reasons(summary: dict[str, Any], config: PoolScanConfig) -> list[str]:
    plan = summary.get("trade_plan") or {}
    trade_metrics = summary.get("trade_metrics") or {}
    prediction_metrics = summary.get("prediction_metrics") or {}
    reasons: list[str] = []

    if plan.get("action") != "BUY_ZONE":
        reasons.append("not BUY_ZONE")
    trades = int(trade_metrics.get("trades") or 0)
    if trades < config.min_trades:
        reasons.append(f"trades {trades} < {config.min_trades}")
    total_return = as_float(trade_metrics.get("total_return"))
    if total_return < config.min_total_return:
        reasons.append(f"return {format_pct(total_return)} < {format_pct(config.min_total_return)}")
    max_dd = as_float(trade_metrics.get("max_drawdown"))
    if max_dd < config.max_drawdown:
        reasons.append(f"drawdown {format_pct(max_dd)} < {format_pct(config.max_drawdown)}")
    band_coverage = as_float(prediction_metrics.get("band_coverage"))
    if band_coverage < config.min_band_coverage:
        reasons.append(f"coverage {format_pct(band_coverage)} < {format_pct(config.min_band_coverage)}")
    return reasons


def rank_score(summary: dict[str, Any], tradable: bool) -> float:
    plan = summary.get("trade_plan") or {}
    trade_metrics = summary.get("trade_metrics") or {}
    prediction = summary.get("prediction") or {}
    prediction_metrics = summary.get("prediction_metrics") or {}
    score = 0.0
    score += as_float(trade_metrics.get("total_return")) * 100
    score += min(as_float(trade_metrics.get("profit_factor")), 10.0) * 2
    score += as_float(plan.get("reward_risk")) * 3
    score += as_float(prediction.get("expected_close_return")) * 100
    score += as_float(prediction_metrics.get("band_coverage")) * 5
    score += as_float(trade_metrics.get("max_drawdown")) * 50
    if tradable:
        score += 100
    return round(score, 6)


def evaluate_summary(candidate: PoolCandidate, summary: dict[str, Any], config: PoolScanConfig) -> PoolScanResult:
    plan = summary.get("trade_plan") or {}
    prediction = summary.get("prediction") or {}
    latest = summary.get("latest_bar") or {}
    trade_metrics = summary.get("trade_metrics") or {}
    prediction_metrics = summary.get("prediction_metrics") or {}
    reasons = reject_reasons(summary, config)
    tradable = not reasons

    return PoolScanResult(
        secucode=candidate.secucode,
        name=candidate.name,
        source=candidate.source,
        source_date=candidate.source_date,
        event_score=candidate.event_score,
        action=str(plan.get("action") or ""),
        tradable=tradable,
        status="ok",
        reject_reason="; ".join(reasons),
        rank_score=rank_score(summary, tradable),
        latest_date=str(latest.get("trade_date") or ""),
        latest_close=as_float(latest.get("close")),
        predicted_high=as_float(prediction.get("predicted_high")),
        predicted_low=as_float(prediction.get("predicted_low")),
        buy_zone_low=as_float(plan.get("buy_zone_low")),
        buy_zone_high=as_float(plan.get("buy_zone_high")),
        stop_loss=as_float(plan.get("stop_loss")),
        take_profit=as_float(plan.get("take_profit")),
        reward_risk=as_float(plan.get("reward_risk")),
        signals=int(trade_metrics.get("signals") or 0),
        trades=int(trade_metrics.get("trades") or 0),
        total_return=as_float(trade_metrics.get("total_return")),
        win_rate=as_float(trade_metrics.get("win_rate")),
        profit_factor=as_float(trade_metrics.get("profit_factor")),
        max_drawdown=as_float(trade_metrics.get("max_drawdown")),
        band_coverage=as_float(prediction_metrics.get("band_coverage")),
        direction_hit=as_float(prediction_metrics.get("direction_hit")),
        detail_dir=str(summary.get("output_dir") or ""),
    )


def error_result(candidate: PoolCandidate, exc: Exception) -> PoolScanResult:
    return PoolScanResult(
        secucode=candidate.secucode,
        name=candidate.name,
        source=candidate.source,
        source_date=candidate.source_date,
        event_score=candidate.event_score,
        action="",
        tradable=False,
        status="error",
        reject_reason=str(exc),
        rank_score=-math.inf,
    )


Analyzer = Callable[[PoolCandidate], dict[str, Any]]


def scan_candidates(
    candidates: list[PoolCandidate],
    analyzer: Analyzer,
    config: PoolScanConfig,
) -> list[PoolScanResult]:
    results: list[PoolScanResult] = []
    for candidate in candidates:
        try:
            results.append(evaluate_summary(candidate, analyzer(candidate), config))
        except Exception as exc:
            results.append(error_result(candidate, exc))

    results.sort(key=lambda item: (item.tradable, item.rank_score, item.source_date, item.secucode), reverse=True)
    return results


def write_pool_outputs(output_dir: Path, results: list[PoolScanResult], config: PoolScanConfig) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = [asdict(item) for item in results]
    fieldnames = list(rows[0].keys()) if rows else [field.name for field in PoolScanResult.__dataclass_fields__.values()]

    with (output_dir / "pool_scan.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "config": asdict(config),
        "results": rows,
    }
    with (output_dir / "pool_scan.json").open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)

    tradable = [item for item in results if item.tradable]
    lines = [
        "# 股票池区间策略扫描",
        "",
        f"- Generated at: {payload['generated_at']}",
        f"- Scanned: {len(results)}",
        f"- Tradable: {len(tradable)}",
        f"- Min trades: {config.min_trades}",
        f"- Min return: {format_pct(config.min_total_return)}",
        f"- Max drawdown floor: {format_pct(config.max_drawdown)}",
        f"- Min band coverage: {format_pct(config.min_band_coverage)}",
        "",
        "## 可交易候选",
        "",
    ]

    if tradable:
        lines.append("| Code | Name | Action | Buy Zone | Stop | Take Profit | R/R | 90d Return | Trades | Max DD | Detail |")
        lines.append("|---|---|---|---|---:|---:|---:|---:|---:|---:|---|")
        for item in tradable[: config.max_results]:
            lines.append(
                f"| {item.secucode} | {item.name} | {item.action} | "
                f"{item.buy_zone_low:.2f}-{item.buy_zone_high:.2f} | {item.stop_loss:.2f} | "
                f"{item.take_profit:.2f} | {item.reward_risk:.2f} | {format_pct(item.total_return)} | "
                f"{item.trades} | {format_pct(item.max_drawdown)} | {item.detail_dir} |"
            )
    else:
        lines.append("No tradable candidates passed all filters.")

    lines.extend(["", "## 观察/拒绝", ""])
    lines.append("| Code | Name | Status | Action | Reason | Rank |")
    lines.append("|---|---|---|---|---|---:|")
    for item in [row for row in results if not row.tradable][: config.max_results]:
        lines.append(
            f"| {item.secucode} | {item.name} | {item.status} | {item.action} | "
            f"{item.reject_reason} | {item.rank_score:.2f} |"
        )

    lines.append("")
    lines.append("This is a research scanner for paper trading. It does not place orders.")
    (output_dir / "pool_scan_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_candidates(args: argparse.Namespace) -> list[PoolCandidate]:
    candidates: list[PoolCandidate] = []
    if args.codes:
        candidates.extend(candidate_from_code(item.strip()) for item in args.codes.split(",") if item.strip())
    if args.codes_file:
        candidates.extend(load_codes_file(Path(args.codes_file)))
    if args.announcement_events:
        candidates.extend(load_announcement_pool(Path(args.announcement_events), args.min_event_score, args.limit))

    deduped: dict[str, PoolCandidate] = {}
    for candidate in candidates:
        if candidate.secucode not in deduped:
            deduped[candidate.secucode] = candidate
    return list(deduped.values())[: args.limit]


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Batch scan A-shares with the range trader")
    parser.add_argument("--codes", default="", help="Comma separated stock codes")
    parser.add_argument("--codes-file", default="", help="Plain text or CSV stock code file")
    parser.add_argument("--announcement-events", default="", help="Announcement event CSV path")
    parser.add_argument("--base-dir", default=str(DEFAULT_BASE_DIR))
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--min-event-score", type=float, default=96)
    parser.add_argument("--beg", default="20240101")
    parser.add_argument("--end", default=date.today().strftime("%Y%m%d"))
    parser.add_argument("--kline-dir", default="", help="Directory with cached Eastmoney K-line JSON files")
    parser.add_argument("--target-count", type=int, default=90)
    parser.add_argument("--history-window", type=int, default=90)
    parser.add_argument("--similar-count", type=int, default=15)
    parser.add_argument("--target-coverage", type=float, default=0.80)
    parser.add_argument("--min-reward-risk", type=float, default=1.8)
    parser.add_argument("--min-trades", type=int, default=5)
    parser.add_argument("--min-total-return", type=float, default=0.0)
    parser.add_argument("--max-drawdown", type=float, default=-0.08)
    parser.add_argument("--min-band-coverage", type=float, default=0.75)
    return parser


def main() -> None:
    args = build_arg_parser().parse_args()
    base_dir = Path(args.base_dir)
    candidates = build_candidates(args)
    if not candidates:
        raise SystemExit("no candidates provided")

    range_config = PredictionConfig(
        history_window=args.history_window,
        similar_count=args.similar_count,
        target_coverage=args.target_coverage,
        min_reward_risk=args.min_reward_risk,
    )
    scan_config = PoolScanConfig(
        min_trades=args.min_trades,
        min_total_return=args.min_total_return,
        max_drawdown=args.max_drawdown,
        min_band_coverage=args.min_band_coverage,
        max_results=args.limit,
    )
    kline_dir = Path(args.kline_dir) if args.kline_dir else None

    def analyzer(candidate: PoolCandidate) -> dict[str, Any]:
        cache_path = find_kline_cache(kline_dir, candidate.secucode)
        bars = load_daily_bars(candidate.secucode, args.beg, args.end, cache_path)
        return analyze_stock(candidate.secucode, bars, range_config, base_dir, args.target_count)

    results = scan_candidates(candidates, analyzer, scan_config)
    output_dir = base_dir / "reports" / "range_trader" / "pool_scan" / datetime.now().strftime("%Y%m%d_%H%M%S")
    write_pool_outputs(output_dir, results, scan_config)

    printable = {
        "scanned": len(results),
        "tradable": sum(1 for item in results if item.tradable),
        "output_dir": str(output_dir),
        "top": [asdict(item) for item in results[: min(5, len(results))]],
    }
    print(json.dumps(printable, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
