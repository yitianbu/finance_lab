# Stock Pool Range Scan Design

## Objective

Extend the single-stock next-day range trader into a batch scanner that can search a candidate stock pool and rank the stocks whose recent behavior best fits the strategy.

## Inputs

- Announcement event CSV: `reports/announcement_backtest/all_scored_events.csv`.
- Optional manual code list through a CLI argument or file.
- Eastmoney adjusted daily K-line data for each stock.

## Outputs

- Combined Markdown report under `reports/range_trader/pool_scan/{timestamp}/pool_scan_report.md`.
- CSV and JSON audit files with every scanned stock, including failed fetches.
- Per-stock detailed reports reuse `stock_range_trader.py`.

## Selection Rules

A stock is marked as tradable only when:

- The single-stock plan says `BUY_ZONE`.
- 90-target trade backtest has enough actual trades.
- Total rule return is positive.
- Maximum drawdown is within the configured limit.
- ATR calibrated band coverage is above the minimum threshold.

Stocks that fail any rule remain in the report with an explicit reason.

## Non-Goals

- No real brokerage orders.
- No intraday tick prediction.
- No guarantee of profitability.
