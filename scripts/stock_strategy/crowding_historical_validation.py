from __future__ import annotations

import argparse
import json
import math
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE_DIR = Path(__file__).resolve().parents[2]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from scripts.stock_strategy.backtest_10b_tencent import DailyBar, SymbolInfo
from scripts.stock_strategy.crowding_warning_v1 import (
    avg_pairwise_corr,
    calc_metrics,
    clamp,
    mean,
    pct,
    score_ratio,
)


OUT_DIR = BASE_DIR / "reports" / "crowding_warning"
SOHU_HQ_URL = "https://q.stock.sohu.com/hisHq"


@dataclass(frozen=True)
class CaseDefinition:
    key: str
    name: str
    start: str
    end: str
    break_date: str
    benchmark: str
    basket: list[str]
    note: str


@dataclass(frozen=True)
class V2Metrics:
    secucode: str
    close: float
    ret5: float
    ret20: float
    ret60: float
    ret120: float
    amount_ratio60: float
    distance_ma60: float
    drawdown60: float
    drawdown120: float
    below_ma20: bool
    below_ma60: bool
    volatility20: float
    returns20: list[float]


def stock(code: str) -> str:
    if "." in code:
        return code
    return f"{code}.SH" if code.startswith("6") else f"{code}.SZ"


CASES: list[CaseDefinition] = [
    CaseDefinition(
        key="bluechip_2007",
        name="2007 大盘蓝筹/金融周期抱团",
        start="20070702",
        end="20071231",
        break_date="20071016",
        benchmark="zs_000001",
        basket=[
            stock(code)
            for code in [
                "601398",
                "601988",
                "601628",
                "601318",
                "600030",
                "600036",
                "600016",
                "600000",
                "601166",
                "600028",
                "600019",
                "601600",
                "600050",
                "600900",
                "000002",
                "000001",
            ]
        ],
        note="以上证综指 2007-10-16 附近见顶作为瓦解起点。",
    ),
    CaseDefinition(
        key="growth_2015",
        name="2015 杠杆中小创/互联网+抱团",
        start="20150302",
        end="20150831",
        break_date="20150612",
        benchmark="zs_000001",
        basket=[
            stock(code)
            for code in [
                "300059",
                "300033",
                "300024",
                "300017",
                "300070",
                "300027",
                "300058",
                "300002",
                "300315",
                "300168",
                "002230",
                "002236",
                "002415",
                "300124",
                "300144",
            ]
        ],
        note="以创业板指 2015-06 上旬见顶、6 月中旬快速下跌作为瓦解起点。",
    ),
    CaseDefinition(
        key="whitehorse_2018",
        name="2018 白马/漂亮50抱团",
        start="20171009",
        end="20180430",
        break_date="20171123",
        benchmark="zs_000001",
        basket=[
            stock(code)
            for code in [
                "600519",
                "000858",
                "000651",
                "000333",
                "600887",
                "600276",
                "600309",
                "601318",
                "600036",
                "600030",
                "600016",
                "002415",
                "002304",
                "000568",
                "000661",
            ]
        ],
        note="以 2017-11 下旬白马股高位放量松动作为首次瓦解起点；2018-01 下旬是后续市场共振。",
    ),
    CaseDefinition(
        key="core_assets_2021",
        name="2021 核心资产/茅指数抱团",
        start="20201102",
        end="20210430",
        break_date="20210218",
        benchmark="zs_000001",
        basket=[
            stock(code)
            for code in [
                "600519",
                "000858",
                "300750",
                "601888",
                "300760",
                "600276",
                "000661",
                "603259",
                "000333",
                "000651",
                "000568",
                "002304",
                "600887",
                "300015",
                "002812",
            ]
        ],
        note="以春节后 2021-02-18 核心资产高位转跌作为瓦解起点。",
    ),
    CaseDefinition(
        key="track_2022",
        name="2021-2022 新能源/赛道抱团",
        start="20210601",
        end="20220430",
        break_date="20210917",
        benchmark="zs_000001",
        basket=[
            stock(code)
            for code in [
                "300750",
                "002594",
                "300274",
                "601012",
                "600438",
                "002129",
                "002460",
                "002466",
                "300014",
                "688599",
                "300450",
                "300751",
                "600905",
                "603806",
                "300037",
            ]
        ],
        note="以 2021-09 中旬赛道第一段高位趋势破坏作为首次瓦解起点；2021 年底至 2022 年是一轮更长的二次瓦解。",
    ),
    CaseDefinition(
        key="tmt_ai_2023",
        name="2023 TMT/AI 主题抱团",
        start="20230201",
        end="20230731",
        break_date="20230420",
        benchmark="zs_000001",
        basket=[
            stock(code)
            for code in [
                "002230",
                "300033",
                "300418",
                "300308",
                "300502",
                "300624",
                "300229",
                "300364",
                "002261",
                "002401",
                "603019",
                "603083",
                "688111",
                "688256",
                "688327",
            ]
        ],
        note="以 2023-04 下旬 AI/TMT 一阶段高位分歧作为瓦解起点。",
    ),
    CaseDefinition(
        key="microcap_2024",
        name="2024 微盘/小票量化抱团",
        start="20231101",
        end="20240315",
        break_date="20240129",
        benchmark="zs_000001",
        basket=[
            stock(code)
            for code in [
                "300489",
                "300313",
                "300209",
                "300023",
                "300278",
                "300517",
                "300799",
                "300312",
                "300356",
                "300392",
                "002621",
                "002642",
                "002808",
                "002915",
                "603023",
            ]
        ],
        note="微盘没有稳定免费长历史成分，使用小市值/小票风格代表篮子；结论置信度低于其他事件。",
    ),
]


def parse_ymd(value: str) -> datetime:
    return datetime.strptime(value, "%Y%m%d")


def ymd(value: datetime) -> str:
    return value.strftime("%Y%m%d")


def sohu_stock_code(secucode: str) -> str:
    code = secucode.split(".")[0]
    return f"cn_{code}"


def fetch_sohu_bars(sohu_code: str, start: str, end: str, timeout: int = 18) -> list[DailyBar]:
    params = {
        "code": sohu_code,
        "start": start,
        "end": end,
        "stat": "1",
        "order": "D",
        "period": "d",
        "rt": "json",
    }
    request = Request(
        f"{SOHU_HQ_URL}?{urlencode(params)}",
        headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://q.stock.sohu.com/",
            "Connection": "close",
        },
    )
    last_error: Exception | None = None
    for attempt in range(7):
        try:
            with urlopen(request, timeout=timeout) as response:
                text = response.read().decode("gbk", errors="ignore")
            break
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            time.sleep(0.5 * (attempt + 1))
    else:
        if last_error is not None:
            raise last_error
        return []
    rows = json.loads(text)
    if not rows or rows[0].get("status") != 0:
        return []

    bars: list[DailyBar] = []
    for row in rows[0].get("hq", []):
        trade_date = str(row[0])
        open_price = float(row[1])
        close = float(row[2])
        high = float(row[6])
        low = float(row[5])
        amount = float(row[8]) * 10000.0
        pct_change = float(str(row[4]).replace("%", "") or 0.0)
        turnover_text = str(row[9]).replace("%", "")
        turnover = float(turnover_text) if turnover_text and turnover_text != "-" else 0.0
        bars.append(
            DailyBar(
                trade_date=trade_date,
                open=open_price,
                close=close,
                high=high,
                low=low,
                amount=amount,
                pct_change=pct_change,
                turnover=turnover,
            )
        )
    bars.sort(key=lambda item: item.trade_date)
    return bars


def fetch_case_data(case: CaseDefinition, pre_days: int, workers: int) -> tuple[dict[str, list[DailyBar]], list[dict[str, str]]]:
    fetch_start = ymd(parse_ymd(case.start) - timedelta(days=pre_days))
    symbols = [(secucode, sohu_stock_code(secucode)) for secucode in case.basket]
    symbols.append(("BENCHMARK", case.benchmark))

    all_bars: dict[str, list[DailyBar]] = {}
    errors: list[dict[str, str]] = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(fetch_sohu_bars, sohu_code, fetch_start, case.end): (secucode, sohu_code)
            for secucode, sohu_code in symbols
        }
        for future in as_completed(futures):
            secucode, sohu_code = futures[future]
            try:
                bars = future.result()
            except Exception as exc:  # noqa: BLE001
                errors.append({"secucode": secucode, "source_code": sohu_code, "error": str(exc)})
                continue
            if not bars:
                errors.append({"secucode": secucode, "source_code": sohu_code, "error": "empty"})
                continue
            all_bars[secucode] = bars
    return all_bars, errors


def benchmark_returns(bars: list[DailyBar], date: str, lookback: int) -> tuple[float, float] | None:
    rows = [bar for bar in bars if bar.trade_date <= date]
    if len(rows) < lookback + 1 or rows[-1].trade_date != date:
        return None
    ret20 = rows[-1].close / rows[-lookback - 1].close - 1.0
    ret5 = rows[-1].close / rows[-6].close - 1.0 if len(rows) >= 6 else 0.0
    return ret20, ret5


def benchmark_return_map(bars: list[DailyBar], date: str, windows: list[int]) -> dict[int, float] | None:
    rows = [bar for bar in bars if bar.trade_date <= date]
    if not rows or rows[-1].trade_date != date:
        return None
    result: dict[int, float] = {}
    for window in windows:
        if len(rows) < window + 1:
            return None
        previous = rows[-window - 1].close
        result[window] = rows[-1].close / previous - 1.0 if previous > 0 else 0.0
    return result


def calc_v2_metrics(secucode: str, bars: list[DailyBar], date: str) -> V2Metrics | None:
    rows = [bar for bar in bars if bar.trade_date <= date]
    if len(rows) < 121 or rows[-1].trade_date != date:
        return None

    closes = [bar.close for bar in rows]
    amounts = [bar.amount for bar in rows]
    close = closes[-1]
    ret5 = close / closes[-6] - 1.0
    ret20 = close / closes[-21] - 1.0
    ret60 = close / closes[-61] - 1.0
    ret120 = close / closes[-121] - 1.0
    amount5 = mean(amounts[-5:])
    amount60 = mean(amounts[-65:-5])
    amount_ratio60 = amount5 / amount60 if amount60 > 0 else 0.0
    ma20 = mean(closes[-20:])
    ma60 = mean(closes[-60:])
    distance_ma60 = close / ma60 - 1.0 if ma60 > 0 else 0.0
    high60 = max(bar.high for bar in rows[-60:])
    high120 = max(bar.high for bar in rows[-120:])
    drawdown60 = close / high60 - 1.0 if high60 > 0 else 0.0
    drawdown120 = close / high120 - 1.0 if high120 > 0 else 0.0
    returns20 = [
        cur.close / prev.close - 1.0
        for prev, cur in zip(rows[-21:-1], rows[-20:])
        if prev.close > 0
    ]
    volatility20 = math.sqrt(mean([(item - mean(returns20)) ** 2 for item in returns20])) if returns20 else 0.0
    return V2Metrics(
        secucode=secucode,
        close=close,
        ret5=ret5,
        ret20=ret20,
        ret60=ret60,
        ret120=ret120,
        amount_ratio60=amount_ratio60,
        distance_ma60=distance_ma60,
        drawdown60=drawdown60,
        drawdown120=drawdown120,
        below_ma20=close < ma20,
        below_ma60=close < ma60,
        volatility20=volatility20,
        returns20=returns20,
    )


def near_high_score(drawdown: float, tolerance: float = 0.12) -> float:
    return clamp((tolerance - abs(min(drawdown, 0.0))) / tolerance * 100.0)


def level(score: float) -> str:
    if score >= 80:
        return "瓦解中"
    if score >= 65:
        return "高危"
    if score >= 50:
        return "警戒"
    if score >= 30:
        return "升温"
    return "正常"


def score_case_day(
    case: CaseDefinition,
    all_bars: dict[str, list[DailyBar]],
    date: str,
    lookback: int,
    min_valid: int,
) -> dict[str, Any] | None:
    symbols = [SymbolInfo(secucode=item, code=item.split(".")[0], name=item) for item in case.basket]
    metrics = []
    v2_metrics = []
    for symbol in symbols:
        bars = all_bars.get(symbol.secucode, [])
        item = calc_metrics(symbol, bars, lookback, date)
        if item is not None:
            metrics.append(item)
        v2_item = calc_v2_metrics(symbol.secucode, bars, date)
        if v2_item is not None:
            v2_metrics.append(v2_item)

    benchmark = benchmark_returns(all_bars.get("BENCHMARK", []), date, lookback)
    benchmark_long = benchmark_return_map(all_bars.get("BENCHMARK", []), date, [5, 20, 60, 120])
    if benchmark is None or benchmark_long is None or len(metrics) < min_valid or len(v2_metrics) < min_valid:
        return None

    benchmark_ret20, benchmark_ret5 = benchmark
    basket_ret20 = mean([item.ret20 for item in metrics])
    basket_ret5 = mean([item.ret5 for item in metrics])
    basket_amount_ratio = mean([item.amount_ratio for item in metrics])
    basket_corr = avg_pairwise_corr(metrics)
    basket_drawdown = mean([item.drawdown20 for item in metrics])
    basket_vol = mean([item.volatility20 for item in metrics])
    below_ma20_ratio = mean([1.0 if item.below_ma20 else 0.0 for item in metrics])
    big_down_ratio = mean([1.0 if item.big_down_5d else 0.0 for item in metrics])

    relative_20d_score = score_ratio(basket_ret20 - benchmark_ret20, 0.05, 0.35)
    volume_heat_score = score_ratio(basket_amount_ratio, 1.0, 2.5)
    corr_score = score_ratio(basket_corr, 0.10, 0.55)
    crowding_score = mean([relative_20d_score, volume_heat_score, corr_score])

    drawdown_score = score_ratio(abs(min(basket_drawdown, 0.0)), 0.03, 0.16)
    volatility_score = score_ratio(basket_vol, 0.025, 0.07)
    ret5_cooldown_score = score_ratio((basket_ret20 / 4.0) - basket_ret5, 0.02, 0.16)
    fragility_score = mean([drawdown_score, volatility_score, ret5_cooldown_score])

    ma20_break_score = below_ma20_ratio * 100.0
    rel5_weak_score = score_ratio(benchmark_ret5 - basket_ret5, 0.00, 0.12)
    big_down_score = big_down_ratio * 100.0
    confirmation_score = mean([ma20_break_score, rel5_weak_score, big_down_score])

    full_score = 0.35 * crowding_score + 0.30 * fragility_score + 0.35 * confirmation_score
    v1_pre_risk_score = 0.55 * crowding_score + 0.45 * fragility_score

    basket_ret60 = mean([item.ret60 for item in v2_metrics])
    basket_ret120 = mean([item.ret120 for item in v2_metrics])
    basket_amount_ratio60 = mean([item.amount_ratio60 for item in v2_metrics])
    basket_distance_ma60 = mean([item.distance_ma60 for item in v2_metrics])
    basket_drawdown60 = mean([item.drawdown60 for item in v2_metrics])
    basket_drawdown120 = mean([item.drawdown120 for item in v2_metrics])
    basket_vol20_v2 = mean([item.volatility20 for item in v2_metrics])
    below_ma20_ratio_v2 = mean([1.0 if item.below_ma20 else 0.0 for item in v2_metrics])
    below_ma60_ratio_v2 = mean([1.0 if item.below_ma60 else 0.0 for item in v2_metrics])
    basket_corr_v2 = avg_pairwise_corr(v2_metrics)  # type: ignore[arg-type]

    rel60 = basket_ret60 - benchmark_long[60]
    rel120 = basket_ret120 - benchmark_long[120]
    relative_60_score = score_ratio(rel60, 0.08, 0.30)
    relative_120_score = score_ratio(rel120, 0.12, 0.60)
    absolute_60_score = score_ratio(basket_ret60, 0.18, 0.60)
    absolute_120_score = score_ratio(basket_ret120, 0.30, 1.20)
    long_performance_score = mean([
        max(relative_60_score, absolute_60_score),
        max(relative_120_score, absolute_120_score),
    ])
    extension_ma60_score = score_ratio(basket_distance_ma60, 0.08, 0.30)
    near_high60_score = near_high_score(basket_drawdown60, tolerance=0.12)
    trend_pressure_score = mean([long_performance_score, extension_ma60_score, near_high60_score])

    volume_60_score = score_ratio(basket_amount_ratio60, 1.05, 2.20)
    corr_score_v2 = score_ratio(basket_corr_v2, 0.15, 0.55)
    volatility_score_v2 = score_ratio(basket_vol20_v2, 0.022, 0.060)
    heat_score_v2 = max(volume_60_score, mean([volume_60_score, corr_score_v2, volatility_score_v2]))

    ret20_decay_score = score_ratio((basket_ret60 / 3.0) - basket_ret20, 0.00, 0.16)
    ret5_decay_score = score_ratio((basket_ret20 / 4.0) - basket_ret5, 0.00, 0.12)
    breadth_decay_score = score_ratio(below_ma20_ratio_v2, 0.10, 0.45)
    ma60_break_score = score_ratio(below_ma60_ratio_v2, 0.05, 0.30)
    early_decay_score = mean([ret20_decay_score, ret5_decay_score, breadth_decay_score, ma60_break_score])

    blended_watch_score = (
        0.55 * trend_pressure_score
        + 0.20 * heat_score_v2
        + 0.25 * early_decay_score
    )
    extreme_trend_score = 0.70 * trend_pressure_score + 0.30 * heat_score_v2
    watch_score = max(
        blended_watch_score,
        extreme_trend_score
        if trend_pressure_score >= 75.0 or (trend_pressure_score >= 60.0 and heat_score_v2 >= 50.0)
        else blended_watch_score,
    )

    rel60 = basket_ret60 - benchmark_long[60]
    rel120 = basket_ret120 - benchmark_long[120]
    rollover_raw_score = 0.60 * early_decay_score + 0.30 * long_performance_score + 0.10 * heat_score_v2
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
        and heat_score_v2 >= 60.0
        and rel120 >= 0.50
    ) else 0.0
    mega_blowoff_score = watch_score if (
        watch_score >= 60.0
        and heat_score_v2 >= 55.0
        and long_performance_score >= 75.0
        and early_decay_score <= 30.0
        and (rel120 >= 0.70 or rel60 >= 0.90 or basket_ret120 >= 1.35)
    ) else 0.0
    broad_bubble_score = watch_score if (
        watch_score >= 60.0
        and long_performance_score >= 80.0
        and basket_ret120 >= 0.85
        and benchmark_long[120] >= 0.50
        and rel120 <= 0.25
    ) else 0.0
    low_vol_quality_score = watch_score if (
        watch_score >= 60.0
        and trend_pressure_score >= 60.0
        and heat_score_v2 >= 70.0
        and rel120 >= 0.30
        and basket_ret120 <= 0.65
        and volatility_score_v2 <= 15.0
    ) else 0.0
    countdown_score = max(
        rollover_countdown_score,
        core_blowoff_score,
        mega_blowoff_score,
        broad_bubble_score,
        low_vol_quality_score,
    )

    return {
        "date": date,
        "valid_count": len(metrics),
        "v2_valid_count": len(v2_metrics),
        "pre_risk_score": countdown_score,
        "v1_pre_risk_score": v1_pre_risk_score,
        "full_score": full_score,
        "full_level": level(full_score),
        "crowding": crowding_score,
        "fragility": fragility_score,
        "confirmation": confirmation_score,
        "v2": {
            "pre_risk_score": countdown_score,
            "watch_score": watch_score,
            "blended_watch": blended_watch_score,
            "extreme_trend": extreme_trend_score,
            "trend_pressure": trend_pressure_score,
            "heat": heat_score_v2,
            "early_decay": early_decay_score,
            "rollover_raw": rollover_raw_score,
            "ma60_rollover_bonus": ma60_rollover_bonus,
            "rollover_countdown": rollover_countdown_score,
            "core_blowoff": core_blowoff_score,
            "mega_blowoff": mega_blowoff_score,
            "broad_bubble": broad_bubble_score,
            "low_vol_quality": low_vol_quality_score,
        },
        "raw": {
            "basket_ret20": basket_ret20,
            "benchmark_ret20": benchmark_ret20,
            "basket_ret5": basket_ret5,
            "benchmark_ret5": benchmark_ret5,
            "basket_ret60": basket_ret60,
            "benchmark_ret60": benchmark_long[60],
            "basket_ret120": basket_ret120,
            "benchmark_ret120": benchmark_long[120],
            "basket_amount_ratio": basket_amount_ratio,
            "basket_amount_ratio60": basket_amount_ratio60,
            "basket_avg_corr": basket_corr,
            "basket_avg_corr_v2": basket_corr_v2,
            "basket_distance_ma60": basket_distance_ma60,
            "basket_drawdown_from_20d_high": basket_drawdown,
            "basket_drawdown_from_60d_high": basket_drawdown60,
            "basket_drawdown_from_120d_high": basket_drawdown120,
            "basket_daily_vol20": basket_vol,
            "basket_daily_vol20_v2": basket_vol20_v2,
            "below_ma20_ratio": below_ma20_ratio,
            "below_ma20_ratio_v2": below_ma20_ratio_v2,
            "below_ma60_ratio_v2": below_ma60_ratio_v2,
            "big_down_5d_ratio": big_down_ratio,
        },
        "component_scores": {
            "relative_20d": relative_20d_score,
            "volume_heat": volume_heat_score,
            "internal_correlation": corr_score,
            "drawdown": drawdown_score,
            "volatility": volatility_score,
            "ret5_cooldown": ret5_cooldown_score,
            "ma20_break": ma20_break_score,
            "relative_5d_weakness": rel5_weak_score,
            "big_down_5d": big_down_score,
            "v2_relative_60d": relative_60_score,
            "v2_relative_120d": relative_120_score,
            "v2_absolute_60d": absolute_60_score,
            "v2_absolute_120d": absolute_120_score,
            "v2_long_performance": long_performance_score,
            "v2_extension_ma60": extension_ma60_score,
            "v2_near_high60": near_high60_score,
            "v2_volume_60d": volume_60_score,
            "v2_internal_correlation": corr_score_v2,
            "v2_volatility": volatility_score_v2,
            "v2_ret20_decay": ret20_decay_score,
            "v2_ret5_decay": ret5_decay_score,
            "v2_breadth_decay": breadth_decay_score,
            "v2_ma60_break": ma60_break_score,
        },
    }


def trading_day_distance(series: list[dict[str, Any]], start_date: str, end_date: str) -> int | None:
    dates = [item["date"] for item in series]
    if start_date not in dates or end_date not in dates:
        return None
    return dates.index(end_date) - dates.index(start_date)


def first_cross(
    series: list[dict[str, Any]],
    field: str,
    threshold: float,
    before_date: str | None = None,
) -> dict[str, Any] | None:
    for item in series:
        if before_date is not None and item["date"] >= before_date:
            break
        if item[field] >= threshold:
            return item
    return None


def max_before(series: list[dict[str, Any]], field: str, before_date: str) -> dict[str, Any] | None:
    rows = [item for item in series if item["date"] < before_date]
    if not rows:
        return None
    return max(rows, key=lambda item: item[field])


def max_after(series: list[dict[str, Any]], field: str, after_date: str) -> dict[str, Any] | None:
    rows = [item for item in series if item["date"] >= after_date]
    if not rows:
        return None
    return max(rows, key=lambda item: item[field])


def run_case(case: CaseDefinition, args: argparse.Namespace) -> dict[str, Any]:
    all_bars, errors = fetch_case_data(case, args.pre_days, args.workers)
    dates = sorted({
        bar.trade_date
        for bars in all_bars.values()
        for bar in bars
        if case.start <= bar.trade_date.replace("-", "") <= case.end
    })
    normalized_start = f"{case.start[:4]}-{case.start[4:6]}-{case.start[6:]}"
    normalized_end = f"{case.end[:4]}-{case.end[4:6]}-{case.end[6:]}"
    normalized_break = f"{case.break_date[:4]}-{case.break_date[4:6]}-{case.break_date[6:]}"
    dates = [date for date in dates if normalized_start <= date <= normalized_end]

    series: list[dict[str, Any]] = []
    for date in dates:
        item = score_case_day(case, all_bars, date, args.lookback, args.min_valid)
        if item is not None:
            series.append(item)

    pre_max = max_before(series, "pre_risk_score", normalized_break)
    first_pre60 = first_cross(series, "pre_risk_score", args.pre_threshold, before_date=normalized_break)
    first_pre70 = first_cross(series, "pre_risk_score", args.high_pre_threshold, before_date=normalized_break)
    first_full65 = first_cross(series, "full_score", args.full_threshold)
    post_full_max = max_after(series, "full_score", normalized_break)
    break_item = next((item for item in series if item["date"] >= normalized_break), None)

    def lead(item: dict[str, Any] | None) -> int | None:
        if item is None:
            return None
        distance = trading_day_distance(series, item["date"], break_item["date"] if break_item else normalized_break)
        return distance

    return {
        "case": asdict(case),
        "break_date_normalized": normalized_break,
        "errors": errors,
        "error_count": len(errors),
        "series": series,
        "summary": {
            "days_scored": len(series),
            "pre_max": pre_max,
            "first_pre_threshold": first_pre60,
            "first_high_pre_threshold": first_pre70,
            "first_full_threshold": first_full65,
            "post_full_max": post_full_max,
            "break_day_or_next": break_item,
            "lead_days_pre_threshold": lead(first_pre60),
            "lead_days_high_pre_threshold": lead(first_pre70),
        },
    }


def verdict(summary: dict[str, Any], pre_threshold: float, high_pre_threshold: float) -> str:
    if summary.get("first_high_pre_threshold"):
        lead_days = summary.get("lead_days_high_pre_threshold")
        if lead_days is not None and lead_days >= 5:
            return "提前高危"
        return "临近高危"
    if summary.get("first_pre_threshold"):
        lead_days = summary.get("lead_days_pre_threshold")
        if lead_days is not None and lead_days >= 5:
            return "提前预警"
        return "临近预警"
    pre_max = summary.get("pre_max") or {}
    if pre_max.get("pre_risk_score", 0.0) >= pre_threshold - 5:
        return "边缘预警"
    return "未预警"


def build_report(results: list[dict[str, Any]], args: argparse.Namespace) -> dict[str, Any]:
    return {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "data_source": "Sohu hisHq daily kline",
        "method": {
            "lookback": args.lookback,
            "pre_threshold": args.pre_threshold,
            "high_pre_threshold": args.high_pre_threshold,
            "full_threshold": args.full_threshold,
            "pre_risk_score": "30d countdown: max(rollover, core_blowoff, mega_blowoff, broad_bubble, low_vol_quality)",
            "watch_score": "v2 watch: max(blended_watch, extreme_trend)",
            "v1_pre_risk_score": "v1: 0.55*crowding + 0.45*fragility",
            "full_score": "0.35*crowding + 0.30*fragility + 0.35*confirmation",
        },
        "results": results,
    }


def fmt_score(item: dict[str, Any] | None, field: str) -> str:
    if not item:
        return "-"
    return f"{item[field]:.1f}"


def fmt_date(item: dict[str, Any] | None) -> str:
    if not item:
        return "-"
    return str(item["date"])


def fmt_lead(value: int | None) -> str:
    if value is None:
        return "-"
    return f"{value}日"


def write_markdown(payload: dict[str, Any], path: Path) -> None:
    method = payload["method"]
    lines = [
        "# 抱团瓦解预警指数历史复盘",
        "",
        f"- 生成时间：{payload['generated_at']}",
        f"- 数据源：{payload['data_source']}",
        f"- 口径：代表篮子逐日复盘，lookback={method['lookback']}。",
        f"- 30日预警分：{method['pre_risk_score']}，预警线 {method['pre_threshold']}，高危线 {method['high_pre_threshold']}。",
        f"- 过热观察分：{method['watch_score']}。",
        f"- v1 对照分：{method['v1_pre_risk_score']}。",
        f"- 全量瓦解确认分：{method['full_score']}，确认线 {method['full_threshold']}。",
        "",
        "## 命中情况",
        "",
        "| 历史场景 | 瓦解起点 | 结论 | 30日预警最高 | 最高日 | 首次预警 | 提前 | 首次高危 | 提前 | 起点确认分 | 后段最高确认分 |",
        "|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for result in payload["results"]:
        case = result["case"]
        summary = result["summary"]
        first_pre = summary.get("first_pre_threshold")
        first_high = summary.get("first_high_pre_threshold")
        pre_max = summary.get("pre_max")
        break_day = summary.get("break_day_or_next")
        post_max = summary.get("post_full_max")
        lines.append(
            "| "
            f"{case['name']} | {result['break_date_normalized']} | "
            f"{verdict(summary, method['pre_threshold'], method['high_pre_threshold'])} | "
            f"{fmt_score(pre_max, 'pre_risk_score')} | {fmt_date(pre_max)} | "
            f"{fmt_date(first_pre)} | {fmt_lead(summary.get('lead_days_pre_threshold'))} | "
            f"{fmt_date(first_high)} | {fmt_lead(summary.get('lead_days_high_pre_threshold'))} | "
            f"{fmt_score(break_day, 'full_score')} | {fmt_score(post_max, 'full_score')} |"
        )

    lines.extend([
        "",
        "## 分场景读数",
        "",
    ])
    for result in payload["results"]:
        case = result["case"]
        summary = result["summary"]
        pre_max = summary.get("pre_max")
        first_pre = summary.get("first_pre_threshold")
        break_day = summary.get("break_day_or_next")
        post_max = summary.get("post_full_max")
        lines.extend([
            f"### {case['name']}",
            "",
            f"- 说明：{case['note']}",
            f"- 成分有效天数：{summary['days_scored']}；数据错误：{result['error_count']}。",
            f"- 30日预警最高：{fmt_date(pre_max)}，预警分 {fmt_score(pre_max, 'pre_risk_score')}。",
            f"- 首次预警：{fmt_date(first_pre)}，提前 {fmt_lead(summary.get('lead_days_pre_threshold'))}。",
            f"- 瓦解起点/下一可算日：{fmt_date(break_day)}，确认分 {fmt_score(break_day, 'full_score')}。",
            f"- 瓦解后最高确认分：{fmt_date(post_max)}，{fmt_score(post_max, 'full_score')}。",
            "",
            "| 日期 | 30日预警分 | 过热观察分 | v1对照 | 确认分 | 趋势压力 | 热度 | 衰减 | 主要触发 | 60日相对 | 120日相对 | 距MA60 |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|",
        ])
        key_dates = {
            item["date"]
            for item in [pre_max, first_pre, break_day, post_max]
            if item is not None
        }
        rows = [item for item in result["series"] if item["date"] in key_dates]
        rows.sort(key=lambda item: item["date"])
        for item in rows:
            raw = item["raw"]
            v2 = item["v2"]
            triggers = {
                "回落": v2["rollover_countdown"],
                "核心冲顶": v2["core_blowoff"],
                "末端冲顶": v2["mega_blowoff"],
                "全市场泡沫": v2["broad_bubble"],
                "低波白马": v2["low_vol_quality"],
            }
            trigger_name, trigger_value = max(triggers.items(), key=lambda pair: pair[1])
            trigger_text = "-" if trigger_value <= 0 else trigger_name
            lines.append(
                "| "
                f"{item['date']} | {item['pre_risk_score']:.1f} | {v2['watch_score']:.1f} | "
                f"{item['v1_pre_risk_score']:.1f} | {item['full_score']:.1f} | "
                f"{v2['trend_pressure']:.1f} | {v2['heat']:.1f} | {v2['early_decay']:.1f} | "
                f"{trigger_text} | {pct(raw['basket_ret60'] - raw['benchmark_ret60'])} | "
                f"{pct(raw['basket_ret120'] - raw['benchmark_ret120'])} | "
                f"{pct(raw['basket_distance_ma60'])} |"
            )
        lines.append("")

    lines.extend([
        "## 限制",
        "",
        "- 这是代表篮子复盘，不是全市场自动 Top50 的完整历史重算；因此没有纳入全市场成交额占比项，横截面中位数用上证综指近似。",
        "- 30日预警分的目标是把正式预警压到约 30 个交易日内；更早的过热只进入观察分，不算正式预警。",
        "- 最终仍需要用真实全市场横截面、行业/主题篮子和持仓数据做二次校准。",
        "- 早期样本存在幸存者偏差，退市股、改名股、当年真实基金持仓无法完整复原。",
        "- 微盘/量化场景没有稳定免费长历史成分，使用小票风格代表篮子，置信度低于其他场景。",
        "- 该指数是风险温度计，不构成买卖建议。",
        "",
    ])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Replay crowding-warning scores on historical A-share crowding cases.")
    parser.add_argument("--lookback", type=int, default=20)
    parser.add_argument("--pre-days", type=int, default=180)
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--min-valid", type=int, default=8)
    parser.add_argument("--pre-threshold", type=float, default=60.0)
    parser.add_argument("--high-pre-threshold", type=float, default=70.0)
    parser.add_argument("--full-threshold", type=float, default=65.0)
    parser.add_argument("--cases", nargs="*", default=[])
    args = parser.parse_args()

    selected = CASES
    if args.cases:
        wanted = set(args.cases)
        selected = [case for case in CASES if case.key in wanted]
        missing = wanted.difference({case.key for case in selected})
        if missing:
            raise SystemExit(f"unknown cases: {', '.join(sorted(missing))}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    results = [run_case(case, args) for case in selected]
    payload = build_report(results, args)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = OUT_DIR / f"crowding_historical_validation_{stamp}.json"
    md_path = OUT_DIR / f"crowding_historical_validation_{stamp}.md"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(payload, md_path)
    print(json.dumps({
        "json": str(json_path),
        "markdown": str(md_path),
        "cases": [
            {
                "name": result["case"]["name"],
                "break_date": result["break_date_normalized"],
                "verdict": verdict(result["summary"], args.pre_threshold, args.high_pre_threshold),
                "pre_max": None if result["summary"]["pre_max"] is None else {
                    "date": result["summary"]["pre_max"]["date"],
                    "score": round(result["summary"]["pre_max"]["pre_risk_score"], 1),
                },
                "first_pre": None if result["summary"]["first_pre_threshold"] is None else {
                    "date": result["summary"]["first_pre_threshold"]["date"],
                    "lead_days": result["summary"]["lead_days_pre_threshold"],
                    "score": round(result["summary"]["first_pre_threshold"]["pre_risk_score"], 1),
                },
                "break_full_score": None if result["summary"]["break_day_or_next"] is None else round(result["summary"]["break_day_or_next"]["full_score"], 1),
                "post_full_max": None if result["summary"]["post_full_max"] is None else {
                    "date": result["summary"]["post_full_max"]["date"],
                    "score": round(result["summary"]["post_full_max"]["full_score"], 1),
                },
                "errors": result["error_count"],
            }
            for result in results
        ],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
