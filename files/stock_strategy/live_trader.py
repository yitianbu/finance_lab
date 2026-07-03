from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

from announcement_backtest import (
    DEFAULT_BASE_DIR,
    CandidateTrade,
    build_candidate,
    event_passes_config,
    fetch_predict_events,
    load_klines,
    named_strategy_config,
    score_predict_event,
    select_trades,
)


@dataclass(frozen=True)
class Position:
    secucode: str
    stock_name: str
    quantity: int
    avg_price: float
    market_price: float
    entry_date: str = ""
    planned_exit_date: str = ""

    @property
    def market_value(self) -> float:
        return self.quantity * self.market_price


@dataclass(frozen=True)
class PaperAccount:
    cash: float
    positions: dict[str, Position] = field(default_factory=dict)

    @property
    def market_value(self) -> float:
        return sum(position.market_value for position in self.positions.values())

    @property
    def equity(self) -> float:
        return self.cash + self.market_value

    @property
    def exposure(self) -> float:
        if self.equity <= 0:
            return 0.0
        return self.market_value / self.equity


@dataclass(frozen=True)
class LiveRiskConfig:
    position_size: float = 0.20
    max_total_exposure: float = 0.80
    max_new_positions: int = 5
    min_order_cash: float = 10_000
    blacklist: tuple[str, ...] = ()
    reject_st: bool = True
    min_price: float = 2.0
    max_price: float = 500.0


@dataclass(frozen=True)
class PaperOrder:
    order_id: str
    trade_date: str
    side: str
    secucode: str
    stock_code: str
    stock_name: str
    quantity: int
    limit_price: float
    target_cash: float
    reason: str
    planned_exit_date: str = ""
    status: str = "planned"


@dataclass(frozen=True)
class RiskRejection:
    trade_date: str
    secucode: str
    stock_code: str
    stock_name: str
    reason: str


@dataclass(frozen=True)
class PaperFill:
    order_id: str
    trade_date: str
    side: str
    secucode: str
    stock_name: str
    quantity: int
    price: float
    cash_amount: float


@dataclass(frozen=True)
class BuyPlan:
    trade_date: str
    accepted_orders: list[PaperOrder]
    rejected: list[RiskRejection]


def is_st_or_delisting(stock_name: str) -> bool:
    upper = stock_name.upper()
    return "ST" in upper or "退" in stock_name


def risk_reject_reason(
    trade: CandidateTrade,
    account: PaperAccount,
    config: LiveRiskConfig,
    reserved_cash: float = 0.0,
    accepted_exposure_cash: float = 0.0,
) -> str:
    if trade.secucode in config.blacklist:
        return "黑名单"
    if config.reject_st and is_st_or_delisting(trade.stock_name):
        return "ST或退市风险"
    if trade.entry_price < config.min_price or trade.entry_price > config.max_price:
        return "价格异常"
    if trade.secucode in account.positions:
        return "已有持仓"

    equity = account.equity
    target_cash = equity * config.position_size
    if target_cash < config.min_order_cash:
        return "订单金额低于下限"
    if target_cash > account.cash - reserved_cash:
        return "现金不足"
    projected_exposure = (account.market_value + accepted_exposure_cash + target_cash) / equity if equity > 0 else 1.0
    if projected_exposure > config.max_total_exposure:
        return "组合仓位超过上限"
    return ""


def build_buy_plan(
    candidates: list[CandidateTrade],
    account: PaperAccount,
    config: LiveRiskConfig,
    trade_date: str,
) -> BuyPlan:
    accepted: list[PaperOrder] = []
    rejected: list[RiskRejection] = []
    reserved_cash = 0.0
    accepted_exposure_cash = 0.0

    for trade in candidates:
        if trade.entry_date != trade_date:
            continue
        if len(accepted) >= config.max_new_positions:
            rejected.append(RiskRejection(trade_date, trade.secucode, trade.stock_code, trade.stock_name, "单日买入上限"))
            continue

        reason = risk_reject_reason(trade, account, config, reserved_cash, accepted_exposure_cash)
        if reason:
            rejected.append(RiskRejection(trade_date, trade.secucode, trade.stock_code, trade.stock_name, reason))
            continue

        target_cash = account.equity * config.position_size
        quantity = int(target_cash / trade.entry_price / 100) * 100
        if quantity <= 0:
            rejected.append(RiskRejection(trade_date, trade.secucode, trade.stock_code, trade.stock_name, "不足一手"))
            continue
        cash_amount = quantity * trade.entry_price
        order_id = f"{trade_date.replace('-', '')}-{len(accepted) + 1:03d}-{trade.stock_code}"
        accepted.append(PaperOrder(
            order_id=order_id,
            trade_date=trade_date,
            side="BUY",
            secucode=trade.secucode,
            stock_code=trade.stock_code,
            stock_name=trade.stock_name,
            quantity=quantity,
            limit_price=trade.entry_price,
            target_cash=cash_amount,
            reason=trade.reasons,
            planned_exit_date=trade.exit_date,
        ))
        reserved_cash += cash_amount
        accepted_exposure_cash += cash_amount

    return BuyPlan(trade_date=trade_date, accepted_orders=accepted, rejected=rejected)


def build_sell_plan(account: PaperAccount, trade_date: str) -> list[PaperOrder]:
    orders: list[PaperOrder] = []
    for position in account.positions.values():
        if not position.planned_exit_date or position.planned_exit_date > trade_date:
            continue
        order_id = f"{trade_date.replace('-', '')}-SELL-{len(orders) + 1:03d}-{position.secucode.split('.')[0]}"
        orders.append(PaperOrder(
            order_id=order_id,
            trade_date=trade_date,
            side="SELL",
            secucode=position.secucode,
            stock_code=position.secucode.split(".")[0],
            stock_name=position.stock_name,
            quantity=position.quantity,
            limit_price=position.market_price,
            target_cash=position.quantity * position.market_price,
            reason="planned_exit",
            planned_exit_date=position.planned_exit_date,
        ))
    return orders


def apply_paper_fills(orders: list[PaperOrder], account: PaperAccount) -> tuple[list[PaperFill], PaperAccount]:
    cash = account.cash
    positions = dict(account.positions)
    fills: list[PaperFill] = []
    for order in orders:
        cash_amount = order.quantity * order.limit_price
        if order.side == "BUY":
            if cash_amount > cash:
                continue
            cash -= cash_amount
            existing = positions.get(order.secucode)
            if existing:
                total_quantity = existing.quantity + order.quantity
                avg_price = ((existing.quantity * existing.avg_price) + cash_amount) / total_quantity
                positions[order.secucode] = Position(
                    order.secucode,
                    order.stock_name,
                    total_quantity,
                    avg_price,
                    order.limit_price,
                    entry_date=existing.entry_date or order.trade_date,
                    planned_exit_date=order.planned_exit_date or existing.planned_exit_date,
                )
            else:
                positions[order.secucode] = Position(
                    order.secucode,
                    order.stock_name,
                    order.quantity,
                    order.limit_price,
                    order.limit_price,
                    entry_date=order.trade_date,
                    planned_exit_date=order.planned_exit_date,
                )
            fills.append(PaperFill(
                order_id=order.order_id,
                trade_date=order.trade_date,
                side=order.side,
                secucode=order.secucode,
                stock_name=order.stock_name,
                quantity=order.quantity,
                price=order.limit_price,
                cash_amount=cash_amount,
            ))
        elif order.side == "SELL":
            existing = positions.get(order.secucode)
            if not existing:
                continue
            quantity = min(order.quantity, existing.quantity)
            cash_amount = quantity * order.limit_price
            cash += cash_amount
            remaining = existing.quantity - quantity
            if remaining > 0:
                positions[order.secucode] = Position(
                    existing.secucode,
                    existing.stock_name,
                    remaining,
                    existing.avg_price,
                    order.limit_price,
                    entry_date=existing.entry_date,
                    planned_exit_date=existing.planned_exit_date,
                )
            else:
                del positions[order.secucode]
            fills.append(PaperFill(
                order_id=order.order_id,
                trade_date=order.trade_date,
                side=order.side,
                secucode=order.secucode,
                stock_name=order.stock_name,
                quantity=quantity,
                price=order.limit_price,
                cash_amount=cash_amount,
            ))
    return fills, PaperAccount(cash=cash, positions=positions)


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_daily_outputs(output_dir: Path, plan: BuyPlan, fills: list[PaperFill], account: PaperAccount) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(
        output_dir / "orders.csv",
        [asdict(order) for order in plan.accepted_orders],
        ["order_id", "trade_date", "side", "secucode", "stock_code", "stock_name", "quantity", "limit_price", "target_cash", "reason", "planned_exit_date", "status"],
    )
    write_csv(
        output_dir / "rejections.csv",
        [asdict(item) for item in plan.rejected],
        ["trade_date", "secucode", "stock_code", "stock_name", "reason"],
    )
    write_csv(
        output_dir / "fills.csv",
        [asdict(fill) for fill in fills],
        ["order_id", "trade_date", "side", "secucode", "stock_name", "quantity", "price", "cash_amount"],
    )
    write_csv(
        output_dir / "positions.csv",
        [asdict(position) | {"market_value": position.market_value} for position in account.positions.values()],
        ["secucode", "stock_name", "quantity", "avg_price", "market_price", "entry_date", "planned_exit_date", "market_value"],
    )
    summary = {
        "trade_date": plan.trade_date,
        "cash": account.cash,
        "market_value": account.market_value,
        "equity": account.equity,
        "exposure": account.exposure,
        "planned_orders": len(plan.accepted_orders),
        "fills": len(fills),
        "rejections": len(plan.rejected),
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), "utf-8")
    lines = [
        "# 纸面实盘日报",
        "",
        f"交易日：{plan.trade_date}",
        f"计划订单：{len(plan.accepted_orders)}",
        f"纸面成交：{len(fills)}",
        f"风控拒绝：{len(plan.rejected)}",
        f"现金：{account.cash:.2f}",
        f"持仓市值：{account.market_value:.2f}",
        f"账户权益：{account.equity:.2f}",
        f"仓位：{account.exposure:.2%}",
        "",
        "## 风控拒绝",
    ]
    if plan.rejected:
        lines.extend(f"- {item.secucode} {item.stock_name}: {item.reason}" for item in plan.rejected)
    else:
        lines.append("- 无")
    lines.extend(["", "## 计划订单"])
    if plan.accepted_orders:
        lines.extend(f"- {order.secucode} {order.stock_name}: {order.quantity} 股 @ {order.limit_price:.2f}" for order in plan.accepted_orders)
    else:
        lines.append("- 无")
    (output_dir / "daily_report.md").write_text("\n".join(lines), "utf-8")


def load_paper_account(path: Path | None, initial_cash: float) -> PaperAccount:
    if path is None or not path.exists():
        return PaperAccount(cash=initial_cash)
    raw = json.loads(path.read_text("utf-8"))
    positions = {
        code: Position(**position)
        for code, position in (raw.get("positions") or {}).items()
    }
    return PaperAccount(cash=float(raw.get("cash", initial_cash)), positions=positions)


def save_paper_account(path: Path, account: PaperAccount) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "cash": account.cash,
        "positions": {code: asdict(position) for code, position in account.positions.items()},
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), "utf-8")


def build_candidates_for_trade_date(base_dir: Path, trade_date: str, refresh: bool = False) -> list[CandidateTrade]:
    run_dir = base_dir / "data" / "announcement_backtest"
    kline_dir = run_dir / "klines"
    config = named_strategy_config("benchmark_constrained")
    events = fetch_predict_events(run_dir, refresh=refresh)
    scored: list[dict[str, Any]] = []
    for event in events:
        score, grade, reasons = score_predict_event(event)
        row = dict(event)
        row["EVENT_SCORE"] = score
        row["EVENT_GRADE"] = grade
        row["SCORE_REASONS"] = ";".join(reasons)
        scored.append(row)
    relevant = [
        event for event in scored
        if event_passes_config(event, config)
        and str(event.get("NOTICE_DATE") or "")[:10] <= trade_date
    ]
    secucodes = sorted({event["SECUCODE"] for event in relevant})
    klines_by_code = load_klines(secucodes, kline_dir, refresh=refresh)
    candidates: list[CandidateTrade] = []
    for event in relevant:
        candidate = build_candidate(event, klines_by_code.get(event["SECUCODE"]) or [], config)
        if candidate and not candidate.skip_reason and candidate.entry_date == trade_date:
            candidates.append(candidate)
    selected = select_trades(candidates, config.min_score, config.max_per_day, config=config)
    return selected


def run_daily_paper_trading(
    base_dir: Path,
    trade_date: str,
    refresh: bool = False,
    initial_cash: float = 1_000_000,
) -> Path:
    account_path = base_dir / "data" / "live_trading" / "paper_account.json"
    account = load_paper_account(account_path, initial_cash)
    sell_orders = build_sell_plan(account, trade_date)
    sell_fills, account_after_sells = apply_paper_fills(sell_orders, account)
    candidates = build_candidates_for_trade_date(base_dir, trade_date, refresh=refresh)
    strategy = named_strategy_config("benchmark_constrained")
    risk = LiveRiskConfig(position_size=strategy.position_size, max_new_positions=strategy.max_per_day)
    buy_plan = build_buy_plan(candidates, account_after_sells, risk, trade_date)
    buy_fills, updated = apply_paper_fills(buy_plan.accepted_orders, account_after_sells)
    plan = BuyPlan(
        trade_date=trade_date,
        accepted_orders=[*sell_orders, *buy_plan.accepted_orders],
        rejected=buy_plan.rejected,
    )
    fills = [*sell_fills, *buy_fills]
    save_paper_account(account_path, updated)
    output_dir = base_dir / "reports" / "live_trading" / trade_date
    write_daily_outputs(output_dir, plan, fills, updated)
    return output_dir


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", type=Path, default=DEFAULT_BASE_DIR)
    parser.add_argument("--trade-date", default=date.today().isoformat())
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--initial-cash", type=float, default=1_000_000)
    args = parser.parse_args()
    output_dir = run_daily_paper_trading(args.base_dir, args.trade_date, args.refresh, args.initial_cash)
    print(json.dumps({"output_dir": str(output_dir)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
