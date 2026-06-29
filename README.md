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

## Output Data

Generated `data/`, `reports/`, `tmp/`, local virtual environments, and automation runtime files are intentionally ignored by Git. Recreate them by running the scripts on the target machine.
