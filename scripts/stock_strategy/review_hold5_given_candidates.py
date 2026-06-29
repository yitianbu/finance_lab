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
class GivenPick:
    batch: str
    report_dir: Path
    trade_date: str
    planned_sell_date: str
    secucode: str
    name: str
    entry_price: float
    buy_low: float
    buy_high: float
    stop_loss: float
    target_low: float
    target_high: float
    win_rate_5d: float
    avg_return_5d: float
    profit_factor_5d: float
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


def normalize_pick(report_dir: Path, row: dict[str, Any]) -> GivenPick:
    trade_date = str(row.get("latest_date") or load_summary(report_dir).get("latest_date") or load_summary(report_dir).get("today"))
    summary = load_summary(report_dir)
    sell_date = (
        summary.get("sell_date")
        or summary.get("plan_sell_date")
        or summary.get("plan_sell_date_weekday_fallback")
        or planned_sell_date(trade_date)
    )

    if "price" in row:
        entry = as_float(row.get("price"))
        buy_low = as_float(row.get("buy_low"), entry)
        buy_high = as_float(row.get("buy_high"), entry)
        stop_loss = as_float(row.get("stop_loss"))
        target_low = as_float(row.get("target_low"))
        target_high = as_float(row.get("target_high"))
        win_rate = as_float(row.get("win_rate"))
        avg_return = as_float(row.get("avg_return"))
        profit_factor = as_float(row.get("profit_factor"))
    else:
        entry = as_float(row.get("latest_close"))
        buy_low = as_float(row.get("buy_zone_low"), entry)
        buy_high = as_float(row.get("buy_zone_high"), entry)
        stop_loss = as_float(row.get("stop_loss"))
        target_low = entry * (1.0 + max(0.0, as_float(row.get("median_return_5d"))))
        target_high = as_float(row.get("take_profit"), entry * (1.0 + max(0.0, as_float(row.get("avg_return_5d")))))
        win_rate = as_float(row.get("win_rate_5d"))
        avg_return = as_float(row.get("avg_return_5d"))
        profit_factor = as_float(row.get("profit_factor_5d"))

    batch = report_dir.name
    note = "intended_tail_run"
    if batch == "20260611_000118":
        note = "after_midnight_rerun_for_2026-06-10"

    return GivenPick(
        batch=batch,
        report_dir=report_dir,
        trade_date=trade_date,
        planned_sell_date=str(sell_date),
        secucode=str(row.get("secucode")),
        name=str(row.get("name")),
        entry_price=entry,
        buy_low=buy_low,
        buy_high=buy_high,
        stop_loss=stop_loss,
        target_low=target_low,
        target_high=target_high,
        win_rate_5d=win_rate,
        avg_return_5d=avg_return,
        profit_factor_5d=profit_factor,
        note=note,
    )


def review_pick(pick: GivenPick) -> dict[str, Any]:
    print(f"review {pick.batch} {pick.secucode} {pick.name}", flush=True)
    bars = fetch_tencent_bars(pick.secucode, pick.trade_date.replace("-", ""), datetime.now().strftime("%Y%m%d"), timeout=8)
    bars = [bar for bar in bars if bar.trade_date >= pick.trade_date]
    if not bars:
        raise RuntimeError("no bars")

    latest = bars[-1]
    sell_bar = next((bar for bar in bars if bar.trade_date == pick.planned_sell_date), None)
    evaluation_bar = sell_bar or latest
    completed = sell_bar is not None
    path_bars = [bar for bar in bars if bar.trade_date > pick.trade_date and bar.trade_date <= evaluation_bar.trade_date]
    has_post_signal_daily_path = bool(path_bars)
    min_low = min([bar.low for bar in path_bars], default=evaluation_bar.close)
    max_high = max([bar.high for bar in path_bars], default=evaluation_bar.close)
    stop_hit = pick.stop_loss > 0 and min_low <= pick.stop_loss
    target_hit = pick.target_low > 0 and max_high >= pick.target_low
    gross_return = evaluation_bar.close / pick.entry_price - 1.0
    net_return = gross_return - ROUND_TRIP_COST
    stop_return = pick.stop_loss / pick.entry_price - 1.0 - ROUND_TRIP_COST if stop_hit else None

    return {
        "batch": pick.batch,
        "trade_date": pick.trade_date,
        "planned_sell_date": pick.planned_sell_date,
        "status": "completed_5d" if completed else "in_progress_mark_to_market",
        "secucode": pick.secucode,
        "name": pick.name,
        "entry_price": pick.entry_price,
        "buy_low": pick.buy_low,
        "buy_high": pick.buy_high,
        "stop_loss": pick.stop_loss,
        "target_low": pick.target_low,
        "target_high": pick.target_high,
        "latest_date": latest.trade_date,
        "evaluation_date": evaluation_bar.trade_date,
        "evaluation_close": evaluation_bar.close,
        "gross_return": gross_return,
        "net_return_after_cost": net_return,
        "min_low_after_signal": min_low,
        "max_high_after_signal": max_high,
        "has_post_signal_daily_path": has_post_signal_daily_path,
        "stop_hit": stop_hit,
        "target_hit": target_hit,
        "stop_rule_net_return": stop_return,
        "win_rate_5d": pick.win_rate_5d,
        "avg_return_5d": pick.avg_return_5d,
        "profit_factor_5d": pick.profit_factor_5d,
        "note": pick.note,
    }


def pct(value: float | None) -> str:
    if value is None:
        return ""
    return f"{value:.2%}"


def main() -> None:
    report_dirs = [
        BASE_DIR / "reports/automation_5_14_50/20260610_185605",
        BASE_DIR / "reports/automation_5_14_50/20260611_000118",
        BASE_DIR / "reports/automation_5_14_50/20260611_150520",
        BASE_DIR / "reports/automation_5_14_50/20260612_145350",
        BASE_DIR / "reports/automation_5_14_50/20260615_145326",
    ]
    picks: list[GivenPick] = []
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
            errors.append({"batch": pick.batch, "secucode": pick.secucode, "name": pick.name, "error": str(exc)})

    out_dir = BASE_DIR / "reports/automation_5_14_50" / f"review_previous_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    out_dir.mkdir(parents=True, exist_ok=True)
    if rows:
        with (out_dir / "given_candidates_returns.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    with (out_dir / "errors.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["batch", "secucode", "name", "error"])
        writer.writeheader()
        writer.writerows(errors)

    completed = [row for row in rows if row["status"] == "completed_5d"]
    in_progress = [row for row in rows if row["status"] != "completed_5d"]
    avg_net = sum(row["net_return_after_cost"] for row in rows) / len(rows) if rows else 0.0
    hit_stop = sum(1 for row in rows if row["stop_hit"])
    hit_target = sum(1 for row in rows if row["target_hit"])

    lines = [
        "# 已给出候选收益回溯",
        "",
        f"- 生成时间：{datetime.now().astimezone().isoformat(timespec='seconds')}",
        "- 口径：以当时报告中的信号价/收盘价为入场价，若计划卖出日已到则用第5交易日收盘；否则用最新日线收盘做浮动净收益估算。",
        "- 交易成本：按往返 13bp 扣减；止损触发只用信号日之后至评估日的日线最低价判断；同日信号不使用全天低点，避免混入信号前价格。",
        f"- 覆盖：正式候选 {len(rows)} 条；已完成5日 {len(completed)} 条；未到期浮动评估 {len(in_progress)} 条；拉取错误 {len(errors)} 条。",
        f"- 汇总：平均当前/到期净收益 {pct(avg_net)}；触及止损 {hit_stop}/{len(rows)}；触及目标下沿 {hit_target}/{len(rows)}。",
        "",
        "## 明细",
        "| 批次 | 信号日 | 卖出日 | 状态 | 代码 | 名称 | 入场 | 评估日 | 评估收盘 | 浮动/到期净收益 | 止损 | 信号后路径 | 是否触损 | 目标下沿 | 是否触达 | 预测胜率 | 预测均值 | PF | 备注 |",
        "|---|---|---|---|---|---|---:|---|---:|---:|---:|---|---|---:|---|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['batch']} | {row['trade_date']} | {row['planned_sell_date']} | {row['status']} | "
            f"{row['secucode']} | {row['name']} | {row['entry_price']:.2f} | {row['evaluation_date']} | "
            f"{row['evaluation_close']:.2f} | {pct(row['net_return_after_cost'])} | {row['stop_loss']:.2f} | "
            f"{'有' if row['has_post_signal_daily_path'] else '无'} | {'是' if row['stop_hit'] else '否'} | "
            f"{row['target_low']:.2f} | {'是' if row['target_hit'] else '否'} | "
            f"{pct(row['win_rate_5d'])} | {pct(row['avg_return_5d'])} | {row['profit_factor_5d']:.2f} | {row['note']} |"
        )
    if errors:
        lines.extend(["", "## 错误", "| 批次 | 代码 | 名称 | 错误 |", "|---|---|---|---|"])
        for error in errors:
            lines.append(f"| {error['batch']} | {error['secucode']} | {error['name']} | {error['error']} |")
    lines.extend([
        "",
        "## 文件",
        f"- CSV：{out_dir / 'given_candidates_returns.csv'}",
        f"- 错误：{out_dir / 'errors.csv'}",
        "",
        "风险提示：这是研究回溯与浮动跟踪，不构成投资建议；未连接券商、未执行真实交易。",
    ])
    (out_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"output_dir": str(out_dir), "rows": len(rows), "errors": len(errors), "avg_net": avg_net, "stop_hits": hit_stop, "target_hits": hit_target}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
