# A股尾盘5日持有策略总结

本文记录当前保留的 14:50 A股尾盘 5 个交易日持有候选筛选策略。

本策略只用于量化研究候选输出，不连接券商接口，不执行真实交易，不构成投资建议。

## 当前保留策略

当前生产口径：

```text
旧底层排序
+ 30样本强收益状态拦截
+ 最终候选Top10轻量实时报价复核
+ 强行情攻击模式首选排序
+ 核心 / 进取 / 观察 风险分层输出
```

已废弃两次手工新权重实验。原因是两次新权重在两年代理回测和最近两个月窗口里都显著弱于旧底层排序。

## 候选池与硬过滤

运行时优先使用全A实时行情构建候选池。

硬剔除：

- ST / *ST / 退市风险
- 停牌或价格异常
- 流动性不足
- 明显无法成交的一字涨停 / 跌停
- 尾盘承接过弱
- 复核报价缺失或异常

候选倾向：

- 成交额充足
- 尾盘承接较强
- 板块有共振
- 当日不过度追高
- 历史相似形态 5 日收益统计稳定

## 底层排序

底层排序仍保留旧评分公式，因为它在当前代理回测中表现最好。

主要因子：

- 历史相似样本 5 日胜率
- 平均 5 日净收益
- 利润因子
- 尾盘区间位置
- 成交额
- 板块平均涨幅
- 主力净额占成交额比例
- 样本收益序列最大回撤

当前评分等价公式：

```text
score =
  win_rate * 30
  + avg_return * 350
  + min(profit_factor, 8) * 4
  + close_pos * 10
  + amount_billion * 1.5
  + industry_avg_pct * 80
  + main_net_ratio * 10
  + max(sample_drawdown, -0.5) * 20
```

排序原则：

- 先按预期 5 日盈利能力 / 综合分排序。
- 风险层级只作为标签，不把低分的“核心”强行排到高分“进取”前面。

## 风险分层

输出分三层：

- `核心`：统计收益、左尾风险、持有回撤、reward/risk 都较干净。
- `进取`：收益预期强，但左尾、持有回撤或止损收益比不够干净，只适合研究。
- `观察`：当前风险或统计质量不足，不建议新开仓。

如果没有核心但存在进取候选，报告应输出：

```text
无核心候选；可研究进取候选 N 只
```

不要简单写成“无候选”。

## 30样本强收益状态拦截

这是当前最重要的风控优化。

使用最近已完成的 Top3 等权 5 日信号结果作为策略状态判断。

门槛：

- 窗口：最近 30 个已完成 5 日信号批次
- 最少样本：12 个完成批次
- 平均 5 日收益 `>= 0.80%`
- 胜率 `>= 50%`
- 相对上证 / 深成 / 创业板三者中最强指数的平均超额 `>= -2.50%`
- 滚动最大回撤 `>= -65%`

若未达标，策略状态转红，默认不建议新开仓。

`recent_metrics.json` 需要包含：

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

如果缺少 `medium_excess_best_return` 或 `medium_max_drawdown`，强收益拦截不会评估，报告会标明“未评估”。

## Top10轻量实时报价复核

为避免尾盘突变，不重复拉全A，只对最终候选 Top10 额外拉轻量实时报价。

复核会降级以下情况：

- 价格较评分快照下跌超过 2%
- 当日跌幅过大
- 尾盘位置跌破 50%
- 上影线 / 回落明显
- 接近一字涨停等不易成交状态
- 报价缺失或异常

## 强行情攻击模式

攻击模式不是独立开仓开关，也不覆盖红色拦截。它只在策略已经没有被红色拦截时生效，用于在同一行动层级里把更适合“强行情择一”的候选提前。

触发门槛：

- 最近 30 个已完成信号批次中至少 12 批
- 中期平均 5 日收益 `>= 6.00%`
- 中期胜率 `>= 55%`
- 相对最强指数超额 `>= -2.50%`
- 中期最大回撤 `>= -65%`
- 当天原 Top3 平均预期收益 `>= 1.50%`
- 当天原 Top3 平均胜率 `>= 54%`
- 当天原 Top3 平均利润因子 `>= 1.4`
- 当天原 Top3 平均 reward/risk `>= 1.0`
- 当天原 Top3 最差样本 `>= -22%`
- 当天原 Top3 最差持有回撤 `>= -25%`
- 当天原 Top3 平均尾盘位置 `>= 55%`

触发后，在 Top10 已复核候选里剔除观察层级和复核异常候选，再按风险收益平衡分选择首选：

```text
attack_score =
  avg_return * 130
  + win_rate * 20
  + min(profit_factor, 6) * 2
  + reward_risk * 8
  + worst_return * 80
  + worst_hold_drawdown * 40
  + max_drawdown * 20
  + close_pos * 5
```

注意：攻击模式只调整排序，不直接扩大候选数量，不放行红色状态。

## 当前回测结论

日线收盘代理回测，非历史 14:50 盘口回放。

| 方案 | 复合收益 | 最大回撤 |
|---|---:|---:|
| 两年无拦截 Top3 | +1552.09% | -89.17% |
| 两年加30样本拦截 Top3 | +4924.91% | -55.82% |
| 最近2个月加30样本拦截 Top3 | +339.18% | -46.89% |
| 两年加拦截 + 攻击模式首选排序 | +7897.67% | -55.82% |
| 最近2个月加拦截 + 攻击模式首选排序 | +694.93% | -28.08% |

对比结论：

- 加拦截后，两年复合收益和最大回撤都明显改善。
- 最近两个月属于盈利状态，拦截没有误伤利润窗口。
- 攻击模式只在 2026-05-20 至 2026-05-29 的 7 个强状态交易日触发；2025Q1 亏损区间未触发。
- 攻击模式样本较少，属于可控增强项，不应取消红色拦截或替代 Top3 默认口径。
- 两年全样本跑赢上证和深成，但没有跑赢极强趋势下的创业板代理。
- 这不是稳定每天交易、稳定每月跑赢所有指数的策略。

## 已废弃的优化实验

尝试过两组手工新评分权重：

| 实验 | 两年无拦截 | 两年加拦截 | 最近2个月加拦截 | 结论 |
|---|---:|---:|---:|---|
| 重风险 / 趋势惩罚 | -94.89% | -33.05% | -23.06% | 废弃 |
| 轻量风险修正 | -97.00% | -69.93% | +24.81% | 废弃 |

结论：不要手工继续调评分权重。当前更有效的优化方向是保存每日已分析候选 TopN，再做可解释的状态切换和 walk-forward 验证。

## 常用命令

运行测试：

```bash
PYTHONPATH=stock_strategy:. python3 -m unittest discover -s stock_strategy/tests
```

14:50 候选筛选：

```bash
python3 scripts/stock_strategy/run_hold5_tail_candidates.py \
  --latest-date YYYY-MM-DD \
  --max-validate 420 \
  --workers 28 \
  --analog-count 120 \
  --recheck-top 10 \
  --recent-metrics-json path/to/recent_metrics.json
```

两年代理回测：

```bash
python3 scripts/stock_strategy/backtest_hold5_tail_proxy.py \
  --start 20240629 \
  --end 20260629 \
  --workers 32 \
  --max-validate 420 \
  --analog-count 60
```

保存每日已分析候选 Top30，用于继续做 TopN / 动态择一研究：

```bash
python3 scripts/stock_strategy/backtest_hold5_tail_proxy.py \
  --start 20240629 \
  --end 20260629 \
  --workers 32 \
  --max-validate 420 \
  --analog-count 60 \
  --save-analyzed-top 30
```

## 换电脑使用

```bash
git clone https://github.com/yitianbu/finance_lab.git
cd finance_lab
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
PYTHONPATH=stock_strategy:. python3 -m unittest discover -s stock_strategy/tests
```

`data/`、`reports/`、`tmp/`、`.venv/` 不纳入 Git，需要在新机器上重新生成。

## 风险与限制

- 历史回测主要是日线收盘代理，不是历史 14:50 盘口回放。
- 当前股票池存在幸存者偏差。
- 重叠 5 日信号复利不是严格的资金容量约束组合净值。
- 公共行情接口没有 SLA，尾盘可能超时或限流。
- 输出是研究候选，不构成投资建议。
