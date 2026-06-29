from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from backtest_10b_tencent import fetch_bars as fetch_tencent_bars
from run_hold5_tail_candidates import planned_sell_date


BASE_DIR = Path(__file__).resolve().parents[2]
ROUND_TRIP_COST = 0.0013


@dataclass(frozen=True)
class Pick:
    batch: str
    report_dir: Path
    signal_date: str
    secucode: str
    name: str
    original_signal_price: float
    original_stop_loss: float
    original_target_low: float
    note: str


def as_float(value: Any, default: float = 0.0) -> float:
    try:
        if value in (None, "", "-"):
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def load_summary(report_dir: Path) -> dict[str, Any]:
    return json.loads((report_dir / "summary.json").read_text(encoding="utf-8"))


def formal_rows(summary: dict[str, Any]) -> list[dict[str, Any]]:
    return [row for row in summary.get("formal", []) if row]


def normalize_pick(report_dir: Path, row: dict[str, Any]) -> Pick:
    summary = load_summary(report_dir)
    signal_date = str(row.get("latest_date") or summary.get("latest_date") or summary.get("today"))
    if "price" in row:
        signal_price = as_float(row.get("price"))
        stop_loss = as_float(row.get("stop_loss"))
        target_low = as_float(row.get("target_low"))
    else:
        signal_price = as_float(row.get("latest_close"))
        stop_loss = as_float(row.get("stop_loss"))
        target_low = signal_price * (1.0 + max(0.0, as_float(row.get("median_return_5d"))))

    batch = report_dir.name
    note = "intended_tail_run"
    if batch == "20260611_000118":
        note = "after_midnight_rerun_for_2026-06-10"

    return Pick(
        batch=batch,
        report_dir=report_dir,
        signal_date=signal_date,
        secucode=str(row.get("secucode")),
        name=str(row.get("name")),
        original_signal_price=signal_price,
        original_stop_loss=stop_loss,
        original_target_low=target_low,
        note=note,
    )


def review_pick(pick: Pick) -> dict[str, Any]:
    print(f"review next-open {pick.batch} {pick.secucode} {pick.name}", flush=True)
    bars = fetch_tencent_bars(pick.secucode, pick.signal_date.replace("-", ""), datetime.now().strftime("%Y%m%d"), timeout=8)
    bars = [bar for bar in bars if bar.trade_date >= pick.signal_date]
    if len(bars) < 2:
        raise RuntimeError("no next trading day bar yet")

    entry_bar = next((bar for bar in bars if bar.trade_date > pick.signal_date), None)
    if entry_bar is None:
        raise RuntimeError("no next trading day bar yet")
    latest = bars[-1]
    entry_price = entry_bar.open
    evaluation_bar = latest
    path_bars = [bar for bar in bars if entry_bar.trade_date <= bar.trade_date <= evaluation_bar.trade_date]
    min_low = min(bar.low for bar in path_bars)
    max_high = max(bar.high for bar in path_bars)
    net_return = evaluation_bar.close / entry_price - 1.0 - ROUND_TRIP_COST
    signal_slippage = entry_price / pick.original_signal_price - 1.0 if pick.original_signal_price > 0 else 0.0
    stop_hit = pick.original_stop_loss > 0 and min_low <= pick.original_stop_loss
    target_hit = pick.original_target_low > 0 and max_high >= pick.original_target_low

    return {
        "batch": pick.batch,
        "signal_date": pick.signal_date,
        "entry_date": entry_bar.trade_date,
        "next_open_entry": entry_price,
        "planned_sell_date_from_entry": planned_sell_date(entry_bar.trade_date),
        "secucode": pick.secucode,
        "name": pick.name,
        "original_signal_price": pick.original_signal_price,
        "signal_to_next_open_slippage": signal_slippage,
        "evaluation_date": evaluation_bar.trade_date,
        "evaluation_close": evaluation_bar.close,
        "net_return_after_cost": net_return,
        "min_low_since_entry": min_low,
        "max_high_since_entry": max_high,
        "original_stop_loss": pick.original_stop_loss,
        "stop_hit": stop_hit,
        "original_target_low": pick.original_target_low,
        "target_hit": target_hit,
        "note": pick.note,
    }


def pct(value: float) -> str:
    return f"{value:.2%}"


def main() -> None:
    report_dirs = [
        BASE_DIR / "reports/automation_5_14_50/20260610_185605",
        BASE_DIR / "reports/automation_5_14_50/20260611_000118",
        BASE_DIR / "reports/automation_5_14_50/20260611_150520",
        BASE_DIR / "reports/automation_5_14_50/20260612_145350",
        BASE_DIR / "reports/automation_5_14_50/20260615_145326",
    ]
    picks: list[Pick] = []
    for report_dir in report_dirs:
        summary = load_summary(report_dir)
        for row in formal_rows(summary)[:3]:
            picks.append(normalize_pick(report_dir, row))

    rows: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    for pick in picks:
        try:
            rows.append(review_pick(pick))
        except Exception as exc:  # noqa: BLE001
            errors.append({"batch": pick.batch, "signal_date": pick.signal_date, "secucode": pick.secucode, "name": pick.name, "error": str(exc)})

    out_dir = BASE_DIR / "reports/automation_5_14_50" / f"review_next_open_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    out_dir.mkdir(parents=True, exist_ok=True)
    if rows:
        with (out_dir / "next_open_returns.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    with (out_dir / "errors.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["batch", "signal_date", "secucode", "name", "error"])
        writer.writeheader()
        writer.writerows(errors)

    avg_net = sum(row["net_return_after_cost"] for row in rows) / len(rows) if rows else 0.0
    wins = sum(1 for row in rows if row["net_return_after_cost"] > 0)
    stop_hits = sum(1 for row in rows if row["stop_hit"])
    target_hits = sum(1 for row in rows if row["target_hit"])
    intended = [row for row in rows if row["note"] == "intended_tail_run"]
    avg_intended = sum(row["net_return_after_cost"] for row in intended) / len(intended) if intended else 0.0

    lines = [
        "# 次日开盘买入收益回溯",
        "",
        f"- 生成时间：{datetime.now().astimezone().isoformat(timespec='seconds')}",
        "- 口径：信号日不买，按下一个交易日开盘价买入；截至最新日线收盘评估浮动净收益，扣往返 13bp。",
        "- 说明：6/15 信号的下一个交易日开盘尚未发生，因此列入错误/未评估，不纳入收益统计。",
        f"- 覆盖：可评估 {len(rows)} 条；未评估 {len(errors)} 条。",
        f"- 汇总：平均浮动净收益 {pct(avg_net)}；正收益 {wins}/{len(rows)}；触及原止损 {stop_hits}/{len(rows)}；触及原目标下沿 {target_hits}/{len(rows)}。",
        f"- 仅 intended_tail_run 可评估批次：{len(intended)} 条，平均浮动净收益 {pct(avg_intended)}。",
        "",
        "## 明细",
        "| 批次 | 信号日 | 次日开盘买入日 | 股票 | 信号价 | 次日开盘 | 跳空/滑点 | 评估日 | 评估收盘 | 当前净收益 | 原止损 | 触损 | 原目标下沿 | 触达 | 计划卖出日(按次日开盘重算) |",
        "|---|---|---|---|---:|---:|---:|---|---:|---:|---:|---|---:|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['batch']} | {row['signal_date']} | {row['entry_date']} | {row['secucode']} {row['name']} | "
            f"{row['original_signal_price']:.2f} | {row['next_open_entry']:.2f} | {pct(row['signal_to_next_open_slippage'])} | "
            f"{row['evaluation_date']} | {row['evaluation_close']:.2f} | {pct(row['net_return_after_cost'])} | "
            f"{row['original_stop_loss']:.2f} | {'是' if row['stop_hit'] else '否'} | "
            f"{row['original_target_low']:.2f} | {'是' if row['target_hit'] else '否'} | {row['planned_sell_date_from_entry']} |"
        )
    if errors:
        lines.extend(["", "## 未评估", "| 批次 | 信号日 | 股票 | 原因 |", "|---|---|---|---|"])
        for error in errors:
            lines.append(f"| {error['batch']} | {error['signal_date']} | {error['secucode']} {error['name']} | {error['error']} |")
    lines.extend([
        "",
        "## 文件",
        f"- CSV：{out_dir / 'next_open_returns.csv'}",
        f"- 错误/未评估：{out_dir / 'errors.csv'}",
        "",
        "风险提示：这是研究回溯与浮动跟踪，不构成投资建议；未连接券商、未执行真实交易。",
    ])
    (out_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"output_dir": str(out_dir), "rows": len(rows), "errors": len(errors), "avg_net": avg_net, "wins": wins, "stop_hits": stop_hits, "target_hits": target_hits, "avg_intended": avg_intended}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
