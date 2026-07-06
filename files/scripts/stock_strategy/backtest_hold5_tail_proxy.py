from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parents[2]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from scripts.stock_strategy.backtest_10b_tencent import (
    DailyBar,
    SymbolInfo,
    fetch_bars,
    fetch_universe,
)
from scripts.stock_strategy.run_hold5_tail_candidates import (
    FEATURE_WEIGHTS,
    ROUND_TRIP_COST,
    as_float,
    candidate_quality_score,
    close_return,
    distance,
    max_drawdown,
    mean,
    relative_strength_profile,
    safe_div,
)

CACHE_DIR = BASE_DIR / "data" / "hold5_tail_proxy" / "klines"
REPORT_DIR = BASE_DIR / "reports" / "automation_5_14_50"


@dataclass(frozen=True)
class ProxyBar:
    date: str
    open: float
    close: float
    high: float
    low: float
    volume: float
    amount: float
    amplitude: float
    pct: float
    change: float
    turnover: float


def pct(value: float) -> str:
    return f"{value * 100:.2f}%"


def compact_date(value: str) -> str:
    return value.replace("-", "")


def dash_date(value: str) -> str:
    return f"{value[:4]}-{value[4:6]}-{value[6:8]}"


def proxy_bars(raw: list[DailyBar]) -> list[ProxyBar]:
    bars: list[ProxyBar] = []
    prev_close = 0.0
    for item in sorted(raw, key=lambda bar: bar.trade_date):
        pct_change = safe_div(item.close, prev_close, 1.0) - 1.0 if prev_close > 0 else item.pct_change / 100.0
        bars.append(ProxyBar(
            date=item.trade_date,
            open=item.open,
            close=item.close,
            high=item.high,
            low=item.low,
            volume=item.amount,
            amount=item.amount,
            amplitude=safe_div(item.high - item.low, prev_close, 0.0) if prev_close > 0 else 0.0,
            pct=pct_change,
            change=item.close - prev_close if prev_close > 0 else 0.0,
            turnover=item.turnover,
        ))
        prev_close = item.close
    return bars


def feature_vector(bars: list[ProxyBar], idx: int) -> dict[str, float]:
    bar = bars[idx]
    prev = bars[idx - 1] if idx > 0 else bar
    ma5 = mean([item.close for item in bars[max(0, idx - 4): idx + 1]]) or bar.close
    ma20 = mean([item.close for item in bars[max(0, idx - 19): idx + 1]]) or bar.close
    vol20 = mean([item.volume for item in bars[max(0, idx - 19): idx + 1]]) or bar.volume
    day_range = max(bar.high - bar.low, 1e-9)
    return {
        "pct": bar.pct,
        "prev_pct": prev.pct,
        "ret3": close_return(bars, max(0, idx - 3), idx),
        "ret5": close_return(bars, max(0, idx - 5), idx),
        "amp": safe_div(bar.high - bar.low, prev.close),
        "close_pos": safe_div(bar.close - bar.low, day_range, 0.5),
        "dist_ma5": safe_div(bar.close, ma5, 1.0) - 1.0,
        "dist_ma20": safe_div(bar.close, ma20, 1.0) - 1.0,
        "atr_pct": atr_pct(bars, idx),
        "vol_ratio_log": math.log(max(safe_div(bar.volume, vol20, 1.0), 1e-6)),
    }


def atr_pct(bars: list[ProxyBar], idx: int, period: int = 14) -> float:
    values: list[float] = []
    for pos in range(max(1, idx - period + 1), idx + 1):
        prev = bars[pos - 1].close
        bar = bars[pos]
        tr = max(bar.high - bar.low, abs(bar.high - prev), abs(bar.low - prev))
        values.append(safe_div(tr, bar.close))
    return mean(values)


def load_cached_bars(symbol: SymbolInfo, beg: str, end: str) -> list[ProxyBar]:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = CACHE_DIR / f"{symbol.secucode}.json"
    raw: list[dict[str, Any]] | None = None
    if path.exists():
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
            if payload.get("end", "") >= end and payload.get("beg", "") <= beg:
                raw = payload.get("bars") or []
        except json.JSONDecodeError:
            raw = None
    if raw is None:
        bars = fetch_bars(symbol.secucode, beg, end, timeout=25)
        raw = [asdict(item) for item in bars]
        path.write_text(json.dumps({"beg": beg, "end": end, "bars": raw}, ensure_ascii=False), encoding="utf-8")
    return proxy_bars([DailyBar(**item) for item in raw])


def board_limit_pct(secucode: str) -> float:
    code, suffix = secucode.split(".")
    if suffix == "BJ" or code.startswith("8"):
        return 0.30
    if code.startswith(("300", "301", "688")):
        return 0.20
    return 0.10


def is_near_one_price_limit(secucode: str, bar: ProxyBar) -> bool:
    prev_close = bar.close / (1.0 + bar.pct) if abs(1.0 + bar.pct) > 1e-9 else 0.0
    if prev_close <= 0:
        return False
    amp = (bar.high - bar.low) / prev_close
    return bar.pct >= board_limit_pct(secucode) - 0.005 and amp <= 0.012


def analyze_candidate(
    symbol: SymbolInfo,
    bars: list[ProxyBar],
    idx: int,
    industry_stats: dict[str, dict[str, float]],
    analog_count: int,
) -> dict[str, Any] | None:
    if idx < 220:
        return None
    current = bars[idx]
    current_features = feature_vector(bars, idx)
    strength = relative_strength_profile(bars, idx)
    start = max(60, idx - 185)
    end_idx = idx - 6
    analogs: list[tuple[float, int, float, float]] = []
    for pos in range(start, end_idx + 1):
        dist = distance(current_features, feature_vector(bars, pos))
        net = close_return(bars, pos, pos + 5) - ROUND_TRIP_COST
        trough = min(item.low for item in bars[pos + 1: pos + 6])
        hold_dd = safe_div(trough, bars[pos].close, 1.0) - 1.0
        analogs.append((dist, pos, net, hold_dd))
    selected = sorted(analogs, key=lambda item: item[0])[:analog_count]
    returns = [item[2] for item in selected]
    drawdowns = [item[3] for item in selected]
    if len(returns) < 30:
        return None
    wins = [item for item in returns if item > 0]
    losses = [item for item in returns if item < 0]
    pf_value = safe_div(sum(wins), abs(sum(losses)), 999.0 if wins else 0.0)
    avg = mean(returns)
    med = statistics.median(returns) if returns else 0.0
    p70 = sorted(returns)[int(0.70 * (len(returns) - 1))] if returns else 0.0
    worst = min(returns) if returns else 0.0
    day_range = max(current.high - current.low, 1e-9)
    close_pos = safe_div(current.close - current.low, day_range, 0.5)
    atr = atr_pct(bars, idx)
    stop_risk = min(0.065, max(0.025, 0.80 * atr))
    reward_risk = safe_div(max(avg, p70, 0.0), stop_risk)
    stats = industry_stats.get(symbol.industry, {})

    reject: list[str] = []
    if safe_div(len(wins), len(returns)) < 0.55:
        reject.append("win_rate_lt_55")
    if avg <= 0:
        reject.append("avg_return_not_positive")
    if pf_value < 1.2:
        reject.append("profit_factor_lt_1_2")
    if reward_risk < 1.0:
        reject.append("stop_risk_gt_expected_reward")
    if close_pos < 0.50:
        reject.append("weak_tail_position")
    if is_near_one_price_limit(symbol.secucode, current):
        reject.append("one_price_or_near_limit_up")

    sample_drawdown = max_drawdown(returns)
    worst_hold = min(drawdowns) if drawdowns else 0.0
    score = candidate_quality_score(
        win_rate=safe_div(len(wins), len(returns)),
        avg_return=avg,
        median_return=med,
        profit_factor=pf_value,
        reward_risk=reward_risk,
        worst_return=worst,
        worst_hold_drawdown=worst_hold,
        sample_max_drawdown=sample_drawdown,
        close_pos=close_pos,
        amount=current.amount,
        industry_avg_pct=stats.get("avg_pct", 0.0),
        industry_adv_ratio=stats.get("adv_ratio", 0.0),
        ret5=current_features.get("ret5", 0.0),
        dist_ma20=current_features.get("dist_ma20", 0.0),
        vol_ratio_log=current_features.get("vol_ratio_log", 0.0),
    )

    formal = not reject
    tier = "观察"
    if formal:
        if reward_risk >= 1.2 and worst >= -0.12 and worst_hold >= -0.15 and sample_drawdown >= -0.35 and close_pos >= 0.55:
            tier = "核心"
        elif reward_risk >= 0.9 and worst >= -0.22 and sample_drawdown >= -0.45:
            tier = "进取"

    return {
        "date": current.date,
        "secucode": symbol.secucode,
        "name": symbol.name,
        "tier": tier,
        "formal": formal,
        "score": score,
        "entry_price": current.close,
        "ret20": strength["ret20"],
        "hist_ret20_median": strength["hist_ret20_median"],
        "strength_percentile_20d": strength["strength_percentile_20d"],
        "strength_state": strength["strength_state"],
        "win_rate": safe_div(len(wins), len(returns)),
        "avg_return": avg,
        "median_return": med,
        "profit_factor": pf_value,
        "reward_risk": reward_risk,
        "worst_return": worst,
        "worst_hold_drawdown": min(drawdowns) if drawdowns else 0.0,
        "max_drawdown": max_drawdown(returns),
        "close_pos": close_pos,
        "reject_reason": ";".join(reject),
    }


def eligible(symbol: SymbolInfo, bar: ProxyBar) -> bool:
    if bar.close < 2 or bar.amount < 300_000_000:
        return False
    if bar.pct <= -0.04 or bar.pct >= (board_limit_pct(symbol.secucode) - 0.015):
        return False
    if is_near_one_price_limit(symbol.secucode, bar):
        return False
    close_pos = safe_div(bar.close - bar.low, max(bar.high - bar.low, 1e-9), 0.5)
    return close_pos >= 0.45


def preselect_score(symbol: SymbolInfo, bar: ProxyBar, industry_stats: dict[str, dict[str, float]]) -> float:
    close_pos = safe_div(bar.close - bar.low, max(bar.high - bar.low, 1e-9), 0.5)
    return (
        close_pos * 30
        + min(bar.amount / 1e9, 20) * 4
        + bar.pct * 120
        + industry_stats.get(symbol.industry, {}).get("avg_pct", 0.0) * 100
    )


def planned_exit_idx(calendar: list[str], idx: int, hold_days: int = 5) -> int:
    return min(idx + hold_days, len(calendar) - 1)


def build_analyzed_export_rows(
    analyzed: list[dict[str, Any]],
    bars_by_code: dict[str, list[ProxyBar]],
    bar_pos_by_code: dict[str, dict[str, int]],
    trade_date: str,
    evaluation_date: str,
    limit: int,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if limit <= 0:
        return rows
    for rank, row in enumerate(analyzed[:limit], start=1):
        bars = bars_by_code.get(row["secucode"])
        signal_pos = bar_pos_by_code.get(row["secucode"], {}).get(trade_date)
        if not bars or signal_pos is None:
            continue
        exit_pos = bar_pos_by_code[row["secucode"]].get(evaluation_date, min(signal_pos + 5, len(bars) - 1))
        rows.append({
            **row,
            "rank": rank,
            "evaluation_date": evaluation_date,
            "strategy_return": close_return(bars, signal_pos, exit_pos) - ROUND_TRIP_COST,
        })
    return rows


def select_trade_candidates(
    analyzed: list[dict[str, Any]],
    limit: int = 3,
    require_strength_state: str = "",
) -> list[dict[str, Any]]:
    tradeable_tiers = {"核心", "进取"}
    return [
        row
        for row in analyzed
        if str(row.get("tier") or "") in tradeable_tiers and not str(row.get("reject_reason") or "")
        and (not require_strength_state or str(row.get("strength_state") or "") == require_strength_state)
    ][:limit]


def rolling_gate(history: list[dict[str, Any]]) -> tuple[bool, dict[str, Any]]:
    completed = [item for item in history if item["evaluation_date"] < item["date_current"]]
    window = completed[-30:]
    if len(window) < 12:
        return True, {
            "benchmark_gate": "样本不足",
            "medium_sample_days": len(window),
            "medium_avg_return": 0.0,
            "medium_win_rate": 0.0,
            "medium_excess_return": 0.0,
            "medium_excess_best_return": 0.0,
            "medium_max_drawdown": 0.0,
        }
    returns = [as_float(item["baseline_top3_return"]) for item in window]
    excess = [as_float(item["baseline_top3_return"]) - as_float(item["sh_return"]) for item in window]
    excess_best = [
        as_float(item["baseline_top3_return"])
        - max(as_float(item["sh_return"]), as_float(item["sz_return"]), as_float(item["cy_return"]))
        for item in window
    ]
    avg_return = mean(returns)
    win_rate = safe_div(sum(1 for item in returns if item > 0), len(returns))
    excess_return = mean(excess)
    excess_best_return = mean(excess_best)
    medium_max_drawdown = max_drawdown(returns)
    allowed = (
        avg_return >= 0.008
        and win_rate >= 0.50
        and excess_best_return >= -0.025
        and medium_max_drawdown >= -0.65
    )
    return allowed, {
        "benchmark_gate": "已达标" if allowed else "未达标",
        "medium_sample_days": len(window),
        "medium_avg_return": avg_return,
        "medium_win_rate": win_rate,
        "medium_excess_return": excess_return,
        "medium_excess_best_return": excess_best_return,
        "medium_max_drawdown": medium_max_drawdown,
    }


def compound_return(values: list[float]) -> float:
    equity = 1.0
    for value in values:
        equity *= 1.0 + value
    return equity - 1.0


def summarize_returns(values: list[float]) -> dict[str, Any]:
    if not values:
        return {"n": 0, "avg": 0.0, "wins": 0, "win_rate": 0.0, "compound": 0.0, "best": 0.0, "worst": 0.0, "max_drawdown": 0.0}
    return {
        "n": len(values),
        "avg": mean(values),
        "wins": sum(1 for item in values if item > 0),
        "win_rate": safe_div(sum(1 for item in values if item > 0), len(values)),
        "compound": compound_return(values),
        "best": max(values),
        "worst": min(values),
        "max_drawdown": max_drawdown(values),
    }


def summarize_rolling_capital(
    pick_rows: list[dict[str, Any]],
    *,
    rank1_only: bool,
    daily_capital: float = 3.0,
    hold_days: int = 5,
) -> dict[str, Any]:
    completed = [row for row in pick_rows if bool(row.get("holding_complete"))]
    if rank1_only:
        completed = [row for row in completed if int(as_float(row.get("rank"))) == 1]
        stake = daily_capital
    else:
        stake = safe_div(daily_capital, 3.0)
    pnl = sum(as_float(row.get("strategy_return")) * stake for row in completed)
    deployed = len(completed) * stake
    max_capital = daily_capital * hold_days
    return {
        "completed_trades": len(completed),
        "deployed_capital": deployed,
        "max_capital": max_capital,
        "pnl": pnl,
        "pnl_on_deployed": safe_div(pnl, deployed),
        "pnl_on_max_capital": safe_div(pnl, max_capital),
    }


def month_key(date: str) -> str:
    return date[:7]


def write_outputs(
    output_dir: Path,
    daily_rows: list[dict[str, Any]],
    pick_rows: list[dict[str, Any]],
    meta: dict[str, Any],
    analyzed_rows: list[dict[str, Any]] | None = None,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    complete_daily_rows = [row for row in daily_rows if bool(row.get("holding_complete"))]
    if daily_rows:
        with (output_dir / "daily_detail.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(daily_rows[0].keys()))
            writer.writeheader()
            writer.writerows(daily_rows)
    if pick_rows:
        with (output_dir / "daily_picks.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(pick_rows[0].keys()))
            writer.writeheader()
            writer.writerows(pick_rows)
    if analyzed_rows:
        with (output_dir / "daily_analyzed_candidates.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(analyzed_rows[0].keys()))
            writer.writeheader()
            writer.writerows(analyzed_rows)

    months = sorted({month_key(row["date"]) for row in complete_daily_rows})
    monthly_rows: list[dict[str, Any]] = []
    for month in months:
        rows = [row for row in complete_daily_rows if month_key(row["date"]) == month]
        metrics = {
            "baseline_top3": summarize_returns([as_float(row["baseline_top3_return"]) for row in rows]),
            "gated_top3": summarize_returns([as_float(row["gated_top3_return"]) for row in rows]),
            "sh": summarize_returns([as_float(row["sh_return"]) for row in rows]),
            "sz": summarize_returns([as_float(row["sz_return"]) for row in rows]),
            "cy": summarize_returns([as_float(row["cy_return"]) for row in rows]),
        }
        monthly_rows.append({
            "month": month,
            "days": len(rows),
            "blocked_days": sum(1 for row in rows if row["gate_allowed"] == "False"),
            "baseline_avg": metrics["baseline_top3"]["avg"],
            "baseline_compound": metrics["baseline_top3"]["compound"],
            "baseline_win_rate": metrics["baseline_top3"]["win_rate"],
            "gated_avg": metrics["gated_top3"]["avg"],
            "gated_compound": metrics["gated_top3"]["compound"],
            "gated_win_rate": metrics["gated_top3"]["win_rate"],
            "sh_compound": metrics["sh"]["compound"],
            "sz_compound": metrics["sz"]["compound"],
            "cy_compound": metrics["cy"]["compound"],
            "gated_excess_sh": metrics["gated_top3"]["compound"] - metrics["sh"]["compound"],
        })
    with (output_dir / "monthly_summary.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(monthly_rows[0].keys()) if monthly_rows else ["month"])
        writer.writeheader()
        writer.writerows(monthly_rows)

    summary = {
        **meta,
        "baseline_top3": summarize_returns([as_float(row["baseline_top3_return"]) for row in complete_daily_rows]),
        "gated_top3": summarize_returns([as_float(row["gated_top3_return"]) for row in complete_daily_rows]),
        "rank1": summarize_returns([as_float(row["rank1_return"]) for row in complete_daily_rows]),
        "sh": summarize_returns([as_float(row["sh_return"]) for row in complete_daily_rows]),
        "sz": summarize_returns([as_float(row["sz_return"]) for row in complete_daily_rows]),
        "cy": summarize_returns([as_float(row["cy_return"]) for row in complete_daily_rows]),
        "rolling_top3_capital": summarize_rolling_capital(pick_rows, rank1_only=False),
        "rolling_rank1_capital": summarize_rolling_capital(pick_rows, rank1_only=True),
        "blocked_days": sum(1 for row in daily_rows if row["gate_allowed"] == "False"),
        "complete_days": len(complete_daily_rows),
        "truncated_days": len(daily_rows) - len(complete_daily_rows),
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# 5日持有尾盘策略代理回测",
        "",
        f"- 区间：{meta['start_date']} 至 {meta['end_date']}",
        f"- 生成时间：{meta['generated_at']}",
        f"- 候选池：当前非ST沪深股票 {meta['universe_count']} 只；成功取得K线 {meta['bars_ok']} 只；K线错误 {meta['bar_errors']} 只。",
        "- 方法限制：历史日线收盘代理，不是真实历史14:50快照；使用当前股票池，存在幸存者偏差。",
        f"- 统计口径：总览只统计完整5个交易日批次 {summary['complete_days']} 天；截尾未满5日 {summary['truncated_days']} 天不计入总览。",
        "- 大盘竞争力拦截：滚动20个已完成Top3等权批次，至少15批后要求均值>=-1%、相对上证超额>=+0.5%、胜率>=55%；否则当日空仓。",
        "",
        "## 完整5日批次总览",
        "| 方案 | 天数 | 日均 | 胜率 | 最好 | 最差 | 复利 | 最大回撤 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for key, label in [
        ("baseline_top3", "无拦截Top3等权"),
        ("gated_top3", "加拦截Top3等权"),
        ("rank1", "第一名全仓批次"),
        ("sh", "上证指数"),
        ("sz", "深证成指"),
        ("cy", "创业板指"),
    ]:
        item = summary[key]
        lines.append(
            f"| {label} | {item['n']} | {pct(item['avg'])} | {item['wins']}/{item['n']} ({pct(item['win_rate'])}) | "
            f"{pct(item['best'])} | {pct(item['worst'])} | {pct(item['compound'])} | {pct(item['max_drawdown'])} |"
        )
    lines.extend([
        "",
        "## 滚动资金占用口径",
        "| 方案 | 完整交易数 | 最大占用资金单位 | 已部署资金单位 | 收益/最大占用 | 收益/已部署 |",
        "|---|---:|---:|---:|---:|---:|",
    ])
    for key, label in [
        ("rolling_top3_capital", "Top3等权每日买入"),
        ("rolling_rank1_capital", "第一名全仓每日买入"),
    ]:
        item = summary[key]
        lines.append(
            f"| {label} | {item['completed_trades']} | {item['max_capital']:.2f} | {item['deployed_capital']:.2f} | "
            f"{pct(item['pnl_on_max_capital'])} | {pct(item['pnl_on_deployed'])} |"
        )
    lines.extend([
        "",
        "## 完整5日月度汇总",
        "| 月份 | 天数 | 拦截日 | 无拦截复利 | 加拦截复利 | 上证 | 深成指 | 创业板 | 加拦截-上证 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ])
    for row in monthly_rows:
        lines.append(
            f"| {row['month']} | {row['days']} | {row['blocked_days']} | {pct(row['baseline_compound'])} | "
            f"{pct(row['gated_compound'])} | {pct(row['sh_compound'])} | {pct(row['sz_compound'])} | "
            f"{pct(row['cy_compound'])} | {pct(row['gated_excess_sh'])} |"
        )
    lines.extend([
        "",
        "## 文件",
        f"- 每日明细：{output_dir / 'daily_detail.csv'}",
        f"- 每日候选：{output_dir / 'daily_picks.csv'}",
        *([f"- 每日已分析候选Top{meta.get('save_analyzed_top')}：{output_dir / 'daily_analyzed_candidates.csv'}"] if analyzed_rows else []),
        f"- 月度汇总：{output_dir / 'monthly_summary.csv'}",
        f"- 摘要JSON：{output_dir / 'summary.json'}",
        f"- 报告：{output_dir / 'report.md'}",
        "",
        "风险提示：仅为量化研究代理回测，不构成投资建议；未连接券商、未执行真实交易。",
    ])
    (output_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def run(args: argparse.Namespace) -> Path:
    start = dash_date(args.start)
    end = dash_date(args.end)
    fetch_beg = str(max(int(args.start) - 10000, 20200101))
    fetch_end = args.end
    symbols = fetch_universe()
    symbols = [item for item in symbols if item.secucode.endswith((".SH", ".SZ"))]
    if args.max_symbols:
        symbols = symbols[:args.max_symbols]

    bars_by_code: dict[str, list[ProxyBar]] = {}
    errors: dict[str, str] = {}

    def load(symbol: SymbolInfo) -> tuple[str, list[ProxyBar]]:
        return symbol.secucode, load_cached_bars(symbol, fetch_beg, fetch_end)

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {executor.submit(load, symbol): symbol for symbol in symbols}
        for idx, future in enumerate(as_completed(futures), start=1):
            symbol = futures[future]
            try:
                secucode, bars = future.result()
                if bars:
                    bars_by_code[secucode] = bars
            except Exception as exc:  # noqa: BLE001
                errors[symbol.secucode] = f"{type(exc).__name__}: {exc}"
            if idx % 250 == 0:
                print(f"loaded {idx}/{len(symbols)} ok={len(bars_by_code)} errors={len(errors)}", flush=True)

    index_symbols = [
        SymbolInfo("000001.SH", "000001", "上证指数"),
        SymbolInfo("399001.SZ", "399001", "深证成指"),
        SymbolInfo("399006.SZ", "399006", "创业板指"),
    ]
    index_bars = {symbol.secucode: load_cached_bars(symbol, fetch_beg, fetch_end) for symbol in index_symbols}
    calendar = [bar.date for bar in index_bars["000001.SH"] if start <= bar.date <= end]
    index_by_date = {
        code: {bar.date: bar for bar in bars}
        for code, bars in index_bars.items()
    }
    index_pos_by_code = {
        code: {bar.date: idx for idx, bar in enumerate(bars)}
        for code, bars in index_bars.items()
    }
    symbol_by_code = {symbol.secucode: symbol for symbol in symbols}
    bar_pos_by_code = {
        code: {bar.date: idx for idx, bar in enumerate(bars)}
        for code, bars in bars_by_code.items()
    }

    daily_rows: list[dict[str, Any]] = []
    pick_rows: list[dict[str, Any]] = []
    analyzed_rows: list[dict[str, Any]] = []
    history_for_gate: list[dict[str, Any]] = []
    for day_idx, trade_date in enumerate(calendar):
        industry_raw: dict[str, list[ProxyBar]] = defaultdict(list)
        day_bars: list[tuple[SymbolInfo, list[ProxyBar], int, ProxyBar]] = []
        for code, bars in bars_by_code.items():
            pos = bar_pos_by_code.get(code, {}).get(trade_date)
            if pos is None or pos < 220:
                continue
            symbol = symbol_by_code[code]
            bar = bars[pos]
            industry_raw[symbol.industry].append(bar)
            day_bars.append((symbol, bars, pos, bar))
        industry_stats: dict[str, dict[str, float]] = {}
        for industry, items in industry_raw.items():
            industry_stats[industry] = {
                "avg_pct": mean([item.pct for item in items]),
                "adv_ratio": safe_div(sum(1 for item in items if item.pct > 0), len(items)),
                "amount": sum(item.amount for item in items),
            }
        eligible_rows = [
            (preselect_score(symbol, bar, industry_stats), symbol, bars, pos)
            for symbol, bars, pos, bar in day_bars
            if eligible(symbol, bar)
        ]
        eligible_rows.sort(key=lambda item: item[0], reverse=True)
        analyzed: list[dict[str, Any]] = []
        for _, symbol, bars, pos in eligible_rows[:args.max_validate]:
            row = analyze_candidate(symbol, bars, pos, industry_stats, args.analog_count)
            if row is not None:
                analyzed.append(row)
        analyzed.sort(key=lambda row: row["score"], reverse=True)
        selected = select_trade_candidates(analyzed, limit=3, require_strength_state=args.require_strength_state)

        exit_idx = planned_exit_idx(calendar, day_idx)
        evaluation_date = calendar[exit_idx]
        analyzed_rows.extend(build_analyzed_export_rows(
            analyzed,
            bars_by_code,
            bar_pos_by_code,
            trade_date,
            evaluation_date,
            args.save_analyzed_top,
        ))
        returns: list[float] = []
        for rank, row in enumerate(selected, start=1):
            bars = bars_by_code[row["secucode"]]
            signal_pos = bar_pos_by_code[row["secucode"]][trade_date]
            exit_pos = bar_pos_by_code[row["secucode"]].get(evaluation_date, min(signal_pos + 5, len(bars) - 1))
            ret = close_return(bars, signal_pos, exit_pos) - ROUND_TRIP_COST
            returns.append(ret)
            pick = {
                **row,
                "rank": rank,
                "evaluation_date": evaluation_date,
                "holding_complete": exit_idx - day_idx >= 5,
                "strategy_return": ret,
            }
            pick_rows.append(pick)

        baseline_top3 = mean(returns)
        sh_return = close_return(index_bars["000001.SH"], index_pos_by_code["000001.SH"][trade_date], index_pos_by_code["000001.SH"][evaluation_date])
        sz_return = close_return(index_bars["399001.SZ"], index_pos_by_code["399001.SZ"][trade_date], index_pos_by_code["399001.SZ"][evaluation_date])
        cy_return = close_return(index_bars["399006.SZ"], index_pos_by_code["399006.SZ"][trade_date], index_pos_by_code["399006.SZ"][evaluation_date])

        gate_input_history = [dict(item, date_current=trade_date) for item in history_for_gate]
        gate_allowed, gate_metrics = rolling_gate(gate_input_history)
        gated_return = baseline_top3 if gate_allowed else 0.0
        daily = {
            "date": trade_date,
            "evaluation_date": evaluation_date,
            "holding_complete": exit_idx - day_idx >= 5,
            "pick_count": len(selected),
            "gate_allowed": str(gate_allowed),
            **gate_metrics,
            "baseline_top3_return": baseline_top3,
            "gated_top3_return": gated_return,
            "sh_return": sh_return,
            "sz_return": sz_return,
            "cy_return": cy_return,
            "rank1_code": selected[0]["secucode"] if selected else "",
            "rank1_name": selected[0]["name"] if selected else "",
            "rank1_return": returns[0] if returns else 0.0,
        }
        daily_rows.append(daily)
        history_for_gate.append(daily)
        if (day_idx + 1) % 20 == 0:
            print(f"processed {day_idx + 1}/{len(calendar)} {trade_date}", flush=True)

    output_dir = REPORT_DIR / f"two_year_benchmark_gate_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    meta = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "start_date": start,
        "end_date": end,
        "universe_count": len(symbols),
        "bars_ok": len(bars_by_code),
        "bar_errors": len(errors),
        "max_validate": args.max_validate,
        "analog_count": args.analog_count,
        "save_analyzed_top": args.save_analyzed_top,
        "require_strength_state": args.require_strength_state,
    }
    write_outputs(output_dir, daily_rows, pick_rows, meta, analyzed_rows)
    (output_dir / "errors.json").write_text(json.dumps(errors, ensure_ascii=False, indent=2), encoding="utf-8")
    return output_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Backtest hold-5 tail proxy with benchmark gate")
    parser.add_argument("--start", required=True, help="YYYYMMDD")
    parser.add_argument("--end", required=True, help="YYYYMMDD")
    parser.add_argument("--workers", type=int, default=24)
    parser.add_argument("--max-symbols", type=int, default=0)
    parser.add_argument("--max-validate", type=int, default=420)
    parser.add_argument("--analog-count", type=int, default=60)
    parser.add_argument("--save-analyzed-top", type=int, default=0, help="write top N analyzed candidates per day for research")
    parser.add_argument("--require-strength-state", default="", help="only select candidates with this strength_state, e.g. 走强")
    return parser.parse_args()


def main() -> None:
    output_dir = run(parse_args())
    print(json.dumps({"output_dir": str(output_dir)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
