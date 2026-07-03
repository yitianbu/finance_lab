# Stock Range Trader Implementation Plan

## Goal

Build a reusable daily tool that takes one A-share code, uses only prior daily bars, predicts the next trading day's high/low range, and turns that range into a conservative buy/sell plan plus a 90-target rolling backtest.

## Scope

- Add `stock_strategy/stock_range_trader.py`.
- Support loading Eastmoney K-line JSON from file or fetching it by stock code.
- Keep model and tests stdlib-only so it can run in the local automation environment.
- Write reports under `reports/range_trader/{code}_{latest_date}/`.

## Model Shape

1. Compute prior-window features: returns, amplitude, candle position, MA distance, ATR percentage, and volume ratio.
2. Find historical similar signal days without using future data.
3. Predict next-day high/low using weighted next-day returns from similar days.
4. Calibrate an ATR band over the previous 90 target days and pick the smallest multiplier that reaches target coverage.
5. Generate a trading plan only when reward/risk is acceptable; otherwise return watch/no-chase guidance.

## Verification

- Unit tests cover no-future leakage, ATR calibration, trade-plan gating, conservative same-day execution, and metrics output.
- Run the full `stock_strategy/tests` suite.
- Run a sample report for `300450` using the latest available Eastmoney K-line data.
