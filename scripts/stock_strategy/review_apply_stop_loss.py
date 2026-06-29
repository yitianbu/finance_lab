from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
ROUND_TRIP_COST = 0.0013


def as_float(value: str) -> float:
    return float(value) if value not in {"", "None"} else 0.0


def pct(value: float) -> str:
    return f"{value:.2%}"


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def apply_stop(row: dict[str, str], entry_col: str, stop_col: str, stop_hit_col: str = "stop_hit") -> dict[str, str | float | bool]:
    entry = as_float(row[entry_col])
    stop = as_float(row[stop_col])
    current_net = as_float(row["net_return_after_cost"])
    stop_hit = row[stop_hit_col] == "True"
    stop_net = stop / entry - 1.0 - ROUND_TRIP_COST if stop_hit and entry > 0 else current_net
    return {
        **row,
        "entry_price_for_stop": entry,
        "current_net_return": current_net,
        "stop_exit_return": stop_net,
        "stop_applied": stop_hit,
        "return_delta_vs_hold": stop_net - current_net,
    }


def summarize(rows: list[dict[str, str | float | bool]]) -> dict[str, float | int]:
    count = len(rows)
    if not rows:
        return {"count": 0, "avg_hold": 0.0, "avg_stop": 0.0, "wins_stop": 0, "stops": 0}
    avg_hold = sum(float(row["current_net_return"]) for row in rows) / count
    avg_stop = sum(float(row["stop_exit_return"]) for row in rows) / count
    return {
        "count": count,
        "avg_hold": avg_hold,
        "avg_stop": avg_stop,
        "wins_stop": sum(1 for row in rows if float(row["stop_exit_return"]) > 0),
        "stops": sum(1 for row in rows if row["stop_applied"] is True),
    }


def write_csv(path: Path, rows: list[dict[str, str | float | bool]]) -> None:
    if not rows:
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    signal_path = BASE_DIR / "reports/automation_5_14_50/review_signal_close_20260615_153629/signal_close_returns.csv"
    next_path = BASE_DIR / "reports/automation_5_14_50/review_next_open_20260615_153217/next_open_returns.csv"
    signal_rows = [apply_stop(row, "signal_close_entry", "original_stop_loss") for row in load_rows(signal_path)]
    next_rows = [apply_stop(row, "next_open_entry", "original_stop_loss") for row in load_rows(next_path)]

    signal_intended_mature = [
        row for row in signal_rows
        if row["note"] == "intended_tail_run" and row["signal_date"] != row["evaluation_date"]
    ]
    next_intended = [row for row in next_rows if row["note"] == "intended_tail_run"]

    out_dir = BASE_DIR / "reports/automation_5_14_50" / f"review_stop_loss_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    out_dir.mkdir(parents=True, exist_ok=True)
    write_csv(out_dir / "signal_close_stop_returns.csv", signal_rows)
    write_csv(out_dir / "next_open_stop_returns.csv", next_rows)

    signal_summary = summarize(signal_rows)
    signal_mature_summary = summarize(signal_intended_mature)
    next_summary = summarize(next_rows)
    next_intended_summary = summarize(next_intended)

    lines = [
        "# 加入止损卖出后的收益回溯",
        "",
        f"- 生成时间：{datetime.now().astimezone().isoformat(timespec='seconds')}",
        "- 规则：如果持有路径触及原止损价，则按止损价卖出并扣往返 13bp；未触损则按 2026-06-15 收盘价估值。",
        "- 说明：这里只加入止损，不加入目标价止盈。",
        "",
        "## 汇总",
        "| 入口口径 | 样本 | 原持有到当前均值 | 加止损后均值 | 正收益数 | 触发止损数 |",
        "|---|---:|---:|---:|---:|---:|",
        f"| 信号日收盘买入-全部 | {signal_summary['count']} | {pct(float(signal_summary['avg_hold']))} | {pct(float(signal_summary['avg_stop']))} | {signal_summary['wins_stop']}/{signal_summary['count']} | {signal_summary['stops']}/{signal_summary['count']} |",
        f"| 信号日收盘买入-真正尾盘且隔日持有 | {signal_mature_summary['count']} | {pct(float(signal_mature_summary['avg_hold']))} | {pct(float(signal_mature_summary['avg_stop']))} | {signal_mature_summary['wins_stop']}/{signal_mature_summary['count']} | {signal_mature_summary['stops']}/{signal_mature_summary['count']} |",
        f"| 次日开盘买入-可评估全部 | {next_summary['count']} | {pct(float(next_summary['avg_hold']))} | {pct(float(next_summary['avg_stop']))} | {next_summary['wins_stop']}/{next_summary['count']} | {next_summary['stops']}/{next_summary['count']} |",
        f"| 次日开盘买入-真正尾盘 | {next_intended_summary['count']} | {pct(float(next_intended_summary['avg_hold']))} | {pct(float(next_intended_summary['avg_stop']))} | {next_intended_summary['wins_stop']}/{next_intended_summary['count']} | {next_intended_summary['stops']}/{next_intended_summary['count']} |",
        "",
        "## 信号日收盘买入明细",
        "| 批次 | 股票 | 入场 | 当前收益 | 止损价 | 是否止损卖出 | 加止损后收益 | 影响 |",
        "|---|---|---:|---:|---:|---|---:|---:|",
    ]
    for row in signal_rows:
        lines.append(
            f"| {row['batch']} | {row['secucode']} {row['name']} | {float(row['entry_price_for_stop']):.2f} | "
            f"{pct(float(row['current_net_return']))} | {as_float(str(row['original_stop_loss'])):.2f} | "
            f"{'是' if row['stop_applied'] else '否'} | {pct(float(row['stop_exit_return']))} | {pct(float(row['return_delta_vs_hold']))} |"
        )
    lines.extend([
        "",
        "## 次日开盘买入明细",
        "| 批次 | 股票 | 入场 | 当前收益 | 止损价 | 是否止损卖出 | 加止损后收益 | 影响 |",
        "|---|---|---:|---:|---:|---|---:|---:|",
    ])
    for row in next_rows:
        lines.append(
            f"| {row['batch']} | {row['secucode']} {row['name']} | {float(row['entry_price_for_stop']):.2f} | "
            f"{pct(float(row['current_net_return']))} | {as_float(str(row['original_stop_loss'])):.2f} | "
            f"{'是' if row['stop_applied'] else '否'} | {pct(float(row['stop_exit_return']))} | {pct(float(row['return_delta_vs_hold']))} |"
        )
    lines.extend([
        "",
        "## 文件",
        f"- 信号日收盘+止损 CSV：{out_dir / 'signal_close_stop_returns.csv'}",
        f"- 次日开盘+止损 CSV：{out_dir / 'next_open_stop_returns.csv'}",
        "",
        "风险提示：这是研究回溯，不构成投资建议；未连接券商、未执行真实交易。",
    ])
    (out_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print({
        "output_dir": str(out_dir),
        "signal": signal_summary,
        "signal_mature": signal_mature_summary,
        "next_open": next_summary,
        "next_intended": next_intended_summary,
    })


if __name__ == "__main__":
    main()
