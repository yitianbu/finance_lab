from __future__ import annotations

import argparse
import json
import math
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from pathlib import Path
from statistics import median
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE_DIR = Path(__file__).resolve().parents[2]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from scripts.stock_strategy.backtest_10b_tencent import (
    DailyBar,
    SymbolInfo,
    fetch_bars,
    fetch_universe,
)


OUT_DIR = BASE_DIR / "reports" / "crowding_warning"
SINA_KLINE_URL = "https://quotes.sina.cn/cn/api/json_v2.php/CN_MarketDataService.getKLineData"


@dataclass(frozen=True)
class StockMetrics:
    secucode: str
    name: str
    latest_date: str
    close: float
    ret20: float
    ret5: float
    amount5: float
    amount_prev15: float
    amount_ratio: float
    drawdown20: float
    volatility20: float
    below_ma20: bool
    big_down_5d: bool
    returns20: list[float]


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def pct(value: float) -> str:
    return f"{value:+.2%}"


def score_ratio(value: float, start: float, end: float) -> float:
    if end == start:
        return 0.0
    return clamp((value - start) / (end - start) * 100.0)


def parse_ymd(value: str) -> datetime:
    return datetime.strptime(value, "%Y%m%d")


def sina_symbol(secucode: str) -> str:
    code, suffix = secucode.split(".")
    return ("sh" if suffix == "SH" else "sz") + code


def fetch_sina_bars(secucode: str, end: str, datalen: int, timeout: int = 18) -> list[DailyBar]:
    params = {
        "symbol": sina_symbol(secucode),
        "scale": "240",
        "ma": "no",
        "datalen": str(datalen),
    }
    request = Request(
        f"{SINA_KLINE_URL}?{urlencode(params)}",
        headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://finance.sina.com.cn/",
        },
    )
    with urlopen(request, timeout=timeout) as response:
        rows = json.loads(response.read().decode("utf-8"))

    bars: list[DailyBar] = []
    previous_close = 0.0
    end_dash = f"{end[:4]}-{end[4:6]}-{end[6:]}"
    for row in rows:
        trade_date = str(row.get("day") or "")
        if not trade_date or trade_date > end_dash:
            continue
        open_price = float(row.get("open") or 0)
        high = float(row.get("high") or 0)
        low = float(row.get("low") or 0)
        close = float(row.get("close") or 0)
        volume = float(row.get("volume") or 0)
        amount = volume * mean([open_price, high, low, close])
        pct_change = (close / previous_close - 1.0) * 100.0 if previous_close > 0 else 0.0
        bars.append(DailyBar(
            trade_date=trade_date,
            open=open_price,
            close=close,
            high=high,
            low=low,
            amount=amount,
            pct_change=pct_change,
            turnover=0.0,
        ))
        previous_close = close
    bars.sort(key=lambda item: item.trade_date)
    return bars


def corr(a: list[float], b: list[float]) -> float | None:
    if len(a) != len(b) or len(a) < 3:
        return None
    ma = mean(a)
    mb = mean(b)
    da = [x - ma for x in a]
    db = [x - mb for x in b]
    va = sum(x * x for x in da)
    vb = sum(x * x for x in db)
    if va <= 1e-12 or vb <= 1e-12:
        return None
    return sum(x * y for x, y in zip(da, db)) / math.sqrt(va * vb)


def avg_pairwise_corr(rows: list[StockMetrics]) -> float:
    values: list[float] = []
    for i, left in enumerate(rows):
        for right in rows[i + 1 :]:
            value = corr(left.returns20, right.returns20)
            if value is not None:
                values.append(value)
    return mean(values)


def calc_metrics(symbol: SymbolInfo, bars: list[DailyBar], lookback: int, latest_date: str) -> StockMetrics | None:
    bars = [bar for bar in bars if bar.trade_date <= latest_date]
    if len(bars) < lookback + 21 or bars[-1].trade_date != latest_date:
        return None

    closes = [bar.close for bar in bars]
    amounts = [bar.amount for bar in bars]
    recent = bars[-(lookback + 1) :]
    close = closes[-1]
    ret20 = close / closes[-lookback - 1] - 1.0
    ret5 = close / closes[-6] - 1.0
    amount5 = mean(amounts[-5:])
    amount_prev15 = mean(amounts[-20:-5])
    amount_ratio = amount5 / amount_prev15 if amount_prev15 > 0 else 0.0
    high20 = max(bar.high for bar in recent[1:])
    drawdown20 = close / high20 - 1.0 if high20 > 0 else 0.0
    ma20 = mean(closes[-20:])
    below_ma20 = close < ma20

    returns20: list[float] = []
    for prev, cur in zip(recent[:-1], recent[1:]):
        if prev.close > 0:
            returns20.append(cur.close / prev.close - 1.0)
    volatility20 = math.sqrt(mean([(item - mean(returns20)) ** 2 for item in returns20])) if returns20 else 0.0
    big_down_5d = any(item <= -0.05 for item in returns20[-5:])

    return StockMetrics(
        secucode=symbol.secucode,
        name=symbol.name,
        latest_date=latest_date,
        close=close,
        ret20=ret20,
        ret5=ret5,
        amount5=amount5,
        amount_prev15=amount_prev15,
        amount_ratio=amount_ratio,
        drawdown20=drawdown20,
        volatility20=volatility20,
        below_ma20=below_ma20,
        big_down_5d=big_down_5d,
        returns20=returns20,
    )


def fetch_one(
    symbol: SymbolInfo,
    beg: str,
    end: str,
    source: str,
    datalen: int,
) -> tuple[SymbolInfo, list[DailyBar] | None, str | None]:
    try:
        if source == "sina":
            return symbol, fetch_sina_bars(symbol.secucode, end, datalen=datalen, timeout=18), None
        if source == "tencent":
            return symbol, fetch_bars(symbol.secucode, beg, end, timeout=18), None
        try:
            bars = fetch_sina_bars(symbol.secucode, end, datalen=datalen, timeout=18)
            if bars:
                return symbol, bars, None
        except Exception:
            pass
        return symbol, fetch_bars(symbol.secucode, beg, end, timeout=18), None
    except Exception as exc:  # noqa: BLE001
        return symbol, None, str(exc)


def score_snapshot(
    args: argparse.Namespace,
    symbols: list[SymbolInfo],
    all_bars: dict[str, list[DailyBar]],
    latest_date: str,
    errors: list[dict[str, str]],
    include_basket: bool = True,
) -> dict[str, Any]:
    metrics: list[StockMetrics] = []
    symbol_by_code = {symbol.secucode: symbol for symbol in symbols}
    for secucode, bars in all_bars.items():
        item = calc_metrics(symbol_by_code[secucode], bars, args.lookback, latest_date)
        if item is None:
            continue
        metrics.append(item)

    liquid = [item for item in metrics if item.amount5 >= args.min_amount]
    basket = sorted(liquid, key=lambda item: item.ret20, reverse=True)[: args.top_n]
    if not basket:
        raise RuntimeError("no basket stocks after liquidity filter")

    universe_ret20 = median([item.ret20 for item in metrics])
    universe_ret5 = median([item.ret5 for item in metrics])
    basket_ret20 = mean([item.ret20 for item in basket])
    basket_ret5 = mean([item.ret5 for item in basket])
    basket_amount_ratio = mean([item.amount_ratio for item in basket])
    basket_corr = avg_pairwise_corr(basket)
    basket_drawdown = mean([item.drawdown20 for item in basket])
    basket_vol = mean([item.volatility20 for item in basket])
    below_ma20_ratio = mean([1.0 if item.below_ma20 else 0.0 for item in basket])
    big_down_ratio = mean([1.0 if item.big_down_5d else 0.0 for item in basket])
    amount_share = sum(item.amount5 for item in basket) / sum(item.amount5 for item in metrics if item.amount5 > 0)

    relative_20d_score = score_ratio(basket_ret20 - universe_ret20, 0.05, 0.35)
    volume_heat_score = score_ratio(basket_amount_ratio, 1.0, 2.5)
    corr_score = score_ratio(basket_corr, 0.10, 0.55)
    amount_share_score = score_ratio(amount_share, 0.08, 0.25)
    crowding_score = mean([relative_20d_score, volume_heat_score, corr_score, amount_share_score])

    drawdown_score = score_ratio(abs(min(basket_drawdown, 0.0)), 0.03, 0.16)
    volatility_score = score_ratio(basket_vol, 0.025, 0.07)
    ret5_cooldown_score = score_ratio((basket_ret20 / 4.0) - basket_ret5, 0.02, 0.16)
    fragility_score = mean([drawdown_score, volatility_score, ret5_cooldown_score])

    ma20_break_score = below_ma20_ratio * 100.0
    rel5_weak_score = score_ratio(universe_ret5 - basket_ret5, 0.00, 0.12)
    big_down_score = big_down_ratio * 100.0
    confirmation_score = mean([ma20_break_score, rel5_weak_score, big_down_score])

    total_score = 0.35 * crowding_score + 0.30 * fragility_score + 0.35 * confirmation_score
    if total_score >= 80:
        level = "瓦解中"
    elif total_score >= 65:
        level = "高危"
    elif total_score >= 50:
        level = "拥挤但趋势未坏"
    elif total_score >= 30:
        level = "升温"
    else:
        level = "正常"

    return {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "end": args.end,
        "latest_date": latest_date,
        "lookback": args.lookback,
        "top_n": args.top_n,
        "symbols_requested": len(symbols),
        "symbols_loaded": len(all_bars),
        "valid_metrics": len(metrics),
        "liquid_metrics": len(liquid),
        "errors": errors[:20],
        "error_count": len(errors),
        "score": {
            "total": total_score,
            "level": level,
            "crowding": crowding_score,
            "fragility": fragility_score,
            "confirmation": confirmation_score,
        },
        "raw": {
            "basket_ret20": basket_ret20,
            "universe_ret20_median": universe_ret20,
            "basket_ret5": basket_ret5,
            "universe_ret5_median": universe_ret5,
            "basket_amount_ratio": basket_amount_ratio,
            "basket_avg_corr": basket_corr,
            "basket_drawdown_from_20d_high": basket_drawdown,
            "basket_daily_vol20": basket_vol,
            "below_ma20_ratio": below_ma20_ratio,
            "big_down_5d_ratio": big_down_ratio,
            "amount_share": amount_share,
        },
        "component_scores": {
            "relative_20d": relative_20d_score,
            "volume_heat": volume_heat_score,
            "internal_correlation": corr_score,
            "amount_share": amount_share_score,
            "drawdown": drawdown_score,
            "volatility": volatility_score,
            "ret5_cooldown": ret5_cooldown_score,
            "ma20_break": ma20_break_score,
            "relative_5d_weakness": rel5_weak_score,
            "big_down_5d": big_down_score,
        },
        "basket": [asdict(item) for item in basket] if include_basket else [],
    }


def build_report(args: argparse.Namespace) -> dict[str, Any]:
    end_dt = parse_ymd(args.end)
    beg = (end_dt - timedelta(days=args.calendar_days)).strftime("%Y%m%d")
    symbols = fetch_universe()
    if args.max_symbols:
        symbols = symbols[: args.max_symbols]

    all_bars: dict[str, list[DailyBar]] = {}
    errors: list[dict[str, str]] = []
    datalen = max(args.lookback + args.series_days + 80, 120)
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(fetch_one, symbol, beg, args.end, args.source, datalen): symbol
            for symbol in symbols
        }
        for future in as_completed(futures):
            symbol, bars, error = future.result()
            if error or not bars:
                errors.append({"secucode": symbol.secucode, "name": symbol.name, "error": error or "empty"})
                continue
            all_bars[symbol.secucode] = bars

    latest_dates = [bars[-1].trade_date for bars in all_bars.values() if bars]
    if not latest_dates:
        raise RuntimeError("no kline data fetched")
    latest_date = max(latest_dates)
    payload = score_snapshot(args, symbols, all_bars, latest_date, errors, include_basket=True)

    if args.series_days > 1:
        date_counts: dict[str, int] = {}
        for bars in all_bars.values():
            for bar in bars:
                if bar.trade_date <= latest_date:
                    date_counts[bar.trade_date] = date_counts.get(bar.trade_date, 0) + 1
        liquid_floor = max(100, int(len(all_bars) * 0.4))
        series_dates = [
            day for day, count in sorted(date_counts.items())
            if count >= liquid_floor
        ][-args.series_days:]
        series: list[dict[str, Any]] = []
        for day in series_dates:
            snapshot = score_snapshot(args, symbols, all_bars, day, errors, include_basket=False)
            series.append({
                "date": day,
                "score": snapshot["score"],
                "raw": snapshot["raw"],
                "valid_metrics": snapshot["valid_metrics"],
                "liquid_metrics": snapshot["liquid_metrics"],
            })
        payload["series"] = series
        payload["series_days"] = len(series)
    return payload


def write_markdown(payload: dict[str, Any], path: Path) -> None:
    score = payload["score"]
    raw = payload["raw"]
    components = payload["component_scores"]
    lines = [
        "# 抱团瓦解预警指数 v1",
        "",
        f"- 生成时间：{payload['generated_at']}",
        f"- 最新交易日：{payload['latest_date']}",
        f"- 口径：近 {payload['lookback']} 个交易日，自动选取成交过滤后的涨幅 Top {payload['top_n']} 作为当前抱团篮子。",
        f"- 股票加载：请求 {payload['symbols_requested']} 只，成功 {payload['symbols_loaded']} 只，有效 {payload['valid_metrics']} 只，流动性过滤后 {payload['liquid_metrics']} 只，错误 {payload['error_count']} 只。",
        "",
        "## 总览",
        "",
        "| 指标 | 分数 |",
        "|---|---:|",
        f"| 总分 | {score['total']:.1f} |",
        f"| 状态 | {score['level']} |",
        f"| 拥挤度 | {score['crowding']:.1f} |",
        f"| 脆弱性 | {score['fragility']:.1f} |",
        f"| 瓦解确认度 | {score['confirmation']:.1f} |",
        "",
        "## 原始读数",
        "",
        "| 项目 | 数值 |",
        "|---|---:|",
        f"| 抱团篮子 20日收益 | {pct(raw['basket_ret20'])} |",
        f"| 全市场 20日中位收益 | {pct(raw['universe_ret20_median'])} |",
        f"| 抱团篮子 5日收益 | {pct(raw['basket_ret5'])} |",
        f"| 全市场 5日中位收益 | {pct(raw['universe_ret5_median'])} |",
        f"| 抱团篮子成交额 5日/前15日 | {raw['basket_amount_ratio']:.2f} |",
        f"| 篮子内部平均相关性 | {raw['basket_avg_corr']:.2f} |",
        f"| 距 20日高点平均回撤 | {pct(raw['basket_drawdown_from_20d_high'])} |",
        f"| 20日平均日波动 | {pct(raw['basket_daily_vol20'])} |",
        f"| 跌破 MA20 比例 | {raw['below_ma20_ratio']:.1%} |",
        f"| 最近 5日出现过 -5% 大跌比例 | {raw['big_down_5d_ratio']:.1%} |",
        f"| Top{payload['top_n']} 成交额占全样本 | {raw['amount_share']:.1%} |",
        "",
        "## 分项分数",
        "",
        "| 分项 | 分数 |",
        "|---|---:|",
    ]
    for key, value in components.items():
        lines.append(f"| {key} | {value:.1f} |")
    if payload.get("series"):
        lines.extend([
            "",
            f"## 最近 {payload.get('series_days', len(payload['series']))} 日每日分数",
            "",
            "| 日期 | 总分 | 状态 | 拥挤度 | 脆弱性 | 瓦解确认度 | Top50 20日 | Top50 5日 | 跌破MA20 |",
            "|---|---:|---|---:|---:|---:|---:|---:|---:|",
        ])
        for item in payload["series"]:
            item_score = item["score"]
            item_raw = item["raw"]
            lines.append(
                "| "
                f"{item['date']} | {item_score['total']:.1f} | {item_score['level']} | "
                f"{item_score['crowding']:.1f} | {item_score['fragility']:.1f} | "
                f"{item_score['confirmation']:.1f} | {pct(item_raw['basket_ret20'])} | "
                f"{pct(item_raw['basket_ret5'])} | {item_raw['below_ma20_ratio']:.1%} |"
            )
    lines.extend([
        "",
        "## 抱团篮子 Top 20",
        "",
        "| 排名 | 代码 | 名称 | 20日 | 5日 | 距20日高点 | 成交额5日/前15日 | MA20 |",
        "|---:|---|---|---:|---:|---:|---:|---|",
    ])
    for rank, item in enumerate(payload["basket"][:20], 1):
        lines.append(
            "| "
            f"{rank} | {item['secucode']} | {item['name']} | {pct(item['ret20'])} | "
            f"{pct(item['ret5'])} | {pct(item['drawdown20'])} | {item['amount_ratio']:.2f} | "
            f"{'下方' if item['below_ma20'] else '上方'} |"
        )
    lines.extend([
        "",
        "## 口径说明",
        "",
        "- v1 只使用行情、成交和横截面强弱，不含基金持仓、估值分位、融资余额、ETF 份额和盈利预测。",
        "- 自动抱团篮子代表“过去一个月最强且有成交的动量拥挤方向”，不等同于行业指数。",
        "- 分数用于风险温度计，不构成买卖建议。",
        "",
    ])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build A-share crowding breakdown warning index v1.")
    parser.add_argument("--end", default=datetime.now().strftime("%Y%m%d"))
    parser.add_argument("--lookback", type=int, default=20)
    parser.add_argument("--calendar-days", type=int, default=120)
    parser.add_argument("--top-n", type=int, default=50)
    parser.add_argument("--min-amount", type=float, default=100_000_000)
    parser.add_argument("--workers", type=int, default=20)
    parser.add_argument("--max-symbols", type=int, default=0)
    parser.add_argument("--source", choices=["sina", "tencent", "auto"], default="sina")
    parser.add_argument("--series-days", type=int, default=1)
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = build_report(args)
    stamp = f"{payload['latest_date'].replace('-', '')}_{datetime.now().strftime('%H%M%S')}"
    json_path = OUT_DIR / f"crowding_warning_v1_{stamp}.json"
    md_path = OUT_DIR / f"crowding_warning_v1_{stamp}.md"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(payload, md_path)
    print(json.dumps({
        "json": str(json_path),
        "markdown": str(md_path),
        "latest_date": payload["latest_date"],
        "score": payload["score"],
        "raw": payload["raw"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
