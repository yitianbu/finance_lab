# A Share Pre-Expectation Strategy Design

## Goal

Build and backtest an A-share strategy for "提前预期": infer that a favorable event may happen before it is officially announced, buy only after price behavior confirms early capital participation, and exit around event realization or by strict risk controls.

## Core Idea

The strategy has two separate research layers:

1. **Event-labeled validation**: use historical high-quality positive announcements as labels, then test whether buying several trading days before the announcement had an edge. This proves whether the market often trades the expectation in advance, but it is not directly tradable because it knows future announcement targets.
2. **Calendar proxy validation**: avoid future event labels. During known disclosure-heavy months, scan the cached stock universe for price strength before any known event is used, then buy the next trading day. This is closer to live use, though the current cached universe is not a full all-A universe.

## Signal Definition

An entry is allowed only when all conditions are true at signal time:

- Price has started to move: recent 5-day return is above a minimum threshold.
- Stock is stronger than the index: recent 10-day return exceeds CSI 300 by a minimum threshold.
- Not already too crowded: recent 20-day return is below a cap.
- Trend is supported: close is above the recent 10-day average.
- Next-day entry is skipped if the open gaps up too much.

For event-labeled validation, the event must also be a strong positive fundamental label:

- Event score at least 96 using the existing `announcement_backtest` scorer.
- Forecast net profit not above 100 million RMB by default, matching the strongest prior sample.
- January and July events are excluded by default because prior tests showed unstable concentrated disclosure behavior.

## Trading Rules

- Entry: next trading day open after a valid signal.
- A-share T+1: no exit is allowed on the entry day.
- Stop loss: default 5% from entry price, checked from the first sellable day.
- Take profit: default 12% from entry price, checked from the first sellable day.
- Time/event exit:
  - Event-labeled validation exits on the first trading day after announcement unless stop/take-profit triggers earlier.
  - Calendar proxy exits after a fixed 5 trading days unless stop/take-profit triggers earlier.
- Same-day stop and take-profit ambiguity is handled conservatively: stop loss wins.
- Portfolio: cash simulation, position size default 10%, max 5 new entries per day, no overlapping position in the same stock.

## Success Criteria

A version is considered usable only if it passes all of these:

- Positive absolute return after transaction costs and slippage.
- Positive excess return versus CSI 300.
- Max drawdown within a range a human can tolerate, preferably under 12%.
- Enough trades to avoid a single-stock or single-month illusion.
- The deployable proxy must not rely on future event labels.

## Limits

- Existing K-line cache lacks volume, so the first version can only model price strength, not true volume confirmation.
- Existing cached universe is a subset of A-shares, not a complete point-in-time all-A universe.
- Historical announcement labels can validate the phenomenon, but cannot by themselves make a live strategy tradable.
- Daily bars cannot know intraday stop/take-profit order; the conservative rule avoids overstating returns.
