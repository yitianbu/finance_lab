from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parents[2]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from scripts.stock_strategy.backtest_10b_tencent import DailyBar, SymbolInfo, fetch_universe
from scripts.stock_strategy.crowding_historical_validation import (
    benchmark_return_map,
    calc_v2_metrics,
)
from scripts.stock_strategy.crowding_warning_v1 import (
    avg_pairwise_corr,
    calc_metrics,
    clamp,
    fetch_sina_bars,
    mean,
    pct,
    score_ratio,
)


OUT_DIR = BASE_DIR / "reports" / "crowding_warning"


def parse_ymd(value: str) -> datetime:
    return datetime.strptime(value, "%Y%m%d")


def fetch_one(symbol: SymbolInfo, end: str, datalen: int) -> tuple[SymbolInfo, list[DailyBar] | None, str | None]:
    try:
        return symbol, fetch_sina_bars(symbol.secucode, end, datalen=datalen, timeout=18), None
    except Exception as exc:  # noqa: BLE001
        return symbol, None, str(exc)


def risk_level(countdown_score: float, watch_score: float) -> str:
    if countdown_score >= 80:
        return "极端高危"
    if countdown_score >= 70:
        return "高危"
    if countdown_score >= 60:
        return "30日预警"
    if watch_score >= 80:
        return "极端过热观察"
    if watch_score >= 60:
        return "过热观察"
    if watch_score >= 40:
        return "升温"
    return "正常"


def trigger_name(v2: dict[str, float]) -> str:
    triggers = {
        "回落": v2["rollover_countdown"],
        "核心冲顶": v2["core_blowoff"],
        "末端冲顶": v2["mega_blowoff"],
        "全市场泡沫": v2["broad_bubble"],
        "低波白马": v2["low_vol_quality"],
    }
    name, value = max(triggers.items(), key=lambda pair: pair[1])
    return "-" if value <= 0 else name


def score_current_day(
    args: argparse.Namespace,
    symbols: list[SymbolInfo],
    all_bars: dict[str, list[DailyBar]],
    benchmark_bars: list[DailyBar],
    trade_date: str,
    include_basket: bool,
) -> dict[str, Any] | None:
    symbol_by_code = {symbol.secucode: symbol for symbol in symbols}
    metrics = []
    v2_by_code = {}
    for secucode, bars in all_bars.items():
        symbol = symbol_by_code.get(secucode)
        if symbol is None:
            continue
        item = calc_metrics(symbol, bars, args.lookback, trade_date)
        v2_item = calc_v2_metrics(secucode, bars, trade_date)
        if item is not None and v2_item is not None:
            metrics.append(item)
            v2_by_code[secucode] = v2_item

    benchmark = benchmark_return_map(benchmark_bars, trade_date, [5, 20, 60, 120])
    if benchmark is None:
        return None

    liquid = [item for item in metrics if item.amount5 >= args.min_amount]
    basket_metrics = sorted(liquid, key=lambda item: item.ret20, reverse=True)[: args.top_n]
    basket_v2 = [v2_by_code[item.secucode] for item in basket_metrics if item.secucode in v2_by_code]
    if len(basket_v2) < args.min_basket:
        return None

    basket_ret5 = mean([item.ret5 for item in basket_v2])
    basket_ret20 = mean([item.ret20 for item in basket_v2])
    basket_ret60 = mean([item.ret60 for item in basket_v2])
    basket_ret120 = mean([item.ret120 for item in basket_v2])
    basket_amount_ratio60 = mean([item.amount_ratio60 for item in basket_v2])
    basket_distance_ma60 = mean([item.distance_ma60 for item in basket_v2])
    basket_drawdown60 = mean([item.drawdown60 for item in basket_v2])
    basket_drawdown120 = mean([item.drawdown120 for item in basket_v2])
    basket_vol20 = mean([item.volatility20 for item in basket_v2])
    below_ma20_ratio = mean([1.0 if item.below_ma20 else 0.0 for item in basket_v2])
    below_ma60_ratio = mean([1.0 if item.below_ma60 else 0.0 for item in basket_v2])
    basket_corr = avg_pairwise_corr(basket_v2)  # type: ignore[arg-type]

    rel60 = basket_ret60 - benchmark[60]
    rel120 = basket_ret120 - benchmark[120]
    relative_60_score = score_ratio(rel60, 0.08, 0.30)
    relative_120_score = score_ratio(rel120, 0.12, 0.60)
    absolute_60_score = score_ratio(basket_ret60, 0.18, 0.60)
    absolute_120_score = score_ratio(basket_ret120, 0.30, 1.20)
    long_performance_score = mean([
        max(relative_60_score, absolute_60_score),
        max(relative_120_score, absolute_120_score),
    ])
    extension_ma60_score = score_ratio(basket_distance_ma60, 0.08, 0.30)
    near_high60_score = clamp((0.12 - abs(min(basket_drawdown60, 0.0))) / 0.12 * 100.0)
    trend_pressure_score = mean([long_performance_score, extension_ma60_score, near_high60_score])

    volume_60_score = score_ratio(basket_amount_ratio60, 1.05, 2.20)
    corr_score = score_ratio(basket_corr, 0.15, 0.55)
    volatility_score = score_ratio(basket_vol20, 0.022, 0.060)
    heat_score = max(volume_60_score, mean([volume_60_score, corr_score, volatility_score]))

    ret20_decay_score = score_ratio((basket_ret60 / 3.0) - basket_ret20, 0.00, 0.16)
    ret5_decay_score = score_ratio((basket_ret20 / 4.0) - basket_ret5, 0.00, 0.12)
    breadth_decay_score = score_ratio(below_ma20_ratio, 0.10, 0.45)
    ma60_break_score = score_ratio(below_ma60_ratio, 0.05, 0.30)
    early_decay_score = mean([ret20_decay_score, ret5_decay_score, breadth_decay_score, ma60_break_score])

    blended_watch_score = 0.55 * trend_pressure_score + 0.20 * heat_score + 0.25 * early_decay_score
    extreme_trend_score = 0.70 * trend_pressure_score + 0.30 * heat_score
    watch_score = max(
        blended_watch_score,
        extreme_trend_score
        if trend_pressure_score >= 75.0 or (trend_pressure_score >= 60.0 and heat_score >= 50.0)
        else blended_watch_score,
    )

    rollover_raw_score = 0.60 * early_decay_score + 0.30 * long_performance_score + 0.10 * heat_score
    ma60_rollover_bonus = score_ratio(0.10 - basket_distance_ma60, 0.0, 0.10) * 0.15
    rollover_candidate_score = clamp(rollover_raw_score + ma60_rollover_bonus)
    rollover_countdown_score = rollover_candidate_score if (
        rollover_candidate_score >= 60.0
        and basket_distance_ma60 <= 0.10
        and (long_performance_score >= 80.0 or rel120 >= 0.50)
    ) else 0.0
    core_blowoff_score = watch_score if (
        watch_score >= 70.0
        and trend_pressure_score >= 85.0
        and heat_score >= 60.0
        and rel120 >= 0.50
    ) else 0.0
    mega_blowoff_score = watch_score if (
        watch_score >= 60.0
        and heat_score >= 55.0
        and long_performance_score >= 75.0
        and early_decay_score <= 30.0
        and (rel120 >= 0.70 or rel60 >= 0.90 or basket_ret120 >= 1.35)
    ) else 0.0
    broad_bubble_score = watch_score if (
        watch_score >= 60.0
        and long_performance_score >= 80.0
        and basket_ret120 >= 0.85
        and benchmark[120] >= 0.50
        and rel120 <= 0.25
    ) else 0.0
    low_vol_quality_score = watch_score if (
        watch_score >= 60.0
        and trend_pressure_score >= 60.0
        and heat_score >= 70.0
        and rel120 >= 0.30
        and basket_ret120 <= 0.65
        and volatility_score <= 15.0
    ) else 0.0
    countdown_score = max(
        rollover_countdown_score,
        core_blowoff_score,
        mega_blowoff_score,
        broad_bubble_score,
        low_vol_quality_score,
    )
    v2 = {
        "watch_score": watch_score,
        "blended_watch": blended_watch_score,
        "extreme_trend": extreme_trend_score,
        "trend_pressure": trend_pressure_score,
        "heat": heat_score,
        "early_decay": early_decay_score,
        "rollover_raw": rollover_raw_score,
        "ma60_rollover_bonus": ma60_rollover_bonus,
        "rollover_countdown": rollover_countdown_score,
        "core_blowoff": core_blowoff_score,
        "mega_blowoff": mega_blowoff_score,
        "broad_bubble": broad_bubble_score,
        "low_vol_quality": low_vol_quality_score,
    }

    return {
        "date": trade_date,
        "valid_metrics": len(metrics),
        "liquid_metrics": len(liquid),
        "basket_count": len(basket_v2),
        "countdown_score": countdown_score,
        "watch_score": watch_score,
        "risk_level": risk_level(countdown_score, watch_score),
        "trigger": trigger_name(v2),
        "v2": v2,
        "raw": {
            "basket_ret5": basket_ret5,
            "benchmark_ret5": benchmark[5],
            "basket_ret20": basket_ret20,
            "benchmark_ret20": benchmark[20],
            "basket_ret60": basket_ret60,
            "benchmark_ret60": benchmark[60],
            "basket_ret120": basket_ret120,
            "benchmark_ret120": benchmark[120],
            "basket_amount_ratio60": basket_amount_ratio60,
            "basket_avg_corr": basket_corr,
            "basket_distance_ma60": basket_distance_ma60,
            "basket_drawdown_from_60d_high": basket_drawdown60,
            "basket_drawdown_from_120d_high": basket_drawdown120,
            "basket_daily_vol20": basket_vol20,
            "below_ma20_ratio": below_ma20_ratio,
            "below_ma60_ratio": below_ma60_ratio,
        },
        "component_scores": {
            "relative_60d": relative_60_score,
            "relative_120d": relative_120_score,
            "absolute_60d": absolute_60_score,
            "absolute_120d": absolute_120_score,
            "long_performance": long_performance_score,
            "extension_ma60": extension_ma60_score,
            "near_high60": near_high60_score,
            "volume_60d": volume_60_score,
            "internal_correlation": corr_score,
            "volatility": volatility_score,
            "ret20_decay": ret20_decay_score,
            "ret5_decay": ret5_decay_score,
            "breadth_decay": breadth_decay_score,
            "ma60_break": ma60_break_score,
        },
        "basket": [asdict(item) for item in basket_metrics] if include_basket else [],
    }


def build_payload(args: argparse.Namespace) -> dict[str, Any]:
    end_dt = parse_ymd(args.end)
    beg = (end_dt - timedelta(days=args.calendar_days)).strftime("%Y%m%d")
    symbols = fetch_universe()
    if args.max_symbols:
        symbols = symbols[: args.max_symbols]

    datalen = max(args.series_days + 180, 220)
    all_bars: dict[str, list[DailyBar]] = {}
    errors: list[dict[str, str]] = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(fetch_one, symbol, args.end, datalen): symbol
            for symbol in symbols
        }
        for future in as_completed(futures):
            symbol, bars, error = future.result()
            if error or not bars:
                errors.append({"secucode": symbol.secucode, "name": symbol.name, "error": error or "empty"})
                continue
            all_bars[symbol.secucode] = bars

    benchmark_bars = fetch_sina_bars(args.benchmark, args.end, datalen=datalen, timeout=18)
    latest_dates = [bars[-1].trade_date for bars in all_bars.values() if bars]
    if not latest_dates:
        raise RuntimeError("no kline data fetched")
    latest_date = max(latest_dates)

    date_counts: dict[str, int] = {}
    for bars in all_bars.values():
        for bar in bars:
            if bar.trade_date <= latest_date:
                date_counts[bar.trade_date] = date_counts.get(bar.trade_date, 0) + 1
    liquid_floor = max(100, int(len(all_bars) * 0.4))
    candidate_dates = [
        day for day, count in sorted(date_counts.items())
        if count >= liquid_floor and day <= latest_date
    ][-args.series_days:]

    series = []
    for day in candidate_dates:
        item = score_current_day(args, symbols, all_bars, benchmark_bars, day, include_basket=False)
        if item is not None:
            series.append(item)

    latest = score_current_day(args, symbols, all_bars, benchmark_bars, latest_date, include_basket=True)
    if latest is None:
        raise RuntimeError(f"latest date {latest_date} cannot be scored")

    return {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "end": args.end,
        "latest_date": latest_date,
        "benchmark": args.benchmark,
        "top_n": args.top_n,
        "lookback": args.lookback,
        "symbols_requested": len(symbols),
        "symbols_loaded": len(all_bars),
        "error_count": len(errors),
        "errors": errors[:20],
        "latest": latest,
        "series": series,
    }


def write_markdown(payload: dict[str, Any], path: Path) -> None:
    latest = payload["latest"]
    raw = latest["raw"]
    lines = [
        "# 抱团 30日预警指数 v2 当前读数",
        "",
        f"- 生成时间：{payload['generated_at']}",
        f"- 最新交易日：{payload['latest_date']}",
        f"- 口径：成交过滤后，自动选取 20日涨幅 Top {payload['top_n']} 作为当前抱团篮子；基准 {payload['benchmark']}。",
        f"- 股票加载：请求 {payload['symbols_requested']} 只，成功 {payload['symbols_loaded']} 只，错误 {payload['error_count']} 只。",
        "",
        "## 最新风险",
        "",
        "| 指标 | 数值 |",
        "|---|---:|",
        f"| 30日预警分 | {latest['countdown_score']:.1f} |",
        f"| 过热观察分 | {latest['watch_score']:.1f} |",
        f"| 状态 | {latest['risk_level']} |",
        f"| 主要触发 | {latest['trigger']} |",
        f"| 抱团篮子 20日收益 | {pct(raw['basket_ret20'])} |",
        f"| 抱团篮子 60日相对基准 | {pct(raw['basket_ret60'] - raw['benchmark_ret60'])} |",
        f"| 抱团篮子 120日相对基准 | {pct(raw['basket_ret120'] - raw['benchmark_ret120'])} |",
        f"| 距 MA60 | {pct(raw['basket_distance_ma60'])} |",
        f"| 跌破 MA20 比例 | {raw['below_ma20_ratio']:.1%} |",
        "",
        f"## 最近 {len(payload['series'])} 日",
        "",
        "| 日期 | 30日预警分 | 过热观察分 | 状态 | 触发 | 趋势压力 | 热度 | 衰减 | 20日收益 | 60日相对 | 120日相对 | 距MA60 | 跌破MA20 |",
        "|---|---:|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for item in payload["series"]:
        item_raw = item["raw"]
        item_v2 = item["v2"]
        lines.append(
            "| "
            f"{item['date']} | {item['countdown_score']:.1f} | {item['watch_score']:.1f} | "
            f"{item['risk_level']} | {item['trigger']} | {item_v2['trend_pressure']:.1f} | "
            f"{item_v2['heat']:.1f} | {item_v2['early_decay']:.1f} | "
            f"{pct(item_raw['basket_ret20'])} | "
            f"{pct(item_raw['basket_ret60'] - item_raw['benchmark_ret60'])} | "
            f"{pct(item_raw['basket_ret120'] - item_raw['benchmark_ret120'])} | "
            f"{pct(item_raw['basket_distance_ma60'])} | {item_raw['below_ma20_ratio']:.1%} |"
        )
    lines.extend([
        "",
        "## 当前抱团篮子 Top 20",
        "",
        "| 排名 | 代码 | 名称 | 20日 | 5日 | 距20日高点 | 成交额5日/前15日 |",
        "|---:|---|---|---:|---:|---:|---:|",
    ])
    for rank, item in enumerate(latest["basket"][:20], 1):
        lines.append(
            "| "
            f"{rank} | {item['secucode']} | {item['name']} | {pct(item['ret20'])} | "
            f"{pct(item['ret5'])} | {pct(item['drawdown20'])} | {item['amount_ratio']:.2f} |"
        )
    lines.extend([
        "",
        "## 口径说明",
        "",
        "- 30日预警分只在倒计时触发器出现时给分；更早的过热只进入观察分。",
        "- 自动篮子代表近期最强方向，不等同于基金真实持仓或固定行业指数。",
        "- 分数用于风险监控，不构成买卖建议。",
        "",
    ])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build current A-share crowding 30-day warning index v2.")
    parser.add_argument("--end", default=datetime.now().strftime("%Y%m%d"))
    parser.add_argument("--lookback", type=int, default=20)
    parser.add_argument("--calendar-days", type=int, default=320)
    parser.add_argument("--series-days", type=int, default=20)
    parser.add_argument("--top-n", type=int, default=50)
    parser.add_argument("--min-basket", type=int, default=30)
    parser.add_argument("--min-amount", type=float, default=100_000_000)
    parser.add_argument("--workers", type=int, default=20)
    parser.add_argument("--max-symbols", type=int, default=0)
    parser.add_argument("--benchmark", default="000001.SH")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = build_payload(args)
    stamp = f"{payload['latest_date'].replace('-', '')}_{datetime.now().strftime('%H%M%S')}"
    json_path = OUT_DIR / f"crowding_warning_v2_current_{stamp}.json"
    md_path = OUT_DIR / f"crowding_warning_v2_current_{stamp}.md"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(payload, md_path)
    print(json.dumps({
        "json": str(json_path),
        "markdown": str(md_path),
        "latest_date": payload["latest_date"],
        "latest": {
            "countdown_score": round(payload["latest"]["countdown_score"], 1),
            "watch_score": round(payload["latest"]["watch_score"], 1),
            "risk_level": payload["latest"]["risk_level"],
            "trigger": payload["latest"]["trigger"],
        },
        "series": [
            {
                "date": item["date"],
                "countdown_score": round(item["countdown_score"], 1),
                "watch_score": round(item["watch_score"], 1),
                "risk_level": item["risk_level"],
                "trigger": item["trigger"],
            }
            for item in payload["series"]
        ],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
