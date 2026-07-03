from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[2]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))
DEFAULT_INPUT = (
    BASE_DIR
    / "reports"
    / "automation_5_14_50"
    / "saved_recommendations_backtest_20260701_180700"
    / "saved_recommendation_trades.csv"
)


def parse_float(value: Any, default: float = math.nan) -> float:
    try:
        if value in ("", None):
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def parse_int(value: Any, default: int = 0) -> int:
    try:
        if value in ("", None):
            return default
        return int(float(value))
    except (TypeError, ValueError):
        return default


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def grouped_signal_rows(rows: list[dict[str, str]], scope: str) -> list[tuple[str, list[dict[str, str]]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        if row.get("scope") == scope:
            grouped[str(row.get("signal_date", ""))].append(row)
    return [
        (date, sorted(items, key=lambda item: parse_int(item.get("rank"))))
        for date, items in sorted(grouped.items())
        if date
    ]


def return_for_mode(row: dict[str, str], mode: str) -> tuple[float, str, str]:
    if mode == "fixed5":
        value = parse_float(row.get("fixed5_return"))
        if math.isnan(value):
            value = parse_float(row.get("fixed5_eval_return"), 0.0)
        status = row.get("fixed5_status", "")
        exit_date = row.get("fixed5_eval_date") or row.get("fixed5_sell_date") or ""
        return value, status, exit_date
    if mode == "ma5":
        value = parse_float(row.get("ma5_return"), 0.0)
        status = row.get("ma5_status", "")
        exit_date = row.get("ma5_exit_date") or ""
        return value, status, exit_date
    raise ValueError(f"unsupported mode: {mode}")


def build_trade(
    date: str,
    candidates: list[dict[str, str]],
    selected: dict[str, str] | None,
    budget: int,
    mode: str,
) -> dict[str, Any]:
    if selected is None:
        return {
            "signal_date": date,
            "budget": budget,
            "mode": mode,
            "action": "skip",
            "skip_reason": "no_affordable_candidate",
            "candidate_count": len(candidates),
            "skipped_candidates": ";".join(
                f"{row.get('rank')}:{row.get('secucode')}@{parse_float(row.get('entry_price'), 0.0):.2f}"
                for row in candidates
            ),
        }

    entry_price = parse_float(selected.get("entry_price"), 0.0)
    one_lot_cost = entry_price * 100
    lots = int(budget // one_lot_cost) if one_lot_cost > 0 else 0
    capital_used = round(lots * one_lot_cost, 2)
    stock_return, status, exit_date = return_for_mode(selected, mode)
    pnl = round(capital_used * stock_return, 2)
    selected_rank = parse_int(selected.get("rank"))
    unaffordable = [
        row.get("secucode", "")
        for row in candidates
        if parse_int(row.get("rank")) < selected_rank
    ]
    return {
        "signal_date": date,
        "budget": budget,
        "mode": mode,
        "action": "buy",
        "selected_rank": selected_rank,
        "secucode": selected.get("secucode", ""),
        "name": selected.get("name", ""),
        "entry_price": entry_price,
        "one_lot_cost": round(one_lot_cost, 2),
        "lots": lots,
        "capital_used": capital_used,
        "return": stock_return,
        "pnl": pnl,
        "status": status,
        "exit_date": exit_date,
        "pnl_type": "realized" if status == "closed" else "floating",
        "mark_refreshed": "no",
        "replaced_unaffordable": ";".join(unaffordable),
        "skip_reason": "",
        "candidate_count": len(candidates),
    }


def apply_mark_price_to_trade(trade: dict[str, Any], close: float, as_of_date: str) -> None:
    entry_price = float(trade.get("entry_price") or 0.0)
    capital_used = float(trade.get("capital_used") or 0.0)
    if entry_price <= 0 or capital_used <= 0:
        return
    stock_return = close / entry_price - 1.0
    trade["return"] = stock_return
    trade["pnl"] = round(capital_used * stock_return, 2)
    trade["exit_date"] = as_of_date
    trade["mark_refreshed"] = "yes"


def refresh_open_marks(trades: list[dict[str, Any]], as_of_date: str) -> None:
    from scripts.stock_strategy.backtest_10b_tencent import fetch_bars

    for trade in trades:
        if trade.get("action") != "buy" or trade.get("pnl_type") != "floating":
            continue
        try:
            beg = str(trade.get("signal_date", "")).replace("-", "")
            end = as_of_date.replace("-", "")
            bars = fetch_bars(str(trade.get("secucode", "")), beg, end, timeout=10)
            eligible = [bar for bar in bars if bar.trade_date <= as_of_date]
            if eligible:
                apply_mark_price_to_trade(trade, close=eligible[-1].close, as_of_date=eligible[-1].trade_date)
        except Exception as exc:  # noqa: BLE001 - keep replay usable when a single mark fails.
            trade["mark_error"] = str(exc)


def replay_budget_mode(
    rows: list[dict[str, str]],
    budget: int,
    mode: str,
    scope: str = "strict_1450_saved",
    replace_unaffordable: bool = True,
) -> list[dict[str, Any]]:
    trades: list[dict[str, Any]] = []
    for date, candidates in grouped_signal_rows(rows, scope):
        ranked = candidates if replace_unaffordable else candidates[:1]
        selected = None
        for row in ranked:
            entry_price = parse_float(row.get("entry_price"), 0.0)
            if entry_price > 0 and entry_price * 100 <= budget:
                selected = row
                break
        trades.append(build_trade(date, ranked, selected, budget, mode))
    return trades


def summarize(trades: list[dict[str, Any]]) -> dict[str, Any]:
    buys = [row for row in trades if row.get("action") == "buy"]
    closed = [row for row in buys if row.get("pnl_type") == "realized"]
    floating = [row for row in buys if row.get("pnl_type") == "floating"]
    return {
        "signals": len(trades),
        "buys": len(buys),
        "skips": sum(1 for row in trades if row.get("action") == "skip"),
        "closed": len(closed),
        "open": len(floating),
        "closed_win_rate": (
            sum(1 for row in closed if float(row.get("return") or 0.0) > 0) / len(closed)
            if closed
            else 0.0
        ),
        "realized_pnl": round(sum(float(row.get("pnl") or 0.0) for row in closed), 2),
        "floating_pnl": round(sum(float(row.get("pnl") or 0.0) for row in floating), 2),
        "total_pnl": round(sum(float(row.get("pnl") or 0.0) for row in buys), 2),
        "capital_used_sum": round(sum(float(row.get("capital_used") or 0.0) for row in buys), 2),
        "replacements": sum(1 for row in buys if row.get("replaced_unaffordable")),
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "signal_date",
        "budget",
        "mode",
        "action",
        "selected_rank",
        "secucode",
        "name",
        "entry_price",
        "one_lot_cost",
        "lots",
        "capital_used",
        "return",
        "pnl",
        "status",
        "exit_date",
        "pnl_type",
        "mark_refreshed",
        "mark_error",
        "replaced_unaffordable",
        "skip_reason",
        "candidate_count",
        "skipped_candidates",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def pct(value: float) -> str:
    return f"{value:.2%}"


def money(value: float) -> str:
    return f"{value:.2f}"


def write_report(output_dir: Path, summaries: dict[str, dict[str, Any]], trades: list[dict[str, Any]], as_of_date: str) -> None:
    lines = [
        "# 14:50策略递补买入复盘",
        "",
        f"- 截止日期：{as_of_date}",
        "- 口径：仅使用真实保存的14:50前三候选 `strict_1450_saved`。",
        "- 新规则：若排名靠前股票一手金额超过单票预算，则顺延买入下一个预算内可以买一手的候选；若前三都买不起才跳过。",
        "- 成本：沿用既有复盘口径；未满卖出日的信号按运行时可取行情刷新浮动收益，无法刷新时保留源文件评估收益。",
        "",
        "## 总览",
        "| 预算 | 卖出规则 | 信号 | 买入 | 跳过 | 已闭合 | 持有中 | 递补次数 | 闭合胜率 | 已实现 | 浮动 | 合计盈亏 |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for key, item in summaries.items():
        budget, mode = key.split("_", 1)
        lines.append(
            f"| {int(budget):,} | {mode} | {item['signals']} | {item['buys']} | {item['skips']} | "
            f"{item['closed']} | {item['open']} | {item['replacements']} | {pct(item['closed_win_rate'])} | "
            f"{money(item['realized_pnl'])} | {money(item['floating_pnl'])} | {money(item['total_pnl'])} |"
        )

    lines.extend(
        [
            "",
            "## 递补明细",
            "| 日期 | 预算 | 规则 | 买入排名 | 代码 | 名称 | 买入价 | 手数 | 本金 | 收益率 | 盈亏 | 递补掉的股票 | 状态 |",
            "|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---|---|",
        ]
    )
    for row in trades:
        if row.get("action") != "buy":
            continue
        lines.append(
            f"| {row.get('signal_date')} | {int(row.get('budget')):,} | {row.get('mode')} | "
            f"{row.get('selected_rank')} | {row.get('secucode')} | {row.get('name')} | "
            f"{float(row.get('entry_price') or 0.0):.2f} | {row.get('lots')} | "
            f"{float(row.get('capital_used') or 0.0):.2f} | {pct(float(row.get('return') or 0.0))} | "
            f"{float(row.get('pnl') or 0.0):.2f} | {row.get('replaced_unaffordable') or ''} | {row.get('status')} |"
        )

    skips = [row for row in trades if row.get("action") == "skip"]
    if skips:
        lines.extend(["", "## 仍然跳过", "| 日期 | 预算 | 规则 | 原因 | 前三候选 |", "|---|---:|---|---|---|"])
        for row in skips:
            lines.append(
                f"| {row.get('signal_date')} | {int(row.get('budget')):,} | {row.get('mode')} | "
                f"{row.get('skip_reason')} | {row.get('skipped_candidates', '')} |"
            )

    lines.extend(
        [
            "",
            "## 文件",
            f"- {output_dir / 'affordable_replacement_trades.csv'}",
            f"- {output_dir / 'summary.json'}",
            "",
            "风险提示：本报告只做策略复盘和研究，不构成投资建议；未连接券商，未执行交易。",
        ]
    )
    (output_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def run(input_path: Path, output_dir: Path, as_of_date: str, budgets: list[int], modes: list[str]) -> Path:
    rows = load_rows(input_path)
    all_trades: list[dict[str, Any]] = []
    summaries: dict[str, dict[str, Any]] = {}
    for budget in budgets:
        for mode in modes:
            trades = replay_budget_mode(rows, budget=budget, mode=mode)
            refresh_open_marks(trades, as_of_date)
            all_trades.extend(trades)
            summaries[f"{budget}_{mode}"] = summarize(trades)
    output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(output_dir / "affordable_replacement_trades.csv", all_trades)
    (output_dir / "summary.json").write_text(json.dumps(summaries, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(output_dir, summaries, all_trades, as_of_date)
    return output_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Replay saved 14:50 recommendations with affordable-candidate replacement.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--as-of-date", default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument("--budgets", nargs="+", type=int, default=[30000, 40000])
    parser.add_argument("--modes", nargs="+", default=["fixed5", "ma5"])
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = args.output_dir or (
        BASE_DIR
        / "reports"
        / "automation_5_14_50"
        / f"affordable_replacement_replay_asof_{args.as_of_date.replace('-', '')}"
    )
    path = run(args.input, output_dir, args.as_of_date, args.budgets, args.modes)
    print(path)


if __name__ == "__main__":
    main()
