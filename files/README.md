# finance_lab

A-share quantitative research scripts for late-session 5-trading-day holding candidates.

This repository is research tooling only. It does not connect to brokerage APIs, does not place real orders, and does not provide investment advice.

## Setup

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
```

Run tests:

```bash
PYTHONPATH=stock_strategy:. python3 -m unittest discover -s stock_strategy/tests
```

## 14:50 Hold-5 Candidate Scan

Main script:

```bash
python3 scripts/stock_strategy/run_hold5_tail_candidates.py \
  --latest-date YYYY-MM-DD \
  --max-validate 420 \
  --workers 28 \
  --analog-count 120 \
  --recheck-top 10 \
  --recent-metrics-json path/to/recent_metrics.json
```

The live scan ranks candidates by expected 5-trading-day profitability first, then labels risk tier (`核心`, `进取`, `观察`). It also performs a lightweight Top10 quote recheck to reduce late-session tail deterioration risk.

The current retained production policy is:

- legacy bottom ranking score
- 30-sample strategy-state gate
- no hard brokerage/trading integration

The strategy-state gate uses completed Top3 equal-weight 5-day signal batches:

- window: latest 30 completed batches
- minimum completed samples: 12
- average 5-day return >= 0.80%
- win rate >= 50%
- average excess return vs the strongest of SH/SZ/CY >= -2.50%
- rolling max drawdown >= -65%

`recent_metrics.json` should include:

```json
{
  "avg_return": 0.02,
  "win_rate": 0.60,
  "worst_return": -0.08,
  "excess_return": 0.01,
  "consecutive_loss_days": 0,
  "medium_sample_days": 30,
  "medium_avg_return": 0.009,
  "medium_win_rate": 0.50,
  "medium_excess_return": 0.02,
  "medium_excess_best_return": -0.02,
  "medium_max_drawdown": -0.60,
  "medium_consecutive_loss_days": 0
}
```

If `medium_excess_best_return` or `medium_max_drawdown` is missing, the optimized benchmark gate is not evaluated.

## Proxy Backtest

```bash
python3 scripts/stock_strategy/backtest_hold5_tail_proxy.py \
  --start 20240629 \
  --end 20260629 \
  --workers 32 \
  --max-validate 420 \
  --analog-count 60
```

Backtest limitations:

- daily close proxy, not historical 14:50 order book replay
- current stock universe creates survivorship bias
- overlapping 5-day signal compounding is not a capital-constrained portfolio simulation

## Bottom Volume Candidate Scan

This scanner looks for A-share candidates that are still close to a recent bottom while showing a price-confirmed volume expansion. It is designed as a high-risk, high-upside research filter, not as an order system.

```bash
PYTHONPATH=stock_strategy:. python3 scripts/stock_strategy/run_bottom_volume_candidates.py \
  --codes 300450,600000.SH \
  --beg 20240101 \
  --end YYYYMMDD
```

For a larger local pool:

```bash
PYTHONPATH=stock_strategy:. python3 scripts/stock_strategy/run_bottom_volume_candidates.py \
  --codes-file path/to/codes.csv \
  --kline-dir path/to/kline_cache \
  --min-volume-ratio 1.8 \
  --max-low-distance 0.16 \
  --stop-loss-pct 0.06 \
  --take-profit-pct 0.15
```

Outputs are written under `reports/bottom_volume/YYYYMMDD_HHMMSS/`:

- `bottom_volume_scan.csv`
- `bottom_volume_scan.json`
- `bottom_volume_scan_report.md`

Core filters:

- drawdown from recent high >= 20%
- latest close within 16% of the 60-day low
- latest volume >= 1.8x prior 20-day average volume
- latest close return >= 2% and close location >= 60% of the day range
- 20-day rebound <= 18% to avoid late chase signals
- default paper plan: stop loss 6%, target 15%, max holding 5 sessions

## Low-Frequency Breakout Buy/Sell Strategy

This scanner is stricter and lower-frequency than the bottom-volume scan. It looks for stocks that have already built a multi-week base, are above medium/long moving averages, and then break out on strong volume. The sell logic is designed to let a winning swing run while cutting failed breakouts quickly.

```bash
PYTHONPATH=stock_strategy:. python3 scripts/stock_strategy/run_low_frequency_breakout_candidates.py \
  --codes 300450,600000.SH \
  --beg 20240101 \
  --end YYYYMMDD
```

For a larger pool:

```bash
PYTHONPATH=stock_strategy:. python3 scripts/stock_strategy/run_low_frequency_breakout_candidates.py \
  --codes-file path/to/codes.csv \
  --kline-dir path/to/kline_cache \
  --min-volume-ratio 1.8 \
  --max-base-range 0.15 \
  --target-high-pct 0.28 \
  --max-initial-risk 0.085
```

Outputs are written under `reports/low_frequency_breakout/YYYYMMDD_HHMMSS/`:

- `low_frequency_breakout_scan.csv`
- `low_frequency_breakout_scan.json`
- `low_frequency_breakout_scan_report.md`

Default buy rules:

- close above MA20/MA60/MA120, with MA20 > MA60 > MA120
- close breaks the prior 55-session high by at least 2.0%
- prior 45-session base range <= 15%
- latest volume >= 1.8x prior 20-session average volume
- close location >= 80% of the day range
- 5-session return <= 16% and 20-session return <= 20% to avoid vertical chase

Default sell rules:

- next-session entry only if the open is not more than 2.0% above signal close
- hard stop around the breakout pivot, capped by 8.5% max initial risk
- target zone: +16% partial reference and +28% high target
- time stop: exit if follow-through is below 3% after 5 sessions
- trailing stop: after a 12% gain, exit if price gives back 8% from the best close
- max holding period: 45 sessions

Run trailing 1-month, 3-month, and 6-month portfolio-style backtests:

```bash
PYTHONPATH=stock_strategy:. python3 scripts/stock_strategy/backtest_low_frequency_breakout_periods.py \
  --events-csv reports/announcement_backtest/all_scored_events.csv \
  --end YYYYMMDD \
  --limit 0 \
  --workers 48
```

The period backtest uses the event CSV as a reproducible stock universe by default, then applies these portfolio rules:

- at most 1 new entry per day
- at most 3 open positions
- 10% notional per selected trade
- same-stock duplicate entries are blocked while a position is open
- same-day signals are sorted by strategy score and reward/risk

Outputs are written under `reports/low_frequency_breakout/period_backtest/YYYYMMDD_HHMMSS/`:

- `period_summary.csv`
- `period_trades.csv`
- `period_results.json`
- `report.md`

## Long-Base Breakout Buy/Sell Strategy

This is the stricter "long sideways consolidation, then breakout" variant. It is designed to make the breakout trend more obvious by requiring a much longer base, a tighter platform, volume expansion, and a next-day entry discipline that avoids chasing excessive gaps.

```bash
PYTHONPATH=stock_strategy:. python3 scripts/stock_strategy/run_long_base_breakout_candidates.py \
  --codes 300450,600000.SH \
  --beg 20240101 \
  --end YYYYMMDD
```

For a larger pool:

```bash
PYTHONPATH=stock_strategy:. python3 scripts/stock_strategy/run_long_base_breakout_candidates.py \
  --codes-file path/to/codes.csv \
  --kline-dir path/to/kline_cache \
  --min-volume-ratio 1.8 \
  --max-base-range 0.18 \
  --min-base-days 90 \
  --max-initial-risk 0.08
```

Outputs are written under `reports/long_base_breakout/YYYYMMDD_HHMMSS/`:

- `long_base_breakout_scan.csv`
- `long_base_breakout_scan.json`
- `long_base_breakout_scan_report.md`

Default buy rules:

- at least 180 sessions of history
- previous 120-session platform, with at least 90 sessions counted as the base
- platform range <= 18% and platform first/last third slope within +/-8%
- close above MA20/MA60/MA120
- close breaks the platform high by at least 2.0% and at least 0.35 ATR
- latest volume >= 1.8x prior 20-session average volume
- close location >= 78% of the day range
- 20-session return <= 18% to avoid late vertical chase
- wait 1 confirmation session after the breakout; confirmation close must be at least 0.5% above signal close and must not deeply pull back into the platform

Default sell rules:

- entry is delayed until the session after confirmation; the open must not be more than 2.5% above confirmation close
- actual entry reward/risk must remain at least 2.0
- hard stop near the platform high, capped by 8% max initial risk
- failed breakout exit if price closes back below the platform high buffer
- target is based on platform height, with 16% minimum and 32% maximum target return
- time stop: exit if follow-through is below 4% after 10 sessions
- trailing stop: after a 12% gain, exit if price gives back 8% from the best close
- max holding period: 60 sessions

Run trailing 1-month, 3-month, and 6-month portfolio-style backtests:

```bash
PYTHONPATH=stock_strategy:. python3 scripts/stock_strategy/backtest_long_base_breakout_periods.py \
  --events-csv reports/announcement_backtest/all_scored_events.csv \
  --kline-dir data/hold5_tail_proxy/klines \
  --end YYYYMMDD \
  --limit 0 \
  --workers 48
```

Outputs are written under `reports/long_base_breakout/period_backtest/YYYYMMDD_HHMMSS/`:

- `period_summary.csv`
- `period_trades.csv`
- `period_results.json`
- `report.md`

## Long-Term Hold Outperform-Benchmark Strategy

This scanner is for a low-turnover, long-only holding style. It looks for a stock that is already in a durable uptrend and is outperforming a broad benchmark, then keeps the sell rules deliberately slow so the position is not churned by normal pullbacks.

```bash
PYTHONPATH=stock_strategy:. python3 scripts/stock_strategy/run_long_term_hold_candidates.py \
  --codes 300450,600000.SH \
  --beg 20240101 \
  --end YYYYMMDD \
  --benchmark-code 000300.SH
```

For a larger pool:

```bash
PYTHONPATH=stock_strategy:. python3 scripts/stock_strategy/run_long_term_hold_candidates.py \
  --codes-file path/to/codes.csv \
  --kline-dir path/to/kline_cache \
  --benchmark-code 000300.SH \
  --min-excess-return-120d 0.06 \
  --min-excess-return-240d 0.08 \
  --min-hold-days 60
```

Run a portfolio-style all-A backtest:

```bash
PYTHONPATH=stock_strategy:. python3 scripts/stock_strategy/backtest_long_term_hold_all_a.py \
  --period-start 2025-07-02 \
  --period-end 2026-07-01
```

The generated report includes the selected stock names. For a fuller local name table, pass a CSV with `secucode,name` or `SECUCODE,SECURITY_NAME_ABBR` columns:

```bash
PYTHONPATH=stock_strategy:. python3 scripts/stock_strategy/backtest_long_term_hold_all_a.py \
  --stock-name-csv path/to/a_share_names.csv
```

Use the benchmark trend gate to pause new entries when the broad market is weak:

```bash
PYTHONPATH=stock_strategy:. python3 scripts/stock_strategy/backtest_long_term_hold_all_a.py \
  --period-start 2024-07-01 \
  --period-end 2026-06-08 \
  --market-gate \
  --market-gate-ma 120 \
  --market-gate-return-lookback 60 \
  --market-gate-min-return 0
```

The all-A portfolio backtest uses the stricter default execution layer:

- rank score must be at least 102
- at most 1 new entry per day
- at most 5 open positions
- 20% target notional per selected trade
- same stock is not bought again while it is already open
- no new entry is opened on the period end date
- optional market gate: when enabled, new entries require benchmark close above the chosen moving average and benchmark trailing return above the configured threshold

Outputs are written under `reports/long_term_hold/YYYYMMDD_HHMMSS/`:

- `long_term_hold_scan.csv`
- `long_term_hold_scan.json`
- `long_term_hold_scan_report.md`

All-A portfolio backtest outputs are written under `reports/long_term_hold/all_a_stock_backtest_YYYYMMDD_HHMMSS/`:

- `all_a_stock_long_term_hold_events.csv`
- `all_a_stock_long_term_hold_trades.csv`
- `equity_curve.csv`
- `summary.json`
- `report.md`

Run robustness validation across rolling periods, parameter grids, and extra round-trip cost assumptions:

```bash
PYTHONPATH=stock_strategy:. python3 scripts/stock_strategy/validate_long_term_hold_robustness.py \
  --period-start 2024-07-01 \
  --market-gate \
  --rank-scores 101,102,103 \
  --max-positions-grid 3,5 \
  --target-weights 0.15,0.20 \
  --max-new-entries-grid 1,2 \
  --extra-round-trip-costs 0,0.001,0.003,0.005
```

Robustness outputs are written under `reports/long_term_hold/robustness/YYYYMMDD_HHMMSS/`:

- `period_summary.csv`
- `parameter_grid.csv`
- `friction_summary.csv`
- `summary.json`
- `robustness_report.md`

Default buy rules:

- at least 260 sessions of stock history and enough benchmark history
- close above MA200, with MA60 > MA120 > MA200
- 120-session stock return >= 6%
- 120-session excess return vs benchmark >= 6%
- 240-session excess return vs benchmark >= 8%
- 120-session drawdown no worse than -28%
- 120-session annualized volatility <= 42%
- close no more than 55% above MA200, to avoid very late long-term chase entries
- buy zone: signal close -3% to signal close +3%; next open above the zone is skipped in backtests

Default sell rules:

- initial stop: the higher of entry price -12% and MA200 -3%
- minimum holding period: 60 sessions before slow trend/relative exits
- trend exit: after the minimum hold, close below MA200 -3%
- relative exit: 60-session excess return vs benchmark <= -6% and close below MA120
- trailing exit: after a 25% open profit, exit when close gives back 15% from the best close
- max holding period: 520 sessions

This strategy is research tooling only. It does not guarantee profit or benchmark outperformance.

## Output Data

Generated `data/`, `reports/`, `tmp/`, local virtual environments, and automation runtime files are intentionally ignored by Git. Recreate them by running the scripts on the target machine.

## Publish Strategy Site

Build a static strategy site that can be uploaded to any static host:

```bash
PYTHONPATH=stock_strategy:. python3 scripts/stock_strategy/build_strategy_site.py --clean
```

The publishable site is written to `dist/strategy_site/`. Preview it locally:

```bash
python3 -m http.server 8899 --bind 127.0.0.1 --directory dist/strategy_site
```
