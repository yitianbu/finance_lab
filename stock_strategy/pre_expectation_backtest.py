from __future__ import annotations

import argparse
import json
import statistics
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from announcement_backtest import (
    CandidateTrade,
    KLine,
    StrategyConfig,
    add_benchmark_metrics,
    fetch_predict_events,
    next_trade_index,
    pct,
    run_portfolio,
    score_predict_event,
    select_trades,
    simulate_trade_from_price,
    write_csv,
)


DEFAULT_BASE_DIR = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class PreExpectationConfig:
    min_event_score: int = 96
    pre_entry_days: int = 5
    post_notice_hold_days: int = 1
    proxy_hold_days: int = 5
    stop_loss: float = 0.05
    take_profit: float = 0.12
    min_pre_5d_return: float = 0.02
    min_pre_10d_excess: float = 0.01
    max_pre_20d_return: float = 0.25
    min_history_days: int = 20
    max_open_gap: float = 0.05
    max_forecast_jz: float | None = 100_000_000
    exclude_notice_months: tuple[str, ...] = ("01", "07")
    proxy_months: tuple[str, ...] = ("03", "04", "08", "10")
    exclude_name_prefixes: tuple[str, ...] = ("*ST", "ST")
    exclude_name_contains: tuple[str, ...] = ("退",)
    position_size: float = 0.10
    max_per_day: int = 5


def close_by_date(klines: list[KLine]) -> dict[str, float]:
    return {bar.trade_date: bar.close for bar in klines}


def is_excluded_stock_name(stock_name: str, config: PreExpectationConfig) -> bool:
    name = stock_name.strip().upper()
    return any(name.startswith(prefix.upper()) for prefix in config.exclude_name_prefixes) or any(
        marker in stock_name for marker in config.exclude_name_contains
    )


def _return_over(klines: list[KLine], end_idx: int, lookback: int) -> float:
    if end_idx < lookback:
        return 0.0
    base = klines[end_idx - lookback].close
    if base <= 0:
        return 0.0
    return klines[end_idx].close / base - 1


def _benchmark_return(benchmark_by_date: dict[str, float], start_date: str, end_date: str) -> float | None:
    start = benchmark_by_date.get(start_date)
    end = benchmark_by_date.get(end_date)
    if start is None or end is None or start <= 0:
        return None
    return end / start - 1


def price_strength_signal(
    klines: list[KLine],
    signal_idx: int,
    benchmark_by_date: dict[str, float],
    config: PreExpectationConfig,
) -> bool:
    if signal_idx < config.min_history_days:
        return False
    if signal_idx >= len(klines):
        return False

    ret5 = _return_over(klines, signal_idx, 5)
    ret10 = _return_over(klines, signal_idx, 10)
    ret20 = _return_over(klines, signal_idx, 20)
    bench10 = _benchmark_return(
        benchmark_by_date,
        klines[max(0, signal_idx - 10)].trade_date,
        klines[signal_idx].trade_date,
    )
    if bench10 is None:
        return False

    ma_start = max(0, signal_idx - 9)
    ma10 = statistics.mean(bar.close for bar in klines[ma_start : signal_idx + 1])
    close = klines[signal_idx].close
    return (
        ret5 >= config.min_pre_5d_return
        and ret10 - bench10 >= config.min_pre_10d_excess
        and ret20 <= config.max_pre_20d_return
        and close >= ma10
    )


def simulate_until_forced_exit(
    klines: list[KLine],
    entry_idx: int,
    entry_price: float,
    forced_exit_idx: int,
    config: PreExpectationConfig,
):
    first_exit_idx = min(len(klines) - 1, entry_idx + 1)
    last_idx = min(len(klines) - 1, max(first_exit_idx, forced_exit_idx))
    hold_days = last_idx - entry_idx + 1
    return simulate_trade_from_price(
        klines,
        entry_idx,
        entry_price,
        hold_days=hold_days,
        stop_loss=config.stop_loss,
        take_profit=config.take_profit,
        stop_mode="intraday",
        first_exit_index=first_exit_idx,
    )


def _event_passes_pre_filters(event: dict[str, Any], score: int, config: PreExpectationConfig) -> bool:
    if score < config.min_event_score:
        return False
    if is_excluded_stock_name(str(event.get("SECURITY_NAME_ABBR") or ""), config):
        return False
    notice_date = str(event.get("NOTICE_DATE") or "")[:10]
    if notice_date[5:7] in config.exclude_notice_months:
        return False
    forecast = event.get("FORECAST_JZ")
    if config.max_forecast_jz is not None and (forecast is None or float(forecast) > config.max_forecast_jz):
        return False
    return True


def build_pre_event_candidate(
    event: dict[str, Any],
    klines: list[KLine],
    benchmark_by_date: dict[str, float],
    config: PreExpectationConfig,
) -> CandidateTrade | None:
    score, grade, reasons = score_predict_event(event)
    if grade == "C" or not _event_passes_pre_filters(event, score, config):
        return None

    notice_date = str(event.get("NOTICE_DATE") or "")[:10]
    reaction_idx = next_trade_index(klines, notice_date)
    if reaction_idx is None:
        return None
    entry_idx = reaction_idx - config.pre_entry_days
    signal_idx = entry_idx - 1
    if entry_idx <= 0 or signal_idx < 0:
        return None

    if not price_strength_signal(klines, signal_idx, benchmark_by_date, config):
        return None

    entry_bar = klines[entry_idx]
    prev_bar = klines[entry_idx - 1]
    if prev_bar.close <= 0:
        return None
    if entry_bar.open / prev_bar.close - 1 > config.max_open_gap:
        return None

    forced_exit_idx = min(len(klines) - 1, reaction_idx + config.post_notice_hold_days - 1)
    result = simulate_until_forced_exit(klines, entry_idx, entry_bar.open, forced_exit_idx, config)
    return CandidateTrade(
        secucode=event["SECUCODE"],
        stock_code=event["SECURITY_CODE"],
        stock_name=event["SECURITY_NAME_ABBR"],
        notice_date=notice_date,
        report_date=str(event.get("REPORT_DATE") or "")[:10],
        entry_date=entry_bar.trade_date,
        exit_date=result.exit_date,
        entry_price=entry_bar.open,
        exit_price=result.exit_price,
        gross_return=result.gross_return,
        net_return=result.net_return,
        exit_reason=result.exit_reason,
        score=score,
        grade=grade,
        predict_type=str(event.get("PREDICT_TYPE") or ""),
        increase_jz=float(event["INCREASE_JZ"]) if event.get("INCREASE_JZ") not in (None, "") else None,
        forecast_jz=float(event["FORECAST_JZ"]) if event.get("FORECAST_JZ") not in (None, "") else None,
        reasons=";".join(reasons) + ";event_labeled_not_directly_tradable",
    )


def load_cached_klines(kline_dir: Path) -> dict[str, list[KLine]]:
    output: dict[str, list[KLine]] = {}
    for path in sorted(kline_dir.glob("*.json")):
        rows = json.loads(path.read_text("utf-8"))
        output[path.stem] = [KLine(**row) for row in rows]
    return output


def build_pre_event_candidates(
    events: list[dict[str, Any]],
    klines_by_code: dict[str, list[KLine]],
    benchmark_by_date: dict[str, float],
    config: PreExpectationConfig,
    start_date: str,
    end_date: str | None,
) -> list[CandidateTrade]:
    candidates: list[CandidateTrade] = []
    for event in events:
        notice_date = str(event.get("NOTICE_DATE") or "")[:10]
        if notice_date < start_date:
            continue
        if end_date is not None and notice_date > end_date:
            continue
        klines = klines_by_code.get(str(event.get("SECUCODE") or "")) or []
        candidate = build_pre_event_candidate(event, klines, benchmark_by_date, config)
        if candidate:
            candidates.append(candidate)
    return candidates


def _proxy_score(klines: list[KLine], signal_idx: int, benchmark_by_date: dict[str, float]) -> tuple[int, str, float, float]:
    ret5 = _return_over(klines, signal_idx, 5)
    ret10 = _return_over(klines, signal_idx, 10)
    bench10 = _benchmark_return(
        benchmark_by_date,
        klines[max(0, signal_idx - 10)].trade_date,
        klines[signal_idx].trade_date,
    ) or 0.0
    excess10 = ret10 - bench10
    score = int(max(60, min(99, 70 + ret5 * 120 + excess10 * 160)))
    reason = f"pre5={ret5:.2%};excess10={excess10:.2%};calendar_proxy_no_future_event_label"
    return score, reason, ret5, excess10


def build_calendar_proxy_candidates(
    klines_by_code: dict[str, list[KLine]],
    benchmark_by_date: dict[str, float],
    names_by_code: dict[str, str],
    config: PreExpectationConfig,
    start_date: str,
    end_date: str | None,
) -> list[CandidateTrade]:
    candidates: list[CandidateTrade] = []
    for secucode, klines in klines_by_code.items():
        if secucode == "000300.SH" or len(klines) < config.min_history_days + config.proxy_hold_days + 2:
            continue
        stock_name = names_by_code.get(secucode, secucode)
        if is_excluded_stock_name(stock_name, config):
            continue
        for signal_idx in range(config.min_history_days, len(klines) - 1):
            signal_date = klines[signal_idx].trade_date
            if signal_date < start_date:
                continue
            if end_date is not None and signal_date > end_date:
                continue
            if signal_date[5:7] not in config.proxy_months:
                continue
            if not price_strength_signal(klines, signal_idx, benchmark_by_date, config):
                continue
            entry_idx = signal_idx + 1
            entry_bar = klines[entry_idx]
            prev_bar = klines[entry_idx - 1]
            if prev_bar.close <= 0 or entry_bar.open / prev_bar.close - 1 > config.max_open_gap:
                continue
            forced_exit_idx = min(len(klines) - 1, entry_idx + config.proxy_hold_days - 1)
            result = simulate_until_forced_exit(klines, entry_idx, entry_bar.open, forced_exit_idx, config)
            score, reason, ret5, _excess10 = _proxy_score(klines, signal_idx, benchmark_by_date)
            stock_code = secucode.split(".")[0]
            candidates.append(CandidateTrade(
                secucode=secucode,
                stock_code=stock_code,
                stock_name=stock_name,
                notice_date=signal_date,
                report_date="",
                entry_date=entry_bar.trade_date,
                exit_date=result.exit_date,
                entry_price=entry_bar.open,
                exit_price=result.exit_price,
                gross_return=result.gross_return,
                net_return=result.net_return,
                exit_reason=result.exit_reason,
                score=score,
                grade="P",
                predict_type="calendar_proxy",
                increase_jz=ret5 * 100,
                forecast_jz=None,
                reasons=reason,
            ))
    return candidates


def _names_by_code(events: list[dict[str, Any]]) -> dict[str, str]:
    return {
        str(event.get("SECUCODE")): str(event.get("SECURITY_NAME_ABBR") or event.get("SECUCODE"))
        for event in events
        if event.get("SECUCODE")
    }


def _strategy_config(config: PreExpectationConfig) -> StrategyConfig:
    return StrategyConfig(
        min_score=0,
        hold_days=config.proxy_hold_days,
        stop_loss=config.stop_loss,
        take_profit=config.take_profit,
        position_size=config.position_size,
        max_per_day=config.max_per_day,
        sort_mode="surprise",
    )


def portfolio_executed_trades(trades: list[CandidateTrade], position_size: float) -> list[CandidateTrade]:
    events: dict[str, dict[str, list[CandidateTrade]]] = defaultdict(lambda: {"entry": [], "exit": []})
    for trade in trades:
        events[trade.entry_date]["entry"].append(trade)
        events[trade.exit_date]["exit"].append(trade)

    cash = 1.0
    active: list[tuple[CandidateTrade, float]] = []
    executed: list[CandidateTrade] = []
    for day in sorted(events):
        def close_due_trades() -> None:
            nonlocal cash
            for trade in events[day]["exit"]:
                for idx, (active_trade, stake) in enumerate(active):
                    if active_trade is trade:
                        cash += stake * (1 + trade.net_return)
                        active.pop(idx)
                        break

        close_due_trades()
        equity_before_entry = cash + sum(stake for _, stake in active)
        for trade in sorted(events[day]["entry"], key=lambda t: t.score, reverse=True):
            if cash <= 0:
                break
            stake = min(cash, equity_before_entry * position_size)
            if stake <= 0:
                continue
            cash -= stake
            active.append((trade, stake))
            executed.append(trade)
        close_due_trades()
    return executed


def _run_variant(
    trades: list[CandidateTrade],
    config: PreExpectationConfig,
    kline_dir: Path,
) -> tuple[list[CandidateTrade], list[CandidateTrade], list[dict[str, Any]], dict[str, Any]]:
    selected = select_trades(
        trades,
        min_score=0,
        max_per_day=config.max_per_day,
        config=_strategy_config(config),
    )
    curve, metrics = run_portfolio(selected, position_size=config.position_size)
    executed = portfolio_executed_trades(selected, config.position_size)
    if metrics:
        add_benchmark_metrics(metrics, kline_dir)
    return selected, executed, curve, metrics


def _metrics_row(name: str, metrics: dict[str, Any]) -> str:
    if not metrics:
        return f"| {name} | 0 | N/A | N/A | N/A | N/A | N/A | N/A | N/A |"
    return (
        f"| {name} | {metrics['trade_count']} | {pct(metrics['total_return'])} | "
        f"{pct(metrics['annual_return'])} | {pct(metrics['max_drawdown'])} | "
        f"{pct(metrics['win_rate'])} | {pct(metrics['avg_trade_return'])} | "
        f"{metrics.get('profit_factor') or 0:.2f} | {pct(metrics.get('excess_vs_hs300'))} |"
    )


def run_pre_expectation_backtest(
    base_dir: Path = DEFAULT_BASE_DIR,
    start_date: str = "2024-01-01",
    end_date: str | None = "2026-06-08",
) -> dict[str, Any]:
    run_dir = base_dir / "data" / "announcement_backtest"
    kline_dir = run_dir / "klines"
    report_dir = base_dir / "reports" / "pre_expectation_backtest" / datetime.now().strftime("%Y%m%d_%H%M%S")
    report_dir.mkdir(parents=True, exist_ok=True)

    events = fetch_predict_events(run_dir, refresh=False)
    klines_by_code = load_cached_klines(kline_dir)
    benchmark_klines = klines_by_code.get("000300.SH") or []
    benchmark_by_date = close_by_date(benchmark_klines)
    names_by_code = _names_by_code(events)

    variants: dict[str, dict[str, Any]] = {}
    for pre_days in (3, 5, 10):
        config = PreExpectationConfig(pre_entry_days=pre_days)
        candidates = build_pre_event_candidates(events, klines_by_code, benchmark_by_date, config, start_date, end_date)
        selected, executed, curve, metrics = _run_variant(candidates, config, kline_dir)
        name = f"event_labeled_pre{pre_days}d"
        write_csv(report_dir / f"{name}_candidates.csv", [asdict(t) for t in candidates])
        write_csv(report_dir / f"{name}_selected_signals.csv", [asdict(t) for t in selected])
        write_csv(report_dir / f"{name}_executed_trades.csv", [asdict(t) for t in executed])
        write_csv(report_dir / f"{name}_equity_curve.csv", curve)
        variants[name] = {
            "kind": "event_labeled_upper_bound_not_directly_tradable",
            "config": asdict(config),
            "candidate_count": len(candidates),
            "selected_signal_count": len(selected),
            "executed_trade_count": len(executed),
            "metrics": metrics,
        }

    proxy_variants = {
        "calendar_proxy_baseline": PreExpectationConfig(pre_entry_days=5),
        "calendar_proxy_grid_best": PreExpectationConfig(
            pre_entry_days=5,
            proxy_hold_days=10,
            stop_loss=0.04,
            min_pre_5d_return=0.04,
            min_pre_10d_excess=0.02,
            max_pre_20d_return=0.25,
            position_size=0.10,
            max_per_day=5,
        ),
    }
    for name, proxy_config in proxy_variants.items():
        proxy_candidates = build_calendar_proxy_candidates(
            klines_by_code,
            benchmark_by_date,
            names_by_code,
            proxy_config,
            start_date,
            end_date,
        )
        selected, executed, proxy_curve, proxy_metrics = _run_variant(proxy_candidates, proxy_config, kline_dir)
        write_csv(report_dir / f"{name}_candidates.csv", [asdict(t) for t in proxy_candidates])
        write_csv(report_dir / f"{name}_selected_signals.csv", [asdict(t) for t in selected])
        write_csv(report_dir / f"{name}_executed_trades.csv", [asdict(t) for t in executed])
        write_csv(report_dir / f"{name}_equity_curve.csv", proxy_curve)
        variants[name] = {
            "kind": "deployable_proxy_no_future_event_label",
            "config": asdict(proxy_config),
            "candidate_count": len(proxy_candidates),
            "selected_signal_count": len(selected),
            "executed_trade_count": len(executed),
            "metrics": proxy_metrics,
        }

    summary = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "start_date": start_date,
        "end_date": end_date,
        "event_count": len(events),
        "cached_kline_count": len(klines_by_code),
        "variants": variants,
        "report_dir": str(report_dir),
    }
    (report_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), "utf-8")

    lines = [
        "# A股提前预期策略回测",
        "",
        f"生成时间：{summary['generated_at']}",
        f"区间：{start_date} 至 {end_date}",
        "",
        "## 口径",
        "",
        "- event_labeled_preXd：使用未来强公告作为历史标签，验证公告前是否存在可交易提前异动；这不是可直接实盘的策略。",
        "- calendar_proxy_baseline：不使用未来公告标签，只在披露高发月份扫描价格强于指数的股票；这是更接近实盘的原始代理版本。",
        "- calendar_proxy_grid_best：同样不使用未来公告标签，是小网格中表现最好的代理参数；它仍需警惕过拟合。",
        "- 入场：信号后下一交易日开盘买入。",
        "- 退出：A股T+1，买入当日不允许卖；之后触发-5%止损、+12%止盈，或到事件/固定持有期退出。",
        "- 成本：复用现有公告回测口径，买卖手续费、印花税和滑点均计入。",
        "",
        "## 结果",
        "",
        "| 版本 | 交易数 | 总收益 | 年化 | 最大回撤 | 胜率 | 平均单笔 | 盈亏比 | 超额沪深300 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for name, payload in variants.items():
        lines.append(_metrics_row(name, payload["metrics"]))
    lines.extend([
        "",
        "## 使用判断",
        "",
        "event_labeled_preXd 若表现好，只能说明提前炒预期现象存在，不能直接作为实盘信号。",
        "calendar_proxy 才是当前可讨论的实盘代理；若它不能同时跑赢沪深300并控制回撤，则不建议自动实盘。",
    ])
    (report_dir / "report.md").write_text("\n".join(lines) + "\n", "utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Backtest A-share pre-expectation strategy.")
    parser.add_argument("--base-dir", default=str(DEFAULT_BASE_DIR))
    parser.add_argument("--start-date", default="2024-01-01")
    parser.add_argument("--end-date", default="2026-06-08")
    args = parser.parse_args()
    summary = run_pre_expectation_backtest(Path(args.base_dir), args.start_date, args.end_date)
    print(json.dumps({
        "report_dir": summary["report_dir"],
        "variants": {
            name: payload["metrics"]
            for name, payload in summary["variants"].items()
        },
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
