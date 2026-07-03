from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[2]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from scripts.stock_strategy.backtest_10b_tencent import DailyBar, fetch_bars
from scripts.stock_strategy.run_hold5_tail_candidates import ma5_exit_decision, ma5_exit_plan, mean


POSITION_FIELDS = [
    "secucode",
    "code",
    "name",
    "market",
    "status",
    "source",
    "added_date",
    "buy_date",
    "buy_price",
    "quantity",
    "amount",
    "weight",
    "strategy",
    "check_date",
    "max_exit_date",
    "notes",
]


def compact_date(value: str) -> str:
    return value.replace("-", "")


def split_secucode(secucode: str) -> tuple[str, str]:
    code = secucode.split(".")[0]
    market = secucode.split(".")[1] if "." in secucode else ("SH" if code.startswith("6") else "SZ")
    return code, market


def build_position_row(
    secucode: str,
    name: str,
    buy_date: str,
    buy_price: float,
    quantity: str = "",
    amount: str = "",
    weight: str = "",
    notes: str = "",
) -> dict[str, str]:
    code, market = split_secucode(secucode)
    exit_plan = ma5_exit_plan(buy_date)
    return {
        "secucode": secucode,
        "code": code,
        "name": name,
        "market": market,
        "status": "holding",
        "source": "user",
        "added_date": datetime.now().astimezone().isoformat(timespec="seconds"),
        "buy_date": buy_date,
        "buy_price": f"{buy_price:.2f}",
        "quantity": str(quantity),
        "amount": str(amount),
        "weight": str(weight),
        "strategy": "hold5_ma5_exit",
        "check_date": str(exit_plan["check_date"]),
        "max_exit_date": str(exit_plan["max_exit_date"]),
        "notes": notes,
    }


def load_positions(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return [
            {field: str(row.get(field) or "") for field in POSITION_FIELDS}
            for row in csv.DictReader(handle)
        ]


def save_positions(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=POSITION_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in POSITION_FIELDS})


def upsert_position(rows: list[dict[str, str]], new_row: dict[str, str]) -> list[dict[str, str]]:
    result = [row for row in rows if row.get("secucode") != new_row.get("secucode") or row.get("status") != "holding"]
    result.append(new_row)
    return result


def latest_bar_on_or_before(bars: list[DailyBar], as_of_date: str) -> DailyBar | None:
    eligible = [bar for bar in sorted(bars, key=lambda item: item.trade_date) if bar.trade_date <= as_of_date]
    return eligible[-1] if eligible else None


def held_sessions(bars: list[DailyBar], buy_date: str, as_of_date: str) -> int:
    return sum(1 for bar in bars if buy_date < bar.trade_date <= as_of_date)


def ma5_at(bars: list[DailyBar], as_of_date: str) -> float:
    eligible = [bar for bar in sorted(bars, key=lambda item: item.trade_date) if bar.trade_date <= as_of_date]
    return mean([bar.close for bar in eligible[-5:]])


def review_position(row: dict[str, str], bars: list[DailyBar], as_of_date: str) -> dict[str, Any]:
    buy_date = str(row.get("buy_date") or "")
    buy_price = float(row.get("buy_price") or 0.0)
    sorted_bars = sorted(bars, key=lambda item: item.trade_date)
    current = latest_bar_on_or_before(sorted_bars, as_of_date)
    if current is None or not buy_date or buy_price <= 0:
        return {
            "secucode": row.get("secucode", ""),
            "name": row.get("name", ""),
            "buy_date": buy_date,
            "as_of_date": as_of_date,
            "action": "wait",
            "reason": "missing_price_or_position_data",
            "missing": "缺少行情或买入信息",
        }

    sessions = held_sessions(sorted_bars, buy_date, current.trade_date)
    ma5 = ma5_at(sorted_bars, current.trade_date)
    decision = ma5_exit_decision(
        entry_price=buy_price,
        close=current.close,
        ma5=ma5,
        held_sessions=sessions,
    )
    return {
        "secucode": row.get("secucode", ""),
        "name": row.get("name", ""),
        "buy_date": buy_date,
        "buy_price": buy_price,
        "as_of_date": current.trade_date,
        "close": current.close,
        "ma5": ma5,
        "held_sessions": sessions,
        "check_date": row.get("check_date", ""),
        "max_exit_date": row.get("max_exit_date", ""),
        "net_return": decision["net_return"],
        "action": decision["action"],
        "reason": decision["reason"],
        "missing": "",
    }


def position_path(base_dir: Path) -> Path:
    return base_dir / "data" / "live_trading" / "user_positions.csv"


def add_position(base_dir: Path, row: dict[str, str]) -> Path:
    path = position_path(base_dir)
    rows = upsert_position(load_positions(path), row)
    save_positions(path, rows)
    return path


def review_positions(base_dir: Path, as_of_date: str, timeout: int = 8) -> Path:
    rows = [row for row in load_positions(position_path(base_dir)) if row.get("status") in ("", "holding")]
    reviews: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    end = compact_date(as_of_date)
    for row in rows:
        try:
            beg = compact_date(str(row.get("buy_date") or as_of_date))
            bars = fetch_bars(str(row.get("secucode")), beg, end, timeout=timeout)
            reviews.append(review_position(row, bars, as_of_date))
        except Exception as exc:  # noqa: BLE001 - review should keep other positions inspectable.
            errors.append({"secucode": row.get("secucode", ""), "name": row.get("name", ""), "error": str(exc)})

    output_dir = base_dir / "reports" / "automation_5_14_50" / f"position_review_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    output_dir.mkdir(parents=True, exist_ok=True)
    fields = ["secucode", "name", "buy_date", "buy_price", "as_of_date", "close", "ma5", "held_sessions", "check_date", "max_exit_date", "net_return", "action", "reason", "missing"]
    with (output_dir / "position_reviews.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows([{field: row.get(field, "") for field in fields} for row in reviews])
    with (output_dir / "errors.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["secucode", "name", "error"])
        writer.writeheader()
        writer.writerows(errors)
    summary = {
        "as_of_date": as_of_date,
        "positions": len(rows),
        "reviews": len(reviews),
        "sell_count": sum(1 for row in reviews if row.get("action") == "sell"),
        "hold_count": sum(1 for row in reviews if row.get("action") == "hold"),
        "errors": len(errors),
        "position_reviews_csv": str(output_dir / "position_reviews.csv"),
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(output_dir, reviews, errors, as_of_date)
    return output_dir


def pct(value: Any) -> str:
    try:
        return f"{float(value):.2%}"
    except (TypeError, ValueError):
        return ""


def write_report(output_dir: Path, reviews: list[dict[str, Any]], errors: list[dict[str, str]], as_of_date: str) -> None:
    lines = [
        "# 持仓MA5卖出确认",
        "",
        f"- 评估日期：{as_of_date}",
        "- 规则：第5个交易日开始检查；净收益不为正或收盘跌破MA5卖出；盈利且站上MA5继续持有；最长持有15个交易日。",
        f"- 覆盖持仓：{len(reviews)} 条；卖出确认 {sum(1 for row in reviews if row.get('action') == 'sell')} 条；继续持有 {sum(1 for row in reviews if row.get('action') == 'hold')} 条；错误 {len(errors)} 条。",
        "",
        "## 明细",
        "| 代码 | 名称 | 买入日 | 买入价 | 评估日 | 收盘 | MA5 | 已持有交易日 | 净收益 | 动作 | 原因 |",
        "|---|---|---|---:|---|---:|---:|---:|---:|---|---|",
    ]
    for row in reviews:
        lines.append(
            f"| {row.get('secucode', '')} | {row.get('name', '')} | {row.get('buy_date', '')} | "
            f"{float(row.get('buy_price') or 0.0):.2f} | {row.get('as_of_date', '')} | "
            f"{float(row.get('close') or 0.0):.2f} | {float(row.get('ma5') or 0.0):.2f} | "
            f"{row.get('held_sessions', '')} | {pct(row.get('net_return'))} | {row.get('action', '')} | {row.get('reason', '')} |"
        )
    if errors:
        lines.extend(["", "## 错误", "| 代码 | 名称 | 原因 |", "|---|---|---|"])
        for error in errors:
            lines.append(f"| {error['secucode']} | {error['name']} | {error['error']} |")
    lines.extend([
        "",
        "## 文件",
        f"- CSV：{output_dir / 'position_reviews.csv'}",
        f"- 摘要：{output_dir / 'summary.json'}",
        "",
        "风险提示：本工具只做持仓策略研究提示，不连接券商、不执行真实交易，不构成投资建议。",
    ])
    (output_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Track manual hold5 positions and review MA5 exit signals")
    parser.add_argument("--base-dir", type=Path, default=BASE_DIR)
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add")
    add.add_argument("--secucode", required=True)
    add.add_argument("--name", required=True)
    add.add_argument("--buy-date", required=True)
    add.add_argument("--buy-price", type=float, required=True)
    add.add_argument("--quantity", default="")
    add.add_argument("--amount", default="")
    add.add_argument("--weight", default="")
    add.add_argument("--notes", default="")

    review = sub.add_parser("review")
    review.add_argument("--as-of-date", default=datetime.now().strftime("%Y-%m-%d"))
    review.add_argument("--timeout", type=int, default=8)

    args = parser.parse_args()
    if args.command == "add":
        path = add_position(
            args.base_dir,
            build_position_row(
                secucode=args.secucode,
                name=args.name,
                buy_date=args.buy_date,
                buy_price=args.buy_price,
                quantity=args.quantity,
                amount=args.amount,
                weight=args.weight,
                notes=args.notes,
            ),
        )
        print(json.dumps({"positions_csv": str(path)}, ensure_ascii=False, indent=2))
    elif args.command == "review":
        output_dir = review_positions(args.base_dir, args.as_of_date, timeout=args.timeout)
        print(json.dumps({"output_dir": str(output_dir)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
