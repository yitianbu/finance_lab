from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[2]
KLINE_CACHE_DIR = Path("/private/tmp/range_review_20260617")
REPORT_DIR = BASE_DIR / "reports" / "range_trader"
CANONICAL_SCAN_DIRS = [
    "20260609_191551",
    "20260610_173425",
    "20260611_222236",
    "20260612_170825",
    "20260615_155000",
    "20260616_173043",
]
MAX_HOLD_DAYS = 5


@dataclass(frozen=True)
class Bar:
    day: str
    open: float
    high: float
    low: float
    close: float


def as_float(value: Any, default: float = 0.0) -> float:
    try:
        if value in (None, ""):
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def pct(value: float | None) -> str:
    if value is None:
        return ""
    return f"{value:+.2%}"


def sina_symbol(secucode: str) -> str:
    code, suffix = secucode.split(".")
    return ("sh" if suffix == "SH" else "sz") + code


def load_bars(secucode: str) -> list[Bar]:
    path = KLINE_CACHE_DIR / f"{sina_symbol(secucode)}.json"
    rows = json.loads(path.read_text(encoding="utf-8"))
    bars = [
        Bar(
            day=str(row["day"]),
            open=as_float(row["open"]),
            high=as_float(row["high"]),
            low=as_float(row["low"]),
            close=as_float(row["close"]),
        )
        for row in rows
    ]
    return sorted(bars, key=lambda item: item.day)


def load_candidates() -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for scan_dir in CANONICAL_SCAN_DIRS:
        path = REPORT_DIR / "all_a_scan" / scan_dir / "pool_scan.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        for row in payload.get("results", []):
            if not row.get("tradable"):
                continue
            key = (str(row.get("latest_date") or ""), str(row.get("secucode") or ""))
            if key in seen:
                continue
            seen.add(key)
            item = dict(row)
            item["scan_dir"] = scan_dir
            candidates.append(item)
    return candidates


def find_entry_index(bars: list[Bar], signal_date: str) -> int | None:
    for index, bar in enumerate(bars):
        if bar.day > signal_date:
            return index
    return None


def strict_replay(candidate: dict[str, Any], bars: list[Bar]) -> dict[str, Any]:
    entry_idx = find_entry_index(bars, str(candidate["latest_date"]))
    if entry_idx is None:
        return {
            "entered": False,
            "entry_date": "",
            "entry_price": None,
            "exit_date": "",
            "exit_price": None,
            "strict_return": None,
            "exit_reason": "pending_no_next_bar",
            "strict_status": "pending",
        }

    buy_low = as_float(candidate["buy_zone_low"])
    buy_high = as_float(candidate["buy_zone_high"])
    stop_loss = as_float(candidate["stop_loss"])
    take_profit = as_float(candidate["take_profit"])
    entry_bar = bars[entry_idx]

    if entry_bar.open < buy_low:
        return {
            "entered": False,
            "entry_date": entry_bar.day,
            "entry_price": None,
            "exit_date": "",
            "exit_price": None,
            "strict_return": None,
            "exit_reason": "open_below_buy_zone",
            "strict_status": "no_fill",
        }
    if entry_bar.low > buy_high:
        return {
            "entered": False,
            "entry_date": entry_bar.day,
            "entry_price": None,
            "exit_date": "",
            "exit_price": None,
            "strict_return": None,
            "exit_reason": "not_filled",
            "strict_status": "no_fill",
        }
    if entry_bar.low <= stop_loss:
        return {
            "entered": False,
            "entry_date": entry_bar.day,
            "entry_price": None,
            "exit_date": "",
            "exit_price": None,
            "strict_return": None,
            "exit_reason": "entry_day_stop_breached",
            "strict_status": "no_fill",
        }

    entry_price = buy_high
    if entry_bar.open <= buy_high:
        entry_price = min(max(entry_bar.open, buy_low), buy_high)

    if entry_idx + 1 >= len(bars):
        return {
            "entered": True,
            "entry_date": entry_bar.day,
            "entry_price": entry_price,
            "exit_date": entry_bar.day,
            "exit_price": entry_bar.close,
            "strict_return": entry_bar.close / entry_price - 1.0,
            "exit_reason": "no_t1_bar_mark_to_market",
            "strict_status": "open_mtm",
        }

    exit_idx = min(len(bars) - 1, entry_idx + max(1, MAX_HOLD_DAYS))
    exit_bar = bars[exit_idx]
    exit_price = exit_bar.close
    exit_reason = "max_hold_close"
    for idx in range(entry_idx + 1, exit_idx + 1):
        bar = bars[idx]
        if bar.open <= stop_loss:
            exit_bar = bar
            exit_price = bar.open
            exit_reason = "t1_stop_gap"
            break
        if bar.open >= take_profit:
            exit_bar = bar
            exit_price = bar.open
            exit_reason = "t1_take_profit_gap"
            break
        if bar.low <= stop_loss:
            exit_bar = bar
            exit_price = stop_loss
            exit_reason = "t1_stop_loss"
            break
        if bar.high >= take_profit:
            exit_bar = bar
            exit_price = take_profit
            exit_reason = "t1_take_profit"
            break

    return {
        "entered": True,
        "entry_date": entry_bar.day,
        "entry_price": entry_price,
        "exit_date": exit_bar.day,
        "exit_price": exit_price,
        "strict_return": exit_price / entry_price - 1.0,
        "exit_reason": exit_reason,
        "strict_status": "closed",
    }


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def median(values: list[float]) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def main() -> None:
    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")
    candidates = load_candidates()
    rows: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []

    for candidate in candidates:
        try:
            bars = load_bars(candidate["secucode"])
            latest = bars[-1]
            signal_close = as_float(candidate["latest_close"])
            signal_return = latest.close / signal_close - 1.0
            replay = strict_replay(candidate, bars)
            rows.append({
                **candidate,
                "review_latest_date": latest.day,
                "review_latest_close": latest.close,
                "signal_close_return": signal_return,
                **replay,
            })
        except Exception as exc:  # noqa: BLE001
            errors.append({
                "secucode": str(candidate.get("secucode")),
                "name": str(candidate.get("name")),
                "error": str(exc),
            })

    out_base = REPORT_DIR / f"review_all_a_range_candidates_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    csv_path = out_base.with_suffix(".csv")
    md_path = out_base.with_suffix(".md")
    if rows:
        fieldnames = [
            "scan_dir", "latest_date", "secucode", "name", "latest_close",
            "review_latest_date", "review_latest_close", "signal_close_return",
            "buy_zone_low", "buy_zone_high", "stop_loss", "take_profit",
            "reward_risk", "trades", "total_return", "max_drawdown",
            "strict_status", "entry_date", "entry_price", "exit_date",
            "exit_price", "strict_return", "exit_reason",
        ]
        with csv_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)

    signal_returns = [row["signal_close_return"] for row in rows]
    closed = [row for row in rows if row["strict_status"] == "closed"]
    open_mtm = [row for row in rows if row["strict_status"] == "open_mtm"]
    no_fill = [row for row in rows if row["strict_status"] == "no_fill"]
    strict_closed_returns = [row["strict_return"] for row in closed if row["strict_return"] is not None]
    strict_all_entered_returns = [
        row["strict_return"]
        for row in rows
        if row["strict_status"] in {"closed", "open_mtm"} and row["strict_return"] is not None
    ]

    lines = [
        "# 全A区间模型正式候选收益复盘",
        "",
        f"- Generated at: {generated_at}",
        f"- Review target: canonical all-A scans {', '.join(CANONICAL_SCAN_DIRS)}",
        "- Market data source: Sina daily K-line endpoint cached under /private/tmp/range_review_20260617",
        "- Scope: research replay only; no broker connection and no real trading",
        "",
        "## Summary",
        "",
        f"- Deduplicated formal candidates: {len(rows)}",
        f"- Latest review date: {max((row['review_latest_date'] for row in rows), default='')}",
        f"- Signal-close mark-to-market: average {pct(mean(signal_returns))}, median {pct(median(signal_returns))}, win rate {sum(1 for value in signal_returns if value > 0)}/{len(signal_returns)}",
        f"- Strict BUY_ZONE replay: closed fills {len(closed)}, open mark-to-market {len(open_mtm)}, no fill / invalidated {len(no_fill)}",
        f"- Strict closed return: average {pct(mean(strict_closed_returns))}, median {pct(median(strict_closed_returns))}, win rate {sum(1 for value in strict_closed_returns if value > 0)}/{len(strict_closed_returns)}",
        f"- Strict entered including open MTM: average {pct(mean(strict_all_entered_returns))}, win rate {sum(1 for value in strict_all_entered_returns if value > 0)}/{len(strict_all_entered_returns)}",
        f"- Data errors: {len(errors)}",
        "",
        "## Strict Filled / Open Trades",
        "",
        "| Signal | Code | Name | Entry | Exit/MTM | Reason | Return |",
        "|---|---|---|---:|---:|---|---:|",
    ]
    for row in [item for item in rows if item["strict_status"] in {"closed", "open_mtm"}]:
        lines.append(
            f"| {row['latest_date']} | {row['secucode']} | {row['name']} | "
            f"{row['entry_date']} @ {row['entry_price']:.2f} | "
            f"{row['exit_date']} @ {row['exit_price']:.2f} | "
            f"{row['exit_reason']} | {pct(row['strict_return'])} |"
        )

    lines.extend([
        "",
        "## All Candidates",
        "",
        "| Signal | Code | Name | Latest Close Return | Strict Replay | Reason |",
        "|---|---|---|---:|---:|---|",
    ])
    for row in rows:
        strict_text = pct(row["strict_return"]) if row["strict_return"] is not None else "no fill"
        lines.append(
            f"| {row['latest_date']} | {row['secucode']} | {row['name']} | "
            f"{pct(row['signal_close_return'])} | {strict_text} | {row['exit_reason']} |"
        )

    if errors:
        lines.extend(["", "## Errors", "", "| Code | Name | Error |", "|---|---|---|"])
        for error in errors:
            lines.append(f"| {error['secucode']} | {error['name']} | {error['error']} |")

    lines.extend([
        "",
        "## Readout",
        "",
        "The raw signal-close basket is still weak and close to flat-to-negative after the latest two sessions. The strict execution discipline remains the main source of risk control: most weak paths are rejected by open-below-zone or entry-day-stop checks, while filled trades are mostly take-profit exits. The current open 603949.SH position is only marked to market because T+1 makes same-day selling unavailable.",
    ])
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(md_path)
    print(csv_path)


if __name__ == "__main__":
    main()
