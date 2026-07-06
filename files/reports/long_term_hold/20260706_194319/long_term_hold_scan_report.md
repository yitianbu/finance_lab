# 长期持有跑赢大盘策略扫描

- Generated at: 2026-07-06T19:43:43
- Benchmark: 000300.SH
- Scanned: 4735
- Candidates: 8
- Target behavior: hold for months, trade rarely, stay only while relative strength is intact.

## 买入规则

- 长期趋势：收盘价在 MA200 上方，且 MA60 > MA120 > MA200
- 跑赢大盘：120 日超额收益不低于 6.00%，240 日超额收益不低于 8.00%
- 风险过滤：120 日回撤不深于 -28.00%，年化波动不高于 42.00%
- 买点：信号收盘价下方 3.00% 到上方 3.00% 之间分批建仓

## 卖出规则

- 初始止损：买入价下方 12.00% 或 MA200 下方 3.00%，取更高者
- 趋势卖点：持有满 60 个交易日后，收盘跌破 MA200 下方缓冲线
- 跑输卖点：60 日超额收益低于 -6.00% 且收盘跌破 MA120
- 回撤卖点：浮盈超过 25.00% 后，从最高收盘回撤 15.00%

## 通过候选

| Code | Name | Score | Close | Stock 120D | Benchmark 120D | Excess 120D | Buy Zone | Initial Stop | Trend Stop | Tags |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---|
| 603259.SH | 药明康德 | 97.32 | 122.97 | 38.07% | 4.58% | 33.49% | 119.28-126.66 | 108.21 | 95.67 | long_term_hold,strong_relative,shallow_drawdown |
| 002458.SZ | 益生股份 | 96.90 | 9.45 | 45.88% | 4.58% | 41.30% | 9.17-9.73 | 8.32 | 7.16 | long_term_hold,strong_relative,shallow_drawdown |
| 002832.SZ | 比音勒芬 | 96.59 | 20.92 | 46.70% | 4.58% | 42.12% | 20.29-21.55 | 18.41 | 15.94 | long_term_hold,strong_relative,shallow_drawdown |
| 603995.SH | 甬金股份 | 94.91 | 23.58 | 34.13% | 4.58% | 29.55% | 22.87-24.29 | 20.75 | 17.76 | long_term_hold,strong_relative,shallow_drawdown |
| 603990.SH | 麦迪科技 | 93.02 | 23.00 | 51.62% | 4.58% | 47.03% | 22.31-23.69 | 20.24 | 15.75 | long_term_hold,strong_relative,shallow_drawdown |
| 002293.SZ | 罗莱生活 | 91.67 | 11.24 | 14.11% | 4.58% | 9.53% | 10.90-11.58 | 9.89 | 9.16 | long_term_hold,strong_relative,shallow_drawdown |
| 002972.SZ | 科安达 | 90.61 | 18.95 | 60.58% | 4.58% | 56.00% | 18.38-19.52 | 16.68 | 12.33 | long_term_hold,strong_relative,shallow_drawdown |
| 603558.SH | 健盛集团 | 76.08 | 12.10 | 11.07% | 4.58% | 6.49% | 11.74-12.46 | 11.22 | 11.22 | long_term_hold |

## 观察/拒绝

| Code | Name | Status | Score | Reason |
|---|---|---|---:|---|
| 301046.SZ | 能辉科技 | ok | 88.13 | ma120_not_above_ma200; volatility_120d 61.29% > 42.00% |
| 002468.SZ | 申通快递 | ok | 87.42 | ma120_not_above_ma200; volatility_120d 42.69% > 42.00% |
| 688173.SH | 希荻微 | ok | 85.98 | volatility_120d 48.40% > 42.00% |
| 000938.SZ | 紫光股份 | ok | 85.67 | volatility_120d 51.59% > 42.00% |
| 002861.SZ | 瀛通通讯 | ok | 85.40 | ma60_not_above_ma120; ma120_not_above_ma200; volatility_120d 43.71% > 42.00% |
| 002266.SZ | 浙富控股 | ok | 85.34 | volatility_120d 44.87% > 42.00% |
| 002860.SZ | 星帅尔 | ok | 85.32 | ma60_not_above_ma120; ma120_not_above_ma200; volatility_120d 44.83% > 42.00% |
| 300199.SZ | 翰宇药业 | ok | 85.19 | ma120_not_above_ma200; volatility_120d 54.71% > 42.00% |
| 600222.SH | 太龙药业 | ok | 85.09 | volatility_120d 45.82% > 42.00% |
| 301356.SZ | 天振股份 | ok | 84.91 | volatility_120d 51.67% > 42.00% |
| 688653.SH | 康希通信 | ok | 84.87 | volatility_120d 45.56% > 42.00% |
| 300596.SZ | 利安隆 | ok | 84.56 | ma60_not_above_ma120; volatility_120d 54.22% > 42.00% |
| 688175.SH | 高凌信息 | ok | 84.49 | volatility_120d 55.16% > 42.00% |
| 603301.SH | 振德医疗 | ok | 84.42 | volatility_120d 45.34% > 42.00% |
| 000301.SZ | 东方盛虹 | ok | 84.30 | volatility_120d 45.87% > 42.00% |
| 688131.SH | 皓元医药 | ok | 84.26 | ma120_not_above_ma200; volatility_120d 51.49% > 42.00% |
| 001287.SZ | 中电港 | ok | 84.25 | volatility_120d 58.49% > 42.00% |
| 300145.SZ | 南方泵业 | ok | 84.25 | volatility_120d 62.48% > 42.00% |
| 603375.SH | 盛景微 | ok | 84.23 | volatility_120d 48.53% > 42.00% |
| 688168.SH | 安博通 | ok | 84.20 | ma120_not_above_ma200; volatility_120d 60.15% > 42.00% |
| 688209.SH | 英集芯 | ok | 84.05 | volatility_120d 54.64% > 42.00% |
| 301305.SZ | 朗坤科技 | ok | 83.85 | volatility_120d 50.16% > 42.00% |
| 603638.SH | 艾迪精密 | ok | 83.85 | volatility_120d 46.27% > 42.00% |
| 600428.SH | 中远海特 | ok | 83.75 | volatility_120d 42.32% > 42.00% |
| 688206.SH | 概伦电子 | ok | 83.60 | ma120_not_above_ma200; volatility_120d 66.28% > 42.00% |
| 301555.SZ | 惠柏新材 | ok | 83.52 | volatility_120d 49.66% > 42.00% |
| 688262.SH | 国芯科技 | ok | 83.52 | volatility_120d 66.01% > 42.00% |
| 301029.SZ | 怡合达 | ok | 83.49 | volatility_120d 48.08% > 42.00% |
| 688202.SH | 美迪西 | ok | 83.30 | volatility_120d 56.94% > 42.00% |
| 600601.SH | 方正科技 | ok | 83.28 | volatility_120d 56.69% > 42.00% |
| 300018.SZ | 中元股份 | ok | 83.27 | volatility_120d 65.08% > 42.00% |
| 600400.SH | 红豆股份 | ok | 83.24 | ma120_not_above_ma200; volatility_120d 47.90% > 42.00% |
| 600546.SH | 山煤国际 | ok | 83.22 | volatility_120d 43.43% > 42.00% |
| 603713.SH | 密尔克卫 | ok | 83.18 | ma60_not_above_ma120; volatility_120d 50.32% > 42.00% |
| 688057.SH | 金达莱 | ok | 83.08 | volatility_120d 43.34% > 42.00% |
| 002648.SZ | 卫星化学 | ok | 83.07 | volatility_120d 54.79% > 42.00% |
| 002838.SZ | 道恩股份 | ok | 83.06 | volatility_120d 48.46% > 42.00% |
| 605208.SH | 永茂泰 | ok | 83.04 | volatility_120d 43.08% > 42.00% |
| 603867.SH | 新化股份 | ok | 83.02 | volatility_120d 52.57% > 42.00% |
| 300560.SZ | 中富通 | ok | 83.02 | volatility_120d 61.21% > 42.00% |
| 603257.SH | 中国瑞林 | ok | 83.01 | ma120_not_above_ma200; volatility_120d 50.28% > 42.00% |
| 300969.SZ | 恒帅股份 | ok | 82.98 | volatility_120d 62.07% > 42.00% |
| 688710.SH | 益诺思 | ok | 82.97 | volatility_120d 69.25% > 42.00% |
| 688248.SH | 南网科技 | ok | 82.89 | volatility_120d 61.51% > 42.00% |
| 300836.SZ | 佰奥智能 | ok | 82.84 | volatility_120d 62.91% > 42.00% |
| 300041.SZ | 回天新材 | ok | 82.80 | volatility_120d 46.77% > 42.00% |
| 688601.SH | 力芯微 | ok | 82.77 | volatility_120d 60.13% > 42.00% |
| 300214.SZ | 日科化学 | ok | 82.73 | volatility_120d 52.41% > 42.00% |
| 300689.SZ | 澄天伟业 | ok | 82.70 | volatility_120d 63.38% > 42.00% |
| 688103.SH | 国力电子 | ok | 82.55 | ma120_not_above_ma200; volatility_120d 56.26% > 42.00% |
| 688678.SH | 福立旺 | ok | 82.50 | volatility_120d 56.20% > 42.00% |
| 688578.SH | 艾力斯 | ok | 82.49 | ma60_not_above_ma120; ma120_not_above_ma200; volatility_120d 46.57% > 42.00% |
| 600499.SH | 科达制造 | ok | 82.47 | volatility_120d 54.09% > 42.00% |
| 600366.SH | 宁波韵升 | ok | 82.45 | ma60_not_above_ma120; ma120_not_above_ma200; volatility_120d 47.35% > 42.00% |
| 002072.SZ | 凯瑞德 | ok | 82.35 | volatility_120d 55.76% > 42.00% |
| 300487.SZ | 蓝晓科技 | ok | 82.34 | ma60_not_above_ma120; volatility_120d 59.66% > 42.00% |
| 000060.SZ | 中金岭南 | ok | 82.34 | volatility_120d 63.50% > 42.00% |
| 688220.SH | 翱捷科技 | ok | 82.31 | ma120_not_above_ma200; volatility_120d 71.30% > 42.00% |
| 603012.SH | 创力集团 | ok | 82.29 | volatility_120d 51.90% > 42.00% |
| 300499.SZ | 高澜股份 | ok | 82.22 | volatility_120d 76.42% > 42.00% |
| 002850.SZ | 科达利 | ok | 82.21 | volatility_120d 50.57% > 42.00% |
| 301382.SZ | 蜂助手 | ok | 82.21 | volatility_120d 63.30% > 42.00% |
| 002001.SZ | 新和成 | ok | 82.21 | volatility_120d 44.53% > 42.00% |
| 002079.SZ | 苏州固锝 | ok | 82.20 | volatility_120d 42.28% > 42.00% |
| 002871.SZ | 伟隆股份 | ok | 82.20 | volatility_120d 55.54% > 42.00% |
| 603020.SH | 爱普股份 | ok | 82.19 | volatility_120d 54.81% > 42.00% |
| 603682.SH | 锦和商管 | ok | 82.15 | volatility_120d 61.13% > 42.00% |
| 001326.SZ | 联域股份 | ok | 82.13 | volatility_120d 58.28% > 42.00% |
| 300568.SZ | 星源材质 | ok | 82.12 | volatility_120d 52.36% > 42.00% |
| 603127.SH | 昭衍新药 | ok | 82.09 | volatility_120d 58.53% > 42.00% |
| 603281.SH | 江瀚新材 | ok | 82.09 | volatility_120d 51.25% > 42.00% |
| 000620.SZ | 盈新发展 | ok | 82.06 | ma60_not_above_ma120; volatility_120d 66.52% > 42.00% |
| 000783.SZ | 长江证券 | ok | 82.05 | ma120_not_above_ma200; volatility_120d 49.24% > 42.00% |
| 688135.SH | 利扬芯片 | ok | 82.04 | volatility_120d 72.77% > 42.00% |
| 300557.SZ | 理工光科 | ok | 82.03 | volatility_120d 59.77% > 42.00% |
| 301360.SZ | 荣旗科技 | ok | 81.95 | volatility_120d 64.26% > 42.00% |
| 601233.SH | 桐昆股份 | ok | 81.94 | volatility_120d 60.96% > 42.00% |
| 002925.SZ | 盈趣科技 | ok | 81.90 | volatility_120d 45.48% > 42.00% |
| 688178.SH | 万德斯 | ok | 81.90 | volatility_120d 54.61% > 42.00% |
| 301280.SZ | 珠城科技 | ok | 81.80 | volatility_120d 52.58% > 42.00% |
| 688558.SH | 国盛智科 | ok | 81.77 | volatility_120d 49.61% > 42.00% |
| 301252.SZ | 同星科技 | ok | 81.72 | volatility_120d 62.42% > 42.00% |
| 301489.SZ | 思泉新材 | ok | 81.66 | ma120_not_above_ma200; volatility_120d 71.52% > 42.00% |
| 605098.SH | 行动教育 | ok | 81.62 | volatility_120d 44.41% > 42.00% |
| 603916.SH | 苏博特 | ok | 81.61 | volatility_120d 62.16% > 42.00% |
| 601339.SH | 百隆东方 | ok | 81.61 | volatility_120d 47.92% > 42.00% |
| 300966.SZ | 共同药业 | ok | 81.55 | volatility_120d 44.69% > 42.00% |
| 002643.SZ | 万润股份 | ok | 81.54 | volatility_120d 46.97% > 42.00% |
| 300931.SZ | 通用电梯 | ok | 81.49 | volatility_120d 60.32% > 42.00% |
| 002745.SZ | 木林森 | ok | 81.47 | volatility_120d 50.02% > 42.00% |
| 688512.SH | 慧智微 | ok | 81.37 | volatility_120d 63.59% > 42.00% |
| 001256.SZ | 炜冈科技 | ok | 81.36 | volatility_120d 43.45% > 42.00% |
| 301237.SZ | 和顺科技 | ok | 81.35 | volatility_120d 72.22% > 42.00% |
| 688325.SH | 赛微微电 | ok | 81.34 | volatility_120d 69.51% > 42.00% |
| 300491.SZ | 通合科技 | ok | 81.34 | ma120_not_above_ma200; volatility_120d 60.99% > 42.00% |
| 301031.SZ | 中熔电气 | ok | 81.33 | volatility_120d 62.88% > 42.00% |
| 605298.SH | 必得科技 | ok | 81.31 | volatility_120d 53.30% > 42.00% |
| 300878.SZ | 维康药业 | ok | 81.29 | volatility_120d 72.86% > 42.00% |
| 600078.SH | 澄星股份 | ok | 81.25 | volatility_120d 71.92% > 42.00% |
| 603032.SH | 德新科技 | ok | 81.24 | ma120_not_above_ma200; volatility_120d 55.52% > 42.00% |
| 002638.SZ | 勤上股份 | ok | 81.20 | volatility_120d 51.60% > 42.00% |
| 601001.SH | 晋控煤业 | ok | 81.14 | volatility_120d 46.71% > 42.00% |
| 300467.SZ | 迅游科技 | ok | 81.07 | volatility_120d 57.61% > 42.00% |
| 002559.SZ | 亚威股份 | ok | 81.07 | ma120_not_above_ma200; volatility_120d 52.73% > 42.00% |
| 603290.SH | 斯达半导 | ok | 81.04 | volatility_120d 56.44% > 42.00% |
| 600236.SH | 桂冠电力 | ok | 81.03 | volatility_120d 53.90% > 42.00% |
| 300483.SZ | 首华燃气 | ok | 81.02 | volatility_120d 78.49% > 42.00% |
| 002126.SZ | 银轮股份 | ok | 81.01 | volatility_120d 58.02% > 42.00% |
| 002654.SZ | 万润科技 | ok | 80.99 | volatility_120d 64.03% > 42.00% |
| 301111.SZ | 粤万年青 | ok | 80.99 | volatility_120d 73.74% > 42.00% |
| 002452.SZ | 长高电气 | ok | 80.96 | volatility_120d 50.15% > 42.00% |
| 002955.SZ | 鸿合科技 | ok | 80.87 | ma120_not_above_ma200 |
| 600392.SH | 盛和资源 | ok | 80.87 | volatility_120d 68.22% > 42.00% |
| 300488.SZ | 恒锋工具 | ok | 80.84 | volatility_120d 67.66% > 42.00% |
| 301028.SZ | 鼎熔岩 | ok | 80.84 | volatility_120d 57.27% > 42.00% |
| 688580.SH | 伟思医疗 | ok | 80.84 | ma60_not_above_ma120; volatility_120d 55.76% > 42.00% |
| 600459.SH | 贵研铂业 | ok | 80.82 | volatility_120d 67.32% > 42.00% |
| 002272.SZ | 川润股份 | ok | 80.75 | volatility_120d 70.12% > 42.00% |
| 605288.SH | 凯迪股份 | ok | 80.73 | ma60_not_above_ma120; volatility_120d 72.57% > 42.00% |
| 000782.SZ | 恒申新材 | ok | 80.72 | volatility_120d 51.65% > 42.00% |
| 301122.SZ | 采纳股份 | ok | 80.67 | ma60_not_above_ma120; volatility_120d 49.14% > 42.00% |
| 603685.SH | 晨丰科技 | ok | 80.66 | volatility_120d 54.46% > 42.00% |
| 603976.SH | 正川股份 | ok | 80.66 | volatility_120d 49.34% > 42.00% |
| 002317.SZ | 众生药业 | ok | 80.63 | volatility_120d 50.42% > 42.00% |
| 002443.SZ | 金洲管道 | ok | 80.62 | volatility_120d 50.33% > 42.00% |
| 603135.SH | 中重科技 | ok | 80.61 | volatility_120d 56.50% > 42.00% |
| 000571.SZ | 新大洲A | ok | 80.60 | ma60_not_above_ma120; volatility_120d 58.40% > 42.00% |
| 688207.SH | 格灵深瞳 | ok | 80.59 | volatility_120d 72.74% > 42.00% |
| 000048.SZ | 京基智农 | ok | 80.51 | ma60_not_above_ma120; volatility_120d 67.53% > 42.00% |
| 601699.SH | 潞安环能 | ok | 80.49 | volatility_120d 49.00% > 42.00% |
| 603937.SH | 丽岛新材 | ok | 80.45 | volatility_120d 56.37% > 42.00% |
| 300001.SZ | 特锐德 | ok | 80.45 | volatility_120d 51.45% > 42.00% |
| 688331.SH | 荣昌生物 | ok | 80.31 | volatility_120d 71.27% > 42.00% |
| 688620.SH | 安凯微 | ok | 80.31 | volatility_120d 47.84% > 42.00% |
| 002803.SZ | 吉宏股份 | ok | 80.29 | volatility_120d 49.77% > 42.00% |
| 301418.SZ | 协昌科技 | ok | 80.24 | volatility_120d 53.52% > 42.00% |
| 600114.SH | 东睦股份 | ok | 80.20 | volatility_120d 53.32% > 42.00% |
| 603110.SH | 东方材料 | ok | 80.17 | volatility_120d 53.34% > 42.00% |
| 603137.SH | 恒尚节能 | ok | 80.14 | ma60_not_above_ma120; ma120_not_above_ma200 |
| 688046.SH | 药康生物 | ok | 80.11 | volatility_120d 51.41% > 42.00% |
| 301286.SZ | 侨源股份 | ok | 80.10 | volatility_120d 73.15% > 42.00% |
| 301372.SZ | 科净源 | ok | 80.08 | volatility_120d 45.68% > 42.00% |
| 603162.SH | 海通发展 | ok | 80.08 | volatility_120d 48.14% > 42.00% |
| 002963.SZ | 豪尔赛 | ok | 80.06 | volatility_120d 56.79% > 42.00% |
| 603165.SH | 荣晟环保 | ok | 80.06 | volatility_120d 55.35% > 42.00% |
| 605305.SH | 中际联合 | ok | 80.06 | volatility_120d 48.02% > 42.00% |
| 688508.SH | 芯朋微 | ok | 80.02 | volatility_120d 58.25% > 42.00% |
| 002025.SZ | 航天电器 | ok | 80.00 | volatility_120d 73.50% > 42.00%; distance_ma200 61.57% > 55.00% |
| 603211.SH | 晋拓股份 | ok | 80.00 | volatility_120d 63.69% > 42.00%; distance_ma200 69.49% > 55.00% |
| 300684.SZ | 中石科技 | ok | 80.00 | volatility_120d 70.25% > 42.00% |
| 688686.SH | 奥普特 | ok | 80.00 | ma120_not_above_ma200; volatility_120d 53.39% > 42.00% |
| 688061.SH | 灿瑞科技 | ok | 80.00 | volatility_120d 46.13% > 42.00% |
| 603823.SH | 百合花 | ok | 79.99 | volatility_120d 65.24% > 42.00%; distance_ma200 225.63% > 55.00% |
| 002135.SZ | 东南网架 | ok | 79.96 | drawdown_120d -30.67% < -28.00%; volatility_120d 57.27% > 42.00% |
| 603726.SH | 朗迪集团 | ok | 79.95 | volatility_120d 54.84% > 42.00% |
| 688433.SH | 华曙高科 | ok | 79.94 | drawdown_120d -35.25% < -28.00%; volatility_120d 73.73% > 42.00% |
| 688336.SH | 三生国健 | ok | 79.93 | volatility_120d 68.45% > 42.00% |
| 688041.SH | 海光信息 | ok | 79.92 | volatility_120d 64.73% > 42.00% |
| 600673.SH | 东阳光 | ok | 79.85 | volatility_120d 71.30% > 42.00% |
| 603725.SH | 天安新材 | ok | 79.83 | volatility_120d 53.06% > 42.00% |
| 300316.SZ | 晶盛机电 | ok | 79.83 | volatility_120d 80.54% > 42.00% |
| 000960.SZ | 锡业股份 | ok | 79.83 | volatility_120d 78.26% > 42.00% |
| 002429.SZ | 兆驰股份 | ok | 79.82 | volatility_120d 73.26% > 42.00% |
| 002653.SZ | 海思科 | ok | 79.81 | ma120_not_above_ma200; volatility_120d 55.40% > 42.00% |
| 300440.SZ | 运达科技 | ok | 79.80 | volatility_120d 52.82% > 42.00% |
| 300849.SZ | 锦盛新材 | ok | 79.79 | volatility_120d 64.30% > 42.00% |
| 301191.SZ | 菲菱科思 | ok | 79.79 | volatility_120d 88.72% > 42.00%; distance_ma200 56.08% > 55.00% |
| 603379.SH | 三美股份 | ok | 79.74 | ma60_not_above_ma120; volatility_120d 51.65% > 42.00% |
| 300786.SZ | 国林科技 | ok | 79.71 | volatility_120d 44.67% > 42.00% |
| 300990.SZ | 同飞股份 | ok | 79.70 | volatility_120d 66.37% > 42.00% |
| 300461.SZ | 田中精机 | ok | 79.70 | drawdown_120d -48.07% < -28.00%; volatility_120d 96.96% > 42.00% |
| 601179.SH | 中国西电 | ok | 79.68 | drawdown_120d -31.93% < -28.00%; volatility_120d 64.54% > 42.00% |
| 600482.SH | 中国动力 | ok | 79.68 | volatility_120d 62.84% > 42.00% |
| 603530.SH | 神马电力 | ok | 79.67 | volatility_120d 50.19% > 42.00% |
| 688258.SH | 卓易信息 | ok | 79.66 | drawdown_120d -34.97% < -28.00%; volatility_120d 93.15% > 42.00% |
| 002580.SZ | 圣阳股份 | ok | 79.66 | drawdown_120d -47.28% < -28.00%; volatility_120d 79.17% > 42.00% |
| 688291.SH | 金橙子 | ok | 79.65 | volatility_120d 69.44% > 42.00% |
| 301081.SZ | 严牌股份 | ok | 79.64 | drawdown_120d -33.36% < -28.00%; volatility_120d 66.74% > 42.00% |
| 301087.SZ | 可孚医疗 | ok | 79.64 | ma60_not_above_ma120; volatility_120d 44.31% > 42.00% |
| 300812.SZ | 易天股份 | ok | 79.64 | drawdown_120d -29.26% < -28.00%; volatility_120d 80.52% > 42.00% |
| 688002.SH | 睿创微纳 | ok | 79.63 | volatility_120d 55.55% > 42.00% |
| 603757.SH | 大元泵业 | ok | 79.61 | volatility_120d 77.93% > 42.00%; distance_ma200 66.01% > 55.00% |
| 300816.SZ | 艾可蓝 | ok | 79.57 | drawdown_120d -34.05% < -28.00%; volatility_120d 77.49% > 42.00% |
| 600791.SH | 京能置业 | ok | 79.57 | drawdown_120d -50.11% < -28.00%; volatility_120d 73.81% > 42.00% |
| 600188.SH | 兖矿能源 | ok | 79.57 | drawdown_120d -32.37% < -28.00%; volatility_120d 55.45% > 42.00% |
| 300442.SZ | 润泽科技 | ok | 79.56 | volatility_120d 78.59% > 42.00% |
| 002132.SZ | 恒星科技 | ok | 79.56 | volatility_120d 50.00% > 42.00% |
| 002913.SZ | 奥士康 | ok | 79.55 | volatility_120d 60.91% > 42.00% |
| 300970.SZ | 华绿生物 | ok | 79.54 | drawdown_120d -49.22% < -28.00%; volatility_120d 62.03% > 42.00% |
| 600703.SH | 三安光电 | ok | 79.53 | volatility_120d 72.77% > 42.00% |
| 688182.SH | 灿勤科技 | ok | 79.51 | volatility_120d 64.82% > 42.00% |
| 600172.SH | 黄河旋风 | ok | 79.51 | volatility_120d 81.37% > 42.00%; distance_ma200 121.61% > 55.00% |
| 300303.SZ | 聚飞光电 | ok | 79.50 | drawdown_120d -28.45% < -28.00%; volatility_120d 72.70% > 42.00% |
| 300617.SZ | 安靠智电 | ok | 79.50 | drawdown_120d -30.22% < -28.00%; volatility_120d 82.44% > 42.00% |
| 300679.SZ | 电连技术 | ok | 79.49 | ma120_not_above_ma200; volatility_120d 65.72% > 42.00% |
| 300304.SZ | 云意电气 | ok | 79.45 | volatility_120d 54.81% > 42.00% |
| 603353.SH | 和顺石油 | ok | 79.44 | drawdown_120d -37.82% < -28.00%; volatility_120d 80.28% > 42.00% |
| 688191.SH | 智洋创新 | ok | 79.44 | drawdown_120d -28.37% < -28.00%; volatility_120d 77.99% > 42.00% |
| 600237.SH | 铜峰电子 | ok | 79.43 | volatility_120d 65.12% > 42.00% |
| 002647.SZ | 仁东控股 | ok | 79.42 | volatility_120d 59.13% > 42.00% |
| 002774.SZ | 快意电梯 | ok | 79.42 | volatility_120d 57.73% > 42.00% |
| 688141.SH | 杰华特 | ok | 79.41 | volatility_120d 85.74% > 42.00%; distance_ma200 160.47% > 55.00% |
| 600162.SH | 香江控股 | ok | 79.40 | drawdown_120d -41.45% < -28.00%; volatility_120d 62.86% > 42.00% |
| 688611.SH | 杭州柯林 | ok | 79.40 | volatility_120d 56.15% > 42.00% |
| 301222.SZ | 浙江恒威 | ok | 79.40 | volatility_120d 70.22% > 42.00% |
| 600228.SH | 返利科技 | ok | 79.39 | drawdown_120d -41.70% < -28.00%; volatility_120d 56.30% > 42.00% |
| 300715.SZ | 凯伦股份 | ok | 79.37 | drawdown_120d -44.32% < -28.00%; volatility_120d 69.19% > 42.00% |
| 300083.SZ | 创世纪 | ok | 79.34 | ma120_not_above_ma200; volatility_120d 63.69% > 42.00% |
| 000534.SZ | 万泽股份 | ok | 79.33 | drawdown_120d -33.88% < -28.00%; volatility_120d 82.46% > 42.00% |
| 688125.SH | 安达智能 | ok | 79.33 | ma60_not_above_ma120; drawdown_120d -42.54% < -28.00%; volatility_120d 84.27% > 42.00% |
| 603335.SH | 迪生力 | ok | 79.32 | volatility_120d 61.46% > 42.00% |
| 688087.SH | 英科再生 | ok | 79.32 | volatility_120d 53.11% > 42.00% |
| 300657.SZ | 弘信电子 | ok | 79.31 | drawdown_120d -34.72% < -28.00%; volatility_120d 72.12% > 42.00% |
| 688480.SH | 赛恩斯 | ok | 79.30 | drawdown_120d -47.16% < -28.00%; volatility_120d 91.19% > 42.00% |
| 002213.SZ | 大为股份 | ok | 79.30 | volatility_120d 63.75% > 42.00% |
| 603985.SH | 恒润股份 | ok | 79.29 | volatility_120d 57.63% > 42.00% |
| 605100.SH | 华丰股份 | ok | 79.26 | volatility_120d 45.93% > 42.00% |
| 002150.SZ | 正泰电源 | ok | 79.24 | drawdown_120d -31.87% < -28.00%; volatility_120d 68.02% > 42.00% |
| 301363.SZ | 美好医疗 | ok | 79.21 | ma60_not_above_ma120; drawdown_120d -29.68% < -28.00%; volatility_120d 73.38% > 42.00% |
| 300592.SZ | 华凯易佰 | ok | 79.19 | volatility_120d 66.79% > 42.00% |
| 301365.SZ | 矩阵股份 | ok | 79.18 | volatility_120d 53.90% > 42.00% |
| 001331.SZ | 胜通能源 | ok | 79.16 | volatility_120d 80.26% > 42.00%; distance_ma200 171.04% > 55.00% |
| 300905.SZ | 宝丽迪 | ok | 79.16 | drawdown_120d -42.68% < -28.00%; volatility_120d 73.62% > 42.00% |
| 301218.SZ | 华是科技 | ok | 79.14 | volatility_120d 72.38% > 42.00% |
| 300561.SZ | 汇金科技 | ok | 79.12 | drawdown_120d -29.00% < -28.00%; volatility_120d 107.57% > 42.00% |
| 002380.SZ | 科远智慧 | ok | 79.12 | drawdown_120d -32.08% < -28.00%; volatility_120d 55.60% > 42.00% |
| 002848.SZ | 高斯贝尔 | ok | 79.10 | volatility_120d 48.02% > 42.00% |
| 688231.SH | 隆达股份 | ok | 79.06 | volatility_120d 67.00% > 42.00%; distance_ma200 82.56% > 55.00% |
| 688319.SH | 欧林生物 | ok | 79.02 | volatility_120d 70.77% > 42.00% |
| 300602.SZ | 飞荣达 | ok | 79.01 | volatility_120d 67.23% > 42.00% |
| 688697.SH | 纽威数控 | ok | 79.01 | volatility_120d 57.75% > 42.00% |
| 002993.SZ | 奥海科技 | ok | 79.00 | volatility_120d 64.60% > 42.00% |
| 300731.SZ | 科创新源 | ok | 78.97 | volatility_120d 76.09% > 42.00% |
| 300097.SZ | 智云股份 | ok | 78.96 | volatility_120d 56.79% > 42.00% |
| 002273.SZ | 水晶光电 | ok | 78.96 | volatility_120d 64.79% > 42.00% |
| 002606.SZ | 大连电瓷 | ok | 78.96 | volatility_120d 60.66% > 42.00% |
| 688221.SH | 前沿生物 | ok | 78.94 | ma60_not_above_ma120; volatility_120d 77.00% > 42.00% |
| 603078.SH | 江化微 | ok | 78.92 | volatility_120d 64.24% > 42.00%; distance_ma200 130.69% > 55.00% |
| 002921.SZ | 联诚精密 | ok | 78.91 | volatility_120d 55.63% > 42.00% |
| 603268.SH | 松发股份 | ok | 78.90 | volatility_120d 54.67% > 42.00%; distance_ma200 65.97% > 55.00% |
| 300671.SZ | 富满微 | ok | 78.90 | volatility_120d 82.56% > 42.00%; distance_ma200 138.03% > 55.00% |
| 002353.SZ | 杰瑞股份 | ok | 78.89 | volatility_120d 66.90% > 42.00%; distance_ma200 83.18% > 55.00% |
| 600160.SH | 巨化股份 | ok | 78.89 | volatility_120d 51.95% > 42.00% |
| 002768.SZ | 国恩股份 | ok | 78.88 | volatility_120d 44.27% > 42.00% |
| 688183.SH | 生益电子 | ok | 78.86 | volatility_120d 73.80% > 42.00% |
| 688559.SH | 海目星 | ok | 78.86 | volatility_120d 65.10% > 42.00% |
| 603308.SH | 应流股份 | ok | 78.84 | volatility_120d 64.17% > 42.00% |
| 300057.SZ | 万顺新材 | ok | 78.83 | volatility_120d 61.60% > 42.00% |
| 301603.SZ | 乔锋智能 | ok | 78.82 | volatility_120d 72.36% > 42.00%; distance_ma200 76.65% > 55.00% |
| 301323.SZ | 新莱福 | ok | 78.81 | drawdown_120d -32.68% < -28.00%; volatility_120d 65.42% > 42.00% |
| 301307.SZ | 美利信 | ok | 78.81 | volatility_120d 71.14% > 42.00%; distance_ma200 104.51% > 55.00% |
| 600184.SH | 光电股份 | ok | 78.78 | drawdown_120d -29.33% < -28.00%; volatility_120d 67.46% > 42.00% |
| 601636.SH | 旗滨集团 | ok | 78.77 | volatility_120d 62.23% > 42.00% |
| 603010.SH | 万盛股份 | ok | 78.77 | volatility_120d 51.10% > 42.00% |
| 688733.SH | 壹石通 | ok | 78.74 | volatility_120d 60.25% > 42.00% |
| 688390.SH | 固德威 | ok | 78.74 | drawdown_120d -44.63% < -28.00%; volatility_120d 71.72% > 42.00% |
| 688400.SH | 凌云光 | ok | 78.73 | volatility_120d 72.08% > 42.00% |
| 002245.SZ | 蔚蓝锂芯 | ok | 78.71 | volatility_120d 56.73% > 42.00%; distance_ma200 63.85% > 55.00% |
| 688107.SH | 安路科技 | ok | 78.71 | volatility_120d 64.64% > 42.00% |
| 688511.SH | 天微电子 | ok | 78.71 | volatility_120d 63.12% > 42.00% |
| 300497.SZ | 富祥股份 | ok | 78.69 | volatility_120d 58.61% > 42.00% |
| 301051.SZ | 信濠光电 | ok | 78.69 | volatility_120d 66.54% > 42.00% |
| 601678.SH | 滨化股份 | ok | 78.68 | volatility_120d 59.93% > 42.00% |
| 301273.SZ | 瑞晨环保 | ok | 78.65 | volatility_120d 48.65% > 42.00% |
| 002536.SZ | 飞龙股份 | ok | 78.65 | volatility_120d 75.72% > 42.00%; distance_ma200 75.07% > 55.00% |
| 300246.SZ | 宝莱特 | ok | 78.65 | drawdown_120d -33.35% < -28.00%; volatility_120d 81.89% > 42.00% |
| 603306.SH | 华懋科技 | ok | 78.64 | volatility_120d 64.32% > 42.00% |
| 688072.SH | 拓荆科技 | ok | 78.64 | volatility_120d 67.11% > 42.00%; distance_ma200 121.44% > 55.00% |
| 002943.SZ | 宇晶股份 | ok | 78.62 | drawdown_120d -40.80% < -28.00%; volatility_120d 81.27% > 42.00% |
| 600259.SH | 中稀有色 | ok | 78.61 | volatility_120d 72.73% > 42.00% |
| 603120.SH | 肯特催化 | ok | 78.59 | volatility_120d 59.48% > 42.00% |
| 300184.SZ | 力源信息 | ok | 78.56 | volatility_120d 65.18% > 42.00% |
| 605303.SH | 园林股份 | ok | 78.56 | drawdown_120d -36.96% < -28.00%; volatility_120d 67.78% > 42.00% |
| 301548.SZ | 崇德科技 | ok | 78.55 | volatility_120d 70.70% > 42.00% |
| 300259.SZ | 新天科技 | ok | 78.55 | volatility_120d 72.45% > 42.00% |
| 301282.SZ | 金禄电子 | ok | 78.50 | volatility_120d 72.13% > 42.00% |
| 300861.SZ | 美畅股份 | ok | 78.49 | volatility_120d 62.66% > 42.00% |
| 002979.SZ | 雷赛智能 | ok | 78.49 | volatility_120d 49.82% > 42.00%; distance_ma200 64.37% > 55.00% |
| 002440.SZ | 闰土股份 | ok | 78.46 | ma60_not_above_ma120; drawdown_120d -32.14% < -28.00%; volatility_120d 64.28% > 42.00% |
| 603067.SH | 振华股份 | ok | 78.46 | volatility_120d 80.64% > 42.00% |
| 301588.SZ | 美新科技 | ok | 78.46 | volatility_120d 73.74% > 42.00%; distance_ma200 108.96% > 55.00% |
| 688222.SH | 成都先导 | ok | 78.44 | ma60_not_above_ma120; volatility_120d 62.36% > 42.00% |
| 000751.SZ | 锌业股份 | ok | 78.43 | ma60_not_above_ma120; drawdown_120d -32.39% < -28.00%; volatility_120d 72.86% > 42.00% |
| 002965.SZ | 祥鑫科技 | ok | 78.41 | ma120_not_above_ma200; volatility_120d 49.27% > 42.00% |
| 000951.SZ | 中国重汽 | ok | 78.38 | volatility_120d 47.31% > 42.00% |
| 600531.SH | 豫光金铅 | ok | 78.38 | ma60_not_above_ma120; drawdown_120d -41.23% < -28.00%; volatility_120d 73.30% > 42.00% |
| 603226.SH | 菲林格尔 | ok | 78.37 | volatility_120d 59.39% > 42.00% |
| 603155.SH | 新亚强 | ok | 78.36 | volatility_120d 59.61% > 42.00%; distance_ma200 63.36% > 55.00% |
| 001309.SZ | 德明利 | ok | 78.36 | volatility_120d 72.34% > 42.00%; distance_ma200 159.80% > 55.00% |
| 002830.SZ | 名雕股份 | ok | 78.35 | ma60_not_above_ma120; drawdown_120d -34.10% < -28.00%; volatility_120d 70.47% > 42.00% |
| 300953.SZ | 震裕科技 | ok | 78.33 | volatility_120d 59.09% > 42.00% |
| 300985.SZ | 致远新能 | ok | 78.32 | volatility_120d 66.49% > 42.00%; distance_ma200 118.29% > 55.00% |
| 002747.SZ | 埃斯顿 | ok | 78.32 | volatility_120d 53.14% > 42.00%; distance_ma200 85.54% > 55.00% |
| 301095.SZ | 广立微 | ok | 78.31 | volatility_120d 74.35% > 42.00% |
| 603950.SH | 长源东谷 | ok | 78.30 | volatility_120d 79.15% > 42.00%; distance_ma200 102.03% > 55.00% |
| 301295.SZ | 美硕科技 | ok | 78.29 | volatility_120d 53.38% > 42.00% |
| 688372.SH | 伟测科技 | ok | 78.29 | volatility_120d 70.25% > 42.00% |
| 002498.SZ | 汉缆股份 | ok | 78.27 | drawdown_120d -45.28% < -28.00%; volatility_120d 80.25% > 42.00% |
| 605287.SH | 德才股份 | ok | 78.26 | drawdown_120d -34.66% < -28.00%; volatility_120d 80.93% > 42.00% |
| 300084.SZ | 海默科技 | ok | 78.26 | volatility_120d 57.26% > 42.00% |
| 301379.SZ | 天山电子 | ok | 78.25 | volatility_120d 75.90% > 42.00%; distance_ma200 73.47% > 55.00% |
| 300951.SZ | 博硕科技 | ok | 78.25 | volatility_120d 54.54% > 42.00% |
| 002158.SZ | 汉钟精机 | ok | 78.24 | volatility_120d 54.50% > 42.00% |
| 300655.SZ | 晶瑞电材 | ok | 78.21 | ma60_not_above_ma120; volatility_120d 60.51% > 42.00% |
| 601918.SH | 新集能源 | ok | 78.20 | volatility_120d 45.14% > 42.00% |
| 300382.SZ | 斯莱克 | ok | 78.20 | ma120_not_above_ma200; volatility_120d 63.97% > 42.00% |
| 688689.SH | 银河微电 | ok | 78.19 | volatility_120d 77.06% > 42.00%; distance_ma200 148.02% > 55.00% |
| 688156.SH | 路德科技 | ok | 78.18 | volatility_120d 57.94% > 42.00% |
| 603991.SH | 领先股份 | ok | 78.16 | volatility_120d 57.06% > 42.00%; distance_ma200 68.81% > 55.00% |
| 688800.SH | 瑞可达 | ok | 78.14 | volatility_120d 79.07% > 42.00% |
| 002422.SZ | 科伦药业 | ok | 78.13 | ma120_not_above_ma200; volatility_120d 45.76% > 42.00% |
| 301389.SZ | 隆扬电子 | ok | 78.13 | drawdown_120d -35.52% < -28.00%; volatility_120d 72.50% > 42.00% |
| 300503.SZ | 昊志机电 | ok | 78.13 | volatility_120d 78.30% > 42.00%; distance_ma200 111.79% > 55.00% |
| 300162.SZ | 雷曼光电 | ok | 78.11 | volatility_120d 76.78% > 42.00% |
| 600563.SH | 法拉电子 | ok | 78.11 | volatility_120d 63.63% > 42.00% |
| 301018.SZ | 申菱环境 | ok | 78.11 | volatility_120d 83.42% > 42.00%; distance_ma200 91.19% > 55.00% |
| 688469.SH | 芯联集成 | ok | 78.10 | volatility_120d 52.44% > 42.00% |
| 688629.SH | 华丰科技 | ok | 78.10 | volatility_120d 81.05% > 42.00%; distance_ma200 84.53% > 55.00% |
| 000338.SZ | 潍柴动力 | ok | 78.06 | volatility_120d 59.72% > 42.00% |
| 300342.SZ | 天银机电 | ok | 78.04 | drawdown_120d -38.39% < -28.00%; volatility_120d 84.37% > 42.00% |
| 000833.SZ | 粤桂股份 | ok | 78.03 | volatility_120d 67.27% > 42.00% |
| 301165.SZ | 锐捷网络 | ok | 78.02 | volatility_120d 78.46% > 42.00%; distance_ma200 66.50% > 55.00% |
| 600596.SH | 新安股份 | ok | 78.02 | volatility_120d 58.80% > 42.00% |
| 002693.SZ | 双成药业 | ok | 78.00 | volatility_120d 49.91% > 42.00% |
| 600063.SH | 皖维高新 | ok | 77.98 | volatility_120d 58.35% > 42.00% |
| 301053.SZ | 远信工业 | ok | 77.96 | volatility_120d 62.03% > 42.00% |
| 002283.SZ | 天润工业 | ok | 77.96 | volatility_120d 63.83% > 42.00% |
| 301003.SZ | 江苏博云 | ok | 77.95 | volatility_120d 63.64% > 42.00% |
| 603063.SH | 禾望电气 | ok | 77.92 | drawdown_120d -34.09% < -28.00%; volatility_120d 61.80% > 42.00% |
| 603001.SH | 奥康国际 | ok | 77.90 | volatility_120d 66.31% > 42.00% |
| 300821.SZ | 东岳硅材 | ok | 77.89 | volatility_120d 77.42% > 42.00%; distance_ma200 67.42% > 55.00% |
| 301070.SZ | 开勒股份 | ok | 77.85 | volatility_120d 66.67% > 42.00%; distance_ma200 67.37% > 55.00% |
| 000688.SZ | 国城矿业 | ok | 77.85 | drawdown_120d -31.88% < -28.00%; volatility_120d 74.35% > 42.00% |
| 002810.SZ | 山东赫达 | ok | 77.84 | volatility_120d 59.76% > 42.00% |
| 688123.SH | 聚辰股份 | ok | 77.82 | volatility_120d 81.70% > 42.00%; distance_ma200 56.63% > 55.00% |
| 300745.SZ | 欣锐科技 | ok | 77.79 | volatility_120d 68.57% > 42.00%; distance_ma200 65.25% > 55.00% |
| 688380.SH | 中微半导 | ok | 77.76 | volatility_120d 78.26% > 42.00% |
| 688690.SH | 纳微科技 | ok | 77.68 | volatility_120d 62.49% > 42.00% |
| 002240.SZ | 盛新锂能 | ok | 77.68 | drawdown_120d -34.37% < -28.00%; volatility_120d 67.87% > 42.00% |
| 000668.SZ | 荣丰控股 | ok | 77.67 | volatility_120d 53.48% > 42.00%; distance_ma200 62.82% > 55.00% |
| 300943.SZ | 春晖智控 | ok | 77.67 | volatility_120d 92.74% > 42.00%; distance_ma200 85.59% > 55.00% |
| 000518.SZ | 四环生物 | ok | 77.64 | volatility_120d 51.93% > 42.00% |
| 002432.SZ | 九安医疗 | ok | 77.60 | drawdown_120d -32.27% < -28.00%; volatility_120d 73.15% > 42.00% |
| 300163.SZ | 先锋新材 | ok | 77.58 | volatility_120d 72.14% > 42.00%; distance_ma200 66.62% > 55.00% |
| 301486.SZ | 致尚科技 | ok | 77.57 | drawdown_120d -37.67% < -28.00%; volatility_120d 98.13% > 42.00% |
| 002350.SZ | 北京科锐 | ok | 77.57 | volatility_120d 59.77% > 42.00% |
| 600026.SH | 中远海能 | ok | 77.55 | drawdown_120d -36.07% < -28.00%; volatility_120d 68.66% > 42.00% |
| 000551.SZ | 创元科技 | ok | 77.53 | volatility_120d 50.68% > 42.00% |
| 301169.SZ | 零点有数 | ok | 77.52 | drawdown_120d -30.04% < -28.00%; volatility_120d 53.91% > 42.00% |
| 301500.SZ | 飞南资源 | ok | 77.49 | volatility_120d 80.13% > 42.00% |
| 688275.SH | 万润新能 | ok | 77.49 | drawdown_120d -35.61% < -28.00%; volatility_120d 55.79% > 42.00% |
| 002250.SZ | 联化科技 | ok | 77.47 | ma60_not_above_ma120; volatility_120d 47.72% > 42.00% |
| 603150.SH | 万朗磁塑 | ok | 77.47 | volatility_120d 55.38% > 42.00% |
| 002733.SZ | 雄韬股份 | ok | 77.43 | drawdown_120d -33.83% < -28.00%; volatility_120d 71.23% > 42.00% |
| 300438.SZ | 鹏辉能源 | ok | 77.43 | volatility_120d 69.42% > 42.00% |
| 688362.SH | 甬矽电子 | ok | 77.43 | volatility_120d 86.14% > 42.00%; distance_ma200 118.93% > 55.00% |
| 300938.SZ | 信测标准 | ok | 77.42 | volatility_120d 67.69% > 42.00%; distance_ma200 88.64% > 55.00% |
| 688699.SH | 明微电子 | ok | 77.42 | volatility_120d 84.73% > 42.00%; distance_ma200 63.71% > 55.00% |
| 000739.SZ | 普洛药业 | ok | 77.39 | ma60_not_above_ma120 |
| 688097.SH | 博众精工 | ok | 77.37 | volatility_120d 64.80% > 42.00% |
| 301529.SZ | 福赛科技 | ok | 77.37 | volatility_120d 74.16% > 42.00%; distance_ma200 56.69% > 55.00% |
| 600497.SH | 驰宏锌锗 | ok | 77.35 | volatility_120d 67.13% > 42.00% |
| 300873.SZ | 海晨股份 | ok | 77.33 | volatility_120d 60.10% > 42.00%; distance_ma200 84.83% > 55.00% |
| 688345.SH | 博力威 | ok | 77.33 | volatility_120d 65.29% > 42.00% |
| 688448.SH | 磁谷科技 | ok | 77.30 | volatility_120d 55.28% > 42.00% |
| 605117.SH | 德业股份 | ok | 77.27 | volatility_120d 59.15% > 42.00% |
| 601958.SH | 金钼股份 | ok | 77.25 | volatility_120d 71.49% > 42.00% |
| 002937.SZ | 兴瑞科技 | ok | 77.25 | volatility_120d 48.15% > 42.00%; distance_ma200 65.06% > 55.00% |
| 300166.SZ | 东方国信 | ok | 77.24 | volatility_120d 89.61% > 42.00% |
| 688350.SH | 富淼科技 | ok | 77.21 | volatility_120d 70.07% > 42.00% |
| 605186.SH | 健麾信息 | ok | 77.21 | volatility_120d 46.03% > 42.00% |
| 002929.SZ | 润建股份 | ok | 77.19 | drawdown_120d -36.31% < -28.00%; volatility_120d 73.79% > 42.00% |
| 300606.SZ | 金太阳 | ok | 77.19 | volatility_120d 91.70% > 42.00% |
| 688758.SH | 赛分科技 | ok | 77.15 | excess_return_240d 7.85% < 8.00%; volatility_120d 46.83% > 42.00% |
| 605060.SH | 联德股份 | ok | 77.14 | volatility_120d 76.35% > 42.00% |
| 688607.SH | 康众医疗 | ok | 77.14 | drawdown_120d -29.45% < -28.00%; volatility_120d 68.72% > 42.00% |
| 605588.SH | 冠石科技 | ok | 77.13 | volatility_120d 54.29% > 42.00% |
| 300131.SZ | 英唐智控 | ok | 77.12 | volatility_120d 77.62% > 42.00% |
| 603317.SH | 天味食品 | ok | 77.11 | volatility_120d 43.47% > 42.00% |
| 605168.SH | 三人行 | ok | 77.11 | volatility_120d 61.73% > 42.00% |
| 688229.SH | 博睿数据 | ok | 77.08 | drawdown_120d -36.90% < -28.00%; volatility_120d 95.63% > 42.00% |
| 600520.SH | 三佳科技 | ok | 77.05 | volatility_120d 57.14% > 42.00% |
| 688195.SH | 腾景科技 | ok | 77.05 | drawdown_120d -48.52% < -28.00%; volatility_120d 87.80% > 42.00% |
| 000922.SZ | 佳电股份 | ok | 77.05 | volatility_120d 46.06% > 42.00% |
| 688486.SH | 龙迅股份 | ok | 77.03 | volatility_120d 50.16% > 42.00% |
| 000811.SZ | 冰轮环境 | ok | 77.03 | volatility_120d 73.07% > 42.00%; distance_ma200 156.58% > 55.00% |
| 603800.SH | 洪田股份 | ok | 77.03 | volatility_120d 61.69% > 42.00%; distance_ma200 64.44% > 55.00% |
| 300394.SZ | 天孚通信 | ok | 77.02 | drawdown_120d -36.72% < -28.00%; volatility_120d 86.88% > 42.00% |
| 300668.SZ | 杰恩股份 | ok | 77.00 | volatility_120d 76.99% > 42.00%; distance_ma200 85.32% > 55.00% |
| 688017.SH | 绿的谐波 | ok | 77.00 | volatility_120d 79.42% > 42.00%; distance_ma200 107.29% > 55.00% |
| 301281.SZ | 科源制药 | ok | 76.98 | volatility_120d 66.65% > 42.00% |
| 000700.SZ | 模塑科技 | ok | 76.96 | volatility_120d 67.74% > 42.00% |
| 301092.SZ | 争光股份 | ok | 76.95 | volatility_120d 71.99% > 42.00% |
| 603906.SH | 龙蟠科技 | ok | 76.94 | volatility_120d 55.49% > 42.00% |
| 688249.SH | 晶合集成 | ok | 76.90 | volatility_120d 62.78% > 42.00%; distance_ma200 75.94% > 55.00% |
| 300820.SZ | 英杰电气 | ok | 76.89 | volatility_120d 61.87% > 42.00% |
| 002056.SZ | 横店东磁 | ok | 76.88 | volatility_120d 61.12% > 42.00% |
| 605366.SH | 宏柏新材 | ok | 76.86 | volatility_120d 73.45% > 42.00% |
| 603859.SH | 能科科技 | ok | 76.84 | volatility_120d 62.42% > 42.00% |
| 688028.SH | 沃尔德 | ok | 76.83 | volatility_120d 89.48% > 42.00%; distance_ma200 70.06% > 55.00% |
| 301629.SZ | 矽电股份 | ok | 76.82 | volatility_120d 83.44% > 42.00% |
| 002169.SZ | 智光电气 | ok | 76.81 | drawdown_120d -29.88% < -28.00%; volatility_120d 55.03% > 42.00% |
| 301228.SZ | 实朴检测 | ok | 76.80 | volatility_120d 65.33% > 42.00%; distance_ma200 68.00% > 55.00% |
| 605222.SH | 起帆电缆 | ok | 76.80 | drawdown_120d -48.33% < -28.00%; volatility_120d 62.22% > 42.00% |
| 600539.SH | 狮头股份 | ok | 76.78 | volatility_120d 75.61% > 42.00% |
| 002046.SZ | 国机精工 | ok | 76.78 | volatility_120d 68.36% > 42.00%; distance_ma200 59.14% > 55.00% |
| 301308.SZ | 江波龙 | ok | 76.76 | volatility_120d 82.24% > 42.00%; distance_ma200 104.66% > 55.00% |
| 688010.SH | 福光股份 | ok | 76.74 | volatility_120d 79.77% > 42.00% |
| 002916.SZ | 深南电路 | ok | 76.73 | volatility_120d 65.35% > 42.00%; distance_ma200 68.13% > 55.00% |
| 301607.SZ | 富特科技 | ok | 76.72 | volatility_120d 71.30% > 42.00%; distance_ma200 61.41% > 55.00% |
| 600246.SH | 万通发展 | ok | 76.71 | volatility_120d 67.93% > 42.00% |
| 600875.SH | 东方电气 | ok | 76.71 | drawdown_120d -34.40% < -28.00%; volatility_120d 62.48% > 42.00% |
| 600301.SH | 华锡有色 | ok | 76.68 | volatility_120d 75.99% > 42.00% |
| 000691.SZ | 亚太实业 | ok | 76.67 | volatility_120d 51.79% > 42.00% |
| 603608.SH | 天创时尚 | ok | 76.65 | volatility_120d 65.78% > 42.00%; distance_ma200 128.68% > 55.00% |
| 688584.SH | 上海合晶 | ok | 76.64 | volatility_120d 76.24% > 42.00% |
| 002635.SZ | 安洁科技 | ok | 76.63 | volatility_120d 54.27% > 42.00% |
| 300223.SZ | 北京君正 | ok | 76.62 | volatility_120d 76.35% > 42.00%; distance_ma200 112.82% > 55.00% |
| 002364.SZ | 中恒电气 | ok | 76.61 | volatility_120d 75.29% > 42.00%; distance_ma200 57.85% > 55.00% |
| 300983.SZ | 尤安设计 | ok | 76.60 | drawdown_120d -32.13% < -28.00%; volatility_120d 61.02% > 42.00% |
| 300780.SZ | 德恩精工 | ok | 76.60 | volatility_120d 81.81% > 42.00% |
| 300769.SZ | 德方纳米 | ok | 76.59 | drawdown_120d -29.68% < -28.00%; volatility_120d 59.55% > 42.00% |
| 688536.SH | 思瑞浦 | ok | 76.59 | volatility_120d 65.09% > 42.00%; distance_ma200 69.01% > 55.00% |
| 688398.SH | 赛特新材 | ok | 76.57 | drawdown_120d -30.21% < -28.00%; volatility_120d 49.85% > 42.00% |
| 688155.SH | 先惠技术 | ok | 76.57 | drawdown_120d -28.89% < -28.00%; volatility_120d 63.96% > 42.00% |
| 603011.SH | 合锻智能 | ok | 76.57 | drawdown_120d -29.71% < -28.00%; volatility_120d 72.77% > 42.00% |
| 605178.SH | 时空科技 | ok | 76.54 | volatility_120d 66.99% > 42.00%; distance_ma200 82.99% > 55.00% |
| 002831.SZ | 裕同科技 | ok | 76.52 | volatility_120d 56.89% > 42.00% |
| 688052.SH | 纳芯微 | ok | 76.49 | volatility_120d 62.11% > 42.00% |
| 600714.SH | 金瑞矿业 | ok | 76.49 | close_below_ma200; drawdown_120d -48.37% < -28.00%; volatility_120d 76.35% > 42.00% |
| 301232.SZ | 飞沃科技 | ok | 76.48 | volatility_120d 96.22% > 42.00%; distance_ma200 72.28% > 55.00% |
| 002674.SZ | 兴业科技 | ok | 76.47 | volatility_120d 56.88% > 42.00%; distance_ma200 92.60% > 55.00% |
| 603897.SH | 长城科技 | ok | 76.44 | drawdown_120d -46.06% < -28.00%; volatility_120d 68.05% > 42.00% |
| 300964.SZ | 本川智能 | ok | 76.41 | volatility_120d 87.19% > 42.00%; distance_ma200 67.75% > 55.00% |
| 688702.SH | 盛科通信 | ok | 76.40 | volatility_120d 90.59% > 42.00%; distance_ma200 92.80% > 55.00% |
| 300265.SZ | 通光线缆 | ok | 76.40 | drawdown_120d -39.42% < -28.00%; volatility_120d 95.63% > 42.00% |
| 002969.SZ | 嘉美包装 | ok | 76.40 | close_below_ma200; ma60_not_above_ma120; drawdown_120d -60.08% < -28.00%; volatility_120d 94.78% > 42.00% |
| 688671.SH | 碧兴物联 | ok | 76.37 | volatility_120d 61.22% > 42.00% |
| 600360.SH | 华微电子 | ok | 76.36 | volatility_120d 53.21% > 42.00% |
| 002805.SZ | 丰元股份 | ok | 76.34 | volatility_120d 57.51% > 42.00% |
| 688388.SH | 嘉元科技 | ok | 76.29 | volatility_120d 69.73% > 42.00% |
| 603267.SH | 鸿远电子 | ok | 76.26 | volatility_120d 62.64% > 42.00% |
| 688322.SH | 奥比中光 | ok | 76.26 | volatility_120d 64.89% > 42.00% |
| 300661.SZ | 圣邦股份 | ok | 76.25 | volatility_120d 59.27% > 42.00%; distance_ma200 65.12% > 55.00% |
| 605389.SH | 长龄液压 | ok | 76.24 | volatility_120d 51.23% > 42.00% |
| 603297.SH | 永新光学 | ok | 76.23 | volatility_120d 49.53% > 42.00% |
| 300151.SZ | 昌红科技 | ok | 76.23 | volatility_120d 61.04% > 42.00% |
| 688205.SH | 德科立 | ok | 76.23 | close_below_ma200; drawdown_120d -45.34% < -28.00%; volatility_120d 95.57% > 42.00% |
| 688379.SH | 华光新材 | ok | 76.22 | volatility_120d 69.42% > 42.00% |
| 688378.SH | 奥来德 | ok | 76.20 | volatility_120d 64.31% > 42.00%; distance_ma200 59.46% > 55.00% |
| 688110.SH | 东芯股份 | ok | 76.18 | volatility_120d 81.13% > 42.00% |
| 001337.SZ | 四川黄金 | ok | 76.16 | close_below_ma200; drawdown_120d -46.50% < -28.00%; volatility_120d 76.20% > 42.00% |
| 301045.SZ | 天禄科技 | ok | 76.16 | volatility_120d 71.64% > 42.00%; distance_ma200 135.08% > 55.00% |
| 002167.SZ | 东方锆业 | ok | 76.13 | volatility_120d 65.29% > 42.00%; distance_ma200 73.33% > 55.00% |
| 002821.SZ | 凯莱英 | ok | 76.13 | volatility_120d 51.17% > 42.00% |
| 603931.SH | 格林达 | ok | 76.12 | volatility_120d 62.05% > 42.00%; distance_ma200 65.42% > 55.00% |
| 688392.SH | 骄成超声 | ok | 76.12 | volatility_120d 68.90% > 42.00%; distance_ma200 67.68% > 55.00% |
| 688347.SH | 华虹宏力 | ok | 76.09 | volatility_120d 83.74% > 42.00%; distance_ma200 119.67% > 55.00% |
| 688605.SH | 先锋精科 | ok | 76.08 | volatility_120d 57.42% > 42.00% |
| 301502.SZ | 华阳智能 | ok | 76.07 | volatility_120d 58.24% > 42.00% |
| 688045.SH | 必易微 | ok | 76.05 | volatility_120d 57.68% > 42.00% |
| 688163.SH | 赛伦生物 | ok | 76.03 | volatility_120d 55.77% > 42.00%; distance_ma200 65.92% > 55.00% |
| 688272.SH | 富吉瑞 | ok | 76.02 | volatility_120d 74.07% > 42.00% |
| 002156.SZ | 通富微电 | ok | 76.02 | volatility_120d 66.12% > 42.00% |
| 002631.SZ | 德尔未来 | ok | 76.01 | volatility_120d 58.12% > 42.00%; distance_ma200 66.03% > 55.00% |
| 300037.SZ | 新宙邦 | ok | 76.01 | volatility_120d 57.22% > 42.00% |
| 002785.SZ | 万里石 | ok | 75.99 | volatility_120d 50.26% > 42.00% |
| 688295.SH | 中复神鹰 | ok | 75.98 | volatility_120d 81.84% > 42.00% |
| 002202.SZ | 金风科技 | ok | 75.98 | ma60_not_above_ma120; drawdown_120d -35.43% < -28.00%; volatility_120d 67.23% > 42.00% |
| 001270.SZ | 铖昌科技 | ok | 75.97 | volatility_120d 69.69% > 42.00%; distance_ma200 62.64% > 55.00% |
| 300854.SZ | 中兰环保 | ok | 75.97 | close_below_ma200; drawdown_120d -49.04% < -28.00%; volatility_120d 79.98% > 42.00% |
| 000070.SZ | 特发信息 | ok | 75.93 | volatility_120d 83.71% > 42.00% |
| 600857.SH | 宁波中百 | ok | 75.93 | ma120_not_above_ma200; volatility_120d 55.50% > 42.00% |
| 603005.SH | 晶方科技 | ok | 75.92 | volatility_120d 62.49% > 42.00% |
| 000703.SZ | 恒逸石化 | ok | 75.90 | volatility_120d 62.70% > 42.00% |
| 300444.SZ | 双杰电气 | ok | 75.90 | close_below_ma200; drawdown_120d -36.08% < -28.00%; volatility_120d 75.30% > 42.00% |
| 688352.SH | 颀中科技 | ok | 75.90 | volatility_120d 72.14% > 42.00% |
| 688286.SH | 敏芯股份 | ok | 75.89 | ma120_not_above_ma200; volatility_120d 70.37% > 42.00% |
| 301115.SZ | 联检科技 | ok | 75.86 | volatility_120d 60.93% > 42.00%; distance_ma200 56.99% > 55.00% |
| 688449.SH | 联芸科技 | ok | 75.86 | volatility_120d 70.12% > 42.00% |
| 300433.SZ | 蓝思科技 | ok | 75.85 | volatility_120d 69.54% > 42.00% |
| 688416.SH | 恒烁股份 | ok | 75.82 | volatility_120d 84.52% > 42.00%; distance_ma200 98.71% > 55.00% |
| 301366.SZ | 一博科技 | ok | 75.82 | volatility_120d 69.19% > 42.00% |
| 688337.SH | 普源精电 | ok | 75.81 | volatility_120d 70.46% > 42.00% |
| 301072.SZ | 中捷精工 | ok | 75.80 | volatility_120d 49.70% > 42.00%; distance_ma200 57.58% > 55.00% |
| 688256.SH | 寒武纪 | ok | 75.80 | volatility_120d 67.86% > 42.00% |
| 002730.SZ | 电光科技 | ok | 75.77 | volatility_120d 56.71% > 42.00% |
| 688593.SH | 新相微 | ok | 75.76 | volatility_120d 78.83% > 42.00% |
| 000593.SZ | 德龙汇能 | ok | 75.75 | volatility_120d 83.76% > 42.00%; distance_ma200 67.21% > 55.00% |
| 301393.SZ | 昊帆生物 | ok | 75.74 | volatility_120d 48.85% > 42.00% |
| 300263.SZ | 隆华科技 | ok | 75.73 | volatility_120d 71.41% > 42.00% |
| 001339.SZ | 智微智能 | ok | 75.73 | volatility_120d 59.24% > 42.00%; distance_ma200 79.41% > 55.00% |
| 601872.SH | 招商轮船 | ok | 75.72 | volatility_120d 72.61% > 42.00% |
| 603285.SH | 键邦股份 | ok | 75.70 | volatility_120d 68.04% > 42.00% |
| 688728.SH | 格科微 | ok | 75.70 | ma60_not_above_ma120; ma120_not_above_ma200; volatility_120d 60.43% > 42.00% |
| 300739.SZ | 明阳电路 | ok | 75.70 | drawdown_120d -30.22% < -28.00%; volatility_120d 76.68% > 42.00% |
| 688525.SH | 佰维存储 | ok | 75.70 | volatility_120d 89.34% > 42.00%; distance_ma200 130.90% > 55.00% |
| 688305.SH | 科德数控 | ok | 75.69 | volatility_120d 42.78% > 42.00% |
| 688301.SH | 奕瑞科技 | ok | 75.69 | volatility_120d 56.48% > 42.00% |
| 688115.SH | 思林杰 | ok | 75.67 | ma120_not_above_ma200; volatility_120d 66.95% > 42.00% |
| 301328.SZ | 维峰电子 | ok | 75.65 | volatility_120d 60.82% > 42.00%; distance_ma200 93.85% > 55.00% |
| 300540.SZ | 蜀道装备 | ok | 75.63 | volatility_120d 85.44% > 42.00%; distance_ma200 75.32% > 55.00% |
| 300613.SZ | 富瀚微 | ok | 75.63 | volatility_120d 57.97% > 42.00% |
| 301285.SZ | 鸿日达 | ok | 75.59 | volatility_120d 58.64% > 42.00% |
| 002515.SZ | 金字火腿 | ok | 75.59 | ma120_not_above_ma200; volatility_120d 55.85% > 42.00% |
| 002057.SZ | 中钢天源 | ok | 75.58 | ma60_not_above_ma120; ma120_not_above_ma200; volatility_120d 44.35% > 42.00% |
| 002990.SZ | 盛视科技 | ok | 75.58 | volatility_120d 70.22% > 42.00%; distance_ma200 95.29% > 55.00% |
| 301528.SZ | 多浦乐 | ok | 75.56 | volatility_120d 62.34% > 42.00%; distance_ma200 63.41% > 55.00% |
| 300842.SZ | 帝科股份 | ok | 75.56 | close_below_ma200; ma60_not_above_ma120; drawdown_120d -40.19% < -28.00%; volatility_120d 79.21% > 42.00% |
| 301536.SZ | 星宸科技 | ok | 75.53 | volatility_120d 61.80% > 42.00%; distance_ma200 60.54% > 55.00% |
| 300909.SZ | 汇创达 | ok | 75.52 | volatility_120d 57.27% > 42.00% |
| 002254.SZ | 泰和新材 | ok | 75.52 | drawdown_120d -29.44% < -28.00%; volatility_120d 72.14% > 42.00% |
| 300868.SZ | 杰美特 | ok | 75.52 | volatility_120d 85.91% > 42.00%; distance_ma200 172.83% > 55.00% |
| 300244.SZ | 迪安诊断 | ok | 75.52 | ma60_not_above_ma120; drawdown_120d -41.08% < -28.00%; volatility_120d 73.43% > 42.00% |
| 300959.SZ | 线上线下 | ok | 75.52 | drawdown_120d -40.31% < -28.00%; volatility_120d 78.41% > 42.00% |
| 603052.SH | 可川科技 | ok | 75.51 | drawdown_120d -40.15% < -28.00%; volatility_120d 78.56% > 42.00% |
| 300843.SZ | 胜蓝股份 | ok | 75.51 | volatility_120d 76.07% > 42.00%; distance_ma200 130.24% > 55.00% |
| 688130.SH | 晶华微 | ok | 75.50 | volatility_120d 52.36% > 42.00% |
| 300420.SZ | 五洋自控 | ok | 75.50 | volatility_120d 62.85% > 42.00%; distance_ma200 103.20% > 55.00% |
| 300196.SZ | 长海股份 | ok | 75.48 | drawdown_120d -33.80% < -28.00%; volatility_120d 78.05% > 42.00% |
| 300566.SZ | 激智科技 | ok | 75.46 | volatility_120d 56.93% > 42.00%; distance_ma200 84.48% > 55.00% |
| 688679.SH | 通源环境 | ok | 75.45 | close_below_ma200; drawdown_120d -49.87% < -28.00%; volatility_120d 75.03% > 42.00% |
| 603876.SH | 鼎胜新材 | ok | 75.44 | drawdown_120d -28.95% < -28.00%; volatility_120d 61.24% > 42.00% |
| 688502.SH | 茂莱光学 | ok | 75.43 | volatility_120d 78.08% > 42.00% |
| 002718.SZ | 友邦吊顶 | ok | 75.43 | volatility_120d 68.75% > 42.00%; distance_ma200 91.83% > 55.00% |
| 300751.SZ | 迈为股份 | ok | 75.43 | ma60_not_above_ma120; drawdown_120d -31.21% < -28.00%; volatility_120d 86.18% > 42.00% |
| 300553.SZ | 集智股份 | ok | 75.42 | volatility_120d 70.80% > 42.00%; distance_ma200 59.64% > 55.00% |
| 300508.SZ | 维宏股份 | ok | 75.41 | volatility_120d 72.27% > 42.00% |
| 300480.SZ | 光力科技 | ok | 75.40 | volatility_120d 76.21% > 42.00%; distance_ma200 59.79% > 55.00% |
| 601101.SH | 昊华能源 | ok | 75.39 | volatility_120d 55.98% > 42.00% |
| 688035.SH | 德邦科技 | ok | 75.38 | volatility_120d 72.80% > 42.00% |
| 301216.SZ | 万凯新材 | ok | 75.36 | close_below_ma200; drawdown_120d -31.39% < -28.00%; volatility_120d 53.66% > 42.00% |
| 001210.SZ | 金房能源 | ok | 75.36 | volatility_120d 58.00% > 42.00% |
| 300179.SZ | 四方达 | ok | 75.36 | volatility_120d 94.79% > 42.00%; distance_ma200 150.02% > 55.00% |
| 600985.SH | 淮北矿业 | ok | 75.33 | volatility_120d 43.08% > 42.00% |
| 300191.SZ | 潜能恒信 | ok | 75.33 | close_below_ma200; drawdown_120d -53.26% < -28.00%; volatility_120d 95.03% > 42.00% |
| 300139.SZ | 晓程科技 | ok | 75.32 | close_below_ma200; ma60_not_above_ma120; drawdown_120d -55.87% < -28.00%; volatility_120d 103.93% > 42.00% |
| 300548.SZ | 长芯博创 | ok | 75.31 | drawdown_120d -30.92% < -28.00%; volatility_120d 86.72% > 42.00% |
| 003043.SZ | 华亚智能 | ok | 75.30 | volatility_120d 56.99% > 42.00%; distance_ma200 68.89% > 55.00% |
| 688138.SH | 清溢光电 | ok | 75.30 | volatility_120d 56.73% > 42.00% |
| 300005.SZ | 探路者 | ok | 75.28 | volatility_120d 64.30% > 42.00%; distance_ma200 71.37% > 55.00% |
| 301200.SZ | 大族数控 | ok | 75.26 | volatility_120d 76.94% > 42.00%; distance_ma200 105.89% > 55.00% |
| 002796.SZ | 世嘉科技 | ok | 75.24 | close_below_ma200; drawdown_120d -48.56% < -28.00%; volatility_120d 78.75% > 42.00% |
| 688359.SH | 三孚新科 | ok | 75.23 | volatility_120d 68.71% > 42.00%; distance_ma200 106.57% > 55.00% |
| 603031.SH | 安孚科技 | ok | 75.21 | volatility_120d 71.51% > 42.00% |
| 688585.SH | 上纬新材 | ok | 75.20 | volatility_120d 73.10% > 42.00% |
| 003004.SZ | 声迅股份 | ok | 75.19 | volatility_120d 59.11% > 42.00%; distance_ma200 125.79% > 55.00% |
| 301099.SZ | 雅创电子 | ok | 75.13 | volatility_120d 76.43% > 42.00%; distance_ma200 64.85% > 55.00% |
| 603139.SH | 康惠股份 | ok | 75.12 | volatility_120d 55.79% > 42.00% |
| 300700.SZ | 岱勒新材 | ok | 75.10 | volatility_120d 48.84% > 42.00% |
| 001266.SZ | 宏英智能 | ok | 75.10 | volatility_120d 57.51% > 42.00% |
| 300863.SZ | 卡倍亿 | ok | 75.10 | drawdown_120d -29.87% < -28.00%; volatility_120d 69.55% > 42.00% |
| 300907.SZ | 康平科技 | ok | 75.06 | volatility_120d 63.03% > 42.00%; distance_ma200 59.63% > 55.00% |
| 300486.SZ | 东杰智能 | ok | 75.05 | volatility_120d 67.45% > 42.00% |
| 603588.SH | 高能环境 | ok | 75.03 | volatility_120d 60.93% > 42.00%; distance_ma200 62.66% > 55.00% |
| 300234.SZ | 开尔新材 | ok | 75.02 | volatility_120d 52.44% > 42.00%; distance_ma200 61.40% > 55.00% |
| 300607.SZ | 拓斯达 | ok | 75.02 | ma120_not_above_ma200; volatility_120d 60.68% > 42.00% |
| 002947.SZ | 恒铭达 | ok | 75.02 | drawdown_120d -29.41% < -28.00%; volatility_120d 52.75% > 42.00% |
| 301369.SZ | 联动科技 | ok | 75.02 | volatility_120d 66.95% > 42.00%; distance_ma200 114.06% > 55.00% |
| 002378.SZ | 章源钨业 | ok | 75.01 | drawdown_120d -37.12% < -28.00%; volatility_120d 77.99% > 42.00% |
| 688661.SH | 和林微纳 | ok | 74.97 | volatility_120d 99.53% > 42.00%; distance_ma200 86.75% > 55.00% |
| 300912.SZ | 凯龙高科 | ok | 74.96 | drawdown_120d -39.31% < -28.00%; volatility_120d 88.18% > 42.00% |
| 301183.SZ | 东田微 | ok | 74.94 | volatility_120d 87.22% > 42.00% |
| 300401.SZ | 花园生物 | ok | 74.94 | ma60_not_above_ma120; volatility_120d 65.42% > 42.00% |
| 301458.SZ | 钧崴电子 | ok | 74.92 | volatility_120d 67.25% > 42.00% |
| 000890.SZ | 法尔胜 | ok | 74.91 | close_below_ma200; drawdown_120d -57.24% < -28.00%; volatility_120d 84.68% > 42.00% |
| 301306.SZ | 西测测试 | ok | 74.89 | volatility_120d 83.58% > 42.00% |
| 688503.SH | 聚和材料 | ok | 74.89 | volatility_120d 79.92% > 42.00% |
| 600584.SH | 长电科技 | ok | 74.85 | volatility_120d 68.08% > 42.00%; distance_ma200 94.07% > 55.00% |
| 688216.SH | 气派科技 | ok | 74.85 | volatility_120d 82.41% > 42.00% |
| 300257.SZ | 开山股份 | ok | 74.81 | volatility_120d 67.80% > 42.00% |
| 688218.SH | 江苏北人 | ok | 74.80 | volatility_120d 51.86% > 42.00%; distance_ma200 69.00% > 55.00% |
| 002203.SZ | 海亮股份 | ok | 74.80 | volatility_120d 64.06% > 42.00% |
| 300677.SZ | 英科医疗 | ok | 74.79 | drawdown_120d -32.69% < -28.00%; volatility_120d 58.76% > 42.00% |
| 600667.SH | 太极实业 | ok | 74.78 | volatility_120d 78.87% > 42.00%; distance_ma200 155.36% > 55.00% |
| 603316.SH | 诚邦股份 | ok | 74.76 | volatility_120d 69.58% > 42.00% |
| 002886.SZ | 沃特股份 | ok | 74.74 | volatility_120d 51.04% > 42.00% |
| 600641.SH | 先导基电 | ok | 74.71 | volatility_120d 63.56% > 42.00%; distance_ma200 101.03% > 55.00% |
| 688418.SH | 震有科技 | ok | 74.69 | volatility_120d 74.30% > 42.00% |
| 300436.SZ | 广生堂 | ok | 74.67 | drawdown_120d -28.40% < -28.00%; volatility_120d 82.19% > 42.00% |
| 688253.SH | 英诺特 | ok | 74.66 | volatility_120d 58.51% > 42.00% |
| 002787.SZ | 华源控股 | ok | 74.65 | volatility_120d 70.80% > 42.00%; distance_ma200 95.21% > 55.00% |
| 002897.SZ | 意华股份 | ok | 74.65 | volatility_120d 73.54% > 42.00% |
| 688332.SH | 中科蓝讯 | ok | 74.64 | volatility_120d 56.40% > 42.00% |
| 301321.SZ | 翰博高新 | ok | 74.61 | volatility_120d 72.76% > 42.00%; distance_ma200 75.04% > 55.00% |
| 300243.SZ | 瑞丰高材 | ok | 74.61 | volatility_120d 83.10% > 42.00% |
| 688172.SH | 燕东微 | ok | 74.60 | volatility_120d 91.48% > 42.00%; distance_ma200 93.74% > 55.00% |
| 301626.SZ | 苏州天脉 | ok | 74.60 | volatility_120d 62.20% > 42.00% |
| 688112.SH | 鼎阳科技 | ok | 74.59 | volatility_120d 69.27% > 42.00%; distance_ma200 67.12% > 55.00% |
| 300834.SZ | 星辉环材 | ok | 74.58 | volatility_120d 75.40% > 42.00% |
| 002976.SZ | 瑞玛精密 | ok | 74.57 | volatility_120d 58.78% > 42.00% |
| 301566.SZ | 达利凯普 | ok | 74.55 | drawdown_120d -28.28% < -28.00%; volatility_120d 74.23% > 42.00% |
| 301235.SZ | 华康洁净 | ok | 74.55 | volatility_120d 83.42% > 42.00% |
| 300331.SZ | 苏大维格 | ok | 74.54 | volatility_120d 75.99% > 42.00% |
| 603687.SH | 大胜达 | ok | 74.53 | volatility_120d 75.25% > 42.00% |
| 000672.SZ | 上峰材料 | ok | 74.53 | volatility_120d 54.75% > 42.00%; distance_ma200 60.45% > 55.00% |
| 688450.SH | 光格科技 | ok | 74.52 | volatility_120d 58.63% > 42.00%; distance_ma200 71.60% > 55.00% |
| 300137.SZ | 先河环保 | ok | 74.47 | volatility_120d 54.92% > 42.00% |
| 300221.SZ | 银禧科技 | ok | 74.46 | volatility_120d 66.59% > 42.00% |
| 300720.SZ | 海川智能 | ok | 74.45 | volatility_120d 87.96% > 42.00%; distance_ma200 125.17% > 55.00% |
| 688652.SH | 京仪装备 | ok | 74.44 | volatility_120d 66.98% > 42.00%; distance_ma200 79.15% > 55.00% |
| 300522.SZ | 世名科技 | ok | 74.42 | volatility_120d 69.17% > 42.00%; distance_ma200 61.70% > 55.00% |
| 688396.SH | 华润微 | ok | 74.41 | volatility_120d 64.06% > 42.00% |
| 301387.SZ | 光大同创 | ok | 74.40 | drawdown_120d -35.08% < -28.00%; volatility_120d 77.16% > 42.00% |
| 301392.SZ | 汇成真空 | ok | 74.39 | volatility_120d 78.36% > 42.00%; distance_ma200 66.01% > 55.00% |
| 603678.SH | 火炬电子 | ok | 74.38 | volatility_120d 70.99% > 42.00%; distance_ma200 92.02% > 55.00% |
| 600353.SH | 旭光电子 | ok | 74.36 | volatility_120d 69.57% > 42.00%; distance_ma200 131.74% > 55.00% |
| 688720.SH | 艾森股份 | ok | 74.35 | volatility_120d 72.04% > 42.00%; distance_ma200 65.20% > 55.00% |
| 002119.SZ | 康强电子 | ok | 74.31 | volatility_120d 68.19% > 42.00%; distance_ma200 64.40% > 55.00% |
| 001316.SZ | 润贝航科 | ok | 74.29 | volatility_120d 64.60% > 42.00% |
| 603061.SH | 金海通 | ok | 74.29 | volatility_120d 75.55% > 42.00%; distance_ma200 155.49% > 55.00% |
| 688012.SH | 中微公司 | ok | 74.29 | volatility_120d 58.64% > 42.00%; distance_ma200 84.77% > 55.00% |
| 301265.SZ | 华新科技 | ok | 74.26 | volatility_120d 70.99% > 42.00% |
| 300088.SZ | 长信科技 | ok | 74.20 | volatility_120d 69.69% > 42.00% |
| 301310.SZ | 鑫宏业 | ok | 74.17 | volatility_120d 76.95% > 42.00%; distance_ma200 59.19% > 55.00% |
| 300576.SZ | 容大感光 | ok | 74.17 | volatility_120d 59.39% > 42.00% |
| 300604.SZ | 长川科技 | ok | 74.15 | volatility_120d 72.47% > 42.00%; distance_ma200 122.78% > 55.00% |
| 688048.SH | 长光华芯 | ok | 74.13 | volatility_120d 101.44% > 42.00%; distance_ma200 115.95% > 55.00% |
| 002185.SZ | 华天科技 | ok | 74.13 | volatility_120d 61.72% > 42.00% |
| 688766.SH | 普冉股份 | ok | 74.12 | volatility_120d 97.79% > 42.00%; distance_ma200 206.33% > 55.00% |
| 002484.SZ | 江海股份 | ok | 74.11 | volatility_120d 74.18% > 42.00%; distance_ma200 138.57% > 55.00% |
| 001267.SZ | 汇绿生态 | ok | 74.09 | drawdown_120d -36.87% < -28.00%; volatility_120d 79.64% > 42.00% |
| 301182.SZ | 凯旺科技 | ok | 74.08 | volatility_120d 69.01% > 42.00%; distance_ma200 87.16% > 55.00% |
| 001211.SZ | 双枪科技 | ok | 74.08 | drawdown_120d -48.53% < -28.00%; volatility_120d 57.81% > 42.00% |
| 300632.SZ | 光莆股份 | ok | 74.07 | drawdown_120d -44.05% < -28.00%; volatility_120d 88.74% > 42.00% |
| 688498.SH | 源杰科技 | ok | 74.05 | volatility_120d 83.13% > 42.00%; distance_ma200 137.23% > 55.00% |
| 003018.SZ | 金富科技 | ok | 74.04 | volatility_120d 81.54% > 42.00%; distance_ma200 128.95% > 55.00% |
| 300929.SZ | 华骐环保 | ok | 74.04 | excess_return_240d 5.20% < 8.00%; volatility_120d 48.65% > 42.00% |
| 300757.SZ | 罗博特科 | ok | 74.03 | drawdown_120d -30.77% < -28.00%; volatility_120d 85.31% > 42.00% |
| 301326.SZ | 捷邦科技 | ok | 74.02 | close_below_ma200; drawdown_120d -34.85% < -28.00%; volatility_120d 63.28% > 42.00% |
| 603065.SH | 宿迁联盛 | ok | 74.02 | volatility_120d 56.35% > 42.00%; distance_ma200 102.45% > 55.00% |
| 600141.SH | 兴发集团 | ok | 74.02 | ma60_not_above_ma120; volatility_120d 62.30% > 42.00% |
| 688055.SH | 龙腾光电 | ok | 73.99 | volatility_120d 72.57% > 42.00% |
| 688158.SH | 优刻得 | ok | 73.96 | close_below_ma200; drawdown_120d -37.08% < -28.00%; volatility_120d 90.31% > 42.00% |
| 688667.SH | 菱电电控 | ok | 73.96 | drawdown_120d -29.36% < -28.00%; volatility_120d 64.32% > 42.00% |
| 002371.SZ | 北方华创 | ok | 73.96 | volatility_120d 48.93% > 42.00%; distance_ma200 61.79% > 55.00% |
| 688485.SH | 九州一轨 | ok | 73.95 | volatility_120d 93.56% > 42.00%; distance_ma200 107.70% > 55.00% |
| 688403.SH | 汇成股份 | ok | 73.94 | volatility_120d 78.97% > 42.00%; distance_ma200 95.42% > 55.00% |
| 600769.SH | 祥龙电业 | ok | 73.92 | volatility_120d 70.96% > 42.00% |
| 300747.SZ | 锐科激光 | ok | 73.91 | volatility_120d 67.86% > 42.00% |
| 603223.SH | 恒通股份 | ok | 73.89 | ma120_not_above_ma200; volatility_120d 44.35% > 42.00% |
| 301093.SZ | 华兰股份 | ok | 73.88 | volatility_120d 80.64% > 42.00%; distance_ma200 61.83% > 55.00% |
| 002047.SZ | 宝鹰股份 | ok | 73.85 | drawdown_120d -29.95% < -28.00%; volatility_120d 50.09% > 42.00% |
| 605318.SH | 法狮龙 | ok | 73.85 | drawdown_120d -32.23% < -28.00%; volatility_120d 61.58% > 42.00% |
| 688600.SH | 皖仪科技 | ok | 73.83 | volatility_120d 51.40% > 42.00% |
| 600176.SH | 中国巨石 | ok | 73.81 | volatility_120d 69.61% > 42.00%; distance_ma200 146.46% > 55.00% |
| 300042.SZ | 朗科科技 | ok | 73.79 | volatility_120d 86.61% > 42.00%; distance_ma200 64.99% > 55.00% |
| 300857.SZ | 协创数据 | ok | 73.75 | volatility_120d 89.83% > 42.00%; distance_ma200 75.76% > 55.00% |
| 300749.SZ | 顶固集创 | ok | 73.72 | ma60_not_above_ma120; drawdown_120d -35.78% < -28.00%; volatility_120d 83.02% > 42.00% |
| 603688.SH | 石英股份 | ok | 73.70 | volatility_120d 65.99% > 42.00% |
| 001359.SZ | 平安电工 | ok | 73.70 | volatility_120d 62.69% > 42.00%; distance_ma200 88.19% > 55.00% |
| 002436.SZ | 兴森科技 | ok | 73.69 | volatility_120d 65.02% > 42.00%; distance_ma200 73.25% > 55.00% |
| 301396.SZ | 宏景科技 | ok | 73.69 | volatility_120d 116.74% > 42.00%; distance_ma200 158.02% > 55.00% |
| 000823.SZ | 超声电子 | ok | 73.69 | drawdown_120d -32.58% < -28.00%; volatility_120d 67.24% > 42.00% |
| 600962.SH | 国投中鲁 | ok | 73.66 | volatility_120d 53.39% > 42.00% |
| 002192.SZ | 融捷股份 | ok | 73.66 | volatility_120d 65.70% > 42.00% |
| 688531.SH | 日联科技 | ok | 73.65 | volatility_120d 73.48% > 42.00%; distance_ma200 100.35% > 55.00% |
| 000429.SZ | 粤高速A | ok | 73.65 | excess_return_240d -11.23% < 8.00% |
| 688181.SH | 八亿时空 | ok | 73.63 | volatility_120d 61.22% > 42.00% |
| 600961.SH | 株冶集团 | ok | 73.62 | volatility_120d 74.62% > 42.00% |
| 002066.SZ | 瑞泰科技 | ok | 73.61 | volatility_120d 46.90% > 42.00% |
| 300811.SZ | 铂科新材 | ok | 73.59 | volatility_120d 67.81% > 42.00% |
| 002851.SZ | 麦格米特 | ok | 73.57 | volatility_120d 73.34% > 42.00% |
| 002741.SZ | 光华科技 | ok | 73.57 | volatility_120d 64.19% > 42.00% |
| 300802.SZ | 矩子科技 | ok | 73.57 | excess_return_240d 6.86% < 8.00%; volatility_120d 51.57% > 42.00% |
| 300201.SZ | 海伦哲 | ok | 73.55 | volatility_120d 61.02% > 42.00%; distance_ma200 80.22% > 55.00% |
| 300502.SZ | 新易盛 | ok | 73.54 | volatility_120d 73.12% > 42.00% |
| 301055.SZ | 张小泉 | ok | 73.54 | volatility_120d 75.16% > 42.00%; distance_ma200 61.64% > 55.00% |
| 605020.SH | 永和股份 | ok | 73.54 | volatility_120d 50.72% > 42.00% |
| 603650.SH | 彤程新材 | ok | 73.51 | volatility_120d 63.57% > 42.00%; distance_ma200 63.20% > 55.00% |
| 688663.SH | 新风光 | ok | 73.51 | volatility_120d 65.50% > 42.00% |
| 300623.SZ | 捷捷微电 | ok | 73.49 | volatility_120d 55.64% > 42.00% |
| 301313.SZ | 凡拓数创 | ok | 73.48 | drawdown_120d -35.55% < -28.00%; volatility_120d 83.73% > 42.00% |
| 300236.SZ | 上海新阳 | ok | 73.48 | volatility_120d 67.72% > 42.00% |
| 603399.SH | 永杉锂业 | ok | 73.46 | volatility_120d 70.17% > 42.00%; distance_ma200 60.74% > 55.00% |
| 605289.SH | 罗曼股份 | ok | 73.46 | volatility_120d 74.44% > 42.00%; distance_ma200 80.22% > 55.00% |
| 000725.SZ | 京东方A | ok | 73.46 | volatility_120d 54.11% > 42.00%; distance_ma200 73.03% > 55.00% |
| 002980.SZ | 华盛昌 | ok | 73.46 | volatility_120d 82.25% > 42.00%; distance_ma200 131.83% > 55.00% |
| 301071.SZ | 力量钻石 | ok | 73.46 | volatility_120d 74.33% > 42.00%; distance_ma200 84.31% > 55.00% |
| 301086.SZ | 鸿富瀚 | ok | 73.45 | volatility_120d 67.08% > 42.00%; distance_ma200 90.24% > 55.00% |
| 300693.SZ | 盛弘股份 | ok | 73.45 | drawdown_120d -37.48% < -28.00%; volatility_120d 57.64% > 42.00% |
| 600460.SH | 士兰微 | ok | 73.45 | volatility_120d 54.79% > 42.00% |
| 002971.SZ | 和远气体 | ok | 73.44 | volatility_120d 68.37% > 42.00%; distance_ma200 80.59% > 55.00% |
| 301322.SZ | 绿通科技 | ok | 73.43 | volatility_120d 66.54% > 42.00% |
| 300054.SZ | 鼎龙股份 | ok | 73.42 | volatility_120d 68.24% > 42.00%; distance_ma200 84.33% > 55.00% |
| 300649.SZ | 杭州园林 | ok | 73.41 | volatility_120d 55.63% > 42.00%; distance_ma200 61.21% > 55.00% |
| 002824.SZ | 和胜股份 | ok | 73.41 | volatility_120d 70.82% > 42.00% |
| 002463.SZ | 沪电股份 | ok | 73.37 | volatility_120d 65.81% > 42.00% |
| 300782.SZ | 卓胜微 | ok | 73.37 | drawdown_120d -33.87% < -28.00%; volatility_120d 65.05% > 42.00% |
| 603324.SH | 盛剑科技 | ok | 73.36 | volatility_120d 59.16% > 42.00%; distance_ma200 66.06% > 55.00% |
| 603163.SH | 圣晖集成 | ok | 73.35 | volatility_120d 78.57% > 42.00% |
| 300736.SZ | 百邦科技 | ok | 73.34 | drawdown_120d -39.85% < -28.00%; volatility_120d 82.96% > 42.00% |
| 688630.SH | 芯碁微装 | ok | 73.34 | volatility_120d 81.04% > 42.00%; distance_ma200 126.94% > 55.00% |
| 300475.SZ | 香农芯创 | ok | 73.33 | volatility_120d 82.82% > 42.00%; distance_ma200 72.54% > 55.00% |
| 002885.SZ | 京泉华 | ok | 73.31 | drawdown_120d -28.75% < -28.00%; volatility_120d 65.81% > 42.00% |
| 688059.SH | 华锐精密 | ok | 73.31 | volatility_120d 65.02% > 42.00%; distance_ma200 69.56% > 55.00% |
| 688719.SH | 爱科赛博 | ok | 73.30 | volatility_120d 72.57% > 42.00% |
| 688381.SH | 帝奥微 | ok | 73.29 | volatility_120d 71.63% > 42.00%; distance_ma200 56.38% > 55.00% |
| 002716.SZ | 湖南白银 | ok | 73.29 | close_below_ma200; ma60_not_above_ma120; drawdown_120d -59.58% < -28.00%; volatility_120d 76.91% > 42.00% |
| 002290.SZ | 禾盛新材 | ok | 73.28 | volatility_120d 68.16% > 42.00% |
| 688535.SH | 华海诚科 | ok | 73.27 | volatility_120d 78.79% > 42.00%; distance_ma200 83.18% > 55.00% |
| 300373.SZ | 扬杰科技 | ok | 73.26 | volatility_120d 70.46% > 42.00%; distance_ma200 65.56% > 55.00% |
| 688082.SH | 盛美上海 | ok | 73.25 | volatility_120d 71.52% > 42.00%; distance_ma200 93.45% > 55.00% |
| 688090.SH | 瑞松科技 | ok | 73.23 | volatility_120d 75.61% > 42.00%; distance_ma200 106.09% > 55.00% |
| 603880.SH | 南卫股份 | ok | 73.23 | excess_return_240d 6.16% < 8.00%; volatility_120d 50.75% > 42.00% |
| 688521.SH | 芯原股份 | ok | 73.20 | volatility_120d 87.17% > 42.00% |
| 688387.SH | 信科移动 | ok | 73.20 | volatility_120d 91.90% > 42.00% |
| 000988.SZ | 华工科技 | ok | 73.17 | volatility_120d 68.68% > 42.00% |
| 002384.SZ | 东山精密 | ok | 73.16 | volatility_120d 72.13% > 42.00%; distance_ma200 88.37% > 55.00% |
| 300260.SZ | 新莱应材 | ok | 73.16 | volatility_120d 68.74% > 42.00% |
| 300400.SZ | 劲拓股份 | ok | 73.14 | volatility_120d 63.23% > 42.00% |
| 003026.SZ | 中晶科技 | ok | 73.14 | drawdown_120d -29.30% < -28.00%; volatility_120d 59.21% > 42.00% |
| 688008.SH | 澜起科技 | ok | 73.11 | volatility_120d 76.86% > 42.00%; distance_ma200 63.87% > 55.00% |
| 688401.SH | 路维光电 | ok | 73.11 | volatility_120d 71.42% > 42.00% |
| 002903.SZ | 宇环数控 | ok | 73.08 | volatility_120d 69.30% > 42.00% |
| 688037.SH | 芯源微 | ok | 73.08 | volatility_120d 87.39% > 42.00%; distance_ma200 97.66% > 55.00% |
| 301317.SZ | 鑫磊股份 | ok | 73.05 | drawdown_120d -28.75% < -28.00%; volatility_120d 89.21% > 42.00% |
| 000021.SZ | 深科技 | ok | 73.04 | volatility_120d 67.90% > 42.00%; distance_ma200 76.48% > 55.00% |
| 001389.SZ | 广合科技 | ok | 73.03 | volatility_120d 73.51% > 42.00%; distance_ma200 67.69% > 55.00% |
| 605198.SH | 安德利 | ok | 73.02 | volatility_120d 59.90% > 42.00% |
| 600183.SH | 生益科技 | ok | 73.00 | volatility_120d 63.46% > 42.00%; distance_ma200 98.84% > 55.00% |
| 688021.SH | 奥福科技 | ok | 72.96 | close_below_ma200; drawdown_120d -33.17% < -28.00%; volatility_120d 61.29% > 42.00% |
| 600999.SH | 招商证券 | ok | 72.95 | ma120_not_above_ma200; excess_return_240d 4.50% < 8.00% |
| 688056.SH | 莱伯泰科 | ok | 72.95 | drawdown_120d -36.24% < -28.00%; volatility_120d 76.59% > 42.00% |
| 002585.SZ | 双星新材 | ok | 72.93 | drawdown_120d -32.64% < -28.00%; volatility_120d 71.37% > 42.00% |
| 603507.SH | 振江股份 | ok | 72.93 | drawdown_120d -33.25% < -28.00%; volatility_120d 48.39% > 42.00% |
| 688371.SH | 菲沃泰 | ok | 72.93 | volatility_120d 68.60% > 42.00% |
| 300903.SZ | 科翔股份 | ok | 72.90 | volatility_120d 92.29% > 42.00%; distance_ma200 160.41% > 55.00% |
| 688596.SH | 正帆科技 | ok | 72.89 | volatility_120d 78.65% > 42.00%; distance_ma200 95.65% > 55.00% |
| 301591.SZ | 肯特股份 | ok | 72.84 | drawdown_120d -30.78% < -28.00%; volatility_120d 69.71% > 42.00% |
| 002806.SZ | 华锋股份 | ok | 72.83 | volatility_120d 57.14% > 42.00% |
| 603929.SH | 亚翔集成 | ok | 72.83 | volatility_120d 80.08% > 42.00%; distance_ma200 80.34% > 55.00% |
| 002208.SZ | 合肥城建 | ok | 72.82 | drawdown_120d -30.01% < -28.00%; volatility_120d 73.54% > 42.00% |
| 001268.SZ | 联合精密 | ok | 72.78 | volatility_120d 52.29% > 42.00% |
| 002407.SZ | 多氟多 | ok | 72.77 | volatility_120d 64.65% > 42.00% |
| 603890.SH | 春秋电子 | ok | 72.77 | volatility_120d 66.14% > 42.00% |
| 002812.SZ | 恩捷股份 | ok | 72.71 | volatility_120d 56.25% > 42.00% |
| 300567.SZ | 精测电子 | ok | 72.69 | volatility_120d 79.51% > 42.00%; distance_ma200 113.28% > 55.00% |
| 300432.SZ | 富临精工 | ok | 72.66 | close_below_ma200; drawdown_120d -32.49% < -28.00%; volatility_120d 50.97% > 42.00% |
| 301179.SZ | 泽宇智能 | ok | 72.65 | drawdown_120d -31.77% < -28.00%; volatility_120d 68.08% > 42.00% |
| 603538.SH | 美诺华 | ok | 72.64 | drawdown_120d -40.93% < -28.00%; volatility_120d 77.76% > 42.00% |
| 300489.SZ | 光智科技 | ok | 72.62 | volatility_120d 87.15% > 42.00%; distance_ma200 243.62% > 55.00% |
| 300852.SZ | 四会富仕 | ok | 72.60 | volatility_120d 74.82% > 42.00% |
| 002428.SZ | 云南锗业 | ok | 72.59 | volatility_120d 83.85% > 42.00%; distance_ma200 112.73% > 55.00% |
| 688718.SH | 唯赛勃 | ok | 72.56 | volatility_120d 46.15% > 42.00% |
| 300174.SZ | 元力股份 | ok | 72.55 | volatility_120d 63.56% > 42.00% |
| 688786.SH | 悦安新材 | ok | 72.54 | volatility_120d 73.39% > 42.00%; distance_ma200 56.71% > 55.00% |
| 600888.SH | 新疆众和 | ok | 72.54 | volatility_120d 57.02% > 42.00% |
| 603683.SH | 晶华新材 | ok | 72.53 | ma120_not_above_ma200; volatility_120d 44.13% > 42.00% |
| 688019.SH | 安集科技 | ok | 72.52 | volatility_120d 66.61% > 42.00% |
| 688290.SH | 景业智能 | ok | 72.52 | ma120_not_above_ma200; volatility_120d 51.68% > 42.00% |
| 688677.SH | 海泰新光 | ok | 72.47 | drawdown_120d -46.04% < -28.00%; volatility_120d 84.00% > 42.00% |
| 688126.SH | 沪硅产业 | ok | 72.46 | volatility_120d 74.14% > 42.00% |
| 603158.SH | 腾龙股份 | ok | 72.46 | drawdown_120d -28.25% < -28.00%; volatility_120d 59.21% > 42.00% |
| 688257.SH | 新锐股份 | ok | 72.45 | volatility_120d 83.79% > 42.00%; distance_ma200 124.87% > 55.00% |
| 688432.SH | 有研硅 | ok | 72.43 | volatility_120d 83.92% > 42.00%; distance_ma200 142.85% > 55.00% |
| 688368.SH | 晶丰明源 | ok | 72.39 | volatility_120d 80.91% > 42.00%; distance_ma200 77.15% > 55.00% |
| 601133.SH | 柏诚股份 | ok | 72.38 | volatility_120d 74.60% > 42.00%; distance_ma200 85.80% > 55.00% |
| 300518.SZ | 新迅达 | ok | 72.38 | volatility_120d 77.35% > 42.00% |
| 300346.SZ | 南大光电 | ok | 72.38 | volatility_120d 69.51% > 42.00%; distance_ma200 57.10% > 55.00% |
| 688312.SH | 燕麦科技 | ok | 72.38 | drawdown_120d -36.75% < -28.00%; volatility_120d 79.10% > 42.00% |
| 688548.SH | 广钢气体 | ok | 72.37 | volatility_120d 82.43% > 42.00%; distance_ma200 112.51% > 55.00% |
| 001229.SZ | 魅视科技 | ok | 72.37 | ma60_not_above_ma120; volatility_120d 44.94% > 42.00% |
| 688147.SH | 微导纳米 | ok | 72.35 | volatility_120d 81.25% > 42.00%; distance_ma200 87.71% > 55.00% |
| 300408.SZ | 三环集团 | ok | 72.35 | volatility_120d 73.14% > 42.00%; distance_ma200 110.30% > 55.00% |
| 000066.SZ | 中国长城 | ok | 72.32 | volatility_120d 66.41% > 42.00% |
| 301128.SZ | 强瑞技术 | ok | 72.31 | volatility_120d 75.10% > 42.00%; distance_ma200 63.75% > 55.00% |
| 301248.SZ | 杰创智能 | ok | 72.29 | volatility_120d 89.07% > 42.00%; distance_ma200 59.83% > 55.00% |
| 688777.SH | 中控技术 | ok | 72.26 | volatility_120d 67.55% > 42.00% |
| 001400.SZ | 江顺科技 | ok | 72.22 | drawdown_120d -28.20% < -28.00%; volatility_120d 89.25% > 42.00% |
| 603002.SH | 宏昌电子 | ok | 72.22 | volatility_120d 72.13% > 42.00%; distance_ma200 95.69% > 55.00% |
| 600110.SH | 诺德股份 | ok | 72.19 | volatility_120d 68.48% > 42.00%; distance_ma200 64.80% > 55.00% |
| 688383.SH | 新益昌 | ok | 72.16 | volatility_120d 63.95% > 42.00%; distance_ma200 75.67% > 55.00% |
| 300285.SZ | 国瓷材料 | ok | 72.16 | volatility_120d 86.98% > 42.00%; distance_ma200 144.63% > 55.00% |
| 300814.SZ | 中富电路 | ok | 72.16 | volatility_120d 71.55% > 42.00%; distance_ma200 77.41% > 55.00% |
| 300666.SZ | 江丰电子 | ok | 72.15 | volatility_120d 80.59% > 42.00%; distance_ma200 130.70% > 55.00% |
| 688234.SH | 天岳先进 | ok | 72.15 | volatility_120d 81.18% > 42.00% |
| 300321.SZ | 同大股份 | ok | 72.14 | ma120_not_above_ma200; volatility_120d 70.46% > 42.00% |
| 688025.SH | 杰普特 | ok | 72.12 | volatility_120d 101.47% > 42.00%; distance_ma200 71.07% > 55.00% |
| 002008.SZ | 大族激光 | ok | 72.11 | volatility_120d 71.63% > 42.00%; distance_ma200 89.99% > 55.00% |
| 688328.SH | 深科达 | ok | 72.09 | volatility_120d 92.79% > 42.00%; distance_ma200 96.92% > 55.00% |
| 600909.SH | 华安证券 | ok | 72.08 | volatility_120d 52.86% > 42.00% |
| 300976.SZ | 达瑞电子 | ok | 72.08 | volatility_120d 61.66% > 42.00% |
| 688150.SH | 莱特光电 | ok | 72.08 | volatility_120d 74.35% > 42.00%; distance_ma200 59.35% > 55.00% |
| 002636.SZ | 金安国纪 | ok | 72.08 | volatility_120d 79.24% > 42.00%; distance_ma200 197.50% > 55.00% |
| 603115.SH | 海星股份 | ok | 72.07 | volatility_120d 85.14% > 42.00%; distance_ma200 149.08% > 55.00% |
| 688200.SH | 华峰测控 | ok | 72.07 | volatility_120d 75.18% > 42.00%; distance_ma200 131.58% > 55.00% |
| 601208.SH | 东材科技 | ok | 72.06 | volatility_120d 73.34% > 42.00%; distance_ma200 93.34% > 55.00% |
| 301568.SZ | 思泰克 | ok | 72.05 | volatility_120d 61.47% > 42.00%; distance_ma200 70.85% > 55.00% |
| 688179.SH | 阿拉丁 | ok | 72.03 | volatility_120d 72.31% > 42.00% |
| 003036.SZ | 泰坦股份 | ok | 72.03 | volatility_120d 78.90% > 42.00%; distance_ma200 170.90% > 55.00% |
| 600378.SH | 昊华科技 | ok | 72.02 | volatility_120d 65.03% > 42.00%; distance_ma200 89.15% > 55.00% |
| 600549.SH | 厦门钨业 | ok | 72.01 | volatility_120d 72.88% > 42.00% |
| 300726.SZ | 宏达电子 | ok | 72.01 | volatility_120d 73.73% > 42.00% |
| 688530.SH | 欧莱新材 | ok | 72.00 | volatility_120d 106.98% > 42.00%; distance_ma200 154.55% > 55.00% |
| 002655.SZ | 共达电声 | ok | 71.99 | volatility_120d 64.19% > 42.00%; distance_ma200 103.16% > 55.00% |
| 688309.SH | 恒誉环保 | ok | 71.99 | volatility_120d 67.99% > 42.00%; distance_ma200 60.83% > 55.00% |
| 300308.SZ | 中际旭创 | ok | 71.99 | volatility_120d 60.31% > 42.00%; distance_ma200 61.05% > 55.00% |
| 301205.SZ | 联特科技 | ok | 71.98 | volatility_120d 91.01% > 42.00% |
| 600683.SH | 京投发展 | ok | 71.98 | drawdown_120d -48.69% < -28.00%; volatility_120d 78.31% > 42.00% |
| 605589.SH | 圣泉集团 | ok | 71.95 | volatility_120d 66.79% > 42.00%; distance_ma200 64.57% > 55.00% |
| 600234.SH | 科新发展 | ok | 71.94 | volatility_120d 65.15% > 42.00% |
| 600498.SH | 烽火通信 | ok | 71.94 | drawdown_120d -33.80% < -28.00%; volatility_120d 81.49% > 42.00% |
| 002938.SZ | 鹏鼎控股 | ok | 71.93 | volatility_120d 69.81% > 42.00% |
| 688515.SH | 裕太微 | ok | 71.92 | volatility_120d 84.08% > 42.00% |
| 688519.SH | 南亚新材 | ok | 71.90 | volatility_120d 92.35% > 42.00%; distance_ma200 160.54% > 55.00% |
| 688628.SH | 优利德 | ok | 71.90 | volatility_120d 71.82% > 42.00%; distance_ma200 77.04% > 55.00% |
| 688127.SH | 蓝特光学 | ok | 71.89 | volatility_120d 67.66% > 42.00% |
| 603986.SH | 兆易创新 | ok | 71.89 | volatility_120d 74.83% > 42.00%; distance_ma200 115.30% > 55.00% |
| 603926.SH | 铁流股份 | ok | 71.88 | ma60_not_above_ma120; drawdown_120d -30.17% < -28.00%; volatility_120d 53.79% > 42.00% |
| 300939.SZ | 秋田微 | ok | 71.85 | volatility_120d 66.98% > 42.00% |
| 600345.SH | 长江通信 | ok | 71.82 | volatility_120d 78.60% > 42.00% |
| 603618.SH | 杭电股份 | ok | 71.82 | volatility_120d 89.76% > 42.00%; distance_ma200 124.97% > 55.00% |
| 002396.SZ | 星网锐捷 | ok | 71.81 | ma60_not_above_ma120; volatility_120d 61.10% > 42.00% |
| 301123.SZ | 奕东电子 | ok | 71.80 | volatility_120d 84.28% > 42.00%; distance_ma200 62.16% > 55.00% |
| 603663.SH | 三祥新材 | ok | 71.80 | volatility_120d 66.62% > 42.00%; distance_ma200 86.58% > 55.00% |
| 300936.SZ | 中英科技 | ok | 71.79 | volatility_120d 81.78% > 42.00%; distance_ma200 77.27% > 55.00% |
| 605111.SH | 新洁能 | ok | 71.77 | volatility_120d 61.65% > 42.00%; distance_ma200 83.57% > 55.00% |
| 300209.SZ | 行云科技 | ok | 71.69 | volatility_120d 96.19% > 42.00%; distance_ma200 113.20% > 55.00% |
| 688655.SH | 迅捷兴 | ok | 71.66 | drawdown_120d -41.78% < -28.00%; volatility_120d 94.07% > 42.00% |
| 002297.SZ | 博云新材 | ok | 71.64 | volatility_120d 76.76% > 42.00%; distance_ma200 92.55% > 55.00% |
| 688227.SH | 品高股份 | ok | 71.63 | drawdown_120d -33.26% < -28.00%; volatility_120d 87.16% > 42.00% |
| 301312.SZ | 智立方 | ok | 71.63 | volatility_120d 96.49% > 42.00%; distance_ma200 71.95% > 55.00% |
| 002138.SZ | 顺络电子 | ok | 71.63 | volatility_120d 59.21% > 42.00% |
| 300390.SZ | 天华新能 | ok | 71.61 | volatility_120d 77.97% > 42.00%; distance_ma200 58.53% > 55.00% |
| 688020.SH | 方邦股份 | ok | 71.61 | volatility_120d 97.29% > 42.00%; distance_ma200 120.35% > 55.00% |
| 603283.SH | 赛腾股份 | ok | 71.61 | volatility_120d 62.71% > 42.00%; distance_ma200 71.71% > 55.00% |
| 300776.SZ | 帝尔激光 | ok | 71.60 | volatility_120d 83.13% > 42.00%; distance_ma200 80.74% > 55.00% |
| 688627.SH | 精智达 | ok | 71.59 | volatility_120d 80.70% > 42.00%; distance_ma200 108.56% > 55.00% |
| 603989.SH | 艾华集团 | ok | 71.58 | volatility_120d 69.57% > 42.00%; distance_ma200 108.21% > 55.00% |
| 300478.SZ | 杭州高新 | ok | 71.58 | volatility_120d 54.40% > 42.00% |
| 002348.SZ | 高乐股份 | ok | 71.53 | drawdown_120d -33.69% < -28.00%; volatility_120d 64.77% > 42.00% |
| 300398.SZ | 飞凯材料 | ok | 71.52 | volatility_120d 69.88% > 42.00%; distance_ma200 70.24% > 55.00% |
| 002975.SZ | 博杰股份 | ok | 71.52 | volatility_120d 72.74% > 42.00%; distance_ma200 65.12% > 55.00% |
| 603936.SH | 博敏电子 | ok | 71.51 | drawdown_120d -30.72% < -28.00%; volatility_120d 64.64% > 42.00% |
| 301611.SZ | 珂玛科技 | ok | 71.49 | volatility_120d 86.89% > 42.00%; distance_ma200 56.98% > 55.00% |
| 300570.SZ | 太辰光 | ok | 71.47 | volatility_120d 94.29% > 42.00%; distance_ma200 64.11% > 55.00% |
| 300323.SZ | 华灿光电 | ok | 71.46 | volatility_120d 80.73% > 42.00%; distance_ma200 63.53% > 55.00% |
| 605055.SH | 迎丰股份 | ok | 71.38 | volatility_120d 52.21% > 42.00% |
| 301150.SZ | 中一科技 | ok | 71.35 | volatility_120d 80.11% > 42.00% |
| 688669.SH | 聚石化学 | ok | 71.34 | volatility_120d 71.95% > 42.00%; distance_ma200 186.71% > 55.00% |
| 688003.SH | 天准科技 | ok | 71.33 | volatility_120d 80.58% > 42.00% |
| 000970.SZ | 中科三环 | ok | 71.31 | ma60_not_above_ma120; ma120_not_above_ma200; volatility_120d 49.09% > 42.00% |
| 002409.SZ | 雅克科技 | ok | 71.31 | volatility_120d 68.90% > 42.00%; distance_ma200 103.48% > 55.00% |
| 688625.SH | 呈和科技 | ok | 71.24 | volatility_120d 77.80% > 42.00%; distance_ma200 69.60% > 55.00% |
| 688120.SH | 华海清科 | ok | 71.22 | volatility_120d 64.74% > 42.00%; distance_ma200 99.35% > 55.00% |
| 301349.SZ | 信德新材 | ok | 71.19 | volatility_120d 57.76% > 42.00% |
| 688700.SH | 东威科技 | ok | 71.16 | volatility_120d 75.57% > 42.00% |
| 000404.SZ | 长虹华意 | ok | 71.16 | excess_return_240d 5.17% < 8.00%; volatility_120d 42.22% > 42.00% |
| 301526.SZ | 国际复材 | ok | 71.14 | volatility_120d 104.10% > 42.00%; distance_ma200 208.57% > 55.00% |
| 600330.SH | 天通股份 | ok | 71.06 | drawdown_120d -32.86% < -28.00%; volatility_120d 88.26% > 42.00% |
| 002281.SZ | 光迅科技 | ok | 71.04 | volatility_120d 75.86% > 42.00%; distance_ma200 97.12% > 55.00% |
| 002080.SZ | 中材科技 | ok | 71.04 | volatility_120d 77.27% > 42.00%; distance_ma200 68.09% > 55.00% |
| 688313.SH | 仕佳光子 | ok | 71.01 | drawdown_120d -28.06% < -28.00%; volatility_120d 82.36% > 42.00% |
| 301189.SZ | 奥尼电子 | ok | 70.98 | drawdown_120d -32.58% < -28.00%; volatility_120d 74.83% > 42.00% |
| 688361.SH | 中科飞测 | ok | 70.98 | volatility_120d 72.60% > 42.00%; distance_ma200 99.75% > 55.00% |
| 688170.SH | 德龙激光 | ok | 70.95 | drawdown_120d -29.04% < -28.00%; volatility_120d 81.43% > 42.00% |
| 603083.SH | 剑桥科技 | ok | 70.95 | volatility_120d 77.33% > 42.00% |
| 002842.SZ | 翔鹭钨业 | ok | 70.95 | volatility_120d 87.03% > 42.00%; distance_ma200 63.86% > 55.00% |
| 603738.SH | 泰晶科技 | ok | 70.93 | volatility_120d 76.86% > 42.00%; distance_ma200 98.76% > 55.00% |
| 002552.SZ | 宝鼎科技 | ok | 70.89 | volatility_120d 77.87% > 42.00%; distance_ma200 132.13% > 55.00% |
| 601991.SH | 大唐发电 | ok | 70.89 | volatility_120d 70.14% > 42.00%; distance_ma200 61.40% > 55.00% |
| 688391.SH | 钜泉科技 | ok | 70.86 | excess_return_240d 0.85% < 8.00% |
| 301580.SZ | 爱迪特 | ok | 70.85 | drawdown_120d -31.47% < -28.00%; volatility_120d 87.66% > 42.00% |
| 603790.SH | 雅运股份 | ok | 70.85 | drawdown_120d -29.89% < -28.00%; volatility_120d 55.52% > 42.00% |
| 000510.SZ | 新金路 | ok | 70.84 | volatility_120d 85.51% > 42.00%; distance_ma200 57.89% > 55.00% |
| 002902.SZ | 铭普光磁 | ok | 70.84 | drawdown_120d -37.72% < -28.00%; volatility_120d 68.52% > 42.00% |
| 688571.SH | 杭华股份 | ok | 70.81 | excess_return_240d 6.07% < 8.00%; volatility_120d 56.91% > 42.00% |
| 603045.SH | 福达合金 | ok | 70.80 | volatility_120d 79.53% > 42.00%; distance_ma200 99.47% > 55.00% |
| 300806.SZ | 斯迪克 | ok | 70.80 | volatility_120d 88.05% > 42.00%; distance_ma200 88.36% > 55.00% |
| 603938.SH | 三孚股份 | ok | 70.79 | volatility_120d 81.73% > 42.00%; distance_ma200 113.75% > 55.00% |
| 002859.SZ | 洁美科技 | ok | 70.78 | volatility_120d 75.69% > 42.00%; distance_ma200 97.77% > 55.00% |
| 688409.SH | 富创精密 | ok | 70.75 | volatility_120d 86.48% > 42.00%; distance_ma200 139.10% > 55.00% |
| 300626.SZ | 华瑞股份 | ok | 70.74 | drawdown_120d -35.98% < -28.00%; volatility_120d 86.59% > 42.00% |
| 688545.SH | 兴福电子 | ok | 70.73 | volatility_120d 90.57% > 42.00%; distance_ma200 105.21% > 55.00% |
| 301511.SZ | 德福科技 | ok | 70.70 | volatility_120d 86.61% > 42.00%; distance_ma200 137.71% > 55.00% |
| 000608.SZ | 阳光股份 | ok | 70.70 | volatility_120d 62.03% > 42.00%; distance_ma200 76.22% > 55.00% |
| 300706.SZ | 阿石创 | ok | 70.69 | volatility_120d 79.61% > 42.00%; distance_ma200 60.74% > 55.00% |
| 300721.SZ | 怡达股份 | ok | 70.69 | volatility_120d 98.36% > 42.00%; distance_ma200 71.19% > 55.00% |
| 002354.SZ | 天娱数科 | ok | 70.67 | excess_return_240d 7.61% < 8.00%; volatility_120d 73.28% > 42.00% |
| 603203.SH | 快克智能 | ok | 70.65 | volatility_120d 69.15% > 42.00%; distance_ma200 85.48% > 55.00% |
| 605376.SH | 博迁新材 | ok | 70.65 | volatility_120d 76.51% > 42.00%; distance_ma200 122.56% > 55.00% |
| 600707.SH | 彩虹股份 | ok | 70.60 | volatility_120d 76.40% > 42.00%; distance_ma200 80.70% > 55.00% |
| 601869.SH | 长飞光纤 | ok | 70.59 | volatility_120d 78.92% > 42.00%; distance_ma200 97.84% > 55.00% |
| 688549.SH | 中巨芯 | ok | 70.58 | volatility_120d 97.36% > 42.00%; distance_ma200 159.88% > 55.00% |
| 300164.SZ | 通源石油 | ok | 70.54 | close_below_ma200; ma60_not_above_ma120; drawdown_120d -70.03% < -28.00%; volatility_120d 105.05% > 42.00% |
| 003031.SZ | 中瓷电子 | ok | 70.52 | volatility_120d 72.78% > 42.00%; distance_ma200 66.89% > 55.00% |
| 688167.SH | 炬光科技 | ok | 70.50 | drawdown_120d -33.47% < -28.00%; volatility_120d 103.16% > 42.00% |
| 600206.SH | 有研新材 | ok | 70.47 | volatility_120d 66.00% > 42.00%; distance_ma200 101.94% > 55.00% |
| 003030.SZ | 祖名股份 | ok | 70.44 | excess_return_240d 5.99% < 8.00%; volatility_120d 47.19% > 42.00% |
| 603124.SH | 江南新材 | ok | 70.44 | volatility_120d 66.02% > 42.00% |
| 688268.SH | 华特气体 | ok | 70.42 | volatility_120d 110.54% > 42.00%; distance_ma200 114.34% > 55.00% |
| 600226.SH | 亨通股份 | ok | 70.41 | volatility_120d 59.61% > 42.00%; distance_ma200 60.03% > 55.00% |
| 301196.SZ | 唯科科技 | ok | 70.41 | drawdown_120d -30.14% < -28.00%; volatility_120d 84.57% > 42.00% |
| 688233.SH | 神工股份 | ok | 70.39 | volatility_120d 91.74% > 42.00%; distance_ma200 133.01% > 55.00% |
| 605358.SH | 立昂微 | ok | 70.35 | drawdown_120d -28.57% < -28.00%; volatility_120d 64.51% > 42.00% |
| 301377.SZ | 鼎泰高科 | ok | 70.35 | volatility_120d 77.78% > 42.00%; distance_ma200 143.03% > 55.00% |
| 600500.SH | 中化国际 | ok | 70.34 | drawdown_120d -29.14% < -28.00%; volatility_120d 63.59% > 42.00% |
| 300870.SZ | 欧陆通 | ok | 70.34 | volatility_120d 86.08% > 42.00% |
| 688478.SH | 晶升股份 | ok | 70.29 | volatility_120d 91.68% > 42.00%; distance_ma200 57.97% > 55.00% |
| 688456.SH | 有研粉材 | ok | 70.28 | volatility_120d 75.51% > 42.00%; distance_ma200 80.43% > 55.00% |
| 300975.SZ | 商络电子 | ok | 70.26 | volatility_120d 90.48% > 42.00%; distance_ma200 103.33% > 55.00% |
| 603311.SH | 金海高科 | ok | 70.25 | volatility_120d 65.74% > 42.00%; distance_ma200 74.71% > 55.00% |
| 600397.SH | 江钨装备 | ok | 70.23 | volatility_120d 77.78% > 42.00%; distance_ma200 92.62% > 55.00% |
| 688069.SH | 德林海 | ok | 70.22 | volatility_120d 69.04% > 42.00%; distance_ma200 61.11% > 55.00% |
| 688146.SH |  | ok | 70.22 | volatility_120d 98.11% > 42.00%; distance_ma200 273.58% > 55.00% |
| 688668.SH | 鼎通科技 | ok | 70.21 | volatility_120d 87.62% > 42.00%; distance_ma200 89.90% > 55.00% |
| 601126.SH | 四方股份 | ok | 70.21 | drawdown_120d -30.85% < -28.00%; volatility_120d 70.78% > 42.00% |
| 688551.SH | 科威尔 | ok | 70.17 | volatility_120d 88.53% > 42.00%; distance_ma200 56.65% > 55.00% |
| 600186.SH | 莲花控股 | ok | 70.16 | volatility_120d 77.38% > 42.00% |
| 000026.SZ | 飞亚达 | ok | 70.15 | volatility_120d 53.38% > 42.00% |
| 300283.SZ | 温州宏丰 | ok | 70.15 | volatility_120d 82.62% > 42.00%; distance_ma200 86.88% > 55.00% |
| 300136.SZ | 信维通信 | ok | 70.13 | volatility_120d 88.25% > 42.00% |
| 688001.SH | 华兴源创 | ok | 70.10 | volatility_120d 85.30% > 42.00%; distance_ma200 67.75% > 55.00% |
| 688307.SH | 中润光学 | ok | 70.10 | drawdown_120d -35.18% < -28.00%; volatility_120d 85.40% > 42.00% |
| 600379.SH | 宝光股份 | ok | 70.08 | volatility_120d 65.00% > 42.00% |
| 301203.SZ | 国泰环保 | ok | 70.06 | excess_return_240d 6.61% < 8.00% |
| 603256.SH | 宏和科技 | ok | 70.05 | volatility_120d 82.61% > 42.00%; distance_ma200 163.09% > 55.00% |
| 301338.SZ | 凯格精机 | ok | 70.03 | volatility_120d 90.41% > 42.00% |
| 603629.SH | 利通电子 | ok | 70.00 | drawdown_120d -28.22% < -28.00%; volatility_120d 95.06% > 42.00%; distance_ma200 138.46% > 55.00% |
| 301362.SZ | 民爆光电 | ok | 70.00 | drawdown_120d -40.19% < -28.00%; volatility_120d 102.74% > 42.00%; distance_ma200 104.43% > 55.00% |
| 688308.SH | 欧科亿 | ok | 70.00 | drawdown_120d -28.88% < -28.00%; volatility_120d 101.56% > 42.00%; distance_ma200 117.15% > 55.00% |
| 600396.SH | 华电辽能 | ok | 70.00 | drawdown_120d -45.05% < -28.00%; volatility_120d 90.67% > 42.00%; distance_ma200 86.08% > 55.00% |
| 301373.SZ | 凌玮科技 | ok | 70.00 | drawdown_120d -34.13% < -28.00%; volatility_120d 107.43% > 42.00%; distance_ma200 100.73% > 55.00% |
| 301217.SZ | 铜冠铜箔 | ok | 70.00 | drawdown_120d -28.68% < -28.00%; volatility_120d 93.61% > 42.00%; distance_ma200 159.57% > 55.00% |
| 002931.SZ | 锋龙股份 | ok | 70.00 | ma60_not_above_ma120; drawdown_120d -32.60% < -28.00%; volatility_120d 92.74% > 42.00%; distance_ma200 72.63% > 55.00% |
| 002491.SZ | 通鼎互联 | ok | 70.00 | drawdown_120d -39.23% < -28.00%; volatility_120d 93.79% > 42.00%; distance_ma200 101.55% > 55.00% |
| 603186.SH | 华正新材 | ok | 70.00 | drawdown_120d -30.88% < -28.00%; volatility_120d 73.77% > 42.00%; distance_ma200 142.40% > 55.00% |
| 301319.SZ | 唯特偶 | ok | 70.00 | drawdown_120d -37.75% < -28.00%; volatility_120d 96.62% > 42.00%; distance_ma200 171.73% > 55.00% |
| 000636.SZ | 风华高科 | ok | 70.00 | drawdown_120d -30.36% < -28.00%; volatility_120d 75.19% > 42.00%; distance_ma200 124.76% > 55.00% |
| 603773.SH | 沃格光电 | ok | 70.00 | drawdown_120d -34.37% < -28.00%; volatility_120d 92.27% > 42.00%; distance_ma200 126.36% > 55.00% |
| 600487.SH | 亨通光电 | ok | 70.00 | drawdown_120d -32.26% < -28.00%; volatility_120d 78.99% > 42.00%; distance_ma200 88.79% > 55.00% |
| 688143.SH | 长盈通 | ok | 70.00 | drawdown_120d -40.67% < -28.00%; volatility_120d 101.29% > 42.00%; distance_ma200 111.50% > 55.00% |
| 600869.SH | 远东股份 | ok | 70.00 | drawdown_120d -33.62% < -28.00%; volatility_120d 77.49% > 42.00%; distance_ma200 83.62% > 55.00% |
| 001896.SZ | 豫能控股 | ok | 70.00 | drawdown_120d -31.32% < -28.00%; volatility_120d 90.23% > 42.00%; distance_ma200 55.45% > 55.00% |
| 688260.SH | 昀冢科技 | ok | 70.00 | drawdown_120d -36.45% < -28.00%; volatility_120d 108.38% > 42.00%; distance_ma200 127.36% > 55.00% |
| 688662.SH | 富信科技 | ok | 70.00 | drawdown_120d -39.55% < -28.00%; volatility_120d 102.95% > 42.00%; distance_ma200 132.61% > 55.00% |
| 688300.SH | 联瑞新材 | ok | 70.00 | drawdown_120d -35.42% < -28.00%; volatility_120d 88.30% > 42.00%; distance_ma200 112.44% > 55.00% |
| 688610.SH | 埃科光电 | ok | 70.00 | drawdown_120d -28.29% < -28.00%; volatility_120d 90.86% > 42.00%; distance_ma200 86.33% > 55.00% |
| 000657.SZ | 中钨高新 | ok | 70.00 | drawdown_120d -29.27% < -28.00%; volatility_120d 77.89% > 42.00%; distance_ma200 82.17% > 55.00% |
| 600367.SH | 红星发展 | ok | 70.00 | drawdown_120d -28.18% < -28.00%; volatility_120d 78.38% > 42.00%; distance_ma200 98.70% > 55.00% |
| 300835.SZ | 龙磁科技 | ok | 70.00 | drawdown_120d -32.44% < -28.00%; volatility_120d 93.06% > 42.00%; distance_ma200 88.91% > 55.00% |
| 301188.SZ | 力诺药包 | ok | 70.00 | drawdown_120d -38.35% < -28.00%; volatility_120d 91.09% > 42.00%; distance_ma200 86.92% > 55.00% |
| 600726.SH | 华电能源 | ok | 70.00 | drawdown_120d -41.78% < -28.00%; volatility_120d 82.77% > 42.00% |
| 600522.SH | 中天科技 | ok | 70.00 | drawdown_120d -29.47% < -28.00%; volatility_120d 71.28% > 42.00%; distance_ma200 76.25% > 55.00% |
| 300302.SZ | 同有科技 | ok | 70.00 | drawdown_120d -28.74% < -28.00%; volatility_120d 88.54% > 42.00%; distance_ma200 67.62% > 55.00% |
| 688693.SH | 锴威特 | ok | 70.00 | drawdown_120d -39.38% < -28.00%; volatility_120d 90.08% > 42.00% |
| 300672.SZ | 国科微 | ok | 70.00 | drawdown_120d -31.35% < -28.00%; volatility_120d 82.43% > 42.00%; distance_ma200 64.57% > 55.00% |
| 605006.SH | 山东玻纤 | ok | 70.00 | drawdown_120d -34.76% < -28.00%; volatility_120d 83.98% > 42.00%; distance_ma200 62.65% > 55.00% |
| 600545.SH | 卓郎智能 | ok | 70.00 | drawdown_120d -29.15% < -28.00%; volatility_120d 84.66% > 42.00% |
| 301176.SZ | 逸豪新材 | ok | 70.00 | drawdown_120d -31.95% < -28.00%; volatility_120d 91.66% > 42.00%; distance_ma200 71.23% > 55.00% |
| 688757.SH | 胜科纳米 | ok | 70.00 | drawdown_120d -28.23% < -28.00%; volatility_120d 73.43% > 42.00%; distance_ma200 75.67% > 55.00% |
| 001259.SZ | 利仁科技 | ok | 70.00 | drawdown_120d -29.08% < -28.00%; volatility_120d 67.58% > 42.00%; distance_ma200 67.96% > 55.00% |
| 002957.SZ | 科瑞技术 | ok | 70.00 | drawdown_120d -37.10% < -28.00%; volatility_120d 75.15% > 42.00% |
| 688507.SH | 索辰科技 | ok | 70.00 | drawdown_120d -30.91% < -28.00%; volatility_120d 96.84% > 42.00%; distance_ma200 79.31% > 55.00% |
| 000962.SZ | 东方钽业 | ok | 70.00 | drawdown_120d -29.34% < -28.00%; volatility_120d 78.82% > 42.00%; distance_ma200 63.63% > 55.00% |
| 300319.SZ | 麦捷科技 | ok | 70.00 | drawdown_120d -28.47% < -28.00%; volatility_120d 70.51% > 42.00%; distance_ma200 70.72% > 55.00% |
| 688079.SH | 美迪凯 | ok | 70.00 | drawdown_120d -31.43% < -28.00%; volatility_120d 88.16% > 42.00% |
| 301021.SZ | 英诺激光 | ok | 70.00 | drawdown_120d -28.91% < -28.00%; volatility_120d 75.84% > 42.00%; distance_ma200 70.59% > 55.00% |
| 301013.SZ | 利和兴 | ok | 70.00 | drawdown_120d -33.94% < -28.00%; volatility_120d 87.27% > 42.00%; distance_ma200 80.16% > 55.00% |
| 300620.SZ | 光库科技 | ok | 70.00 | drawdown_120d -28.21% < -28.00%; volatility_120d 89.05% > 42.00%; distance_ma200 58.81% > 55.00% |
| 002645.SZ | 华宏科技 | ok | 70.00 | drawdown_120d -33.41% < -28.00%; volatility_120d 71.85% > 42.00% |
| 688603.SH | 天承科技 | ok | 70.00 | drawdown_120d -29.74% < -28.00%; volatility_120d 92.00% > 42.00% |
| 600105.SH | 永鼎股份 | ok | 70.00 | drawdown_120d -32.34% < -28.00%; volatility_120d 77.47% > 42.00%; distance_ma200 68.60% > 55.00% |
| 300069.SZ | 金利华电 | ok | 70.00 | drawdown_120d -43.76% < -28.00%; volatility_120d 83.22% > 42.00% |
| 688106.SH | 金宏气体 | ok | 70.00 | drawdown_120d -28.93% < -28.00%; volatility_120d 86.85% > 42.00% |
| 600552.SH | 凯盛科技 | ok | 70.00 | drawdown_120d -30.06% < -28.00%; volatility_120d 69.05% > 42.00%; distance_ma200 60.35% > 55.00% |
| 300819.SZ | 聚杰微纤 | ok | 70.00 | drawdown_120d -29.70% < -28.00%; volatility_120d 89.91% > 42.00% |
| 688323.SH | 瑞华泰 | ok | 70.00 | drawdown_120d -42.81% < -28.00%; volatility_120d 110.59% > 42.00%; distance_ma200 67.53% > 55.00% |
| 688598.SH | 金博股份 | ok | 70.00 | ma120_not_above_ma200; drawdown_120d -28.02% < -28.00%; volatility_120d 73.15% > 42.00% |
| 002328.SZ | 新朋股份 | ok | 69.82 | drawdown_120d -43.33% < -28.00%; volatility_120d 58.08% > 42.00% |
| 300505.SZ | 川金诺 | ok | 69.67 | ma60_not_above_ma120; drawdown_120d -34.84% < -28.00%; volatility_120d 72.53% > 42.00% |
| 300270.SZ | 中威电子 | ok | 69.57 | volatility_120d 61.00% > 42.00% |
| 002155.SZ | 湖南黄金 | ok | 69.53 | close_below_ma200; ma60_not_above_ma120; drawdown_120d -44.15% < -28.00%; volatility_120d 68.18% > 42.00% |
| 603318.SH | 水发燃气 | ok | 69.51 | excess_return_240d 7.86% < 8.00%; drawdown_120d -42.85% < -28.00%; volatility_120d 76.76% > 42.00% |
| 301210.SZ | 金杨精密 | ok | 69.45 | ma120_not_above_ma200; excess_return_240d -11.97% < 8.00%; volatility_120d 43.88% > 42.00% |
| 000415.SZ | 渤海租赁 | ok | 69.41 | ma60_not_above_ma120; volatility_120d 46.71% > 42.00% |
| 002887.SZ | 绿茵生态 | ok | 69.31 | drawdown_120d -32.23% < -28.00%; volatility_120d 45.18% > 42.00% |
| 300656.SZ | 民德电子 | ok | 69.20 | volatility_120d 71.27% > 42.00% |
| 601975.SH | 招商南油 | ok | 69.18 | close_below_ma200; drawdown_120d -37.38% < -28.00%; volatility_120d 68.52% > 42.00% |
| 603928.SH | 兴业股份 | ok | 68.88 | ma120_not_above_ma200; excess_return_240d 2.65% < 8.00%; volatility_120d 48.24% > 42.00% |
| 301446.SZ | 福事特 | ok | 68.85 | close_below_ma200; drawdown_120d -30.05% < -28.00%; volatility_120d 59.22% > 42.00% |
| 603519.SH | 立霸股份 | ok | 68.83 | excess_return_240d -2.83% < 8.00% |
| 688197.SH | 首药控股 | ok | 68.81 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_240d -7.13% < 8.00%; volatility_120d 56.47% > 42.00% |
| 605580.SH | 恒盛能源 | ok | 68.77 | close_below_ma200; ma120_not_above_ma200; volatility_120d 64.57% > 42.00% |
| 300853.SZ | 申昊科技 | ok | 68.75 | excess_return_240d 7.87% < 8.00%; volatility_120d 69.16% > 42.00% |
| 600676.SH | 交运股份 | ok | 68.72 | close_below_ma200; ma60_not_above_ma120; drawdown_120d -33.50% < -28.00%; volatility_120d 58.79% > 42.00% |
| 300334.SZ | 津膜科技 | ok | 68.61 | drawdown_120d -31.87% < -28.00%; volatility_120d 57.35% > 42.00% |
| 300481.SZ | 濮阳惠成 | ok | 68.54 | ma60_not_above_ma120; excess_return_240d 6.36% < 8.00%; volatility_120d 62.20% > 42.00% |
| 301259.SZ | 艾布鲁 | ok | 68.45 | ma120_not_above_ma200; excess_return_240d -35.37% < 8.00%; volatility_120d 54.69% > 42.00% |
| 301358.SZ | 湖南裕能 | ok | 68.44 | drawdown_120d -33.07% < -28.00%; volatility_120d 59.11% > 42.00% |
| 001286.SZ | 陕西能源 | ok | 68.28 | excess_return_240d 4.72% < 8.00% |
| 603339.SH | 四方科技 | ok | 68.11 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_240d 0.65% < 8.00% |
| 300165.SZ | 天瑞仪器 | ok | 67.97 | drawdown_120d -40.72% < -28.00%; volatility_120d 59.16% > 42.00% |
| 688711.SH | 宏微科技 | ok | 67.89 | volatility_120d 76.71% > 42.00% |
| 000062.SZ | 深圳华强 | ok | 67.88 | excess_return_240d 3.35% < 8.00%; volatility_120d 64.65% > 42.00% |
| 688665.SH | 四方光电 | ok | 67.79 | ma120_not_above_ma200; excess_return_240d 4.52% < 8.00%; volatility_120d 45.67% > 42.00% |
| 688623.SH | 双元科技 | ok | 67.76 | ma60_not_above_ma120; volatility_120d 43.21% > 42.00% |
| 300932.SZ | 三友联众 | ok | 67.72 | excess_return_240d 3.12% < 8.00%; volatility_120d 58.96% > 42.00% |
| 002141.SZ | 贤丰控股 | ok | 67.70 | ma60_not_above_ma120; excess_return_240d 6.16% < 8.00%; volatility_120d 64.03% > 42.00% |
| 002077.SZ | 大港股份 | ok | 67.70 | excess_return_240d 3.73% < 8.00%; volatility_120d 48.04% > 42.00% |
| 002106.SZ | 莱宝高科 | ok | 67.69 | excess_return_240d 6.64% < 8.00%; drawdown_120d -28.23% < -28.00%; volatility_120d 55.75% > 42.00% |
| 603669.SH | 灵康药业 | ok | 67.60 | ma120_not_above_ma200; excess_return_240d -15.62% < 8.00% |
| 002457.SZ | 青龙管业 | ok | 67.51 | excess_return_240d -4.64% < 8.00%; volatility_120d 51.00% > 42.00% |
| 600152.SH | 维科技术 | ok | 67.47 | close_below_ma200; excess_return_240d 7.92% < 8.00%; drawdown_120d -45.43% < -28.00%; volatility_120d 72.06% > 42.00% |
| 688105.SH | 诺唯赞 | ok | 67.44 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_240d -13.70% < 8.00%; volatility_120d 49.06% > 42.00% |
| 600322.SH | 津投城开 | ok | 67.34 | ma120_not_above_ma200; excess_return_240d -20.07% < 8.00%; volatility_120d 50.57% > 42.00% |
| 301348.SZ | 蓝箭电子 | ok | 67.30 | ma60_not_above_ma120; excess_return_240d 6.37% < 8.00%; drawdown_120d -30.21% < -28.00%; volatility_120d 74.23% > 42.00% |
| 688428.SH | 诺诚健华 | ok | 67.14 | ma120_not_above_ma200; excess_return_240d -1.16% < 8.00%; volatility_120d 50.57% > 42.00% |
| 300889.SZ | 爱克股份 | ok | 67.12 | ma60_not_above_ma120; volatility_120d 49.42% > 42.00% |
| 002179.SZ | 中航光电 | ok | 67.10 | excess_return_240d -9.96% < 8.00%; volatility_120d 44.59% > 42.00% |
| 603722.SH | 阿科力 | ok | 67.09 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_240d -21.95% < 8.00%; volatility_120d 45.72% > 42.00% |
| 601838.SH | 成都银行 | ok | 67.07 | excess_return_240d -25.54% < 8.00% |
| 603777.SH | 来伊份 | ok | 67.06 | excess_return_240d 4.87% < 8.00%; volatility_120d 54.24% > 42.00% |
| 300948.SZ | 冠中生态 | ok | 67.03 | volatility_120d 64.06% > 42.00% |
| 603270.SH | 金帝股份 | ok | 66.90 | excess_return_240d 5.92% < 8.00% |
| 002216.SZ | 三全食品 | ok | 66.68 | excess_return_240d 0.07% < 8.00% |
| 000007.SZ | 全新好 | ok | 66.63 | volatility_120d 52.06% > 42.00% |
| 001314.SZ | 亿道信息 | ok | 66.57 | excess_return_240d -2.44% < 8.00%; volatility_120d 50.42% > 42.00% |
| 002876.SZ | 三利谱 | ok | 66.42 | excess_return_240d 0.07% < 8.00%; volatility_120d 49.07% > 42.00% |
| 003022.SZ | 联泓新科 | ok | 66.27 | volatility_120d 49.71% > 42.00% |
| 301617.SZ | 博苑新材 | ok | 66.08 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_120d 4.99% < 6.00%; volatility_120d 54.64% > 42.00% |
| 688721.SH | 龙图光罩 | ok | 66.05 | ma120_not_above_ma200; excess_return_240d 5.43% < 8.00%; volatility_120d 64.22% > 42.00% |
| 688375.SH | 国博电子 | ok | 66.03 | ma60_not_above_ma120; drawdown_120d -41.21% < -28.00%; volatility_120d 75.66% > 42.00% |
| 688799.SH | 华纳药厂 | ok | 65.98 | ma120_not_above_ma200; excess_return_240d -3.77% < 8.00%; volatility_120d 53.20% > 42.00% |
| 600722.SH | 金牛化工 | ok | 65.95 | close_below_ma200; drawdown_120d -59.29% < -28.00%; volatility_120d 80.02% > 42.00% |
| 605118.SH | 力鼎光电 | ok | 65.70 | close_below_ma200; ma60_not_above_ma120; drawdown_120d -30.19% < -28.00%; volatility_120d 52.49% > 42.00% |
| 688266.SH | 泽璟制药 | ok | 65.62 | ma120_not_above_ma200; excess_return_240d 5.95% < 8.00%; volatility_120d 53.60% > 42.00% |
| 600971.SH | 恒源煤电 | ok | 65.57 | excess_return_240d -7.75% < 8.00% |
| 002520.SZ | 日发精机 | ok | 65.56 | ma120_not_above_ma200; excess_return_240d -7.15% < 8.00%; volatility_120d 54.60% > 42.00% |
| 688199.SH | 久日新材 | ok | 65.53 | excess_return_240d -9.39% < 8.00%; volatility_120d 50.34% > 42.00% |
| 605377.SH | 华旺科技 | ok | 65.49 | excess_return_240d -6.84% < 8.00%; volatility_120d 42.09% > 42.00% |
| 688187.SH | 时代电气 | ok | 65.39 | volatility_120d 55.45% > 42.00% |
| 300986.SZ | 志特新材 | ok | 65.37 | close_below_ma200; ma60_not_above_ma120; drawdown_120d -62.11% < -28.00%; volatility_120d 106.62% > 42.00% |
| 603009.SH | 北特科技 | ok | 65.37 | ma60_not_above_ma120; excess_return_120d 5.58% < 6.00%; volatility_120d 50.18% > 42.00% |
| 002833.SZ | 弘亚数控 | ok | 65.36 | excess_return_240d 1.29% < 8.00% |
| 688071.SH | 华依科技 | ok | 65.34 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_240d -3.01% < 8.00%; volatility_120d 61.70% > 42.00% |
| 301520.SZ | 万邦医药 | ok | 65.32 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_240d 0.97% < 8.00%; volatility_120d 53.34% > 42.00% |
| 002137.SZ | 实益达 | ok | 65.20 | excess_return_240d -0.84% < 8.00%; volatility_120d 50.67% > 42.00% |
| 688211.SH | 中科微至 | ok | 65.20 | excess_return_240d -8.04% < 8.00% |
| 301251.SZ | 威尔高 | ok | 65.16 | close_below_ma200; volatility_120d 67.56% > 42.00% |
| 603019.SH | 中科曙光 | ok | 65.15 | ma120_not_above_ma200; volatility_120d 46.80% > 42.00% |
| 001226.SZ | 拓山重工 | ok | 65.08 | excess_return_120d 5.26% < 6.00%; volatility_120d 44.73% > 42.00% |
| 600458.SH | 时代新材 | ok | 64.98 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_240d -3.54% < 8.00%; volatility_120d 46.12% > 42.00% |
| 002392.SZ | 北京利尔 | ok | 64.87 | ma120_not_above_ma200; volatility_120d 53.93% > 42.00% |
| 603776.SH | 永安行 | ok | 64.81 | excess_return_240d -22.96% < 8.00% |
| 688358.SH | 祥生医疗 | ok | 64.78 | ma60_not_above_ma120; excess_return_240d 2.85% < 8.00%; volatility_120d 55.02% > 42.00% |
| 002028.SZ | 思源电气 | ok | 64.77 | ma60_not_above_ma120; volatility_120d 56.67% > 42.00% |
| 603466.SH | 风语筑 | ok | 64.63 | excess_return_240d -3.74% < 8.00%; volatility_120d 62.84% > 42.00% |
| 605007.SH | 五洲特纸 | ok | 64.56 | ma60_not_above_ma120; volatility_120d 46.00% > 42.00% |
| 603861.SH | 白云电器 | ok | 64.56 | close_below_ma200; ma60_not_above_ma120; drawdown_120d -38.93% < -28.00%; volatility_120d 67.51% > 42.00% |
| 002628.SZ | 成都路桥 | ok | 64.54 | excess_return_240d -0.60% < 8.00%; volatility_120d 52.07% > 42.00% |
| 300501.SZ | 海顺新材 | ok | 64.51 | excess_return_240d -10.09% < 8.00%; volatility_120d 46.15% > 42.00% |
| 603056.SH | 德邦股份 | ok | 64.50 | ma60_not_above_ma120; excess_return_120d 4.21% < 6.00% |
| 300737.SZ | 科顺股份 | ok | 64.44 | excess_return_240d 5.16% < 8.00%; drawdown_120d -30.20% < -28.00%; volatility_120d 81.36% > 42.00% |
| 000949.SZ | 新乡化纤 | ok | 64.44 | drawdown_120d -30.48% < -28.00%; volatility_120d 62.05% > 42.00% |
| 600578.SH | 京能电力 | ok | 64.42 | excess_return_240d 6.20% < 8.00%; drawdown_120d -40.60% < -28.00%; volatility_120d 64.28% > 42.00% |
| 301297.SZ | 富乐德 | ok | 64.37 | excess_return_240d 4.19% < 8.00%; volatility_120d 58.74% > 42.00% |
| 300416.SZ | 苏试试验 | ok | 64.35 | excess_return_120d 5.09% < 6.00%; volatility_120d 53.96% > 42.00% |
| 301127.SZ | 武汉天源 | ok | 64.30 | ma60_not_above_ma120; excess_return_240d -2.06% < 8.00%; volatility_120d 61.03% > 42.00% |
| 603679.SH | 华体科技 | ok | 64.28 | excess_return_240d 7.96% < 8.00%; volatility_120d 48.53% > 42.00% |
| 300681.SZ | 英搏尔 | ok | 64.23 | ma120_not_above_ma200; excess_return_240d -7.01% < 8.00%; volatility_120d 45.54% > 42.00% |
| 688595.SH | 芯海科技 | ok | 64.22 | excess_return_240d -12.69% < 8.00%; volatility_120d 60.44% > 42.00% |
| 600060.SH | 海信视像 | ok | 64.13 | ma120_not_above_ma200; excess_return_240d -0.23% < 8.00% |
| 001218.SZ | 丽臣实业 | ok | 64.00 | excess_return_120d 5.59% < 6.00%; volatility_120d 42.60% > 42.00% |
| 688310.SH | 迈得医疗 | ok | 63.97 | ma120_not_above_ma200; excess_return_240d -10.17% < 8.00%; volatility_120d 44.71% > 42.00% |
| 600906.SH | 财达证券 | ok | 63.97 | ma120_not_above_ma200; excess_return_240d -10.61% < 8.00% |
| 002475.SZ | 立讯精密 | ok | 63.85 | volatility_120d 55.59% > 42.00% |
| 600488.SH | 津药药业 | ok | 63.84 | excess_return_240d 2.49% < 8.00%; drawdown_120d -35.43% < -28.00%; volatility_120d 76.49% > 42.00% |
| 603826.SH | 坤彩科技 | ok | 63.83 | excess_return_240d 3.13% < 8.00%; drawdown_120d -35.63% < -28.00%; volatility_120d 58.12% > 42.00% |
| 301371.SZ | 敷尔佳 | ok | 63.52 | excess_return_240d -11.41% < 8.00% |
| 002039.SZ | 黔源电力 | ok | 63.47 | excess_return_240d 6.77% < 8.00% |
| 300537.SZ | 广信材料 | ok | 63.47 | excess_return_240d -14.73% < 8.00%; volatility_120d 58.04% > 42.00% |
| 300142.SZ | 沃森生物 | ok | 63.33 | excess_return_240d -0.71% < 8.00%; volatility_120d 53.36% > 42.00% |
| 300558.SZ | 贝达药业 | ok | 63.30 | ma120_not_above_ma200; excess_return_240d 1.28% < 8.00%; volatility_120d 50.55% > 42.00% |
| 300077.SZ | 国民技术 | ok | 63.24 | excess_return_240d -7.66% < 8.00%; volatility_120d 67.68% > 42.00% |
| 300345.SZ | 华民股份 | ok | 63.09 | ma60_not_above_ma120; excess_return_240d -22.51% < 8.00%; volatility_120d 76.37% > 42.00% |
| 688633.SH | 星球石墨 | ok | 63.06 | excess_return_240d -7.35% < 8.00%; volatility_120d 56.33% > 42.00% |
| 002068.SZ | 黑猫股份 | ok | 62.99 | ma120_not_above_ma200; excess_return_240d 2.98% < 8.00%; volatility_120d 57.83% > 42.00% |
| 301132.SZ | 满坤科技 | ok | 62.99 | excess_return_240d 1.25% < 8.00%; volatility_120d 64.39% > 42.00% |
| 000539.SZ | 粤电力A | ok | 62.97 | excess_return_240d 1.39% < 8.00%; drawdown_120d -37.88% < -28.00%; volatility_120d 71.25% > 42.00% |
| 603330.SH | 天洋新材 | ok | 62.94 | ma120_not_above_ma200; excess_return_240d -0.31% < 8.00%; volatility_120d 54.76% > 42.00% |
| 300065.SZ | 海兰信 | ok | 62.87 | ma60_not_above_ma120; excess_return_240d 2.92% < 8.00%; drawdown_120d -29.60% < -28.00%; volatility_120d 71.93% > 42.00% |
| 002687.SZ | 乔治白 | ok | 62.67 | ma60_not_above_ma120; excess_return_240d -2.21% < 8.00%; volatility_120d 45.04% > 42.00% |
| 300687.SZ | 赛意信息 | ok | 62.49 | ma120_not_above_ma200; excess_return_240d -10.62% < 8.00%; volatility_120d 74.09% > 42.00% |
| 603661.SH | 恒林股份 | ok | 62.27 | excess_return_240d 2.21% < 8.00%; volatility_120d 53.59% > 42.00% |
| 600012.SH | 皖通高速 | ok | 62.18 | excess_return_240d -18.51% < 8.00% |
| 688129.SH | 东来技术 | ok | 62.15 | excess_return_240d -26.94% < 8.00%; volatility_120d 48.84% > 42.00% |
| 300571.SZ | 平治信息 | ok | 62.13 | excess_return_240d 0.62% < 8.00%; drawdown_120d -46.66% < -28.00%; volatility_120d 85.99% > 42.00% |
| 000100.SZ | TCL科技 | ok | 62.08 | ma60_not_above_ma120; excess_return_240d 1.02% < 8.00%; volatility_120d 48.09% > 42.00% |
| 300545.SZ | 联得装备 | ok | 61.96 | excess_return_240d -2.55% < 8.00%; volatility_120d 62.93% > 42.00% |
| 300998.SZ | 宁波方正 | ok | 61.95 | excess_return_240d -6.40% < 8.00%; volatility_120d 43.40% > 42.00% |
| 600919.SH | 江苏银行 | ok | 61.80 | excess_return_240d -24.61% < 8.00% |
| 603903.SH | 中持股份 | ok | 61.79 | ma120_not_above_ma200; excess_return_120d 2.43% < 6.00%; volatility_120d 54.51% > 42.00% |
| 000791.SZ | 甘肃能源 | ok | 61.70 | excess_return_240d -0.22% < 8.00%; volatility_120d 58.66% > 42.00% |
| 301148.SZ | 嘉戎技术 | ok | 61.67 | drawdown_120d -39.97% < -28.00%; volatility_120d 61.98% > 42.00% |
| 300536.SZ | 农尚环境 | ok | 61.66 | excess_return_240d -13.38% < 8.00%; drawdown_120d -31.86% < -28.00%; volatility_120d 66.50% > 42.00% |
| 300723.SZ | 一品红 | ok | 61.59 | close_below_ma200; ma120_not_above_ma200; excess_return_240d -40.79% < 8.00%; volatility_120d 63.00% > 42.00% |
| 601677.SH | 明泰铝业 | ok | 61.56 | volatility_120d 44.51% > 42.00% |
| 301197.SZ | 工大科雅 | ok | 61.49 | excess_return_240d -8.39% < 8.00%; drawdown_120d -36.40% < -28.00%; volatility_120d 75.35% > 42.00% |
| 601100.SH | 恒立液压 | ok | 61.30 | ma60_not_above_ma120; excess_return_120d 2.33% < 6.00%; volatility_120d 47.17% > 42.00% |
| 603727.SH | 博迈科 | ok | 61.24 | ma60_not_above_ma120; excess_return_240d -4.78% < 8.00%; volatility_120d 57.82% > 42.00% |
| 688518.SH | 联赢激光 | ok | 61.19 | volatility_120d 59.95% > 42.00% |
| 300825.SZ | 阿尔特 | ok | 61.19 | excess_return_240d -2.44% < 8.00%; drawdown_120d -30.82% < -28.00%; volatility_120d 56.78% > 42.00% |
| 605016.SH | 百龙创园 | ok | 61.09 | excess_return_240d -1.40% < 8.00%; volatility_120d 44.32% > 42.00% |
| 002843.SZ | 泰嘉股份 | ok | 61.07 | excess_return_240d -3.37% < 8.00%; volatility_120d 69.10% > 42.00% |
| 688277.SH | 天智航 | ok | 61.03 | close_below_ma200; ma60_not_above_ma120; excess_return_240d 5.68% < 8.00%; drawdown_120d -37.42% < -28.00%; volatility_120d 67.69% > 42.00% |
| 688117.SH | 圣诺生物 | ok | 61.02 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_240d -0.16% < 8.00%; volatility_120d 45.35% > 42.00% |
| 300586.SZ | 美联新材 | ok | 60.99 | excess_return_240d -3.34% < 8.00%; volatility_120d 61.97% > 42.00% |
| 300767.SZ | 震安科技 | ok | 60.96 | ma120_not_above_ma200; excess_return_120d 4.22% < 6.00%; volatility_120d 52.23% > 42.00% |
| 688237.SH | 超卓航科 | ok | 60.91 | ma120_not_above_ma200; excess_return_120d 4.14% < 6.00%; volatility_120d 43.05% > 42.00% |
| 300599.SZ | 雄塑科技 | ok | 60.78 | excess_return_240d -2.15% < 8.00%; drawdown_120d -28.45% < -28.00%; volatility_120d 57.69% > 42.00% |
| 002129.SZ | TCL中环 | ok | 60.77 | ma60_not_above_ma120; excess_return_240d 0.65% < 8.00%; volatility_120d 56.49% > 42.00% |
| 603980.SH | 吉华集团 | ok | 60.64 | ma60_not_above_ma120; excess_return_240d -9.49% < 8.00%; drawdown_120d -28.86% < -28.00%; volatility_120d 51.90% > 42.00% |
| 688516.SH | 奥特维 | ok | 60.56 | close_below_ma200; ma60_not_above_ma120; drawdown_120d -60.13% < -28.00%; volatility_120d 79.23% > 42.00% |
| 301161.SZ | 唯万密封 | ok | 60.35 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_120d 2.47% < 6.00%; volatility_120d 47.03% > 42.00% |
| 603373.SH | 安邦护卫 | ok | 60.35 | ma120_not_above_ma200; excess_return_240d -12.10% < 8.00%; volatility_120d 52.67% > 42.00% |
| 600449.SH | 宁夏建材 | ok | 60.18 | excess_return_240d -15.52% < 8.00% |
| 002081.SZ | 金螳螂 | ok | 60.16 | excess_return_240d -1.21% < 8.00%; drawdown_120d -50.89% < -28.00%; volatility_120d 75.53% > 42.00% |
| 605018.SH | 长华集团 | ok | 60.13 | excess_return_240d -2.48% < 8.00%; drawdown_120d -30.54% < -28.00%; volatility_120d 49.47% > 42.00% |
| 688096.SH | 京源环保 | ok | 60.13 | excess_return_240d -35.90% < 8.00%; drawdown_120d -36.45% < -28.00%; volatility_120d 76.54% > 42.00% |
| 301230.SZ | 泓博医药 | ok | 60.10 | ma60_not_above_ma120; excess_return_240d -8.04% < 8.00%; drawdown_120d -41.81% < -28.00%; volatility_120d 80.92% > 42.00% |
| 300429.SZ | 强力新材 | ok | 60.03 | excess_return_240d -11.84% < 8.00%; volatility_120d 52.01% > 42.00% |
| 300120.SZ | 经纬辉开 | ok | 59.98 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_240d -15.96% < 8.00%; volatility_120d 50.77% > 42.00% |
| 002015.SZ | 协鑫能科 | ok | 59.91 | excess_return_240d -12.72% < 8.00%; drawdown_120d -40.98% < -28.00%; volatility_120d 72.81% > 42.00% |
| 603132.SH | 金徽股份 | ok | 59.84 | drawdown_120d -31.13% < -28.00%; volatility_120d 56.05% > 42.00% |
| 603213.SH | 镇洋发展 | ok | 59.84 | excess_return_120d 5.36% < 6.00%; excess_return_240d 6.60% < 8.00% |
| 002782.SZ | 可立克 | ok | 59.83 | close_below_ma200; drawdown_120d -35.89% < -28.00%; volatility_120d 69.85% > 42.00% |
| 301290.SZ | 东星医疗 | ok | 59.80 | excess_return_240d -6.43% < 8.00%; volatility_120d 44.19% > 42.00% |
| 688355.SH | 明志科技 | ok | 59.80 | excess_return_240d -3.54% < 8.00%; volatility_120d 55.91% > 42.00% |
| 000601.SZ | 韶能股份 | ok | 59.76 | excess_return_240d -6.61% < 8.00%; volatility_120d 74.71% > 42.00% |
| 300845.SZ | 捷安高科 | ok | 59.66 | excess_return_240d -1.25% < 8.00%; volatility_120d 43.03% > 42.00% |
| 601225.SH | 陕西煤业 | ok | 59.55 | excess_return_240d 5.87% < 8.00% |
| 300877.SZ | 金春股份 | ok | 59.31 | excess_return_120d 2.67% < 6.00%; volatility_120d 61.23% > 42.00% |
| 001223.SZ | 欧克科技 | ok | 59.16 | excess_return_240d 3.15% < 8.00%; volatility_120d 64.82% > 42.00% |
| 600719.SH | 大连热电 | ok | 59.11 | excess_return_240d -9.60% < 8.00%; drawdown_120d -33.56% < -28.00%; volatility_120d 60.05% > 42.00% |
| 000969.SZ | 安泰科技 | ok | 59.01 | ma60_not_above_ma120; excess_return_120d 4.74% < 6.00%; volatility_120d 52.69% > 42.00% |
| 000831.SZ | 中国稀土 | ok | 58.94 | close_below_ma200; excess_return_120d 5.61% < 6.00%; volatility_120d 57.74% > 42.00% |
| 600268.SH | 国电南自 | ok | 58.89 | close_below_ma200; drawdown_120d -33.47% < -28.00%; volatility_120d 54.28% > 42.00% |
| 002049.SZ | 紫光国微 | ok | 58.75 | ma120_not_above_ma200; excess_return_120d 5.58% < 6.00%; volatility_120d 45.02% > 42.00% |
| 000767.SZ | 晋控电力 | ok | 58.70 | excess_return_240d -9.88% < 8.00%; drawdown_120d -45.91% < -28.00%; volatility_120d 71.10% > 42.00% |
| 603255.SH | 鼎际得 | ok | 58.62 | ma120_not_above_ma200; excess_return_240d -9.22% < 8.00%; volatility_120d 44.12% > 42.00% |
| 300871.SZ | 回盛生物 | ok | 58.57 | ma60_not_above_ma120; excess_return_240d -3.79% < 8.00%; volatility_120d 60.25% > 42.00% |
| 300219.SZ | 鸿利智汇 | ok | 58.57 | excess_return_240d 3.90% < 8.00%; volatility_120d 49.17% > 42.00% |
| 600770.SH | 综艺股份 | ok | 58.53 | excess_return_240d -4.74% < 8.00%; drawdown_120d -28.70% < -28.00%; volatility_120d 57.21% > 42.00% |
| 300264.SZ | 佳创视讯 | ok | 58.52 | excess_return_240d 1.49% < 8.00%; drawdown_120d -30.12% < -28.00%; volatility_120d 84.70% > 42.00% |
| 300790.SZ | 宇瞳光学 | ok | 58.45 | ma120_not_above_ma200; excess_return_120d 3.98% < 6.00%; volatility_120d 58.24% > 42.00% |
| 603779.SH | 威龙股份 | ok | 58.41 | excess_return_240d -17.30% < 8.00%; drawdown_120d -45.94% < -28.00%; volatility_120d 62.36% > 42.00% |
| 600768.SH | 宁波富邦 | ok | 58.37 | volatility_120d 46.43% > 42.00% |
| 603118.SH | 共进股份 | ok | 58.28 | excess_return_240d -3.20% < 8.00%; volatility_120d 58.72% > 42.00% |
| 300717.SZ | 华信新材 | ok | 58.27 | ma60_not_above_ma120; excess_return_240d -3.16% < 8.00% |
| 301309.SZ | 万得凯 | ok | 58.21 | excess_return_240d 1.05% < 8.00%; volatility_120d 46.03% > 42.00% |
| 601016.SH | 节能风电 | ok | 58.01 | close_below_ma200; excess_return_240d 0.44% < 8.00%; drawdown_120d -38.85% < -28.00%; volatility_120d 65.08% > 42.00% |
| 600589.SH | 大位科技 | ok | 57.93 | close_below_ma200; excess_return_240d -13.63% < 8.00%; drawdown_120d -39.61% < -28.00%; volatility_120d 82.89% > 42.00% |
| 300686.SZ | 智动力 | ok | 57.87 | excess_return_120d 4.45% < 6.00%; volatility_120d 62.01% > 42.00% |
| 603488.SH | 展鹏科技 | ok | 57.85 | close_below_ma200; excess_return_240d -10.11% < 8.00%; drawdown_120d -28.78% < -28.00%; volatility_120d 61.66% > 42.00% |
| 300434.SZ | 金石亚药 | ok | 57.81 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_240d -1.42% < 8.00%; volatility_120d 48.62% > 42.00% |
| 688081.SH | 兴图新科 | ok | 57.69 | excess_return_120d 5.23% < 6.00%; drawdown_120d -38.08% < -28.00%; volatility_120d 59.61% > 42.00% |
| 603386.SH | 骏亚科技 | ok | 57.64 | excess_return_240d 7.36% < 8.00%; volatility_120d 50.44% > 42.00% |
| 300840.SZ | 酷特智能 | ok | 57.45 | excess_return_240d -9.45% < 8.00%; volatility_120d 59.08% > 42.00% |
| 300051.SZ | 琏升科技 | ok | 57.45 | close_below_ma200; excess_return_240d 1.44% < 8.00%; drawdown_120d -53.67% < -28.00%; volatility_120d 80.18% > 42.00% |
| 301577.SZ | 美信科技 | ok | 57.40 | excess_return_240d -15.29% < 8.00%; drawdown_120d -38.06% < -28.00%; volatility_120d 55.45% > 42.00% |
| 300453.SZ | 三鑫医疗 | ok | 57.23 | excess_return_240d 0.62% < 8.00% |
| 300017.SZ | 网宿科技 | ok | 57.21 | close_below_ma200; ma60_not_above_ma120; excess_return_240d 1.04% < 8.00%; drawdown_120d -46.79% < -28.00%; volatility_120d 82.21% > 42.00% |
| 600156.SH | 华升股份 | ok | 57.08 | drawdown_120d -41.32% < -28.00%; volatility_120d 71.26% > 42.00% |
| 301027.SZ | 华蓝集团 | ok | 56.79 | excess_return_240d -2.71% < 8.00%; volatility_120d 58.75% > 42.00% |
| 688411.SH | 海博思创 | ok | 56.78 | ma120_not_above_ma200; excess_return_120d 2.40% < 6.00%; volatility_120d 70.39% > 42.00% |
| 688517.SH | 金冠电气 | ok | 56.75 | close_below_ma200; excess_return_240d 2.01% < 8.00%; drawdown_120d -30.52% < -28.00%; volatility_120d 50.71% > 42.00% |
| 688583.SH | 思看科技 | ok | 56.66 | ma60_not_above_ma120; excess_return_240d -3.06% < 8.00%; drawdown_120d -35.41% < -28.00%; volatility_120d 75.54% > 42.00% |
| 600267.SH | 海正药业 | ok | 56.65 | ma120_not_above_ma200; excess_return_240d -19.71% < 8.00% |
| 300227.SZ | 光韵达 | ok | 56.57 | ma60_not_above_ma120; excess_return_240d -3.44% < 8.00%; volatility_120d 62.03% > 42.00% |
| 002579.SZ | 中京电子 | ok | 56.57 | excess_return_240d -5.77% < 8.00%; volatility_120d 70.56% > 42.00% |
| 603439.SH | 三力制药 | ok | 56.57 | excess_return_240d -7.69% < 8.00%; volatility_120d 43.80% > 42.00% |
| 002910.SZ | 庄园牧场 | ok | 56.49 | ma60_not_above_ma120; excess_return_120d 5.41% < 6.00%; excess_return_240d 6.46% < 8.00%; volatility_120d 51.43% > 42.00% |
| 688550.SH | 瑞联新材 | ok | 56.47 | ma120_not_above_ma200; excess_return_240d 5.72% < 8.00%; volatility_120d 58.53% > 42.00% |
| 688279.SH | 峰岹科技 | ok | 56.40 | ma120_not_above_ma200; excess_return_240d 3.47% < 8.00%; volatility_120d 54.91% > 42.00% |
| 300395.SZ | 菲利华 | ok | 56.32 | excess_return_120d 3.88% < 6.00%; drawdown_120d -29.16% < -28.00%; volatility_120d 77.50% > 42.00% |
| 603681.SH | 永冠新材 | ok | 56.32 | excess_return_120d 4.17% < 6.00%; drawdown_120d -28.16% < -28.00%; volatility_120d 49.39% > 42.00% |
| 000690.SZ | 宝新能源 | ok | 56.19 | excess_return_240d -20.45% < 8.00%; volatility_120d 45.50% > 42.00% |
| 003035.SZ | 南网能源 | ok | 56.13 | close_below_ma200; ma60_not_above_ma120; excess_return_240d -3.12% < 8.00%; drawdown_120d -48.27% < -28.00%; volatility_120d 62.97% > 42.00% |
| 301292.SZ | 海科新源 | ok | 56.04 | excess_return_120d 3.80% < 6.00%; drawdown_120d -34.67% < -28.00%; volatility_120d 84.13% > 42.00% |
| 600989.SH | 宝丰能源 | ok | 55.99 | close_below_ma200; excess_return_120d 5.41% < 6.00%; drawdown_120d -41.42% < -28.00%; volatility_120d 52.27% > 42.00% |
| 000692.SZ | 惠天热电 | ok | 55.82 | close_below_ma200; excess_return_240d -11.93% < 8.00%; volatility_120d 45.52% > 42.00% |
| 301107.SZ | 瑜欣电子 | ok | 55.75 | excess_return_240d -15.71% < 8.00%; volatility_120d 57.73% > 42.00% |
| 603225.SH | 新凤鸣 | ok | 55.70 | ma60_not_above_ma120; stock_return_120d 5.35% < 6.00%; excess_return_120d 0.77% < 6.00%; volatility_120d 60.06% > 42.00% |
| 603856.SH | 东宏股份 | ok | 55.58 | ma60_not_above_ma120; excess_return_240d -0.31% < 8.00% |
| 301067.SZ | 显盈科技 | ok | 55.57 | ma120_not_above_ma200; excess_return_240d -5.66% < 8.00%; volatility_120d 53.41% > 42.00% |
| 688098.SH | 申联生物 | ok | 55.55 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_120d 2.40% < 6.00%; volatility_120d 47.17% > 42.00% |
| 002763.SZ | 汇洁股份 | ok | 55.41 | excess_return_240d 2.51% < 8.00% |
| 688102.SH | 斯瑞新材 | ok | 55.19 | ma60_not_above_ma120; excess_return_120d 4.21% < 6.00%; volatility_120d 75.70% > 42.00% |
| 603026.SH | 石大胜华 | ok | 55.08 | excess_return_120d 3.60% < 6.00%; drawdown_120d -33.76% < -28.00%; volatility_120d 60.97% > 42.00% |
| 603505.SH | 金石资源 | ok | 55.07 | ma60_not_above_ma120; excess_return_120d 3.77% < 6.00%; volatility_120d 53.81% > 42.00% |
| 001378.SZ | 德冠新材 | ok | 54.89 | excess_return_240d -2.44% < 8.00% |
| 603958.SH | 哈森股份 | ok | 54.88 | close_below_ma200; excess_return_240d -29.72% < 8.00%; drawdown_120d -40.67% < -28.00%; volatility_120d 60.83% > 42.00% |
| 000935.SZ | 四川双马 | ok | 54.78 | excess_return_120d 2.51% < 6.00% |
| 688320.SH | 禾川科技 | ok | 54.69 | ma120_not_above_ma200; excess_return_240d -33.90% < 8.00%; volatility_120d 46.63% > 42.00% |
| 600150.SH | 中国船舶 | ok | 54.63 | excess_return_240d -8.82% < 8.00% |
| 300327.SZ | 中颖电子 | ok | 54.54 | ma60_not_above_ma120; excess_return_120d 5.41% < 6.00%; excess_return_240d 7.62% < 8.00%; volatility_120d 49.73% > 42.00% |
| 000519.SZ | 中兵红箭 | ok | 54.52 | excess_return_240d -21.61% < 8.00%; volatility_120d 44.18% > 42.00% |
| 300109.SZ | 新开源 | ok | 54.48 | excess_return_240d -7.05% < 8.00% |
| 688726.SH | 拉普拉斯 | ok | 54.17 | close_below_ma200; excess_return_240d -26.64% < 8.00%; drawdown_120d -46.90% < -28.00%; volatility_120d 81.91% > 42.00% |
| 000815.SZ | 美利云 | ok | 54.14 | close_below_ma200; excess_return_240d -16.85% < 8.00%; drawdown_120d -42.43% < -28.00%; volatility_120d 77.03% > 42.00% |
| 300980.SZ | 祥源新材 | ok | 54.11 | ma60_not_above_ma120; stock_return_120d 5.16% < 6.00%; excess_return_120d 0.58% < 6.00%; volatility_120d 61.24% > 42.00% |
| 002709.SZ | 天赐材料 | ok | 54.09 | excess_return_120d 1.98% < 6.00%; volatility_120d 55.50% > 42.00% |
| 600233.SH | 圆通速递 | ok | 54.06 | close_below_ma200; excess_return_120d 3.09% < 6.00% |
| 603328.SH | 依顿电子 | ok | 54.03 | excess_return_240d 0.76% < 8.00%; volatility_120d 54.97% > 42.00% |
| 000697.SZ | 炼石航空 | ok | 53.88 | excess_return_240d 7.46% < 8.00%; volatility_120d 44.65% > 42.00% |
| 301157.SZ | 华塑科技 | ok | 53.85 | excess_return_240d 4.64% < 8.00%; drawdown_120d -37.38% < -28.00%; volatility_120d 62.03% > 42.00% |
| 600642.SH | 申能股份 | ok | 53.83 | excess_return_240d -17.21% < 8.00% |
| 688484.SH | 南芯科技 | ok | 53.80 | ma120_not_above_ma200; excess_return_240d -2.87% < 8.00%; volatility_120d 64.60% > 42.00% |
| 002472.SZ | 双环传动 | ok | 53.76 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -0.81% < 6.00%; excess_return_120d -5.39% < 6.00%; volatility_120d 42.85% > 42.00% |
| 300490.SZ | 华自科技 | ok | 53.73 | close_below_ma200; excess_return_120d 5.01% < 6.00%; drawdown_120d -39.95% < -28.00%; volatility_120d 64.33% > 42.00% |
| 002956.SZ | 西麦食品 | ok | 53.63 | excess_return_120d 2.93% < 6.00%; volatility_120d 42.40% > 42.00% |
| 002112.SZ | 三变科技 | ok | 53.62 | close_below_ma200; ma60_not_above_ma120; excess_return_240d -8.13% < 8.00%; drawdown_120d -44.15% < -28.00%; volatility_120d 71.09% > 42.00% |
| 002342.SZ | 巨力索具 | ok | 53.49 | close_below_ma200; excess_return_120d 5.27% < 6.00%; drawdown_120d -57.91% < -28.00%; volatility_120d 90.08% > 42.00% |
| 603819.SH | 神力股份 | ok | 53.35 | excess_return_240d -21.24% < 8.00%; volatility_120d 46.94% > 42.00% |
| 002756.SZ | 永兴材料 | ok | 53.16 | excess_return_120d 3.08% < 6.00%; drawdown_120d -35.21% < -28.00%; volatility_120d 63.75% > 42.00% |
| 688226.SH | 威腾电气 | ok | 53.14 | close_below_ma200; excess_return_120d 4.67% < 6.00%; drawdown_120d -40.11% < -28.00%; volatility_120d 67.57% > 42.00% |
| 301219.SZ | 腾远钴业 | ok | 52.92 | excess_return_120d 2.30% < 6.00%; volatility_120d 57.47% > 42.00% |
| 301171.SZ | 易点天下 | ok | 52.90 | close_below_ma200; ma60_not_above_ma120; excess_return_120d 5.27% < 6.00%; drawdown_120d -54.55% < -28.00%; volatility_120d 96.45% > 42.00% |
| 601609.SH | 金田股份 | ok | 52.88 | excess_return_120d 2.13% < 6.00%; volatility_120d 53.09% > 42.00% |
| 301557.SZ | 常友科技 | ok | 52.86 | stock_return_120d -3.45% < 6.00%; excess_return_120d -8.03% < 6.00%; volatility_120d 51.31% > 42.00% |
| 600623.SH | 华谊集团 | ok | 52.69 | close_below_ma200; ma60_not_above_ma120; excess_return_240d -8.17% < 8.00%; volatility_120d 52.26% > 42.00% |
| 603271.SH | 永杰新材 | ok | 52.63 | excess_return_240d 2.20% < 8.00%; volatility_120d 50.27% > 42.00% |
| 301345.SZ | 涛涛车业 | ok | 52.47 | stock_return_120d 3.28% < 6.00%; excess_return_120d -1.30% < 6.00%; volatility_120d 52.36% > 42.00% |
| 003007.SZ | 直真科技 | ok | 52.45 | excess_return_120d 4.25% < 6.00%; drawdown_120d -32.12% < -28.00%; volatility_120d 69.04% > 42.00% |
| 002600.SZ | 领益智造 | ok | 52.43 | stock_return_120d 4.57% < 6.00%; excess_return_120d -0.01% < 6.00%; volatility_120d 54.94% > 42.00% |
| 688193.SH | 仁度生物 | ok | 52.20 | excess_return_120d 5.87% < 6.00%; excess_return_240d 5.45% < 8.00%; volatility_120d 42.64% > 42.00% |
| 603057.SH | 紫燕食品 | ok | 52.19 | close_below_ma200; ma60_not_above_ma120; excess_return_240d -10.10% < 8.00%; drawdown_120d -34.65% < -28.00%; volatility_120d 55.55% > 42.00% |
| 300058.SZ | 蓝色光标 | ok | 52.11 | close_below_ma200; ma60_not_above_ma120; excess_return_120d 3.85% < 6.00%; drawdown_120d -48.89% < -28.00%; volatility_120d 84.39% > 42.00% |
| 603006.SH | 联明股份 | ok | 51.83 | ma120_not_above_ma200; excess_return_120d 5.73% < 6.00%; excess_return_240d 1.79% < 8.00% |
| 301550.SZ | 斯菱智驱 | ok | 51.79 | ma60_not_above_ma120; excess_return_120d 1.90% < 6.00%; drawdown_120d -30.66% < -28.00%; volatility_120d 64.62% > 42.00% |
| 600483.SH | 福能股份 | ok | 51.75 | excess_return_240d -10.76% < 8.00% |
| 603356.SH | 华菱精工 | ok | 51.47 | close_below_ma200; excess_return_240d -3.32% < 8.00%; volatility_120d 56.47% > 42.00% |
| 688767.SH | 博拓生物 | ok | 51.29 | ma120_not_above_ma200; excess_return_240d -1.71% < 8.00%; volatility_120d 58.79% > 42.00% |
| 688386.SH | 泛亚微透 | ok | 51.07 | ma60_not_above_ma120; stock_return_120d 1.82% < 6.00%; excess_return_120d -2.76% < 6.00%; volatility_120d 55.51% > 42.00% |
| 301279.SZ | 金道科技 | ok | 50.92 | stock_return_120d -4.41% < 6.00%; excess_return_120d -8.99% < 6.00%; volatility_120d 53.67% > 42.00% |
| 300855.SZ | 图南股份 | ok | 50.81 | ma60_not_above_ma120; excess_return_120d 2.39% < 6.00%; drawdown_120d -30.74% < -28.00%; volatility_120d 59.37% > 42.00% |
| 300241.SZ | 瑞丰光电 | ok | 50.69 | excess_return_240d -10.30% < 8.00%; volatility_120d 56.64% > 42.00% |
| 688717.SH | 艾罗能源 | ok | 50.60 | close_below_ma200; ma60_not_above_ma120; excess_return_240d -8.39% < 8.00%; drawdown_120d -53.33% < -28.00%; volatility_120d 70.46% > 42.00% |
| 603181.SH | 皇马科技 | ok | 50.60 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_240d 0.22% < 8.00% |
| 002734.SZ | 利民股份 | ok | 50.55 | close_below_ma200; ma60_not_above_ma120; excess_return_240d -35.33% < 8.00%; volatility_120d 52.20% > 42.00% |
| 601156.SH | 东航物流 | ok | 50.50 | ma60_not_above_ma120; stock_return_120d -2.50% < 6.00%; excess_return_120d -7.08% < 6.00% |
| 002493.SZ | 荣盛石化 | ok | 50.49 | ma60_not_above_ma120; stock_return_120d 5.65% < 6.00%; excess_return_120d 1.07% < 6.00%; volatility_120d 50.54% > 42.00% |
| 688011.SH | 新光光电 | ok | 50.33 | ma60_not_above_ma120; stock_return_120d 2.37% < 6.00%; excess_return_120d -2.21% < 6.00%; volatility_120d 61.74% > 42.00% |
| 603690.SH | 至纯科技 | ok | 50.32 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 5.50% < 6.00%; excess_return_120d 0.92% < 6.00%; volatility_120d 48.16% > 42.00% |
| 002466.SZ | 天齐锂业 | ok | 50.15 | excess_return_120d 1.79% < 6.00%; drawdown_120d -28.59% < -28.00%; volatility_120d 50.34% > 42.00% |
| 600821.SH | 金开新能 | ok | 50.13 | close_below_ma200; excess_return_240d -10.07% < 8.00%; drawdown_120d -51.48% < -28.00%; volatility_120d 70.38% > 42.00% |
| 000977.SZ | 浪潮信息 | ok | 50.09 | stock_return_120d 4.73% < 6.00%; excess_return_120d 0.15% < 6.00%; volatility_120d 49.76% > 42.00% |
| 688779.SH | 五矿新能 | ok | 50.06 | close_below_ma200; ma60_not_above_ma120; excess_return_120d 3.35% < 6.00%; drawdown_120d -36.89% < -28.00%; volatility_120d 45.73% > 42.00% |
| 301314.SZ | 科瑞思 | ok | 49.96 | excess_return_240d -4.59% < 8.00%; volatility_120d 47.19% > 42.00% |
| 688230.SH | 芯导科技 | ok | 49.89 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 1.85% < 6.00%; excess_return_120d -2.73% < 6.00%; volatility_120d 46.94% > 42.00% |
| 002531.SZ | 天顺风能 | ok | 49.88 | close_below_ma200; excess_return_240d -9.28% < 8.00%; drawdown_120d -40.67% < -28.00%; volatility_120d 46.76% > 42.00% |
| 600058.SH | 五矿发展 | ok | 49.82 | close_below_ma200; ma60_not_above_ma120; excess_return_120d 4.56% < 6.00%; drawdown_120d -37.51% < -28.00%; volatility_120d 58.42% > 42.00% |
| 600179.SH | 安通控股 | ok | 49.74 | ma60_not_above_ma120; stock_return_120d -15.76% < 6.00%; excess_return_120d -20.34% < 6.00% |
| 002303.SZ | 美盈森 | ok | 49.73 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_120d 4.03% < 6.00%; excess_return_240d 1.68% < 8.00% |
| 688618.SH | 三旺通信 | ok | 49.62 | close_below_ma200; excess_return_240d 1.95% < 8.00%; drawdown_120d -37.57% < -28.00%; volatility_120d 69.71% > 42.00% |
| 301172.SZ | 君逸数码 | ok | 49.43 | close_below_ma200; excess_return_240d -0.67% < 8.00%; drawdown_120d -39.50% < -28.00%; volatility_120d 59.00% > 42.00% |
| 301085.SZ | 亚康股份 | ok | 49.28 | close_below_ma200; excess_return_240d -18.23% < 8.00%; drawdown_120d -32.35% < -28.00%; volatility_120d 72.69% > 42.00% |
| 001872.SZ | 招商港口 | ok | 49.04 | excess_return_120d 5.56% < 6.00%; excess_return_240d -15.96% < 8.00% |
| 002301.SZ | 齐心集团 | ok | 48.94 | ma60_not_above_ma120; excess_return_120d 4.84% < 6.00%; excess_return_240d -0.48% < 8.00%; volatility_120d 43.76% > 42.00% |
| 002935.SZ | 天奥电子 | ok | 48.88 | ma60_not_above_ma120; stock_return_120d 0.90% < 6.00%; excess_return_120d -3.68% < 6.00%; volatility_120d 49.33% > 42.00% |
| 001324.SZ | 长青科技 | ok | 48.87 | excess_return_240d -21.74% < 8.00% |
| 002563.SZ | 森马服饰 | ok | 48.82 | ma120_not_above_ma200; excess_return_120d 3.96% < 6.00%; excess_return_240d -5.77% < 8.00% |
| 000630.SZ | 铜陵有色 | ok | 48.81 | ma60_not_above_ma120; stock_return_120d 5.70% < 6.00%; excess_return_120d 1.12% < 6.00%; drawdown_120d -31.07% < -28.00%; volatility_120d 64.81% > 42.00% |
| 002064.SZ | 华峰化学 | ok | 48.70 | ma60_not_above_ma120; stock_return_120d 2.02% < 6.00%; excess_return_120d -2.56% < 6.00%; volatility_120d 52.67% > 42.00% |
| 300031.SZ | 宝通科技 | ok | 48.69 | excess_return_240d -13.90% < 8.00%; volatility_120d 44.40% > 42.00% |
| 002896.SZ | 中大力德 | ok | 48.66 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.98% < 6.00%; excess_return_120d -10.56% < 6.00%; volatility_120d 54.58% > 42.00% |
| 600847.SH | 万里股份 | ok | 48.63 | excess_return_240d -4.21% < 8.00%; volatility_120d 51.48% > 42.00% |
| 605167.SH | 利柏特 | ok | 48.51 | ma60_not_above_ma120; stock_return_120d -1.22% < 6.00%; excess_return_120d -5.80% < 6.00%; volatility_120d 60.94% > 42.00% |
| 000533.SZ | 顺钠股份 | ok | 48.43 | close_below_ma200; ma60_not_above_ma120; drawdown_120d -57.78% < -28.00%; volatility_120d 75.11% > 42.00% |
| 002541.SZ | 鸿路钢构 | ok | 48.42 | close_below_ma200; ma60_not_above_ma120; excess_return_240d -19.58% < 8.00%; volatility_120d 52.60% > 42.00% |
| 301269.SZ | 华大九天 | ok | 48.35 | ma120_not_above_ma200; excess_return_120d 5.81% < 6.00%; excess_return_240d -19.13% < 8.00%; volatility_120d 61.31% > 42.00% |
| 601778.SH | 晶科科技 | ok | 48.24 | close_below_ma200; excess_return_120d 4.85% < 6.00%; drawdown_120d -48.55% < -28.00%; volatility_120d 63.76% > 42.00% |
| 301631.SZ | 壹连科技 | ok | 48.18 | stock_return_120d 5.82% < 6.00%; excess_return_120d 1.24% < 6.00%; volatility_120d 48.15% > 42.00% |
| 300750.SZ | 宁德时代 | ok | 48.17 | close_below_ma200; stock_return_120d 3.93% < 6.00%; excess_return_120d -0.65% < 6.00% |
| 301376.SZ | 致欧科技 | ok | 48.16 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_120d 4.54% < 6.00%; excess_return_240d -14.02% < 8.00%; volatility_120d 42.53% > 42.00% |
| 600671.SH | 天目药业 | ok | 48.13 | close_below_ma200; ma60_not_above_ma120; excess_return_120d 2.24% < 6.00%; volatility_120d 47.61% > 42.00% |
| 688343.SH | 云天励飞 | ok | 47.98 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 5.78% < 6.00%; excess_return_120d 1.20% < 6.00%; volatility_120d 74.40% > 42.00% |
| 300881.SZ | 盛德鑫泰 | ok | 47.92 | close_below_ma200; excess_return_240d -14.10% < 8.00%; drawdown_120d -32.70% < -28.00%; volatility_120d 56.38% > 42.00% |
| 603701.SH | 德宏股份 | ok | 47.92 | excess_return_120d 5.11% < 6.00%; excess_return_240d 3.59% < 8.00% |
| 688338.SH | 赛科希德 | ok | 47.82 | ma60_not_above_ma120; excess_return_240d -6.59% < 8.00%; volatility_120d 52.86% > 42.00% |
| 601198.SH | 东兴证券 | ok | 47.78 | ma60_not_above_ma120; stock_return_120d 0.50% < 6.00%; excess_return_120d -4.08% < 6.00%; excess_return_240d 7.92% < 8.00% |
| 688165.SH | 埃夫特 | ok | 47.73 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_240d -40.28% < 8.00%; volatility_120d 58.04% > 42.00% |
| 603660.SH | 苏州科达 | ok | 47.61 | stock_return_120d 1.45% < 6.00%; excess_return_120d -3.13% < 6.00%; volatility_120d 50.70% > 42.00% |
| 301201.SZ | 诚达药业 | ok | 47.54 | ma60_not_above_ma120; stock_return_120d 4.79% < 6.00%; excess_return_120d 0.21% < 6.00%; drawdown_120d -34.41% < -28.00%; volatility_120d 64.60% > 42.00% |
| 001301.SZ | 尚太科技 | ok | 47.51 | ma120_not_above_ma200; stock_return_120d -2.99% < 6.00%; excess_return_120d -7.57% < 6.00%; volatility_120d 50.94% > 42.00% |
| 000629.SZ | 钒钛股份 | ok | 47.46 | ma60_not_above_ma120; excess_return_120d 4.45% < 6.00%; excess_return_240d 7.91% < 8.00%; volatility_120d 51.97% > 42.00% |
| 688180.SH | 君实生物 | ok | 47.40 | ma120_not_above_ma200; excess_return_240d -20.49% < 8.00%; volatility_120d 51.58% > 42.00% |
| 603933.SH | 睿能科技 | ok | 47.35 | stock_return_120d -4.39% < 6.00%; excess_return_120d -10.11% < 6.00%; volatility_120d 49.46% > 42.00% |
| 600177.SH | 雅戈尔 | ok | 47.33 | excess_return_120d 1.95% < 6.00%; excess_return_240d -8.10% < 8.00% |
| 300801.SZ | 泰和科技 | ok | 47.24 | ma60_not_above_ma120; excess_return_120d 4.75% < 6.00%; excess_return_240d 3.79% < 8.00%; volatility_120d 58.55% > 42.00% |
| 688353.SH | 华盛锂电 | ok | 47.17 | ma60_not_above_ma120; stock_return_120d -4.38% < 6.00%; excess_return_120d -8.96% < 6.00%; volatility_120d 67.73% > 42.00% |
| 002386.SZ | 天原股份 | ok | 47.10 | excess_return_240d -3.16% < 8.00%; volatility_120d 42.82% > 42.00% |
| 300727.SZ | 润禾材料 | ok | 47.06 | ma120_not_above_ma200; stock_return_120d 2.24% < 6.00%; excess_return_120d -2.34% < 6.00%; volatility_120d 52.60% > 42.00% |
| 300759.SZ | 康龙化成 | ok | 47.02 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_120d 3.76% < 6.00%; excess_return_240d 2.80% < 8.00% |
| 301042.SZ | 安联锐视 | ok | 46.99 | stock_return_120d 1.22% < 6.00%; excess_return_120d -3.36% < 6.00% |
| 688768.SH | 容知日新 | ok | 46.90 | ma60_not_above_ma120; excess_return_240d -4.83% < 8.00%; drawdown_120d -29.94% < -28.00%; volatility_120d 60.53% > 42.00% |
| 688261.SH | 东微半导 | ok | 46.89 | ma60_not_above_ma120; stock_return_120d 3.85% < 6.00%; excess_return_120d -0.73% < 6.00%; volatility_120d 78.69% > 42.00% |
| 688148.SH | 芳源股份 | ok | 46.86 | stock_return_120d 2.62% < 6.00%; excess_return_120d -1.96% < 6.00%; volatility_120d 53.84% > 42.00% |
| 002837.SZ | 英维克 | ok | 46.84 | ma60_not_above_ma120; stock_return_120d -9.78% < 6.00%; excess_return_120d -14.36% < 6.00%; volatility_120d 66.58% > 42.00% |
| 300222.SZ | 科大智能 | ok | 46.75 | close_below_ma200; excess_return_240d 0.16% < 8.00%; drawdown_120d -30.24% < -28.00%; volatility_120d 58.41% > 42.00% |
| 600982.SH | 宁波能源 | ok | 46.73 | close_below_ma200; excess_return_240d -17.83% < 8.00%; drawdown_120d -36.80% < -28.00%; volatility_120d 62.31% > 42.00% |
| 600784.SH | 鲁银投资 | ok | 46.72 | excess_return_120d 5.09% < 6.00%; excess_return_240d -1.22% < 8.00%; volatility_120d 43.62% > 42.00% |
| 000990.SZ | 诚志股份 | ok | 46.66 | excess_return_240d -4.99% < 8.00%; drawdown_120d -33.38% < -28.00%; volatility_120d 55.03% > 42.00% |
| 603296.SH | 华勤技术 | ok | 46.65 | excess_return_240d -4.25% < 8.00%; volatility_120d 53.34% > 42.00% |
| 301075.SZ | 多瑞医药 | ok | 46.53 | close_below_ma200; stock_return_120d 5.62% < 6.00%; excess_return_120d 1.25% < 6.00%; drawdown_120d -39.20% < -28.00%; volatility_120d 60.07% > 42.00% |
| 603610.SH | 麒盛科技 | ok | 46.52 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.19% < 6.00%; excess_return_120d -10.77% < 6.00%; volatility_120d 45.72% > 42.00% |
| 301246.SZ | 宏源药业 | ok | 46.51 | stock_return_120d 3.33% < 6.00%; excess_return_120d -1.25% < 6.00%; volatility_120d 57.93% > 42.00% |
| 003033.SZ | 征和工业 | ok | 46.50 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.99% < 6.00%; excess_return_120d -22.57% < 6.00%; volatility_120d 52.04% > 42.00% |
| 600288.SH | 大恒科技 | ok | 46.38 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.61% < 6.00%; excess_return_120d -10.19% < 6.00% |
| 002611.SZ | 东方精工 | ok | 46.29 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.75% < 6.00%; excess_return_120d -13.33% < 6.00% |
| 300562.SZ | 乐心医疗 | ok | 46.29 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_120d 5.80% < 6.00%; excess_return_240d -26.68% < 8.00% |
| 301468.SZ | 博盈特焊 | ok | 46.26 | ma60_not_above_ma120; stock_return_120d 3.61% < 6.00%; excess_return_120d -0.97% < 6.00%; drawdown_120d -32.97% < -28.00%; volatility_120d 83.20% > 42.00% |
| 603616.SH | 韩建河山 | ok | 46.25 | close_below_ma200; ma60_not_above_ma120; excess_return_240d 2.13% < 8.00%; drawdown_120d -38.01% < -28.00%; volatility_120d 71.10% > 42.00% |
| 600879.SH | 航天电子 | ok | 46.24 | ma60_not_above_ma120; stock_return_120d 0.89% < 6.00%; excess_return_120d -3.69% < 6.00%; drawdown_120d -33.28% < -28.00%; volatility_120d 66.69% > 42.00% |
| 002986.SZ | 宇新股份 | ok | 46.19 | close_below_ma200; ma60_not_above_ma120; excess_return_240d -12.44% < 8.00%; drawdown_120d -33.21% < -28.00%; volatility_120d 49.22% > 42.00% |
| 002326.SZ | 永太科技 | ok | 46.13 | ma60_not_above_ma120; stock_return_120d -3.88% < 6.00%; excess_return_120d -8.36% < 6.00%; volatility_120d 61.53% > 42.00% |
| 002617.SZ | 露笑科技 | ok | 46.11 | ma120_not_above_ma200; excess_return_240d -6.39% < 8.00%; volatility_120d 52.25% > 42.00% |
| 601168.SH | 西部矿业 | ok | 46.03 | ma60_not_above_ma120; stock_return_120d 4.03% < 6.00%; excess_return_120d -0.55% < 6.00%; drawdown_120d -30.43% < -28.00%; volatility_120d 57.96% > 42.00% |
| 002534.SZ | 西子洁能 | ok | 46.01 | close_below_ma200; stock_return_120d 3.84% < 6.00%; excess_return_120d -0.74% < 6.00%; volatility_120d 55.56% > 42.00% |
| 002346.SZ | 柘中股份 | ok | 45.93 | ma60_not_above_ma120; stock_return_120d -3.69% < 6.00%; excess_return_120d -8.27% < 6.00%; volatility_120d 49.87% > 42.00% |
| 002171.SZ | 楚江新材 | ok | 45.88 | ma60_not_above_ma120; stock_return_120d -3.41% < 6.00%; excess_return_120d -7.99% < 6.00%; volatility_120d 52.04% > 42.00% |
| 000417.SZ | 合百集团 | ok | 45.85 | ma60_not_above_ma120; stock_return_120d -0.86% < 6.00%; excess_return_120d -5.44% < 6.00%; volatility_120d 57.05% > 42.00% |
| 301133.SZ | 金钟股份 | ok | 45.79 | stock_return_120d 0.63% < 6.00%; excess_return_120d -3.95% < 6.00%; volatility_120d 54.70% > 42.00% |
| 002668.SZ | TCL智家 | ok | 45.73 | ma120_not_above_ma200; excess_return_120d 2.24% < 6.00%; excess_return_240d -6.63% < 8.00% |
| 300033.SZ | 同花顺 | ok | 45.72 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_120d 3.60% < 6.00%; excess_return_240d 6.04% < 8.00%; volatility_120d 53.66% > 42.00% |
| 688160.SH | 步科股份 | ok | 45.71 | ma60_not_above_ma120; stock_return_120d -14.90% < 6.00%; excess_return_120d -19.48% < 6.00%; volatility_120d 64.48% > 42.00% |
| 601995.SH | 中金公司 | ok | 45.68 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_120d 1.82% < 6.00%; excess_return_240d -14.73% < 8.00% |
| 301257.SZ | 普蕊斯 | ok | 45.63 | ma60_not_above_ma120; stock_return_120d 4.23% < 6.00%; excess_return_120d -0.35% < 6.00%; drawdown_120d -36.19% < -28.00%; volatility_120d 63.68% > 42.00% |
| 600203.SH | 福日电子 | ok | 45.59 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -5.17% < 6.00%; excess_return_120d -9.75% < 6.00%; volatility_120d 43.36% > 42.00% |
| 688333.SH | 铂力特 | ok | 45.55 | ma60_not_above_ma120; stock_return_120d -10.21% < 6.00%; excess_return_120d -14.79% < 6.00%; drawdown_120d -28.63% < -28.00%; volatility_120d 81.87% > 42.00% |
| 601138.SH | 工业富联 | ok | 45.49 | ma120_not_above_ma200; stock_return_120d 3.03% < 6.00%; excess_return_120d -1.55% < 6.00%; volatility_120d 53.03% > 42.00% |
| 002446.SZ | 盛路通信 | ok | 45.49 | ma60_not_above_ma120; stock_return_120d 1.62% < 6.00%; excess_return_120d -2.96% < 6.00%; volatility_120d 65.75% > 42.00% |
| 002134.SZ | 天津普林 | ok | 45.28 | excess_return_120d 1.84% < 6.00%; excess_return_240d 7.21% < 8.00%; volatility_120d 50.05% > 42.00% |
| 000408.SZ | 藏格矿业 | ok | 45.27 | ma60_not_above_ma120; stock_return_120d -9.87% < 6.00%; excess_return_120d -14.45% < 6.00%; volatility_120d 46.17% > 42.00% |
| 601665.SH | 齐鲁银行 | ok | 45.19 | excess_return_120d 2.73% < 6.00%; excess_return_240d -25.82% < 8.00% |
| 301288.SZ | 清研环境 | ok | 45.17 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -1.63% < 6.00%; excess_return_120d -5.73% < 6.00%; volatility_120d 52.09% > 42.00% |
| 601066.SH | 中信建投 | ok | 45.15 | ma120_not_above_ma200; excess_return_120d 3.14% < 6.00%; excess_return_240d -0.93% < 8.00% |
| 603667.SH | 五洲新春 | ok | 45.11 | ma60_not_above_ma120; stock_return_120d -1.89% < 6.00%; excess_return_120d -6.47% < 6.00%; drawdown_120d -29.03% < -28.00%; volatility_120d 64.77% > 42.00% |
| 002149.SZ | 西部材料 | ok | 45.10 | stock_return_120d -2.20% < 6.00%; excess_return_120d -6.78% < 6.00%; drawdown_120d -43.57% < -28.00%; volatility_120d 80.79% > 42.00% |
| 301596.SZ | 瑞迪智驱 | ok | 45.07 | ma120_not_above_ma200; excess_return_120d 3.61% < 6.00%; excess_return_240d -17.06% < 8.00%; volatility_120d 58.21% > 42.00% |
| 688099.SH | 晶晨股份 | ok | 45.06 | excess_return_120d 2.73% < 6.00%; volatility_120d 54.71% > 42.00% |
| 600470.SH | 六国化工 | ok | 45.05 | ma60_not_above_ma120; excess_return_240d -13.19% < 8.00%; drawdown_120d -29.13% < -28.00%; volatility_120d 67.60% > 42.00% |
| 300900.SZ | 广联航空 | ok | 44.98 | stock_return_120d 3.48% < 6.00%; excess_return_120d -1.10% < 6.00%; volatility_120d 85.05% > 42.00% |
| 600118.SH | 中国卫星 | ok | 44.93 | ma60_not_above_ma120; stock_return_120d -12.43% < 6.00%; excess_return_120d -17.01% < 6.00%; drawdown_120d -34.92% < -28.00%; volatility_120d 65.46% > 42.00% |
| 603978.SH | 深圳新星 | ok | 44.84 | stock_return_120d -3.90% < 6.00%; excess_return_120d -8.48% < 6.00%; volatility_120d 56.58% > 42.00% |
| 300762.SZ | 上海瀚讯 | ok | 44.83 | ma60_not_above_ma120; stock_return_120d -1.10% < 6.00%; excess_return_120d -5.68% < 6.00%; drawdown_120d -32.17% < -28.00%; volatility_120d 70.32% > 42.00% |
| 605319.SH | 无锡振华 | ok | 44.75 | close_below_ma200; excess_return_240d -20.33% < 8.00% |
| 002577.SZ | 雷柏科技 | ok | 44.69 | ma120_not_above_ma200; excess_return_120d 2.78% < 6.00%; excess_return_240d -26.96% < 8.00% |
| 603699.SH | 纽威股份 | ok | 44.65 | stock_return_120d 0.33% < 6.00%; excess_return_120d -4.25% < 6.00%; volatility_120d 52.18% > 42.00% |
| 688788.SH | 科思科技 | ok | 44.63 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.83% < 6.00%; excess_return_120d -13.41% < 6.00%; volatility_120d 67.64% > 42.00% |
| 600329.SH | 达仁堂 | ok | 44.55 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.13% < 6.00%; excess_return_120d -11.71% < 6.00% |
| 002845.SZ | 同兴达 | ok | 44.48 | excess_return_120d 4.33% < 6.00%; excess_return_240d -22.39% < 8.00%; volatility_120d 48.55% > 42.00% |
| 600166.SH | 福田汽车 | ok | 44.41 | excess_return_120d 5.01% < 6.00%; excess_return_240d -7.22% < 8.00% |
| 688523.SH | 航天环宇 | ok | 44.40 | ma60_not_above_ma120; stock_return_120d -4.27% < 6.00%; excess_return_120d -8.85% < 6.00%; drawdown_120d -43.43% < -28.00%; volatility_120d 90.46% > 42.00% |
| 688683.SH | 莱尔科技 | ok | 44.32 | close_below_ma200; stock_return_120d 5.88% < 6.00%; excess_return_120d 1.30% < 6.00%; drawdown_120d -34.25% < -28.00%; volatility_120d 48.89% > 42.00% |
| 300880.SZ | 迦南智能 | ok | 44.26 | close_below_ma200; excess_return_240d -28.28% < 8.00%; drawdown_120d -31.67% < -28.00%; volatility_120d 60.48% > 42.00% |
| 300197.SZ | 节能铁汉 | ok | 44.18 | ma120_not_above_ma200; excess_return_240d -28.14% < 8.00%; drawdown_120d -38.51% < -28.00%; volatility_120d 73.08% > 42.00% |
| 300756.SZ | 金马游乐 | ok | 44.16 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -17.32% < 6.00%; excess_return_120d -21.90% < 6.00%; volatility_120d 47.92% > 42.00% |
| 600936.SH | 北投科技 | ok | 44.15 | excess_return_120d 4.42% < 6.00%; excess_return_240d 3.90% < 8.00%; drawdown_120d -30.93% < -28.00%; volatility_120d 56.91% > 42.00% |
| 002989.SZ | 中天精装 | ok | 44.12 | excess_return_120d 4.11% < 6.00%; excess_return_240d -19.52% < 8.00%; volatility_120d 65.28% > 42.00% |
| 003009.SZ | 中天火箭 | ok | 44.07 | ma60_not_above_ma120; stock_return_120d -18.04% < 6.00%; excess_return_120d -22.62% < 6.00%; drawdown_120d -36.01% < -28.00%; volatility_120d 62.83% > 42.00% |
| 301421.SZ | 波长光电 | ok | 44.04 | ma120_not_above_ma200; stock_return_120d -2.74% < 6.00%; excess_return_120d -7.32% < 6.00%; volatility_120d 71.94% > 42.00% |
| 002361.SZ | 神剑股份 | ok | 43.96 | stock_return_120d -10.81% < 6.00%; excess_return_120d -15.39% < 6.00%; drawdown_120d -46.60% < -28.00%; volatility_120d 88.07% > 42.00% |
| 000032.SZ | 深桑达A | ok | 43.88 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_120d 5.54% < 6.00%; excess_return_240d -14.94% < 8.00%; volatility_120d 58.52% > 42.00% |
| 601886.SH | 江河集团 | ok | 43.81 | close_below_ma200; stock_return_120d 3.46% < 6.00%; excess_return_120d -1.12% < 6.00% |
| 688513.SH | 苑东生物 | ok | 43.75 | ma60_not_above_ma120; stock_return_120d -3.86% < 6.00%; excess_return_120d -8.44% < 6.00%; volatility_120d 61.71% > 42.00% |
| 002050.SZ | 三花智控 | ok | 43.66 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.38% < 6.00%; excess_return_120d -20.96% < 6.00%; volatility_120d 43.06% > 42.00% |
| 301043.SZ | 绿岛风 | ok | 43.64 | ma60_not_above_ma120; stock_return_120d -16.62% < 6.00%; excess_return_120d -21.20% < 6.00%; drawdown_120d -34.37% < -28.00%; volatility_120d 61.86% > 42.00% |
| 000792.SZ | 盐湖股份 | ok | 43.60 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 3.87% < 6.00%; excess_return_120d -0.71% < 6.00%; drawdown_120d -29.69% < -28.00%; volatility_120d 46.82% > 42.00% |
| 301162.SZ | 国能日新 | ok | 43.59 | close_below_ma200; ma60_not_above_ma120; excess_return_240d -15.72% < 8.00%; drawdown_120d -32.23% < -28.00%; volatility_120d 61.63% > 42.00% |
| 600111.SH | 北方稀土 | ok | 43.53 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 2.87% < 6.00%; excess_return_120d -1.71% < 6.00%; volatility_120d 55.34% > 42.00% |
| 002571.SZ | 德力股份 | ok | 43.52 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.90% < 6.00%; excess_return_120d -16.48% < 6.00%; volatility_120d 45.14% > 42.00% |
| 600189.SH | 泉阳泉 | ok | 43.52 | close_below_ma200; excess_return_120d 5.12% < 6.00%; excess_return_240d -18.80% < 8.00% |
| 688676.SH | 金盘科技 | ok | 43.49 | ma60_not_above_ma120; stock_return_120d -7.72% < 6.00%; excess_return_120d -12.30% < 6.00%; volatility_120d 68.15% > 42.00% |
| 002083.SZ | 孚日股份 | ok | 43.48 | ma60_not_above_ma120; stock_return_120d -14.06% < 6.00%; excess_return_120d -18.64% < 6.00%; drawdown_120d -31.00% < -28.00%; volatility_120d 58.00% > 42.00% |
| 300710.SZ | 万隆光电 | ok | 43.48 | stock_return_120d -4.33% < 6.00%; excess_return_120d -8.91% < 6.00%; drawdown_120d -37.92% < -28.00%; volatility_120d 63.95% > 42.00% |
| 300476.SZ | 胜宏科技 | ok | 43.47 | close_below_ma200; stock_return_120d 2.52% < 6.00%; excess_return_120d -2.06% < 6.00%; volatility_120d 63.32% > 42.00% |
| 301005.SZ | 超捷股份 | ok | 43.46 | ma60_not_above_ma120; stock_return_120d -3.48% < 6.00%; excess_return_120d -8.06% < 6.00%; drawdown_120d -34.42% < -28.00%; volatility_120d 84.12% > 42.00% |
| 603601.SH | 再升科技 | ok | 43.45 | stock_return_120d -11.16% < 6.00%; excess_return_120d -15.74% < 6.00%; drawdown_120d -52.93% < -28.00%; volatility_120d 90.77% > 42.00% |
| 300895.SZ | 铜牛信息 | ok | 43.44 | close_below_ma200; excess_return_240d -10.50% < 8.00%; drawdown_120d -40.32% < -28.00%; volatility_120d 81.24% > 42.00% |
| 300277.SZ | 汽轮科技 | ok | 43.38 | close_below_ma200; ma60_not_above_ma120; excess_return_240d -7.55% < 8.00%; drawdown_120d -44.21% < -28.00%; volatility_120d 77.10% > 42.00% |
| 603179.SH | 新泉股份 | ok | 43.35 | ma60_not_above_ma120; stock_return_120d 0.69% < 6.00%; excess_return_120d -3.89% < 6.00%; drawdown_120d -31.47% < -28.00%; volatility_120d 60.32% > 42.00% |
| 600783.SH | 鲁信创投 | ok | 43.24 | ma60_not_above_ma120; stock_return_120d -18.71% < 6.00%; excess_return_120d -23.29% < 6.00%; drawdown_120d -49.08% < -28.00%; volatility_120d 74.65% > 42.00% |
| 688553.SH | 汇宇制药 | ok | 43.22 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_240d -19.78% < 8.00%; volatility_120d 62.77% > 42.00% |
| 300885.SZ | 海昌新材 | ok | 43.07 | stock_return_120d -24.18% < 6.00%; excess_return_120d -28.76% < 6.00%; drawdown_120d -29.61% < -28.00%; volatility_120d 63.51% > 42.00% |
| 301448.SZ | 开创电气 | ok | 43.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.48% < 6.00%; excess_return_120d -17.06% < 6.00%; volatility_120d 49.06% > 42.00% |
| 688239.SH | 航宇科技 | ok | 42.92 | ma60_not_above_ma120; stock_return_120d -12.91% < 6.00%; excess_return_120d -17.49% < 6.00%; volatility_120d 65.21% > 42.00% |
| 301302.SZ | 华如科技 | ok | 42.90 | ma60_not_above_ma120; excess_return_240d -11.40% < 8.00%; drawdown_120d -35.23% < -28.00%; volatility_120d 76.42% > 42.00% |
| 605566.SH | 福莱蒽特 | ok | 42.90 | close_below_ma200; stock_return_120d 0.67% < 6.00%; excess_return_120d -3.91% < 6.00%; drawdown_120d -40.11% < -28.00%; volatility_120d 60.27% > 42.00% |
| 301002.SZ | 崧盛股份 | ok | 42.88 | close_below_ma200; stock_return_120d 3.19% < 6.00%; excess_return_120d -1.39% < 6.00%; drawdown_120d -42.29% < -28.00%; volatility_120d 65.40% > 42.00% |
| 600872.SH | 中炬高新 | ok | 42.75 | excess_return_120d 3.45% < 6.00%; excess_return_240d -19.49% < 8.00% |
| 001203.SZ | 大中矿业 | ok | 42.66 | stock_return_120d 0.16% < 6.00%; excess_return_120d -4.42% < 6.00%; drawdown_120d -43.99% < -28.00%; volatility_120d 69.81% > 42.00% |
| 002497.SZ | 雅化集团 | ok | 42.63 | stock_return_120d -9.24% < 6.00%; excess_return_120d -13.82% < 6.00%; drawdown_120d -29.84% < -28.00%; volatility_120d 55.81% > 42.00% |
| 600023.SH | 浙能电力 | ok | 42.59 | excess_return_120d 4.71% < 6.00%; excess_return_240d -19.02% < 8.00% |
| 002518.SZ | 科士达 | ok | 42.51 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -1.29% < 6.00%; excess_return_120d -5.87% < 6.00%; volatility_120d 56.83% > 42.00% |
| 603993.SH | 洛阳钼业 | ok | 42.48 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.12% < 6.00%; excess_return_120d -11.70% < 6.00%; drawdown_120d -35.74% < -28.00%; volatility_120d 62.92% > 42.00% |
| 688273.SH | 麦澜德 | ok | 42.46 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -1.62% < 6.00%; excess_return_120d -6.20% < 6.00%; drawdown_120d -31.91% < -28.00%; volatility_120d 62.42% > 42.00% |
| 300593.SZ | 新雷能 | ok | 42.46 | close_below_ma200; stock_return_120d -8.53% < 6.00%; excess_return_120d -13.12% < 6.00%; drawdown_120d -35.85% < -28.00%; volatility_120d 75.51% > 42.00% |
| 601698.SH | 中国卫通 | ok | 42.45 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.02% < 6.00%; excess_return_120d -20.60% < 6.00%; drawdown_120d -44.33% < -28.00%; volatility_120d 63.32% > 42.00% |
| 002922.SZ | 伊戈尔 | ok | 42.32 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 3.82% < 6.00%; excess_return_120d -0.76% < 6.00%; drawdown_120d -35.99% < -28.00%; volatility_120d 66.51% > 42.00% |
| 603228.SH | 景旺电子 | ok | 42.31 | stock_return_120d -6.56% < 6.00%; excess_return_120d -11.14% < 6.00%; volatility_120d 60.32% > 42.00% |
| 000973.SZ | 佛塑科技 | ok | 42.29 | close_below_ma200; stock_return_120d -9.79% < 6.00%; excess_return_120d -14.37% < 6.00%; drawdown_120d -40.42% < -28.00%; volatility_120d 62.06% > 42.00% |
| 603319.SH | 美湖股份 | ok | 42.20 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.50% < 6.00%; excess_return_120d -11.08% < 6.00%; volatility_120d 57.14% > 42.00% |
| 002470.SZ | 金正大 | ok | 42.18 | close_below_ma200; excess_return_240d -9.37% < 8.00%; drawdown_120d -47.64% < -28.00%; volatility_120d 66.34% > 42.00% |
| 688385.SH | 复旦微电 | ok | 42.14 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.16% < 6.00%; excess_return_120d -13.74% < 6.00%; drawdown_120d -33.04% < -28.00%; volatility_120d 58.41% > 42.00% |
| 300955.SZ | 嘉亨家化 | ok | 42.14 | close_below_ma200; stock_return_120d -12.17% < 6.00%; excess_return_120d -16.65% < 6.00%; drawdown_120d -29.31% < -28.00%; volatility_120d 55.12% > 42.00% |
| 300410.SZ | 正业科技 | ok | 42.14 | close_below_ma200; excess_return_240d -2.06% < 8.00%; drawdown_120d -32.97% < -28.00%; volatility_120d 56.97% > 42.00% |
| 002448.SZ | 中原内配 | ok | 42.03 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.47% < 6.00%; excess_return_120d -5.05% < 6.00%; drawdown_120d -28.70% < -28.00%; volatility_120d 55.16% > 42.00% |
| 300435.SZ | 中泰股份 | ok | 42.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 1.59% < 6.00%; excess_return_120d -2.99% < 6.00%; drawdown_120d -38.43% < -28.00%; volatility_120d 69.51% > 42.00% |
| 603119.SH | 浙江荣泰 | ok | 41.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.64% < 6.00%; excess_return_120d -26.22% < 6.00%; volatility_120d 56.86% > 42.00% |
| 002421.SZ | 达实智能 | ok | 41.94 | close_below_ma200; excess_return_240d -26.47% < 8.00%; drawdown_120d -48.54% < -28.00%; volatility_120d 70.20% > 42.00% |
| 688176.SH | 亚虹医药 | ok | 41.91 | ma60_not_above_ma120; excess_return_120d 1.68% < 6.00%; drawdown_120d -32.47% < -28.00%; volatility_120d 65.97% > 42.00% |
| 301227.SZ | 森鹰窗业 | ok | 41.88 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.92% < 6.00%; excess_return_120d -33.50% < 6.00%; drawdown_120d -28.91% < -28.00%; volatility_120d 59.63% > 42.00% |
| 002196.SZ | 方正电机 | ok | 41.84 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.95% < 6.00%; excess_return_120d -21.53% < 6.00%; drawdown_120d -32.76% < -28.00%; volatility_120d 59.13% > 42.00% |
| 002256.SZ | 兆新股份 | ok | 41.83 | close_below_ma200; stock_return_120d 2.01% < 6.00%; excess_return_120d -2.57% < 6.00%; drawdown_120d -38.09% < -28.00%; volatility_120d 56.10% > 42.00% |
| 300550.SZ | 和仁科技 | ok | 41.81 | ma60_not_above_ma120; excess_return_120d 2.39% < 6.00%; excess_return_240d -8.21% < 8.00%; volatility_120d 59.15% > 42.00% |
| 600295.SH | 鄂尔多斯 | ok | 41.75 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 1.37% < 6.00%; excess_return_120d -3.21% < 6.00%; drawdown_120d -31.91% < -28.00%; volatility_120d 47.85% > 42.00% |
| 688367.SH | 工大高科 | ok | 41.73 | close_below_ma200; stock_return_120d -0.58% < 6.00%; excess_return_120d -5.16% < 6.00%; drawdown_120d -42.34% < -28.00%; volatility_120d 71.09% > 42.00% |
| 002335.SZ | 科华数据 | ok | 41.73 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.03% < 6.00%; excess_return_120d -4.61% < 6.00%; volatility_120d 61.73% > 42.00% |
| 603979.SH | 金诚信 | ok | 41.73 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.46% < 6.00%; excess_return_120d -19.04% < 6.00%; volatility_120d 60.49% > 42.00% |
| 300894.SZ | 火星人 | ok | 41.72 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_120d 1.70% < 6.00%; excess_return_240d -24.41% < 8.00%; volatility_120d 50.52% > 42.00% |
| 603286.SH | 日盈电子 | ok | 41.70 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.10% < 6.00%; excess_return_120d -25.68% < 6.00%; drawdown_120d -35.64% < -28.00%; volatility_120d 59.83% > 42.00% |
| 300105.SZ | 龙源技术 | ok | 41.64 | ma60_not_above_ma120; ma120_not_above_ma200; excess_return_120d 2.55% < 6.00%; excess_return_240d -25.55% < 8.00%; volatility_120d 49.49% > 42.00% |
| 300748.SZ | 金力永磁 | ok | 41.60 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.89% < 6.00%; excess_return_120d -8.48% < 6.00%; volatility_120d 52.14% > 42.00% |
| 601231.SH | 环旭电子 | ok | 41.56 | close_below_ma200; stock_return_120d 0.27% < 6.00%; excess_return_120d -4.31% < 6.00%; drawdown_120d -39.43% < -28.00%; volatility_120d 78.34% > 42.00% |
| 600580.SH | 卧龙电驱 | ok | 41.49 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.51% < 6.00%; excess_return_120d -27.09% < 6.00%; volatility_120d 42.14% > 42.00% |
| 600877.SH | 电科芯片 | ok | 41.47 | ma60_not_above_ma120; stock_return_120d -4.27% < 6.00%; excess_return_120d -8.85% < 6.00%; drawdown_120d -35.16% < -28.00%; volatility_120d 55.78% > 42.00% |
| 688577.SH | 浙海德曼 | ok | 41.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.09% < 6.00%; excess_return_120d -24.67% < 6.00%; volatility_120d 51.51% > 42.00% |
| 603626.SH | 科森科技 | ok | 41.38 | close_below_ma200; stock_return_120d -10.89% < 6.00%; excess_return_120d -15.47% < 6.00%; drawdown_120d -36.10% < -28.00%; volatility_120d 64.53% > 42.00% |
| 301186.SZ | 超达装备 | ok | 41.38 | excess_return_240d 0.13% < 8.00%; drawdown_120d -33.97% < -28.00%; volatility_120d 47.28% > 42.00% |
| 600201.SH | 生物股份 | ok | 41.33 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.26% < 6.00%; excess_return_120d -19.84% < 6.00%; drawdown_120d -32.82% < -28.00%; volatility_120d 45.08% > 42.00% |
| 600096.SH | 云天化 | ok | 41.24 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.96% < 6.00%; excess_return_120d -10.54% < 6.00%; drawdown_120d -31.81% < -28.00%; volatility_120d 48.74% > 42.00% |
| 002853.SZ | 皮阿诺 | ok | 41.23 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.01% < 6.00%; excess_return_120d -8.59% < 6.00%; drawdown_120d -40.37% < -28.00%; volatility_120d 51.48% > 42.00% |
| 002154.SZ | 报喜鸟 | ok | 41.18 | ma120_not_above_ma200; excess_return_120d 2.76% < 6.00%; excess_return_240d -13.17% < 8.00% |
| 001228.SZ | 永泰运 | ok | 41.17 | ma60_not_above_ma120; excess_return_120d 4.62% < 6.00%; excess_return_240d -6.30% < 8.00% |
| 000612.SZ | 焦作万方 | ok | 41.06 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -1.17% < 6.00%; excess_return_120d -5.75% < 6.00%; drawdown_120d -30.80% < -28.00%; volatility_120d 58.51% > 42.00% |
| 603391.SH | 力聚热能 | ok | 41.06 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.16% < 6.00%; excess_return_120d -15.74% < 6.00%; volatility_120d 44.57% > 42.00% |
| 300619.SZ | 金银河 | ok | 41.02 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.16% < 6.00%; excess_return_120d -12.74% < 6.00%; drawdown_120d -29.38% < -28.00%; volatility_120d 60.88% > 42.00% |
| 603992.SH | 松霖科技 | ok | 40.95 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.23% < 6.00%; excess_return_120d -27.81% < 6.00%; drawdown_120d -34.86% < -28.00%; volatility_120d 59.21% > 42.00% |
| 600030.SH | 中信证券 | ok | 40.94 | ma120_not_above_ma200; stock_return_120d 4.36% < 6.00%; excess_return_120d -0.22% < 6.00%; excess_return_240d -13.00% < 8.00% |
| 605069.SH | 正和生态 | ok | 40.92 | ma60_not_above_ma120; stock_return_120d -5.31% < 6.00%; excess_return_120d -9.89% < 6.00%; volatility_120d 65.72% > 42.00% |
| 002772.SZ | 众兴菌业 | ok | 40.87 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.33% < 6.00%; excess_return_120d -11.91% < 6.00%; drawdown_120d -32.53% < -28.00%; volatility_120d 54.17% > 42.00% |
| 301008.SZ | 宏昌科技 | ok | 40.86 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.87% < 6.00%; excess_return_120d -10.45% < 6.00%; drawdown_120d -34.41% < -28.00%; volatility_120d 71.82% > 42.00% |
| 603358.SH | 华达科技 | ok | 40.80 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.70% < 6.00%; excess_return_120d -16.28% < 6.00%; volatility_120d 55.36% > 42.00% |
| 002919.SZ | 名臣健康 | ok | 40.73 | ma60_not_above_ma120; stock_return_120d -3.84% < 6.00%; excess_return_120d -8.42% < 6.00%; volatility_120d 50.05% > 42.00% |
| 300504.SZ | 天邑股份 | ok | 40.70 | excess_return_120d 4.62% < 6.00%; excess_return_240d -16.46% < 8.00%; volatility_120d 54.83% > 42.00% |
| 002962.SZ | 五方光电 | ok | 40.68 | excess_return_120d 5.60% < 6.00%; excess_return_240d -13.33% < 8.00%; volatility_120d 60.29% > 42.00% |
| 002738.SZ | 中矿资源 | ok | 40.65 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.68% < 6.00%; excess_return_120d -23.26% < 6.00%; drawdown_120d -36.76% < -28.00%; volatility_120d 61.95% > 42.00% |
| 600362.SH | 江西铜业 | ok | 40.63 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.63% < 6.00%; excess_return_120d -28.21% < 6.00%; drawdown_120d -40.68% < -28.00%; volatility_120d 59.28% > 42.00% |
| 603659.SH | 璞泰来 | ok | 40.62 | close_below_ma200; stock_return_120d -0.26% < 6.00%; excess_return_120d -4.84% < 6.00%; drawdown_120d -28.20% < -28.00%; volatility_120d 48.36% > 42.00% |
| 002895.SZ | 川恒股份 | ok | 40.60 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.24% < 6.00%; excess_return_120d -14.82% < 6.00%; drawdown_120d -29.11% < -28.00%; volatility_120d 48.79% > 42.00% |
| 301041.SZ | 金百泽 | ok | 40.56 | excess_return_120d 5.54% < 6.00%; excess_return_240d -11.15% < 8.00%; volatility_120d 51.26% > 42.00% |
| 002249.SZ | 大洋电机 | ok | 40.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.01% < 6.00%; excess_return_120d -23.59% < 6.00% |
| 600750.SH | 华润江中 | ok | 40.49 | ma60_not_above_ma120; excess_return_120d 2.06% < 6.00%; excess_return_240d -5.20% < 8.00% |
| 002128.SZ | 电投能源 | ok | 40.48 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.84% < 6.00%; excess_return_120d -11.42% < 6.00%; volatility_120d 45.58% > 42.00% |
| 603520.SH | 司太立 | ok | 40.41 | close_below_ma200; ma120_not_above_ma200; excess_return_240d -17.31% < 8.00%; drawdown_120d -28.26% < -28.00%; volatility_120d 47.17% > 42.00% |
| 603798.SH | 康普顿 | ok | 40.36 | close_below_ma200; stock_return_120d -8.79% < 6.00%; excess_return_120d -12.89% < 6.00%; volatility_120d 57.23% > 42.00% |
| 002460.SZ | 赣锋锂业 | ok | 40.31 | close_below_ma200; stock_return_120d -0.10% < 6.00%; excess_return_120d -4.68% < 6.00%; drawdown_120d -31.46% < -28.00%; volatility_120d 49.82% > 42.00% |
| 002792.SZ | 通宇通讯 | ok | 40.30 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.80% < 6.00%; excess_return_120d -26.38% < 6.00%; drawdown_120d -54.49% < -28.00%; volatility_120d 73.71% > 42.00% |
| 600841.SH | 动力新科 | ok | 40.28 | close_below_ma200; ma60_not_above_ma120; excess_return_240d -10.15% < 8.00%; drawdown_120d -40.02% < -28.00%; volatility_120d 63.05% > 42.00% |
| 600143.SH | 金发科技 | ok | 40.25 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.44% < 6.00%; excess_return_120d -21.02% < 6.00%; volatility_120d 44.28% > 42.00% |
| 600388.SH | 龙净环保 | ok | 40.24 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.02% < 6.00%; excess_return_120d -7.60% < 6.00% |
| 603090.SH | 宏盛股份 | ok | 40.19 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.63% < 6.00%; excess_return_120d -5.21% < 6.00%; drawdown_120d -44.48% < -28.00%; volatility_120d 70.86% > 42.00% |
| 301276.SZ | 嘉曼服饰 | ok | 40.18 | ma60_not_above_ma120; stock_return_120d -15.03% < 6.00%; excess_return_120d -19.61% < 6.00%; volatility_120d 59.61% > 42.00% |
| 000893.SZ | 亚钾国际 | ok | 40.16 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.60% < 6.00%; excess_return_120d -11.18% < 6.00%; drawdown_120d -37.46% < -28.00%; volatility_120d 53.82% > 42.00% |
| 601108.SH | 财通证券 | ok | 40.11 | ma60_not_above_ma120; stock_return_120d 5.31% < 6.00%; excess_return_120d 0.73% < 6.00%; excess_return_240d -3.29% < 8.00% |
| 688619.SH | 罗普特 | ok | 40.07 | close_below_ma200; excess_return_240d -2.67% < 8.00%; drawdown_120d -28.99% < -28.00%; volatility_120d 56.99% > 42.00% |
| 003041.SZ | 真爱美家 | ok | 40.07 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -1.89% < 6.00%; excess_return_120d -6.18% < 6.00%; drawdown_120d -42.35% < -28.00%; volatility_120d 75.72% > 42.00% |
| 000719.SZ | 中原传媒 | ok | 40.04 | close_below_ma200; excess_return_120d 2.90% < 6.00%; excess_return_240d -24.96% < 8.00% |
| 300590.SZ | 移为通信 | ok | 40.03 | excess_return_120d 3.30% < 6.00%; excess_return_240d -13.90% < 8.00%; volatility_120d 49.67% > 42.00% |
| 601689.SH | 拓普集团 | ok | 40.03 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.02% < 6.00%; excess_return_120d -25.60% < 6.00%; drawdown_120d -28.75% < -28.00%; volatility_120d 45.62% > 42.00% |
| 300456.SZ | 赛微电子 | ok | 39.97 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -28.85% < 6.00%; excess_return_120d -33.43% < 6.00%; drawdown_120d -39.35% < -28.00%; volatility_120d 71.34% > 42.00% |
| 600343.SH | 航天动力 | ok | 39.95 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -47.01% < 6.00%; excess_return_120d -51.59% < 6.00%; drawdown_120d -49.00% < -28.00%; volatility_120d 73.40% > 42.00% |
| 688039.SH | 当虹科技 | ok | 39.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -2.66% < 6.00%; excess_return_120d -7.24% < 6.00%; drawdown_120d -37.77% < -28.00%; volatility_120d 68.32% > 42.00% |
| 000559.SZ | 万向钱潮 | ok | 39.85 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.82% < 6.00%; excess_return_120d -27.40% < 6.00%; drawdown_120d -39.26% < -28.00%; volatility_120d 54.68% > 42.00% |
| 688006.SH | 杭可科技 | ok | 39.81 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -2.01% < 6.00%; excess_return_120d -6.59% < 6.00%; drawdown_120d -32.96% < -28.00%; volatility_120d 64.49% > 42.00% |
| 000426.SZ | 兴业银锡 | ok | 39.80 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 0.00% < 6.00%; excess_return_120d -4.58% < 6.00%; drawdown_120d -52.41% < -28.00%; volatility_120d 72.91% > 42.00% |
| 603050.SH | 科林电气 | ok | 39.74 | close_below_ma200; excess_return_120d 5.45% < 6.00%; excess_return_240d 0.16% < 8.00%; drawdown_120d -28.38% < -28.00%; volatility_120d 50.96% > 42.00% |
| 002545.SZ | 东方铁塔 | ok | 39.74 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -1.41% < 6.00%; excess_return_120d -5.99% < 6.00%; drawdown_120d -41.13% < -28.00%; volatility_120d 59.88% > 42.00% |
| 002970.SZ | 锐明技术 | ok | 39.64 | close_below_ma200; ma60_not_above_ma120; excess_return_240d -14.05% < 8.00%; drawdown_120d -36.92% < -28.00%; volatility_120d 62.04% > 42.00% |
| 002444.SZ | 巨星科技 | ok | 39.62 | ma60_not_above_ma120; stock_return_120d 0.15% < 6.00%; excess_return_120d -4.43% < 6.00%; excess_return_240d 7.46% < 8.00% |
| 300102.SZ | 乾照光电 | ok | 39.56 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.81% < 6.00%; excess_return_120d -22.39% < 6.00%; drawdown_120d -51.64% < -28.00%; volatility_120d 83.75% > 42.00% |
| 688556.SH | 高测股份 | ok | 39.52 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -1.23% < 6.00%; excess_return_120d -5.81% < 6.00%; drawdown_120d -39.32% < -28.00%; volatility_120d 80.26% > 42.00% |
| 603196.SH | 璞源材料 | ok | 39.46 | close_below_ma200; stock_return_120d -9.71% < 6.00%; excess_return_120d -14.29% < 6.00%; drawdown_120d -34.79% < -28.00%; volatility_120d 49.59% > 42.00% |
| 601899.SH | 紫金矿业 | ok | 39.43 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.04% < 6.00%; excess_return_120d -21.62% < 6.00%; drawdown_120d -36.54% < -28.00%; volatility_120d 50.60% > 42.00% |
| 600089.SH | 特变电工 | ok | 39.41 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -2.33% < 6.00%; excess_return_120d -6.91% < 6.00%; drawdown_120d -35.15% < -28.00%; volatility_120d 46.31% > 42.00% |
| 300322.SZ | 硕贝德 | ok | 39.38 | close_below_ma200; stock_return_120d -14.14% < 6.00%; excess_return_120d -18.72% < 6.00%; drawdown_120d -36.47% < -28.00%; volatility_120d 72.01% > 42.00% |
| 300458.SZ | 全志科技 | ok | 39.35 | ma120_not_above_ma200; excess_return_120d 1.91% < 6.00%; excess_return_240d -4.76% < 8.00%; volatility_120d 48.25% > 42.00% |
| 002413.SZ | 雷科防务 | ok | 39.24 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.66% < 6.00%; excess_return_120d -30.24% < 6.00%; drawdown_120d -54.02% < -28.00%; volatility_120d 64.92% > 42.00% |
| 002176.SZ | 江特电机 | ok | 39.22 | close_below_ma200; stock_return_120d 1.44% < 6.00%; excess_return_120d -3.14% < 6.00%; drawdown_120d -41.78% < -28.00%; volatility_120d 50.31% > 42.00% |
| 600711.SH | 盛屯矿业 | ok | 39.13 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -24.76% < 6.00%; excess_return_120d -29.34% < 6.00%; drawdown_120d -39.14% < -28.00%; volatility_120d 60.28% > 42.00% |
| 600550.SH | 保变电气 | ok | 39.05 | close_below_ma200; ma60_not_above_ma120; excess_return_120d 3.29% < 6.00%; excess_return_240d 6.48% < 8.00%; drawdown_120d -41.88% < -28.00%; volatility_120d 58.99% > 42.00% |
| 300455.SZ | 航天智装 | ok | 39.02 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -28.76% < 6.00%; excess_return_120d -33.34% < 6.00%; drawdown_120d -48.43% < -28.00%; volatility_120d 58.06% > 42.00% |
| 601061.SH | 中信金属 | ok | 38.90 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.38% < 6.00%; excess_return_120d -24.96% < 6.00%; drawdown_120d -34.55% < -28.00%; volatility_120d 45.16% > 42.00% |
| 002487.SZ | 大金重工 | ok | 38.89 | close_below_ma200; stock_return_120d 0.57% < 6.00%; excess_return_120d -4.01% < 6.00%; drawdown_120d -44.64% < -28.00%; volatility_120d 53.18% > 42.00% |
| 601882.SH | 海天精工 | ok | 38.88 | excess_return_120d 3.14% < 6.00%; excess_return_240d -10.19% < 8.00% |
| 688691.SH | 灿芯股份 | ok | 38.82 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.59% < 6.00%; excess_return_120d -9.17% < 6.00%; drawdown_120d -42.28% < -28.00%; volatility_120d 87.53% > 42.00% |
| 002048.SZ | 宁波华翔 | ok | 38.79 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.28% < 6.00%; excess_return_120d -22.86% < 6.00%; drawdown_120d -29.62% < -28.00%; volatility_120d 50.45% > 42.00% |
| 000921.SZ | 海信家电 | ok | 38.69 | ma120_not_above_ma200; excess_return_120d 1.71% < 6.00%; excess_return_240d -15.58% < 8.00% |
| 300115.SZ | 长盈精密 | ok | 38.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.89% < 6.00%; excess_return_120d -38.47% < 6.00%; drawdown_120d -33.89% < -28.00%; volatility_120d 49.35% > 42.00% |
| 603898.SH | 好莱客 | ok | 38.55 | ma60_not_above_ma120; stock_return_120d 4.96% < 6.00%; excess_return_120d 0.38% < 6.00%; excess_return_240d 6.72% < 8.00%; volatility_120d 44.83% > 42.00% |
| 300421.SZ | 力星股份 | ok | 38.54 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -43.35% < 6.00%; excess_return_120d -47.93% < 6.00%; drawdown_120d -45.65% < -28.00%; volatility_120d 50.85% > 42.00% |
| 600348.SH | 华阳股份 | ok | 38.52 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 3.03% < 6.00%; excess_return_120d -1.55% < 6.00% |
| 002901.SZ | 大博医疗 | ok | 38.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -2.53% < 6.00%; excess_return_120d -7.11% < 6.00%; excess_return_240d 6.27% < 8.00% |
| 603298.SH | 杭叉集团 | ok | 38.38 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 1.26% < 6.00%; excess_return_120d -3.32% < 6.00%; excess_return_240d 6.61% < 8.00% |
| 002549.SZ | 凯美特气 | ok | 38.38 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.82% < 6.00%; excess_return_120d -21.40% < 6.00%; drawdown_120d -28.85% < -28.00%; volatility_120d 55.80% > 42.00% |
| 605090.SH | 九丰能源 | ok | 38.35 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.25% < 6.00%; excess_return_120d -23.83% < 6.00%; drawdown_120d -37.18% < -28.00%; volatility_120d 51.21% > 42.00% |
| 002983.SZ | 芯瑞达 | ok | 38.33 | excess_return_120d 2.26% < 6.00%; excess_return_240d -3.87% < 8.00%; volatility_120d 48.86% > 42.00% |
| 301097.SZ | 天益医疗 | ok | 38.27 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 2.52% < 6.00%; excess_return_120d -2.06% < 6.00%; volatility_120d 48.84% > 42.00% |
| 601985.SH | 中国核电 | ok | 38.27 | close_below_ma200; stock_return_120d 2.67% < 6.00%; excess_return_120d -1.92% < 6.00%; excess_return_240d -25.31% < 8.00% |
| 600801.SH | 华新建材 | ok | 38.24 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -26.22% < 6.00%; excess_return_120d -30.80% < 6.00%; drawdown_120d -31.57% < -28.00%; volatility_120d 42.19% > 42.00% |
| 603087.SH | 甘李药业 | ok | 38.21 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 0.03% < 6.00%; excess_return_120d -4.55% < 6.00%; excess_return_240d 4.07% < 8.00% |
| 600346.SH | 恒力石化 | ok | 38.15 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.74% < 6.00%; excess_return_120d -20.32% < 6.00%; drawdown_120d -30.52% < -28.00%; volatility_120d 55.36% > 42.00% |
| 300588.SZ | 熙菱信息 | ok | 38.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.33% < 6.00%; excess_return_120d -27.91% < 6.00%; drawdown_120d -32.35% < -28.00%; volatility_120d 57.19% > 42.00% |
| 688108.SH | 赛诺医疗 | ok | 38.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -2.86% < 6.00%; excess_return_120d -7.44% < 6.00%; drawdown_120d -28.83% < -28.00%; volatility_120d 54.37% > 42.00% |
| 301538.SZ | 骏鼎达 | ok | 38.05 | close_below_ma200; stock_return_120d -11.84% < 6.00%; excess_return_120d -16.42% < 6.00%; drawdown_120d -41.56% < -28.00%; volatility_120d 59.65% > 42.00% |
| 300014.SZ | 亿纬锂能 | ok | 38.02 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -9.39% < 6.00%; excess_return_120d -13.97% < 6.00%; volatility_120d 49.64% > 42.00% |
| 000547.SZ | 航天发展 | ok | 37.99 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -46.38% < 6.00%; excess_return_120d -50.96% < 6.00%; drawdown_120d -56.46% < -28.00%; volatility_120d 68.71% > 42.00% |
| 002565.SZ | 顺灏股份 | ok | 37.99 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -38.08% < 6.00%; excess_return_120d -42.66% < 6.00%; drawdown_120d -51.50% < -28.00%; volatility_120d 78.57% > 42.00% |
| 002370.SZ | 亚太药业 | ok | 37.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.20% < 6.00%; excess_return_120d -25.78% < 6.00%; drawdown_120d -29.93% < -28.00%; volatility_120d 45.18% > 42.00% |
| 600884.SH | 杉杉股份 | ok | 37.95 | close_below_ma200; stock_return_120d -2.74% < 6.00%; excess_return_120d -7.32% < 6.00%; volatility_120d 48.23% > 42.00% |
| 603920.SH | 世运电路 | ok | 37.92 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.02% < 6.00%; excess_return_120d -15.60% < 6.00%; drawdown_120d -40.85% < -28.00%; volatility_120d 66.02% > 42.00% |
| 600489.SH | 中金黄金 | ok | 37.90 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.82% < 6.00%; excess_return_120d -16.40% < 6.00%; drawdown_120d -50.34% < -28.00%; volatility_120d 60.16% > 42.00% |
| 000685.SZ | 中山公用 | ok | 37.88 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -2.49% < 6.00%; excess_return_120d -7.07% < 6.00%; excess_return_240d 6.57% < 8.00% |
| 300464.SZ | 星徽股份 | ok | 37.88 | close_below_ma200; excess_return_120d 3.78% < 6.00%; excess_return_240d 3.59% < 8.00%; drawdown_120d -37.72% < -28.00%; volatility_120d 49.01% > 42.00% |
| 603345.SH | 安井食品 | ok | 37.86 | excess_return_120d 3.56% < 6.00%; excess_return_240d -6.80% < 8.00% |
| 002445.SZ | 中南文化 | ok | 37.83 | close_below_ma200; excess_return_120d 5.30% < 6.00%; excess_return_240d -8.92% < 8.00%; drawdown_120d -40.88% < -28.00%; volatility_120d 62.93% > 42.00% |
| 688188.SH | 柏楚电子 | ok | 37.80 | excess_return_120d 3.18% < 6.00%; excess_return_240d -7.72% < 8.00% |
| 688031.SH | 星环科技 | ok | 37.78 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.38% < 6.00%; excess_return_120d -10.96% < 6.00%; drawdown_120d -61.76% < -28.00%; volatility_120d 117.50% > 42.00% |
| 600151.SH | 航天机电 | ok | 37.74 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -39.43% < 6.00%; excess_return_120d -44.01% < 6.00%; drawdown_120d -53.38% < -28.00%; volatility_120d 62.38% > 42.00% |
| 000651.SZ | 格力电器 | ok | 37.74 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -0.57% < 6.00%; excess_return_120d -5.15% < 6.00%; excess_return_240d -31.67% < 8.00% |
| 000933.SZ | 神火股份 | ok | 37.69 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.58% < 6.00%; excess_return_120d -20.16% < 6.00%; drawdown_120d -41.79% < -28.00%; volatility_120d 52.33% > 42.00% |
| 301592.SZ | 六九一二 | ok | 37.68 | ma120_not_above_ma200; excess_return_120d 1.54% < 6.00%; excess_return_240d -29.01% < 8.00%; volatility_120d 56.29% > 42.00% |
| 000807.SZ | 云铝股份 | ok | 37.61 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -29.52% < 6.00%; excess_return_120d -34.10% < 6.00%; drawdown_120d -39.55% < -28.00%; volatility_120d 54.38% > 42.00% |
| 688027.SH | 国盾量子 | ok | 37.59 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.55% < 6.00%; excess_return_120d -18.13% < 6.00%; drawdown_120d -42.76% < -28.00%; volatility_120d 64.11% > 42.00% |
| 603416.SH | 信捷电气 | ok | 37.58 | ma120_not_above_ma200; excess_return_120d 1.79% < 6.00%; excess_return_240d -14.11% < 8.00%; volatility_120d 48.39% > 42.00% |
| 688252.SH | 天德钰 | ok | 37.57 | close_below_ma200; ma120_not_above_ma200; excess_return_120d 2.69% < 6.00%; excess_return_240d -26.31% < 8.00%; volatility_120d 49.19% > 42.00% |
| 603977.SH | 国泰集团 | ok | 37.55 | ma60_not_above_ma120; excess_return_120d 2.03% < 6.00%; excess_return_240d -0.27% < 8.00%; volatility_120d 52.20% > 42.00% |
| 600377.SH | 宁沪高速 | ok | 37.50 | close_below_ma200; ma120_not_above_ma200; stock_return_120d 1.73% < 6.00%; excess_return_120d -2.85% < 6.00%; excess_return_240d -37.12% < 8.00% |
| 002120.SZ | 韵达股份 | ok | 37.43 | ma120_not_above_ma200; excess_return_120d 1.52% < 6.00%; excess_return_240d -15.64% < 8.00% |
| 605598.SH | 上海港湾 | ok | 37.42 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -45.88% < 6.00%; excess_return_120d -50.46% < 6.00%; drawdown_120d -51.42% < -28.00%; volatility_120d 64.46% > 42.00% |
| 300274.SZ | 阳光电源 | ok | 37.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.76% < 6.00%; excess_return_120d -29.34% < 6.00%; drawdown_120d -33.14% < -28.00%; volatility_120d 60.03% > 42.00% |
| 600688.SH | 上海石化 | ok | 37.28 | ma60_not_above_ma120; excess_return_120d 3.33% < 6.00%; excess_return_240d -16.57% < 8.00%; volatility_120d 47.24% > 42.00% |
| 301120.SZ | 新特电气 | ok | 37.27 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.44% < 6.00%; excess_return_120d -10.02% < 6.00%; drawdown_120d -45.49% < -28.00%; volatility_120d 77.48% > 42.00% |
| 603075.SH | 热威股份 | ok | 37.24 | excess_return_120d 2.80% < 6.00%; excess_return_240d -4.75% < 8.00% |
| 688251.SH | 井松智能 | ok | 37.24 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.97% < 6.00%; excess_return_120d -21.55% < 6.00%; drawdown_120d -37.06% < -28.00%; volatility_120d 42.92% > 42.00% |
| 688282.SH | 理工导航 | ok | 37.20 | close_below_ma200; stock_return_120d -0.16% < 6.00%; excess_return_120d -4.74% < 6.00%; drawdown_120d -38.37% < -28.00%; volatility_120d 77.98% > 42.00% |
| 002560.SZ | 通达股份 | ok | 37.17 | close_below_ma200; stock_return_120d 1.74% < 6.00%; excess_return_120d -2.84% < 6.00%; drawdown_120d -43.72% < -28.00%; volatility_120d 63.68% > 42.00% |
| 600182.SH | S佳通 | ok | 37.16 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 0.54% < 6.00%; excess_return_120d -4.04% < 6.00%; excess_return_240d -25.38% < 8.00% |
| 600510.SH | 黑牡丹 | ok | 37.16 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.14% < 6.00%; excess_return_120d -19.72% < 6.00%; drawdown_120d -39.14% < -28.00%; volatility_120d 52.74% > 42.00% |
| 688330.SH | 宏力达 | ok | 37.09 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.93% < 6.00%; excess_return_120d -8.51% < 6.00%; drawdown_120d -42.20% < -28.00%; volatility_120d 58.92% > 42.00% |
| 301213.SZ | 观想科技 | ok | 37.08 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.17% < 6.00%; excess_return_120d -5.89% < 6.00%; drawdown_120d -41.43% < -28.00%; volatility_120d 72.14% > 42.00% |
| 600895.SH | 张江高科 | ok | 37.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.46% < 6.00%; excess_return_120d -26.04% < 6.00%; drawdown_120d -30.12% < -28.00%; volatility_120d 42.66% > 42.00% |
| 002430.SZ | 杭氧股份 | ok | 37.06 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.60% < 6.00%; excess_return_120d -16.18% < 6.00%; volatility_120d 49.91% > 42.00% |
| 600076.SH | 康欣新材 | ok | 37.06 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -1.19% < 6.00%; excess_return_120d -5.77% < 6.00%; drawdown_120d -29.45% < -28.00%; volatility_120d 67.33% > 42.00% |
| 002729.SZ | 好利科技 | ok | 37.03 | excess_return_120d 3.55% < 6.00%; excess_return_240d -9.09% < 8.00%; volatility_120d 53.92% > 42.00% |
| 603803.SH | 瑞斯康达 | ok | 37.00 | close_below_ma200; stock_return_120d 2.16% < 6.00%; excess_return_120d -2.42% < 6.00%; drawdown_120d -36.02% < -28.00%; volatility_120d 66.72% > 42.00% |
| 001289.SZ | 龙源电力 | ok | 36.98 | close_below_ma200; excess_return_120d 2.98% < 6.00%; excess_return_240d -22.98% < 8.00% |
| 001313.SZ | 粤海饲料 | ok | 36.93 | excess_return_120d 3.07% < 6.00%; excess_return_240d -19.66% < 8.00%; volatility_120d 51.93% > 42.00% |
| 603068.SH | 博通集成 | ok | 36.89 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 4.37% < 6.00%; excess_return_120d -0.21% < 6.00%; excess_return_240d -5.41% < 8.00% |
| 000762.SZ | 西藏矿业 | ok | 36.88 | close_below_ma200; stock_return_120d 1.52% < 6.00%; excess_return_120d -3.06% < 6.00%; drawdown_120d -35.63% < -28.00%; volatility_120d 54.16% > 42.00% |
| 300554.SZ | 三超新材 | ok | 36.86 | close_below_ma200; excess_return_120d 4.17% < 6.00%; excess_return_240d -25.32% < 8.00%; volatility_120d 51.56% > 42.00% |
| 001332.SZ | 锡装股份 | ok | 36.84 | close_below_ma200; stock_return_120d -12.24% < 6.00%; excess_return_120d -16.82% < 6.00%; drawdown_120d -35.21% < -28.00%; volatility_120d 57.14% > 42.00% |
| 300469.SZ | 信息发展 | ok | 36.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.06% < 6.00%; excess_return_120d -22.64% < 6.00%; drawdown_120d -34.13% < -28.00%; volatility_120d 64.09% > 42.00% |
| 300022.SZ | 吉峰科技 | ok | 36.57 | close_below_ma200; excess_return_120d 2.45% < 6.00%; excess_return_240d -35.25% < 8.00% |
| 603082.SH | 北自科技 | ok | 36.54 | excess_return_120d 2.83% < 6.00%; excess_return_240d -18.65% < 8.00%; volatility_120d 56.46% > 42.00% |
| 600998.SH | 九州通 | ok | 36.50 | ma60_not_above_ma120; stock_return_120d 2.64% < 6.00%; excess_return_120d -1.94% < 6.00%; excess_return_240d -21.10% < 8.00% |
| 002532.SZ | 天山铝业 | ok | 36.42 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -26.67% < 6.00%; excess_return_120d -31.25% < 6.00%; drawdown_120d -46.08% < -28.00%; volatility_120d 56.37% > 42.00% |
| 000901.SZ | 航天科技 | ok | 36.41 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -40.20% < 6.00%; excess_return_120d -44.78% < 6.00%; drawdown_120d -51.91% < -28.00%; volatility_120d 56.40% > 42.00% |
| 002051.SZ | 中工国际 | ok | 36.31 | excess_return_120d 3.68% < 6.00%; excess_return_240d -4.58% < 8.00%; drawdown_120d -30.17% < -28.00%; volatility_120d 69.54% > 42.00% |
| 300329.SZ | 海伦钢琴 | ok | 36.29 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.65% < 6.00%; excess_return_120d -34.23% < 6.00%; drawdown_120d -30.72% < -28.00% |
| 605196.SH | 华通线缆 | ok | 36.29 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.09% < 6.00%; excess_return_120d -20.67% < 6.00%; drawdown_120d -51.08% < -28.00%; volatility_120d 65.59% > 42.00% |
| 601211.SH | 国泰海通 | ok | 36.26 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -1.98% < 6.00%; excess_return_120d -6.56% < 6.00%; excess_return_240d -14.87% < 8.00% |
| 002032.SZ | 苏泊尔 | ok | 36.23 | close_below_ma200; ma120_not_above_ma200; stock_return_120d 3.96% < 6.00%; excess_return_120d -0.62% < 6.00%; excess_return_240d -33.51% < 8.00% |
| 600025.SH | 华能水电 | ok | 36.22 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 4.00% < 6.00%; excess_return_120d -0.58% < 6.00%; excess_return_240d -22.64% < 8.00% |
| 601212.SH | 白银有色 | ok | 36.20 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.26% < 6.00%; excess_return_120d -14.84% < 6.00%; drawdown_120d -65.44% < -28.00%; volatility_120d 74.04% > 42.00% |
| 300050.SZ | 世纪鼎利 | ok | 36.19 | close_below_ma200; excess_return_120d 4.46% < 6.00%; excess_return_240d -14.18% < 8.00%; volatility_120d 45.54% > 42.00% |
| 002009.SZ | 天奇股份 | ok | 36.15 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.42% < 6.00%; excess_return_120d -14.00% < 6.00%; drawdown_120d -46.08% < -28.00%; volatility_120d 64.79% > 42.00% |
| 688215.SH | 瑞晟智能 | ok | 36.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.84% < 6.00%; excess_return_120d -27.42% < 6.00%; drawdown_120d -30.84% < -28.00%; volatility_120d 42.73% > 42.00% |
| 300658.SZ | 延江股份 | ok | 36.10 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.38% < 6.00%; excess_return_120d -10.10% < 6.00%; drawdown_120d -63.22% < -28.00%; volatility_120d 97.70% > 42.00% |
| 600410.SH | 华胜天成 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.11% < 6.00%; excess_return_120d -20.69% < 6.00%; drawdown_120d -56.28% < -28.00%; volatility_120d 70.82% > 42.00% |
| 688335.SH | 复洁科技 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.36% < 6.00%; excess_return_120d -23.94% < 6.00%; drawdown_120d -51.55% < -28.00%; volatility_120d 75.67% > 42.00% |
| 301057.SZ | 汇隆新材 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.33% < 6.00%; excess_return_120d -25.82% < 6.00%; drawdown_120d -50.39% < -28.00%; volatility_120d 58.18% > 42.00% |
| 000603.SZ | 盛达资源 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.79% < 6.00%; excess_return_120d -26.37% < 6.00%; drawdown_120d -67.17% < -28.00%; volatility_120d 73.91% > 42.00% |
| 300450.SZ | 先导智能 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.78% < 6.00%; excess_return_120d -28.36% < 6.00%; drawdown_120d -43.63% < -28.00%; volatility_120d 51.85% > 42.00% |
| 600021.SH | 上海电力 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.78% < 6.00%; excess_return_120d -29.36% < 6.00%; drawdown_120d -39.62% < -28.00%; volatility_120d 48.56% > 42.00% |
| 301413.SZ | 安培龙 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.05% < 6.00%; excess_return_120d -30.63% < 6.00%; drawdown_120d -44.34% < -28.00%; volatility_120d 60.49% > 42.00% |
| 603778.SH | 国晟科技 | ok | 36.00 | close_below_ma200; stock_return_120d -31.41% < 6.00%; excess_return_120d -35.38% < 6.00%; drawdown_120d -69.48% < -28.00%; volatility_120d 107.32% > 42.00% |
| 688210.SH | 统联精密 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.03% < 6.00%; excess_return_120d -36.61% < 6.00%; drawdown_120d -40.19% < -28.00%; volatility_120d 65.72% > 42.00% |
| 600629.SH | 华建集团 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.57% < 6.00%; excess_return_120d -39.15% < 6.00%; drawdown_120d -44.72% < -28.00%; volatility_120d 47.08% > 42.00% |
| 600376.SH | 首开股份 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.94% < 6.00%; excess_return_120d -44.52% < 6.00%; drawdown_120d -39.20% < -28.00%; volatility_120d 53.97% > 42.00% |
| 688109.SH | 品茗科技 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.84% < 6.00%; excess_return_120d -45.42% < 6.00%; drawdown_120d -52.00% < -28.00%; volatility_120d 62.20% > 42.00% |
| 301117.SZ | 佳缘科技 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -41.45% < 6.00%; excess_return_120d -46.03% < 6.00%; drawdown_120d -63.09% < -28.00%; volatility_120d 69.89% > 42.00% |
| 300539.SZ | 横河精密 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -45.83% < 6.00%; excess_return_120d -50.41% < 6.00%; drawdown_120d -46.63% < -28.00%; volatility_120d 62.92% > 42.00% |
| 603516.SH | 淳中科技 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -48.16% < 6.00%; excess_return_120d -52.75% < 6.00%; drawdown_120d -56.71% < -28.00%; volatility_120d 71.17% > 42.00% |
| 605255.SH | 天普股份 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -48.84% < 6.00%; excess_return_120d -53.63% < 6.00%; drawdown_120d -64.77% < -28.00%; volatility_120d 81.09% > 42.00% |
| 002759.SZ | 天际股份 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -49.54% < 6.00%; excess_return_120d -54.12% < 6.00%; drawdown_120d -58.15% < -28.00%; volatility_120d 66.10% > 42.00% |
| 300300.SZ | 海峡创新 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -50.77% < 6.00%; excess_return_120d -55.35% < 6.00%; drawdown_120d -54.04% < -28.00%; volatility_120d 70.82% > 42.00% |
| 603122.SH | 合富中国 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -54.26% < 6.00%; excess_return_120d -58.84% < 6.00%; drawdown_120d -54.50% < -28.00%; volatility_120d 56.48% > 42.00% |
| 603216.SH | 梦天家居 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -54.59% < 6.00%; excess_return_120d -59.17% < 6.00%; drawdown_120d -63.76% < -28.00%; volatility_120d 57.92% > 42.00% |
| 600693.SH | 东百集团 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -54.94% < 6.00%; excess_return_120d -59.52% < 6.00%; drawdown_120d -63.86% < -28.00%; volatility_120d 58.22% > 42.00% |
| 000592.SZ | 平潭发展 | ok | 36.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -58.05% < 6.00%; excess_return_120d -62.63% < 6.00%; drawdown_120d -61.08% < -28.00%; volatility_120d 69.90% > 42.00% |
| 600323.SH | 瀚蓝环境 | ok | 36.00 | close_below_ma200; stock_return_120d 0.76% < 6.00%; excess_return_120d -3.60% < 6.00%; excess_return_240d 2.55% < 8.00% |
| 002890.SZ | 弘宇股份 | ok | 35.97 | close_below_ma200; ma60_not_above_ma120; excess_return_120d 1.57% < 6.00%; excess_return_240d -3.85% < 8.00% |
| 688235.SH | 百济神州 | ok | 35.91 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 3.13% < 6.00%; excess_return_120d -1.45% < 6.00%; excess_return_240d 3.03% < 8.00%; volatility_120d 45.39% > 42.00% |
| 600256.SH | 广汇能源 | ok | 35.90 | close_below_ma200; excess_return_120d 4.57% < 6.00%; excess_return_240d -21.25% < 8.00%; drawdown_120d -31.59% < -28.00%; volatility_120d 57.44% > 42.00% |
| 002488.SZ | 金固股份 | ok | 35.87 | close_below_ma200; ma60_not_above_ma120; excess_return_120d 5.33% < 6.00%; excess_return_240d -54.45% < 8.00%; drawdown_120d -29.82% < -28.00%; volatility_120d 46.58% > 42.00% |
| 605296.SH | 神农集团 | ok | 35.83 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 2.86% < 6.00%; excess_return_120d -1.72% < 6.00%; excess_return_240d -22.50% < 8.00% |
| 301225.SZ | 恒勃股份 | ok | 35.83 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -41.47% < 6.00%; excess_return_120d -46.05% < 6.00%; drawdown_120d -46.19% < -28.00%; volatility_120d 59.44% > 42.00% |
| 300129.SZ | 泰胜风能 | ok | 35.82 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.65% < 6.00%; excess_return_120d -12.23% < 6.00%; drawdown_120d -47.56% < -28.00%; volatility_120d 73.83% > 42.00% |
| 600595.SH | 中孚实业 | ok | 35.79 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.74% < 6.00%; excess_return_120d -27.32% < 6.00%; drawdown_120d -44.35% < -28.00%; volatility_120d 57.39% > 42.00% |
| 600886.SH | 国投电力 | ok | 35.76 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 2.82% < 6.00%; excess_return_120d -1.76% < 6.00%; excess_return_240d -28.09% < 8.00% |
| 600309.SH | 万华化学 | ok | 35.74 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.85% < 6.00%; excess_return_120d -10.43% < 6.00% |
| 603806.SH | 福斯特 | ok | 35.71 | close_below_ma200; excess_return_120d 4.25% < 6.00%; excess_return_240d -16.21% < 8.00%; volatility_120d 58.10% > 42.00% |
| 300709.SZ | 精研科技 | ok | 35.59 | ma120_not_above_ma200; excess_return_120d 2.49% < 6.00%; excess_return_240d -1.37% < 8.00%; volatility_120d 60.70% > 42.00% |
| 300049.SZ | 福瑞医科 | ok | 35.58 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.48% < 6.00%; excess_return_120d -42.06% < 6.00%; drawdown_120d -49.36% < -28.00%; volatility_120d 51.60% > 42.00% |
| 603217.SH | 元利科技 | ok | 35.55 | close_below_ma200; stock_return_120d -5.61% < 6.00%; excess_return_120d -10.19% < 6.00%; volatility_120d 49.37% > 42.00% |
| 600535.SH | 天士力 | ok | 35.41 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.61% < 6.00%; excess_return_120d -8.19% < 6.00%; excess_return_240d -28.36% < 8.00% |
| 600867.SH | 通化东宝 | ok | 35.36 | close_below_ma200; ma60_not_above_ma120; excess_return_120d 2.03% < 6.00%; excess_return_240d -10.12% < 8.00% |
| 002807.SZ | 江阴银行 | ok | 35.34 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -1.88% < 6.00%; excess_return_120d -6.46% < 6.00%; excess_return_240d -27.99% < 8.00% |
| 000628.SZ | 高新发展 | ok | 35.21 | close_below_ma200; excess_return_120d 4.32% < 6.00%; excess_return_240d -5.55% < 8.00%; drawdown_120d -28.70% < -28.00%; volatility_120d 54.12% > 42.00% |
| 603662.SH | 柯力传感 | ok | 35.20 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 1.67% < 6.00%; excess_return_120d -2.91% < 6.00%; excess_return_240d -2.08% < 8.00%; volatility_120d 43.11% > 42.00% |
| 603129.SH | 春风动力 | ok | 35.18 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -1.92% < 6.00%; excess_return_120d -6.50% < 6.00%; excess_return_240d -3.99% < 8.00% |
| 002841.SZ | 视源股份 | ok | 35.13 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 0.63% < 6.00%; excess_return_120d -3.95% < 6.00%; excess_return_240d -4.73% < 8.00% |
| 300694.SZ | 蠡湖股份 | ok | 35.12 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 3.79% < 6.00%; excess_return_120d -0.79% < 6.00%; excess_return_240d -31.95% < 8.00% |
| 300012.SZ | 华测检测 | ok | 35.11 | close_below_ma200; ma60_not_above_ma120; excess_return_120d 1.99% < 6.00%; excess_return_240d -2.01% < 8.00% |
| 601128.SH | 常熟银行 | ok | 35.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -2.40% < 6.00%; excess_return_120d -6.98% < 6.00%; excess_return_240d -28.19% < 8.00% |
| 002669.SZ | 康达新材 | ok | 35.05 | stock_return_120d 3.68% < 6.00%; excess_return_120d -0.90% < 6.00%; excess_return_240d 2.17% < 8.00%; volatility_120d 58.69% > 42.00% |
| 605228.SH | 神通科技 | ok | 35.04 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 0.64% < 6.00%; excess_return_120d -3.94% < 6.00%; excess_return_240d 4.00% < 8.00% |
| 688506.SH | 百利天恒 | ok | 34.98 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 2.14% < 6.00%; excess_return_120d -2.44% < 6.00%; excess_return_240d -8.16% < 8.00%; volatility_120d 61.50% > 42.00% |
| 601333.SH | 广深铁路 | ok | 34.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 0.00% < 6.00%; excess_return_120d -4.58% < 6.00%; excess_return_240d -14.98% < 8.00% |
| 301047.SZ | 义翘神州 | ok | 34.95 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 5.54% < 6.00%; excess_return_120d 0.96% < 6.00%; excess_return_240d -9.66% < 8.00% |
| 002107.SZ | 沃华医药 | ok | 34.93 | close_below_ma200; ma60_not_above_ma120; excess_return_120d 2.74% < 6.00%; excess_return_240d -6.64% < 8.00%; volatility_120d 42.51% > 42.00% |
| 301076.SZ | 新瀚新材 | ok | 34.91 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.51% < 6.00%; excess_return_120d -31.09% < 6.00%; drawdown_120d -31.76% < -28.00%; volatility_120d 49.82% > 42.00% |
| 600018.SH | 上港集团 | ok | 34.90 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.08% < 6.00%; excess_return_120d -11.66% < 6.00%; excess_return_240d -31.75% < 8.00% |
| 300249.SZ | 依米康 | ok | 34.89 | close_below_ma200; excess_return_120d 3.28% < 6.00%; excess_return_240d -3.86% < 8.00%; volatility_120d 62.65% > 42.00% |
| 601898.SH | 中煤能源 | ok | 34.85 | close_below_ma200; excess_return_120d 3.30% < 6.00%; excess_return_240d 2.29% < 8.00%; drawdown_120d -32.12% < -28.00%; volatility_120d 53.12% > 42.00% |
| 000034.SZ | 神州数码 | ok | 34.83 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 4.11% < 6.00%; excess_return_120d -0.47% < 6.00%; excess_return_240d -11.22% < 8.00%; volatility_120d 52.55% > 42.00% |
| 002258.SZ | 利尔化学 | ok | 34.83 | ma60_not_above_ma120; excess_return_120d 2.27% < 6.00%; excess_return_240d 0.52% < 8.00%; volatility_120d 50.10% > 42.00% |
| 000088.SZ | 盐田港 | ok | 34.82 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -2.83% < 6.00%; excess_return_120d -7.41% < 6.00%; excess_return_240d -24.42% < 8.00% |
| 601607.SH | 上海医药 | ok | 34.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.27% < 6.00%; excess_return_120d -11.85% < 6.00%; excess_return_240d -27.52% < 8.00% |
| 601518.SH | 吉林高速 | ok | 34.77 | close_below_ma200; stock_return_120d 2.97% < 6.00%; excess_return_120d -1.61% < 6.00%; excess_return_240d -14.97% < 8.00% |
| 688213.SH | 思特威 | ok | 34.71 | ma120_not_above_ma200; excess_return_120d 2.20% < 6.00%; excess_return_240d -24.64% < 8.00%; volatility_120d 50.89% > 42.00% |
| 000779.SZ | 甘咨询 | ok | 34.71 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; excess_return_120d 1.54% < 6.00%; excess_return_240d -28.76% < 8.00% |
| 600548.SH | 深高速 | ok | 34.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 0.23% < 6.00%; excess_return_120d -4.35% < 6.00%; excess_return_240d -34.76% < 8.00% |
| 600403.SH | 大有能源 | ok | 34.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.35% < 6.00%; excess_return_120d -27.93% < 6.00%; drawdown_120d -40.22% < -28.00%; volatility_120d 71.95% > 42.00% |
| 688219.SH | 会通股份 | ok | 34.60 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 1.30% < 6.00%; excess_return_120d -3.28% < 6.00%; excess_return_240d -10.22% < 8.00% |
| 688772.SH | 珠海冠宇 | ok | 34.52 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.56% < 6.00%; excess_return_120d -20.14% < 6.00%; volatility_120d 54.94% > 42.00% |
| 603811.SH | 诚意药业 | ok | 34.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 5.68% < 6.00%; excess_return_120d 1.10% < 6.00%; excess_return_240d -11.99% < 8.00% |
| 601059.SH | 信达证券 | ok | 34.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.42% < 6.00%; excess_return_120d -10.00% < 6.00%; excess_return_240d -17.24% < 8.00% |
| 600338.SH | 西藏珠峰 | ok | 34.25 | close_below_ma200; stock_return_120d -1.26% < 6.00%; excess_return_120d -5.84% < 6.00%; drawdown_120d -47.49% < -28.00%; volatility_120d 65.70% > 42.00% |
| 300418.SZ | 昆仑万维 | ok | 34.18 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 3.24% < 6.00%; excess_return_120d -1.34% < 6.00%; drawdown_120d -40.28% < -28.00%; volatility_120d 78.19% > 42.00% |
| 605123.SH | 派克新材 | ok | 34.12 | ma60_not_above_ma120; stock_return_120d -4.23% < 6.00%; excess_return_120d -8.81% < 6.00%; excess_return_240d 5.69% < 8.00%; volatility_120d 58.17% > 42.00% |
| 002332.SZ | 仙琚制药 | ok | 34.06 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.97% < 6.00%; excess_return_120d -8.55% < 6.00%; excess_return_240d -28.03% < 8.00% |
| 600035.SH | 楚天高速 | ok | 34.06 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.38% < 6.00%; excess_return_120d -9.96% < 6.00%; excess_return_240d -37.29% < 8.00% |
| 600351.SH | 亚宝药业 | ok | 34.06 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 2.28% < 6.00%; excess_return_120d -2.30% < 6.00%; excess_return_240d -15.19% < 8.00% |
| 603167.SH | 渤海轮渡 | ok | 34.01 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.82% < 6.00%; excess_return_120d -8.40% < 6.00%; excess_return_240d -35.45% < 8.00% |
| 002870.SZ | 香山股份 | ok | 33.99 | stock_return_120d 0.52% < 6.00%; excess_return_120d -4.06% < 6.00%; excess_return_240d 1.05% < 8.00% |
| 600666.SH | 奥瑞德 | ok | 33.98 | close_below_ma200; excess_return_120d 4.65% < 6.00%; excess_return_240d -15.94% < 8.00%; drawdown_120d -51.52% < -28.00%; volatility_120d 71.47% > 42.00% |
| 301178.SZ | 天亿马 | ok | 33.96 | close_below_ma200; ma120_not_above_ma200; excess_return_120d 3.07% < 6.00%; excess_return_240d -33.05% < 8.00%; volatility_120d 60.15% > 42.00% |
| 000859.SZ | 国风新材 | ok | 33.91 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.10% < 6.00%; excess_return_120d -12.68% < 6.00%; drawdown_120d -33.95% < -28.00%; volatility_120d 66.17% > 42.00% |
| 600109.SH | 国金证券 | ok | 33.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.55% < 6.00%; excess_return_120d -8.13% < 6.00%; excess_return_240d -22.31% < 8.00% |
| 001965.SZ | 招商公路 | ok | 33.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.95% < 6.00%; excess_return_120d -10.53% < 6.00%; excess_return_240d -39.33% < 8.00% |
| 300252.SZ | 金信诺 | ok | 33.75 | stock_return_120d 0.89% < 6.00%; excess_return_120d -3.69% < 6.00%; excess_return_240d 6.17% < 8.00%; volatility_120d 58.92% > 42.00% |
| 000810.SZ | 创维数字 | ok | 33.73 | ma120_not_above_ma200; stock_return_120d 4.36% < 6.00%; excess_return_120d -0.22% < 6.00%; excess_return_240d -13.80% < 8.00% |
| 600988.SH | 赤峰黄金 | ok | 33.71 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 0.57% < 6.00%; excess_return_120d -3.79% < 6.00%; drawdown_120d -38.26% < -28.00%; volatility_120d 67.99% > 42.00% |
| 000089.SZ | 深圳机场 | ok | 33.66 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.12% < 6.00%; excess_return_120d -9.70% < 6.00%; excess_return_240d -25.24% < 8.00% |
| 002795.SZ | 永和智控 | ok | 33.63 | close_below_ma200; stock_return_120d 5.71% < 6.00%; excess_return_120d 1.13% < 6.00%; excess_return_240d 4.80% < 8.00%; drawdown_120d -38.33% < -28.00%; volatility_120d 59.57% > 42.00% |
| 301068.SZ | 大地海洋 | ok | 33.55 | close_below_ma200; excess_return_120d 3.09% < 6.00%; excess_return_240d -33.06% < 8.00%; drawdown_120d -29.64% < -28.00%; volatility_120d 57.34% > 42.00% |
| 300763.SZ | 锦浪科技 | ok | 33.55 | close_below_ma200; excess_return_120d 2.64% < 6.00%; excess_return_240d 3.56% < 8.00%; drawdown_120d -38.82% < -28.00%; volatility_120d 67.92% > 42.00% |
| 000686.SZ | 东北证券 | ok | 33.44 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -4.58% < 6.00%; excess_return_120d -9.16% < 6.00%; excess_return_240d -4.59% < 8.00% |
| 002637.SZ | 赞宇科技 | ok | 33.43 | close_below_ma200; ma60_not_above_ma120; excess_return_120d 3.56% < 6.00%; excess_return_240d -11.99% < 8.00%; drawdown_120d -35.70% < -28.00%; volatility_120d 64.25% > 42.00% |
| 002828.SZ | 贝肯能源 | ok | 33.42 | close_below_ma200; ma60_not_above_ma120; excess_return_120d 2.92% < 6.00%; excess_return_240d -14.39% < 8.00%; drawdown_120d -35.98% < -28.00%; volatility_120d 63.52% > 42.00% |
| 002164.SZ | 宁波东力 | ok | 33.32 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.80% < 6.00%; excess_return_120d -30.38% < 6.00%; volatility_120d 45.27% > 42.00% |
| 600490.SH | 鹏欣资源 | ok | 33.30 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.38% < 6.00%; excess_return_120d -24.96% < 6.00%; drawdown_120d -49.08% < -28.00%; volatility_120d 64.16% > 42.00% |
| 001227.SZ | 兰州银行 | ok | 33.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.04% < 6.00%; excess_return_120d -12.62% < 6.00%; excess_return_240d -38.99% < 8.00% |
| 603077.SH | 和邦生物 | ok | 33.21 | close_below_ma200; stock_return_120d 3.10% < 6.00%; excess_return_120d -1.48% < 6.00%; excess_return_240d 7.63% < 8.00%; drawdown_120d -34.18% < -28.00%; volatility_120d 53.42% > 42.00% |
| 300353.SZ | 东土科技 | ok | 33.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; excess_return_120d 1.71% < 6.00%; excess_return_240d -21.38% < 8.00%; volatility_120d 57.49% > 42.00% |
| 002174.SZ | 游族网络 | ok | 33.15 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 1.23% < 6.00%; excess_return_120d -3.35% < 6.00%; excess_return_240d -19.04% < 8.00%; volatility_120d 45.91% > 42.00% |
| 000521.SZ | 长虹美菱 | ok | 33.12 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.23% < 6.00%; excess_return_120d -7.81% < 6.00%; excess_return_240d -35.64% < 8.00% |
| 000899.SZ | 赣能股份 | ok | 33.10 | close_below_ma200; excess_return_120d 3.64% < 6.00%; excess_return_240d -9.78% < 8.00%; drawdown_120d -35.19% < -28.00%; volatility_120d 60.98% > 42.00% |
| 603565.SH | 中谷物流 | ok | 33.08 | close_below_ma200; ma120_not_above_ma200; stock_return_120d 4.80% < 6.00%; excess_return_120d 0.22% < 6.00%; excess_return_240d -6.73% < 8.00% |
| 601816.SH | 京沪高铁 | ok | 33.01 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.71% < 6.00%; excess_return_120d -14.29% < 6.00%; excess_return_240d -37.36% < 8.00% |
| 000623.SZ | 吉林敖东 | ok | 32.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.94% < 6.00%; excess_return_120d -8.52% < 6.00%; excess_return_240d -8.76% < 8.00% |
| 300187.SZ | 永清环保 | ok | 32.94 | close_below_ma200; excess_return_120d 1.82% < 6.00%; excess_return_240d -21.35% < 8.00%; volatility_120d 51.82% > 42.00% |
| 600103.SH | 青山纸业 | ok | 32.86 | close_below_ma200; stock_return_120d -27.53% < 6.00%; excess_return_120d -32.11% < 6.00%; drawdown_120d -46.94% < -28.00%; volatility_120d 53.73% > 42.00% |
| 600699.SH | 均胜电子 | ok | 32.86 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.98% < 6.00%; excess_return_120d -31.56% < 6.00%; drawdown_120d -31.85% < -28.00%; volatility_120d 45.45% > 42.00% |
| 603966.SH | 法兰泰克 | ok | 32.85 | close_below_ma200; stock_return_120d 1.65% < 6.00%; excess_return_120d -2.32% < 6.00%; excess_return_240d 6.06% < 8.00%; volatility_120d 42.16% > 42.00% |
| 000553.SZ | 安道麦A | ok | 32.81 | close_below_ma200; ma120_not_above_ma200; excess_return_120d 2.54% < 6.00%; excess_return_240d -42.62% < 8.00%; volatility_120d 45.36% > 42.00% |
| 300006.SZ | 莱美药业 | ok | 32.72 | close_below_ma200; stock_return_120d -3.11% < 6.00%; excess_return_120d -7.69% < 6.00%; excess_return_240d 7.92% < 8.00%; volatility_120d 53.51% > 42.00% |
| 000520.SZ | 凤凰航运 | ok | 32.71 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -2.89% < 6.00%; excess_return_120d -7.47% < 6.00%; excess_return_240d -27.66% < 8.00%; volatility_120d 51.18% > 42.00% |
| 002327.SZ | 富安娜 | ok | 32.69 | close_below_ma200; ma120_not_above_ma200; stock_return_120d 1.50% < 6.00%; excess_return_120d -3.08% < 6.00%; excess_return_240d -29.84% < 8.00% |
| 000538.SZ | 云南白药 | ok | 32.69 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.69% < 6.00%; excess_return_120d -15.27% < 6.00%; excess_return_240d -28.74% < 8.00% |
| 601375.SH | 中原证券 | ok | 32.68 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -4.88% < 6.00%; excess_return_120d -9.46% < 6.00%; excess_return_240d -22.19% < 8.00% |
| 603222.SH | 济民健康 | ok | 32.67 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -4.93% < 6.00%; excess_return_120d -9.51% < 6.00%; volatility_120d 46.25% > 42.00% |
| 000828.SZ | 东莞控股 | ok | 32.67 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.76% < 6.00%; excess_return_120d -11.34% < 6.00%; excess_return_240d -27.94% < 8.00% |
| 003000.SZ | 劲仔食品 | ok | 32.66 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.35% < 6.00%; excess_return_120d -10.93% < 6.00%; excess_return_240d -38.22% < 8.00% |
| 300161.SZ | 华中数控 | ok | 32.61 | excess_return_120d 2.20% < 6.00%; excess_return_240d -2.33% < 8.00%; volatility_120d 52.97% > 42.00% |
| 002926.SZ | 华西证券 | ok | 32.61 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.97% < 6.00%; excess_return_120d -12.55% < 6.00%; excess_return_240d -27.41% < 8.00% |
| 000552.SZ | 甘肃能化 | ok | 32.45 | close_below_ma200; excess_return_120d 0.69% < 6.00%; excess_return_240d -19.05% < 8.00% |
| 300826.SZ | 测绘股份 | ok | 32.45 | ma120_not_above_ma200; stock_return_120d 2.20% < 6.00%; excess_return_120d -2.38% < 6.00%; excess_return_240d -21.35% < 8.00% |
| 002136.SZ | 安纳达 | ok | 32.42 | close_below_ma200; stock_return_120d 5.68% < 6.00%; excess_return_120d 1.10% < 6.00%; excess_return_240d -1.86% < 8.00%; volatility_120d 46.73% > 42.00% |
| 603886.SH | 元祖股份 | ok | 32.42 | ma60_not_above_ma120; stock_return_120d -4.26% < 6.00%; excess_return_120d -8.84% < 6.00%; excess_return_240d -19.27% < 8.00% |
| 002181.SZ | 粤传媒 | ok | 32.40 | close_below_ma200; excess_return_120d 1.68% < 6.00%; excess_return_240d 5.91% < 8.00%; drawdown_120d -57.71% < -28.00%; volatility_120d 81.11% > 42.00% |
| 001308.SZ | 康冠科技 | ok | 32.37 | close_below_ma200; ma120_not_above_ma200; stock_return_120d 0.79% < 6.00%; excess_return_120d -3.79% < 6.00%; excess_return_240d -26.78% < 8.00% |
| 601033.SH | 永兴股份 | ok | 32.31 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.17% < 6.00%; excess_return_120d -7.75% < 6.00%; excess_return_240d -28.67% < 8.00% |
| 600368.SH | 五洲交通 | ok | 32.29 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.85% < 6.00%; excess_return_120d -10.43% < 6.00%; excess_return_240d -36.76% < 8.00% |
| 600369.SH | 西南证券 | ok | 32.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.70% < 6.00%; excess_return_120d -11.28% < 6.00%; excess_return_240d -24.89% < 8.00% |
| 688698.SH | 伟创电气 | ok | 32.25 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.25% < 6.00%; excess_return_120d -43.83% < 6.00%; drawdown_120d -47.13% < -28.00%; volatility_120d 58.68% > 42.00% |
| 301069.SZ | 凯盛新材 | ok | 32.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.68% < 6.00%; excess_return_120d -29.26% < 6.00%; drawdown_120d -29.39% < -28.00%; volatility_120d 46.50% > 42.00% |
| 601928.SH | 凤凰传媒 | ok | 32.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.26% < 6.00%; excess_return_120d -13.84% < 6.00%; excess_return_240d -39.97% < 8.00% |
| 000028.SZ | 国药一致 | ok | 32.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -2.93% < 6.00%; excess_return_120d -7.51% < 6.00%; excess_return_240d -25.93% < 8.00% |
| 600008.SH | 首创环保 | ok | 32.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.12% < 6.00%; excess_return_120d -7.71% < 6.00%; excess_return_240d -27.16% < 8.00% |
| 688410.SH | 山外山 | ok | 32.15 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 4.81% < 6.00%; excess_return_120d 0.23% < 6.00%; excess_return_240d -12.14% < 8.00% |
| 301211.SZ | 亨迪药业 | ok | 32.15 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 3.21% < 6.00%; excess_return_120d -1.37% < 6.00%; excess_return_240d -19.85% < 8.00%; volatility_120d 48.91% > 42.00% |
| 600795.SH | 国电电力 | ok | 32.13 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -5.95% < 6.00%; excess_return_120d -10.53% < 6.00%; excess_return_240d -20.89% < 8.00% |
| 002299.SZ | 圣农发展 | ok | 32.11 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 2.33% < 6.00%; excess_return_120d -2.25% < 6.00%; excess_return_240d -6.67% < 8.00% |
| 600743.SH | 华远控股 | ok | 32.08 | close_below_ma200; excess_return_120d 2.42% < 6.00%; excess_return_240d -24.70% < 8.00%; drawdown_120d -39.38% < -28.00%; volatility_120d 56.19% > 42.00% |
| 600925.SH | 苏能股份 | ok | 32.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.32% < 6.00%; excess_return_120d -7.90% < 6.00%; excess_return_240d -36.08% < 8.00% |
| 603128.SH | 华贸物流 | ok | 32.06 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.97% < 6.00%; excess_return_120d -16.55% < 6.00%; excess_return_240d -32.72% < 8.00% |
| 002723.SZ | 小崧股份 | ok | 32.04 | close_below_ma200; stock_return_120d 5.79% < 6.00%; excess_return_120d 1.20% < 6.00%; excess_return_240d 0.64% < 8.00%; volatility_120d 56.96% > 42.00% |
| 002246.SZ | 北化股份 | ok | 32.00 | close_below_ma200; stock_return_120d 3.56% < 6.00%; excess_return_120d -1.02% < 6.00%; excess_return_240d 7.62% < 8.00%; drawdown_120d -33.01% < -28.00%; volatility_120d 53.90% > 42.00% |
| 600780.SH | 通宝能源 | ok | 31.99 | close_below_ma200; excess_return_120d 2.64% < 6.00%; excess_return_240d -23.03% < 8.00%; volatility_120d 45.19% > 42.00% |
| 000800.SZ | 一汽解放 | ok | 31.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.34% < 6.00%; excess_return_120d -10.92% < 6.00%; excess_return_240d -29.99% < 8.00% |
| 603190.SH | 亚通精工 | ok | 31.87 | ma60_not_above_ma120; stock_return_120d -3.93% < 6.00%; excess_return_120d -8.51% < 6.00%; excess_return_240d -9.61% < 8.00% |
| 000885.SZ | 城发环境 | ok | 31.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.43% < 6.00%; excess_return_120d -10.01% < 6.00%; excess_return_240d -27.58% < 8.00% |
| 600941.SH | 中国移动 | ok | 31.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.98% < 6.00%; excess_return_120d -15.56% < 6.00%; excess_return_240d -39.04% < 8.00% |
| 601901.SH | 方正证券 | ok | 31.74 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.06% < 6.00%; excess_return_120d -11.64% < 6.00%; excess_return_240d -28.40% < 8.00% |
| 000012.SZ | 南玻A | ok | 31.67 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 4.29% < 6.00%; excess_return_120d -0.29% < 6.00%; excess_return_240d -24.46% < 8.00%; volatility_120d 50.59% > 42.00% |
| 601668.SH | 中国建筑 | ok | 31.63 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.70% < 6.00%; excess_return_120d -16.28% < 6.00%; excess_return_240d -41.33% < 8.00% |
| 601878.SH | 浙商证券 | ok | 31.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.94% < 6.00%; excess_return_120d -13.52% < 6.00%; excess_return_240d -30.46% < 8.00% |
| 301397.SZ | 溯联股份 | ok | 31.59 | ma120_not_above_ma200; stock_return_120d 0.14% < 6.00%; excess_return_120d -4.44% < 6.00%; excess_return_240d 4.56% < 8.00%; volatility_120d 51.94% > 42.00% |
| 603895.SH | 天永智能 | ok | 31.55 | excess_return_120d 1.56% < 6.00%; excess_return_240d -0.76% < 8.00%; volatility_120d 53.56% > 42.00% |
| 603004.SH | 鼎龙科技 | ok | 31.53 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -1.20% < 6.00%; excess_return_120d -5.78% < 6.00%; excess_return_240d -15.54% < 8.00% |
| 603195.SH | 公牛集团 | ok | 31.52 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -1.41% < 6.00%; excess_return_120d -5.99% < 6.00%; excess_return_240d -37.46% < 8.00% |
| 601666.SH | 平煤股份 | ok | 31.50 | ma60_not_above_ma120; stock_return_120d 5.12% < 6.00%; excess_return_120d 0.54% < 6.00%; excess_return_240d -11.04% < 8.00%; volatility_120d 46.36% > 42.00% |
| 000900.SZ | 现代投资 | ok | 31.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.11% < 6.00%; excess_return_120d -10.69% < 6.00%; excess_return_240d -34.88% < 8.00% |
| 002394.SZ | 联发股份 | ok | 31.50 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -32.03% < 6.00%; excess_return_120d -36.61% < 6.00%; drawdown_120d -47.01% < -28.00%; volatility_120d 56.50% > 42.00% |
| 002818.SZ | 富森美 | ok | 31.49 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -0.93% < 6.00%; excess_return_120d -5.51% < 6.00%; excess_return_240d -30.95% < 8.00% |
| 301391.SZ | 卡莱特 | ok | 31.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.02% < 6.00%; excess_return_120d -38.60% < 6.00%; drawdown_120d -39.02% < -28.00%; volatility_120d 57.86% > 42.00% |
| 000513.SZ | 丽珠集团 | ok | 31.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.57% < 6.00%; excess_return_120d -10.15% < 6.00%; excess_return_240d -31.88% < 8.00% |
| 688171.SH | 纬德信息 | ok | 31.42 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.87% < 6.00%; excess_return_120d -21.45% < 6.00%; drawdown_120d -38.86% < -28.00%; volatility_120d 58.40% > 42.00% |
| 601098.SH | 中南传媒 | ok | 31.36 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.82% < 6.00%; excess_return_120d -12.40% < 6.00%; excess_return_240d -43.86% < 8.00% |
| 000728.SZ | 国元证券 | ok | 31.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.73% < 6.00%; excess_return_120d -13.31% < 6.00%; excess_return_240d -24.56% < 8.00% |
| 600283.SH | 钱江水利 | ok | 31.27 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.98% < 6.00%; excess_return_120d -12.56% < 6.00%; excess_return_240d -37.15% < 8.00% |
| 603855.SH | 华荣股份 | ok | 31.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.98% < 6.00%; excess_return_120d -8.56% < 6.00%; excess_return_240d -33.78% < 8.00% |
| 001387.SZ | 雪祺电气 | ok | 31.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -2.50% < 6.00%; excess_return_120d -7.08% < 6.00%; excess_return_240d -28.16% < 8.00% |
| 600521.SH | 华海药业 | ok | 31.15 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -0.42% < 6.00%; excess_return_120d -5.00% < 6.00%; excess_return_240d -44.22% < 8.00% |
| 002061.SZ | 浙江交科 | ok | 31.14 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.24% < 6.00%; excess_return_120d -11.82% < 6.00%; excess_return_240d -29.98% < 8.00% |
| 688685.SH | 迈信林 | ok | 31.12 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.94% < 6.00%; excess_return_120d -8.52% < 6.00%; excess_return_240d -20.56% < 8.00%; volatility_120d 62.81% > 42.00% |
| 603368.SH | 柳药集团 | ok | 31.10 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.97% < 6.00%; excess_return_120d -13.55% < 6.00%; excess_return_240d -26.26% < 8.00% |
| 601919.SH | 中远海控 | ok | 31.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.16% < 6.00%; excess_return_120d -9.74% < 6.00%; excess_return_240d -23.47% < 8.00% |
| 603310.SH | 巍华新材 | ok | 31.06 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.36% < 6.00%; excess_return_120d -9.94% < 6.00%; excess_return_240d -36.90% < 8.00% |
| 603983.SH | 丸美生物 | ok | 31.05 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.12% < 6.00%; excess_return_120d -10.70% < 6.00%; excess_return_240d -46.74% < 8.00% |
| 603066.SH | 音飞储存 | ok | 31.04 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -0.90% < 6.00%; excess_return_120d -5.48% < 6.00%; excess_return_240d -32.93% < 8.00% |
| 601088.SH | 中国神华 | ok | 31.04 | close_below_ma200; stock_return_120d 3.48% < 6.00%; excess_return_120d -1.10% < 6.00%; excess_return_240d -9.55% < 8.00% |
| 002500.SZ | 山西证券 | ok | 31.04 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.97% < 6.00%; excess_return_120d -13.55% < 6.00%; excess_return_240d -28.18% < 8.00% |
| 300528.SZ | 幸福蓝海 | ok | 31.03 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.84% < 6.00%; excess_return_120d -36.42% < 6.00%; drawdown_120d -51.90% < -28.00%; volatility_120d 66.71% > 42.00% |
| 600230.SH | 沧州大化 | ok | 30.95 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.37% < 6.00%; excess_return_120d -13.95% < 6.00%; drawdown_120d -49.23% < -28.00%; volatility_120d 66.56% > 42.00% |
| 000166.SZ | 申万宏源 | ok | 30.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.57% < 6.00%; excess_return_120d -16.16% < 6.00%; excess_return_240d -27.50% < 8.00% |
| 601456.SH | 国联民生 | ok | 30.94 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.60% < 6.00%; excess_return_120d -16.18% < 6.00%; excess_return_240d -34.10% < 8.00% |
| 600737.SH | 中粮糖业 | ok | 30.91 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.58% < 6.00%; excess_return_120d -34.16% < 6.00%; drawdown_120d -35.67% < -28.00%; volatility_120d 47.53% > 42.00% |
| 601107.SH | 四川成渝 | ok | 30.85 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.37% < 6.00%; excess_return_120d -8.96% < 6.00%; excess_return_240d -25.97% < 8.00% |
| 601688.SH | 华泰证券 | ok | 30.84 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.67% < 6.00%; excess_return_120d -14.25% < 6.00%; excess_return_240d -0.57% < 8.00% |
| 600298.SH | 安琪酵母 | ok | 30.84 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.09% < 6.00%; excess_return_120d -15.67% < 6.00%; excess_return_240d -8.26% < 8.00% |
| 601827.SH | 三峰环境 | ok | 30.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.78% < 6.00%; excess_return_120d -10.36% < 6.00%; excess_return_240d -24.46% < 8.00% |
| 300154.SZ | 瑞凌股份 | ok | 30.80 | stock_return_120d 1.04% < 6.00%; excess_return_120d -3.54% < 6.00%; excess_return_240d -9.41% < 8.00%; volatility_120d 49.84% > 42.00% |
| 000423.SZ | 东阿阿胶 | ok | 30.79 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.23% < 6.00%; excess_return_120d -4.81% < 6.00%; excess_return_240d -23.44% < 8.00% |
| 601326.SH | 秦港股份 | ok | 30.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -4.58% < 6.00%; excess_return_120d -9.16% < 6.00%; excess_return_240d -18.48% < 8.00% |
| 603049.SH | 中策橡胶 | ok | 30.73 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.31% < 6.00%; excess_return_120d -14.89% < 6.00%; excess_return_240d -8.86% < 8.00% |
| 000567.SZ | 海德股份 | ok | 30.68 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -3.58% < 6.00%; excess_return_120d -8.16% < 6.00%; excess_return_240d -22.22% < 8.00% |
| 000566.SZ | 海南海药 | ok | 30.66 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.07% < 6.00%; excess_return_120d -14.65% < 6.00%; excess_return_240d -16.37% < 8.00%; volatility_120d 51.80% > 42.00% |
| 301118.SZ | 恒光股份 | ok | 30.62 | close_below_ma200; excess_return_120d 1.72% < 6.00%; excess_return_240d -7.60% < 8.00%; drawdown_120d -32.44% < -28.00%; volatility_120d 50.92% > 42.00% |
| 601825.SH | 沪农商行 | ok | 30.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.03% < 6.00%; excess_return_120d -18.61% < 6.00%; excess_return_240d -39.25% < 8.00% |
| 600020.SH | 中原高速 | ok | 30.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.80% < 6.00%; excess_return_120d -15.38% < 6.00%; excess_return_240d -40.42% < 8.00% |
| 003816.SZ | 中国广核 | ok | 30.56 | close_below_ma200; stock_return_120d 3.46% < 6.00%; excess_return_120d -1.12% < 6.00%; excess_return_240d -16.53% < 8.00% |
| 300547.SZ | 川环科技 | ok | 30.53 | ma120_not_above_ma200; stock_return_120d -5.17% < 6.00%; excess_return_120d -9.75% < 6.00%; excess_return_240d 1.45% < 8.00%; volatility_120d 58.78% > 42.00% |
| 000650.SZ | 仁和药业 | ok | 30.53 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -4.25% < 6.00%; excess_return_120d -8.83% < 6.00%; excess_return_240d -22.91% < 8.00% |
| 002003.SZ | 伟星股份 | ok | 30.48 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.55% < 6.00%; excess_return_120d -17.13% < 6.00%; excess_return_240d -33.56% < 8.00% |
| 603858.SH | 步长制药 | ok | 30.48 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -0.58% < 6.00%; excess_return_120d -5.16% < 6.00%; excess_return_240d -24.81% < 8.00% |
| 000589.SZ | 贵州轮胎 | ok | 30.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.77% < 6.00%; excess_return_120d -17.35% < 6.00%; excess_return_240d -19.98% < 8.00% |
| 601187.SH | 厦门银行 | ok | 30.44 | close_below_ma200; stock_return_120d -3.60% < 6.00%; excess_return_120d -8.18% < 6.00%; excess_return_240d -22.93% < 8.00% |
| 603693.SH | 江苏新能 | ok | 30.43 | close_below_ma200; excess_return_120d 2.42% < 6.00%; excess_return_240d -36.21% < 8.00%; drawdown_120d -38.03% < -28.00%; volatility_120d 55.66% > 42.00% |
| 003013.SZ | 地铁设计 | ok | 30.41 | close_below_ma200; ma120_not_above_ma200; stock_return_120d 1.88% < 6.00%; excess_return_120d -2.70% < 6.00%; excess_return_240d -22.01% < 8.00% |
| 002584.SZ | 西陇科学 | ok | 30.35 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 1.63% < 6.00%; excess_return_120d -2.95% < 6.00%; excess_return_240d -23.80% < 8.00%; volatility_120d 51.23% > 42.00% |
| 300738.SZ | 奥飞数据 | ok | 30.30 | close_below_ma200; excess_return_120d 2.59% < 6.00%; excess_return_240d -27.99% < 8.00%; drawdown_120d -32.83% < -28.00%; volatility_120d 70.08% > 42.00% |
| 300972.SZ | 万辰集团 | ok | 30.29 | ma60_not_above_ma120; stock_return_120d -0.40% < 6.00%; excess_return_120d -4.98% < 6.00%; excess_return_240d 0.76% < 8.00%; volatility_120d 47.16% > 42.00% |
| 002746.SZ | 仙坛股份 | ok | 30.25 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.30% < 6.00%; excess_return_120d -10.88% < 6.00%; excess_return_240d -22.71% < 8.00% |
| 603338.SH | 浙江鼎力 | ok | 30.21 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -4.51% < 6.00%; excess_return_120d -9.09% < 6.00%; excess_return_240d -3.71% < 8.00% |
| 601788.SH | 光大证券 | ok | 30.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.14% < 6.00%; excess_return_120d -16.72% < 6.00%; excess_return_240d -34.57% < 8.00% |
| 000430.SZ | 张家界 | ok | 30.20 | close_below_ma200; stock_return_120d 0.42% < 6.00%; excess_return_120d -3.95% < 6.00%; excess_return_240d -20.88% < 8.00% |
| 002641.SZ | 公元股份 | ok | 30.18 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.37% < 6.00%; excess_return_120d -12.95% < 6.00%; excess_return_240d -26.39% < 8.00% |
| 600066.SH | 宇通客车 | ok | 30.17 | close_below_ma200; stock_return_120d -4.43% < 6.00%; excess_return_120d -9.01% < 6.00%; excess_return_240d 2.28% < 8.00% |
| 601598.SH | 中国外运 | ok | 30.16 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.35% < 6.00%; excess_return_120d -10.93% < 6.00%; excess_return_240d -4.18% < 8.00% |
| 301303.SZ | 真兰仪表 | ok | 30.12 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 4.17% < 6.00%; excess_return_120d -0.41% < 6.00%; excess_return_240d -17.41% < 8.00%; volatility_120d 48.88% > 42.00% |
| 600572.SH | 康恩贝 | ok | 30.12 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -4.18% < 6.00%; excess_return_120d -8.76% < 6.00%; excess_return_240d -25.27% < 8.00% |
| 600211.SH | 西藏药业 | ok | 30.10 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.37% < 6.00%; excess_return_120d -10.95% < 6.00%; excess_return_240d -10.01% < 8.00% |
| 300864.SZ | 南大环境 | ok | 30.04 | close_below_ma200; stock_return_120d 4.93% < 6.00%; excess_return_120d 0.35% < 6.00%; excess_return_240d -19.14% < 8.00% |
| 601368.SH | 绿城水务 | ok | 30.03 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.55% < 6.00%; excess_return_120d -8.13% < 6.00%; excess_return_240d -24.65% < 8.00% |
| 000755.SZ | 山西高速 | ok | 30.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.53% < 6.00%; excess_return_120d -8.11% < 6.00%; excess_return_240d -24.62% < 8.00% |
| 000750.SZ | 国海证券 | ok | 30.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.38% < 6.00%; excess_return_120d -14.96% < 6.00%; excess_return_240d -28.59% < 8.00% |
| 002867.SZ | 周大生 | ok | 30.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -0.33% < 6.00%; excess_return_120d -4.91% < 6.00%; excess_return_240d -27.57% < 8.00% |
| 600153.SH | 建发股份 | ok | 29.97 | close_below_ma200; ma120_not_above_ma200; stock_return_120d 0.35% < 6.00%; excess_return_120d -4.23% < 6.00%; excess_return_240d -33.72% < 8.00% |
| 600958.SH | 东方证券 | ok | 29.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.32% < 6.00%; excess_return_120d -19.04% < 6.00%; excess_return_240d -22.35% < 8.00% |
| 002403.SZ | 爱仕达 | ok | 29.94 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.95% < 6.00%; excess_return_120d -11.53% < 6.00%; excess_return_240d -36.53% < 8.00% |
| 301628.SZ | 强达电路 | ok | 29.94 | close_below_ma200; excess_return_120d 2.04% < 6.00%; excess_return_240d -17.13% < 8.00%; drawdown_120d -36.19% < -28.00%; volatility_120d 61.36% > 42.00% |
| 000029.SZ | 深深房A | ok | 29.93 | close_below_ma200; ma120_not_above_ma200; stock_return_120d 4.34% < 6.00%; excess_return_120d -0.24% < 6.00%; excess_return_240d 3.48% < 8.00%; volatility_120d 56.00% > 42.00% |
| 000989.SZ | 九芝堂 | ok | 29.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -0.15% < 6.00%; excess_return_120d -4.73% < 6.00%; excess_return_240d -34.32% < 8.00% |
| 300692.SZ | 中赋科技 | ok | 29.90 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -1.55% < 6.00%; excess_return_120d -6.13% < 6.00%; excess_return_240d 1.95% < 8.00%; volatility_120d 44.00% > 42.00% |
| 601528.SH | 瑞丰银行 | ok | 29.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.66% < 6.00%; excess_return_120d -20.25% < 6.00%; excess_return_240d -40.58% < 8.00% |
| 600905.SH | 三峡能源 | ok | 29.77 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.09% < 6.00%; excess_return_120d -11.67% < 6.00%; excess_return_240d -31.96% < 8.00% |
| 000925.SZ | 众合科技 | ok | 29.74 | stock_return_120d 1.45% < 6.00%; excess_return_120d -3.13% < 6.00%; excess_return_240d -2.94% < 8.00%; volatility_120d 61.71% > 42.00% |
| 601963.SH | 重庆银行 | ok | 29.71 | close_below_ma200; stock_return_120d -3.96% < 6.00%; excess_return_120d -8.54% < 6.00%; excess_return_240d -29.11% < 8.00% |
| 600406.SH | 国电南瑞 | ok | 29.70 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 5.23% < 6.00%; excess_return_120d 0.65% < 6.00%; excess_return_240d -13.24% < 8.00% |
| 300538.SZ | 同益股份 | ok | 29.70 | close_below_ma200; ma120_not_above_ma200; stock_return_120d 1.56% < 6.00%; excess_return_120d -3.02% < 6.00%; excess_return_240d -17.74% < 8.00%; volatility_120d 42.11% > 42.00% |
| 603111.SH | 康尼机电 | ok | 29.69 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.58% < 6.00%; excess_return_120d -12.16% < 6.00%; excess_return_240d -21.29% < 8.00% |
| 002652.SZ | 扬子新材 | ok | 29.66 | close_below_ma200; stock_return_120d 4.56% < 6.00%; excess_return_120d -0.02% < 6.00%; excess_return_240d 4.05% < 8.00%; drawdown_120d -39.00% < -28.00%; volatility_120d 58.58% > 42.00% |
| 300860.SZ | 锋尚文化 | ok | 29.66 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -0.94% < 6.00%; excess_return_120d -5.52% < 6.00%; excess_return_240d -26.04% < 8.00% |
| 600380.SH | 健康元 | ok | 29.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.53% < 6.00%; excess_return_120d -14.11% < 6.00%; excess_return_240d -27.58% < 8.00% |
| 000550.SZ | 江铃汽车 | ok | 29.57 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.82% < 6.00%; excess_return_120d -13.40% < 6.00%; excess_return_240d -35.32% < 8.00% |
| 600033.SH | 福建高速 | ok | 29.57 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.95% < 6.00%; excess_return_120d -21.53% < 6.00%; excess_return_240d -22.82% < 8.00% |
| 301571.SZ | 国科天成 | ok | 29.55 | stock_return_120d 2.29% < 6.00%; excess_return_120d -2.29% < 6.00%; excess_return_240d 1.08% < 8.00%; volatility_120d 51.17% > 42.00% |
| 000883.SZ | 湖北能源 | ok | 29.53 | close_below_ma200; stock_return_120d -0.66% < 6.00%; excess_return_120d -5.24% < 6.00%; excess_return_240d -23.27% < 8.00% |
| 002708.SZ | 光洋股份 | ok | 29.50 | close_below_ma200; stock_return_120d -1.96% < 6.00%; excess_return_120d -6.54% < 6.00%; excess_return_240d 2.90% < 8.00%; volatility_120d 50.15% > 42.00% |
| 688657.SH | 浩辰软件 | ok | 29.49 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -2.61% < 6.00%; excess_return_120d -7.19% < 6.00%; excess_return_240d 1.12% < 8.00% |
| 603235.SH | 天新药业 | ok | 29.49 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.36% < 6.00%; excess_return_120d -15.94% < 6.00%; excess_return_240d -36.52% < 8.00% |
| 301168.SZ | 通灵股份 | ok | 29.47 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -8.31% < 6.00%; excess_return_120d -12.89% < 6.00%; excess_return_240d -3.44% < 8.00%; volatility_120d 45.46% > 42.00% |
| 688505.SH | 复旦张江 | ok | 29.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.30% < 6.00%; excess_return_120d -9.88% < 6.00%; excess_return_240d -33.08% < 8.00% |
| 000733.SZ | 振华科技 | ok | 29.45 | ma60_not_above_ma120; stock_return_120d -0.48% < 6.00%; excess_return_120d -5.06% < 6.00%; excess_return_240d -12.82% < 8.00%; volatility_120d 56.38% > 42.00% |
| 300752.SZ | 隆利科技 | ok | 29.44 | close_below_ma200; ma120_not_above_ma200; stock_return_120d 2.97% < 6.00%; excess_return_120d -1.61% < 6.00%; excess_return_240d -35.95% < 8.00%; volatility_120d 55.88% > 42.00% |
| 600717.SH | 天津港 | ok | 29.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.78% < 6.00%; excess_return_120d -13.13% < 6.00%; excess_return_240d -31.12% < 8.00% |
| 002737.SZ | 葵花药业 | ok | 29.38 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.68% < 6.00%; excess_return_120d -18.26% < 6.00%; excess_return_240d -37.55% < 8.00% |
| 601298.SH | 青岛港 | ok | 29.36 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.00% < 6.00%; excess_return_120d -7.58% < 6.00%; excess_return_240d -26.07% < 8.00% |
| 300307.SZ | 慈星股份 | ok | 29.36 | ma120_not_above_ma200; stock_return_120d 1.84% < 6.00%; excess_return_120d -2.74% < 6.00%; excess_return_240d -30.44% < 8.00% |
| 601137.SH | 博威合金 | ok | 29.30 | ma120_not_above_ma200; stock_return_120d 2.54% < 6.00%; excess_return_120d -2.04% < 6.00%; excess_return_240d 0.01% < 8.00%; volatility_120d 52.58% > 42.00% |
| 301517.SZ | 陕西华达 | ok | 29.30 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -28.27% < 6.00%; excess_return_120d -32.85% < 6.00%; excess_return_240d 7.49% < 8.00%; drawdown_120d -52.07% < -28.00%; volatility_120d 59.82% > 42.00% |
| 603609.SH | 禾丰股份 | ok | 29.29 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.46% < 6.00%; excess_return_120d -13.04% < 6.00%; excess_return_240d -44.74% < 8.00% |
| 002352.SZ | 顺丰控股 | ok | 29.29 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.12% < 6.00%; excess_return_120d -17.70% < 6.00%; excess_return_240d -50.15% < 8.00% |
| 603276.SH | 恒兴新材 | ok | 29.29 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -1.82% < 6.00%; excess_return_120d -6.40% < 6.00%; excess_return_240d -23.10% < 8.00% |
| 600600.SH | 青岛啤酒 | ok | 29.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.05% < 6.00%; excess_return_120d -15.63% < 6.00%; excess_return_240d -41.96% < 8.00% |
| 688047.SH | 龙芯中科 | ok | 29.25 | close_below_ma200; ma60_not_above_ma120; excess_return_120d 1.49% < 6.00%; excess_return_240d -17.06% < 8.00%; drawdown_120d -30.99% < -28.00%; volatility_120d 67.00% > 42.00% |
| 600660.SH | 福耀玻璃 | ok | 29.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.40% < 6.00%; excess_return_120d -19.98% < 6.00%; excess_return_240d -24.27% < 8.00% |
| 600757.SH | 长江传媒 | ok | 29.18 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.39% < 6.00%; excess_return_120d -14.97% < 6.00%; excess_return_240d -40.09% < 8.00% |
| 000830.SZ | 鲁西化工 | ok | 29.16 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.98% < 6.00%; excess_return_120d -24.56% < 6.00%; excess_return_240d 7.71% < 8.00%; drawdown_120d -39.35% < -28.00%; volatility_120d 56.29% > 42.00% |
| 600755.SH | 厦门国贸 | ok | 29.15 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.65% < 6.00%; excess_return_120d -22.23% < 6.00%; excess_return_240d -24.79% < 8.00% |
| 002907.SZ | 华森制药 | ok | 29.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.97% < 6.00%; excess_return_120d -11.55% < 6.00%; excess_return_240d -38.55% < 8.00% |
| 600785.SH | 新华百货 | ok | 29.12 | close_below_ma200; ma60_not_above_ma120; excess_return_120d 2.22% < 6.00%; excess_return_240d -0.39% < 8.00%; drawdown_120d -48.07% < -28.00%; volatility_120d 59.00% > 42.00% |
| 603233.SH | 大参林 | ok | 29.09 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 0.41% < 6.00%; excess_return_120d -4.17% < 6.00%; excess_return_240d -15.25% < 8.00% |
| 600409.SH | 三友化工 | ok | 29.08 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 1.46% < 6.00%; excess_return_120d -3.12% < 6.00%; excess_return_240d 4.91% < 8.00%; drawdown_120d -34.00% < -28.00%; volatility_120d 54.15% > 42.00% |
| 688576.SH | 西山科技 | ok | 29.07 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 5.53% < 6.00%; excess_return_120d 0.95% < 6.00%; excess_return_240d -17.94% < 8.00%; volatility_120d 47.73% > 42.00% |
| 600269.SH | 赣粤高速 | ok | 29.04 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.96% < 6.00%; excess_return_120d -21.54% < 6.00%; excess_return_240d -36.75% < 8.00% |
| 603967.SH | 中创物流 | ok | 28.99 | close_below_ma200; stock_return_120d -10.86% < 6.00%; excess_return_120d -15.44% < 6.00%; excess_return_240d -12.33% < 8.00% |
| 300919.SZ | 中伟新材 | ok | 28.99 | close_below_ma200; stock_return_120d -8.69% < 6.00%; excess_return_120d -13.27% < 6.00%; excess_return_240d 7.60% < 8.00%; drawdown_120d -36.20% < -28.00%; volatility_120d 54.94% > 42.00% |
| 000837.SZ | 秦川机床 | ok | 28.98 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.39% < 6.00%; excess_return_120d -12.97% < 6.00%; excess_return_240d -19.98% < 8.00% |
| 688659.SH | 元琛科技 | ok | 28.93 | close_below_ma200; stock_return_120d 4.97% < 6.00%; excess_return_120d 0.39% < 6.00%; excess_return_240d -8.75% < 8.00% |
| 600391.SH | 航发科技 | ok | 28.88 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.25% < 6.00%; excess_return_120d -10.83% < 6.00%; excess_return_240d 4.83% < 8.00%; drawdown_120d -40.35% < -28.00%; volatility_120d 70.04% > 42.00% |
| 600305.SH | 恒顺醋业 | ok | 28.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.62% < 6.00%; excess_return_120d -19.20% < 6.00%; excess_return_240d -32.53% < 8.00% |
| 601377.SH | 兴业证券 | ok | 28.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.31% < 6.00%; excess_return_120d -20.89% < 6.00%; excess_return_240d -19.46% < 8.00% |
| 300024.SZ | 机器人 | ok | 28.85 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.38% < 6.00%; excess_return_120d -10.96% < 6.00%; excess_return_240d -19.36% < 8.00%; volatility_120d 53.28% > 42.00% |
| 300580.SZ | 贝斯特 | ok | 28.84 | ma120_not_above_ma200; stock_return_120d -1.91% < 6.00%; excess_return_120d -6.49% < 6.00%; excess_return_240d -12.27% < 8.00%; volatility_120d 54.41% > 42.00% |
| 600827.SH | 百联股份 | ok | 28.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.13% < 6.00%; excess_return_120d -17.71% < 6.00%; excess_return_240d -33.49% < 8.00% |
| 002675.SZ | 东诚药业 | ok | 28.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.34% < 6.00%; excess_return_120d -9.92% < 6.00%; excess_return_240d -30.55% < 8.00% |
| 601555.SH | 东吴证券 | ok | 28.77 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.61% < 6.00%; excess_return_120d -14.34% < 6.00%; excess_return_240d -29.49% < 8.00% |
| 600694.SH | 大商股份 | ok | 28.76 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.57% < 6.00%; excess_return_120d -11.15% < 6.00%; excess_return_240d -33.32% < 8.00% |
| 301149.SZ | 隆华新材 | ok | 28.76 | close_below_ma200; stock_return_120d 5.36% < 6.00%; excess_return_120d 0.78% < 6.00%; excess_return_240d -24.29% < 8.00%; volatility_120d 50.84% > 42.00% |
| 000682.SZ | 东方电子 | ok | 28.75 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 4.30% < 6.00%; excess_return_120d -0.28% < 6.00%; excess_return_240d -0.98% < 8.00%; volatility_120d 44.20% > 42.00% |
| 600116.SH | 三峡水利 | ok | 28.74 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.26% < 6.00%; excess_return_120d -11.84% < 6.00%; excess_return_240d -33.48% < 8.00% |
| 688458.SH | 美芯晟 | ok | 28.74 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 1.51% < 6.00%; excess_return_120d -3.07% < 6.00%; excess_return_240d -33.29% < 8.00%; volatility_120d 56.63% > 42.00% |
| 603161.SH | 科华控股 | ok | 28.71 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 1.97% < 6.00%; excess_return_120d -2.61% < 6.00%; excess_return_240d -11.98% < 8.00% |
| 601236.SH | 红塔证券 | ok | 28.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.83% < 6.00%; excess_return_120d -17.41% < 6.00%; excess_return_240d -35.84% < 8.00% |
| 000999.SZ | 华润三九 | ok | 28.66 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.88% < 6.00%; excess_return_120d -17.46% < 6.00%; excess_return_240d -40.35% < 8.00% |
| 601163.SH | 三角轮胎 | ok | 28.65 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.48% < 6.00%; excess_return_120d -9.06% < 6.00%; excess_return_240d -20.66% < 8.00% |
| 001298.SZ | 好上好 | ok | 28.62 | close_below_ma200; ma120_not_above_ma200; stock_return_120d 2.51% < 6.00%; excess_return_120d -2.07% < 6.00%; excess_return_240d -28.67% < 8.00% |
| 603666.SH | 亿嘉和 | ok | 28.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -2.32% < 6.00%; excess_return_120d -6.90% < 6.00%; excess_return_240d -33.40% < 8.00% |
| 300765.SZ | 新诺威 | ok | 28.60 | ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 1.83% < 6.00%; excess_return_120d -2.75% < 6.00%; excess_return_240d -48.13% < 8.00%; volatility_120d 66.19% > 42.00% |
| 600639.SH | 浦东金桥 | ok | 28.58 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.89% < 6.00%; excess_return_120d -12.47% < 6.00%; excess_return_240d -29.57% < 8.00% |
| 600420.SH | 国药现代 | ok | 28.57 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.19% < 6.00%; excess_return_120d -13.77% < 6.00%; excess_return_240d -34.49% < 8.00% |
| 601921.SH | 浙版传媒 | ok | 28.51 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.24% < 6.00%; excess_return_120d -11.82% < 6.00%; excess_return_240d -29.78% < 8.00% |
| 688538.SH | 和辉光电 | ok | 28.51 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.65% < 6.00%; excess_return_120d -16.23% < 6.00%; excess_return_240d -21.94% < 8.00% |
| 002557.SZ | 洽洽食品 | ok | 28.49 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -2.51% < 6.00%; excess_return_120d -7.09% < 6.00%; excess_return_240d -23.99% < 8.00% |
| 002865.SZ | 钧达股份 | ok | 28.49 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 0.49% < 6.00%; excess_return_120d -4.09% < 6.00%; excess_return_240d 7.46% < 8.00%; drawdown_120d -52.97% < -28.00%; volatility_120d 72.66% > 42.00% |
| 688029.SH | 南微医学 | ok | 28.48 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.95% < 6.00%; excess_return_120d -10.53% < 6.00%; excess_return_240d -12.45% < 8.00% |
| 600566.SH | 济川药业 | ok | 28.46 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.05% < 6.00%; excess_return_120d -9.63% < 6.00%; excess_return_240d -25.31% < 8.00% |
| 603917.SH | 合力科技 | ok | 28.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.43% < 6.00%; excess_return_120d -14.01% < 6.00%; excess_return_240d -25.36% < 8.00% |
| 603948.SH | 建业股份 | ok | 28.45 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -2.17% < 6.00%; excess_return_120d -6.75% < 6.00%; excess_return_240d -1.64% < 8.00%; volatility_120d 45.20% > 42.00% |
| 688016.SH | 心脉医疗 | ok | 28.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 2.28% < 6.00%; excess_return_120d -2.30% < 6.00%; excess_return_240d -18.72% < 8.00% |
| 300121.SZ | 阳谷华泰 | ok | 28.41 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 2.70% < 6.00%; excess_return_120d -1.88% < 6.00%; excess_return_240d -34.96% < 8.00%; volatility_120d 60.83% > 42.00% |
| 688475.SH | 萤石网络 | ok | 28.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.45% < 6.00%; excess_return_120d -13.03% < 6.00%; excess_return_240d -34.58% < 8.00% |
| 603766.SH | 隆鑫通用 | ok | 28.37 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.26% < 6.00%; excess_return_120d -16.84% < 6.00%; excess_return_240d -13.28% < 8.00% |
| 300921.SZ | 南凌科技 | ok | 28.36 | close_below_ma200; stock_return_120d 5.84% < 6.00%; excess_return_120d 1.26% < 6.00%; excess_return_240d -29.92% < 8.00%; drawdown_120d -29.63% < -28.00%; volatility_120d 61.80% > 42.00% |
| 001213.SZ | 中铁特货 | ok | 28.33 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.08% < 6.00%; excess_return_120d -17.66% < 6.00%; excess_return_240d -34.82% < 8.00% |
| 002603.SZ | 以岭药业 | ok | 28.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -4.65% < 6.00%; excess_return_120d -9.23% < 6.00%; excess_return_240d -7.59% < 8.00% |
| 003025.SZ | 思进智能 | ok | 28.28 | stock_return_120d 1.55% < 6.00%; excess_return_120d -3.03% < 6.00%; excess_return_240d -13.48% < 8.00% |
| 000981.SZ | 山子高科 | ok | 28.28 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -32.69% < 6.00%; excess_return_120d -37.27% < 6.00%; drawdown_120d -50.62% < -28.00%; volatility_120d 54.68% > 42.00% |
| 300628.SZ | 亿联网络 | ok | 28.27 | close_below_ma200; stock_return_120d -1.83% < 6.00%; excess_return_120d -6.41% < 6.00%; excess_return_240d -19.29% < 8.00% |
| 600576.SH | 祥源文旅 | ok | 28.27 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -1.76% < 6.00%; excess_return_120d -6.34% < 6.00%; excess_return_240d -43.80% < 8.00% |
| 688459.SH | 哈铁科技 | ok | 28.22 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.33% < 6.00%; excess_return_120d -17.91% < 6.00%; excess_return_240d -33.78% < 8.00% |
| 300908.SZ | 仲景食品 | ok | 28.22 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.22% < 6.00%; excess_return_120d -14.80% < 6.00%; excess_return_240d -37.72% < 8.00% |
| 300397.SZ | 天和防务 | ok | 28.21 | ma60_not_above_ma120; stock_return_120d -6.34% < 6.00%; excess_return_120d -10.92% < 6.00%; excess_return_240d -21.02% < 8.00%; volatility_120d 47.61% > 42.00% |
| 000037.SZ | 深南电A | ok | 28.19 | close_below_ma200; excess_return_120d 1.63% < 6.00%; excess_return_240d -37.65% < 8.00%; drawdown_120d -33.42% < -28.00%; volatility_120d 60.54% > 42.00% |
| 300890.SZ | 翔丰华 | ok | 28.16 | close_below_ma200; stock_return_120d 5.76% < 6.00%; excess_return_120d 1.18% < 6.00%; excess_return_240d -19.41% < 8.00%; drawdown_120d -29.70% < -28.00%; volatility_120d 49.91% > 42.00% |
| 601083.SH | 锦江航运 | ok | 28.16 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 1.44% < 6.00%; excess_return_120d -3.14% < 6.00%; excess_return_240d -20.89% < 8.00% |
| 601018.SH | 宁波港 | ok | 28.11 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.93% < 6.00%; excess_return_120d -10.51% < 6.00%; excess_return_240d -28.34% < 8.00% |
| 688626.SH | 翔宇医疗 | ok | 28.03 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.17% < 6.00%; excess_return_120d -16.75% < 6.00%; excess_return_240d 4.97% < 8.00%; drawdown_120d -44.13% < -28.00%; volatility_120d 55.42% > 42.00% |
| 002673.SZ | 西部证券 | ok | 28.03 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.10% < 6.00%; excess_return_120d -18.68% < 6.00%; excess_return_240d -34.20% < 8.00% |
| 601881.SH | 中国银河 | ok | 27.98 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.99% < 6.00%; excess_return_120d -18.58% < 6.00%; excess_return_240d -41.19% < 8.00% |
| 603055.SH | 台华新材 | ok | 27.97 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.86% < 6.00%; excess_return_120d -9.44% < 6.00%; excess_return_240d -24.92% < 8.00% |
| 603733.SH | 仙鹤股份 | ok | 27.95 | stock_return_120d -0.72% < 6.00%; excess_return_120d -5.30% < 6.00%; excess_return_240d -2.76% < 8.00%; volatility_120d 44.87% > 42.00% |
| 002157.SZ | 正邦科技 | ok | 27.92 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.79% < 6.00%; excess_return_120d -11.37% < 6.00%; excess_return_240d -13.24% < 8.00% |
| 002262.SZ | 恩华药业 | ok | 27.88 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.82% < 6.00%; excess_return_120d -18.40% < 6.00%; excess_return_240d -22.78% < 8.00% |
| 002367.SZ | 康力电梯 | ok | 27.86 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.41% < 6.00%; excess_return_120d -18.99% < 6.00%; excess_return_240d -24.38% < 8.00% |
| 300067.SZ | 安诺其 | ok | 27.83 | close_below_ma200; excess_return_120d 0.21% < 6.00%; excess_return_240d -32.92% < 8.00%; drawdown_120d -36.43% < -28.00%; volatility_120d 78.37% > 42.00% |
| 002387.SZ | 维信诺 | ok | 27.83 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.92% < 6.00%; excess_return_120d -10.50% < 6.00%; excess_return_240d -39.37% < 8.00% |
| 301510.SZ | 固高科技 | ok | 27.83 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.49% < 6.00%; excess_return_120d -12.07% < 6.00%; excess_return_240d -3.01% < 8.00%; volatility_120d 50.07% > 42.00% |
| 605128.SH | 上海沿浦 | ok | 27.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -4.51% < 6.00%; excess_return_120d -9.09% < 6.00%; excess_return_240d -7.02% < 8.00% |
| 002952.SZ | 亚世光电 | ok | 27.80 | close_below_ma200; excess_return_120d 1.55% < 6.00%; excess_return_240d -24.44% < 8.00%; drawdown_120d -38.29% < -28.00%; volatility_120d 60.12% > 42.00% |
| 600582.SH | 天地科技 | ok | 27.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.12% < 6.00%; excess_return_120d -16.70% < 6.00%; excess_return_240d -37.59% < 8.00% |
| 001299.SZ | 美能能源 | ok | 27.77 | stock_return_120d -5.65% < 6.00%; excess_return_120d -10.23% < 6.00%; excess_return_240d 2.09% < 8.00%; volatility_120d 58.29% > 42.00% |
| 600039.SH | 四川路桥 | ok | 27.77 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.97% < 6.00%; excess_return_120d -18.55% < 6.00%; excess_return_240d -27.45% < 8.00% |
| 300059.SZ | 东方财富 | ok | 27.74 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.23% < 6.00%; excess_return_120d -12.81% < 6.00%; excess_return_240d -29.21% < 8.00% |
| 002888.SZ | 惠威科技 | ok | 27.74 | stock_return_120d 2.08% < 6.00%; excess_return_120d -2.50% < 6.00%; excess_return_240d -12.25% < 8.00%; volatility_120d 49.18% > 42.00% |
| 002267.SZ | 陕天然气 | ok | 27.73 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.41% < 6.00%; excess_return_120d -7.99% < 6.00%; excess_return_240d -27.82% < 8.00% |
| 688351.SH | 微电生理 | ok | 27.71 | close_below_ma200; stock_return_120d 0.09% < 6.00%; excess_return_120d -4.49% < 6.00%; excess_return_240d -4.35% < 8.00% |
| 603477.SH | 巨星农牧 | ok | 27.71 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -2.68% < 6.00%; excess_return_120d -7.26% < 6.00%; excess_return_240d -41.51% < 8.00%; volatility_120d 45.19% > 42.00% |
| 300670.SZ | 大烨智能 | ok | 27.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.91% < 6.00%; excess_return_120d -10.49% < 6.00%; excess_return_240d -38.91% < 8.00%; volatility_120d 47.39% > 42.00% |
| 600509.SH | 天富能源 | ok | 27.68 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.20% < 6.00%; excess_return_120d -4.78% < 6.00%; excess_return_240d 3.75% < 8.00%; volatility_120d 50.36% > 42.00% |
| 300735.SZ | 光弘科技 | ok | 27.68 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.34% < 6.00%; excess_return_120d -10.92% < 6.00%; excess_return_240d -27.09% < 8.00%; volatility_120d 60.02% > 42.00% |
| 002287.SZ | 奇正藏药 | ok | 27.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.98% < 6.00%; excess_return_120d -15.56% < 6.00%; excess_return_240d -25.16% < 8.00% |
| 002007.SZ | 华兰生物 | ok | 27.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.46% < 6.00%; excess_return_120d -15.04% < 6.00%; excess_return_240d -32.94% < 8.00% |
| 000049.SZ | 德赛电池 | ok | 27.61 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.40% < 6.00%; excess_return_120d -9.98% < 6.00%; excess_return_240d -8.15% < 8.00% |
| 300445.SZ | 康斯特 | ok | 27.61 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.49% < 6.00%; excess_return_120d -22.07% < 6.00%; excess_return_240d 3.15% < 8.00%; volatility_120d 50.92% > 42.00% |
| 600918.SH | 中泰证券 | ok | 27.60 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.38% < 6.00%; excess_return_120d -19.96% < 6.00%; excess_return_240d -37.64% < 8.00% |
| 600310.SH | 广西能源 | ok | 27.59 | close_below_ma200; stock_return_120d 5.82% < 6.00%; excess_return_120d 1.24% < 6.00%; excess_return_240d -27.64% < 8.00%; drawdown_120d -44.67% < -28.00%; volatility_120d 63.25% > 42.00% |
| 600630.SH | 龙头股份 | ok | 27.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -4.10% < 6.00%; excess_return_120d -8.68% < 6.00%; excess_return_240d -14.87% < 8.00% |
| 002797.SZ | 第一创业 | ok | 27.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -2.04% < 6.00%; excess_return_120d -6.62% < 6.00%; excess_return_240d -25.77% < 8.00% |
| 603889.SH | 新澳股份 | ok | 27.58 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.34% < 6.00%; excess_return_120d -13.92% < 6.00%; excess_return_240d 4.41% < 8.00% |
| 301261.SZ | 恒工精密 | ok | 27.56 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.03% < 6.00%; excess_return_120d -21.61% < 6.00%; excess_return_240d 2.09% < 8.00%; volatility_120d 57.57% > 42.00% |
| 300190.SZ | 维尔利 | ok | 27.55 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -1.17% < 6.00%; excess_return_120d -5.75% < 6.00%; excess_return_240d -3.65% < 8.00%; volatility_120d 43.13% > 42.00% |
| 688247.SH | 宣泰医药 | ok | 27.54 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -4.75% < 6.00%; excess_return_120d -9.33% < 6.00%; excess_return_240d -35.04% < 8.00% |
| 002695.SZ | 煌上煌 | ok | 27.53 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -7.39% < 6.00%; excess_return_120d -11.97% < 6.00%; excess_return_240d -25.78% < 8.00% |
| 603956.SH | 威派格 | ok | 27.53 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.81% < 6.00%; excess_return_120d -11.39% < 6.00%; excess_return_240d -33.09% < 8.00%; volatility_120d 50.61% > 42.00% |
| 688018.SH | 乐鑫科技 | ok | 27.51 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -4.49% < 6.00%; excess_return_120d -9.07% < 6.00%; excess_return_240d -11.56% < 8.00%; volatility_120d 49.55% > 42.00% |
| 688036.SH | 传音控股 | ok | 27.48 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.14% < 6.00%; excess_return_120d -11.72% < 6.00%; excess_return_240d -40.69% < 8.00%; volatility_120d 44.67% > 42.00% |
| 688009.SH | 中国通号 | ok | 27.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.69% < 6.00%; excess_return_120d -14.27% < 6.00%; excess_return_240d -24.42% < 8.00% |
| 000507.SZ | 珠海港 | ok | 27.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.50% < 6.00%; excess_return_120d -12.08% < 6.00%; excess_return_240d -35.10% < 8.00% |
| 600993.SH | 马应龙 | ok | 27.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.32% < 6.00%; excess_return_120d -21.90% < 6.00%; excess_return_240d -34.65% < 8.00% |
| 603337.SH | 杰克科技 | ok | 27.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -4.55% < 6.00%; excess_return_120d -9.13% < 6.00%; excess_return_240d -2.65% < 8.00%; volatility_120d 49.35% > 42.00% |
| 603893.SH | 瑞芯微 | ok | 27.38 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -1.05% < 6.00%; excess_return_120d -5.63% < 6.00%; excess_return_240d -4.58% < 8.00%; volatility_120d 44.67% > 42.00% |
| 000680.SZ | 山推股份 | ok | 27.38 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.84% < 6.00%; excess_return_120d -12.42% < 6.00%; excess_return_240d -3.17% < 8.00% |
| 002200.SZ | 交投生态 | ok | 27.35 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.14% < 6.00%; excess_return_120d -15.24% < 6.00%; excess_return_240d -24.67% < 8.00% |
| 002236.SZ | 大华股份 | ok | 27.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.40% < 6.00%; excess_return_120d -14.98% < 6.00%; excess_return_240d -12.69% < 8.00% |
| 300611.SZ | 美力科技 | ok | 27.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -4.06% < 6.00%; excess_return_120d -8.64% < 6.00%; excess_return_240d -3.51% < 8.00%; volatility_120d 47.71% > 42.00% |
| 001358.SZ | 兴欣新材 | ok | 27.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 1.21% < 6.00%; excess_return_120d -3.37% < 6.00%; excess_return_240d -10.87% < 8.00%; volatility_120d 43.41% > 42.00% |
| 600995.SH | 南网储能 | ok | 27.26 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.26% < 6.00%; excess_return_120d -4.85% < 6.00%; excess_return_240d 3.71% < 8.00%; volatility_120d 42.04% > 42.00% |
| 300920.SZ | 润阳科技 | ok | 27.24 | stock_return_120d -3.88% < 6.00%; excess_return_120d -8.46% < 6.00%; excess_return_240d -25.60% < 8.00%; volatility_120d 50.40% > 42.00% |
| 603033.SH | 三维股份 | ok | 27.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.55% < 6.00%; excess_return_120d -10.13% < 6.00%; excess_return_240d -29.36% < 8.00%; volatility_120d 43.85% > 42.00% |
| 301199.SZ | 迈赫股份 | ok | 27.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.43% < 6.00%; excess_return_120d -10.01% < 6.00%; excess_return_240d -33.12% < 8.00%; volatility_120d 45.00% > 42.00% |
| 688455.SH | 科捷智能 | ok | 27.21 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.00% < 6.00%; excess_return_120d -16.58% < 6.00%; excess_return_240d 5.46% < 8.00%; drawdown_120d -42.75% < -28.00%; volatility_120d 62.61% > 42.00% |
| 002100.SZ | 天康生物 | ok | 27.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.43% < 6.00%; excess_return_120d -12.01% < 6.00%; excess_return_240d -12.44% < 8.00% |
| 300026.SZ | 红日药业 | ok | 27.18 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.23% < 6.00%; excess_return_120d -14.81% < 6.00%; excess_return_240d -40.69% < 8.00% |
| 300643.SZ | 万通智控 | ok | 27.16 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -1.15% < 6.00%; excess_return_120d -5.73% < 6.00%; excess_return_240d -23.57% < 8.00%; volatility_120d 42.39% > 42.00% |
| 600056.SH | 中国医药 | ok | 27.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.41% < 6.00%; excess_return_120d -13.99% < 6.00%; excess_return_240d -31.07% < 8.00% |
| 688589.SH | 力合微 | ok | 27.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -2.16% < 6.00%; excess_return_120d -6.74% < 6.00%; excess_return_240d -16.81% < 8.00%; volatility_120d 52.42% > 42.00% |
| 002311.SZ | 海大集团 | ok | 27.12 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.12% < 6.00%; excess_return_120d -17.70% < 6.00%; excess_return_240d -39.17% < 8.00% |
| 000597.SZ | 东北制药 | ok | 27.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.33% < 6.00%; excess_return_120d -15.91% < 6.00%; excess_return_240d -34.44% < 8.00% |
| 603768.SH | 常青股份 | ok | 27.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.38% < 6.00%; excess_return_120d -15.96% < 6.00%; excess_return_240d -40.91% < 8.00% |
| 300013.SZ | 新宁物流 | ok | 27.06 | close_below_ma200; ma120_not_above_ma200; stock_return_120d 2.54% < 6.00%; excess_return_120d -2.04% < 6.00%; excess_return_240d -22.32% < 8.00% |
| 605369.SH | 拱东医疗 | ok | 27.05 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -1.89% < 6.00%; excess_return_120d -6.47% < 6.00%; excess_return_240d -28.21% < 8.00% |
| 002748.SZ | 世龙实业 | ok | 27.03 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.25% < 6.00%; excess_return_120d -18.83% < 6.00%; excess_return_240d -8.37% < 8.00% |
| 000906.SZ | 浙商中拓 | ok | 26.99 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.04% < 6.00%; excess_return_120d -10.63% < 6.00%; excess_return_240d -35.70% < 8.00% |
| 002793.SZ | 罗欣药业 | ok | 26.98 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -1.25% < 6.00%; excess_return_120d -5.83% < 6.00%; excess_return_240d -23.97% < 8.00%; volatility_120d 43.54% > 42.00% |
| 601500.SH | 通用股份 | ok | 26.98 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.26% < 6.00%; excess_return_120d -22.84% < 6.00%; excess_return_240d -36.55% < 8.00% |
| 600282.SH | 南钢股份 | ok | 26.97 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.52% < 6.00%; excess_return_120d -10.10% < 6.00%; excess_return_240d -7.59% < 8.00% |
| 000795.SZ | 英洛华 | ok | 26.96 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.18% < 6.00%; excess_return_120d -10.76% < 6.00%; excess_return_240d -33.39% < 8.00% |
| 603689.SH | 皖天然气 | ok | 26.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.89% < 6.00%; excess_return_120d -10.47% < 6.00%; excess_return_240d -31.68% < 8.00% |
| 600130.SH | 波导股份 | ok | 26.95 | close_below_ma200; stock_return_120d -0.24% < 6.00%; excess_return_120d -4.34% < 6.00%; excess_return_240d 3.34% < 8.00%; drawdown_120d -38.92% < -28.00%; volatility_120d 47.23% > 42.00% |
| 600739.SH | 辽宁成大 | ok | 26.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.44% < 6.00%; excess_return_120d -11.02% < 6.00%; excess_return_240d -27.45% < 8.00% |
| 301079.SZ | 邵阳液压 | ok | 26.92 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 5.48% < 6.00%; excess_return_120d 0.90% < 6.00%; excess_return_240d -18.19% < 8.00%; drawdown_120d -52.48% < -28.00%; volatility_120d 92.31% > 42.00% |
| 000063.SZ | 中兴通讯 | ok | 26.90 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -4.12% < 6.00%; excess_return_120d -8.70% < 6.00%; excess_return_240d -10.22% < 8.00%; volatility_120d 43.69% > 42.00% |
| 300740.SZ | 水羊股份 | ok | 26.89 | close_below_ma200; stock_return_120d -13.02% < 6.00%; excess_return_120d -17.60% < 6.00%; excess_return_240d 3.67% < 8.00%; volatility_120d 50.66% > 42.00% |
| 301121.SZ | 紫建电子 | ok | 26.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.68% < 6.00%; excess_return_120d -12.26% < 6.00%; excess_return_240d -32.36% < 8.00% |
| 002338.SZ | 奥普光电 | ok | 26.87 | close_below_ma200; stock_return_120d -6.41% < 6.00%; excess_return_120d -10.99% < 6.00%; excess_return_240d -1.17% < 8.00%; volatility_120d 46.58% > 42.00% |
| 002233.SZ | 塔牌集团 | ok | 26.85 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.57% < 6.00%; excess_return_120d -13.15% < 6.00%; excess_return_240d -14.99% < 8.00% |
| 600975.SH | 新五丰 | ok | 26.83 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.45% < 6.00%; excess_return_120d -20.03% < 6.00%; excess_return_240d -40.51% < 8.00% |
| 301332.SZ | 德尔玛 | ok | 26.83 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.74% < 6.00%; excess_return_120d -17.32% < 6.00%; excess_return_240d -49.05% < 8.00% |
| 300016.SZ | 北陆药业 | ok | 26.82 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 5.29% < 6.00%; excess_return_120d 0.71% < 6.00%; excess_return_240d -38.73% < 8.00%; volatility_120d 49.34% > 42.00% |
| 688612.SH | 威迈斯 | ok | 26.80 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -3.41% < 6.00%; excess_return_120d -7.99% < 6.00%; excess_return_240d -2.98% < 8.00%; volatility_120d 48.77% > 42.00% |
| 603899.SH | 晨光股份 | ok | 26.80 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.33% < 6.00%; excess_return_120d -19.91% < 6.00%; excess_return_240d -43.76% < 8.00% |
| 600519.SH | 贵州茅台 | ok | 26.72 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.54% < 6.00%; excess_return_120d -15.12% < 6.00%; excess_return_240d -32.62% < 8.00% |
| 605266.SH | 健之佳 | ok | 26.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.40% < 6.00%; excess_return_120d -14.98% < 6.00%; excess_return_240d -38.90% < 8.00% |
| 300665.SZ | 飞鹿股份 | ok | 26.70 | ma120_not_above_ma200; stock_return_120d -2.85% < 6.00%; excess_return_120d -7.14% < 6.00%; excess_return_240d -8.78% < 8.00%; volatility_120d 55.57% > 42.00% |
| 002023.SZ | 海特高新 | ok | 26.68 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -8.71% < 6.00%; excess_return_120d -13.30% < 6.00%; excess_return_240d -3.94% < 8.00%; volatility_120d 55.74% > 42.00% |
| 000878.SZ | 云南铜业 | ok | 26.66 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.20% < 6.00%; excess_return_120d -25.78% < 6.00%; excess_return_240d 5.73% < 8.00%; drawdown_120d -45.35% < -28.00%; volatility_120d 59.25% > 42.00% |
| 300124.SZ | 汇川技术 | ok | 26.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.69% < 6.00%; excess_return_120d -13.27% < 6.00%; excess_return_240d -11.82% < 8.00% |
| 000543.SZ | 皖能电力 | ok | 26.64 | close_below_ma200; stock_return_120d -1.38% < 6.00%; excess_return_120d -5.96% < 6.00%; excess_return_240d -14.43% < 8.00% |
| 600593.SH | 大连圣亚 | ok | 26.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.26% < 6.00%; excess_return_120d -12.84% < 6.00%; excess_return_240d 3.19% < 8.00%; volatility_120d 51.05% > 42.00% |
| 603091.SH | 众鑫股份 | ok | 26.63 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.74% < 6.00%; excess_return_120d -14.32% < 6.00%; excess_return_240d -11.27% < 8.00% |
| 605058.SH | 澳弘电子 | ok | 26.61 | close_below_ma200; stock_return_120d 3.90% < 6.00%; excess_return_120d -0.68% < 6.00%; excess_return_240d -11.31% < 8.00%; volatility_120d 53.42% > 42.00% |
| 601177.SH | 杭齿前进 | ok | 26.61 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.94% < 6.00%; excess_return_120d -15.52% < 6.00%; excess_return_240d -34.64% < 8.00%; volatility_120d 43.17% > 42.00% |
| 601021.SH | 春秋航空 | ok | 26.60 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.51% < 6.00%; excess_return_120d -24.09% < 6.00%; excess_return_240d -32.52% < 8.00% |
| 300021.SZ | 大禹节水 | ok | 26.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.09% < 6.00%; excess_return_120d -15.67% < 6.00%; excess_return_240d -36.07% < 8.00% |
| 000600.SZ | 建投能源 | ok | 26.59 | close_below_ma200; stock_return_120d 4.75% < 6.00%; excess_return_120d 0.17% < 6.00%; excess_return_240d -3.45% < 8.00%; drawdown_120d -33.80% < -28.00%; volatility_120d 54.00% > 42.00% |
| 300181.SZ | 佐力药业 | ok | 26.58 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.13% < 6.00%; excess_return_120d -13.71% < 6.00%; excess_return_240d -42.97% < 8.00% |
| 301439.SZ | 泓淋电力 | ok | 26.57 | close_below_ma200; stock_return_120d 4.89% < 6.00%; excess_return_120d 0.31% < 6.00%; excess_return_240d -31.13% < 8.00%; drawdown_120d -39.13% < -28.00%; volatility_120d 57.86% > 42.00% |
| 002752.SZ | 昇兴股份 | ok | 26.57 | close_below_ma200; stock_return_120d -6.57% < 6.00%; excess_return_120d -11.16% < 6.00%; excess_return_240d -10.21% < 8.00% |
| 300320.SZ | 海达股份 | ok | 26.54 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 0.97% < 6.00%; excess_return_120d -3.61% < 6.00%; excess_return_240d -26.15% < 8.00% |
| 002522.SZ | 浙江众成 | ok | 26.52 | close_below_ma200; stock_return_120d 3.91% < 6.00%; excess_return_120d -0.67% < 6.00%; excess_return_240d -6.59% < 8.00%; drawdown_120d -30.81% < -28.00%; volatility_120d 56.59% > 42.00% |
| 000915.SZ | 华特达因 | ok | 26.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.07% < 6.00%; excess_return_120d -22.65% < 6.00%; excess_return_240d -36.30% < 8.00% |
| 002550.SZ | 千红制药 | ok | 26.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.14% < 6.00%; excess_return_120d -14.72% < 6.00%; excess_return_240d -43.07% < 8.00% |
| 600004.SH | 白云机场 | ok | 26.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.77% < 6.00%; excess_return_120d -24.35% < 6.00%; excess_return_240d -37.41% < 8.00% |
| 600597.SH | 光明乳业 | ok | 26.48 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.27% < 6.00%; excess_return_120d -24.85% < 6.00%; excess_return_240d -43.48% < 8.00% |
| 300406.SZ | 九强生物 | ok | 26.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.20% < 6.00%; excess_return_120d -9.78% < 6.00%; excess_return_240d -29.51% < 8.00% |
| 301096.SZ | 百诚医药 | ok | 26.46 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -1.62% < 6.00%; excess_return_120d -6.11% < 6.00%; excess_return_240d -4.11% < 8.00%; volatility_120d 44.62% > 42.00% |
| 000544.SZ | 中原环保 | ok | 26.45 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.56% < 6.00%; excess_return_120d -15.14% < 6.00%; excess_return_240d -31.54% < 8.00% |
| 300529.SZ | 健帆生物 | ok | 26.44 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.02% < 6.00%; excess_return_120d -17.60% < 6.00%; excess_return_240d -46.33% < 8.00% |
| 000937.SZ | 冀中能源 | ok | 26.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.71% < 6.00%; excess_return_120d -12.29% < 6.00%; excess_return_240d -36.65% < 8.00% |
| 603014.SH | 威高血净 | ok | 26.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.60% < 6.00%; excess_return_120d -14.18% < 6.00%; excess_return_240d -25.06% < 8.00% |
| 603191.SH | 望变电气 | ok | 26.41 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 5.83% < 6.00%; excess_return_120d 1.25% < 6.00%; excess_return_240d 0.93% < 8.00%; drawdown_120d -43.49% < -28.00%; volatility_120d 58.52% > 42.00% |
| 002587.SZ | 奥拓电子 | ok | 26.40 | close_below_ma200; stock_return_120d -5.22% < 6.00%; excess_return_120d -9.80% < 6.00%; excess_return_240d -23.25% < 8.00%; volatility_120d 46.58% > 42.00% |
| 002521.SZ | 齐峰新材 | ok | 26.40 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.33% < 6.00%; excess_return_120d -13.91% < 6.00%; excess_return_240d -37.88% < 8.00% |
| 000758.SZ | 中色股份 | ok | 26.40 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.77% < 6.00%; excess_return_120d -8.35% < 6.00%; excess_return_240d 3.46% < 8.00%; drawdown_120d -32.95% < -28.00%; volatility_120d 56.21% > 42.00% |
| 300193.SZ | 佳士科技 | ok | 26.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.67% < 6.00%; excess_return_120d -13.25% < 6.00%; excess_return_240d -31.02% < 8.00% |
| 000506.SZ | 招金黄金 | ok | 26.38 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 0.38% < 6.00%; excess_return_120d -4.20% < 6.00%; excess_return_240d 4.48% < 8.00%; drawdown_120d -54.03% < -28.00%; volatility_120d 75.06% > 42.00% |
| 600897.SH | 厦门空港 | ok | 26.38 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.49% < 6.00%; excess_return_120d -18.07% < 6.00%; excess_return_240d -18.48% < 8.00% |
| 688716.SH | 中研股份 | ok | 26.38 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.74% < 6.00%; excess_return_120d -16.32% < 6.00%; excess_return_240d -12.36% < 8.00%; volatility_120d 48.46% > 42.00% |
| 002826.SZ | 易明医药 | ok | 26.36 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 0.38% < 6.00%; excess_return_120d -4.20% < 6.00%; excess_return_240d -21.70% < 8.00%; volatility_120d 50.52% > 42.00% |
| 688321.SH | 微芯生物 | ok | 26.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -1.17% < 6.00%; excess_return_120d -5.75% < 6.00%; excess_return_240d -29.14% < 8.00% |
| 600027.SH | 华电国际 | ok | 26.32 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.81% < 6.00%; excess_return_120d -10.39% < 6.00%; excess_return_240d -35.44% < 8.00% |
| 002662.SZ | 峰璟股份 | ok | 26.32 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.32% < 6.00%; excess_return_120d -13.90% < 6.00%; excess_return_240d -18.53% < 8.00% |
| 300409.SZ | 道氏技术 | ok | 26.31 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.46% < 6.00%; excess_return_120d -14.04% < 6.00%; excess_return_240d 6.50% < 8.00%; drawdown_120d -45.76% < -28.00%; volatility_120d 59.47% > 42.00% |
| 600123.SH | 兰花科创 | ok | 26.30 | close_below_ma200; ma120_not_above_ma200; stock_return_120d 2.03% < 6.00%; excess_return_120d -2.55% < 6.00%; excess_return_240d -28.04% < 8.00% |
| 600973.SH | 宝胜股份 | ok | 26.29 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.42% < 6.00%; excess_return_120d -18.00% < 6.00%; excess_return_240d 2.58% < 8.00%; drawdown_120d -32.62% < -28.00%; volatility_120d 51.49% > 42.00% |
| 002170.SZ | 芭田股份 | ok | 26.27 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -1.81% < 6.00%; excess_return_120d -6.39% < 6.00%; excess_return_240d -10.42% < 8.00% |
| 000541.SZ | 佛山照明 | ok | 26.24 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.09% < 6.00%; excess_return_120d -17.67% < 6.00%; excess_return_240d -40.54% < 8.00% |
| 600054.SH | 黄山旅游 | ok | 26.24 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.26% < 6.00%; excess_return_120d -4.84% < 6.00%; excess_return_240d -24.22% < 8.00% |
| 301098.SZ | 金埔园林 | ok | 26.24 | close_below_ma200; stock_return_120d 1.63% < 6.00%; excess_return_120d -2.95% < 6.00%; excess_return_240d -26.31% < 8.00%; volatility_120d 50.05% > 42.00% |
| 600210.SH | 紫江企业 | ok | 26.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.88% < 6.00%; excess_return_120d -18.46% < 6.00%; excess_return_240d -23.41% < 8.00% |
| 688755.SH | 汉邦科技 | ok | 26.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.32% < 6.00%; excess_return_120d -14.90% < 6.00%; excess_return_240d -43.93% < 8.00% |
| 002374.SZ | 中锐股份 | ok | 26.23 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.83% < 6.00%; excess_return_120d -15.41% < 6.00%; excess_return_240d -9.25% < 8.00%; volatility_120d 46.99% > 42.00% |
| 601065.SH | 江盐集团 | ok | 26.22 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.70% < 6.00%; excess_return_120d -19.28% < 6.00%; excess_return_240d -35.59% < 8.00% |
| 600356.SH | 恒丰纸业 | ok | 26.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -4.89% < 6.00%; excess_return_120d -9.47% < 6.00%; excess_return_240d -18.59% < 8.00% |
| 301206.SZ | 三元生物 | ok | 26.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.85% < 6.00%; excess_return_120d -14.43% < 6.00%; excess_return_240d -43.41% < 8.00% |
| 600977.SH | 中国电影 | ok | 26.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.39% < 6.00%; excess_return_120d -15.97% < 6.00%; excess_return_240d 3.84% < 8.00%; drawdown_120d -32.90% < -28.00%; volatility_120d 46.71% > 42.00% |
| 002173.SZ | 创新医疗 | ok | 26.20 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.90% < 6.00%; excess_return_120d -14.48% < 6.00%; excess_return_240d 6.32% < 8.00%; drawdown_120d -49.41% < -28.00%; volatility_120d 66.80% > 42.00% |
| 000790.SZ | 华神科技 | ok | 26.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -2.84% < 6.00%; excess_return_120d -7.42% < 6.00%; excess_return_240d -26.86% < 8.00% |
| 300230.SZ | 永利股份 | ok | 26.18 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.73% < 6.00%; excess_return_120d -12.31% < 6.00%; excess_return_240d -32.49% < 8.00% |
| 002111.SZ | 威海广泰 | ok | 26.16 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.60% < 6.00%; excess_return_120d -16.18% < 6.00%; excess_return_240d -32.13% < 8.00% |
| 600976.SH | 健民集团 | ok | 26.16 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.54% < 6.00%; excess_return_120d -16.12% < 6.00%; excess_return_240d -45.72% < 8.00% |
| 603219.SH | 富佳股份 | ok | 26.15 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.69% < 6.00%; excess_return_120d -8.27% < 6.00%; excess_return_240d -9.20% < 8.00%; volatility_120d 42.23% > 42.00% |
| 601069.SH | 西部黄金 | ok | 26.14 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.46% < 6.00%; excess_return_120d -9.04% < 6.00%; excess_return_240d 5.51% < 8.00%; drawdown_120d -49.67% < -28.00%; volatility_120d 65.22% > 42.00% |
| 300823.SZ | 建科智能 | ok | 26.11 | close_below_ma200; stock_return_120d 0.43% < 6.00%; excess_return_120d -4.15% < 6.00%; excess_return_240d -16.45% < 8.00% |
| 600894.SH | 广日股份 | ok | 26.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.60% < 6.00%; excess_return_120d -14.18% < 6.00%; excess_return_240d -38.37% < 8.00% |
| 600727.SH | 鲁北化工 | ok | 26.07 | close_below_ma200; stock_return_120d 3.24% < 6.00%; excess_return_120d -1.34% < 6.00%; excess_return_240d -30.65% < 8.00%; volatility_120d 46.75% > 42.00% |
| 300194.SZ | 福安药业 | ok | 26.06 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.98% < 6.00%; excess_return_120d -20.56% < 6.00%; excess_return_240d -35.91% < 8.00% |
| 301223.SZ | 中荣股份 | ok | 26.05 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.17% < 6.00%; excess_return_120d -13.75% < 6.00%; excess_return_240d -23.56% < 8.00% |
| 002084.SZ | 海鸥住工 | ok | 26.05 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.76% < 6.00%; excess_return_120d -13.34% < 6.00%; excess_return_240d -23.84% < 8.00% |
| 603194.SH | 中力股份 | ok | 26.05 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.80% < 6.00%; excess_return_120d -17.38% < 6.00%; excess_return_240d -38.30% < 8.00% |
| 600011.SH | 华能国际 | ok | 26.03 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -0.71% < 6.00%; excess_return_120d -5.29% < 6.00%; excess_return_240d -18.76% < 8.00% |
| 002191.SZ | 劲嘉股份 | ok | 26.03 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.79% < 6.00%; excess_return_120d -14.37% < 6.00%; excess_return_240d -28.68% < 8.00% |
| 002011.SZ | 盾安环境 | ok | 26.01 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.80% < 6.00%; excess_return_120d -18.38% < 6.00%; excess_return_240d -28.86% < 8.00% |
| 002849.SZ | 威星智能 | ok | 26.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.25% < 6.00%; excess_return_120d -4.83% < 6.00%; excess_return_240d -15.50% < 8.00%; volatility_120d 51.74% > 42.00% |
| 603987.SH | 康德莱 | ok | 25.99 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.46% < 6.00%; excess_return_120d -17.04% < 6.00%; excess_return_240d -24.63% < 8.00% |
| 601038.SH | 一拖股份 | ok | 25.99 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.90% < 6.00%; excess_return_120d -17.48% < 6.00%; excess_return_240d -26.57% < 8.00% |
| 300883.SZ | 龙利得 | ok | 25.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.30% < 6.00%; excess_return_120d -12.88% < 6.00%; excess_return_240d -27.02% < 8.00% |
| 600300.SH | 维维股份 | ok | 25.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.51% < 6.00%; excess_return_120d -17.09% < 6.00%; excess_return_240d -32.56% < 8.00% |
| 001219.SZ | 青岛食品 | ok | 25.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.79% < 6.00%; excess_return_120d -16.37% < 6.00%; excess_return_240d -31.80% < 8.00% |
| 605008.SH | 长鸿高科 | ok | 25.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.30% < 6.00%; excess_return_120d -18.88% < 6.00%; excess_return_240d -39.80% < 8.00% |
| 688065.SH | 凯赛生物 | ok | 25.93 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.68% < 6.00%; excess_return_120d -5.26% < 6.00%; excess_return_240d -13.81% < 8.00%; volatility_120d 45.55% > 42.00% |
| 600736.SH | 苏州高新 | ok | 25.93 | stock_return_120d -1.78% < 6.00%; excess_return_120d -6.36% < 6.00%; excess_return_240d 1.14% < 8.00%; drawdown_120d -37.42% < -28.00%; volatility_120d 55.39% > 42.00% |
| 603051.SH | 鹿山新材 | ok | 25.93 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 3.49% < 6.00%; excess_return_120d -1.09% < 6.00%; excess_return_240d -13.41% < 8.00%; volatility_120d 48.57% > 42.00% |
| 600749.SH | 西藏旅游 | ok | 25.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.47% < 6.00%; excess_return_120d -17.05% < 6.00%; excess_return_240d 4.64% < 8.00%; drawdown_120d -32.05% < -28.00%; volatility_120d 44.21% > 42.00% |
| 601728.SH | 中国电信 | ok | 25.92 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -10.29% < 6.00%; excess_return_120d -14.87% < 6.00%; excess_return_240d -45.40% < 8.00% |
| 300702.SZ | 天宇股份 | ok | 25.91 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.43% < 6.00%; excess_return_120d -12.01% < 6.00%; excess_return_240d -32.80% < 8.00% |
| 600333.SH | 长春燃气 | ok | 25.90 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -1.27% < 6.00%; excess_return_120d -5.85% < 6.00%; excess_return_240d -10.12% < 8.00% |
| 002189.SZ | 中光学 | ok | 25.88 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.61% < 6.00%; excess_return_120d -15.19% < 6.00%; excess_return_240d -43.33% < 8.00% |
| 603116.SH | 红蜻蜓 | ok | 25.88 | stock_return_120d 2.03% < 6.00%; excess_return_120d -2.55% < 6.00%; excess_return_240d -18.20% < 8.00%; volatility_120d 47.34% > 42.00% |
| 002939.SZ | 长城证券 | ok | 25.86 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.25% < 6.00%; excess_return_120d -21.84% < 6.00%; excess_return_240d -19.43% < 8.00% |
| 603107.SH | 上海汽配 | ok | 25.85 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.10% < 6.00%; excess_return_120d -22.68% < 6.00%; excess_return_240d -43.22% < 8.00% |
| 002736.SZ | 国信证券 | ok | 25.85 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.81% < 6.00%; excess_return_120d -21.39% < 6.00%; excess_return_240d -27.07% < 8.00% |
| 300053.SZ | 航宇微 | ok | 25.84 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.88% < 6.00%; excess_return_120d -20.46% < 6.00%; excess_return_240d 2.74% < 8.00%; drawdown_120d -38.13% < -28.00%; volatility_120d 67.28% > 42.00% |
| 002390.SZ | 信邦制药 | ok | 25.83 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.40% < 6.00%; excess_return_120d -16.98% < 6.00%; excess_return_240d -41.77% < 8.00% |
| 301337.SZ | 亚华电子 | ok | 25.83 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 0.36% < 6.00%; excess_return_120d -4.22% < 6.00%; excess_return_240d -26.99% < 8.00%; volatility_120d 43.22% > 42.00% |
| 002594.SZ | 比亚迪 | ok | 25.83 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.42% < 6.00%; excess_return_120d -15.00% < 6.00%; excess_return_240d -39.77% < 8.00% |
| 603038.SH | 华立股份 | ok | 25.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -1.37% < 6.00%; excess_return_120d -5.95% < 6.00%; excess_return_240d -10.78% < 8.00%; volatility_120d 42.55% > 42.00% |
| 605507.SH | 国邦医药 | ok | 25.80 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.84% < 6.00%; excess_return_120d -12.42% < 6.00%; excess_return_240d -8.29% < 8.00% |
| 300866.SZ | 安克创新 | ok | 25.80 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -5.02% < 6.00%; excess_return_120d -9.60% < 6.00%; excess_return_240d -29.38% < 8.00%; volatility_120d 50.61% > 42.00% |
| 603329.SH | 上海雅仕 | ok | 25.79 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.82% < 6.00%; excess_return_120d -17.40% < 6.00%; excess_return_240d -37.57% < 8.00% |
| 600019.SH | 宝钢股份 | ok | 25.79 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.28% < 6.00%; excess_return_120d -26.86% < 6.00%; excess_return_240d -38.76% < 8.00% |
| 603408.SH | 建霖家居 | ok | 25.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.39% < 6.00%; excess_return_120d -24.97% < 6.00%; excess_return_240d -24.03% < 8.00% |
| 002391.SZ | 长青股份 | ok | 25.78 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.68% < 6.00%; excess_return_120d -13.26% < 6.00%; excess_return_240d -28.97% < 8.00% |
| 001230.SZ | 劲旅环境 | ok | 25.78 | close_below_ma200; stock_return_120d 3.58% < 6.00%; excess_return_120d -1.00% < 6.00%; excess_return_240d -15.80% < 8.00%; volatility_120d 43.28% > 42.00% |
| 688798.SH | 艾为电子 | ok | 25.77 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.03% < 6.00%; excess_return_120d -12.61% < 6.00%; excess_return_240d -16.28% < 8.00%; volatility_120d 45.26% > 42.00% |
| 603717.SH | 天域生物 | ok | 25.75 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.61% < 6.00%; excess_return_120d -16.19% < 6.00%; excess_return_240d -28.20% < 8.00%; volatility_120d 51.11% > 42.00% |
| 000869.SZ | 张裕A | ok | 25.73 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.10% < 6.00%; excess_return_120d -22.68% < 6.00%; excess_return_240d -42.71% < 8.00% |
| 300233.SZ | 金城医药 | ok | 25.72 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.12% < 6.00%; excess_return_120d -7.70% < 6.00%; excess_return_240d -39.34% < 8.00% |
| 301109.SZ | 军信股份 | ok | 25.70 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.43% < 6.00%; excess_return_120d -11.01% < 6.00%; excess_return_240d -29.69% < 8.00% |
| 688787.SH | 海天瑞声 | ok | 25.65 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 4.63% < 6.00%; excess_return_120d 0.04% < 6.00%; excess_return_240d 0.76% < 8.00%; drawdown_120d -38.74% < -28.00%; volatility_120d 73.18% > 42.00% |
| 603307.SH | 扬州金泉 | ok | 25.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.48% < 6.00%; excess_return_120d -11.06% < 6.00%; excess_return_240d -23.04% < 8.00% |
| 002377.SZ | 国创高新 | ok | 25.65 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 3.15% < 6.00%; excess_return_120d -1.43% < 6.00%; excess_return_240d -34.08% < 8.00% |
| 600648.SH | 外高桥 | ok | 25.63 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.26% < 6.00%; excess_return_120d -19.84% < 6.00%; excess_return_240d -43.01% < 8.00% |
| 603231.SH | 索宝蛋白 | ok | 25.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.04% < 6.00%; excess_return_120d -17.62% < 6.00%; excess_return_240d -26.89% < 8.00% |
| 600690.SH | 海尔智家 | ok | 25.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.12% < 6.00%; excess_return_120d -25.70% < 6.00%; excess_return_240d -36.40% < 8.00% |
| 603221.SH | 爱丽家居 | ok | 25.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.08% < 6.00%; excess_return_120d -14.66% < 6.00%; excess_return_240d -16.66% < 8.00% |
| 300648.SZ | 星云股份 | ok | 25.58 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.03% < 6.00%; excess_return_120d -22.61% < 6.00%; excess_return_240d 5.11% < 8.00%; drawdown_120d -34.95% < -28.00%; volatility_120d 45.33% > 42.00% |
| 002960.SZ | 青鸟智控 | ok | 25.57 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -1.53% < 6.00%; excess_return_120d -6.11% < 6.00%; excess_return_240d -16.89% < 8.00% |
| 000983.SZ | 山西焦煤 | ok | 25.55 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 0.31% < 6.00%; excess_return_120d -4.27% < 6.00%; excess_return_240d -18.12% < 8.00%; volatility_120d 43.78% > 42.00% |
| 600741.SH | 华域汽车 | ok | 25.53 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.75% < 6.00%; excess_return_120d -23.33% < 6.00%; excess_return_240d -29.03% < 8.00% |
| 300376.SZ | 易事特 | ok | 25.51 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.99% < 6.00%; excess_return_120d -28.09% < 6.00%; excess_return_240d 4.99% < 8.00%; drawdown_120d -40.28% < -28.00%; volatility_120d 56.84% > 42.00% |
| 301395.SZ | 仁信新材 | ok | 25.49 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 1.96% < 6.00%; excess_return_120d -2.62% < 6.00%; excess_return_240d -12.02% < 8.00%; volatility_120d 50.76% > 42.00% |
| 301166.SZ | 优宁维 | ok | 25.49 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.49% < 6.00%; excess_return_120d -10.07% < 6.00%; excess_return_240d -31.10% < 8.00% |
| 002767.SZ | 先锋电子 | ok | 25.48 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.40% < 6.00%; excess_return_120d -17.98% < 6.00%; excess_return_240d -7.89% < 8.00%; volatility_120d 42.26% > 42.00% |
| 600155.SH | 华创云信 | ok | 25.48 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.80% < 6.00%; excess_return_120d -19.38% < 6.00%; excess_return_240d -40.41% < 8.00% |
| 002661.SZ | 克明食品 | ok | 25.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.85% < 6.00%; excess_return_120d -19.43% < 6.00%; excess_return_240d -46.47% < 8.00% |
| 603949.SH | 雪龙集团 | ok | 25.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -1.02% < 6.00%; excess_return_120d -5.60% < 6.00%; excess_return_240d -21.21% < 8.00%; volatility_120d 51.38% > 42.00% |
| 000027.SZ | 深圳能源 | ok | 25.45 | close_below_ma200; stock_return_120d -0.79% < 6.00%; excess_return_120d -5.37% < 6.00%; excess_return_240d -24.02% < 8.00% |
| 603617.SH | 君禾股份 | ok | 25.44 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.95% < 6.00%; excess_return_120d -15.53% < 6.00%; excess_return_240d -32.04% < 8.00% |
| 000050.SZ | 深天马A | ok | 25.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -4.54% < 6.00%; excess_return_120d -9.12% < 6.00%; excess_return_240d -20.98% < 8.00%; volatility_120d 48.48% > 42.00% |
| 600551.SH | 时代出版 | ok | 25.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.64% < 6.00%; excess_return_120d -18.22% < 6.00%; excess_return_240d -43.19% < 8.00% |
| 688581.SH | 安杰思 | ok | 25.41 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.28% < 6.00%; excess_return_120d -7.86% < 6.00%; excess_return_240d -32.12% < 8.00% |
| 002786.SZ | 银宝山新 | ok | 25.40 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.19% < 6.00%; excess_return_120d -13.77% < 6.00%; excess_return_240d -42.37% < 8.00% |
| 600419.SH | 天润乳业 | ok | 25.40 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.72% < 6.00%; excess_return_120d -23.30% < 6.00%; excess_return_240d -39.49% < 8.00% |
| 603600.SH | 永艺股份 | ok | 25.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.46% < 6.00%; excess_return_120d -22.04% < 6.00%; excess_return_240d -28.02% < 8.00% |
| 601222.SH | 林洋能源 | ok | 25.39 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.37% < 6.00%; excess_return_120d -4.95% < 6.00%; excess_return_240d -30.61% < 8.00% |
| 000708.SZ | 中信特钢 | ok | 25.37 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.22% < 6.00%; excess_return_120d -19.80% < 6.00%; excess_return_240d -7.50% < 8.00% |
| 688306.SH | 均普智能 | ok | 25.37 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.42% < 6.00%; excess_return_120d -19.00% < 6.00%; excess_return_240d -15.14% < 8.00%; volatility_120d 45.99% > 42.00% |
| 603170.SH | 宝立食品 | ok | 25.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.59% < 6.00%; excess_return_120d -19.17% < 6.00%; excess_return_240d -22.50% < 8.00% |
| 603508.SH | 思维列控 | ok | 25.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.41% < 6.00%; excess_return_120d -22.89% < 6.00%; excess_return_240d -30.43% < 8.00% |
| 002801.SZ | 微光股份 | ok | 25.33 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.84% < 6.00%; excess_return_120d -18.42% < 6.00%; excess_return_240d -30.52% < 8.00% |
| 001390.SZ | 古麒绒材 | ok | 25.33 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.29% < 6.00%; excess_return_120d -21.87% < 6.00%; excess_return_240d -40.08% < 8.00% |
| 002145.SZ | 钛能化学 | ok | 25.31 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.35% < 6.00%; excess_return_120d -9.93% < 6.00%; excess_return_240d -10.33% < 8.00% |
| 001205.SZ | 盛航股份 | ok | 25.31 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.48% < 6.00%; excess_return_120d -23.06% < 6.00%; excess_return_240d -35.80% < 8.00% |
| 603071.SH | 物产环能 | ok | 25.30 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.61% < 6.00%; excess_return_120d -12.19% < 6.00%; excess_return_240d -28.34% < 8.00% |
| 002033.SZ | 丽江股份 | ok | 25.27 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.18% < 6.00%; excess_return_120d -7.76% < 6.00%; excess_return_240d -20.15% < 8.00% |
| 300439.SZ | 美康生物 | ok | 25.27 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.09% < 6.00%; excess_return_120d -16.67% < 6.00%; excess_return_240d -41.17% < 8.00% |
| 601628.SH | 中国人寿 | ok | 25.25 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.77% < 6.00%; excess_return_120d -19.35% < 6.00%; excess_return_240d -25.14% < 8.00% |
| 600171.SH | 上海贝岭 | ok | 25.25 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.22% < 6.00%; excess_return_120d -12.80% < 6.00%; excess_return_240d -35.56% < 8.00%; volatility_120d 42.04% > 42.00% |
| 603387.SH | 基蛋生物 | ok | 25.24 | close_below_ma200; stock_return_120d 1.34% < 6.00%; excess_return_120d -3.24% < 6.00%; excess_return_240d -15.25% < 8.00%; volatility_120d 45.87% > 42.00% |
| 300009.SZ | 安科生物 | ok | 25.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.98% < 6.00%; excess_return_120d -14.56% < 6.00%; excess_return_240d -22.62% < 8.00% |
| 300066.SZ | 三川智慧 | ok | 25.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.84% < 6.00%; excess_return_120d -15.42% < 6.00%; excess_return_240d 4.70% < 8.00%; drawdown_120d -35.93% < -28.00%; volatility_120d 56.95% > 42.00% |
| 002567.SZ | 唐人神 | ok | 25.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.82% < 6.00%; excess_return_120d -21.40% < 6.00%; excess_return_240d -45.16% < 8.00% |
| 603577.SH | 汇金通 | ok | 25.21 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.64% < 6.00%; excess_return_120d -12.22% < 6.00%; excess_return_240d -16.65% < 8.00%; volatility_120d 42.52% > 42.00% |
| 600834.SH | 申通地铁 | ok | 25.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.92% < 6.00%; excess_return_120d -21.50% < 6.00%; excess_return_240d -42.57% < 8.00% |
| 301238.SZ | 瑞泰新材 | ok | 25.16 | close_below_ma200; stock_return_120d 1.98% < 6.00%; excess_return_120d -2.60% < 6.00%; excess_return_240d -10.76% < 8.00%; volatility_120d 45.47% > 42.00% |
| 300899.SZ | 上海凯鑫 | ok | 25.14 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.39% < 6.00%; excess_return_120d -15.49% < 6.00%; excess_return_240d 4.05% < 8.00%; drawdown_120d -37.71% < -28.00%; volatility_120d 47.38% > 42.00% |
| 601766.SH | 中国中车 | ok | 25.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.23% < 6.00%; excess_return_120d -24.81% < 6.00%; excess_return_240d -41.80% < 8.00% |
| 600125.SH | 铁龙物流 | ok | 25.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.00% < 6.00%; excess_return_120d -20.58% < 6.00%; excess_return_240d -24.51% < 8.00% |
| 688077.SH | 大地熊 | ok | 25.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -0.62% < 6.00%; excess_return_120d -5.20% < 6.00%; excess_return_240d -24.08% < 8.00%; volatility_120d 53.09% > 42.00% |
| 603518.SH | 锦泓集团 | ok | 25.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.07% < 6.00%; excess_return_120d -20.65% < 6.00%; excess_return_240d -38.61% < 8.00% |
| 600773.SH | 西藏城投 | ok | 25.10 | close_below_ma200; stock_return_120d 2.02% < 6.00%; excess_return_120d -2.56% < 6.00%; excess_return_240d 3.56% < 8.00%; drawdown_120d -56.23% < -28.00%; volatility_120d 59.05% > 42.00% |
| 300441.SZ | 鲍斯股份 | ok | 25.10 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.83% < 6.00%; excess_return_120d -18.41% < 6.00%; excess_return_240d -40.42% < 8.00% |
| 001696.SZ | 宗申动力 | ok | 25.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.21% < 6.00%; excess_return_120d -11.79% < 6.00%; excess_return_240d -37.42% < 8.00%; volatility_120d 55.47% > 42.00% |
| 603676.SH | 卫信康 | ok | 25.03 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.87% < 6.00%; excess_return_120d -17.45% < 6.00%; excess_return_240d -55.50% < 8.00% |
| 601336.SH | 新华保险 | ok | 25.03 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.49% < 6.00%; excess_return_120d -12.07% < 6.00%; excess_return_240d -9.79% < 8.00% |
| 603350.SH | 安乃达 | ok | 25.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.59% < 6.00%; excess_return_120d -20.17% < 6.00%; excess_return_240d -29.72% < 8.00% |
| 300761.SZ | 立华股份 | ok | 25.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.02% < 6.00%; excess_return_120d -13.60% < 6.00%; excess_return_240d -19.57% < 8.00%; volatility_120d 43.57% > 42.00% |
| 300328.SZ | 宜安科技 | ok | 25.00 | close_below_ma200; stock_return_120d -12.77% < 6.00%; excess_return_120d -17.35% < 6.00%; excess_return_240d 3.92% < 8.00%; drawdown_120d -36.69% < -28.00%; volatility_120d 63.58% > 42.00% |
| 300019.SZ | 硅宝科技 | ok | 24.99 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.76% < 6.00%; excess_return_120d -12.34% < 6.00%; excess_return_240d -31.03% < 8.00%; volatility_120d 44.74% > 42.00% |
| 000987.SZ | 越秀资本 | ok | 24.98 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 1.61% < 6.00%; excess_return_120d -2.97% < 6.00%; excess_return_240d -0.34% < 8.00%; drawdown_120d -32.79% < -28.00%; volatility_120d 47.18% > 42.00% |
| 002399.SZ | 海普瑞 | ok | 24.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.13% < 6.00%; excess_return_120d -21.71% < 6.00%; excess_return_240d -38.72% < 8.00% |
| 300928.SZ | 华安鑫创 | ok | 24.96 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.19% < 6.00%; excess_return_120d -11.77% < 6.00%; excess_return_240d -36.86% < 8.00% |
| 300915.SZ | 海融科技 | ok | 24.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.91% < 6.00%; excess_return_120d -16.49% < 6.00%; excess_return_240d -48.67% < 8.00% |
| 600331.SH | 宏达股份 | ok | 24.95 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.12% < 6.00%; excess_return_120d -16.70% < 6.00%; excess_return_240d 4.77% < 8.00%; drawdown_120d -50.66% < -28.00%; volatility_120d 59.88% > 42.00% |
| 002043.SZ | 兔宝宝 | ok | 24.94 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.03% < 6.00%; excess_return_120d -22.61% < 6.00%; excess_return_240d 3.80% < 8.00%; drawdown_120d -35.32% < -28.00%; volatility_120d 47.06% > 42.00% |
| 000957.SZ | 中通客车 | ok | 24.93 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.84% < 6.00%; excess_return_120d -18.42% < 6.00%; excess_return_240d -35.39% < 8.00% |
| 000422.SZ | 湖北宜化 | ok | 24.92 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 0.93% < 6.00%; excess_return_120d -3.65% < 6.00%; excess_return_240d 1.32% < 8.00%; drawdown_120d -29.37% < -28.00%; volatility_120d 50.38% > 42.00% |
| 603209.SH | 兴通股份 | ok | 24.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.65% < 6.00%; excess_return_120d -15.23% < 6.00%; excess_return_240d -33.39% < 8.00% |
| 300725.SZ | 药石科技 | ok | 24.91 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -2.17% < 6.00%; excess_return_120d -6.75% < 6.00%; excess_return_240d -24.43% < 8.00% |
| 603939.SH | 益丰药房 | ok | 24.91 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.82% < 6.00%; excess_return_120d -10.40% < 6.00%; excess_return_240d -37.43% < 8.00% |
| 688570.SH | 天玛智控 | ok | 24.90 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.28% < 6.00%; excess_return_120d -19.86% < 6.00%; excess_return_240d -44.27% < 8.00% |
| 300206.SZ | 理邦仪器 | ok | 24.89 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 0.97% < 6.00%; excess_return_120d -3.61% < 6.00%; excess_return_240d -14.76% < 8.00%; volatility_120d 43.37% > 42.00% |
| 600157.SH | 永泰能源 | ok | 24.89 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 0.00% < 6.00%; excess_return_120d -4.58% < 6.00%; excess_return_240d -9.75% < 8.00% |
| 603998.SH | 方盛制药 | ok | 24.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.15% < 6.00%; excess_return_120d -15.73% < 6.00%; excess_return_240d -22.42% < 8.00% |
| 300473.SZ | 德尔股份 | ok | 24.88 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 0.94% < 6.00%; excess_return_120d -3.64% < 6.00%; excess_return_240d -27.68% < 8.00%; volatility_120d 47.72% > 42.00% |
| 000931.SZ | 中关村 | ok | 24.88 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.34% < 6.00%; excess_return_120d -15.92% < 6.00%; excess_return_240d -42.49% < 8.00% |
| 688569.SH | 铁科轨道 | ok | 24.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.59% < 6.00%; excess_return_120d -24.17% < 6.00%; excess_return_240d -36.31% < 8.00% |
| 688557.SH | 兰剑智能 | ok | 24.86 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.77% < 6.00%; excess_return_120d -14.35% < 6.00%; excess_return_240d -12.44% < 8.00% |
| 688602.SH | 康鹏科技 | ok | 24.84 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.94% < 6.00%; excess_return_120d -15.52% < 6.00%; excess_return_240d -26.71% < 8.00%; volatility_120d 45.07% > 42.00% |
| 300498.SZ | 温氏股份 | ok | 24.84 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.69% < 6.00%; excess_return_120d -22.27% < 6.00%; excess_return_240d -38.74% < 8.00% |
| 600793.SH | 宜宾纸业 | ok | 24.82 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.54% < 6.00%; excess_return_120d -21.12% < 6.00%; excess_return_240d -63.36% < 8.00%; volatility_120d 47.73% > 42.00% |
| 600098.SH | 广州发展 | ok | 24.82 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -1.27% < 6.00%; excess_return_120d -5.85% < 6.00%; excess_return_240d -21.58% < 8.00% |
| 300636.SZ | 同和药业 | ok | 24.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.76% < 6.00%; excess_return_120d -12.34% < 6.00%; excess_return_240d -34.10% < 8.00% |
| 601019.SH | 山东出版 | ok | 24.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.93% < 6.00%; excess_return_120d -20.51% < 6.00%; excess_return_240d -43.49% < 8.00% |
| 688609.SH | 九联科技 | ok | 24.80 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -3.53% < 6.00%; excess_return_120d -8.11% < 6.00%; excess_return_240d -21.70% < 8.00%; volatility_120d 46.57% > 42.00% |
| 300381.SZ | 溢多利 | ok | 24.80 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.80% < 6.00%; excess_return_120d -11.38% < 6.00%; excess_return_240d -40.80% < 8.00% |
| 000958.SZ | 电投产融 | ok | 24.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.29% < 6.00%; excess_return_120d -17.87% < 6.00%; excess_return_240d -40.49% < 8.00% |
| 688329.SH | 艾隆科技 | ok | 24.77 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 3.32% < 6.00%; excess_return_120d -1.26% < 6.00%; excess_return_240d -6.02% < 8.00%; drawdown_120d -32.38% < -28.00%; volatility_120d 44.32% > 42.00% |
| 301267.SZ | 华厦眼科 | ok | 24.76 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.55% < 6.00%; excess_return_120d -19.13% < 6.00%; excess_return_240d -39.85% < 8.00% |
| 603700.SH | 宁水集团 | ok | 24.76 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.67% < 6.00%; excess_return_120d -20.25% < 6.00%; excess_return_240d -25.47% < 8.00% |
| 603229.SH | 奥翔药业 | ok | 24.76 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.52% < 6.00%; excess_return_120d -19.10% < 6.00%; excess_return_240d -26.77% < 8.00% |
| 002393.SZ | 力生制药 | ok | 24.76 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.63% < 6.00%; excess_return_120d -17.21% < 6.00%; excess_return_240d -22.66% < 8.00% |
| 688093.SH | 世华科技 | ok | 24.75 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.16% < 6.00%; excess_return_120d -17.74% < 6.00%; excess_return_240d -17.72% < 8.00%; volatility_120d 55.96% > 42.00% |
| 600168.SH | 武汉控股 | ok | 24.74 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.65% < 6.00%; excess_return_120d -20.23% < 6.00%; excess_return_240d -30.67% < 8.00% |
| 301606.SZ | 绿联科技 | ok | 24.74 | close_below_ma200; stock_return_120d -0.15% < 6.00%; excess_return_120d -4.73% < 6.00%; excess_return_240d 3.29% < 8.00%; drawdown_120d -37.18% < -28.00%; volatility_120d 60.32% > 42.00% |
| 600538.SH | 国发股份 | ok | 24.73 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.08% < 6.00%; excess_return_120d -8.67% < 6.00%; excess_return_240d -17.02% < 8.00% |
| 601162.SH | 天风证券 | ok | 24.73 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.74% < 6.00%; excess_return_120d -17.32% < 6.00%; excess_return_240d -48.35% < 8.00% |
| 688526.SH | 科前生物 | ok | 24.72 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.08% < 6.00%; excess_return_120d -15.66% < 6.00%; excess_return_240d -36.46% < 8.00% |
| 600221.SH | 海航控股 | ok | 24.71 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.76% < 6.00%; excess_return_120d -28.34% < 6.00%; excess_return_240d -19.63% < 8.00% |
| 601686.SH | 友发集团 | ok | 24.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.85% < 6.00%; excess_return_120d -20.43% < 6.00%; excess_return_240d -33.73% < 8.00% |
| 301507.SZ | 民生健康 | ok | 24.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.51% < 6.00%; excess_return_120d -21.09% < 6.00%; excess_return_240d -36.44% < 8.00% |
| 600826.SH | 兰生股份 | ok | 24.69 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.67% < 6.00%; excess_return_120d -12.25% < 6.00%; excess_return_240d 1.60% < 8.00%; volatility_120d 42.02% > 42.00% |
| 002471.SZ | 中超控股 | ok | 24.69 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.44% < 6.00%; excess_return_120d -30.02% < 6.00%; excess_return_240d 3.49% < 8.00%; drawdown_120d -44.99% < -28.00%; volatility_120d 74.46% > 42.00% |
| 603085.SH | 天成自控 | ok | 24.68 | close_below_ma200; stock_return_120d -7.00% < 6.00%; excess_return_120d -11.58% < 6.00%; excess_return_240d -24.51% < 8.00% |
| 301512.SZ | 智信精密 | ok | 24.64 | close_below_ma200; stock_return_120d 3.18% < 6.00%; excess_return_120d -1.40% < 6.00%; excess_return_240d -14.18% < 8.00%; volatility_120d 47.49% > 42.00% |
| 600927.SH | 永安期货 | ok | 24.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.25% < 6.00%; excess_return_120d -23.83% < 6.00%; excess_return_240d -45.51% < 8.00% |
| 688592.SH | 司南导航 | ok | 24.63 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 2.05% < 6.00%; excess_return_120d -2.53% < 6.00%; excess_return_240d -2.19% < 8.00%; volatility_120d 54.20% > 42.00% |
| 600031.SH | 三一重工 | ok | 24.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.60% < 6.00%; excess_return_120d -15.18% < 6.00%; excess_return_240d -20.41% < 8.00% |
| 600215.SH | 派斯林 | ok | 24.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.78% < 6.00%; excess_return_120d -8.36% < 6.00%; excess_return_240d -28.25% < 8.00%; volatility_120d 47.91% > 42.00% |
| 688198.SH | 佰仁医疗 | ok | 24.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.58% < 6.00%; excess_return_120d -17.16% < 6.00%; excess_return_240d -27.60% < 8.00%; volatility_120d 44.83% > 42.00% |
| 688389.SH | 普门科技 | ok | 24.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.16% < 6.00%; excess_return_120d -18.74% < 6.00%; excess_return_240d -35.99% < 8.00% |
| 301662.SZ | 宏工科技 | ok | 24.57 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 5.21% < 6.00%; excess_return_120d 0.63% < 6.00%; excess_return_240d -14.48% < 8.00%; drawdown_120d -39.29% < -28.00%; volatility_120d 74.14% > 42.00% |
| 688636.SH | 智明达 | ok | 24.57 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.76% < 6.00%; excess_return_120d -10.34% < 6.00%; excess_return_240d -6.92% < 8.00%; drawdown_120d -34.73% < -28.00%; volatility_120d 61.58% > 42.00% |
| 603456.SH | 九洲药业 | ok | 24.56 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.04% < 6.00%; excess_return_120d -18.63% < 6.00%; excess_return_240d -20.19% < 8.00% |
| 000529.SZ | 广弘控股 | ok | 24.55 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.86% < 6.00%; excess_return_120d -24.44% < 6.00%; excess_return_240d -43.97% < 8.00% |
| 300281.SZ | 金明精机 | ok | 24.55 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.83% < 6.00%; excess_return_120d -20.41% < 6.00%; excess_return_240d -29.26% < 8.00% |
| 301116.SZ | 益客食品 | ok | 24.54 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.19% < 6.00%; excess_return_120d -19.77% < 6.00%; excess_return_240d -38.26% < 8.00% |
| 001283.SZ | 豪鹏科技 | ok | 24.48 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -7.04% < 6.00%; excess_return_120d -11.62% < 6.00%; excess_return_240d -11.59% < 8.00%; volatility_120d 47.13% > 42.00% |
| 000042.SZ | 中洲控股 | ok | 24.47 | close_below_ma200; stock_return_120d 2.89% < 6.00%; excess_return_120d -1.69% < 6.00%; excess_return_240d -22.60% < 8.00%; volatility_120d 43.95% > 42.00% |
| 688314.SH | 康拓医疗 | ok | 24.47 | close_below_ma200; stock_return_120d 4.89% < 6.00%; excess_return_120d 0.31% < 6.00%; excess_return_240d -15.21% < 8.00%; drawdown_120d -41.08% < -28.00%; volatility_120d 52.72% > 42.00% |
| 300404.SZ | 博济医药 | ok | 24.44 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 1.86% < 6.00%; excess_return_120d -2.72% < 6.00%; excess_return_240d -22.91% < 8.00%; volatility_120d 46.97% > 42.00% |
| 600732.SH | 爱旭股份 | ok | 24.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -2.54% < 6.00%; excess_return_120d -7.12% < 6.00%; excess_return_240d -31.83% < 8.00%; volatility_120d 49.14% > 42.00% |
| 300415.SZ | 伊之密 | ok | 24.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.29% < 6.00%; excess_return_120d -18.87% < 6.00%; excess_return_240d -10.84% < 8.00% |
| 301023.SZ | 奕帆传动 | ok | 24.42 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.86% < 6.00%; excess_return_120d -9.44% < 6.00%; excess_return_240d -24.35% < 8.00%; drawdown_120d -36.90% < -28.00%; volatility_120d 60.79% > 42.00% |
| 301012.SZ | 扬电科技 | ok | 24.42 | close_below_ma200; stock_return_120d -9.88% < 6.00%; excess_return_120d -14.46% < 6.00%; excess_return_240d 4.00% < 8.00%; drawdown_120d -45.70% < -28.00%; volatility_120d 58.84% > 42.00% |
| 600516.SH | 方大炭素 | ok | 24.42 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.22% < 6.00%; excess_return_120d -7.80% < 6.00%; excess_return_240d -3.40% < 8.00%; volatility_120d 53.37% > 42.00% |
| 600812.SH | 华北制药 | ok | 24.41 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.56% < 6.00%; excess_return_120d -20.14% < 6.00%; excess_return_240d -47.97% < 8.00% |
| 002546.SZ | 新联电子 | ok | 24.41 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 0.58% < 6.00%; excess_return_120d -4.00% < 6.00%; excess_return_240d 2.30% < 8.00%; drawdown_120d -43.73% < -28.00%; volatility_120d 55.69% > 42.00% |
| 000920.SZ | 沃顿科技 | ok | 24.39 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.62% < 6.00%; excess_return_120d -5.20% < 6.00%; excess_return_240d -22.12% < 8.00%; volatility_120d 52.09% > 42.00% |
| 600358.SH | 国旅联合 | ok | 24.38 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.75% < 6.00%; excess_return_120d -13.85% < 6.00%; excess_return_240d -34.65% < 8.00% |
| 301181.SZ | 标榜股份 | ok | 24.38 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -29.67% < 6.00%; excess_return_120d -34.25% < 6.00%; excess_return_240d 5.30% < 8.00%; drawdown_120d -42.37% < -28.00%; volatility_120d 61.64% > 42.00% |
| 002127.SZ | 南极电商 | ok | 24.36 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.29% < 6.00%; excess_return_120d -17.87% < 6.00%; excess_return_240d -48.44% < 8.00% |
| 003017.SZ | 大洋生物 | ok | 24.33 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.99% < 6.00%; excess_return_120d -11.57% < 6.00%; excess_return_240d -15.07% < 8.00% |
| 600390.SH | 五矿资本 | ok | 24.31 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.48% < 6.00%; excess_return_120d -18.06% < 6.00%; excess_return_240d -41.53% < 8.00% |
| 300146.SZ | 汤臣倍健 | ok | 24.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.84% < 6.00%; excess_return_120d -24.42% < 6.00%; excess_return_240d -36.47% < 8.00% |
| 600787.SH | 中储股份 | ok | 24.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.56% < 6.00%; excess_return_120d -24.14% < 6.00%; excess_return_240d -44.28% < 8.00% |
| 600395.SH | 盘江股份 | ok | 24.27 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 3.00% < 6.00%; excess_return_120d -1.58% < 6.00%; excess_return_240d -20.04% < 8.00% |
| 002701.SZ | 奥瑞金 | ok | 24.27 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.27% < 6.00%; excess_return_120d -25.85% < 6.00%; excess_return_240d -42.64% < 8.00% |
| 688026.SH | 洁特生物 | ok | 24.26 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.96% < 6.00%; excess_return_120d -10.54% < 6.00%; excess_return_240d -31.35% < 8.00%; volatility_120d 51.87% > 42.00% |
| 301112.SZ | 信邦智能 | ok | 24.25 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.88% < 6.00%; excess_return_120d -16.46% < 6.00%; excess_return_240d -23.35% < 8.00%; volatility_120d 43.95% > 42.00% |
| 688488.SH | 艾迪药业 | ok | 24.24 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.08% < 6.00%; excess_return_120d -9.66% < 6.00%; excess_return_240d -11.56% < 8.00%; drawdown_120d -31.26% < -28.00%; volatility_120d 65.44% > 42.00% |
| 002511.SZ | 中顺洁柔 | ok | 24.22 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.83% < 6.00%; excess_return_120d -22.41% < 6.00%; excess_return_240d -18.40% < 8.00% |
| 603997.SH | 继峰股份 | ok | 24.20 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.42% < 6.00%; excess_return_120d -17.00% < 6.00%; excess_return_240d -20.46% < 8.00% |
| 605399.SH | 晨光新材 | ok | 24.20 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -2.44% < 6.00%; excess_return_120d -7.02% < 6.00%; excess_return_240d -17.97% < 8.00%; volatility_120d 50.95% > 42.00% |
| 000876.SZ | 新希望 | ok | 24.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.93% < 6.00%; excess_return_120d -25.51% < 6.00%; excess_return_240d -44.97% < 8.00% |
| 002406.SZ | 远东传动 | ok | 24.17 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.34% < 6.00%; excess_return_120d -15.92% < 6.00%; excess_return_240d -24.92% < 8.00% |
| 600567.SH | 山鹰国际 | ok | 24.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.34% < 6.00%; excess_return_120d -22.92% < 6.00%; excess_return_240d -49.96% < 8.00% |
| 605259.SH | 绿田机械 | ok | 24.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.31% < 6.00%; excess_return_120d -19.89% < 6.00%; excess_return_240d -25.69% < 8.00% |
| 603836.SH | 海程邦达 | ok | 24.16 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.99% < 6.00%; excess_return_120d -17.57% < 6.00%; excess_return_240d -44.23% < 8.00% |
| 000729.SZ | 燕京啤酒 | ok | 24.14 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -2.94% < 6.00%; excess_return_120d -7.52% < 6.00%; excess_return_240d -35.74% < 8.00% |
| 300583.SZ | 赛托生物 | ok | 24.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.72% < 6.00%; excess_return_120d -14.30% < 6.00%; excess_return_240d -48.69% < 8.00% |
| 603566.SH | 普莱柯 | ok | 24.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.30% < 6.00%; excess_return_120d -16.88% < 6.00%; excess_return_240d -41.06% < 8.00% |
| 300070.SZ | 碧水源 | ok | 24.12 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.22% < 6.00%; excess_return_120d -19.80% < 6.00%; excess_return_240d -48.07% < 8.00% |
| 603207.SH | 小方制药 | ok | 24.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.89% < 6.00%; excess_return_120d -20.47% < 6.00%; excess_return_240d -48.46% < 8.00% |
| 002333.SZ | 罗普斯金 | ok | 24.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.41% < 6.00%; excess_return_120d -15.99% < 6.00%; excess_return_240d -32.98% < 8.00% |
| 600292.SH | 电投水电 | ok | 24.09 | close_below_ma200; stock_return_120d -2.22% < 6.00%; excess_return_120d -6.81% < 6.00%; excess_return_240d -16.39% < 8.00% |
| 688315.SH | 诺禾致源 | ok | 24.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 1.54% < 6.00%; excess_return_120d -3.04% < 6.00%; excess_return_240d -28.95% < 8.00%; volatility_120d 43.27% > 42.00% |
| 002235.SZ | 安妮股份 | ok | 24.08 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.64% < 6.00%; excess_return_120d -15.22% < 6.00%; excess_return_240d -43.56% < 8.00%; volatility_120d 61.20% > 42.00% |
| 603237.SH | 五芳斋 | ok | 24.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.20% < 6.00%; excess_return_120d -22.78% < 6.00%; excess_return_240d -41.31% < 8.00% |
| 688238.SH | 和元生物 | ok | 24.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -4.65% < 6.00%; excess_return_120d -9.23% < 6.00%; excess_return_240d -26.74% < 8.00%; volatility_120d 45.69% > 42.00% |
| 605009.SH | 豪悦护理 | ok | 24.06 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.13% < 6.00%; excess_return_120d -23.71% < 6.00%; excess_return_240d -60.10% < 8.00% |
| 605189.SH | 富春染织 | ok | 24.05 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -2.61% < 6.00%; excess_return_120d -7.19% < 6.00%; excess_return_240d -1.23% < 8.00%; volatility_120d 54.68% > 42.00% |
| 605277.SH | 新亚电子 | ok | 24.04 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.57% < 6.00%; excess_return_120d -8.15% < 6.00%; excess_return_240d -26.83% < 8.00%; volatility_120d 49.76% > 42.00% |
| 603198.SH | 迎驾贡酒 | ok | 24.03 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.08% < 6.00%; excess_return_120d -18.66% < 6.00%; excess_return_240d -35.23% < 8.00% |
| 002927.SZ | 泰永长征 | ok | 24.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.46% < 6.00%; excess_return_120d -14.04% < 6.00%; excess_return_240d 0.26% < 8.00%; drawdown_120d -29.29% < -28.00%; volatility_120d 62.88% > 42.00% |
| 002437.SZ | 誉衡药业 | ok | 24.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -1.30% < 6.00%; excess_return_120d -5.88% < 6.00%; excess_return_240d -17.33% < 8.00%; volatility_120d 42.50% > 42.00% |
| 600508.SH | 上海能源 | ok | 23.99 | close_below_ma200; stock_return_120d 0.16% < 6.00%; excess_return_120d -4.42% < 6.00%; excess_return_240d -19.62% < 8.00% |
| 002182.SZ | 宝武镁业 | ok | 23.99 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.05% < 6.00%; excess_return_120d -8.63% < 6.00%; excess_return_240d 1.24% < 8.00%; drawdown_120d -36.56% < -28.00%; volatility_120d 53.27% > 42.00% |
| 300298.SZ | 三诺生物 | ok | 23.98 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.74% < 6.00%; excess_return_120d -17.32% < 6.00%; excess_return_240d -53.23% < 8.00% |
| 300999.SZ | 金龙鱼 | ok | 23.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.98% < 6.00%; excess_return_120d -17.56% < 6.00%; excess_return_240d -36.74% < 8.00% |
| 300175.SZ | 朗源股份 | ok | 23.96 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.91% < 6.00%; excess_return_120d -9.01% < 6.00%; excess_return_240d -10.36% < 8.00%; volatility_120d 45.96% > 42.00% |
| 002755.SZ | 奥赛康 | ok | 23.96 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.35% < 6.00%; excess_return_120d -10.93% < 6.00%; excess_return_240d -39.00% < 8.00%; volatility_120d 45.65% > 42.00% |
| 601369.SH | 陕鼓动力 | ok | 23.93 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.40% < 6.00%; excess_return_120d -13.76% < 6.00%; excess_return_240d -13.18% < 8.00% |
| 002615.SZ | 哈尔斯 | ok | 23.92 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -2.61% < 6.00%; excess_return_120d -7.19% < 6.00%; excess_return_240d -34.54% < 8.00%; volatility_120d 45.81% > 42.00% |
| 002078.SZ | 太阳纸业 | ok | 23.91 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.36% < 6.00%; excess_return_120d -21.94% < 6.00%; excess_return_240d -21.87% < 8.00% |
| 002408.SZ | 齐翔腾达 | ok | 23.90 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 2.66% < 6.00%; excess_return_120d -1.92% < 6.00%; excess_return_240d -14.27% < 8.00%; drawdown_120d -29.93% < -28.00%; volatility_120d 44.97% > 42.00% |
| 605028.SH | 世茂能源 | ok | 23.88 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.08% < 6.00%; excess_return_120d -17.57% < 6.00%; excess_return_240d 2.56% < 8.00%; drawdown_120d -34.30% < -28.00%; volatility_120d 52.49% > 42.00% |
| 601099.SH | 太平洋 | ok | 23.86 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.33% < 6.00%; excess_return_120d -19.91% < 6.00%; excess_return_240d -32.77% < 8.00% |
| 000726.SZ | 鲁泰A | ok | 23.86 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.36% < 6.00%; excess_return_120d -21.94% < 6.00%; excess_return_240d -29.81% < 8.00% |
| 301065.SZ | 本立科技 | ok | 23.86 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.01% < 6.00%; excess_return_120d -14.59% < 6.00%; excess_return_240d -40.52% < 8.00% |
| 688443.SH | 智翔金泰 | ok | 23.85 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.24% < 6.00%; excess_return_120d -10.82% < 6.00%; excess_return_240d -32.66% < 8.00%; volatility_120d 46.54% > 42.00% |
| 300292.SZ | 吴通控股 | ok | 23.85 | close_below_ma200; stock_return_120d 2.88% < 6.00%; excess_return_120d -1.70% < 6.00%; excess_return_240d -26.40% < 8.00%; drawdown_120d -36.78% < -28.00%; volatility_120d 58.77% > 42.00% |
| 601058.SH | 赛轮轮胎 | ok | 23.85 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.06% < 6.00%; excess_return_120d -23.64% < 6.00%; excess_return_240d -22.02% < 8.00% |
| 301007.SZ | 德迈仕 | ok | 23.84 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.65% < 6.00%; excess_return_120d -18.23% < 6.00%; excess_return_240d -6.84% < 8.00%; volatility_120d 51.09% > 42.00% |
| 300357.SZ | 我武生物 | ok | 23.84 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.19% < 6.00%; excess_return_120d -18.77% < 6.00%; excess_return_240d -6.76% < 8.00% |
| 688708.SH | 佳驰科技 | ok | 23.84 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.31% < 6.00%; excess_return_120d -16.89% < 6.00%; excess_return_240d -24.50% < 8.00%; volatility_120d 43.13% > 42.00% |
| 301260.SZ | 格力博 | ok | 23.83 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.31% < 6.00%; excess_return_120d -17.89% < 6.00%; excess_return_240d -48.54% < 8.00% |
| 300733.SZ | 西菱动力 | ok | 23.80 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.27% < 6.00%; excess_return_120d -15.85% < 6.00%; excess_return_240d -30.49% < 8.00%; volatility_120d 50.63% > 42.00% |
| 002633.SZ | 申科股份 | ok | 23.78 | close_below_ma200; stock_return_120d -3.95% < 6.00%; excess_return_120d -8.53% < 6.00%; excess_return_240d -12.45% < 8.00% |
| 002131.SZ | 利欧股份 | ok | 23.77 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.42% < 6.00%; excess_return_120d -20.39% < 6.00%; excess_return_240d 5.13% < 8.00%; drawdown_120d -58.73% < -28.00%; volatility_120d 69.84% > 42.00% |
| 603299.SH | 苏盐井神 | ok | 23.76 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.21% < 6.00%; excess_return_120d -14.79% < 6.00%; excess_return_240d -23.43% < 8.00% |
| 601568.SH | 北元化工 | ok | 23.75 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.09% < 6.00%; excess_return_120d -8.67% < 6.00%; excess_return_240d -36.68% < 8.00% |
| 601319.SH | 中国人保 | ok | 23.74 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.32% < 6.00%; excess_return_120d -22.90% < 6.00%; excess_return_240d -34.77% < 8.00%; drawdown_120d -28.19% < -28.00% |
| 300485.SZ | 赛升药业 | ok | 23.74 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.59% < 6.00%; excess_return_120d -10.17% < 6.00%; excess_return_240d -51.35% < 8.00%; volatility_120d 51.34% > 42.00% |
| 603605.SH | 珀莱雅 | ok | 23.74 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.05% < 6.00%; excess_return_120d -18.63% < 6.00%; excess_return_240d -48.71% < 8.00% |
| 300572.SZ | 安车检测 | ok | 23.74 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -8.55% < 6.00%; excess_return_120d -13.13% < 6.00%; excess_return_240d 1.77% < 8.00%; drawdown_120d -28.67% < -28.00%; volatility_120d 51.25% > 42.00% |
| 600653.SH | 申华控股 | ok | 23.73 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.42% < 6.00%; excess_return_120d -23.00% < 6.00%; excess_return_240d -40.79% < 8.00% |
| 002116.SZ | 中国海诚 | ok | 23.73 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.63% < 6.00%; excess_return_120d -21.21% < 6.00%; excess_return_240d -38.05% < 8.00% |
| 301296.SZ | 新巨丰 | ok | 23.72 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.54% < 6.00%; excess_return_120d -23.12% < 6.00%; excess_return_240d -48.96% < 8.00% |
| 688739.SH | 成大生物 | ok | 23.71 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.77% < 6.00%; excess_return_120d -25.35% < 6.00%; excess_return_240d -43.53% < 8.00% |
| 301080.SZ | 百普赛斯 | ok | 23.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.12% < 6.00%; excess_return_120d -11.70% < 6.00%; excess_return_240d -18.68% < 8.00%; drawdown_120d -30.03% < -28.00%; volatility_120d 50.21% > 42.00% |
| 603711.SH | 香飘飘 | ok | 23.68 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -11.75% < 6.00%; excess_return_120d -16.33% < 6.00%; excess_return_240d -36.15% < 8.00% |
| 600227.SH | 赤天化 | ok | 23.67 | close_below_ma200; stock_return_120d 5.04% < 6.00%; excess_return_120d 0.46% < 6.00%; excess_return_240d -20.29% < 8.00%; drawdown_120d -53.70% < -28.00%; volatility_120d 69.97% > 42.00% |
| 301381.SZ | 赛维时代 | ok | 23.66 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.15% < 6.00%; excess_return_120d -10.73% < 6.00%; excess_return_240d -23.40% < 8.00%; volatility_120d 44.90% > 42.00% |
| 002282.SZ | 博深股份 | ok | 23.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.75% < 6.00%; excess_return_120d -23.33% < 6.00%; excess_return_240d -42.78% < 8.00% |
| 000727.SZ | 冠捷科技 | ok | 23.65 | close_below_ma200; stock_return_120d -4.72% < 6.00%; excess_return_120d -9.30% < 6.00%; excess_return_240d -21.92% < 8.00%; volatility_120d 48.70% > 42.00% |
| 300718.SZ | 长盛轴承 | ok | 23.63 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.13% < 6.00%; excess_return_120d -21.71% < 6.00%; excess_return_240d -15.80% < 8.00%; volatility_120d 52.29% > 42.00% |
| 301198.SZ | 喜悦智行 | ok | 23.63 | close_below_ma200; stock_return_120d 2.71% < 6.00%; excess_return_120d -1.87% < 6.00%; excess_return_240d -7.94% < 8.00%; drawdown_120d -33.68% < -28.00%; volatility_120d 50.33% > 42.00% |
| 600830.SH | 香溢融通 | ok | 23.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.78% < 6.00%; excess_return_120d -19.36% < 6.00%; excess_return_240d -42.62% < 8.00% |
| 000428.SZ | 华天酒店 | ok | 23.62 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.45% < 6.00%; excess_return_120d -10.03% < 6.00%; excess_return_240d -28.79% < 8.00% |
| 000155.SZ | 川能动力 | ok | 23.61 | close_below_ma200; stock_return_120d 3.09% < 6.00%; excess_return_120d -1.49% < 6.00%; excess_return_240d -0.15% < 8.00%; drawdown_120d -37.90% < -28.00%; volatility_120d 51.59% > 42.00% |
| 000963.SZ | 华东医药 | ok | 23.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.69% < 6.00%; excess_return_120d -26.27% < 6.00%; excess_return_240d -41.60% < 8.00% |
| 301017.SZ | 漱玉平民 | ok | 23.58 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.97% < 6.00%; excess_return_120d -11.55% < 6.00%; excess_return_240d -12.91% < 8.00%; drawdown_120d -40.43% < -28.00%; volatility_120d 57.55% > 42.00% |
| 600455.SH | 博通股份 | ok | 23.57 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.74% < 6.00%; excess_return_120d -16.32% < 6.00%; excess_return_240d -40.08% < 8.00% |
| 605151.SH | 西上海 | ok | 23.57 | close_below_ma200; stock_return_120d 1.01% < 6.00%; excess_return_120d -3.57% < 6.00%; excess_return_240d -20.83% < 8.00%; drawdown_120d -28.35% < -28.00%; volatility_120d 46.09% > 42.00% |
| 000887.SZ | 中鼎股份 | ok | 23.57 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.12% < 6.00%; excess_return_120d -23.70% < 6.00%; excess_return_240d -11.84% < 8.00%; volatility_120d 43.49% > 42.00% |
| 600587.SH | 新华医疗 | ok | 23.57 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.22% < 6.00%; excess_return_120d -17.80% < 6.00%; excess_return_240d -37.19% < 8.00% |
| 603341.SH | 龙旗科技 | ok | 23.56 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.92% < 6.00%; excess_return_120d -10.50% < 6.00%; excess_return_240d -19.39% < 8.00% |
| 603333.SH | 尚纬股份 | ok | 23.55 | close_below_ma200; stock_return_120d -6.95% < 6.00%; excess_return_120d -11.53% < 6.00%; excess_return_240d -27.14% < 8.00%; volatility_120d 47.84% > 42.00% |
| 301336.SZ | 趣睡科技 | ok | 23.51 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.62% < 6.00%; excess_return_120d -8.20% < 6.00%; excess_return_240d -30.86% < 8.00%; volatility_120d 44.95% > 42.00% |
| 002426.SZ | 胜利精密 | ok | 23.51 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.57% < 6.00%; excess_return_120d -12.15% < 6.00%; excess_return_240d -9.43% < 8.00%; volatility_120d 60.08% > 42.00% |
| 301585.SZ | 蓝宇股份 | ok | 23.51 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.30% < 6.00%; excess_return_120d -19.88% < 6.00%; excess_return_240d -45.68% < 8.00% |
| 688091.SH | 上海谊众 | ok | 23.49 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d 2.36% < 6.00%; excess_return_120d -2.22% < 6.00%; excess_return_240d -41.47% < 8.00%; volatility_120d 65.45% > 42.00% |
| 600903.SH | 贵州燃气 | ok | 23.49 | close_below_ma200; stock_return_120d 1.27% < 6.00%; excess_return_120d -3.31% < 6.00%; excess_return_240d -24.45% < 8.00%; drawdown_120d -37.25% < -28.00%; volatility_120d 52.46% > 42.00% |
| 002381.SZ | 双箭股份 | ok | 23.49 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.87% < 6.00%; excess_return_120d -20.45% < 6.00%; excess_return_240d -39.97% < 8.00% |
| 300200.SZ | 高盟新材 | ok | 23.47 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.43% < 6.00%; excess_return_120d -13.01% < 6.00%; excess_return_240d -13.42% < 8.00%; drawdown_120d -33.71% < -28.00%; volatility_120d 61.73% > 42.00% |
| 600312.SH | 平高电气 | ok | 23.47 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 2.52% < 6.00%; excess_return_120d -2.06% < 6.00%; excess_return_240d -4.58% < 8.00%; drawdown_120d -30.84% < -28.00%; volatility_120d 43.83% > 42.00% |
| 600883.SH | 博闻科技 | ok | 23.47 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.53% < 6.00%; excess_return_120d -14.11% < 6.00%; excess_return_240d -31.52% < 8.00% |
| 002091.SZ | 江苏国泰 | ok | 23.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.23% < 6.00%; excess_return_120d -19.82% < 6.00%; excess_return_240d -12.75% < 8.00% |
| 688068.SH | 热景生物 | ok | 23.45 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.67% < 6.00%; excess_return_120d -21.25% < 6.00%; excess_return_240d -43.35% < 8.00%; drawdown_120d -37.14% < -28.00%; volatility_120d 75.14% > 42.00% |
| 002012.SZ | 凯恩股份 | ok | 23.45 | close_below_ma200; stock_return_120d -2.63% < 6.00%; excess_return_120d -7.21% < 6.00%; excess_return_240d -7.88% < 8.00%; drawdown_120d -35.13% < -28.00%; volatility_120d 48.08% > 42.00% |
| 600132.SH | 重庆啤酒 | ok | 23.43 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.46% < 6.00%; excess_return_120d -20.04% < 6.00%; excess_return_240d -39.23% < 8.00% |
| 301595.SZ | 太力科技 | ok | 23.43 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.77% < 6.00%; excess_return_120d -13.35% < 6.00%; excess_return_240d -6.80% < 8.00%; drawdown_120d -35.41% < -28.00%; volatility_120d 57.39% > 42.00% |
| 000950.SZ | 重药控股 | ok | 23.41 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.44% < 6.00%; excess_return_120d -11.02% < 6.00%; excess_return_240d -13.96% < 8.00%; volatility_120d 42.79% > 42.00% |
| 600605.SH | 汇通能源 | ok | 23.40 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -9.48% < 6.00%; excess_return_120d -14.06% < 6.00%; excess_return_240d -47.46% < 8.00%; volatility_120d 46.53% > 42.00% |
| 688520.SH | 神州细胞 | ok | 23.40 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.10% < 6.00%; excess_return_120d -12.68% < 6.00%; excess_return_240d -70.83% < 8.00%; volatility_120d 43.95% > 42.00% |
| 300388.SZ | 节能国祯 | ok | 23.38 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.65% < 6.00%; excess_return_120d -18.23% < 6.00%; excess_return_240d -24.40% < 8.00% |
| 300354.SZ | 东华测试 | ok | 23.38 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.89% < 6.00%; excess_return_120d -21.47% < 6.00%; excess_return_240d -20.35% < 8.00%; volatility_120d 46.11% > 42.00% |
| 002461.SZ | 珠江啤酒 | ok | 23.37 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.52% < 6.00%; excess_return_120d -18.10% < 6.00%; excess_return_240d -48.96% < 8.00% |
| 002722.SZ | 物产金轮 | ok | 23.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.19% < 6.00%; excess_return_120d -20.77% < 6.00%; excess_return_240d -42.57% < 8.00% |
| 002758.SZ | 浙农股份 | ok | 23.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.57% < 6.00%; excess_return_120d -23.15% < 6.00%; excess_return_240d -31.48% < 8.00% |
| 301329.SZ | 信音电子 | ok | 23.35 | close_below_ma200; stock_return_120d -3.93% < 6.00%; excess_return_120d -8.52% < 6.00%; excess_return_240d -7.58% < 8.00%; drawdown_120d -32.19% < -28.00%; volatility_120d 59.10% > 42.00% |
| 688425.SH | 铁建重工 | ok | 23.33 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.95% < 6.00%; excess_return_120d -22.53% < 6.00%; excess_return_240d -17.49% < 8.00% |
| 300996.SZ | 普联软件 | ok | 23.32 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.88% < 6.00%; excess_return_120d -8.46% < 6.00%; excess_return_240d -18.75% < 8.00%; volatility_120d 50.00% > 42.00% |
| 600621.SH | 华鑫股份 | ok | 23.32 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.99% < 6.00%; excess_return_120d -17.57% < 6.00%; excess_return_240d -33.53% < 8.00% |
| 300470.SZ | 中密控股 | ok | 23.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.76% < 6.00%; excess_return_120d -23.34% < 6.00%; excess_return_240d -37.09% < 8.00% |
| 002206.SZ | 海利得 | ok | 23.30 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.91% < 6.00%; excess_return_120d -8.49% < 6.00%; excess_return_240d -21.66% < 8.00% |
| 301059.SZ | 金三江 | ok | 23.29 | close_below_ma200; stock_return_120d -1.62% < 6.00%; excess_return_120d -6.20% < 6.00%; excess_return_240d -16.47% < 8.00%; volatility_120d 45.17% > 42.00% |
| 002414.SZ | 高德红外 | ok | 23.29 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.02% < 6.00%; excess_return_120d -20.60% < 6.00%; excess_return_240d 1.49% < 8.00%; drawdown_120d -33.83% < -28.00% |
| 601618.SH | 中国中冶 | ok | 23.27 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.14% < 6.00%; excess_return_120d -18.72% < 6.00%; excess_return_240d -35.35% < 8.00% |
| 600685.SH | 中船防务 | ok | 23.26 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.53% < 6.00%; excess_return_120d -9.11% < 6.00%; excess_return_240d -20.50% < 8.00%; drawdown_120d -29.55% < -28.00% |
| 000722.SZ | 湖南发展 | ok | 23.26 | close_below_ma200; stock_return_120d 2.38% < 6.00%; excess_return_120d -2.20% < 6.00%; excess_return_240d -33.03% < 8.00%; drawdown_120d -38.75% < -28.00%; volatility_120d 57.34% > 42.00% |
| 300119.SZ | 瑞普生物 | ok | 23.25 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.00% < 6.00%; excess_return_120d -17.58% < 6.00%; excess_return_240d -38.07% < 8.00% |
| 000720.SZ | 新能泰山 | ok | 23.25 | close_below_ma200; stock_return_120d 4.89% < 6.00%; excess_return_120d 0.31% < 6.00%; excess_return_240d -29.14% < 8.00%; drawdown_120d -52.23% < -28.00%; volatility_120d 75.44% > 42.00% |
| 600433.SH | 冠豪高新 | ok | 23.25 | close_below_ma200; stock_return_120d 0.91% < 6.00%; excess_return_120d -3.67% < 6.00%; excess_return_240d -16.68% < 8.00%; drawdown_120d -38.25% < -28.00%; volatility_120d 51.44% > 42.00% |
| 600846.SH | 同济科技 | ok | 23.24 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.93% < 6.00%; excess_return_120d -17.51% < 6.00%; excess_return_240d -16.35% < 8.00%; volatility_120d 43.00% > 42.00% |
| 001201.SZ | 东瑞股份 | ok | 23.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.70% < 6.00%; excess_return_120d -24.28% < 6.00%; excess_return_240d -49.58% < 8.00% |
| 603551.SH | 奥普科技 | ok | 23.22 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.41% < 6.00%; excess_return_120d -17.99% < 6.00%; excess_return_240d -26.72% < 8.00% |
| 002481.SZ | 双塔食品 | ok | 23.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.92% < 6.00%; excess_return_120d -26.50% < 6.00%; excess_return_240d -50.35% < 8.00% |
| 603309.SH | 维力医疗 | ok | 23.18 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.33% < 6.00%; excess_return_120d -11.91% < 6.00%; excess_return_240d -23.43% < 8.00% |
| 603153.SH | 上海建科 | ok | 23.18 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.65% < 6.00%; excess_return_120d -25.23% < 6.00%; excess_return_240d -42.75% < 8.00% |
| 600817.SH | 宇通重工 | ok | 23.16 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.50% < 6.00%; excess_return_120d -20.08% < 6.00%; excess_return_240d -38.84% < 8.00% |
| 600710.SH | 苏美达 | ok | 23.15 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 0.24% < 6.00%; excess_return_120d -4.34% < 6.00%; excess_return_240d -8.02% < 8.00%; drawdown_120d -29.57% < -28.00%; volatility_120d 44.35% > 42.00% |
| 300573.SZ | 兴齐眼药 | ok | 23.14 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.58% < 6.00%; excess_return_120d -16.17% < 6.00%; excess_return_240d -0.60% < 8.00% |
| 603183.SH | 建研院 | ok | 23.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.96% < 6.00%; excess_return_120d -16.54% < 6.00%; excess_return_240d -33.47% < 8.00% |
| 002456.SZ | 欧菲光 | ok | 23.12 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.78% < 6.00%; excess_return_120d -19.36% < 6.00%; excess_return_240d -42.33% < 8.00%; volatility_120d 43.38% > 42.00% |
| 600335.SH | 国机汽车 | ok | 23.12 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.51% < 6.00%; excess_return_120d -26.09% < 6.00%; excess_return_240d -41.87% < 8.00%; drawdown_120d -29.52% < -28.00% |
| 605005.SH | 合兴股份 | ok | 23.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.81% < 6.00%; excess_return_120d -21.39% < 6.00%; excess_return_240d -34.43% < 8.00% |
| 605088.SH | 冠盛股份 | ok | 23.10 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.02% < 6.00%; excess_return_120d -15.60% < 6.00%; excess_return_240d -35.59% < 8.00% |
| 301020.SZ | 密封科技 | ok | 23.10 | close_below_ma200; stock_return_120d -0.64% < 6.00%; excess_return_120d -5.22% < 6.00%; excess_return_240d -22.32% < 8.00%; drawdown_120d -37.43% < -28.00%; volatility_120d 50.44% > 42.00% |
| 603365.SH | 水星家纺 | ok | 23.09 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.83% < 6.00%; excess_return_120d -17.41% < 6.00%; excess_return_240d -18.41% < 8.00%; drawdown_120d -28.18% < -28.00% |
| 600059.SH | 古越龙山 | ok | 23.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.92% < 6.00%; excess_return_120d -20.50% < 6.00%; excess_return_240d -47.03% < 8.00%; drawdown_120d -28.61% < -28.00% |
| 603707.SH | 健友股份 | ok | 23.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.78% < 6.00%; excess_return_120d -19.36% < 6.00%; excess_return_240d -51.47% < 8.00% |
| 600771.SH | 广誉远 | ok | 23.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.69% < 6.00%; excess_return_120d -25.27% < 6.00%; excess_return_240d -50.05% < 8.00% |
| 603048.SH | 浙江黎明 | ok | 23.06 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.04% < 6.00%; excess_return_120d -12.62% < 6.00%; excess_return_240d -10.40% < 8.00%; volatility_120d 42.20% > 42.00% |
| 603173.SH | 福斯达 | ok | 23.04 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.12% < 6.00%; excess_return_120d -14.70% < 6.00%; excess_return_240d -17.25% < 8.00% |
| 600579.SH | 中化装备 | ok | 23.04 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.72% < 6.00%; excess_return_120d -15.30% < 6.00%; excess_return_240d -27.16% < 8.00%; volatility_120d 44.23% > 42.00% |
| 301598.SZ | 博科测试 | ok | 23.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.41% < 6.00%; excess_return_120d -18.99% < 6.00%; excess_return_240d -34.25% < 8.00% |
| 301587.SZ | 中瑞股份 | ok | 23.00 | close_below_ma200; stock_return_120d -2.82% < 6.00%; excess_return_120d -7.40% < 6.00%; excess_return_240d -19.42% < 8.00%; volatility_120d 45.94% > 42.00% |
| 002404.SZ | 嘉欣丝绸 | ok | 23.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.52% < 6.00%; excess_return_120d -17.10% < 6.00%; excess_return_240d -26.11% < 8.00% |
| 600085.SH | 同仁堂 | ok | 23.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.35% < 6.00%; excess_return_120d -29.93% < 6.00%; excess_return_240d -53.60% < 8.00% |
| 600651.SH | 飞乐音响 | ok | 22.99 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.73% < 6.00%; excess_return_120d -28.31% < 6.00%; excess_return_240d 4.13% < 8.00%; drawdown_120d -40.53% < -28.00% |
| 300239.SZ | 东宝生物 | ok | 22.98 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.13% < 6.00%; excess_return_120d -17.71% < 6.00%; excess_return_240d -33.02% < 8.00% |
| 600009.SH | 上海机场 | ok | 22.98 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.46% < 6.00%; excess_return_120d -33.04% < 6.00%; excess_return_240d -45.66% < 8.00%; drawdown_120d -29.40% < -28.00% |
| 688114.SH | 华大智造 | ok | 22.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.04% < 6.00%; excess_return_120d -11.62% < 6.00%; excess_return_240d -30.12% < 8.00%; drawdown_120d -31.85% < -28.00%; volatility_120d 52.86% > 42.00% |
| 603458.SH | 勘设股份 | ok | 22.97 | close_below_ma200; stock_return_120d -0.70% < 6.00%; excess_return_120d -5.28% < 6.00%; excess_return_240d -6.86% < 8.00%; drawdown_120d -39.88% < -28.00%; volatility_120d 60.69% > 42.00% |
| 301353.SZ | 普莱得 | ok | 22.96 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.19% < 6.00%; excess_return_120d -17.77% < 6.00%; excess_return_240d -30.73% < 8.00% |
| 300992.SZ | 泰福泵业 | ok | 22.95 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.11% < 6.00%; excess_return_120d -4.60% < 6.00%; excess_return_240d -19.44% < 8.00%; drawdown_120d -36.20% < -28.00%; volatility_120d 56.89% > 42.00% |
| 603697.SH | 有友食品 | ok | 22.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.69% < 6.00%; excess_return_120d -17.27% < 6.00%; excess_return_240d -36.65% < 8.00%; volatility_120d 42.34% > 42.00% |
| 002388.SZ | 新亚制程 | ok | 22.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.54% < 6.00%; excess_return_120d -22.64% < 6.00%; excess_return_240d -9.89% < 8.00%; volatility_120d 48.05% > 42.00% |
| 601136.SH | 首创证券 | ok | 22.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.09% < 6.00%; excess_return_120d -26.67% < 6.00%; excess_return_240d -46.15% < 8.00% |
| 603860.SH | 中公高科 | ok | 22.94 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.97% < 6.00%; excess_return_120d -20.55% < 6.00%; excess_return_240d -39.75% < 8.00% |
| 301479.SZ | 弘景光电 | ok | 22.94 | close_below_ma200; stock_return_120d 0.57% < 6.00%; excess_return_120d -4.01% < 6.00%; excess_return_240d -16.38% < 8.00%; drawdown_120d -38.07% < -28.00%; volatility_120d 56.68% > 42.00% |
| 600037.SH | 歌华有线 | ok | 22.94 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.72% < 6.00%; excess_return_120d -16.30% < 6.00%; excess_return_240d -37.55% < 8.00% |
| 600198.SH | 大唐电信 | ok | 22.93 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.16% < 6.00%; excess_return_120d -17.74% < 6.00%; excess_return_240d -21.93% < 8.00%; drawdown_120d -32.85% < -28.00%; volatility_120d 58.93% > 42.00% |
| 605488.SH | 福莱新材 | ok | 22.93 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.50% < 6.00%; excess_return_120d -9.08% < 6.00%; excess_return_240d -11.76% < 8.00%; drawdown_120d -32.70% < -28.00%; volatility_120d 65.48% > 42.00% |
| 000709.SZ | 河钢股份 | ok | 22.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.55% < 6.00%; excess_return_120d -17.13% < 6.00%; excess_return_240d -34.03% < 8.00% |
| 600590.SH | 泰豪科技 | ok | 22.92 | close_below_ma200; stock_return_120d 4.83% < 6.00%; excess_return_120d 0.25% < 6.00%; excess_return_240d -13.99% < 8.00%; drawdown_120d -46.92% < -28.00%; volatility_120d 73.31% > 42.00% |
| 603041.SH | 美思德 | ok | 22.92 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.06% < 6.00%; excess_return_120d -14.64% < 6.00%; excess_return_240d -31.53% < 8.00% |
| 603719.SH | 良品铺子 | ok | 22.91 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.60% < 6.00%; excess_return_120d -25.18% < 6.00%; excess_return_240d -46.28% < 8.00% |
| 001279.SZ | 强邦新材 | ok | 22.90 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.10% < 6.00%; excess_return_120d -21.68% < 6.00%; excess_return_240d -49.76% < 8.00% |
| 000778.SZ | 新兴铸管 | ok | 22.90 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.89% < 6.00%; excess_return_120d -12.47% < 6.00%; excess_return_240d -17.60% < 8.00% |
| 300267.SZ | 尔康制药 | ok | 22.90 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 1.76% < 6.00%; excess_return_120d -2.82% < 6.00%; excess_return_240d -17.82% < 8.00%; drawdown_120d -32.09% < -28.00%; volatility_120d 59.17% > 42.00% |
| 601096.SH | 宏盛华源 | ok | 22.89 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 4.17% < 6.00%; excess_return_120d -0.41% < 6.00%; excess_return_240d -20.96% < 8.00%; drawdown_120d -41.40% < -28.00%; volatility_120d 47.32% > 42.00% |
| 001336.SZ | 楚环科技 | ok | 22.89 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.91% < 6.00%; excess_return_120d -11.49% < 6.00%; excess_return_240d -15.98% < 8.00% |
| 001288.SZ | 运机集团 | ok | 22.89 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.58% < 6.00%; excess_return_120d -27.16% < 6.00%; excess_return_240d 2.61% < 8.00%; drawdown_120d -39.74% < -28.00%; volatility_120d 52.39% > 42.00% |
| 300867.SZ | 圣元环保 | ok | 22.89 | close_below_ma200; stock_return_120d -3.79% < 6.00%; excess_return_120d -8.37% < 6.00%; excess_return_240d -24.98% < 8.00%; volatility_120d 44.61% > 42.00% |
| 000695.SZ | 滨海能源 | ok | 22.88 | close_below_ma200; stock_return_120d -2.91% < 6.00%; excess_return_120d -7.49% < 6.00%; excess_return_240d -25.07% < 8.00%; volatility_120d 52.28% > 42.00% |
| 001208.SZ | 华菱线缆 | ok | 22.87 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -41.73% < 6.00%; excess_return_120d -46.31% < 6.00%; excess_return_240d 3.69% < 8.00%; drawdown_120d -56.12% < -28.00%; volatility_120d 62.36% > 42.00% |
| 002270.SZ | 华明装备 | ok | 22.85 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.02% < 6.00%; excess_return_120d -24.60% < 6.00%; excess_return_240d 4.02% < 8.00%; drawdown_120d -47.46% < -28.00%; volatility_120d 54.90% > 42.00% |
| 600575.SH | 淮河能源 | ok | 22.85 | close_below_ma200; stock_return_120d -4.05% < 6.00%; excess_return_120d -8.63% < 6.00%; excess_return_240d -32.34% < 8.00%; drawdown_120d -29.84% < -28.00% |
| 300103.SZ | 达刚控股 | ok | 22.83 | close_below_ma200; stock_return_120d -10.09% < 6.00%; excess_return_120d -14.67% < 6.00%; excess_return_240d -13.66% < 8.00%; volatility_120d 53.77% > 42.00% |
| 603665.SH | 康隆达 | ok | 22.83 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.37% < 6.00%; excess_return_120d -16.95% < 6.00%; excess_return_240d -9.51% < 8.00%; drawdown_120d -31.49% < -28.00%; volatility_120d 52.73% > 42.00% |
| 301130.SZ | 西点药业 | ok | 22.82 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.55% < 6.00%; excess_return_120d -13.13% < 6.00%; excess_return_240d -36.11% < 8.00% |
| 300610.SZ | 晨化股份 | ok | 22.80 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.30% < 6.00%; excess_return_120d -16.88% < 6.00%; excess_return_240d -35.35% < 8.00% |
| 603199.SH | 九华旅游 | ok | 22.80 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.84% < 6.00%; excess_return_120d -14.42% < 6.00%; excess_return_240d -29.20% < 8.00% |
| 603868.SH | 飞科电器 | ok | 22.79 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.82% < 6.00%; excess_return_120d -32.40% < 6.00%; excess_return_240d -34.26% < 8.00%; drawdown_120d -30.61% < -28.00% |
| 301026.SZ | 浩通科技 | ok | 22.77 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.54% < 6.00%; excess_return_120d -5.12% < 6.00%; excess_return_240d -11.04% < 8.00%; drawdown_120d -33.07% < -28.00%; volatility_120d 63.55% > 42.00% |
| 603007.SH | 顺景科技 | ok | 22.76 | close_below_ma200; stock_return_120d -3.42% < 6.00%; excess_return_120d -7.52% < 6.00%; excess_return_240d -5.14% < 8.00%; drawdown_120d -38.98% < -28.00%; volatility_120d 60.62% > 42.00% |
| 002004.SZ | 华邦健康 | ok | 22.76 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.53% < 6.00%; excess_return_120d -12.11% < 6.00%; excess_return_240d -13.16% < 8.00%; drawdown_120d -28.14% < -28.00% |
| 300452.SZ | 山河药辅 | ok | 22.76 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.68% < 6.00%; excess_return_120d -9.26% < 6.00%; excess_return_240d -32.04% < 8.00%; volatility_120d 44.00% > 42.00% |
| 002967.SZ | 广电计量 | ok | 22.75 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.06% < 6.00%; excess_return_120d -18.64% < 6.00%; excess_return_240d -15.30% < 8.00%; drawdown_120d -29.16% < -28.00% |
| 603970.SH | 中农立华 | ok | 22.74 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.35% < 6.00%; excess_return_120d -20.93% < 6.00%; excess_return_240d -44.42% < 8.00%; drawdown_120d -28.05% < -28.00% |
| 002644.SZ | 佛慈制药 | ok | 22.73 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.57% < 6.00%; excess_return_120d -18.15% < 6.00%; excess_return_240d -32.72% < 8.00%; drawdown_120d -32.27% < -28.00% |
| 002020.SZ | 京新药业 | ok | 22.73 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.93% < 6.00%; excess_return_120d -24.51% < 6.00%; excess_return_240d -20.05% < 8.00% |
| 603527.SH | 众源新材 | ok | 22.73 | close_below_ma200; stock_return_120d -1.00% < 6.00%; excess_return_120d -5.58% < 6.00%; excess_return_240d -25.66% < 8.00%; drawdown_120d -29.12% < -28.00%; volatility_120d 62.27% > 42.00% |
| 603197.SH | 保隆科技 | ok | 22.72 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.81% < 6.00%; excess_return_120d -24.39% < 6.00%; excess_return_240d -42.64% < 8.00%; drawdown_120d -28.01% < -28.00% |
| 601866.SH | 中远海发 | ok | 22.72 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.14% < 6.00%; excess_return_120d -11.72% < 6.00%; excess_return_240d -25.55% < 8.00% |
| 688582.SH | 芯动联科 | ok | 22.71 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.62% < 6.00%; excess_return_120d -16.20% < 6.00%; excess_return_240d -31.88% < 8.00%; volatility_120d 53.72% > 42.00% |
| 301033.SZ | 迈普医学 | ok | 22.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.24% < 6.00%; excess_return_120d -14.82% < 6.00%; excess_return_240d -24.05% < 8.00%; drawdown_120d -34.33% < -28.00%; volatility_120d 52.84% > 42.00% |
| 600955.SH | 维远股份 | ok | 22.69 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.90% < 6.00%; excess_return_120d -8.48% < 6.00%; excess_return_240d -11.95% < 8.00%; drawdown_120d -29.29% < -28.00%; volatility_120d 55.01% > 42.00% |
| 002997.SZ | 瑞鹄模具 | ok | 22.68 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.75% < 6.00%; excess_return_120d -25.33% < 6.00%; excess_return_240d -42.59% < 8.00% |
| 002982.SZ | 湘佳股份 | ok | 22.68 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.04% < 6.00%; excess_return_120d -14.62% < 6.00%; excess_return_240d -43.29% < 8.00%; volatility_120d 45.56% > 42.00% |
| 603201.SH | 常润股份 | ok | 22.68 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.97% < 6.00%; excess_return_120d -10.55% < 6.00%; excess_return_240d -16.89% < 8.00%; volatility_120d 47.77% > 42.00% |
| 002034.SZ | 旺能环境 | ok | 22.66 | close_below_ma200; stock_return_120d -0.63% < 6.00%; excess_return_120d -5.21% < 6.00%; excess_return_240d -27.16% < 8.00%; drawdown_120d -33.61% < -28.00% |
| 300110.SZ | 华仁药业 | ok | 22.66 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.19% < 6.00%; excess_return_120d -20.77% < 6.00%; excess_return_240d -42.76% < 8.00% |
| 000157.SZ | 中联重科 | ok | 22.66 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.52% < 6.00%; excess_return_120d -18.10% < 6.00%; excess_return_240d -14.83% < 8.00%; drawdown_120d -28.25% < -28.00% |
| 300685.SZ | 艾德生物 | ok | 22.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.75% < 6.00%; excess_return_120d -15.05% < 6.00%; excess_return_240d -36.15% < 8.00% |
| 002234.SZ | 民和股份 | ok | 22.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.55% < 6.00%; excess_return_120d -20.13% < 6.00%; excess_return_240d -32.75% < 8.00% |
| 603499.SH | 翔港科技 | ok | 22.64 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.41% < 6.00%; excess_return_120d -12.99% < 6.00%; excess_return_240d -11.14% < 8.00%; volatility_120d 53.40% > 42.00% |
| 600248.SH | 陕建股份 | ok | 22.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.11% < 6.00%; excess_return_120d -24.69% < 6.00%; excess_return_240d -46.69% < 8.00% |
| 301015.SZ | 百洋医药 | ok | 22.63 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.90% < 6.00%; excess_return_120d -13.48% < 6.00%; excess_return_240d -19.40% < 8.00% |
| 000090.SZ | 天健集团 | ok | 22.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.22% < 6.00%; excess_return_120d -20.80% < 6.00%; excess_return_240d -34.02% < 8.00% |
| 000713.SZ | 国投丰乐 | ok | 22.61 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.69% < 6.00%; excess_return_120d -21.27% < 6.00%; excess_return_240d -44.95% < 8.00%; drawdown_120d -28.42% < -28.00% |
| 603818.SH | 曲美家居 | ok | 22.61 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.74% < 6.00%; excess_return_120d -17.32% < 6.00%; excess_return_240d -56.55% < 8.00% |
| 002823.SZ | 凯中精密 | ok | 22.60 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -4.78% < 6.00%; excess_return_120d -9.36% < 6.00%; excess_return_240d -10.23% < 8.00%; drawdown_120d -29.46% < -28.00%; volatility_120d 42.12% > 42.00% |
| 002761.SZ | 浙江建投 | ok | 22.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.79% < 6.00%; excess_return_120d -23.37% < 6.00%; excess_return_240d -43.59% < 8.00% |
| 688075.SH | 安旭生物 | ok | 22.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.04% < 6.00%; excess_return_120d -24.62% < 6.00%; excess_return_240d -40.62% < 8.00%; drawdown_120d -29.16% < -28.00% |
| 300218.SZ | 安利股份 | ok | 22.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.41% < 6.00%; excess_return_120d -20.99% < 6.00%; excess_return_240d -30.60% < 8.00% |
| 300888.SZ | 稳健医疗 | ok | 22.58 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.31% < 6.00%; excess_return_120d -27.89% < 6.00%; excess_return_240d -47.67% < 8.00% |
| 605066.SH | 天正电气 | ok | 22.56 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.97% < 6.00%; excess_return_120d -10.55% < 6.00%; excess_return_240d -31.19% < 8.00% |
| 300052.SZ | 中青宝 | ok | 22.56 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.95% < 6.00%; excess_return_120d -8.05% < 6.00%; excess_return_240d -6.48% < 8.00%; drawdown_120d -29.32% < -28.00%; volatility_120d 66.99% > 42.00% |
| 603278.SH | 大业股份 | ok | 22.56 | close_below_ma200; stock_return_120d -36.03% < 6.00%; excess_return_120d -40.61% < 6.00%; excess_return_240d -2.88% < 8.00%; drawdown_120d -40.27% < -28.00%; volatility_120d 68.38% > 42.00% |
| 603877.SH | 太平鸟 | ok | 22.56 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.56% < 6.00%; excess_return_120d -14.14% < 6.00%; excess_return_240d -32.15% < 8.00% |
| 002714.SZ | 牧原股份 | ok | 22.55 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.88% < 6.00%; excess_return_120d -27.46% < 6.00%; excess_return_240d -29.73% < 8.00% |
| 603578.SH | 三星新材 | ok | 22.53 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 1.16% < 6.00%; excess_return_120d -3.42% < 6.00%; excess_return_240d -35.34% < 8.00%; drawdown_120d -31.58% < -28.00%; volatility_120d 58.82% > 42.00% |
| 600287.SH | 苏豪时尚 | ok | 22.53 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.75% < 6.00%; excess_return_120d -20.33% < 6.00%; excess_return_240d -48.98% < 8.00% |
| 000581.SZ | 威孚高科 | ok | 22.53 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.40% < 6.00%; excess_return_120d -15.98% < 6.00%; excess_return_240d -24.23% < 8.00%; drawdown_120d -29.73% < -28.00% |
| 300519.SZ | 新光药业 | ok | 22.53 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.51% < 6.00%; excess_return_120d -16.09% < 6.00%; excess_return_240d -34.85% < 8.00% |
| 600816.SH | 建元信托 | ok | 22.52 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -13.43% < 6.00%; excess_return_120d -18.01% < 6.00%; excess_return_240d -38.05% < 8.00% |
| 603315.SH | 福鞍股份 | ok | 22.51 | close_below_ma200; stock_return_120d -8.44% < 6.00%; excess_return_120d -13.02% < 6.00%; excess_return_240d -7.31% < 8.00%; drawdown_120d -30.97% < -28.00%; volatility_120d 58.88% > 42.00% |
| 600216.SH | 浙江医药 | ok | 22.51 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.29% < 6.00%; excess_return_120d -11.87% < 6.00%; excess_return_240d -34.88% < 8.00%; drawdown_120d -30.84% < -28.00% |
| 300422.SZ | 博世科 | ok | 22.51 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -0.65% < 6.00%; excess_return_120d -5.23% < 6.00%; excess_return_240d -32.55% < 8.00%; volatility_120d 44.82% > 42.00% |
| 600272.SH | 开开实业 | ok | 22.51 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.37% < 6.00%; excess_return_120d -23.95% < 6.00%; excess_return_240d -42.88% < 8.00% |
| 002573.SZ | 清新环境 | ok | 22.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.38% < 6.00%; excess_return_120d -21.96% < 6.00%; excess_return_240d -44.23% < 8.00% |
| 002059.SZ | 云南旅游 | ok | 22.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.14% < 6.00%; excess_return_120d -23.73% < 6.00%; excess_return_240d -38.08% < 8.00% |
| 603500.SH | 祥和实业 | ok | 22.49 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.80% < 6.00%; excess_return_120d -15.38% < 6.00%; excess_return_240d -3.23% < 8.00%; volatility_120d 51.03% > 42.00% |
| 600452.SH | 涪陵电力 | ok | 22.47 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 2.77% < 6.00%; excess_return_120d -1.81% < 6.00%; excess_return_240d -18.60% < 8.00%; drawdown_120d -42.86% < -28.00%; volatility_120d 55.54% > 42.00% |
| 301469.SZ | 恒达新材 | ok | 22.47 | close_below_ma200; stock_return_120d -3.70% < 6.00%; excess_return_120d -8.28% < 6.00%; excess_return_240d -21.16% < 8.00%; drawdown_120d -32.73% < -28.00%; volatility_120d 42.88% > 42.00% |
| 301106.SZ | 骏成科技 | ok | 22.46 | close_below_ma200; stock_return_120d -3.64% < 6.00%; excess_return_120d -8.22% < 6.00%; excess_return_240d -29.50% < 8.00%; volatility_120d 49.51% > 42.00% |
| 603444.SH | 吉比特 | ok | 22.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.28% < 6.00%; excess_return_120d -17.86% < 6.00%; excess_return_240d -5.83% < 8.00% |
| 002915.SZ | 中欣氟材 | ok | 22.45 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.37% < 6.00%; excess_return_120d -22.95% < 6.00%; excess_return_240d -5.62% < 8.00%; volatility_120d 52.02% > 42.00% |
| 002494.SZ | 华斯股份 | ok | 22.45 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.43% < 6.00%; excess_return_120d -17.01% < 6.00%; excess_return_240d -29.98% < 8.00% |
| 002038.SZ | 双鹭药业 | ok | 22.44 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.08% < 6.00%; excess_return_120d -16.66% < 6.00%; excess_return_240d -33.17% < 8.00%; drawdown_120d -31.06% < -28.00%; volatility_120d 58.55% > 42.00% |
| 600997.SH | 开滦股份 | ok | 22.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.85% < 6.00%; excess_return_120d -12.43% < 6.00%; excess_return_240d -32.80% < 8.00% |
| 603187.SH | 海容冷链 | ok | 22.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.89% < 6.00%; excess_return_120d -23.47% < 6.00%; excess_return_240d -14.13% < 8.00% |
| 301233.SZ | 盛帮股份 | ok | 22.42 | close_below_ma200; stock_return_120d -6.20% < 6.00%; excess_return_120d -10.78% < 6.00%; excess_return_240d -31.78% < 8.00%; drawdown_120d -29.05% < -28.00% |
| 600558.SH | 大西洋 | ok | 22.41 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.69% < 6.00%; excess_return_120d -23.27% < 6.00%; excess_return_240d -26.62% < 8.00%; drawdown_120d -28.63% < -28.00% |
| 605138.SH | 盛泰集团 | ok | 22.41 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.68% < 6.00%; excess_return_120d -17.26% < 6.00%; excess_return_240d -32.76% < 8.00% |
| 600527.SH | 江南高纤 | ok | 22.39 | close_below_ma200; stock_return_120d 0.94% < 6.00%; excess_return_120d -3.64% < 6.00%; excess_return_240d -19.19% < 8.00%; drawdown_120d -38.33% < -28.00%; volatility_120d 56.66% > 42.00% |
| 688382.SH | 益方生物 | ok | 22.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.35% < 6.00%; excess_return_120d -19.93% < 6.00%; excess_return_240d -47.26% < 8.00%; drawdown_120d -33.35% < -28.00%; volatility_120d 66.69% > 42.00% |
| 600933.SH | 爱柯迪 | ok | 22.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.30% < 6.00%; excess_return_120d -27.88% < 6.00%; excess_return_240d -23.49% < 8.00% |
| 600824.SH | 益民集团 | ok | 22.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.18% < 6.00%; excess_return_120d -27.76% < 6.00%; excess_return_240d -37.88% < 8.00%; drawdown_120d -29.84% < -28.00% |
| 600863.SH | 华能蒙电 | ok | 22.38 | close_below_ma200; stock_return_120d -0.22% < 6.00%; excess_return_120d -4.80% < 6.00%; excess_return_240d -10.18% < 8.00%; drawdown_120d -44.33% < -28.00%; volatility_120d 47.84% > 42.00% |
| 002601.SZ | 龙佰集团 | ok | 22.38 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.02% < 6.00%; excess_return_120d -17.60% < 6.00%; excess_return_240d -18.08% < 8.00%; drawdown_120d -28.42% < -28.00%; volatility_120d 44.15% > 42.00% |
| 600861.SH | 北京人力 | ok | 22.36 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.52% < 6.00%; excess_return_120d -30.10% < 6.00%; excess_return_240d -52.01% < 8.00%; drawdown_120d -32.57% < -28.00% |
| 002124.SZ | 天邦食品 | ok | 22.36 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.68% < 6.00%; excess_return_120d -16.26% < 6.00%; excess_return_240d -40.16% < 8.00%; volatility_120d 54.47% > 42.00% |
| 002597.SZ | 金禾实业 | ok | 22.36 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -1.76% < 6.00%; excess_return_120d -6.34% < 6.00%; excess_return_240d -34.67% < 8.00%; drawdown_120d -30.42% < -28.00%; volatility_120d 49.65% > 42.00% |
| 300034.SZ | 钢研高纳 | ok | 22.36 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.35% < 6.00%; excess_return_120d -16.93% < 6.00%; excess_return_240d -14.92% < 8.00%; drawdown_120d -32.70% < -28.00%; volatility_120d 52.49% > 42.00% |
| 002732.SZ | 燕塘乳业 | ok | 22.34 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.29% < 6.00%; excess_return_120d -26.87% < 6.00%; excess_return_240d -44.42% < 8.00% |
| 600790.SH | 轻纺城 | ok | 22.34 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -10.18% < 6.00%; excess_return_120d -14.76% < 6.00%; excess_return_240d -31.04% < 8.00%; drawdown_120d -31.47% < -28.00% |
| 688468.SH | 科美诊断 | ok | 22.32 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.49% < 6.00%; excess_return_120d -21.07% < 6.00%; excess_return_240d -38.59% < 8.00% |
| 000591.SZ | 太阳能 | ok | 22.32 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 2.35% < 6.00%; excess_return_120d -2.23% < 6.00%; excess_return_240d -21.34% < 8.00%; drawdown_120d -34.12% < -28.00%; volatility_120d 49.82% > 42.00% |
| 688281.SH | 华秦科技 | ok | 22.31 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.64% < 6.00%; excess_return_120d -9.22% < 6.00%; excess_return_240d -1.09% < 8.00%; drawdown_120d -38.14% < -28.00%; volatility_120d 65.92% > 42.00% |
| 603511.SH | 爱慕股份 | ok | 22.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.52% < 6.00%; excess_return_120d -23.10% < 6.00%; excess_return_240d -44.05% < 8.00%; drawdown_120d -30.16% < -28.00% |
| 002252.SZ | 上海莱士 | ok | 22.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.41% < 6.00%; excess_return_120d -30.99% < 6.00%; excess_return_240d -52.80% < 8.00%; drawdown_120d -29.01% < -28.00% |
| 603320.SH | 迪贝电气 | ok | 22.28 | close_below_ma200; stock_return_120d 0.53% < 6.00%; excess_return_120d -4.05% < 6.00%; excess_return_240d -19.82% < 8.00%; drawdown_120d -28.56% < -28.00%; volatility_120d 51.38% > 42.00% |
| 600104.SH | 上汽集团 | ok | 22.26 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.59% < 6.00%; excess_return_120d -37.17% < 6.00%; excess_return_240d -62.07% < 8.00%; drawdown_120d -35.75% < -28.00% |
| 002439.SZ | 启明星辰 | ok | 22.25 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -10.41% < 6.00%; excess_return_120d -14.99% < 6.00%; excess_return_240d -40.98% < 8.00% |
| 002397.SZ | 梦洁股份 | ok | 22.24 | close_below_ma200; stock_return_120d -3.47% < 6.00%; excess_return_120d -8.05% < 6.00%; excess_return_240d -15.96% < 8.00%; drawdown_120d -34.18% < -28.00%; volatility_120d 53.51% > 42.00% |
| 300817.SZ | 双飞集团 | ok | 22.24 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.65% < 6.00%; excess_return_120d -22.24% < 6.00%; excess_return_240d -43.22% < 8.00%; volatility_120d 45.68% > 42.00% |
| 600028.SH | 中国石化 | ok | 22.23 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.57% < 6.00%; excess_return_120d -25.15% < 6.00%; excess_return_240d -33.14% < 8.00%; drawdown_120d -39.73% < -28.00% |
| 002508.SZ | 老板电器 | ok | 22.22 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.73% < 6.00%; excess_return_120d -23.31% < 6.00%; excess_return_240d -35.70% < 8.00%; drawdown_120d -30.36% < -28.00% |
| 600708.SH | 光明地产 | ok | 22.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.91% < 6.00%; excess_return_120d -19.49% < 6.00%; excess_return_240d -25.71% < 8.00%; drawdown_120d -29.57% < -28.00%; volatility_120d 48.97% > 42.00% |
| 002438.SZ | 江苏神通 | ok | 22.20 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.43% < 6.00%; excess_return_120d -14.01% < 6.00%; excess_return_240d -8.33% < 8.00%; drawdown_120d -29.15% < -28.00%; volatility_120d 50.03% > 42.00% |
| 688073.SH | 毕得医药 | ok | 22.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.72% < 6.00%; excess_return_120d -11.30% < 6.00%; excess_return_240d -20.45% < 8.00%; volatility_120d 54.14% > 42.00% |
| 600022.SH | 山东钢铁 | ok | 22.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.89% < 6.00%; excess_return_120d -20.47% < 6.00%; excess_return_240d -30.38% < 8.00%; drawdown_120d -30.60% < -28.00% |
| 600425.SH | 青松建化 | ok | 22.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.75% < 6.00%; excess_return_120d -21.33% < 6.00%; excess_return_240d -29.50% < 8.00%; drawdown_120d -28.24% < -28.00% |
| 603260.SH | 合盛硅业 | ok | 22.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.57% < 6.00%; excess_return_120d -22.15% < 6.00%; excess_return_240d -34.00% < 8.00%; volatility_120d 51.01% > 42.00% |
| 601966.SH | 玲珑轮胎 | ok | 22.16 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.14% < 6.00%; excess_return_120d -28.72% < 6.00%; excess_return_240d -46.18% < 8.00%; drawdown_120d -29.09% < -28.00% |
| 301170.SZ | 锡南科技 | ok | 22.15 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.82% < 6.00%; excess_return_120d -21.40% < 6.00%; excess_return_240d -37.32% < 8.00% |
| 301509.SZ | 金凯生科 | ok | 22.15 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -2.07% < 6.00%; excess_return_120d -6.65% < 6.00%; excess_return_240d -34.77% < 8.00%; drawdown_120d -32.49% < -28.00%; volatility_120d 51.22% > 42.00% |
| 603093.SH | 南华期货 | ok | 22.15 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -5.54% < 6.00%; excess_return_120d -10.12% < 6.00%; excess_return_240d -32.88% < 8.00%; drawdown_120d -29.14% < -28.00%; volatility_120d 58.63% > 42.00% |
| 301125.SZ | 腾亚精工 | ok | 22.14 | close_below_ma200; stock_return_120d 1.26% < 6.00%; excess_return_120d -3.32% < 6.00%; excess_return_240d -0.84% < 8.00%; drawdown_120d -30.78% < -28.00%; volatility_120d 61.43% > 42.00% |
| 301195.SZ | 北路智控 | ok | 22.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.39% < 6.00%; excess_return_120d -20.97% < 6.00%; excess_return_240d -41.74% < 8.00%; volatility_120d 49.08% > 42.00% |
| 001391.SZ | 国货航 | ok | 22.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.62% < 6.00%; excess_return_120d -31.20% < 6.00%; excess_return_240d -58.23% < 8.00%; drawdown_120d -29.17% < -28.00% |
| 002319.SZ | 乐通股份 | ok | 22.13 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.89% < 6.00%; excess_return_120d -11.47% < 6.00%; excess_return_240d -29.21% < 8.00%; drawdown_120d -30.72% < -28.00%; volatility_120d 49.35% > 42.00% |
| 601311.SH | 骆驼股份 | ok | 22.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.71% < 6.00%; excess_return_120d -17.29% < 6.00%; excess_return_240d -28.67% < 8.00%; drawdown_120d -29.58% < -28.00% |
| 600129.SH | 太极集团 | ok | 22.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.66% < 6.00%; excess_return_120d -25.25% < 6.00%; excess_return_240d -55.62% < 8.00% |
| 002069.SZ | 獐子岛 | ok | 22.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.09% < 6.00%; excess_return_120d -20.67% < 6.00%; excess_return_240d -42.85% < 8.00% |
| 002715.SZ | 登云股份 | ok | 22.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.65% < 6.00%; excess_return_120d -18.23% < 6.00%; excess_return_240d -39.81% < 8.00%; volatility_120d 45.51% > 42.00% |
| 300958.SZ | 建工修复 | ok | 22.09 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.96% < 6.00%; excess_return_120d -15.54% < 6.00%; excess_return_240d -37.64% < 8.00% |
| 301000.SZ | 肇民科技 | ok | 22.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.02% < 6.00%; excess_return_120d -20.60% < 6.00%; excess_return_240d -46.03% < 8.00%; volatility_120d 61.72% > 42.00% |
| 300833.SZ | 浩洋股份 | ok | 22.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.46% < 6.00%; excess_return_120d -19.04% < 6.00%; excess_return_240d -18.02% < 8.00% |
| 600178.SH | 东安动力 | ok | 22.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.09% < 6.00%; excess_return_120d -24.67% < 6.00%; excess_return_240d -48.74% < 8.00%; volatility_120d 43.39% > 42.00% |
| 688228.SH | 开普云 | ok | 22.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -61.57% < 6.00%; excess_return_120d -66.15% < 6.00%; excess_return_240d 3.63% < 8.00%; drawdown_120d -73.27% < -28.00%; volatility_120d 68.48% > 42.00% |
| 600138.SH | 中青旅 | ok | 22.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.62% < 6.00%; excess_return_120d -35.20% < 6.00%; excess_return_240d -51.36% < 8.00%; drawdown_120d -35.29% < -28.00% |
| 603227.SH | 雪峰科技 | ok | 22.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.63% < 6.00%; excess_return_120d -16.21% < 6.00%; excess_return_240d -34.63% < 8.00%; drawdown_120d -31.89% < -28.00% |
| 002495.SZ | 佳隆股份 | ok | 22.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.74% < 6.00%; excess_return_120d -22.32% < 6.00%; excess_return_240d -37.57% < 8.00% |
| 300192.SZ | 科德教育 | ok | 22.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.94% < 6.00%; excess_return_120d -21.52% < 6.00%; excess_return_240d 0.19% < 8.00%; drawdown_120d -32.42% < -28.00%; volatility_120d 46.56% > 42.00% |
| 601238.SH | 广汽集团 | ok | 22.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.93% < 6.00%; excess_return_120d -39.51% < 6.00%; excess_return_240d -50.58% < 8.00%; drawdown_120d -38.75% < -28.00% |
| 301207.SZ | 华兰疫苗 | ok | 22.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -3.35% < 6.00%; excess_return_120d -7.93% < 6.00%; excess_return_240d -10.40% < 8.00%; drawdown_120d -36.36% < -28.00%; volatility_120d 55.91% > 42.00% |
| 603112.SH | 华翔股份 | ok | 22.07 | close_below_ma200; stock_return_120d -4.04% < 6.00%; excess_return_120d -8.62% < 6.00%; excess_return_240d -27.08% < 8.00%; drawdown_120d -31.23% < -28.00%; volatility_120d 47.51% > 42.00% |
| 688255.SH | 凯尔达 | ok | 22.06 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.06% < 6.00%; excess_return_120d -23.64% < 6.00%; excess_return_240d -32.14% < 8.00%; volatility_120d 42.70% > 42.00% |
| 000625.SZ | 长安汽车 | ok | 22.06 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.46% < 6.00%; excess_return_120d -44.04% < 6.00%; excess_return_240d -63.03% < 8.00%; drawdown_120d -40.17% < -28.00% |
| 002864.SZ | 盘龙药业 | ok | 22.06 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.92% < 6.00%; excess_return_120d -13.50% < 6.00%; excess_return_240d -24.03% < 8.00%; drawdown_120d -29.97% < -28.00% |
| 301234.SZ | 五洲医疗 | ok | 22.06 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.65% < 6.00%; excess_return_120d -20.23% < 6.00%; excess_return_240d -24.77% < 8.00%; volatility_120d 51.85% > 42.00% |
| 601857.SH | 中国石油 | ok | 22.05 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.53% < 6.00%; excess_return_120d -15.11% < 6.00%; excess_return_240d -8.87% < 8.00%; drawdown_120d -32.37% < -28.00% |
| 605122.SH | 四方新材 | ok | 22.05 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.44% < 6.00%; excess_return_120d -20.02% < 6.00%; excess_return_240d -43.12% < 8.00% |
| 600073.SH | 光明肉业 | ok | 22.04 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.47% < 6.00%; excess_return_120d -25.05% < 6.00%; excess_return_240d -50.60% < 8.00%; drawdown_120d -28.11% < -28.00% |
| 600251.SH | 冠农股份 | ok | 22.04 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -2.51% < 6.00%; excess_return_120d -7.09% < 6.00%; excess_return_240d -2.69% < 8.00%; drawdown_120d -32.02% < -28.00%; volatility_120d 43.11% > 42.00% |
| 300046.SZ | 台基股份 | ok | 22.04 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.56% < 6.00%; excess_return_120d -15.14% < 6.00%; excess_return_240d -44.54% < 8.00%; volatility_120d 50.58% > 42.00% |
| 601600.SH | 中国铝业 | ok | 22.02 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -30.61% < 6.00%; excess_return_120d -35.19% < 6.00%; excess_return_240d 3.57% < 8.00%; drawdown_120d -46.50% < -28.00%; volatility_120d 57.70% > 42.00% |
| 000509.SZ | 华塑控股 | ok | 22.02 | close_below_ma200; stock_return_120d -2.59% < 6.00%; excess_return_120d -7.17% < 6.00%; excess_return_240d -23.41% < 8.00%; drawdown_120d -46.35% < -28.00%; volatility_120d 64.21% > 42.00% |
| 601800.SH | 中国交建 | ok | 22.01 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.63% < 6.00%; excess_return_120d -31.21% < 6.00%; excess_return_240d -53.32% < 8.00%; drawdown_120d -32.81% < -28.00% |
| 002658.SZ | 雪迪龙 | ok | 22.01 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.97% < 6.00%; excess_return_120d -14.55% < 6.00%; excess_return_240d -25.08% < 8.00%; drawdown_120d -31.47% < -28.00%; volatility_120d 46.67% > 42.00% |
| 601900.SH | 南方传媒 | ok | 22.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.38% < 6.00%; excess_return_120d -16.96% < 6.00%; excess_return_240d -42.87% < 8.00%; drawdown_120d -30.23% < -28.00% |
| 600261.SH | 阳光照明 | ok | 22.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.79% < 6.00%; excess_return_120d -11.37% < 6.00%; excess_return_240d -28.17% < 8.00% |
| 002345.SZ | 潮宏基 | ok | 21.98 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.67% < 6.00%; excess_return_120d -17.26% < 6.00%; excess_return_240d -49.46% < 8.00%; drawdown_120d -29.97% < -28.00%; volatility_120d 53.13% > 42.00% |
| 688420.SH | 美腾科技 | ok | 21.98 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.26% < 6.00%; excess_return_120d -13.84% < 6.00%; excess_return_240d -34.32% < 8.00% |
| 603205.SH | 健尔康 | ok | 21.98 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.34% < 6.00%; excess_return_120d -28.92% < 6.00%; excess_return_240d -48.83% < 8.00%; drawdown_120d -28.83% < -28.00% |
| 688137.SH | 近岸蛋白 | ok | 21.96 | close_below_ma200; stock_return_120d -2.85% < 6.00%; excess_return_120d -7.43% < 6.00%; excess_return_240d -24.40% < 8.00%; drawdown_120d -28.68% < -28.00%; volatility_120d 50.45% > 42.00% |
| 600308.SH | 华泰股份 | ok | 21.96 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.95% < 6.00%; excess_return_120d -22.53% < 6.00%; excess_return_240d -30.45% < 8.00% |
| 603042.SH | 华脉科技 | ok | 21.95 | close_below_ma200; stock_return_120d -1.78% < 6.00%; excess_return_120d -6.36% < 6.00%; excess_return_240d -21.85% < 8.00%; drawdown_120d -31.14% < -28.00%; volatility_120d 61.95% > 42.00% |
| 301215.SZ | 中汽股份 | ok | 21.94 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.20% < 6.00%; excess_return_120d -25.78% < 6.00%; excess_return_240d -33.69% < 8.00% |
| 601007.SH | 金陵饭店 | ok | 21.93 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.26% < 6.00%; excess_return_120d -21.84% < 6.00%; excess_return_240d -36.49% < 8.00%; drawdown_120d -29.01% < -28.00% |
| 300185.SZ | 通裕重工 | ok | 21.93 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -1.69% < 6.00%; excess_return_120d -6.27% < 6.00%; excess_return_240d -23.61% < 8.00%; drawdown_120d -36.27% < -28.00%; volatility_120d 52.01% > 42.00% |
| 603489.SH | 八方股份 | ok | 21.93 | close_below_ma200; stock_return_120d -7.59% < 6.00%; excess_return_120d -12.17% < 6.00%; excess_return_240d -16.72% < 8.00%; drawdown_120d -30.41% < -28.00%; volatility_120d 46.74% > 42.00% |
| 002277.SZ | 友阿股份 | ok | 21.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.78% < 6.00%; excess_return_120d -16.36% < 6.00%; excess_return_240d -19.61% < 8.00%; drawdown_120d -28.94% < -28.00%; volatility_120d 50.82% > 42.00% |
| 000998.SZ | 隆平高科 | ok | 21.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.75% < 6.00%; excess_return_120d -20.33% < 6.00%; excess_return_240d -41.47% < 8.00%; drawdown_120d -29.39% < -28.00% |
| 688370.SH | 丛麟科技 | ok | 21.91 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.37% < 6.00%; excess_return_120d -12.95% < 6.00%; excess_return_240d -11.23% < 8.00%; drawdown_120d -29.90% < -28.00% |
| 000545.SZ | 金浦钛业 | ok | 21.91 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.90% < 6.00%; excess_return_120d -8.48% < 6.00%; excess_return_240d -16.91% < 8.00%; drawdown_120d -37.41% < -28.00%; volatility_120d 64.76% > 42.00% |
| 301277.SZ | 新天地 | ok | 21.91 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.91% < 6.00%; excess_return_120d -21.49% < 6.00%; excess_return_240d -55.14% < 8.00% |
| 688285.SH | 高铁电气 | ok | 21.90 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.21% < 6.00%; excess_return_120d -19.79% < 6.00%; excess_return_240d -32.66% < 8.00% |
| 000863.SZ | 三湘印象 | ok | 21.90 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -30.02% < 6.00%; excess_return_120d -34.60% < 6.00%; excess_return_240d 0.69% < 8.00%; drawdown_120d -37.27% < -28.00%; volatility_120d 56.10% > 42.00% |
| 300984.SZ | 金沃股份 | ok | 21.90 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.95% < 6.00%; excess_return_120d -34.53% < 6.00%; excess_return_240d -7.49% < 8.00%; drawdown_120d -33.90% < -28.00%; volatility_120d 50.21% > 42.00% |
| 300347.SZ | 泰格医药 | ok | 21.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.76% < 6.00%; excess_return_120d -18.34% < 6.00%; excess_return_240d -34.43% < 8.00%; volatility_120d 43.59% > 42.00% |
| 300654.SZ | 世纪天鸿 | ok | 21.89 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.14% < 6.00%; excess_return_120d -7.72% < 6.00%; excess_return_240d -28.38% < 8.00%; drawdown_120d -31.10% < -28.00%; volatility_120d 51.78% > 42.00% |
| 600664.SH | 哈药股份 | ok | 21.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.83% < 6.00%; excess_return_120d -12.41% < 6.00%; excess_return_240d -37.63% < 8.00%; drawdown_120d -34.84% < -28.00% |
| 600881.SH | 亚泰集团 | ok | 21.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.82% < 6.00%; excess_return_120d -23.40% < 6.00%; excess_return_240d -40.35% < 8.00%; volatility_120d 43.48% > 42.00% |
| 002376.SZ | 新北洋 | ok | 21.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.98% < 6.00%; excess_return_120d -26.56% < 6.00%; excess_return_240d -44.70% < 8.00%; drawdown_120d -28.10% < -28.00% |
| 600720.SH | 中交设计 | ok | 21.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.09% < 6.00%; excess_return_120d -33.67% < 6.00%; excess_return_240d -53.20% < 8.00%; drawdown_120d -32.10% < -28.00% |
| 002906.SZ | 华阳集团 | ok | 21.88 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.89% < 6.00%; excess_return_120d -19.47% < 6.00%; excess_return_240d -37.84% < 8.00% |
| 688139.SH | 海尔生物 | ok | 21.88 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.14% < 6.00%; excess_return_120d -15.72% < 6.00%; excess_return_240d -29.65% < 8.00% |
| 688529.SH | 豪森智能 | ok | 21.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.07% < 6.00%; excess_return_120d -17.65% < 6.00%; excess_return_240d -29.91% < 8.00% |
| 300901.SZ | 中胤时尚 | ok | 21.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.66% < 6.00%; excess_return_120d -15.24% < 6.00%; excess_return_240d -31.92% < 8.00%; volatility_120d 46.24% > 42.00% |
| 002771.SZ | 真视通 | ok | 21.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.55% < 6.00%; excess_return_120d -10.13% < 6.00%; excess_return_240d -33.80% < 8.00%; drawdown_120d -29.29% < -28.00%; volatility_120d 57.07% > 42.00% |
| 300449.SZ | 汉邦高科 | ok | 21.87 | close_below_ma200; stock_return_120d -9.19% < 6.00%; excess_return_120d -13.77% < 6.00%; excess_return_240d -32.72% < 8.00%; drawdown_120d -46.06% < -28.00%; volatility_120d 69.29% > 42.00% |
| 002239.SZ | 奥特佳 | ok | 21.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.28% < 6.00%; excess_return_120d -21.86% < 6.00%; excess_return_240d -36.39% < 8.00%; drawdown_120d -28.78% < -28.00% |
| 000683.SZ | 博源化工 | ok | 21.87 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.55% < 6.00%; excess_return_120d -23.13% < 6.00%; excess_return_240d 2.58% < 8.00%; drawdown_120d -39.40% < -28.00%; volatility_120d 43.71% > 42.00% |
| 601005.SH | 重庆钢铁 | ok | 21.86 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.86% < 6.00%; excess_return_120d -24.44% < 6.00%; excess_return_240d -39.28% < 8.00%; drawdown_120d -30.36% < -28.00% |
| 301333.SZ | 诺思格 | ok | 21.86 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.17% < 6.00%; excess_return_120d -12.75% < 6.00%; excess_return_240d -13.76% < 8.00%; drawdown_120d -40.47% < -28.00%; volatility_120d 64.87% > 42.00% |
| 002753.SZ | 永东股份 | ok | 21.83 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.31% < 6.00%; excess_return_120d -19.89% < 6.00%; excess_return_240d -35.93% < 8.00% |
| 300531.SZ | 优博讯 | ok | 21.83 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.20% < 6.00%; excess_return_120d -16.78% < 6.00%; excess_return_240d -50.79% < 8.00%; volatility_120d 53.64% > 42.00% |
| 605166.SH | 聚合顺 | ok | 21.83 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.35% < 6.00%; excess_return_120d -14.93% < 6.00%; excess_return_240d -39.16% < 8.00%; volatility_120d 47.17% > 42.00% |
| 002697.SZ | 红旗连锁 | ok | 21.83 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.05% < 6.00%; excess_return_120d -28.63% < 6.00%; excess_return_240d -38.49% < 8.00%; drawdown_120d -33.61% < -28.00% |
| 600854.SH | 春兰股份 | ok | 21.82 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.88% < 6.00%; excess_return_120d -15.46% < 6.00%; excess_return_240d -38.59% < 8.00%; drawdown_120d -31.97% < -28.00% |
| 002690.SZ | 美亚光电 | ok | 21.82 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.42% < 6.00%; excess_return_120d -30.00% < 6.00%; excess_return_240d -26.46% < 8.00%; drawdown_120d -32.02% < -28.00% |
| 300629.SZ | 新劲刚 | ok | 21.82 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.24% < 6.00%; excess_return_120d -18.82% < 6.00%; excess_return_240d -22.94% < 8.00%; drawdown_120d -40.75% < -28.00%; volatility_120d 68.16% > 42.00% |
| 002591.SZ | 恒大高新 | ok | 21.82 | close_below_ma200; stock_return_120d -20.94% < 6.00%; excess_return_120d -25.52% < 6.00%; excess_return_240d -15.50% < 8.00%; drawdown_120d -32.42% < -28.00%; volatility_120d 49.07% > 42.00% |
| 603355.SH | 莱克电气 | ok | 21.81 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.27% < 6.00%; excess_return_120d -21.85% < 6.00%; excess_return_240d -5.86% < 8.00%; drawdown_120d -32.55% < -28.00%; volatility_120d 50.74% > 42.00% |
| 600655.SH | 豫园股份 | ok | 21.80 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.59% < 6.00%; excess_return_120d -20.17% < 6.00%; excess_return_240d -43.08% < 8.00%; drawdown_120d -29.59% < -28.00% |
| 002728.SZ | 特一药业 | ok | 21.80 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.94% < 6.00%; excess_return_120d -15.52% < 6.00%; excess_return_240d -8.61% < 8.00%; drawdown_120d -33.45% < -28.00%; volatility_120d 43.86% > 42.00% |
| 002344.SZ | 海宁皮城 | ok | 21.80 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.36% < 6.00%; excess_return_120d -26.94% < 6.00%; excess_return_240d -37.12% < 8.00%; drawdown_120d -31.21% < -28.00% |
| 603656.SH | 泰禾智能 | ok | 21.79 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.85% < 6.00%; excess_return_120d -27.43% < 6.00%; excess_return_240d -24.59% < 8.00%; drawdown_120d -31.12% < -28.00% |
| 600469.SH | 风神股份 | ok | 21.79 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.40% < 6.00%; excess_return_120d -21.98% < 6.00%; excess_return_240d -19.30% < 8.00%; drawdown_120d -30.42% < -28.00% |
| 301370.SZ | 国科恒泰 | ok | 21.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.12% < 6.00%; excess_return_120d -30.70% < 6.00%; excess_return_240d -41.35% < 8.00%; drawdown_120d -34.35% < -28.00% |
| 002237.SZ | 恒邦股份 | ok | 21.78 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 0.11% < 6.00%; excess_return_120d -4.47% < 6.00%; excess_return_240d -6.89% < 8.00%; drawdown_120d -43.23% < -28.00%; volatility_120d 63.75% > 42.00% |
| 002959.SZ | 小熊电器 | ok | 21.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.53% < 6.00%; excess_return_120d -23.11% < 6.00%; excess_return_240d -48.31% < 8.00% |
| 002727.SZ | 一心堂 | ok | 21.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.48% < 6.00%; excess_return_120d -22.06% < 6.00%; excess_return_240d -55.07% < 8.00%; drawdown_120d -28.44% < -28.00% |
| 688293.SH | 奥浦迈 | ok | 21.77 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.29% < 6.00%; excess_return_120d -13.87% < 6.00%; excess_return_240d -21.37% < 8.00%; volatility_120d 50.73% > 42.00% |
| 688271.SH | 联影医疗 | ok | 21.77 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.94% < 6.00%; excess_return_120d -19.52% < 6.00%; excess_return_240d -37.50% < 8.00%; drawdown_120d -29.30% < -28.00% |
| 301386.SZ | 未来电器 | ok | 21.77 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.70% < 6.00%; excess_return_120d -14.28% < 6.00%; excess_return_240d -27.28% < 8.00%; drawdown_120d -28.63% < -28.00% |
| 300106.SZ | 西部牧业 | ok | 21.76 | close_below_ma200; stock_return_120d -5.12% < 6.00%; excess_return_120d -9.70% < 6.00%; excess_return_240d -31.94% < 8.00%; drawdown_120d -35.48% < -28.00%; volatility_120d 47.03% > 42.00% |
| 002286.SZ | 保龄宝 | ok | 21.76 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.25% < 6.00%; excess_return_120d -8.83% < 6.00%; excess_return_240d -49.16% < 8.00%; volatility_120d 42.57% > 42.00% |
| 002539.SZ | 云图控股 | ok | 21.76 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.44% < 6.00%; excess_return_120d -8.02% < 6.00%; excess_return_240d -7.76% < 8.00%; drawdown_120d -34.27% < -28.00%; volatility_120d 48.12% > 42.00% |
| 688682.SH | 霍莱沃 | ok | 21.75 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -30.72% < 6.00%; excess_return_120d -35.30% < 6.00%; excess_return_240d 1.29% < 8.00%; drawdown_120d -49.84% < -28.00%; volatility_120d 64.62% > 42.00% |
| 000809.SZ | 和展能源 | ok | 21.73 | close_below_ma200; stock_return_120d -12.64% < 6.00%; excess_return_120d -17.22% < 6.00%; excess_return_240d -19.82% < 8.00%; drawdown_120d -33.05% < -28.00%; volatility_120d 45.35% > 42.00% |
| 601216.SH | 君正集团 | ok | 21.72 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.62% < 6.00%; excess_return_120d -5.20% < 6.00%; excess_return_240d -34.16% < 8.00%; drawdown_120d -29.04% < -28.00% |
| 601008.SH | 连云港 | ok | 21.71 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.44% < 6.00%; excess_return_120d -23.02% < 6.00%; excess_return_240d -56.00% < 8.00%; drawdown_120d -30.58% < -28.00% |
| 002555.SZ | 三七互娱 | ok | 21.71 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.72% < 6.00%; excess_return_120d -22.30% < 6.00%; excess_return_240d -12.77% < 8.00%; drawdown_120d -37.77% < -28.00% |
| 000570.SZ | 苏常柴A | ok | 21.71 | close_below_ma200; stock_return_120d -10.08% < 6.00%; excess_return_120d -14.66% < 6.00%; excess_return_240d -35.79% < 8.00%; drawdown_120d -28.12% < -28.00% |
| 601633.SH | 长城汽车 | ok | 21.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.31% < 6.00%; excess_return_120d -34.89% < 6.00%; excess_return_240d -47.78% < 8.00%; drawdown_120d -30.25% < -28.00% |
| 000019.SZ | 深粮控股 | ok | 21.70 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.01% < 6.00%; excess_return_120d -16.59% < 6.00%; excess_return_240d -30.86% < 8.00%; drawdown_120d -28.96% < -28.00% |
| 600526.SH | 菲达环保 | ok | 21.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.77% < 6.00%; excess_return_120d -24.35% < 6.00%; excess_return_240d -33.08% < 8.00%; drawdown_120d -30.51% < -28.00% |
| 301256.SZ | 华融化学 | ok | 21.70 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.08% < 6.00%; excess_return_120d -14.66% < 6.00%; excess_return_240d -5.13% < 8.00%; drawdown_120d -37.92% < -28.00%; volatility_120d 59.42% > 42.00% |
| 301138.SZ | 华研精机 | ok | 21.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.54% < 6.00%; excess_return_120d -19.12% < 6.00%; excess_return_240d -26.88% < 8.00%; drawdown_120d -33.01% < -28.00%; volatility_120d 50.77% > 42.00% |
| 000717.SZ | 中南股份 | ok | 21.69 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.60% < 6.00%; excess_return_120d -21.18% < 6.00%; excess_return_240d -39.89% < 8.00% |
| 603102.SH | 百合股份 | ok | 21.69 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.69% < 6.00%; excess_return_120d -26.27% < 6.00%; excess_return_240d -40.73% < 8.00%; drawdown_120d -29.01% < -28.00% |
| 002688.SZ | 金河生物 | ok | 21.68 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.02% < 6.00%; excess_return_120d -17.60% < 6.00%; excess_return_240d -45.60% < 8.00% |
| 300149.SZ | 睿智医药 | ok | 21.67 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -1.15% < 6.00%; excess_return_120d -5.73% < 6.00%; excess_return_240d -36.72% < 8.00%; drawdown_120d -33.59% < -28.00%; volatility_120d 64.06% > 42.00% |
| 002780.SZ | 三夫户外 | ok | 21.67 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.15% < 6.00%; excess_return_120d -13.73% < 6.00%; excess_return_240d -24.94% < 8.00%; volatility_120d 43.53% > 42.00% |
| 300730.SZ | 科创信息 | ok | 21.67 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -3.44% < 6.00%; excess_return_120d -8.02% < 6.00%; excess_return_240d -35.76% < 8.00%; volatility_120d 60.37% > 42.00% |
| 002101.SZ | 广东鸿图 | ok | 21.67 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.84% < 6.00%; excess_return_120d -29.42% < 6.00%; excess_return_240d -45.75% < 8.00%; drawdown_120d -28.77% < -28.00% |
| 300800.SZ | 力合科技 | ok | 21.66 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.63% < 6.00%; excess_return_120d -20.21% < 6.00%; excess_return_240d -34.62% < 8.00% |
| 000420.SZ | 吉林化纤 | ok | 21.66 | close_below_ma200; stock_return_120d -11.26% < 6.00%; excess_return_120d -15.84% < 6.00%; excess_return_240d -20.35% < 8.00%; drawdown_120d -31.52% < -28.00%; volatility_120d 48.14% > 42.00% |
| 301578.SZ | 辰奕智能 | ok | 21.66 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.68% < 6.00%; excess_return_120d -21.26% < 6.00%; excess_return_240d -43.39% < 8.00% |
| 002010.SZ | 传化智联 | ok | 21.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.99% < 6.00%; excess_return_120d -21.57% < 6.00%; excess_return_240d -34.44% < 8.00%; drawdown_120d -34.98% < -28.00% |
| 688278.SH | 特宝生物 | ok | 21.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.54% < 6.00%; excess_return_120d -34.12% < 6.00%; excess_return_240d -36.51% < 8.00%; drawdown_120d -30.77% < -28.00% |
| 603708.SH | 家家悦 | ok | 21.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.75% < 6.00%; excess_return_120d -26.33% < 6.00%; excess_return_240d -28.96% < 8.00%; drawdown_120d -34.76% < -28.00% |
| 002204.SZ | 大连重工 | ok | 21.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.53% < 6.00%; excess_return_120d -33.11% < 6.00%; excess_return_240d -34.22% < 8.00%; drawdown_120d -33.22% < -28.00% |
| 002739.SZ | 儒意电影 | ok | 21.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.40% < 6.00%; excess_return_120d -21.98% < 6.00%; excess_return_240d -38.72% < 8.00%; drawdown_120d -32.59% < -28.00% |
| 002318.SZ | 久立特材 | ok | 21.65 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.14% < 6.00%; excess_return_120d -20.73% < 6.00%; excess_return_240d -17.21% < 8.00%; drawdown_120d -33.30% < -28.00% |
| 002533.SZ | 金杯电工 | ok | 21.65 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.51% < 6.00%; excess_return_120d -12.09% < 6.00%; excess_return_240d -4.23% < 8.00%; drawdown_120d -31.10% < -28.00% |
| 300856.SZ | 科思股份 | ok | 21.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.52% < 6.00%; excess_return_120d -22.10% < 6.00%; excess_return_240d -49.28% < 8.00% |
| 603901.SH | 永创智能 | ok | 21.64 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.88% < 6.00%; excess_return_120d -26.46% < 6.00%; excess_return_240d -13.49% < 8.00%; drawdown_120d -32.33% < -28.00% |
| 301263.SZ | 泰恩康 | ok | 21.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.40% < 6.00%; excess_return_120d -14.98% < 6.00%; excess_return_240d -55.53% < 8.00%; volatility_120d 49.45% > 42.00% |
| 688334.SH | 西高院 | ok | 21.64 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.00% < 6.00%; excess_return_120d -7.58% < 6.00%; excess_return_240d -11.18% < 8.00%; drawdown_120d -34.86% < -28.00%; volatility_120d 47.32% > 42.00% |
| 000759.SZ | 中百集团 | ok | 21.63 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.79% < 6.00%; excess_return_120d -24.37% < 6.00%; excess_return_240d -41.10% < 8.00%; volatility_120d 56.22% > 42.00% |
| 600512.SH | 腾达建设 | ok | 21.63 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.67% < 6.00%; excess_return_120d -23.25% < 6.00%; excess_return_240d -37.34% < 8.00% |
| 301103.SZ | 何氏眼科 | ok | 21.61 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.27% < 6.00%; excess_return_120d -21.85% < 6.00%; excess_return_240d -46.70% < 8.00% |
| 301105.SZ | 鸿铭股份 | ok | 21.59 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.58% < 6.00%; excess_return_120d -10.16% < 6.00%; excess_return_240d -3.27% < 8.00%; drawdown_120d -29.77% < -28.00%; volatility_120d 47.38% > 42.00% |
| 600984.SH | 建设机械 | ok | 21.59 | close_below_ma200; stock_return_120d -8.31% < 6.00%; excess_return_120d -12.89% < 6.00%; excess_return_240d -8.15% < 8.00%; drawdown_120d -30.30% < -28.00%; volatility_120d 48.89% > 42.00% |
| 688153.SH | 唯捷创芯 | ok | 21.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.29% < 6.00%; excess_return_120d -20.87% < 6.00%; excess_return_240d -19.45% < 8.00%; drawdown_120d -31.81% < -28.00%; volatility_120d 49.52% > 42.00% |
| 301202.SZ | 朗威股份 | ok | 21.58 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.81% < 6.00%; excess_return_120d -17.39% < 6.00%; excess_return_240d -38.30% < 8.00%; volatility_120d 46.99% > 42.00% |
| 600006.SH | 东风股份 | ok | 21.58 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.21% < 6.00%; excess_return_120d -29.79% < 6.00%; excess_return_240d -46.15% < 8.00%; drawdown_120d -29.62% < -28.00% |
| 688395.SH | 正弦电气 | ok | 21.58 | close_below_ma200; stock_return_120d -7.37% < 6.00%; excess_return_120d -11.95% < 6.00%; excess_return_240d -22.03% < 8.00%; drawdown_120d -32.67% < -28.00% |
| 301301.SZ | 川宁生物 | ok | 21.58 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.21% < 6.00%; excess_return_120d -16.79% < 6.00%; excess_return_240d -48.16% < 8.00%; drawdown_120d -31.25% < -28.00% |
| 688680.SH | 海优新材 | ok | 21.57 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 3.74% < 6.00%; excess_return_120d -0.84% < 6.00%; excess_return_240d -36.65% < 8.00%; drawdown_120d -47.07% < -28.00%; volatility_120d 66.12% > 42.00% |
| 003008.SZ | 开普检测 | ok | 21.57 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.68% < 6.00%; excess_return_120d -19.26% < 6.00%; excess_return_240d -34.08% < 8.00% |
| 002479.SZ | 富春环保 | ok | 21.57 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.87% < 6.00%; excess_return_120d -11.46% < 6.00%; excess_return_240d -36.44% < 8.00%; drawdown_120d -28.93% < -28.00% |
| 600738.SH | 丽尚国潮 | ok | 21.56 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.72% < 6.00%; excess_return_120d -28.30% < 6.00%; excess_return_240d -47.57% < 8.00%; drawdown_120d -29.69% < -28.00% |
| 002588.SZ | 史丹利 | ok | 21.56 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.53% < 6.00%; excess_return_120d -16.11% < 6.00%; excess_return_240d -23.43% < 8.00%; drawdown_120d -28.12% < -28.00% |
| 300768.SZ | 迪普科技 | ok | 21.54 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.29% < 6.00%; excess_return_120d -19.87% < 6.00%; excess_return_240d -28.62% < 8.00% |
| 603073.SH | 彩蝶实业 | ok | 21.54 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.52% < 6.00%; excess_return_120d -20.10% < 6.00%; excess_return_240d -28.60% < 8.00% |
| 600803.SH | 新奥股份 | ok | 21.54 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.82% < 6.00%; excess_return_120d -22.40% < 6.00%; excess_return_240d -27.82% < 8.00%; drawdown_120d -30.51% < -28.00% |
| 000652.SZ | 泰达股份 | ok | 21.53 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.31% < 6.00%; excess_return_120d -21.89% < 6.00%; excess_return_240d -39.00% < 8.00%; drawdown_120d -30.08% < -28.00% |
| 688360.SH | 德马科技 | ok | 21.53 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -12.81% < 6.00%; excess_return_120d -17.39% < 6.00%; excess_return_240d -22.28% < 8.00%; drawdown_120d -33.88% < -28.00%; volatility_120d 57.60% > 42.00% |
| 000737.SZ | 北方铜业 | ok | 21.52 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.71% < 6.00%; excess_return_120d -18.29% < 6.00%; excess_return_240d -4.09% < 8.00%; drawdown_120d -38.23% < -28.00%; volatility_120d 57.44% > 42.00% |
| 300337.SZ | 银邦股份 | ok | 21.52 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -26.37% < 6.00%; excess_return_120d -30.95% < 6.00%; excess_return_240d -16.33% < 8.00%; drawdown_120d -47.45% < -28.00%; volatility_120d 62.20% > 42.00% |
| 301060.SZ | 兰卫医学 | ok | 21.52 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -2.77% < 6.00%; excess_return_120d -7.35% < 6.00%; excess_return_240d -31.01% < 8.00%; drawdown_120d -38.63% < -28.00%; volatility_120d 53.64% > 42.00% |
| 002183.SZ | 怡亚通 | ok | 21.52 | close_below_ma200; stock_return_120d 0.63% < 6.00%; excess_return_120d -3.95% < 6.00%; excess_return_240d -15.82% < 8.00%; drawdown_120d -39.60% < -28.00%; volatility_120d 57.50% > 42.00% |
| 301525.SZ | 儒竞科技 | ok | 21.51 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.78% < 6.00%; excess_return_120d -18.36% < 6.00%; excess_return_240d -22.12% < 8.00%; drawdown_120d -30.37% < -28.00%; volatility_120d 52.72% > 42.00% |
| 002261.SZ | 拓维信息 | ok | 21.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.06% < 6.00%; excess_return_120d -13.64% < 6.00%; excess_return_240d -21.99% < 8.00%; drawdown_120d -31.68% < -28.00%; volatility_120d 56.16% > 42.00% |
| 603088.SH | 宁波精达 | ok | 21.49 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.98% < 6.00%; excess_return_120d -5.56% < 6.00%; excess_return_240d -7.94% < 8.00%; drawdown_120d -28.65% < -28.00%; volatility_120d 53.34% > 42.00% |
| 300699.SZ | 光威复材 | ok | 21.49 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.19% < 6.00%; excess_return_120d -29.77% < 6.00%; excess_return_240d -25.50% < 8.00%; drawdown_120d -37.59% < -28.00%; volatility_120d 50.97% > 42.00% |
| 300923.SZ | 研奥股份 | ok | 21.49 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.09% < 6.00%; excess_return_120d -16.67% < 6.00%; excess_return_240d -33.12% < 8.00% |
| 301565.SZ | 中仑新材 | ok | 21.48 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.69% < 6.00%; excess_return_120d -14.27% < 6.00%; excess_return_240d -28.88% < 8.00%; volatility_120d 55.43% > 42.00% |
| 002998.SZ | 优彩资源 | ok | 21.47 | close_below_ma200; stock_return_120d -1.63% < 6.00%; excess_return_120d -6.21% < 6.00%; excess_return_240d -22.05% < 8.00%; drawdown_120d -29.38% < -28.00%; volatility_120d 48.69% > 42.00% |
| 601512.SH | 中新集团 | ok | 21.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.78% < 6.00%; excess_return_120d -14.36% < 6.00%; excess_return_240d -10.17% < 8.00%; drawdown_120d -28.83% < -28.00% |
| 300847.SZ | 中船汉光 | ok | 21.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.93% < 6.00%; excess_return_120d -26.51% < 6.00%; excess_return_240d -60.23% < 8.00%; drawdown_120d -29.59% < -28.00% |
| 603277.SH | 银都股份 | ok | 21.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.10% < 6.00%; excess_return_120d -38.68% < 6.00%; excess_return_240d -50.16% < 8.00%; drawdown_120d -34.81% < -28.00% |
| 002449.SZ | 国星光电 | ok | 21.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.54% < 6.00%; excess_return_120d -19.12% < 6.00%; excess_return_240d -47.47% < 8.00%; volatility_120d 44.22% > 42.00% |
| 301508.SZ | 中机认检 | ok | 21.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.69% < 6.00%; excess_return_120d -28.27% < 6.00%; excess_return_240d -50.20% < 8.00%; drawdown_120d -29.82% < -28.00% |
| 688621.SH | 阳光诺和 | ok | 21.45 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.00% < 6.00%; excess_return_120d -13.58% < 6.00%; excess_return_240d -4.63% < 8.00%; drawdown_120d -29.97% < -28.00%; volatility_120d 48.24% > 42.00% |
| 603015.SH | 弘讯科技 | ok | 21.45 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.82% < 6.00%; excess_return_120d -13.40% < 6.00%; excess_return_240d -29.48% < 8.00%; drawdown_120d -39.33% < -28.00%; volatility_120d 58.12% > 42.00% |
| 301516.SZ | 中远通 | ok | 21.44 | close_below_ma200; stock_return_120d -0.06% < 6.00%; excess_return_120d -4.64% < 6.00%; excess_return_240d -30.24% < 8.00%; drawdown_120d -34.56% < -28.00%; volatility_120d 43.39% > 42.00% |
| 300425.SZ | 中建环能 | ok | 21.44 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.74% < 6.00%; excess_return_120d -25.32% < 6.00%; excess_return_240d -48.10% < 8.00% |
| 605258.SH | 协和电子 | ok | 21.43 | close_below_ma200; stock_return_120d -5.49% < 6.00%; excess_return_120d -10.07% < 6.00%; excess_return_240d -28.54% < 8.00%; volatility_120d 50.78% > 42.00% |
| 600729.SH | 重百集团 | ok | 21.41 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.18% < 6.00%; excess_return_120d -27.76% < 6.00%; excess_return_240d -48.97% < 8.00%; drawdown_120d -33.70% < -28.00% |
| 600968.SH | 海油发展 | ok | 21.41 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.68% < 6.00%; excess_return_120d -9.26% < 6.00%; excess_return_240d -33.16% < 8.00%; drawdown_120d -37.73% < -28.00%; volatility_120d 45.26% > 42.00% |
| 600665.SH | 天地源 | ok | 21.41 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.62% < 6.00%; excess_return_120d -12.20% < 6.00%; excess_return_240d -32.50% < 8.00%; volatility_120d 47.15% > 42.00% |
| 605179.SH | 一鸣食品 | ok | 21.40 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.75% < 6.00%; excess_return_120d -40.33% < 6.00%; excess_return_240d -54.14% < 8.00%; drawdown_120d -39.82% < -28.00% |
| 300215.SZ | 电科院 | ok | 21.40 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 2.23% < 6.00%; excess_return_120d -2.35% < 6.00%; excess_return_240d -9.76% < 8.00%; drawdown_120d -42.52% < -28.00%; volatility_120d 69.41% > 42.00% |
| 002419.SZ | 天虹股份 | ok | 21.40 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.43% < 6.00%; excess_return_120d -24.01% < 6.00%; excess_return_240d -39.02% < 8.00%; drawdown_120d -29.39% < -28.00% |
| 000017.SZ | 深中华A | ok | 21.38 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.38% < 6.00%; excess_return_120d -27.96% < 6.00%; excess_return_240d -26.88% < 8.00%; drawdown_120d -31.01% < -28.00% |
| 301428.SZ | 世纪恒通 | ok | 21.38 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.37% < 6.00%; excess_return_120d -9.95% < 6.00%; excess_return_240d -44.65% < 8.00%; drawdown_120d -36.63% < -28.00%; volatility_120d 70.23% > 42.00% |
| 002996.SZ | 顺博合金 | ok | 21.38 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.25% < 6.00%; excess_return_120d -20.83% < 6.00%; excess_return_240d -36.56% < 8.00%; drawdown_120d -31.06% < -28.00% |
| 605116.SH | 奥锐特 | ok | 21.37 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.82% < 6.00%; excess_return_120d -19.40% < 6.00%; excess_return_240d -20.87% < 8.00%; drawdown_120d -40.27% < -28.00%; volatility_120d 47.88% > 42.00% |
| 001282.SZ | 三联锻造 | ok | 21.36 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.37% < 6.00%; excess_return_120d -15.95% < 6.00%; excess_return_240d -27.30% < 8.00%; drawdown_120d -28.04% < -28.00%; volatility_120d 47.95% > 42.00% |
| 603097.SH | 江苏华辰 | ok | 21.36 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.92% < 6.00%; excess_return_120d -13.50% < 6.00%; excess_return_240d -4.40% < 8.00%; drawdown_120d -39.40% < -28.00%; volatility_120d 50.68% > 42.00% |
| 300424.SZ | 航新科技 | ok | 21.35 | close_below_ma200; stock_return_120d -13.82% < 6.00%; excess_return_120d -18.40% < 6.00%; excess_return_240d -31.33% < 8.00%; drawdown_120d -32.27% < -28.00%; volatility_120d 48.90% > 42.00% |
| 000055.SZ | 方大集团 | ok | 21.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.54% < 6.00%; excess_return_120d -23.12% < 6.00%; excess_return_240d -43.78% < 8.00% |
| 000548.SZ | 湖南投资 | ok | 21.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.07% < 6.00%; excess_return_120d -25.65% < 6.00%; excess_return_240d -42.46% < 8.00% |
| 600161.SH | 天坛生物 | ok | 21.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.36% < 6.00%; excess_return_120d -28.94% < 6.00%; excess_return_240d -57.78% < 8.00%; drawdown_120d -29.69% < -28.00% |
| 600315.SH | 上海家化 | ok | 21.34 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.65% < 6.00%; excess_return_120d -25.23% < 6.00%; excess_return_240d -36.73% < 8.00% |
| 300235.SZ | 方直科技 | ok | 21.34 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.73% < 6.00%; excess_return_120d -28.31% < 6.00%; excess_return_240d -9.26% < 8.00%; drawdown_120d -32.33% < -28.00% |
| 600382.SH | 广东明珠 | ok | 21.34 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.99% < 6.00%; excess_return_120d -11.57% < 6.00%; excess_return_240d 1.58% < 8.00%; drawdown_120d -38.11% < -28.00%; volatility_120d 62.84% > 42.00% |
| 000858.SZ | 五粮液 | ok | 21.33 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.38% < 6.00%; excess_return_120d -34.96% < 6.00%; excess_return_240d -56.98% < 8.00%; drawdown_120d -33.42% < -28.00% |
| 300127.SZ | 银河磁体 | ok | 21.32 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -5.98% < 6.00%; excess_return_120d -10.56% < 6.00%; excess_return_240d -19.42% < 8.00%; drawdown_120d -32.36% < -28.00%; volatility_120d 45.95% > 42.00% |
| 688373.SH | 盟科药业 | ok | 21.32 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.07% < 6.00%; excess_return_120d -18.65% < 6.00%; excess_return_240d -46.53% < 8.00% |
| 301289.SZ | 国缆检测 | ok | 21.31 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.67% < 6.00%; excess_return_120d -25.25% < 6.00%; excess_return_240d -27.40% < 8.00%; drawdown_120d -29.58% < -28.00% |
| 000159.SZ | 国际实业 | ok | 21.31 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.63% < 6.00%; excess_return_120d -8.21% < 6.00%; excess_return_240d -25.39% < 8.00%; drawdown_120d -32.57% < -28.00%; volatility_120d 46.46% > 42.00% |
| 000919.SZ | 金陵药业 | ok | 21.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.64% < 6.00%; excess_return_120d -25.22% < 6.00%; excess_return_240d -29.48% < 8.00%; drawdown_120d -35.77% < -28.00% |
| 688356.SH | 键凯科技 | ok | 21.30 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -1.67% < 6.00%; excess_return_120d -6.25% < 6.00%; excess_return_240d -9.48% < 8.00%; drawdown_120d -31.98% < -28.00%; volatility_120d 52.53% > 42.00% |
| 600223.SH | 福瑞达 | ok | 21.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.49% < 6.00%; excess_return_120d -31.07% < 6.00%; excess_return_240d -55.44% < 8.00%; drawdown_120d -29.92% < -28.00% |
| 688302.SH | 海创药业 | ok | 21.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.45% < 6.00%; excess_return_120d -23.03% < 6.00%; excess_return_240d -39.43% < 8.00%; volatility_120d 46.53% > 42.00% |
| 603639.SH | 海利尔 | ok | 21.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.98% < 6.00%; excess_return_120d -20.56% < 6.00%; excess_return_240d -43.67% < 8.00%; drawdown_120d -28.63% < -28.00% |
| 600794.SH | 保税科技 | ok | 21.29 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.91% < 6.00%; excess_return_120d -26.49% < 6.00%; excess_return_240d -61.80% < 8.00% |
| 688563.SH | 航材股份 | ok | 21.29 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.37% < 6.00%; excess_return_120d -16.95% < 6.00%; excess_return_240d -29.27% < 8.00%; drawdown_120d -35.07% < -28.00%; volatility_120d 45.82% > 42.00% |
| 600893.SH | 航发动力 | ok | 21.28 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.15% < 6.00%; excess_return_120d -7.73% < 6.00%; excess_return_240d -17.34% < 8.00%; drawdown_120d -39.25% < -28.00%; volatility_120d 56.19% > 42.00% |
| 002863.SZ | 今飞凯达 | ok | 21.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.89% < 6.00%; excess_return_120d -28.47% < 6.00%; excess_return_240d -34.83% < 8.00%; drawdown_120d -28.64% < -28.00% |
| 300082.SZ | 奥克股份 | ok | 21.28 | close_below_ma200; stock_return_120d -11.31% < 6.00%; excess_return_120d -15.89% < 6.00%; excess_return_240d -2.93% < 8.00%; drawdown_120d -35.11% < -28.00%; volatility_120d 56.53% > 42.00% |
| 002817.SZ | 黄山胶囊 | ok | 21.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.19% < 6.00%; excess_return_120d -21.77% < 6.00%; excess_return_240d -37.81% < 8.00% |
| 000789.SZ | 万年青 | ok | 21.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.15% < 6.00%; excess_return_120d -26.73% < 6.00%; excess_return_240d -52.17% < 8.00%; drawdown_120d -31.09% < -28.00% |
| 300268.SZ | 佳沃食品 | ok | 21.28 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.88% < 6.00%; excess_return_120d -21.98% < 6.00%; excess_return_240d -15.98% < 8.00%; volatility_120d 43.64% > 42.00% |
| 603035.SH | 常熟汽饰 | ok | 21.27 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.72% < 6.00%; excess_return_120d -30.30% < 6.00%; excess_return_240d -34.80% < 8.00%; drawdown_120d -32.02% < -28.00% |
| 002125.SZ | 湘潭电化 | ok | 21.27 | close_below_ma200; stock_return_120d -8.65% < 6.00%; excess_return_120d -13.23% < 6.00%; excess_return_240d -27.55% < 8.00%; drawdown_120d -38.49% < -28.00%; volatility_120d 51.78% > 42.00% |
| 000557.SZ | 西部创业 | ok | 21.26 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.31% < 6.00%; excess_return_120d -30.89% < 6.00%; excess_return_240d -49.56% < 8.00%; drawdown_120d -31.40% < -28.00% |
| 605099.SH | 共创草坪 | ok | 21.26 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.73% < 6.00%; excess_return_120d -9.31% < 6.00%; excess_return_240d -26.67% < 8.00%; drawdown_120d -39.67% < -28.00%; volatility_120d 62.94% > 42.00% |
| 600805.SH | 悦达投资 | ok | 21.26 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.47% < 6.00%; excess_return_120d -27.05% < 6.00%; excess_return_240d -37.90% < 8.00%; drawdown_120d -29.12% < -28.00% |
| 600081.SH | 东风科技 | ok | 21.26 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.93% < 6.00%; excess_return_120d -23.52% < 6.00%; excess_return_240d -47.33% < 8.00% |
| 001317.SZ | 三羊马 | ok | 21.25 | close_below_ma200; stock_return_120d -20.90% < 6.00%; excess_return_120d -25.48% < 6.00%; excess_return_240d -27.96% < 8.00%; drawdown_120d -29.67% < -28.00%; volatility_120d 51.14% > 42.00% |
| 002554.SZ | 惠博普 | ok | 21.24 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.61% < 6.00%; excess_return_120d -12.90% < 6.00%; excess_return_240d -15.09% < 8.00%; drawdown_120d -39.96% < -28.00%; volatility_120d 52.30% > 42.00% |
| 000419.SZ | 通程控股 | ok | 21.24 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.20% < 6.00%; excess_return_120d -29.78% < 6.00%; excess_return_240d -36.19% < 8.00%; drawdown_120d -29.50% < -28.00% |
| 600278.SH | 东方创业 | ok | 21.24 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.68% < 6.00%; excess_return_120d -23.26% < 6.00%; excess_return_240d -35.23% < 8.00%; drawdown_120d -33.04% < -28.00% |
| 601022.SH | 宁波远洋 | ok | 21.24 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.92% < 6.00%; excess_return_120d -17.50% < 6.00%; excess_return_240d -41.72% < 8.00%; drawdown_120d -29.05% < -28.00% |
| 002951.SZ | 金时科技 | ok | 21.23 | close_below_ma200; stock_return_120d -9.46% < 6.00%; excess_return_120d -14.04% < 6.00%; excess_return_240d -35.34% < 8.00%; drawdown_120d -45.58% < -28.00%; volatility_120d 69.65% > 42.00% |
| 688005.SH | 容百科技 | ok | 21.23 | close_below_ma200; stock_return_120d -20.18% < 6.00%; excess_return_120d -24.14% < 6.00%; excess_return_240d -6.07% < 8.00%; drawdown_120d -33.38% < -28.00%; volatility_120d 61.47% > 42.00% |
| 000679.SZ | 大连友谊 | ok | 21.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.19% < 6.00%; excess_return_120d -18.77% < 6.00%; excess_return_240d -26.95% < 8.00% |
| 000868.SZ | 安凯客车 | ok | 21.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.92% < 6.00%; excess_return_120d -35.50% < 6.00%; excess_return_240d -61.37% < 8.00%; drawdown_120d -32.68% < -28.00% |
| 300160.SZ | 秀强股份 | ok | 21.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.17% < 6.00%; excess_return_120d -22.75% < 6.00%; excess_return_240d -52.88% < 8.00%; drawdown_120d -29.14% < -28.00% |
| 002946.SZ | 新乳业 | ok | 21.23 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.03% < 6.00%; excess_return_120d -23.61% < 6.00%; excess_return_240d -33.69% < 8.00% |
| 601588.SH | 北辰实业 | ok | 21.22 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -5.17% < 6.00%; excess_return_120d -9.75% < 6.00%; excess_return_240d -31.42% < 8.00%; drawdown_120d -29.49% < -28.00%; volatility_120d 47.49% > 42.00% |
| 002186.SZ | 全聚德 | ok | 21.22 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.04% < 6.00%; excess_return_120d -29.62% < 6.00%; excess_return_240d -39.11% < 8.00%; drawdown_120d -30.91% < -28.00% |
| 301390.SZ | 经纬股份 | ok | 21.22 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.51% < 6.00%; excess_return_120d -12.09% < 6.00%; excess_return_240d -39.16% < 8.00%; drawdown_120d -28.87% < -28.00% |
| 300667.SZ | 必创科技 | ok | 21.22 | close_below_ma200; stock_return_120d -13.07% < 6.00%; excess_return_120d -17.65% < 6.00%; excess_return_240d -22.76% < 8.00%; drawdown_120d -29.11% < -28.00%; volatility_120d 62.47% > 42.00% |
| 301058.SZ | 中粮科工 | ok | 21.22 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.35% < 6.00%; excess_return_120d -29.93% < 6.00%; excess_return_240d -48.00% < 8.00%; drawdown_120d -33.14% < -28.00% |
| 300133.SZ | 华策影视 | ok | 21.21 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.87% < 6.00%; excess_return_120d -17.45% < 6.00%; excess_return_240d -25.44% < 8.00%; drawdown_120d -36.71% < -28.00%; volatility_120d 66.01% > 42.00% |
| 688297.SH | 中无人机 | ok | 21.21 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.38% < 6.00%; excess_return_120d -15.96% < 6.00%; excess_return_240d -36.93% < 8.00%; drawdown_120d -35.01% < -28.00%; volatility_120d 56.85% > 42.00% |
| 600585.SH | 海螺水泥 | ok | 21.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.06% < 6.00%; excess_return_120d -23.64% < 6.00%; excess_return_240d -41.21% < 8.00%; drawdown_120d -34.65% < -28.00% |
| 002561.SZ | 徐家汇 | ok | 21.20 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.97% < 6.00%; excess_return_120d -30.55% < 6.00%; excess_return_240d -45.16% < 8.00%; drawdown_120d -36.59% < -28.00% |
| 001318.SZ | 阳光乳业 | ok | 21.20 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.47% < 6.00%; excess_return_120d -36.05% < 6.00%; excess_return_240d -39.23% < 8.00%; drawdown_120d -34.25% < -28.00% |
| 600518.SH | 康美药业 | ok | 21.20 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.94% < 6.00%; excess_return_120d -36.52% < 6.00%; excess_return_240d -53.39% < 8.00%; drawdown_120d -35.96% < -28.00% |
| 002351.SZ | 漫步者 | ok | 21.20 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.68% < 6.00%; excess_return_120d -26.26% < 6.00%; excess_return_240d -51.04% < 8.00%; drawdown_120d -30.26% < -28.00% |
| 301408.SZ | 华人健康 | ok | 21.20 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.39% < 6.00%; excess_return_120d -21.97% < 6.00%; excess_return_240d -14.60% < 8.00%; drawdown_120d -48.58% < -28.00%; volatility_120d 73.32% > 42.00% |
| 301239.SZ | 普瑞眼科 | ok | 21.19 | close_below_ma200; stock_return_120d -3.89% < 6.00%; excess_return_120d -8.47% < 6.00%; excess_return_240d -40.09% < 8.00%; drawdown_120d -34.58% < -28.00%; volatility_120d 42.97% > 42.00% |
| 600217.SH | 中再资环 | ok | 21.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.23% < 6.00%; excess_return_120d -30.81% < 6.00%; excess_return_240d -54.21% < 8.00%; drawdown_120d -32.66% < -28.00% |
| 603182.SH | 嘉华股份 | ok | 21.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.59% < 6.00%; excess_return_120d -27.08% < 6.00%; excess_return_240d -28.91% < 8.00%; drawdown_120d -31.13% < -28.00% |
| 300095.SZ | 华伍股份 | ok | 21.19 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -26.82% < 6.00%; excess_return_120d -31.40% < 6.00%; excess_return_240d -30.03% < 8.00%; drawdown_120d -33.31% < -28.00%; volatility_120d 45.95% > 42.00% |
| 300797.SZ | 钢研纳克 | ok | 21.18 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.94% < 6.00%; excess_return_120d -24.52% < 6.00%; excess_return_240d -25.47% < 8.00%; drawdown_120d -28.12% < -28.00% |
| 300293.SZ | 蓝英装备 | ok | 21.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.82% < 6.00%; excess_return_120d -19.40% < 6.00%; excess_return_240d -48.62% < 8.00%; volatility_120d 43.74% > 42.00% |
| 300358.SZ | 楚天科技 | ok | 21.16 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.99% < 6.00%; excess_return_120d -18.57% < 6.00%; excess_return_240d -16.07% < 8.00%; drawdown_120d -38.62% < -28.00% |
| 301316.SZ | 慧博云通 | ok | 21.16 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -5.76% < 6.00%; excess_return_120d -10.35% < 6.00%; excess_return_240d -16.36% < 8.00%; drawdown_120d -31.55% < -28.00%; volatility_120d 62.84% > 42.00% |
| 688133.SH | 泰坦科技 | ok | 21.15 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.68% < 6.00%; excess_return_120d -12.26% < 6.00%; excess_return_240d -38.48% < 8.00%; drawdown_120d -33.64% < -28.00%; volatility_120d 64.34% > 42.00% |
| 000421.SZ | 南京公用 | ok | 21.15 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.90% < 6.00%; excess_return_120d -26.48% < 6.00%; excess_return_240d -40.89% < 8.00%; drawdown_120d -30.25% < -28.00% |
| 603099.SH | 长白山 | ok | 21.15 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.35% < 6.00%; excess_return_120d -24.93% < 6.00%; excess_return_240d -28.23% < 8.00%; drawdown_120d -31.11% < -28.00% |
| 300688.SZ | 创业黑马 | ok | 21.14 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.53% < 6.00%; excess_return_120d -18.11% < 6.00%; excess_return_240d -46.42% < 8.00%; drawdown_120d -28.96% < -28.00%; volatility_120d 54.99% > 42.00% |
| 301589.SZ | 诺瓦星云 | ok | 21.13 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.08% < 6.00%; excess_return_120d -16.66% < 6.00%; excess_return_240d -24.86% < 8.00%; drawdown_120d -34.29% < -28.00% |
| 002698.SZ | 博实股份 | ok | 21.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.70% < 6.00%; excess_return_120d -25.28% < 6.00%; excess_return_240d -35.48% < 8.00%; drawdown_120d -29.73% < -28.00% |
| 301175.SZ | 中科环保 | ok | 21.13 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.56% < 6.00%; excess_return_120d -17.14% < 6.00%; excess_return_240d -23.22% < 8.00%; drawdown_120d -36.02% < -28.00%; volatility_120d 42.15% > 42.00% |
| 300534.SZ | 陇神戎发 | ok | 21.12 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.66% < 6.00%; excess_return_120d -24.24% < 6.00%; excess_return_240d -44.48% < 8.00%; drawdown_120d -35.76% < -28.00% |
| 003011.SZ | 海象新材 | ok | 21.12 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.17% < 6.00%; excess_return_120d -13.75% < 6.00%; excess_return_240d -13.39% < 8.00%; drawdown_120d -31.36% < -28.00%; volatility_120d 51.63% > 42.00% |
| 002035.SZ | 华帝股份 | ok | 21.12 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.89% < 6.00%; excess_return_120d -26.47% < 6.00%; excess_return_240d -45.01% < 8.00%; drawdown_120d -31.45% < -28.00% |
| 600051.SH | 宁波联合 | ok | 21.12 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.19% < 6.00%; excess_return_120d -24.77% < 6.00%; excess_return_240d -40.96% < 8.00% |
| 300851.SZ | 交大思诺 | ok | 21.12 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.77% < 6.00%; excess_return_120d -13.50% < 6.00%; excess_return_240d -35.69% < 8.00%; drawdown_120d -39.10% < -28.00% |
| 300639.SZ | 凯普生物 | ok | 21.12 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.93% < 6.00%; excess_return_120d -5.51% < 6.00%; excess_return_240d -32.26% < 8.00%; drawdown_120d -47.07% < -28.00%; volatility_120d 64.02% > 42.00% |
| 002019.SZ | 亿帆医药 | ok | 21.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.83% < 6.00%; excess_return_120d -18.41% < 6.00%; excess_return_240d -49.28% < 8.00%; drawdown_120d -30.14% < -28.00% |
| 002991.SZ | 甘源食品 | ok | 21.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.51% < 6.00%; excess_return_120d -29.09% < 6.00%; excess_return_240d -50.62% < 8.00%; drawdown_120d -33.53% < -28.00% |
| 300988.SZ | 津荣天宇 | ok | 21.11 | close_below_ma200; stock_return_120d -2.79% < 6.00%; excess_return_120d -7.37% < 6.00%; excess_return_240d -14.69% < 8.00%; drawdown_120d -29.54% < -28.00%; volatility_120d 43.75% > 42.00% |
| 002576.SZ | 通达动力 | ok | 21.11 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.86% < 6.00%; excess_return_120d -18.44% < 6.00%; excess_return_240d -30.90% < 8.00% |
| 001356.SZ | 富岭股份 | ok | 21.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.34% < 6.00%; excess_return_120d -36.92% < 6.00%; excess_return_240d -65.08% < 8.00%; drawdown_120d -35.01% < -28.00% |
| 603367.SH | 辰欣药业 | ok | 21.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.59% < 6.00%; excess_return_120d -23.17% < 6.00%; excess_return_240d -28.41% < 8.00% |
| 603871.SH | 嘉友国际 | ok | 21.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.86% < 6.00%; excess_return_120d -20.44% < 6.00%; excess_return_240d -8.12% < 8.00%; drawdown_120d -29.24% < -28.00%; volatility_120d 43.60% > 42.00% |
| 002382.SZ | 蓝帆医疗 | ok | 21.11 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.46% < 6.00%; excess_return_120d -9.04% < 6.00%; excess_return_240d -32.08% < 8.00%; drawdown_120d -39.96% < -28.00% |
| 300858.SZ | 科拓生物 | ok | 21.10 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.63% < 6.00%; excess_return_120d -12.21% < 6.00%; excess_return_240d -36.59% < 8.00%; drawdown_120d -42.80% < -28.00%; volatility_120d 55.19% > 42.00% |
| 600761.SH | 安徽合力 | ok | 21.10 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.58% < 6.00%; excess_return_120d -21.16% < 6.00%; excess_return_240d -25.10% < 8.00%; drawdown_120d -28.80% < -28.00%; volatility_120d 43.53% > 42.00% |
| 001367.SZ | 海森药业 | ok | 21.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -8.86% < 6.00%; excess_return_120d -13.44% < 6.00%; excess_return_240d -35.37% < 8.00%; drawdown_120d -28.63% < -28.00% |
| 600663.SH | 陆家嘴 | ok | 21.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.73% < 6.00%; excess_return_120d -23.31% < 6.00%; excess_return_240d -49.63% < 8.00%; drawdown_120d -28.23% < -28.00% |
| 002423.SZ | 中粮资本 | ok | 21.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.42% < 6.00%; excess_return_120d -28.00% < 6.00%; excess_return_240d -49.08% < 8.00%; drawdown_120d -28.49% < -28.00% |
| 002148.SZ | 北纬科技 | ok | 21.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.46% < 6.00%; excess_return_120d -26.04% < 6.00%; excess_return_240d -22.09% < 8.00% |
| 300224.SZ | 正海磁材 | ok | 21.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.33% < 6.00%; excess_return_120d -16.91% < 6.00%; excess_return_240d -25.67% < 8.00%; drawdown_120d -31.74% < -28.00%; volatility_120d 46.25% > 42.00% |
| 300979.SZ | 华利集团 | ok | 21.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.02% < 6.00%; excess_return_120d -39.60% < 6.00%; excess_return_240d -59.30% < 8.00%; drawdown_120d -37.11% < -28.00% |
| 300203.SZ | 聚光科技 | ok | 21.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.47% < 6.00%; excess_return_120d -23.05% < 6.00%; excess_return_240d -58.63% < 8.00%; volatility_120d 47.19% > 42.00% |
| 001914.SZ | 招商积余 | ok | 21.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.01% < 6.00%; excess_return_120d -23.59% < 6.00%; excess_return_240d -48.35% < 8.00%; drawdown_120d -29.39% < -28.00% |
| 603206.SH | 嘉环科技 | ok | 21.07 | close_below_ma200; stock_return_120d -14.05% < 6.00%; excess_return_120d -18.63% < 6.00%; excess_return_240d -33.67% < 8.00%; drawdown_120d -35.80% < -28.00%; volatility_120d 46.81% > 42.00% |
| 600938.SH | 中国海油 | ok | 21.07 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.33% < 6.00%; excess_return_120d -10.91% < 6.00%; excess_return_240d -7.05% < 8.00%; drawdown_120d -36.53% < -28.00%; volatility_120d 45.69% > 42.00% |
| 301459.SZ | 丰茂股份 | ok | 21.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.87% < 6.00%; excess_return_120d -24.45% < 6.00%; excess_return_240d -36.16% < 8.00%; drawdown_120d -35.39% < -28.00%; volatility_120d 45.04% > 42.00% |
| 600515.SH | 海南机场 | ok | 21.06 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -47.47% < 6.00%; excess_return_120d -52.05% < 6.00%; excess_return_240d -44.49% < 8.00%; drawdown_120d -46.77% < -28.00% |
| 600170.SH | 上海建工 | ok | 21.06 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.19% < 6.00%; excess_return_120d -17.77% < 6.00%; excess_return_240d -23.04% < 8.00%; drawdown_120d -29.61% < -28.00% |
| 603275.SH | 众辰科技 | ok | 21.04 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.67% < 6.00%; excess_return_120d -16.25% < 6.00%; excess_return_240d -37.05% < 8.00%; volatility_120d 42.83% > 42.00% |
| 688267.SH | 中触媒 | ok | 21.04 | close_below_ma200; stock_return_120d -10.25% < 6.00%; excess_return_120d -14.83% < 6.00%; excess_return_240d -41.09% < 8.00%; drawdown_120d -29.40% < -28.00% |
| 002608.SZ | 江苏国信 | ok | 21.04 | close_below_ma200; stock_return_120d -5.41% < 6.00%; excess_return_120d -9.99% < 6.00%; excess_return_240d -29.84% < 8.00%; drawdown_120d -37.20% < -28.00% |
| 002375.SZ | 亚厦股份 | ok | 21.03 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.80% < 6.00%; excess_return_120d -12.38% < 6.00%; excess_return_240d -33.67% < 8.00%; drawdown_120d -31.80% < -28.00% |
| 300989.SZ | 蕾奥规划 | ok | 21.03 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.83% < 6.00%; excess_return_120d -32.41% < 6.00%; excess_return_240d -47.81% < 8.00%; drawdown_120d -28.04% < -28.00% |
| 000156.SZ | 华数传媒 | ok | 21.03 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.08% < 6.00%; excess_return_120d -17.66% < 6.00%; excess_return_240d -37.59% < 8.00%; drawdown_120d -34.27% < -28.00% |
| 002999.SZ | 天禾股份 | ok | 21.03 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.68% < 6.00%; excess_return_120d -20.26% < 6.00%; excess_return_240d -39.67% < 8.00%; drawdown_120d -30.15% < -28.00% |
| 601996.SH | 丰林集团 | ok | 21.02 | close_below_ma200; stock_return_120d -3.11% < 6.00%; excess_return_120d -7.69% < 6.00%; excess_return_240d -24.21% < 8.00%; drawdown_120d -31.87% < -28.00%; volatility_120d 49.62% > 42.00% |
| 300962.SZ | 中金辐照 | ok | 21.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.29% < 6.00%; excess_return_120d -23.87% < 6.00%; excess_return_240d -45.42% < 8.00%; drawdown_120d -32.65% < -28.00% |
| 000401.SZ | 金隅冀东 | ok | 21.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.87% < 6.00%; excess_return_120d -22.45% < 6.00%; excess_return_240d -41.72% < 8.00%; drawdown_120d -32.95% < -28.00% |
| 002027.SZ | 分众传媒 | ok | 21.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.34% < 6.00%; excess_return_120d -35.92% < 6.00%; excess_return_240d -52.07% < 8.00%; drawdown_120d -39.18% < -28.00% |
| 301108.SZ | 洁雅股份 | ok | 21.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.42% < 6.00%; excess_return_120d -25.00% < 6.00%; excess_return_240d -7.87% < 8.00%; drawdown_120d -30.01% < -28.00% |
| 300577.SZ | 开润股份 | ok | 21.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.10% < 6.00%; excess_return_120d -22.68% < 6.00%; excess_return_240d -33.75% < 8.00%; drawdown_120d -30.31% < -28.00% |
| 300516.SZ | 久之洋 | ok | 21.01 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -40.04% < 6.00%; excess_return_120d -44.62% < 6.00%; excess_return_240d -0.34% < 8.00%; drawdown_120d -51.01% < -28.00%; volatility_120d 67.06% > 42.00% |
| 601828.SH | 美凯龙 | ok | 21.01 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.11% < 6.00%; excess_return_120d -25.69% < 6.00%; excess_return_240d -50.57% < 8.00%; drawdown_120d -30.62% < -28.00% |
| 688265.SH | 南模生物 | ok | 21.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.10% < 6.00%; excess_return_120d -11.68% < 6.00%; excess_return_240d -0.53% < 8.00%; drawdown_120d -35.18% < -28.00%; volatility_120d 45.32% > 42.00% |
| 002757.SZ | 南兴股份 | ok | 21.00 | close_below_ma200; stock_return_120d -7.94% < 6.00%; excess_return_120d -12.52% < 6.00%; excess_return_240d -21.60% < 8.00%; drawdown_120d -45.58% < -28.00%; volatility_120d 73.40% > 42.00% |
| 300884.SZ | 狄耐克 | ok | 21.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.92% < 6.00%; excess_return_120d -23.50% < 6.00%; excess_return_240d -30.40% < 8.00%; drawdown_120d -37.53% < -28.00% |
| 002358.SZ | 森源电气 | ok | 21.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 1.29% < 6.00%; excess_return_120d -3.29% < 6.00%; excess_return_240d -15.32% < 8.00%; drawdown_120d -42.21% < -28.00%; volatility_120d 54.01% > 42.00% |
| 300496.SZ | 中科创达 | ok | 21.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.13% < 6.00%; excess_return_120d -16.71% < 6.00%; excess_return_240d -13.60% < 8.00%; drawdown_120d -33.75% < -28.00%; volatility_120d 48.54% > 42.00% |
| 688289.SH | 圣湘生物 | ok | 21.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.88% < 6.00%; excess_return_120d -23.46% < 6.00%; excess_return_240d -45.90% < 8.00%; drawdown_120d -32.88% < -28.00% |
| 600562.SH | 国睿科技 | ok | 20.99 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.71% < 6.00%; excess_return_120d -20.29% < 6.00%; excess_return_240d -42.57% < 8.00%; drawdown_120d -31.88% < -28.00%; volatility_120d 44.88% > 42.00% |
| 000788.SZ | 北大医药 | ok | 20.98 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.97% < 6.00%; excess_return_120d -15.55% < 6.00%; excess_return_240d -36.62% < 8.00%; drawdown_120d -32.61% < -28.00%; volatility_120d 42.81% > 42.00% |
| 301220.SZ | 亚香股份 | ok | 20.98 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.10% < 6.00%; excess_return_120d -13.68% < 6.00%; excess_return_240d -43.18% < 8.00%; drawdown_120d -31.78% < -28.00%; volatility_120d 45.73% > 42.00% |
| 301088.SZ | 戎美股份 | ok | 20.98 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.15% < 6.00%; excess_return_120d -31.73% < 6.00%; excess_return_240d -30.66% < 8.00%; drawdown_120d -36.71% < -28.00% |
| 300172.SZ | 中电环保 | ok | 20.98 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.75% < 6.00%; excess_return_120d -25.33% < 6.00%; excess_return_240d -47.23% < 8.00%; drawdown_120d -35.37% < -28.00% |
| 603062.SH | 麦加芯彩 | ok | 20.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.98% < 6.00%; excess_return_120d -15.56% < 6.00%; excess_return_240d -30.15% < 8.00%; drawdown_120d -30.17% < -28.00% |
| 001239.SZ | 永达股份 | ok | 20.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.77% < 6.00%; excess_return_120d -25.35% < 6.00%; excess_return_240d -35.47% < 8.00% |
| 300961.SZ | 深水海纳 | ok | 20.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.32% < 6.00%; excess_return_120d -15.90% < 6.00%; excess_return_240d -56.09% < 8.00%; drawdown_120d -29.42% < -28.00%; volatility_120d 64.13% > 42.00% |
| 000803.SZ | 山高环能 | ok | 20.97 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.22% < 6.00%; excess_return_120d -7.80% < 6.00%; excess_return_240d -15.61% < 8.00%; drawdown_120d -38.60% < -28.00%; volatility_120d 50.85% > 42.00% |
| 301429.SZ | 森泰股份 | ok | 20.97 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.34% < 6.00%; excess_return_120d -15.92% < 6.00%; excess_return_240d -32.15% < 8.00%; drawdown_120d -29.68% < -28.00% |
| 301090.SZ | 华润材料 | ok | 20.97 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.26% < 6.00%; excess_return_120d -9.84% < 6.00%; excess_return_240d -36.13% < 8.00%; drawdown_120d -29.64% < -28.00%; volatility_120d 44.08% > 42.00% |
| 688586.SH | 江航装备 | ok | 20.96 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.32% < 6.00%; excess_return_120d -17.90% < 6.00%; excess_return_240d -16.79% < 8.00%; drawdown_120d -37.83% < -28.00%; volatility_120d 64.37% > 42.00% |
| 603230.SH | 内蒙新华 | ok | 20.96 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.75% < 6.00%; excess_return_120d -29.33% < 6.00%; excess_return_240d -50.15% < 8.00%; drawdown_120d -30.87% < -28.00% |
| 300760.SZ | 迈瑞医疗 | ok | 20.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.57% < 6.00%; excess_return_120d -30.15% < 6.00%; excess_return_240d -55.12% < 8.00%; drawdown_120d -33.85% < -28.00% |
| 600609.SH | 金杯汽车 | ok | 20.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.89% < 6.00%; excess_return_120d -34.47% < 6.00%; excess_return_240d -59.42% < 8.00%; drawdown_120d -37.49% < -28.00% |
| 300839.SZ | 博汇股份 | ok | 20.94 | close_below_ma200; stock_return_120d -0.33% < 6.00%; excess_return_120d -4.91% < 6.00%; excess_return_240d -5.49% < 8.00%; drawdown_120d -42.14% < -28.00%; volatility_120d 69.83% > 42.00% |
| 688062.SH | 迈威生物 | ok | 20.94 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.93% < 6.00%; excess_return_120d -16.51% < 6.00%; excess_return_240d -10.34% < 8.00%; drawdown_120d -29.12% < -28.00%; volatility_120d 52.37% > 42.00% |
| 003037.SZ | 三和管桩 | ok | 20.94 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.60% < 6.00%; excess_return_120d -28.18% < 6.00%; excess_return_240d -38.78% < 8.00%; drawdown_120d -31.21% < -28.00% |
| 600038.SH | 中直股份 | ok | 20.94 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.75% < 6.00%; excess_return_120d -32.33% < 6.00%; excess_return_240d -53.13% < 8.00%; drawdown_120d -33.62% < -28.00% |
| 003012.SZ | 东鹏控股 | ok | 20.94 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.44% < 6.00%; excess_return_120d -31.02% < 6.00%; excess_return_240d -36.39% < 8.00%; drawdown_120d -37.20% < -28.00% |
| 600241.SH | 时代万恒 | ok | 20.93 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.26% < 6.00%; excess_return_120d -15.84% < 6.00%; excess_return_240d -35.33% < 8.00%; drawdown_120d -29.09% < -28.00% |
| 300144.SZ | 宋城演艺 | ok | 20.93 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.82% < 6.00%; excess_return_120d -29.40% < 6.00%; excess_return_240d -48.92% < 8.00%; drawdown_120d -35.19% < -28.00% |
| 600859.SH | 王府井 | ok | 20.93 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.93% < 6.00%; excess_return_120d -42.51% < 6.00%; excess_return_240d -51.19% < 8.00%; drawdown_120d -41.04% < -28.00% |
| 300930.SZ | 屹通新材 | ok | 20.93 | close_below_ma200; stock_return_120d -7.57% < 6.00%; excess_return_120d -12.15% < 6.00%; excess_return_240d -40.20% < 8.00%; drawdown_120d -31.39% < -28.00%; volatility_120d 48.79% > 42.00% |
| 002582.SZ | 好想你 | ok | 20.92 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.18% < 6.00%; excess_return_120d -17.77% < 6.00%; excess_return_240d -23.97% < 8.00%; drawdown_120d -43.18% < -28.00%; volatility_120d 48.94% > 42.00% |
| 002322.SZ | 理工能科 | ok | 20.92 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.21% < 6.00%; excess_return_120d -17.79% < 6.00%; excess_return_240d -35.97% < 8.00%; drawdown_120d -33.46% < -28.00% |
| 600436.SH | 片仔癀 | ok | 20.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.89% < 6.00%; excess_return_120d -36.47% < 6.00%; excess_return_240d -62.28% < 8.00%; drawdown_120d -34.54% < -28.00% |
| 002242.SZ | 九阳股份 | ok | 20.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.83% < 6.00%; excess_return_120d -24.41% < 6.00%; excess_return_240d -33.98% < 8.00%; drawdown_120d -33.47% < -28.00% |
| 000517.SZ | 荣安地产 | ok | 20.91 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -4.97% < 6.00%; excess_return_120d -9.55% < 6.00%; excess_return_240d -29.61% < 8.00%; drawdown_120d -31.47% < -28.00%; volatility_120d 45.43% > 42.00% |
| 000927.SZ | 中国铁物 | ok | 20.90 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.06% < 6.00%; excess_return_120d -12.64% < 6.00%; excess_return_240d -29.52% < 8.00%; drawdown_120d -30.32% < -28.00%; volatility_120d 42.39% > 42.00% |
| 301367.SZ | 瑞迈特 | ok | 20.90 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.51% < 6.00%; excess_return_120d -29.09% < 6.00%; excess_return_240d -42.12% < 8.00%; drawdown_120d -35.34% < -28.00% |
| 301039.SZ | 中集车辆 | ok | 20.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.32% < 6.00%; excess_return_120d -23.90% < 6.00%; excess_return_240d -32.90% < 8.00%; drawdown_120d -29.91% < -28.00% |
| 605158.SH | 华达新材 | ok | 20.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.89% < 6.00%; excess_return_120d -20.48% < 6.00%; excess_return_240d -40.42% < 8.00%; volatility_120d 42.98% > 42.00% |
| 600405.SH | 动力源 | ok | 20.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.69% < 6.00%; excess_return_120d -15.79% < 6.00%; excess_return_240d -40.23% < 8.00%; volatility_120d 44.49% > 42.00% |
| 605300.SH | 佳禾食品 | ok | 20.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.00% < 6.00%; excess_return_120d -25.58% < 6.00%; excess_return_240d -56.90% < 8.00% |
| 001333.SZ | 光华股份 | ok | 20.89 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.06% < 6.00%; excess_return_120d -9.64% < 6.00%; excess_return_240d -22.67% < 8.00%; volatility_120d 43.01% > 42.00% |
| 000670.SZ | 盈方微 | ok | 20.89 | close_below_ma200; stock_return_120d -0.55% < 6.00%; excess_return_120d -6.27% < 6.00%; excess_return_240d -17.07% < 8.00%; drawdown_120d -35.62% < -28.00%; volatility_120d 68.40% > 42.00% |
| 300351.SZ | 永贵电器 | ok | 20.88 | close_below_ma200; stock_return_120d -11.56% < 6.00%; excess_return_120d -16.14% < 6.00%; excess_return_240d -24.02% < 8.00%; drawdown_120d -43.90% < -28.00%; volatility_120d 62.22% > 42.00% |
| 600956.SH | 新天绿能 | ok | 20.87 | close_below_ma200; stock_return_120d -3.17% < 6.00%; excess_return_120d -7.75% < 6.00%; excess_return_240d -28.12% < 8.00%; drawdown_120d -37.54% < -28.00%; volatility_120d 48.90% > 42.00% |
| 002205.SZ | 国统股份 | ok | 20.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.03% < 6.00%; excess_return_120d -24.61% < 6.00%; excess_return_240d -30.02% < 8.00%; drawdown_120d -29.94% < -28.00% |
| 688616.SH | 西力科技 | ok | 20.87 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.86% < 6.00%; excess_return_120d -17.44% < 6.00%; excess_return_240d -39.17% < 8.00%; drawdown_120d -32.27% < -28.00% |
| 600697.SH | 欧亚集团 | ok | 20.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.90% < 6.00%; excess_return_120d -27.48% < 6.00%; excess_return_240d -38.41% < 8.00%; drawdown_120d -29.13% < -28.00% |
| 300204.SZ | 舒泰神 | ok | 20.86 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -7.21% < 6.00%; excess_return_120d -11.79% < 6.00%; excess_return_240d -58.70% < 8.00%; volatility_120d 65.93% > 42.00% |
| 000738.SZ | 航发控制 | ok | 20.86 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.81% < 6.00%; excess_return_120d -18.39% < 6.00%; excess_return_240d -29.93% < 8.00%; drawdown_120d -39.15% < -28.00%; volatility_120d 53.45% > 42.00% |
| 688030.SH | 山石网科 | ok | 20.86 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.25% < 6.00%; excess_return_120d -18.83% < 6.00%; excess_return_240d -22.80% < 8.00%; drawdown_120d -28.07% < -28.00%; volatility_120d 43.72% > 42.00% |
| 600716.SH | 凤凰股份 | ok | 20.86 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.89% < 6.00%; excess_return_120d -16.47% < 6.00%; excess_return_240d -30.89% < 8.00%; drawdown_120d -30.69% < -28.00% |
| 688670.SH | 金迪克 | ok | 20.86 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.44% < 6.00%; excess_return_120d -23.02% < 6.00%; excess_return_240d -4.32% < 8.00%; drawdown_120d -35.82% < -28.00%; volatility_120d 55.48% > 42.00% |
| 300286.SZ | 安科瑞 | ok | 20.86 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.79% < 6.00%; excess_return_120d -5.37% < 6.00%; excess_return_240d -19.75% < 8.00%; drawdown_120d -38.89% < -28.00%; volatility_120d 63.06% > 42.00% |
| 002749.SZ | 国光股份 | ok | 20.85 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.60% < 6.00%; excess_return_120d -29.18% < 6.00%; excess_return_240d -51.96% < 8.00%; drawdown_120d -31.01% < -28.00% |
| 002201.SZ | 九鼎新材 | ok | 20.85 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.68% < 6.00%; excess_return_120d -22.26% < 6.00%; excess_return_240d -17.62% < 8.00%; drawdown_120d -44.28% < -28.00%; volatility_120d 73.27% > 42.00% |
| 002465.SZ | 海格通信 | ok | 20.84 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.04% < 6.00%; excess_return_120d -22.62% < 6.00%; excess_return_240d -22.26% < 8.00%; drawdown_120d -51.58% < -28.00%; volatility_120d 65.26% > 42.00% |
| 688119.SH | 中钢洛耐 | ok | 20.83 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.04% < 6.00%; excess_return_120d -24.62% < 6.00%; excess_return_240d -14.16% < 8.00%; drawdown_120d -52.09% < -28.00%; volatility_120d 64.19% > 42.00% |
| 001202.SZ | 炬申股份 | ok | 20.83 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.90% < 6.00%; excess_return_120d -14.48% < 6.00%; excess_return_240d -12.43% < 8.00%; drawdown_120d -41.39% < -28.00%; volatility_120d 44.15% > 42.00% |
| 600195.SH | 中牧股份 | ok | 20.83 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.57% < 6.00%; excess_return_120d -24.15% < 6.00%; excess_return_240d -35.56% < 8.00%; drawdown_120d -29.90% < -28.00% |
| 600496.SH | 精工钢构 | ok | 20.83 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.03% < 6.00%; excess_return_120d -20.61% < 6.00%; excess_return_240d -13.61% < 8.00% |
| 002455.SZ | 百川股份 | ok | 20.82 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 3.35% < 6.00%; excess_return_120d -1.23% < 6.00%; excess_return_240d -13.71% < 8.00%; drawdown_120d -56.79% < -28.00%; volatility_120d 66.52% > 42.00% |
| 002880.SZ | 卫光生物 | ok | 20.82 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.34% < 6.00%; excess_return_120d -15.92% < 6.00%; excess_return_240d -42.86% < 8.00%; drawdown_120d -33.22% < -28.00% |
| 688510.SH | 航亚科技 | ok | 20.82 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.49% < 6.00%; excess_return_120d -9.07% < 6.00%; excess_return_240d -11.14% < 8.00%; drawdown_120d -49.27% < -28.00%; volatility_120d 69.25% > 42.00% |
| 603100.SH | 川仪股份 | ok | 20.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.79% < 6.00%; excess_return_120d -24.37% < 6.00%; excess_return_240d -29.71% < 8.00%; drawdown_120d -31.64% < -28.00% |
| 601279.SH | 英利汽车 | ok | 20.80 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.19% < 6.00%; excess_return_120d -44.77% < 6.00%; excess_return_240d -41.96% < 8.00%; drawdown_120d -41.43% < -28.00% |
| 600101.SH | 明星电力 | ok | 20.79 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.29% < 6.00%; excess_return_120d -15.87% < 6.00%; excess_return_240d -48.15% < 8.00%; drawdown_120d -29.81% < -28.00% |
| 300210.SZ | 森远股份 | ok | 20.79 | close_below_ma200; stock_return_120d -5.62% < 6.00%; excess_return_120d -10.20% < 6.00%; excess_return_240d -42.90% < 8.00%; drawdown_120d -33.15% < -28.00%; volatility_120d 59.36% > 42.00% |
| 000531.SZ | 穗恒运A | ok | 20.79 | close_below_ma200; stock_return_120d -8.18% < 6.00%; excess_return_120d -12.76% < 6.00%; excess_return_240d -31.13% < 8.00%; drawdown_120d -31.37% < -28.00%; volatility_120d 45.35% > 42.00% |
| 301016.SZ | 雷尔伟 | ok | 20.79 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.11% < 6.00%; excess_return_120d -18.69% < 6.00%; excess_return_240d -7.72% < 8.00%; drawdown_120d -36.65% < -28.00%; volatility_120d 62.53% > 42.00% |
| 002224.SZ | 三力士 | ok | 20.79 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.74% < 6.00%; excess_return_120d -27.32% < 6.00%; excess_return_240d -47.38% < 8.00%; drawdown_120d -34.43% < -28.00% |
| 002271.SZ | 东方雨虹 | ok | 20.79 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.27% < 6.00%; excess_return_120d -13.85% < 6.00%; excess_return_240d -4.28% < 8.00%; drawdown_120d -35.95% < -28.00%; volatility_120d 50.18% > 42.00% |
| 301581.SZ | 黄山谷捷 | ok | 20.79 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.02% < 6.00%; excess_return_120d -16.60% < 6.00%; excess_return_240d -43.33% < 8.00%; volatility_120d 47.09% > 42.00% |
| 603025.SH | 大豪科技 | ok | 20.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.27% < 6.00%; excess_return_120d -26.85% < 6.00%; excess_return_240d -19.45% < 8.00%; drawdown_120d -29.85% < -28.00% |
| 688083.SH | 中望软件 | ok | 20.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.67% < 6.00%; excess_return_120d -20.25% < 6.00%; excess_return_240d -28.95% < 8.00%; drawdown_120d -31.36% < -28.00%; volatility_120d 61.77% > 42.00% |
| 001368.SZ | 通达创智 | ok | 20.78 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.70% < 6.00%; excess_return_120d -14.28% < 6.00%; excess_return_240d -25.47% < 8.00%; drawdown_120d -34.27% < -28.00% |
| 600822.SH | 上海物贸 | ok | 20.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.21% < 6.00%; excess_return_120d -29.79% < 6.00%; excess_return_240d -40.51% < 8.00%; drawdown_120d -34.77% < -28.00% |
| 300770.SZ | 新媒股份 | ok | 20.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.94% < 6.00%; excess_return_120d -26.52% < 6.00%; excess_return_240d -35.53% < 8.00%; drawdown_120d -35.84% < -28.00% |
| 000897.SZ | 津滨发展 | ok | 20.77 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.32% < 6.00%; excess_return_120d -30.90% < 6.00%; excess_return_240d -47.89% < 8.00%; drawdown_120d -29.11% < -28.00% |
| 301193.SZ | 家联科技 | ok | 20.77 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.45% < 6.00%; excess_return_120d -16.03% < 6.00%; excess_return_240d -25.60% < 8.00%; drawdown_120d -36.31% < -28.00%; volatility_120d 62.91% > 42.00% |
| 600628.SH | 新世界 | ok | 20.77 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.32% < 6.00%; excess_return_120d -29.90% < 6.00%; excess_return_240d -41.02% < 8.00%; drawdown_120d -37.15% < -28.00% |
| 600935.SH | 华塑股份 | ok | 20.75 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.35% < 6.00%; excess_return_120d -11.93% < 6.00%; excess_return_240d -28.44% < 8.00%; drawdown_120d -34.01% < -28.00%; volatility_120d 42.06% > 42.00% |
| 002292.SZ | 奥飞娱乐 | ok | 20.75 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.38% < 6.00%; excess_return_120d -20.96% < 6.00%; excess_return_240d -44.49% < 8.00%; drawdown_120d -31.99% < -28.00%; volatility_120d 45.32% > 42.00% |
| 300708.SZ | 聚灿光电 | ok | 20.74 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.93% < 6.00%; excess_return_120d -13.51% < 6.00%; excess_return_240d -26.79% < 8.00%; drawdown_120d -35.47% < -28.00%; volatility_120d 53.74% > 42.00% |
| 000568.SZ | 泸州老窖 | ok | 20.73 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.89% < 6.00%; excess_return_120d -36.47% < 6.00%; excess_return_240d -48.70% < 8.00%; drawdown_120d -38.84% < -28.00% |
| 000058.SZ | 深赛格 | ok | 20.73 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.98% < 6.00%; excess_return_120d -38.56% < 6.00%; excess_return_240d -47.02% < 8.00%; drawdown_120d -39.23% < -28.00% |
| 301665.SZ | 泰禾股份 | ok | 20.73 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.28% < 6.00%; excess_return_120d -21.86% < 6.00%; excess_return_240d -48.31% < 8.00%; drawdown_120d -31.17% < -28.00% |
| 300848.SZ | 美瑞新材 | ok | 20.72 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.25% < 6.00%; excess_return_120d -17.83% < 6.00%; excess_return_240d -41.05% < 8.00%; drawdown_120d -30.06% < -28.00%; volatility_120d 44.05% > 42.00% |
| 605080.SH | 浙江自然 | ok | 20.72 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.70% < 6.00%; excess_return_120d -15.28% < 6.00%; excess_return_240d -47.32% < 8.00% |
| 688606.SH | 奥泰生物 | ok | 20.72 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.13% < 6.00%; excess_return_120d -34.71% < 6.00%; excess_return_240d -53.01% < 8.00%; drawdown_120d -38.87% < -28.00% |
| 603808.SH | 歌力思 | ok | 20.72 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.46% < 6.00%; excess_return_120d -11.04% < 6.00%; excess_return_240d -23.80% < 8.00%; drawdown_120d -29.84% < -28.00%; volatility_120d 45.59% > 42.00% |
| 688283.SH | 坤恒顺维 | ok | 20.71 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.01% < 6.00%; excess_return_120d -23.59% < 6.00%; excess_return_240d 0.96% < 8.00%; drawdown_120d -45.08% < -28.00%; volatility_120d 70.98% > 42.00% |
| 600833.SH | 第一医药 | ok | 20.71 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.14% < 6.00%; excess_return_120d -28.72% < 6.00%; excess_return_240d -42.73% < 8.00%; drawdown_120d -29.87% < -28.00% |
| 688092.SH | 爱科科技 | ok | 20.71 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.49% < 6.00%; excess_return_120d -12.07% < 6.00%; excess_return_240d -18.02% < 8.00% |
| 001319.SZ | 铭科精技 | ok | 20.71 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.40% < 6.00%; excess_return_120d -22.98% < 6.00%; excess_return_240d -34.82% < 8.00%; drawdown_120d -29.43% < -28.00% |
| 600148.SH | 长春一东 | ok | 20.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.45% < 6.00%; excess_return_120d -26.03% < 6.00%; excess_return_240d -53.58% < 8.00%; drawdown_120d -29.11% < -28.00% |
| 300482.SZ | 万孚生物 | ok | 20.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.19% < 6.00%; excess_return_120d -16.77% < 6.00%; excess_return_240d -40.81% < 8.00%; drawdown_120d -34.22% < -28.00%; volatility_120d 56.51% > 42.00% |
| 300532.SZ | 今天国际 | ok | 20.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.05% < 6.00%; excess_return_120d -25.63% < 6.00%; excess_return_240d -42.96% < 8.00%; drawdown_120d -28.13% < -28.00% |
| 300697.SZ | 电工合金 | ok | 20.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.54% < 6.00%; excess_return_120d -18.12% < 6.00%; excess_return_240d -23.87% < 8.00%; drawdown_120d -36.75% < -28.00%; volatility_120d 55.16% > 42.00% |
| 300773.SZ | 拉卡拉 | ok | 20.70 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -24.22% < 6.00%; excess_return_120d -28.80% < 6.00%; excess_return_240d -51.17% < 8.00%; drawdown_120d -32.83% < -28.00%; volatility_120d 57.73% > 42.00% |
| 300729.SZ | 乐歌股份 | ok | 20.69 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.34% < 6.00%; excess_return_120d -28.92% < 6.00%; excess_return_240d -50.33% < 8.00%; drawdown_120d -30.36% < -28.00% |
| 600742.SH | 富维股份 | ok | 20.69 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.05% < 6.00%; excess_return_120d -27.63% < 6.00%; excess_return_240d -37.93% < 8.00%; drawdown_120d -34.01% < -28.00% |
| 002441.SZ | 众业达 | ok | 20.69 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.64% < 6.00%; excess_return_120d -17.22% < 6.00%; excess_return_240d -30.76% < 8.00%; drawdown_120d -29.83% < -28.00% |
| 300595.SZ | 欧普康视 | ok | 20.68 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.96% < 6.00%; excess_return_120d -28.54% < 6.00%; excess_return_240d -48.99% < 8.00%; drawdown_120d -35.37% < -28.00% |
| 600679.SH | 上海凤凰 | ok | 20.68 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.54% < 6.00%; excess_return_120d -37.12% < 6.00%; excess_return_240d -50.70% < 8.00%; drawdown_120d -34.54% < -28.00% |
| 600613.SH | 神奇制药 | ok | 20.68 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.67% < 6.00%; excess_return_120d -24.25% < 6.00%; excess_return_240d -48.62% < 8.00%; drawdown_120d -29.94% < -28.00% |
| 603606.SH | 东方电缆 | ok | 20.68 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.82% < 6.00%; excess_return_120d -19.40% < 6.00%; excess_return_240d -21.83% < 8.00%; volatility_120d 42.31% > 42.00% |
| 301287.SZ | 康力源 | ok | 20.68 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.60% < 6.00%; excess_return_120d -24.18% < 6.00%; excess_return_240d -38.45% < 8.00%; drawdown_120d -30.29% < -28.00% |
| 603801.SH | 志邦家居 | ok | 20.67 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.16% < 6.00%; excess_return_120d -39.74% < 6.00%; excess_return_240d -61.93% < 8.00%; drawdown_120d -40.59% < -28.00% |
| 600127.SH | 金健米业 | ok | 20.67 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.20% < 6.00%; excess_return_120d -23.78% < 6.00%; excess_return_240d -43.53% < 8.00%; drawdown_120d -30.38% < -28.00% |
| 600618.SH | 氯碱化工 | ok | 20.67 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.93% < 6.00%; excess_return_120d -14.51% < 6.00%; excess_return_240d -8.35% < 8.00%; drawdown_120d -41.18% < -28.00%; volatility_120d 50.03% > 42.00% |
| 002097.SZ | 山河智能 | ok | 20.67 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.77% < 6.00%; excess_return_120d -45.35% < 6.00%; excess_return_240d -28.99% < 8.00%; drawdown_120d -43.68% < -28.00% |
| 300971.SZ | 博亚精工 | ok | 20.67 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.30% < 6.00%; excess_return_120d -22.88% < 6.00%; excess_return_240d -36.46% < 8.00%; drawdown_120d -28.33% < -28.00% |
| 601968.SH | 宝钢包装 | ok | 20.66 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.22% < 6.00%; excess_return_120d -26.80% < 6.00%; excess_return_240d -38.60% < 8.00%; drawdown_120d -35.87% < -28.00% |
| 600235.SH | 民丰特纸 | ok | 20.66 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.48% < 6.00%; excess_return_120d -27.06% < 6.00%; excess_return_240d -39.61% < 8.00%; drawdown_120d -28.97% < -28.00% |
| 603060.SH | 国检集团 | ok | 20.66 | close_below_ma200; stock_return_120d -7.03% < 6.00%; excess_return_120d -11.61% < 6.00%; excess_return_240d -36.05% < 8.00%; drawdown_120d -30.76% < -28.00%; volatility_120d 46.19% > 42.00% |
| 002605.SZ | 姚记科技 | ok | 20.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.27% < 6.00%; excess_return_120d -20.85% < 6.00%; excess_return_240d -50.29% < 8.00%; drawdown_120d -37.70% < -28.00% |
| 002742.SZ | 三圣股份 | ok | 20.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.88% < 6.00%; excess_return_120d -21.98% < 6.00%; excess_return_240d -43.67% < 8.00%; drawdown_120d -29.28% < -28.00% |
| 600577.SH | 精达股份 | ok | 20.65 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -24.25% < 6.00%; excess_return_120d -28.83% < 6.00%; excess_return_240d 2.03% < 8.00%; drawdown_120d -42.69% < -28.00%; volatility_120d 49.47% > 42.00% |
| 600616.SH | 金枫酒业 | ok | 20.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.75% < 6.00%; excess_return_120d -30.33% < 6.00%; excess_return_240d -50.15% < 8.00%; drawdown_120d -33.67% < -28.00% |
| 603039.SH | 泛微网络 | ok | 20.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.25% < 6.00%; excess_return_120d -21.83% < 6.00%; excess_return_240d -37.62% < 8.00%; drawdown_120d -40.56% < -28.00%; volatility_120d 59.78% > 42.00% |
| 000402.SZ | 金融街 | ok | 20.64 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -9.82% < 6.00%; excess_return_120d -14.40% < 6.00%; excess_return_240d -35.58% < 8.00%; drawdown_120d -28.94% < -28.00%; volatility_120d 45.84% > 42.00% |
| 002940.SZ | 昂利康 | ok | 20.64 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -8.91% < 6.00%; excess_return_120d -13.49% < 6.00%; excess_return_240d -44.30% < 8.00%; drawdown_120d -33.19% < -28.00%; volatility_120d 65.44% > 42.00% |
| 003039.SZ | 顺控发展 | ok | 20.63 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -26.43% < 6.00%; excess_return_120d -31.01% < 6.00%; excess_return_240d -36.97% < 8.00%; drawdown_120d -37.56% < -28.00% |
| 002790.SZ | 瑞尔特 | ok | 20.63 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.06% < 6.00%; excess_return_120d -36.64% < 6.00%; excess_return_240d -43.73% < 8.00%; drawdown_120d -35.89% < -28.00% |
| 300824.SZ | 北鼎股份 | ok | 20.63 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.01% < 6.00%; excess_return_120d -37.59% < 6.00%; excess_return_240d -59.07% < 8.00%; drawdown_120d -38.30% < -28.00% |
| 000886.SZ | 海南高速 | ok | 20.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.07% < 6.00%; excess_return_120d -43.65% < 6.00%; excess_return_240d -59.99% < 8.00%; drawdown_120d -41.13% < -28.00% |
| 603172.SH | 万丰股份 | ok | 20.62 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.27% < 6.00%; excess_return_120d -7.85% < 6.00%; excess_return_240d -15.04% < 8.00%; drawdown_120d -44.78% < -28.00%; volatility_120d 52.32% > 42.00% |
| 000898.SZ | 鞍钢股份 | ok | 20.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.51% < 6.00%; excess_return_120d -29.09% < 6.00%; excess_return_240d -46.19% < 8.00%; drawdown_120d -31.54% < -28.00% |
| 600583.SH | 海油工程 | ok | 20.62 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.46% < 6.00%; excess_return_120d -10.04% < 6.00%; excess_return_240d -27.25% < 8.00%; drawdown_120d -40.48% < -28.00%; volatility_120d 43.75% > 42.00% |
| 603721.SH | 中广天择 | ok | 20.61 | close_below_ma200; stock_return_120d -4.91% < 6.00%; excess_return_120d -9.70% < 6.00%; excess_return_240d -29.97% < 8.00%; drawdown_120d -34.56% < -28.00%; volatility_120d 43.26% > 42.00% |
| 000860.SZ | 顺鑫农业 | ok | 20.61 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.97% < 6.00%; excess_return_120d -34.55% < 6.00%; excess_return_240d -55.50% < 8.00%; drawdown_120d -35.47% < -28.00% |
| 003016.SZ | 欣贺股份 | ok | 20.61 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.02% < 6.00%; excess_return_120d -37.60% < 6.00%; excess_return_240d -35.70% < 8.00%; drawdown_120d -33.64% < -28.00% |
| 688192.SH | 迪哲医药 | ok | 20.60 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.06% < 6.00%; excess_return_120d -18.64% < 6.00%; excess_return_240d -44.78% < 8.00%; drawdown_120d -30.54% < -28.00%; volatility_120d 59.80% > 42.00% |
| 300712.SZ | 永福股份 | ok | 20.60 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.66% < 6.00%; excess_return_120d -18.24% < 6.00%; excess_return_240d -32.98% < 8.00%; drawdown_120d -30.89% < -28.00% |
| 002054.SZ | 德美化工 | ok | 20.60 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.79% < 6.00%; excess_return_120d -9.37% < 6.00%; excess_return_240d -22.37% < 8.00%; drawdown_120d -42.10% < -28.00%; volatility_120d 51.82% > 42.00% |
| 301355.SZ | 南王科技 | ok | 20.60 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.30% < 6.00%; excess_return_120d -29.88% < 6.00%; excess_return_240d -46.51% < 8.00%; drawdown_120d -28.67% < -28.00% |
| 000061.SZ | 农产品 | ok | 20.60 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -43.99% < 6.00%; excess_return_120d -48.57% < 6.00%; excess_return_240d -32.26% < 8.00%; drawdown_120d -44.15% < -28.00% |
| 601388.SH | 怡球资源 | ok | 20.60 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -2.51% < 6.00%; excess_return_120d -7.09% < 6.00%; excess_return_240d -8.09% < 8.00%; drawdown_120d -39.06% < -28.00%; volatility_120d 53.21% > 42.00% |
| 300511.SZ | 雪榕生物 | ok | 20.60 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.97% < 6.00%; excess_return_120d -13.55% < 6.00%; excess_return_240d -34.51% < 8.00%; drawdown_120d -33.02% < -28.00% |
| 603657.SH | 春光科技 | ok | 20.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.58% < 6.00%; excess_return_120d -16.16% < 6.00%; excess_return_240d -43.37% < 8.00%; volatility_120d 57.70% > 42.00% |
| 605567.SH | 春雪食品 | ok | 20.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.02% < 6.00%; excess_return_120d -26.60% < 6.00%; excess_return_240d -39.21% < 8.00%; drawdown_120d -30.04% < -28.00% |
| 688692.SH | 达梦数据 | ok | 20.59 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -14.75% < 6.00%; excess_return_120d -19.33% < 6.00%; excess_return_240d -18.94% < 8.00%; drawdown_120d -33.57% < -28.00%; volatility_120d 54.90% > 42.00% |
| 300521.SZ | 爱司凯 | ok | 20.58 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.88% < 6.00%; excess_return_120d -17.46% < 6.00%; excess_return_240d -18.83% < 8.00%; drawdown_120d -37.12% < -28.00%; volatility_120d 55.63% > 42.00% |
| 600530.SH | 交大昂立 | ok | 20.58 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.09% < 6.00%; excess_return_120d -14.67% < 6.00%; excess_return_240d -52.00% < 8.00%; drawdown_120d -30.91% < -28.00%; volatility_120d 57.36% > 42.00% |
| 002480.SZ | 新筑股份 | ok | 20.58 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.24% < 6.00%; excess_return_120d -20.82% < 6.00%; excess_return_240d -41.55% < 8.00%; drawdown_120d -28.63% < -28.00% |
| 301608.SZ | 博实结 | ok | 20.58 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.57% < 6.00%; excess_return_120d -22.15% < 6.00%; excess_return_240d -28.89% < 8.00%; drawdown_120d -30.30% < -28.00% |
| 600970.SH | 中材国际 | ok | 20.58 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.63% < 6.00%; excess_return_120d -30.21% < 6.00%; excess_return_240d -32.52% < 8.00%; drawdown_120d -33.78% < -28.00% |
| 002108.SZ | 沧州明珠 | ok | 20.57 | close_below_ma200; stock_return_120d -12.71% < 6.00%; excess_return_120d -17.29% < 6.00%; excess_return_240d -8.53% < 8.00%; drawdown_120d -35.52% < -28.00%; volatility_120d 44.04% > 42.00% |
| 688050.SH | 爱博医疗 | ok | 20.57 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.95% < 6.00%; excess_return_120d -39.53% < 6.00%; excess_return_240d -63.40% < 8.00%; drawdown_120d -40.64% < -28.00% |
| 301024.SZ | 霍普股份 | ok | 20.57 | close_below_ma200; stock_return_120d -2.63% < 6.00%; excess_return_120d -7.21% < 6.00%; excess_return_240d -64.41% < 8.00%; drawdown_120d -34.06% < -28.00%; volatility_120d 53.79% > 42.00% |
| 300138.SZ | 晨光生物 | ok | 20.57 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.34% < 6.00%; excess_return_120d -21.92% < 6.00%; excess_return_240d -47.06% < 8.00%; drawdown_120d -35.42% < -28.00% |
| 600429.SH | 三元股份 | ok | 20.57 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.11% < 6.00%; excess_return_120d -23.69% < 6.00%; excess_return_240d -29.97% < 8.00%; drawdown_120d -33.91% < -28.00% |
| 605089.SH | 味知香 | ok | 20.56 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.65% < 6.00%; excess_return_120d -21.23% < 6.00%; excess_return_240d -34.61% < 8.00%; drawdown_120d -36.63% < -28.00% |
| 003023.SZ | 彩虹集团 | ok | 20.56 | close_below_ma200; stock_return_120d -7.66% < 6.00%; excess_return_120d -12.24% < 6.00%; excess_return_240d -16.85% < 8.00%; drawdown_120d -39.32% < -28.00%; volatility_120d 48.22% > 42.00% |
| 603709.SH | 中源家居 | ok | 20.55 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.66% < 6.00%; excess_return_120d -18.24% < 6.00%; excess_return_240d -16.34% < 8.00%; drawdown_120d -30.21% < -28.00% |
| 605108.SH | 同庆楼 | ok | 20.55 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.25% < 6.00%; excess_return_120d -41.83% < 6.00%; excess_return_240d -57.69% < 8.00%; drawdown_120d -41.74% < -28.00% |
| 300585.SZ | 奥联电子 | ok | 20.54 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -11.69% < 6.00%; excess_return_120d -16.27% < 6.00%; excess_return_240d -24.00% < 8.00%; drawdown_120d -33.88% < -28.00%; volatility_120d 51.51% > 42.00% |
| 600055.SH | 万东医疗 | ok | 20.54 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.19% < 6.00%; excess_return_120d -35.77% < 6.00%; excess_return_240d -59.35% < 8.00%; drawdown_120d -41.23% < -28.00% |
| 000966.SZ | 长源电力 | ok | 20.54 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.20% < 6.00%; excess_return_120d -12.78% < 6.00%; excess_return_240d -38.01% < 8.00%; drawdown_120d -34.12% < -28.00%; volatility_120d 44.70% > 42.00% |
| 000631.SZ | 顺发恒能 | ok | 20.54 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.74% < 6.00%; excess_return_120d -14.32% < 6.00%; excess_return_240d -27.66% < 8.00%; drawdown_120d -35.47% < -28.00%; volatility_120d 49.06% > 42.00% |
| 603390.SH | 通达电气 | ok | 20.54 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.99% < 6.00%; excess_return_120d -22.57% < 6.00%; excess_return_240d -42.18% < 8.00%; drawdown_120d -31.69% < -28.00% |
| 688276.SH | 百克生物 | ok | 20.54 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.52% < 6.00%; excess_return_120d -25.10% < 6.00%; excess_return_240d -50.75% < 8.00%; drawdown_120d -30.60% < -28.00% |
| 600197.SH | 伊力特 | ok | 20.54 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.60% < 6.00%; excess_return_120d -32.18% < 6.00%; excess_return_240d -52.28% < 8.00%; drawdown_120d -32.16% < -28.00% |
| 301035.SZ | 润丰股份 | ok | 20.53 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.38% < 6.00%; excess_return_120d -11.96% < 6.00%; excess_return_240d -10.70% < 8.00%; drawdown_120d -28.71% < -28.00% |
| 001258.SZ | 立新能源 | ok | 20.53 | close_below_ma200; stock_return_120d -1.13% < 6.00%; excess_return_120d -5.71% < 6.00%; excess_return_240d -27.39% < 8.00%; drawdown_120d -43.09% < -28.00%; volatility_120d 57.47% > 42.00% |
| 301156.SZ | 美农生物 | ok | 20.53 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.46% < 6.00%; excess_return_120d -17.04% < 6.00%; excess_return_240d -41.76% < 8.00%; drawdown_120d -29.46% < -28.00% |
| 688722.SH | 同益中 | ok | 20.53 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.49% < 6.00%; excess_return_120d -24.07% < 6.00%; excess_return_240d -49.95% < 8.00%; drawdown_120d -30.28% < -28.00%; volatility_120d 45.13% > 42.00% |
| 600718.SH | 东软集团 | ok | 20.53 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.01% < 6.00%; excess_return_120d -31.59% < 6.00%; excess_return_240d -43.57% < 8.00%; drawdown_120d -41.99% < -28.00% |
| 002320.SZ | 海峡股份 | ok | 20.52 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -46.17% < 6.00%; excess_return_120d -50.75% < 6.00%; excess_return_240d -22.31% < 8.00%; drawdown_120d -45.08% < -28.00% |
| 600517.SH | 国网英大 | ok | 20.52 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.38% < 6.00%; excess_return_120d -22.96% < 6.00%; excess_return_240d -26.87% < 8.00%; drawdown_120d -37.26% < -28.00% |
| 603166.SH | 福达股份 | ok | 20.51 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.94% < 6.00%; excess_return_120d -20.52% < 6.00%; excess_return_240d -32.46% < 8.00%; drawdown_120d -28.84% < -28.00%; volatility_120d 47.51% > 42.00% |
| 688049.SH | 炬芯科技 | ok | 20.51 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.83% < 6.00%; excess_return_120d -21.41% < 6.00%; excess_return_240d -33.02% < 8.00%; volatility_120d 44.44% > 42.00% |
| 000407.SZ | 胜利股份 | ok | 20.50 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.88% < 6.00%; excess_return_120d -27.46% < 6.00%; excess_return_240d -8.21% < 8.00%; drawdown_120d -37.64% < -28.00% |
| 300387.SZ | 富邦科技 | ok | 20.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.56% < 6.00%; excess_return_120d -19.14% < 6.00%; excess_return_240d -43.55% < 8.00%; drawdown_120d -34.66% < -28.00% |
| 300691.SZ | 联合光电 | ok | 20.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.42% < 6.00%; excess_return_120d -19.00% < 6.00%; excess_return_240d -41.29% < 8.00%; volatility_120d 42.15% > 42.00% |
| 603369.SH | 今世缘 | ok | 20.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.82% < 6.00%; excess_return_120d -28.40% < 6.00%; excess_return_240d -53.39% < 8.00% |
| 603188.SH | 亚邦股份 | ok | 20.50 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.11% < 6.00%; excess_return_120d -15.69% < 6.00%; excess_return_240d -26.43% < 8.00%; drawdown_120d -35.03% < -28.00%; volatility_120d 43.78% > 42.00% |
| 300673.SZ | 佩蒂股份 | ok | 20.49 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.12% < 6.00%; excess_return_120d -24.70% < 6.00%; excess_return_240d -32.39% < 8.00% |
| 002180.SZ | 奔图科技 | ok | 20.49 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.55% < 6.00%; excess_return_120d -23.13% < 6.00%; excess_return_240d -50.11% < 8.00%; volatility_120d 44.17% > 42.00% |
| 000528.SZ | 柳工 | ok | 20.49 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.42% < 6.00%; excess_return_120d -33.00% < 6.00%; excess_return_240d -35.87% < 8.00%; drawdown_120d -31.34% < -28.00% |
| 300294.SZ | 博雅生物 | ok | 20.49 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.17% < 6.00%; excess_return_120d -36.75% < 6.00%; excess_return_240d -62.14% < 8.00%; drawdown_120d -36.11% < -28.00% |
| 600929.SH | 雪天盐业 | ok | 20.48 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.58% < 6.00%; excess_return_120d -18.16% < 6.00%; excess_return_240d -25.14% < 8.00%; drawdown_120d -33.42% < -28.00% |
| 301173.SZ | 毓恬冠佳 | ok | 20.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.40% < 6.00%; excess_return_120d -33.98% < 6.00%; excess_return_240d -51.96% < 8.00%; drawdown_120d -37.11% < -28.00% |
| 002042.SZ | 华孚时尚 | ok | 20.47 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -8.94% < 6.00%; excess_return_120d -13.52% < 6.00%; excess_return_240d -35.87% < 8.00%; drawdown_120d -30.94% < -28.00%; volatility_120d 52.41% > 42.00% |
| 300784.SZ | 利安科技 | ok | 20.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.93% < 6.00%; excess_return_120d -18.51% < 6.00%; excess_return_240d -39.86% < 8.00%; drawdown_120d -32.52% < -28.00% |
| 002228.SZ | 合兴包装 | ok | 20.47 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -32.17% < 6.00%; excess_return_120d -36.75% < 6.00%; excess_return_240d -34.43% < 8.00%; drawdown_120d -41.43% < -28.00% |
| 003021.SZ | 兆威机电 | ok | 20.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.95% < 6.00%; excess_return_120d -27.53% < 6.00%; excess_return_240d -30.07% < 8.00%; drawdown_120d -30.29% < -28.00%; volatility_120d 50.54% > 42.00% |
| 605177.SH | 东亚药业 | ok | 20.47 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -1.85% < 6.00%; excess_return_120d -6.43% < 6.00%; excess_return_240d -31.23% < 8.00%; drawdown_120d -29.27% < -28.00%; volatility_120d 50.22% > 42.00% |
| 002215.SZ | 诺普信 | ok | 20.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.19% < 6.00%; excess_return_120d -18.77% < 6.00%; excess_return_240d -35.53% < 8.00% |
| 002482.SZ | 广田集团 | ok | 20.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.22% < 6.00%; excess_return_120d -31.80% < 6.00%; excess_return_240d -53.88% < 8.00%; drawdown_120d -34.22% < -28.00% |
| 002700.SZ | 万憬能源 | ok | 20.46 | close_below_ma200; stock_return_120d -8.79% < 6.00%; excess_return_120d -13.37% < 6.00%; excess_return_240d -49.77% < 8.00%; drawdown_120d -37.04% < -28.00%; volatility_120d 52.84% > 42.00% |
| 000411.SZ | 英特集团 | ok | 20.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.63% < 6.00%; excess_return_120d -29.21% < 6.00%; excess_return_240d -32.44% < 8.00%; drawdown_120d -33.08% < -28.00% |
| 601601.SH | 中国太保 | ok | 20.46 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -28.30% < 6.00%; excess_return_120d -32.88% < 6.00%; excess_return_240d -39.33% < 8.00%; drawdown_120d -37.90% < -28.00% |
| 003003.SZ | 天元股份 | ok | 20.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.99% < 6.00%; excess_return_120d -24.57% < 6.00%; excess_return_240d -45.33% < 8.00%; drawdown_120d -31.28% < -28.00% |
| 600010.SH | 包钢股份 | ok | 20.45 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.56% < 6.00%; excess_return_120d -12.14% < 6.00%; excess_return_240d -1.53% < 8.00%; drawdown_120d -35.48% < -28.00%; volatility_120d 46.56% > 42.00% |
| 300015.SZ | 爱尔眼科 | ok | 20.45 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.20% < 6.00%; excess_return_120d -26.78% < 6.00%; excess_return_240d -51.59% < 8.00%; drawdown_120d -29.74% < -28.00% |
| 603395.SH | 红四方 | ok | 20.45 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.24% < 6.00%; excess_return_120d -32.82% < 6.00%; excess_return_240d -58.93% < 8.00%; drawdown_120d -38.20% < -28.00% |
| 603885.SH | 吉祥航空 | ok | 20.45 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.23% < 6.00%; excess_return_120d -31.81% < 6.00%; excess_return_240d -37.39% < 8.00%; drawdown_120d -32.26% < -28.00% |
| 300171.SZ | 东富龙 | ok | 20.44 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.33% < 6.00%; excess_return_120d -28.91% < 6.00%; excess_return_240d -30.11% < 8.00%; drawdown_120d -41.75% < -28.00% |
| 002950.SZ | 奥美医疗 | ok | 20.44 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.69% < 6.00%; excess_return_120d -17.27% < 6.00%; excess_return_240d -12.29% < 8.00%; drawdown_120d -36.24% < -28.00%; volatility_120d 54.43% > 42.00% |
| 300743.SZ | 天地数码 | ok | 20.44 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -30.49% < 6.00%; excess_return_120d -35.07% < 6.00%; excess_return_240d -42.44% < 8.00%; drawdown_120d -35.98% < -28.00% |
| 002613.SZ | 北玻股份 | ok | 20.43 | close_below_ma200; stock_return_120d -6.72% < 6.00%; excess_return_120d -11.30% < 6.00%; excess_return_240d -31.66% < 8.00%; drawdown_120d -38.58% < -28.00%; volatility_120d 60.81% > 42.00% |
| 688298.SH | 东方生物 | ok | 20.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.54% < 6.00%; excess_return_120d -20.12% < 6.00%; excess_return_240d -49.94% < 8.00%; drawdown_120d -31.50% < -28.00% |
| 000009.SZ | 中国宝安 | ok | 20.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.13% < 6.00%; excess_return_120d -39.71% < 6.00%; excess_return_240d -49.06% < 8.00%; drawdown_120d -39.26% < -28.00% |
| 601002.SH | 晋亿实业 | ok | 20.43 | close_below_ma200; stock_return_120d -10.87% < 6.00%; excess_return_120d -15.45% < 6.00%; excess_return_240d -31.61% < 8.00%; drawdown_120d -32.99% < -28.00%; volatility_120d 43.39% > 42.00% |
| 300705.SZ | 九典制药 | ok | 20.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.16% < 6.00%; excess_return_120d -30.74% < 6.00%; excess_return_240d -52.69% < 8.00%; drawdown_120d -31.94% < -28.00% |
| 002933.SZ | 新兴装备 | ok | 20.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.96% < 6.00%; excess_return_120d -29.54% < 6.00%; excess_return_240d -42.45% < 8.00%; drawdown_120d -29.22% < -28.00% |
| 002568.SZ | 百润股份 | ok | 20.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.90% < 6.00%; excess_return_120d -26.48% < 6.00%; excess_return_240d -52.95% < 8.00%; volatility_120d 47.35% > 42.00% |
| 000877.SZ | 天山股份 | ok | 20.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.32% < 6.00%; excess_return_120d -33.90% < 6.00%; excess_return_240d -44.83% < 8.00%; drawdown_120d -35.17% < -28.00% |
| 002945.SZ | 华林证券 | ok | 20.42 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.83% < 6.00%; excess_return_120d -15.41% < 6.00%; excess_return_240d -26.03% < 8.00%; drawdown_120d -35.58% < -28.00%; volatility_120d 46.77% > 42.00% |
| 002026.SZ | 山东威达 | ok | 20.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.65% < 6.00%; excess_return_120d -29.23% < 6.00%; excess_return_240d -23.42% < 8.00%; drawdown_120d -34.41% < -28.00% |
| 603136.SH | 天目湖 | ok | 20.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.83% < 6.00%; excess_return_120d -28.41% < 6.00%; excess_return_240d -53.30% < 8.00%; drawdown_120d -29.16% < -28.00% |
| 002961.SZ | 瑞达期货 | ok | 20.42 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.11% < 6.00%; excess_return_120d -29.69% < 6.00%; excess_return_240d -20.60% < 8.00%; drawdown_120d -28.39% < -28.00%; volatility_120d 44.01% > 42.00% |
| 300258.SZ | 精锻科技 | ok | 20.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.38% < 6.00%; excess_return_120d -23.96% < 6.00%; excess_return_240d -30.77% < 8.00%; drawdown_120d -33.30% < -28.00%; volatility_120d 61.99% > 42.00% |
| 688366.SH | 昊海生科 | ok | 20.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.90% < 6.00%; excess_return_120d -31.48% < 6.00%; excess_return_240d -57.57% < 8.00%; drawdown_120d -35.67% < -28.00% |
| 001373.SZ | 翔腾新材 | ok | 20.41 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.06% < 6.00%; excess_return_120d -11.64% < 6.00%; excess_return_240d -22.99% < 8.00%; drawdown_120d -35.48% < -28.00%; volatility_120d 45.90% > 42.00% |
| 600361.SH | 创新新材 | ok | 20.41 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.81% < 6.00%; excess_return_120d -17.39% < 6.00%; excess_return_240d -31.09% < 8.00%; drawdown_120d -28.63% < -28.00% |
| 002255.SZ | 海陆重工 | ok | 20.40 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -24.70% < 6.00%; excess_return_120d -29.28% < 6.00%; excess_return_240d -11.45% < 8.00%; drawdown_120d -37.80% < -28.00%; volatility_120d 43.68% > 42.00% |
| 003020.SZ | 立方制药 | ok | 20.40 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.16% < 6.00%; excess_return_120d -27.74% < 6.00%; excess_return_240d -31.79% < 8.00%; drawdown_120d -31.99% < -28.00% |
| 002041.SZ | 登海种业 | ok | 20.40 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.15% < 6.00%; excess_return_120d -18.73% < 6.00%; excess_return_240d -38.87% < 8.00%; drawdown_120d -35.00% < -28.00% |
| 688038.SH | 中科通达 | ok | 20.40 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.51% < 6.00%; excess_return_120d -11.09% < 6.00%; excess_return_240d -15.61% < 8.00%; drawdown_120d -34.50% < -28.00%; volatility_120d 54.78% > 42.00% |
| 002626.SZ | 金达威 | ok | 20.40 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.26% < 6.00%; excess_return_120d -30.84% < 6.00%; excess_return_240d -49.40% < 8.00%; drawdown_120d -30.23% < -28.00% |
| 600372.SH | 中航机载 | ok | 20.39 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.23% < 6.00%; excess_return_120d -21.81% < 6.00%; excess_return_240d -27.69% < 8.00%; drawdown_120d -34.59% < -28.00%; volatility_120d 42.97% > 42.00% |
| 002310.SZ | 东方新能 | ok | 20.39 | close_below_ma200; stock_return_120d -0.44% < 6.00%; excess_return_120d -5.02% < 6.00%; excess_return_240d -16.91% < 8.00%; drawdown_120d -45.50% < -28.00%; volatility_120d 60.85% > 42.00% |
| 001238.SZ | 浙江正特 | ok | 20.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.60% < 6.00%; excess_return_120d -25.18% < 6.00%; excess_return_240d -19.66% < 8.00%; drawdown_120d -32.96% < -28.00% |
| 601877.SH | 正泰电器 | ok | 20.39 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.01% < 6.00%; excess_return_120d -12.59% < 6.00%; excess_return_240d -10.85% < 8.00%; drawdown_120d -39.55% < -28.00% |
| 002152.SZ | 广电运通 | ok | 20.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.06% < 6.00%; excess_return_120d -34.64% < 6.00%; excess_return_240d -51.31% < 8.00%; drawdown_120d -33.80% < -28.00% |
| 000705.SZ | 浙江震元 | ok | 20.38 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.28% < 6.00%; excess_return_120d -34.86% < 6.00%; excess_return_240d -47.55% < 8.00%; drawdown_120d -35.68% < -28.00% |
| 600835.SH | 上海机电 | ok | 20.38 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.44% < 6.00%; excess_return_120d -32.02% < 6.00%; excess_return_240d -19.83% < 8.00%; drawdown_120d -31.30% < -28.00% |
| 300407.SZ | 凯发电气 | ok | 20.36 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.80% < 6.00%; excess_return_120d -11.38% < 6.00%; excess_return_240d -23.23% < 8.00%; drawdown_120d -28.13% < -28.00% |
| 603969.SH | 银龙股份 | ok | 20.36 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.88% < 6.00%; excess_return_120d -24.46% < 6.00%; excess_return_240d -12.23% < 8.00%; drawdown_120d -29.75% < -28.00%; volatility_120d 44.76% > 42.00% |
| 603022.SH | 新通联 | ok | 20.36 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.39% < 6.00%; excess_return_120d -22.97% < 6.00%; excess_return_240d -41.60% < 8.00%; drawdown_120d -29.60% < -28.00% |
| 002900.SZ | 哈三联 | ok | 20.36 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.58% < 6.00%; excess_return_120d -24.16% < 6.00%; excess_return_240d -59.96% < 8.00%; drawdown_120d -28.43% < -28.00% |
| 600163.SH | 中闽能源 | ok | 20.35 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.64% < 6.00%; excess_return_120d -11.22% < 6.00%; excess_return_240d -28.20% < 8.00%; drawdown_120d -42.63% < -28.00%; volatility_120d 54.62% > 42.00% |
| 300633.SZ | 开立医疗 | ok | 20.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.31% < 6.00%; excess_return_120d -29.89% < 6.00%; excess_return_240d -51.65% < 8.00%; drawdown_120d -34.58% < -28.00% |
| 600809.SH | 山西汾酒 | ok | 20.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.92% < 6.00%; excess_return_120d -39.50% < 6.00%; excess_return_240d -57.57% < 8.00%; drawdown_120d -39.26% < -28.00% |
| 002099.SZ | 海翔药业 | ok | 20.35 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.14% < 6.00%; excess_return_120d -17.72% < 6.00%; excess_return_240d -31.06% < 8.00%; drawdown_120d -40.37% < -28.00%; volatility_120d 53.83% > 42.00% |
| 300242.SZ | 佳云科技 | ok | 20.35 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.40% < 6.00%; excess_return_120d -18.98% < 6.00%; excess_return_240d -30.42% < 8.00%; drawdown_120d -37.52% < -28.00%; volatility_120d 60.29% > 42.00% |
| 000812.SZ | 陕西金叶 | ok | 20.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.26% < 6.00%; excess_return_120d -37.84% < 6.00%; excess_return_240d -52.96% < 8.00%; drawdown_120d -34.36% < -28.00% |
| 603348.SH | 文灿股份 | ok | 20.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.21% < 6.00%; excess_return_120d -31.79% < 6.00%; excess_return_240d -53.92% < 8.00%; drawdown_120d -36.27% < -28.00% |
| 001395.SZ | 亚联机械 | ok | 20.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.56% < 6.00%; excess_return_120d -29.14% < 6.00%; excess_return_240d -54.38% < 8.00%; drawdown_120d -29.51% < -28.00% |
| 603212.SH | 赛伍技术 | ok | 20.35 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.91% < 6.00%; excess_return_120d -22.49% < 6.00%; excess_return_240d -31.42% < 8.00%; drawdown_120d -38.43% < -28.00%; volatility_120d 60.19% > 42.00% |
| 600480.SH | 凌云股份 | ok | 20.34 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.60% < 6.00%; excess_return_120d -27.18% < 6.00%; excess_return_240d -39.12% < 8.00%; volatility_120d 43.00% > 42.00% |
| 600675.SH | 中华企业 | ok | 20.33 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.66% < 6.00%; excess_return_120d -25.24% < 6.00%; excess_return_240d -50.37% < 8.00%; drawdown_120d -29.28% < -28.00% |
| 601619.SH | 嘉泽新能 | ok | 20.33 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -1.58% < 6.00%; excess_return_120d -6.16% < 6.00%; excess_return_240d -3.85% < 8.00%; drawdown_120d -38.99% < -28.00%; volatility_120d 52.47% > 42.00% |
| 603927.SH | 中科软 | ok | 20.33 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.54% < 6.00%; excess_return_120d -37.12% < 6.00%; excess_return_240d -57.42% < 8.00%; drawdown_120d -41.18% < -28.00% |
| 600373.SH | 中文传媒 | ok | 20.33 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.82% < 6.00%; excess_return_120d -30.40% < 6.00%; excess_return_240d -53.16% < 8.00%; drawdown_120d -34.49% < -28.00% |
| 002090.SZ | 金智科技 | ok | 20.33 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.20% < 6.00%; excess_return_120d -24.78% < 6.00%; excess_return_240d -28.26% < 8.00%; drawdown_120d -30.80% < -28.00% |
| 300446.SZ | 航天智造 | ok | 20.32 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -31.97% < 6.00%; excess_return_120d -36.55% < 6.00%; excess_return_240d -19.06% < 8.00%; drawdown_120d -46.28% < -28.00%; volatility_120d 46.33% > 42.00% |
| 002735.SZ | 王子新材 | ok | 20.32 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.30% < 6.00%; excess_return_120d -26.88% < 6.00%; excess_return_240d -31.80% < 8.00%; drawdown_120d -41.62% < -28.00%; volatility_120d 56.23% > 42.00% |
| 605268.SH | 王力安防 | ok | 20.32 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.43% < 6.00%; excess_return_120d -16.01% < 6.00%; excess_return_240d -18.49% < 8.00%; drawdown_120d -49.06% < -28.00%; volatility_120d 49.80% > 42.00% |
| 300039.SZ | 上海凯宝 | ok | 20.31 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.93% < 6.00%; excess_return_120d -27.51% < 6.00%; excess_return_240d -46.42% < 8.00%; drawdown_120d -31.48% < -28.00% |
| 002881.SZ | 美格智能 | ok | 20.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.69% < 6.00%; excess_return_120d -20.27% < 6.00%; excess_return_240d -37.50% < 8.00%; drawdown_120d -30.37% < -28.00%; volatility_120d 53.79% > 42.00% |
| 603321.SH | 梅轮电梯 | ok | 20.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.41% < 6.00%; excess_return_120d -28.99% < 6.00%; excess_return_240d -44.25% < 8.00%; drawdown_120d -29.60% < -28.00% |
| 600255.SH | 鑫科材料 | ok | 20.30 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -15.06% < 6.00%; excess_return_120d -19.65% < 6.00%; excess_return_240d -26.59% < 8.00%; drawdown_120d -32.30% < -28.00%; volatility_120d 55.26% > 42.00% |
| 002022.SZ | 科华生物 | ok | 20.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.51% < 6.00%; excess_return_120d -22.09% < 6.00%; excess_return_240d -44.77% < 8.00%; drawdown_120d -35.01% < -28.00% |
| 002483.SZ | 润邦股份 | ok | 20.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.18% < 6.00%; excess_return_120d -29.76% < 6.00%; excess_return_240d -37.28% < 8.00%; drawdown_120d -35.99% < -28.00% |
| 000902.SZ | 新洋丰 | ok | 20.30 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.13% < 6.00%; excess_return_120d -23.71% < 6.00%; excess_return_240d -31.19% < 8.00%; drawdown_120d -35.22% < -28.00% |
| 002073.SZ | 软控股份 | ok | 20.29 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.83% < 6.00%; excess_return_120d -38.41% < 6.00%; excess_return_240d -60.44% < 8.00%; drawdown_120d -38.65% < -28.00% |
| 301339.SZ | 通行宝 | ok | 20.29 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.60% < 6.00%; excess_return_120d -33.18% < 6.00%; excess_return_240d -58.69% < 8.00%; drawdown_120d -34.87% < -28.00% |
| 603214.SH | 爱婴室 | ok | 20.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.64% < 6.00%; excess_return_120d -28.22% < 6.00%; excess_return_240d -52.12% < 8.00%; drawdown_120d -32.26% < -28.00% |
| 002021.SZ | 中捷资源 | ok | 20.28 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 0.00% < 6.00%; excess_return_120d -4.58% < 6.00%; excess_return_240d -18.18% < 8.00%; drawdown_120d -36.50% < -28.00%; volatility_120d 51.42% > 42.00% |
| 000839.SZ | 国安股份 | ok | 20.28 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.30% < 6.00%; excess_return_120d -9.88% < 6.00%; excess_return_240d -28.85% < 8.00%; drawdown_120d -41.31% < -28.00%; volatility_120d 58.89% > 42.00% |
| 002589.SZ | 瑞康医药 | ok | 20.28 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.34% < 6.00%; excess_return_120d -21.92% < 6.00%; excess_return_240d -32.37% < 8.00%; drawdown_120d -35.25% < -28.00%; volatility_120d 42.47% > 42.00% |
| 688439.SH | 振华风光 | ok | 20.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.33% < 6.00%; excess_return_120d -32.91% < 6.00%; excess_return_240d -37.51% < 8.00%; drawdown_120d -35.20% < -28.00% |
| 603589.SH | 口子窖 | ok | 20.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.33% < 6.00%; excess_return_120d -39.91% < 6.00%; excess_return_240d -63.19% < 8.00%; drawdown_120d -38.06% < -28.00% |
| 603668.SH | 天马科技 | ok | 20.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.25% < 6.00%; excess_return_120d -31.83% < 6.00%; excess_return_240d -29.83% < 8.00%; drawdown_120d -30.30% < -28.00%; volatility_120d 43.22% > 42.00% |
| 688681.SH | 科汇股份 | ok | 20.28 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.83% < 6.00%; excess_return_120d -19.41% < 6.00%; excess_return_240d -17.01% < 8.00%; drawdown_120d -31.94% < -28.00% |
| 600559.SH | 老白干酒 | ok | 20.27 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.27% < 6.00%; excess_return_120d -31.85% < 6.00%; excess_return_240d -51.45% < 8.00%; drawdown_120d -32.12% < -28.00% |
| 605337.SH | 李子园 | ok | 20.26 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.70% < 6.00%; excess_return_120d -29.28% < 6.00%; excess_return_240d -49.97% < 8.00%; drawdown_120d -40.35% < -28.00% |
| 603535.SH | 嘉诚国际 | ok | 20.26 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -41.46% < 6.00%; excess_return_120d -46.04% < 6.00%; excess_return_240d -65.81% < 8.00%; drawdown_120d -41.84% < -28.00% |
| 300238.SZ | 冠昊生物 | ok | 20.25 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.61% < 6.00%; excess_return_120d -15.19% < 6.00%; excess_return_240d -44.44% < 8.00%; drawdown_120d -31.22% < -28.00% |
| 605599.SH | 菜百股份 | ok | 20.25 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.35% < 6.00%; excess_return_120d -10.93% < 6.00%; excess_return_240d -30.64% < 8.00%; drawdown_120d -47.04% < -28.00%; volatility_120d 49.80% > 42.00% |
| 002593.SZ | 日上集团 | ok | 20.25 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.35% < 6.00%; excess_return_120d -33.93% < 6.00%; excess_return_240d -36.43% < 8.00%; drawdown_120d -32.46% < -28.00% |
| 300869.SZ | 康泰医学 | ok | 20.25 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.93% < 6.00%; excess_return_120d -32.51% < 6.00%; excess_return_240d -48.30% < 8.00%; drawdown_120d -35.39% < -28.00% |
| 000586.SZ | 汇源通信 | ok | 20.25 | close_below_ma200; stock_return_120d -5.03% < 6.00%; excess_return_120d -9.61% < 6.00%; excess_return_240d -6.31% < 8.00%; drawdown_120d -48.85% < -28.00%; volatility_120d 67.38% > 42.00% |
| 601366.SH | 利群股份 | ok | 20.25 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.30% < 6.00%; excess_return_120d -33.88% < 6.00%; excess_return_240d -46.58% < 8.00%; drawdown_120d -40.31% < -28.00% |
| 301602.SZ | 超研股份 | ok | 20.24 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.07% < 6.00%; excess_return_120d -36.65% < 6.00%; excess_return_240d -67.58% < 8.00%; drawdown_120d -42.66% < -28.00% |
| 300040.SZ | 九洲集团 | ok | 20.24 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -2.67% < 6.00%; excess_return_120d -7.25% < 6.00%; excess_return_240d -48.01% < 8.00%; drawdown_120d -38.33% < -28.00%; volatility_120d 56.00% > 42.00% |
| 301177.SZ | 迪阿股份 | ok | 20.24 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.05% < 6.00%; excess_return_120d -14.63% < 6.00%; excess_return_240d -34.12% < 8.00%; drawdown_120d -41.08% < -28.00%; volatility_120d 57.05% > 42.00% |
| 002646.SZ | 天佑德酒 | ok | 20.24 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.70% < 6.00%; excess_return_120d -28.28% < 6.00%; excess_return_240d -50.50% < 8.00%; drawdown_120d -32.72% < -28.00% |
| 300625.SZ | 三雄极光 | ok | 20.24 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.52% < 6.00%; excess_return_120d -25.10% < 6.00%; excess_return_240d -41.68% < 8.00%; drawdown_120d -29.02% < -28.00% |
| 300898.SZ | 熊猫乳品 | ok | 20.24 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.76% < 6.00%; excess_return_120d -32.34% < 6.00%; excess_return_240d -49.70% < 8.00%; drawdown_120d -37.48% < -28.00% |
| 002556.SZ | 辉隆股份 | ok | 20.23 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.75% < 6.00%; excess_return_120d -25.33% < 6.00%; excess_return_240d -39.24% < 8.00%; drawdown_120d -34.52% < -28.00% |
| 688363.SH | 华熙生物 | ok | 20.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.94% < 6.00%; excess_return_120d -21.52% < 6.00%; excess_return_240d -50.35% < 8.00%; drawdown_120d -31.13% < -28.00% |
| 300564.SZ | 筑博设计 | ok | 20.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.32% < 6.00%; excess_return_120d -20.90% < 6.00%; excess_return_240d -29.57% < 8.00%; drawdown_120d -29.63% < -28.00%; volatility_120d 46.96% > 42.00% |
| 300383.SZ | 光环新网 | ok | 20.22 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -0.32% < 6.00%; excess_return_120d -4.90% < 6.00%; excess_return_240d -33.85% < 8.00%; drawdown_120d -34.95% < -28.00%; volatility_120d 74.82% > 42.00% |
| 600252.SH | 中恒集团 | ok | 20.22 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.83% < 6.00%; excess_return_120d -33.41% < 6.00%; excess_return_240d -48.06% < 8.00%; drawdown_120d -31.34% < -28.00% |
| 301519.SZ | 舜禹股份 | ok | 20.22 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.64% < 6.00%; excess_return_120d -19.22% < 6.00%; excess_return_240d -38.96% < 8.00%; drawdown_120d -28.49% < -28.00% |
| 002166.SZ | 莱茵生物 | ok | 20.22 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.22% < 6.00%; excess_return_120d -25.80% < 6.00%; excess_return_240d -37.13% < 8.00%; drawdown_120d -33.35% < -28.00% |
| 000888.SZ | 峨眉山A | ok | 20.22 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.59% < 6.00%; excess_return_120d -32.17% < 6.00%; excess_return_240d -52.70% < 8.00%; drawdown_120d -34.35% < -28.00% |
| 002329.SZ | 皇氏集团 | ok | 20.21 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.15% < 6.00%; excess_return_120d -20.73% < 6.00%; excess_return_240d -32.96% < 8.00%; drawdown_120d -33.54% < -28.00%; volatility_120d 47.07% > 42.00% |
| 000926.SZ | 福星股份 | ok | 20.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.00% < 6.00%; excess_return_120d -16.58% < 6.00%; excess_return_240d -32.31% < 8.00%; volatility_120d 45.46% > 42.00% |
| 300559.SZ | 佳发教育 | ok | 20.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.96% < 6.00%; excess_return_120d -18.54% < 6.00%; excess_return_240d -25.27% < 8.00%; drawdown_120d -30.70% < -28.00%; volatility_120d 50.75% > 42.00% |
| 002942.SZ | 新农股份 | ok | 20.20 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.49% < 6.00%; excess_return_120d -23.07% < 6.00%; excess_return_240d -33.34% < 8.00%; drawdown_120d -34.36% < -28.00% |
| 001322.SZ | 箭牌家居 | ok | 20.20 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.89% < 6.00%; excess_return_120d -33.47% < 6.00%; excess_return_240d -47.14% < 8.00%; drawdown_120d -35.46% < -28.00% |
| 600336.SH | 澳柯玛 | ok | 20.20 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.63% < 6.00%; excess_return_120d -27.21% < 6.00%; excess_return_240d -32.02% < 8.00%; drawdown_120d -29.96% < -28.00%; volatility_120d 44.33% > 42.00% |
| 600207.SH | 安彩高科 | ok | 20.20 | close_below_ma200; stock_return_120d -6.99% < 6.00%; excess_return_120d -11.57% < 6.00%; excess_return_240d -24.91% < 8.00%; drawdown_120d -42.01% < -28.00%; volatility_120d 62.53% > 42.00% |
| 000590.SZ | 古汉医药 | ok | 20.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.17% < 6.00%; excess_return_120d -28.76% < 6.00%; excess_return_240d -44.52% < 8.00%; drawdown_120d -33.07% < -28.00% |
| 600493.SH | 凤竹纺织 | ok | 20.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.05% < 6.00%; excess_return_120d -24.63% < 6.00%; excess_return_240d -30.19% < 8.00%; drawdown_120d -31.40% < -28.00% |
| 301293.SZ | 三博脑科 | ok | 20.18 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.92% < 6.00%; excess_return_120d -11.50% < 6.00%; excess_return_240d -9.70% < 8.00%; drawdown_120d -46.70% < -28.00%; volatility_120d 62.69% > 42.00% |
| 300741.SZ | 华宝股份 | ok | 20.18 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.05% < 6.00%; excess_return_120d -32.63% < 6.00%; excess_return_240d -50.03% < 8.00%; drawdown_120d -32.33% < -28.00% |
| 300865.SZ | 大宏立 | ok | 20.18 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.47% < 6.00%; excess_return_120d -16.05% < 6.00%; excess_return_240d -38.74% < 8.00%; drawdown_120d -28.05% < -28.00% |
| 603882.SH | 金域医学 | ok | 20.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.50% < 6.00%; excess_return_120d -18.08% < 6.00%; excess_return_240d -33.90% < 8.00%; drawdown_120d -40.28% < -28.00%; volatility_120d 43.58% > 42.00% |
| 600339.SH | 中油工程 | ok | 20.17 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.90% < 6.00%; excess_return_120d -10.48% < 6.00%; excess_return_240d -24.75% < 8.00%; drawdown_120d -43.19% < -28.00%; volatility_120d 54.37% > 42.00% |
| 603896.SH | 寿仙谷 | ok | 20.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.06% < 6.00%; excess_return_120d -30.64% < 6.00%; excess_return_240d -53.69% < 8.00%; drawdown_120d -37.61% < -28.00% |
| 002773.SZ | 康弘药业 | ok | 20.16 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.36% < 6.00%; excess_return_120d -24.94% < 6.00%; excess_return_240d -40.10% < 8.00%; drawdown_120d -33.13% < -28.00% |
| 301040.SZ | 中环海陆 | ok | 20.16 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.41% < 6.00%; excess_return_120d -15.99% < 6.00%; excess_return_240d -28.54% < 8.00%; drawdown_120d -42.68% < -28.00%; volatility_120d 73.61% > 42.00% |
| 000813.SZ | 德展健康 | ok | 20.16 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.62% < 6.00%; excess_return_120d -20.21% < 6.00%; excess_return_240d -25.52% < 8.00%; drawdown_120d -28.32% < -28.00%; volatility_120d 44.43% > 42.00% |
| 300428.SZ | 立中集团 | ok | 20.16 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.08% < 6.00%; excess_return_120d -23.66% < 6.00%; excess_return_240d -16.66% < 8.00%; drawdown_120d -30.67% < -28.00%; volatility_120d 43.27% > 42.00% |
| 603070.SH | 万控智造 | ok | 20.16 | close_below_ma200; stock_return_120d -5.36% < 6.00%; excess_return_120d -9.94% < 6.00%; excess_return_240d -31.86% < 8.00%; drawdown_120d -34.57% < -28.00%; volatility_120d 57.41% > 42.00% |
| 603081.SH | 大丰实业 | ok | 20.16 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.50% < 6.00%; excess_return_120d -40.08% < 6.00%; excess_return_240d -36.91% < 8.00%; drawdown_120d -39.16% < -28.00% |
| 603327.SH | 福蓉科技 | ok | 20.16 | close_below_ma200; stock_return_120d -21.49% < 6.00%; excess_return_120d -26.07% < 6.00%; excess_return_240d -36.10% < 8.00%; volatility_120d 51.02% > 42.00% |
| 300683.SZ | 海特生物 | ok | 20.14 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -0.76% < 6.00%; excess_return_120d -5.34% < 6.00%; excess_return_240d -17.87% < 8.00%; drawdown_120d -45.70% < -28.00%; volatility_120d 61.87% > 42.00% |
| 300601.SZ | 康泰生物 | ok | 20.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.76% < 6.00%; excess_return_120d -23.35% < 6.00%; excess_return_240d -42.53% < 8.00%; drawdown_120d -31.46% < -28.00% |
| 300653.SZ | 正海生物 | ok | 20.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.68% < 6.00%; excess_return_120d -28.26% < 6.00%; excess_return_240d -48.04% < 8.00%; drawdown_120d -34.09% < -28.00% |
| 600733.SH | 北汽蓝谷 | ok | 20.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.97% < 6.00%; excess_return_120d -45.55% < 6.00%; excess_return_240d -57.81% < 8.00%; drawdown_120d -46.74% < -28.00% |
| 300732.SZ | 设研院 | ok | 20.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.27% < 6.00%; excess_return_120d -26.85% < 6.00%; excess_return_240d -42.53% < 8.00%; drawdown_120d -28.47% < -28.00% |
| 301167.SZ | 建研设计 | ok | 20.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.05% < 6.00%; excess_return_120d -24.63% < 6.00%; excess_return_240d -43.36% < 8.00%; drawdown_120d -31.35% < -28.00% |
| 605011.SH | 杭州热电 | ok | 20.12 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.14% < 6.00%; excess_return_120d -22.72% < 6.00%; excess_return_240d -51.26% < 8.00%; drawdown_120d -29.89% < -28.00% |
| 600135.SH | 乐凯胶片 | ok | 20.12 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -24.52% < 6.00%; excess_return_120d -29.10% < 6.00%; excess_return_240d -21.99% < 8.00%; drawdown_120d -42.21% < -28.00%; volatility_120d 60.04% > 42.00% |
| 002139.SZ | 拓邦股份 | ok | 20.12 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.58% < 6.00%; excess_return_120d -32.16% < 6.00%; excess_return_240d -47.71% < 8.00%; drawdown_120d -31.90% < -28.00% |
| 600731.SH | 湖南海利 | ok | 20.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.50% < 6.00%; excess_return_120d -24.08% < 6.00%; excess_return_240d -45.19% < 8.00%; drawdown_120d -32.38% < -28.00% |
| 600071.SH | 凤凰光学 | ok | 20.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.81% < 6.00%; excess_return_120d -28.39% < 6.00%; excess_return_240d -43.43% < 8.00%; drawdown_120d -28.38% < -28.00% |
| 603126.SH | 中材节能 | ok | 20.11 | close_below_ma200; stock_return_120d -7.75% < 6.00%; excess_return_120d -12.33% < 6.00%; excess_return_240d -22.84% < 8.00%; drawdown_120d -37.47% < -28.00% |
| 000501.SZ | 武商集团 | ok | 20.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.96% < 6.00%; excess_return_120d -33.54% < 6.00%; excess_return_240d -37.87% < 8.00%; drawdown_120d -36.95% < -28.00% |
| 300935.SZ | 盈建科 | ok | 20.11 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.07% < 6.00%; excess_return_120d -15.65% < 6.00%; excess_return_240d -11.20% < 8.00%; drawdown_120d -38.82% < -28.00%; volatility_120d 62.25% > 42.00% |
| 603076.SH | 乐惠国际 | ok | 20.11 | close_below_ma200; stock_return_120d -8.13% < 6.00%; excess_return_120d -12.71% < 6.00%; excess_return_240d -50.66% < 8.00%; drawdown_120d -35.83% < -28.00% |
| 603176.SH | 汇通集团 | ok | 20.10 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.30% < 6.00%; excess_return_120d -20.88% < 6.00%; excess_return_240d -33.38% < 8.00%; drawdown_120d -28.33% < -28.00% |
| 002365.SZ | 永安药业 | ok | 20.10 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.26% < 6.00%; excess_return_120d -30.84% < 6.00%; excess_return_240d -82.89% < 8.00%; drawdown_120d -32.33% < -28.00% |
| 301077.SZ | 星华新材 | ok | 20.09 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.95% < 6.00%; excess_return_120d -13.53% < 6.00%; excess_return_240d -2.63% < 8.00%; drawdown_120d -40.59% < -28.00%; volatility_120d 55.78% > 42.00% |
| 002705.SZ | 新宝股份 | ok | 20.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.49% < 6.00%; excess_return_120d -21.07% < 6.00%; excess_return_240d -39.30% < 8.00%; drawdown_120d -39.84% < -28.00% |
| 301613.SZ | 新铝时代 | ok | 20.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.67% < 6.00%; excess_return_120d -26.25% < 6.00%; excess_return_240d -42.89% < 8.00%; drawdown_120d -34.44% < -28.00% |
| 601858.SH | 中国科传 | ok | 20.08 | close_below_ma200; stock_return_120d -2.09% < 6.00%; excess_return_120d -6.67% < 6.00%; excess_return_240d -27.75% < 8.00%; drawdown_120d -43.23% < -28.00%; volatility_120d 55.55% > 42.00% |
| 301056.SZ | 森赫股份 | ok | 20.08 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -32.11% < 6.00%; excess_return_120d -36.69% < 6.00%; excess_return_240d -3.82% < 8.00%; drawdown_120d -39.08% < -28.00%; volatility_120d 58.09% > 42.00% |
| 300696.SZ | 爱乐达 | ok | 20.08 | close_below_ma200; stock_return_120d -21.42% < 6.00%; excess_return_120d -26.00% < 6.00%; excess_return_240d -2.47% < 8.00%; drawdown_120d -43.79% < -28.00%; volatility_120d 58.96% > 42.00% |
| 600858.SH | 银座股份 | ok | 20.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.68% < 6.00%; excess_return_120d -30.26% < 6.00%; excess_return_240d -40.36% < 8.00%; drawdown_120d -40.18% < -28.00% |
| 000948.SZ | 南天信息 | ok | 20.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.09% < 6.00%; excess_return_120d -38.67% < 6.00%; excess_return_240d -66.05% < 8.00%; drawdown_120d -39.08% < -28.00% |
| 002385.SZ | 大北农 | ok | 20.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.75% < 6.00%; excess_return_120d -30.33% < 6.00%; excess_return_240d -48.12% < 8.00%; drawdown_120d -37.61% < -28.00% |
| 601700.SH | 风范股份 | ok | 20.08 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.85% < 6.00%; excess_return_120d -25.43% < 6.00%; excess_return_240d -26.60% < 8.00%; drawdown_120d -37.60% < -28.00%; volatility_120d 47.45% > 42.00% |
| 301456.SZ | 盘古智能 | ok | 20.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.36% < 6.00%; excess_return_120d -26.94% < 6.00%; excess_return_240d -21.95% < 8.00%; drawdown_120d -28.74% < -28.00% |
| 300556.SZ | 丝路视觉 | ok | 20.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.85% < 6.00%; excess_return_120d -17.43% < 6.00%; excess_return_240d -37.60% < 8.00%; drawdown_120d -28.04% < -28.00%; volatility_120d 47.65% > 42.00% |
| 301311.SZ | 昆船智能 | ok | 20.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.94% < 6.00%; excess_return_120d -32.52% < 6.00%; excess_return_240d -59.10% < 8.00%; drawdown_120d -38.68% < -28.00% |
| 002230.SZ | 科大讯飞 | ok | 20.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.17% < 6.00%; excess_return_120d -23.75% < 6.00%; excess_return_240d -34.31% < 8.00%; drawdown_120d -39.78% < -28.00% |
| 002159.SZ | 三特索道 | ok | 20.07 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.23% < 6.00%; excess_return_120d -15.81% < 6.00%; excess_return_240d -32.62% < 8.00%; drawdown_120d -37.39% < -28.00%; volatility_120d 43.44% > 42.00% |
| 300228.SZ | 富瑞特装 | ok | 20.07 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.23% < 6.00%; excess_return_120d -27.81% < 6.00%; excess_return_240d -24.70% < 8.00%; drawdown_120d -42.13% < -28.00%; volatility_120d 52.51% > 42.00% |
| 000516.SZ | 国际医学 | ok | 20.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -6.99% < 6.00%; excess_return_120d -11.57% < 6.00%; excess_return_240d -44.51% < 8.00%; drawdown_120d -35.54% < -28.00%; volatility_120d 46.29% > 42.00% |
| 603385.SH | 惠达卫浴 | ok | 20.06 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.42% < 6.00%; excess_return_120d -29.00% < 6.00%; excess_return_240d -45.40% < 8.00%; drawdown_120d -31.70% < -28.00% |
| 002798.SZ | 帝欧水华 | ok | 20.06 | close_below_ma200; stock_return_120d -5.06% < 6.00%; excess_return_120d -9.64% < 6.00%; excess_return_240d -35.02% < 8.00%; drawdown_120d -37.97% < -28.00%; volatility_120d 52.62% > 42.00% |
| 603982.SH | 泉峰汽车 | ok | 20.06 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.47% < 6.00%; excess_return_120d -35.05% < 6.00%; excess_return_240d -65.30% < 8.00%; drawdown_120d -36.39% < -28.00% |
| 603912.SH | 佳力图 | ok | 20.06 | close_below_ma200; stock_return_120d -9.22% < 6.00%; excess_return_120d -13.80% < 6.00%; excess_return_240d -31.15% < 8.00%; drawdown_120d -36.12% < -28.00%; volatility_120d 56.15% > 42.00% |
| 601890.SH | 亚星锚链 | ok | 20.05 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.42% < 6.00%; excess_return_120d -21.00% < 6.00%; excess_return_240d -36.36% < 8.00%; drawdown_120d -40.04% < -28.00% |
| 002995.SZ | 天地在线 | ok | 20.05 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 2.18% < 6.00%; excess_return_120d -2.40% < 6.00%; excess_return_240d -32.25% < 8.00%; drawdown_120d -56.22% < -28.00%; volatility_120d 78.77% > 42.00% |
| 300474.SZ | 景嘉微 | ok | 20.05 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.17% < 6.00%; excess_return_120d -23.75% < 6.00%; excess_return_240d -39.81% < 8.00%; drawdown_120d -29.58% < -28.00%; volatility_120d 44.01% > 42.00% |
| 688575.SH | 亚辉龙 | ok | 20.05 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.76% < 6.00%; excess_return_120d -39.34% < 6.00%; excess_return_240d -58.47% < 8.00%; drawdown_120d -45.52% < -28.00% |
| 605368.SH | 蓝天燃气 | ok | 20.05 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.93% < 6.00%; excess_return_120d -20.51% < 6.00%; excess_return_240d -52.92% < 8.00%; drawdown_120d -33.44% < -28.00% |
| 002616.SZ | 长青集团 | ok | 20.05 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.52% < 6.00%; excess_return_120d -16.10% < 6.00%; excess_return_240d -43.49% < 8.00%; drawdown_120d -32.70% < -28.00% |
| 600097.SH | 开创国际 | ok | 20.05 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.73% < 6.00%; excess_return_120d -31.31% < 6.00%; excess_return_240d -42.53% < 8.00%; drawdown_120d -35.45% < -28.00% |
| 002340.SZ | 格林美 | ok | 20.04 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.58% < 6.00%; excess_return_120d -22.16% < 6.00%; excess_return_240d -12.42% < 8.00%; drawdown_120d -32.32% < -28.00%; volatility_120d 46.51% > 42.00% |
| 300771.SZ | 智莱科技 | ok | 20.04 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -29.10% < 6.00%; excess_return_120d -33.68% < 6.00%; excess_return_240d -32.91% < 8.00%; drawdown_120d -35.93% < -28.00% |
| 600426.SH | 华鲁恒升 | ok | 20.04 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.28% < 6.00%; excess_return_120d -21.86% < 6.00%; excess_return_240d 0.28% < 8.00%; drawdown_120d -41.04% < -28.00%; volatility_120d 46.55% > 42.00% |
| 600744.SH | 华银电力 | ok | 20.04 | close_below_ma200; stock_return_120d 0.51% < 6.00%; excess_return_120d -4.07% < 6.00%; excess_return_240d -40.91% < 8.00%; drawdown_120d -39.51% < -28.00%; volatility_120d 61.57% > 42.00% |
| 300393.SZ | 中来股份 | ok | 20.04 | close_below_ma200; stock_return_120d 1.49% < 6.00%; excess_return_120d -3.09% < 6.00%; excess_return_240d -10.35% < 8.00%; drawdown_120d -50.18% < -28.00%; volatility_120d 67.09% > 42.00% |
| 603501.SH | 豪威集团 | ok | 20.04 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.89% < 6.00%; excess_return_120d -27.47% < 6.00%; excess_return_240d -43.23% < 8.00%; drawdown_120d -28.27% < -28.00% |
| 002401.SZ | 中远海科 | ok | 20.04 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.42% < 6.00%; excess_return_120d -31.00% < 6.00%; excess_return_240d -50.11% < 8.00%; drawdown_120d -33.19% < -28.00% |
| 600029.SH | 南方航空 | ok | 20.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.71% < 6.00%; excess_return_120d -39.29% < 6.00%; excess_return_240d -29.98% < 8.00%; drawdown_120d -38.18% < -28.00% |
| 601956.SH | 东贝集团 | ok | 20.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.01% < 6.00%; excess_return_120d -34.59% < 6.00%; excess_return_240d -50.51% < 8.00%; drawdown_120d -35.09% < -28.00% |
| 002917.SZ | 金奥博 | ok | 20.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.51% < 6.00%; excess_return_120d -24.09% < 6.00%; excess_return_240d -43.43% < 8.00%; drawdown_120d -29.00% < -28.00% |
| 301283.SZ | 聚胶股份 | ok | 20.02 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.55% < 6.00%; excess_return_120d -24.13% < 6.00%; excess_return_240d -6.18% < 8.00%; drawdown_120d -39.96% < -28.00%; volatility_120d 45.86% > 42.00% |
| 688190.SH | 云路股份 | ok | 20.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.12% < 6.00%; excess_return_120d -15.70% < 6.00%; excess_return_240d -24.93% < 8.00%; drawdown_120d -35.68% < -28.00%; volatility_120d 57.04% > 42.00% |
| 600864.SH | 哈投股份 | ok | 20.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.25% < 6.00%; excess_return_120d -22.83% < 6.00%; excess_return_240d -31.06% < 8.00%; drawdown_120d -29.52% < -28.00% |
| 605001.SH | 威奥股份 | ok | 20.01 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.64% < 6.00%; excess_return_120d -28.22% < 6.00%; excess_return_240d -40.45% < 8.00%; drawdown_120d -30.89% < -28.00% |
| 000735.SZ | 罗牛山 | ok | 20.01 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -43.14% < 6.00%; excess_return_120d -47.72% < 6.00%; excess_return_240d -38.45% < 8.00%; drawdown_120d -42.24% < -28.00% |
| 603496.SH | 恒为科技 | ok | 20.01 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.00% < 6.00%; excess_return_120d -16.58% < 6.00%; excess_return_240d -26.37% < 8.00%; drawdown_120d -39.25% < -28.00%; volatility_120d 59.25% > 42.00% |
| 002016.SZ | 世荣兆业 | ok | 20.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.32% < 6.00%; excess_return_120d -32.90% < 6.00%; excess_return_240d -48.03% < 8.00%; drawdown_120d -37.35% < -28.00% |
| 688709.SH | 成都华微 | ok | 20.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.90% < 6.00%; excess_return_120d -25.48% < 6.00%; excess_return_240d -6.30% < 8.00%; drawdown_120d -34.80% < -28.00%; volatility_120d 54.66% > 42.00% |
| 000928.SZ | 中钢国际 | ok | 20.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.88% < 6.00%; excess_return_120d -26.46% < 6.00%; excess_return_240d -38.72% < 8.00%; drawdown_120d -31.22% < -28.00% |
| 601127.SH | 赛力斯 | ok | 20.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -50.08% < 6.00%; excess_return_120d -54.66% < 6.00%; excess_return_240d -77.81% < 8.00%; drawdown_120d -53.93% < -28.00% |
| 300341.SZ | 麦克奥迪 | ok | 20.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.95% < 6.00%; excess_return_120d -22.53% < 6.00%; excess_return_240d -37.66% < 8.00%; drawdown_120d -32.68% < -28.00% |
| 300946.SZ | 恒而达 | ok | 20.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.94% < 6.00%; excess_return_120d -28.52% < 6.00%; excess_return_240d -31.56% < 8.00%; volatility_120d 44.00% > 42.00% |
| 002312.SZ | 川发龙蟒 | ok | 20.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.02% < 6.00%; excess_return_120d -18.60% < 6.00%; excess_return_240d -38.18% < 8.00%; drawdown_120d -33.71% < -28.00%; volatility_120d 43.69% > 42.00% |
| 600939.SH | 重庆建工 | ok | 19.99 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.40% < 6.00%; excess_return_120d -26.98% < 6.00%; excess_return_240d -49.79% < 8.00% |
| 605033.SH | 美邦股份 | ok | 19.99 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.36% < 6.00%; excess_return_120d -13.94% < 6.00%; excess_return_240d -27.70% < 8.00%; drawdown_120d -47.64% < -28.00%; volatility_120d 45.13% > 42.00% |
| 002103.SZ | 广博股份 | ok | 19.99 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.22% < 6.00%; excess_return_120d -37.80% < 6.00%; excess_return_240d -64.71% < 8.00%; drawdown_120d -42.38% < -28.00% |
| 603536.SH | 惠发食品 | ok | 19.98 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.26% < 6.00%; excess_return_120d -30.84% < 6.00%; excess_return_240d -33.86% < 8.00%; drawdown_120d -30.33% < -28.00% |
| 002330.SZ | 得利斯 | ok | 19.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.76% < 6.00%; excess_return_120d -28.34% < 6.00%; excess_return_240d -42.59% < 8.00%; drawdown_120d -31.92% < -28.00% |
| 605183.SH | 确成股份 | ok | 19.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.57% < 6.00%; excess_return_120d -26.15% < 6.00%; excess_return_240d -32.55% < 8.00%; drawdown_120d -34.91% < -28.00% |
| 603058.SH | 永吉股份 | ok | 19.97 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.51% < 6.00%; excess_return_120d -11.09% < 6.00%; excess_return_240d -15.74% < 8.00%; drawdown_120d -38.61% < -28.00%; volatility_120d 53.89% > 42.00% |
| 603615.SH | 茶花股份 | ok | 19.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.96% < 6.00%; excess_return_120d -23.54% < 6.00%; excess_return_240d -44.24% < 8.00%; drawdown_120d -30.99% < -28.00%; volatility_120d 43.64% > 42.00% |
| 301272.SZ | 英华特 | ok | 19.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.93% < 6.00%; excess_return_120d -21.51% < 6.00%; excess_return_240d -28.72% < 8.00%; drawdown_120d -29.90% < -28.00% |
| 300993.SZ | 玉马科技 | ok | 19.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.42% < 6.00%; excess_return_120d -36.00% < 6.00%; excess_return_240d -56.69% < 8.00%; drawdown_120d -37.84% < -28.00% |
| 688509.SH | 正元地信 | ok | 19.97 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -26.59% < 6.00%; excess_return_120d -31.17% < 6.00%; excess_return_240d -27.59% < 8.00%; drawdown_120d -37.03% < -28.00%; volatility_120d 43.04% > 42.00% |
| 603332.SH | 苏州龙杰 | ok | 19.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.66% < 6.00%; excess_return_120d -25.24% < 6.00%; excess_return_240d -49.07% < 8.00%; drawdown_120d -29.20% < -28.00% |
| 600052.SH | 东望时代 | ok | 19.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.44% < 6.00%; excess_return_120d -26.02% < 6.00%; excess_return_240d -40.49% < 8.00%; volatility_120d 46.52% > 42.00% |
| 300305.SZ | 裕兴股份 | ok | 19.97 | close_below_ma200; stock_return_120d -8.24% < 6.00%; excess_return_120d -12.82% < 6.00%; excess_return_240d -37.87% < 8.00%; drawdown_120d -34.22% < -28.00%; volatility_120d 44.41% > 42.00% |
| 300627.SZ | 华测导航 | ok | 19.97 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.01% < 6.00%; excess_return_120d -23.59% < 6.00%; excess_return_240d -38.43% < 8.00%; drawdown_120d -41.30% < -28.00%; volatility_120d 49.11% > 42.00% |
| 301399.SZ | 英特科技 | ok | 19.97 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.76% < 6.00%; excess_return_120d -18.34% < 6.00%; excess_return_240d -31.86% < 8.00%; drawdown_120d -34.48% < -28.00%; volatility_120d 52.60% > 42.00% |
| 002775.SZ | 文科股份 | ok | 19.96 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.29% < 6.00%; excess_return_120d -21.87% < 6.00%; excess_return_240d -29.62% < 8.00%; drawdown_120d -32.95% < -28.00%; volatility_120d 43.75% > 42.00% |
| 600048.SH | 保利发展 | ok | 19.96 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.52% < 6.00%; excess_return_120d -26.10% < 6.00%; excess_return_240d -61.72% < 8.00%; drawdown_120d -34.39% < -28.00% |
| 300256.SZ | 星星科技 | ok | 19.96 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.72% < 6.00%; excess_return_120d -42.30% < 6.00%; excess_return_240d -61.48% < 8.00%; drawdown_120d -42.95% < -28.00% |
| 002651.SZ | 利君股份 | ok | 19.96 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.30% < 6.00%; excess_return_120d -38.88% < 6.00%; excess_return_240d -56.34% < 8.00%; drawdown_120d -40.37% < -28.00% |
| 603569.SH | 长久物流 | ok | 19.96 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.62% < 6.00%; excess_return_120d -29.20% < 6.00%; excess_return_240d -44.36% < 8.00%; drawdown_120d -30.25% < -28.00% |
| 603506.SH | 南都物业 | ok | 19.96 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.41% < 6.00%; excess_return_120d -26.99% < 6.00%; excess_return_240d -45.16% < 8.00%; drawdown_120d -32.95% < -28.00% |
| 600829.SH | 人民同泰 | ok | 19.96 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.94% < 6.00%; excess_return_120d -27.52% < 6.00%; excess_return_240d -9.73% < 8.00%; drawdown_120d -36.70% < -28.00% |
| 000715.SZ | 中兴商业 | ok | 19.96 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.25% < 6.00%; excess_return_120d -26.83% < 6.00%; excess_return_240d -35.51% < 8.00%; drawdown_120d -28.35% < -28.00% |
| 003028.SZ | 振邦智能 | ok | 19.96 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.24% < 6.00%; excess_return_120d -22.82% < 6.00%; excess_return_240d -41.77% < 8.00%; drawdown_120d -30.31% < -28.00% |
| 600814.SH | 杭州解百 | ok | 19.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.86% < 6.00%; excess_return_120d -25.44% < 6.00%; excess_return_240d -37.62% < 8.00%; drawdown_120d -42.67% < -28.00% |
| 600966.SH | 博汇纸业 | ok | 19.95 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.87% < 6.00%; excess_return_120d -28.45% < 6.00%; excess_return_240d -6.41% < 8.00%; drawdown_120d -42.09% < -28.00%; volatility_120d 44.40% > 42.00% |
| 000036.SZ | 华联控股 | ok | 19.95 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -35.15% < 6.00%; excess_return_120d -39.73% < 6.00%; excess_return_240d -7.57% < 8.00%; drawdown_120d -42.47% < -28.00%; volatility_120d 54.45% > 42.00% |
| 601113.SH | 华鼎股份 | ok | 19.95 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -28.42% < 6.00%; excess_return_120d -33.00% < 6.00%; excess_return_240d -38.58% < 8.00%; drawdown_120d -33.66% < -28.00% |
| 002098.SZ | 浔兴股份 | ok | 19.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.47% < 6.00%; excess_return_120d -36.05% < 6.00%; excess_return_240d -53.25% < 8.00%; drawdown_120d -44.24% < -28.00% |
| 301533.SZ | 威马农机 | ok | 19.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.61% < 6.00%; excess_return_120d -42.19% < 6.00%; excess_return_240d -60.44% < 8.00%; drawdown_120d -39.91% < -28.00% |
| 002984.SZ | 森麒麟 | ok | 19.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.62% < 6.00%; excess_return_120d -38.20% < 6.00%; excess_return_240d -45.72% < 8.00%; drawdown_120d -37.21% < -28.00% |
| 002551.SZ | 尚荣医疗 | ok | 19.94 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.82% < 6.00%; excess_return_120d -25.40% < 6.00%; excess_return_240d -48.15% < 8.00%; drawdown_120d -29.51% < -28.00% |
| 300371.SZ | 汇中股份 | ok | 19.93 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.21% < 6.00%; excess_return_120d -22.79% < 6.00%; excess_return_240d -33.48% < 8.00%; drawdown_120d -29.90% < -28.00% |
| 600764.SH | 中国海防 | ok | 19.93 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.50% < 6.00%; excess_return_120d -36.08% < 6.00%; excess_return_240d -65.93% < 8.00%; drawdown_120d -39.15% < -28.00% |
| 600117.SH | 西宁特钢 | ok | 19.93 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.00% < 6.00%; excess_return_120d -29.58% < 6.00%; excess_return_240d -30.46% < 8.00%; drawdown_120d -30.39% < -28.00% |
| 301049.SZ | 超越科技 | ok | 19.93 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.15% < 6.00%; excess_return_120d -16.73% < 6.00%; excess_return_240d -42.73% < 8.00%; drawdown_120d -32.51% < -28.00% |
| 600980.SH | 北矿科技 | ok | 19.93 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.34% < 6.00%; excess_return_120d -21.92% < 6.00%; excess_return_240d -38.05% < 8.00%; drawdown_120d -29.84% < -28.00% |
| 001269.SZ | 欧晶科技 | ok | 19.93 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.70% < 6.00%; excess_return_120d -18.28% < 6.00%; excess_return_240d -50.30% < 8.00%; drawdown_120d -33.44% < -28.00%; volatility_120d 55.18% > 42.00% |
| 600606.SH | 绿地控股 | ok | 19.93 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.89% < 6.00%; excess_return_120d -27.47% < 6.00%; excess_return_240d -46.24% < 8.00% |
| 601111.SH | 中国国航 | ok | 19.93 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.94% < 6.00%; excess_return_120d -38.52% < 6.00%; excess_return_240d -39.00% < 8.00%; drawdown_120d -34.08% < -28.00% |
| 603210.SH | 泰鸿万立 | ok | 19.93 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.09% < 6.00%; excess_return_120d -32.67% < 6.00%; excess_return_240d -53.55% < 8.00%; drawdown_120d -31.72% < -28.00% |
| 603029.SH | 天鹅股份 | ok | 19.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.03% < 6.00%; excess_return_120d -22.61% < 6.00%; excess_return_240d -38.07% < 8.00%; drawdown_120d -30.89% < -28.00% |
| 002304.SZ | 洋河股份 | ok | 19.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.88% < 6.00%; excess_return_120d -38.46% < 6.00%; excess_return_240d -59.91% < 8.00%; drawdown_120d -38.02% < -28.00% |
| 003040.SZ | 楚天龙 | ok | 19.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -49.25% < 6.00%; excess_return_120d -53.83% < 6.00%; excess_return_240d -78.03% < 8.00%; drawdown_120d -50.00% < -28.00% |
| 300412.SZ | 迦南科技 | ok | 19.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.23% < 6.00%; excess_return_120d -21.81% < 6.00%; excess_return_240d -35.58% < 8.00%; volatility_120d 42.97% > 42.00% |
| 301212.SZ | 联盛化学 | ok | 19.91 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.69% < 6.00%; excess_return_120d -24.27% < 6.00%; excess_return_240d -31.95% < 8.00%; drawdown_120d -32.56% < -28.00%; volatility_120d 45.71% > 42.00% |
| 002302.SZ | 西部建设 | ok | 19.91 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.12% < 6.00%; excess_return_120d -31.70% < 6.00%; excess_return_240d -46.51% < 8.00%; drawdown_120d -34.12% < -28.00% |
| 000030.SZ | 富奥股份 | ok | 19.90 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.83% < 6.00%; excess_return_120d -31.41% < 6.00%; excess_return_240d -48.71% < 8.00% |
| 600202.SH | 哈空调 | ok | 19.90 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.61% < 6.00%; excess_return_120d -25.19% < 6.00%; excess_return_240d -40.05% < 8.00%; drawdown_120d -29.82% < -28.00% |
| 688533.SH | 上声电子 | ok | 19.90 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.81% < 6.00%; excess_return_120d -27.39% < 6.00%; excess_return_240d -36.37% < 8.00%; drawdown_120d -35.25% < -28.00% |
| 301158.SZ | 德石股份 | ok | 19.90 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.42% < 6.00%; excess_return_120d -19.00% < 6.00%; excess_return_240d -10.49% < 8.00%; drawdown_120d -49.05% < -28.00%; volatility_120d 64.71% > 42.00% |
| 688311.SH | 盟升电子 | ok | 19.90 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -31.56% < 6.00%; excess_return_120d -36.14% < 6.00%; excess_return_240d -42.06% < 8.00%; drawdown_120d -48.50% < -28.00%; volatility_120d 60.77% > 42.00% |
| 000850.SZ | 华茂股份 | ok | 19.89 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.42% < 6.00%; excess_return_120d -32.00% < 6.00%; excess_return_240d -28.40% < 8.00%; drawdown_120d -40.39% < -28.00% |
| 001231.SZ | 农心科技 | ok | 19.89 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.22% < 6.00%; excess_return_120d -27.80% < 6.00%; excess_return_240d -26.34% < 8.00%; drawdown_120d -36.53% < -28.00% |
| 603193.SH | 润本股份 | ok | 19.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.52% < 6.00%; excess_return_120d -24.10% < 6.00%; excess_return_240d -55.73% < 8.00% |
| 603089.SH | 正裕工业 | ok | 19.88 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.91% < 6.00%; excess_return_120d -34.49% < 6.00%; excess_return_240d -59.36% < 8.00%; drawdown_120d -40.27% < -28.00% |
| 300360.SZ | 炬华科技 | ok | 19.88 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.54% < 6.00%; excess_return_120d -35.12% < 6.00%; excess_return_240d -43.97% < 8.00%; drawdown_120d -37.89% < -28.00% |
| 600326.SH | 西藏天路 | ok | 19.88 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.89% < 6.00%; excess_return_120d -44.47% < 6.00%; excess_return_240d -44.63% < 8.00%; drawdown_120d -44.98% < -28.00% |
| 300158.SZ | 振东制药 | ok | 19.88 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.08% < 6.00%; excess_return_120d -17.66% < 6.00%; excess_return_240d -12.73% < 8.00%; volatility_120d 42.54% > 42.00% |
| 600386.SH | 北巴传媒 | ok | 19.88 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.20% < 6.00%; excess_return_120d -30.78% < 6.00%; excess_return_240d -51.12% < 8.00%; drawdown_120d -31.93% < -28.00% |
| 002489.SZ | 浙江永强 | ok | 19.88 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.93% < 6.00%; excess_return_120d -29.51% < 6.00%; excess_return_240d -43.99% < 8.00%; drawdown_120d -31.81% < -28.00% |
| 688617.SH | 惠泰医疗 | ok | 19.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.73% < 6.00%; excess_return_120d -24.31% < 6.00%; excess_return_240d -53.64% < 8.00% |
| 605180.SH | 华生科技 | ok | 19.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.81% < 6.00%; excess_return_120d -20.40% < 6.00%; excess_return_240d -36.03% < 8.00%; drawdown_120d -30.42% < -28.00% |
| 002820.SZ | 桂发祥 | ok | 19.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.06% < 6.00%; excess_return_120d -30.64% < 6.00%; excess_return_240d -46.78% < 8.00%; drawdown_120d -30.55% < -28.00% |
| 600712.SH | 南宁百货 | ok | 19.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.86% < 6.00%; excess_return_120d -32.44% < 6.00%; excess_return_240d -36.99% < 8.00%; drawdown_120d -30.51% < -28.00% |
| 603888.SH | 新华网 | ok | 19.86 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.15% < 6.00%; excess_return_120d -16.73% < 6.00%; excess_return_240d -26.92% < 8.00%; drawdown_120d -45.81% < -28.00%; volatility_120d 54.41% > 42.00% |
| 002337.SZ | 赛象科技 | ok | 19.86 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.17% < 6.00%; excess_return_120d -34.75% < 6.00%; excess_return_240d -41.95% < 8.00%; drawdown_120d -35.40% < -28.00% |
| 600617.SH | 国新能源 | ok | 19.86 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.83% < 6.00%; excess_return_120d -15.41% < 6.00%; excess_return_240d -21.81% < 8.00%; drawdown_120d -39.39% < -28.00%; volatility_120d 49.84% > 42.00% |
| 605333.SH | 沪光股份 | ok | 19.86 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.26% < 6.00%; excess_return_120d -44.84% < 6.00%; excess_return_240d -56.14% < 8.00%; drawdown_120d -45.72% < -28.00% |
| 600789.SH | 鲁抗医药 | ok | 19.85 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.57% < 6.00%; excess_return_120d -27.15% < 6.00%; excess_return_240d -53.33% < 8.00%; drawdown_120d -35.00% < -28.00% |
| 300791.SZ | 仙乐健康 | ok | 19.85 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.64% < 6.00%; excess_return_120d -40.22% < 6.00%; excess_return_240d -48.88% < 8.00%; drawdown_120d -36.21% < -28.00% |
| 600843.SH | 上工申贝 | ok | 19.85 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.11% < 6.00%; excess_return_120d -33.69% < 6.00%; excess_return_240d -41.01% < 8.00%; drawdown_120d -31.35% < -28.00%; volatility_120d 42.12% > 42.00% |
| 603305.SH | 旭升集团 | ok | 19.85 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.73% < 6.00%; excess_return_120d -24.31% < 6.00%; excess_return_240d -18.72% < 8.00%; drawdown_120d -42.31% < -28.00%; volatility_120d 49.54% > 42.00% |
| 688015.SH | 交控科技 | ok | 19.84 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.04% < 6.00%; excess_return_120d -32.62% < 6.00%; excess_return_240d -43.29% < 8.00%; drawdown_120d -39.44% < -28.00% |
| 301009.SZ | 可靠股份 | ok | 19.84 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.18% < 6.00%; excess_return_120d -36.76% < 6.00%; excess_return_240d -58.41% < 8.00%; drawdown_120d -38.58% < -28.00% |
| 002835.SZ | 同为股份 | ok | 19.84 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.28% < 6.00%; excess_return_120d -30.86% < 6.00%; excess_return_240d -56.17% < 8.00%; drawdown_120d -34.10% < -28.00% |
| 000069.SZ | 华侨城A | ok | 19.83 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.85% < 6.00%; excess_return_120d -36.44% < 6.00%; excess_return_240d -47.62% < 8.00%; drawdown_120d -41.11% < -28.00% |
| 002151.SZ | 北斗星通 | ok | 19.83 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -31.79% < 6.00%; excess_return_120d -36.37% < 6.00%; excess_return_240d -9.50% < 8.00%; drawdown_120d -53.68% < -28.00%; volatility_120d 55.41% > 42.00% |
| 600760.SH | 中航沈飞 | ok | 19.83 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.76% < 6.00%; excess_return_120d -31.34% < 6.00%; excess_return_240d -52.56% < 8.00%; drawdown_120d -37.23% < -28.00% |
| 300838.SZ | 浙江力诺 | ok | 19.83 | close_below_ma200; stock_return_120d -14.30% < 6.00%; excess_return_120d -18.88% < 6.00%; excess_return_240d -32.79% < 8.00%; drawdown_120d -41.55% < -28.00%; volatility_120d 42.66% > 42.00% |
| 001360.SZ | 南矿集团 | ok | 19.83 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.08% < 6.00%; excess_return_120d -25.66% < 6.00%; excess_return_240d -0.15% < 8.00%; drawdown_120d -45.26% < -28.00%; volatility_120d 62.61% > 42.00% |
| 600798.SH | 宁波海运 | ok | 19.83 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.51% < 6.00%; excess_return_120d -15.09% < 6.00%; excess_return_240d -53.06% < 8.00%; drawdown_120d -32.11% < -28.00%; volatility_120d 42.93% > 42.00% |
| 002540.SZ | 亚太科技 | ok | 19.82 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.14% < 6.00%; excess_return_120d -34.72% < 6.00%; excess_return_240d -35.32% < 8.00%; drawdown_120d -38.88% < -28.00% |
| 000514.SZ | 渝开发 | ok | 19.82 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.00% < 6.00%; excess_return_120d -26.58% < 6.00%; excess_return_240d -53.43% < 8.00%; drawdown_120d -30.99% < -28.00% |
| 000910.SZ | 大亚圣象 | ok | 19.82 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.31% < 6.00%; excess_return_120d -29.89% < 6.00%; excess_return_240d -48.60% < 8.00%; drawdown_120d -30.65% < -28.00% |
| 002274.SZ | 华昌化工 | ok | 19.82 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.09% < 6.00%; excess_return_120d -14.67% < 6.00%; excess_return_240d -51.21% < 8.00%; drawdown_120d -35.03% < -28.00% |
| 300618.SZ | 寒锐钴业 | ok | 19.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.19% < 6.00%; excess_return_120d -20.77% < 6.00%; excess_return_240d -14.55% < 8.00%; drawdown_120d -32.14% < -28.00%; volatility_120d 52.91% > 42.00% |
| 001207.SZ | 联科科技 | ok | 19.81 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.40% < 6.00%; excess_return_120d -20.98% < 6.00%; excess_return_240d -33.09% < 8.00%; drawdown_120d -38.54% < -28.00%; volatility_120d 47.90% > 42.00% |
| 301101.SZ | 明月镜片 | ok | 19.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.10% < 6.00%; excess_return_120d -34.68% < 6.00%; excess_return_240d -59.72% < 8.00%; drawdown_120d -42.09% < -28.00% |
| 300512.SZ | 中亚股份 | ok | 19.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.37% < 6.00%; excess_return_120d -30.95% < 6.00%; excess_return_240d -38.63% < 8.00%; drawdown_120d -36.04% < -28.00% |
| 600561.SH | 江西长运 | ok | 19.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.67% < 6.00%; excess_return_120d -23.25% < 6.00%; excess_return_240d -41.49% < 8.00%; drawdown_120d -28.40% < -28.00% |
| 000959.SZ | 首钢股份 | ok | 19.81 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.41% < 6.00%; excess_return_120d -24.13% < 6.00%; excess_return_240d -16.86% < 8.00%; drawdown_120d -38.63% < -28.00% |
| 300176.SZ | 鸿特科技 | ok | 19.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.76% < 6.00%; excess_return_120d -28.34% < 6.00%; excess_return_240d -48.98% < 8.00%; drawdown_120d -39.14% < -28.00% |
| 600133.SH | 东湖高新 | ok | 19.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.87% < 6.00%; excess_return_120d -19.45% < 6.00%; excess_return_240d -35.68% < 8.00%; drawdown_120d -33.13% < -28.00%; volatility_120d 44.16% > 42.00% |
| 688269.SH | 凯立新材 | ok | 19.80 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.33% < 6.00%; excess_return_120d -21.91% < 6.00%; excess_return_240d -19.77% < 8.00%; drawdown_120d -39.35% < -28.00%; volatility_120d 42.91% > 42.00% |
| 301331.SZ | 恩威医药 | ok | 19.80 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.07% < 6.00%; excess_return_120d -14.65% < 6.00%; excess_return_240d -53.04% < 8.00%; drawdown_120d -30.36% < -28.00%; volatility_120d 45.28% > 42.00% |
| 002543.SZ | 万和电气 | ok | 19.80 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.31% < 6.00%; excess_return_120d -37.89% < 6.00%; excess_return_240d -60.70% < 8.00%; drawdown_120d -36.49% < -28.00% |
| 300967.SZ | 晓鸣股份 | ok | 19.80 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.50% < 6.00%; excess_return_120d -17.08% < 6.00%; excess_return_240d -35.49% < 8.00%; drawdown_120d -35.05% < -28.00%; volatility_120d 57.76% > 42.00% |
| 601727.SH | 上海电气 | ok | 19.80 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.74% < 6.00%; excess_return_120d -24.32% < 6.00%; excess_return_240d -27.47% < 8.00%; drawdown_120d -28.47% < -28.00% |
| 002811.SZ | 郑中设计 | ok | 19.80 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.69% < 6.00%; excess_return_120d -28.27% < 6.00%; excess_return_240d -13.74% < 8.00%; drawdown_120d -37.09% < -28.00%; volatility_120d 45.21% > 42.00% |
| 600782.SH | 新钢股份 | ok | 19.79 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.57% < 6.00%; excess_return_120d -35.15% < 6.00%; excess_return_240d -57.60% < 8.00%; drawdown_120d -38.61% < -28.00% |
| 600689.SH | 上海三毛 | ok | 19.79 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.26% < 6.00%; excess_return_120d -27.84% < 6.00%; excess_return_240d -35.39% < 8.00%; drawdown_120d -33.13% < -28.00% |
| 002006.SZ | 精工科技 | ok | 19.79 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.60% < 6.00%; excess_return_120d -37.18% < 6.00%; excess_return_240d -24.02% < 8.00%; drawdown_120d -36.78% < -28.00% |
| 301236.SZ | 软通动力 | ok | 19.79 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.66% < 6.00%; excess_return_120d -23.24% < 6.00%; excess_return_240d -48.28% < 8.00%; drawdown_120d -30.12% < -28.00%; volatility_120d 58.78% > 42.00% |
| 300030.SZ | 阳普医疗 | ok | 19.79 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.13% < 6.00%; excess_return_120d -18.71% < 6.00%; excess_return_240d -46.92% < 8.00%; drawdown_120d -29.78% < -28.00% |
| 600796.SH | 钱江生化 | ok | 19.79 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.46% < 6.00%; excess_return_120d -25.04% < 6.00%; excess_return_240d -40.49% < 8.00%; drawdown_120d -33.88% < -28.00% |
| 000619.SZ | 海螺新材 | ok | 19.79 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.73% < 6.00%; excess_return_120d -31.31% < 6.00%; excess_return_240d -47.71% < 8.00%; drawdown_120d -33.19% < -28.00% |
| 002527.SZ | 新时达 | ok | 19.79 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.04% < 6.00%; excess_return_120d -30.62% < 6.00%; excess_return_240d -28.18% < 8.00%; drawdown_120d -29.16% < -28.00%; volatility_120d 46.68% > 42.00% |
| 000825.SZ | 太钢不锈 | ok | 19.78 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -28.91% < 6.00%; excess_return_120d -33.49% < 6.00%; excess_return_240d -35.86% < 8.00%; drawdown_120d -39.66% < -28.00% |
| 301037.SZ | 保立佳 | ok | 19.78 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.51% < 6.00%; excess_return_120d -19.09% < 6.00%; excess_return_240d -28.40% < 8.00%; drawdown_120d -30.69% < -28.00% |
| 000721.SZ | 西安饮食 | ok | 19.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.09% < 6.00%; excess_return_120d -41.68% < 6.00%; excess_return_240d -55.56% < 8.00%; drawdown_120d -45.07% < -28.00% |
| 001338.SZ | 永顺泰 | ok | 19.78 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.61% < 6.00%; excess_return_120d -30.19% < 6.00%; excess_return_240d -45.76% < 8.00%; drawdown_120d -37.51% < -28.00% |
| 605339.SH | 南侨食品 | ok | 19.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.83% < 6.00%; excess_return_120d -42.41% < 6.00%; excess_return_240d -48.73% < 8.00%; drawdown_120d -40.06% < -28.00% |
| 002614.SZ | 奥佳华 | ok | 19.77 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.51% < 6.00%; excess_return_120d -40.09% < 6.00%; excess_return_240d -49.12% < 8.00%; drawdown_120d -40.99% < -28.00% |
| 600740.SH | 山西焦化 | ok | 19.77 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.43% < 6.00%; excess_return_120d -13.01% < 6.00%; excess_return_240d -30.50% < 8.00%; drawdown_120d -37.07% < -28.00%; volatility_120d 47.69% > 42.00% |
| 002454.SZ | 松芝股份 | ok | 19.77 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.86% < 6.00%; excess_return_120d -21.44% < 6.00%; excess_return_240d -26.38% < 8.00%; drawdown_120d -34.96% < -28.00% |
| 002226.SZ | 江南化工 | ok | 19.77 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.56% < 6.00%; excess_return_120d -23.14% < 6.00%; excess_return_240d -37.16% < 8.00%; drawdown_120d -28.77% < -28.00% |
| 000011.SZ | 深物业A | ok | 19.77 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.92% < 6.00%; excess_return_120d -31.50% < 6.00%; excess_return_240d -45.93% < 8.00%; drawdown_120d -29.28% < -28.00% |
| 688565.SH | 力源科技 | ok | 19.76 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.62% < 6.00%; excess_return_120d -18.20% < 6.00%; excess_return_240d -20.58% < 8.00%; drawdown_120d -37.89% < -28.00%; volatility_120d 43.54% > 42.00% |
| 000707.SZ | 双环科技 | ok | 19.76 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.61% < 6.00%; excess_return_120d -31.19% < 6.00%; excess_return_240d -52.05% < 8.00%; drawdown_120d -36.57% < -28.00% |
| 000797.SZ | 中国武夷 | ok | 19.76 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -41.98% < 6.00%; excess_return_120d -46.56% < 6.00%; excess_return_240d -38.19% < 8.00%; drawdown_120d -42.57% < -28.00% |
| 002602.SZ | 世纪华通 | ok | 19.76 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.12% < 6.00%; excess_return_120d -21.70% < 6.00%; excess_return_240d -6.53% < 8.00%; drawdown_120d -32.32% < -28.00% |
| 603238.SH | 诺邦股份 | ok | 19.76 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.93% < 6.00%; excess_return_120d -36.51% < 6.00%; excess_return_240d -53.06% < 8.00%; drawdown_120d -41.26% < -28.00% |
| 600776.SH | 东方通信 | ok | 19.76 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.00% < 6.00%; excess_return_120d -26.58% < 6.00%; excess_return_240d -2.47% < 8.00%; drawdown_120d -52.49% < -28.00%; volatility_120d 59.98% > 42.00% |
| 603331.SH | 百达精工 | ok | 19.76 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.96% < 6.00%; excess_return_120d -26.55% < 6.00%; excess_return_240d -14.07% < 8.00%; drawdown_120d -48.94% < -28.00%; volatility_120d 55.47% > 42.00% |
| 300140.SZ | 节能环境 | ok | 19.75 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.31% < 6.00%; excess_return_120d -25.89% < 6.00%; excess_return_240d -35.24% < 8.00%; drawdown_120d -37.07% < -28.00% |
| 301361.SZ | 众智科技 | ok | 19.75 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.07% < 6.00%; excess_return_120d -12.65% < 6.00%; excess_return_240d -29.14% < 8.00%; drawdown_120d -42.76% < -28.00%; volatility_120d 55.84% > 42.00% |
| 300143.SZ | 盈康生命 | ok | 19.75 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.86% < 6.00%; excess_return_120d -11.44% < 6.00%; excess_return_240d -26.34% < 8.00%; drawdown_120d -36.06% < -28.00%; volatility_120d 48.78% > 42.00% |
| 002985.SZ | 北摩高科 | ok | 19.75 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.92% < 6.00%; excess_return_120d -18.50% < 6.00%; excess_return_240d -26.71% < 8.00%; drawdown_120d -41.93% < -28.00%; volatility_120d 50.12% > 42.00% |
| 000953.SZ | 中哲精化 | ok | 19.74 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.93% < 6.00%; excess_return_120d -29.51% < 6.00%; excess_return_240d -45.71% < 8.00%; drawdown_120d -31.91% < -28.00% |
| 300515.SZ | 三德科技 | ok | 19.74 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.22% < 6.00%; excess_return_120d -33.80% < 6.00%; excess_return_240d -66.34% < 8.00%; drawdown_120d -35.99% < -28.00% |
| 300073.SZ | 当升科技 | ok | 19.74 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.68% < 6.00%; excess_return_120d -23.27% < 6.00%; excess_return_240d -10.50% < 8.00%; drawdown_120d -28.83% < -28.00% |
| 603202.SH | 天有为 | ok | 19.74 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -42.61% < 6.00%; excess_return_120d -47.19% < 6.00%; excess_return_240d -66.75% < 8.00%; drawdown_120d -48.43% < -28.00% |
| 300669.SZ | 沪宁股份 | ok | 19.73 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -2.78% < 6.00%; excess_return_120d -7.36% < 6.00%; excess_return_240d -25.34% < 8.00%; drawdown_120d -34.81% < -28.00%; volatility_120d 54.70% > 42.00% |
| 688151.SH | 华强科技 | ok | 19.73 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.14% < 6.00%; excess_return_120d -28.72% < 6.00%; excess_return_240d -56.67% < 8.00%; drawdown_120d -35.23% < -28.00% |
| 600095.SH | 湘财股份 | ok | 19.73 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.93% < 6.00%; excess_return_120d -34.51% < 6.00%; excess_return_240d -52.51% < 8.00%; drawdown_120d -37.20% < -28.00% |
| 300758.SZ | 七彩化学 | ok | 19.73 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.38% < 6.00%; excess_return_120d -10.96% < 6.00%; excess_return_240d -41.86% < 8.00%; drawdown_120d -45.13% < -28.00%; volatility_120d 72.07% > 42.00% |
| 002524.SZ | 光正眼科 | ok | 19.72 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.86% < 6.00%; excess_return_120d -17.44% < 6.00%; excess_return_240d -42.02% < 8.00%; drawdown_120d -35.43% < -28.00%; volatility_120d 45.63% > 42.00% |
| 600706.SH | 曲江文旅 | ok | 19.72 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.96% < 6.00%; excess_return_120d -38.54% < 6.00%; excess_return_240d -53.07% < 8.00%; drawdown_120d -40.02% < -28.00% |
| 300896.SZ | 爱美客 | ok | 19.72 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.01% < 6.00%; excess_return_120d -39.59% < 6.00%; excess_return_240d -67.83% < 8.00%; drawdown_120d -42.04% < -28.00% |
| 002110.SZ | 三钢闽光 | ok | 19.72 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.12% < 6.00%; excess_return_120d -36.70% < 6.00%; excess_return_240d -46.41% < 8.00%; drawdown_120d -37.79% < -28.00% |
| 600327.SH | 大东方 | ok | 19.72 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.93% < 6.00%; excess_return_120d -37.51% < 6.00%; excess_return_240d -52.78% < 8.00%; drawdown_120d -38.29% < -28.00% |
| 002044.SZ | 美年健康 | ok | 19.71 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.04% < 6.00%; excess_return_120d -14.62% < 6.00%; excess_return_240d -26.66% < 8.00%; drawdown_120d -46.51% < -28.00%; volatility_120d 56.87% > 42.00% |
| 001366.SZ | 播恩集团 | ok | 19.71 | close_below_ma200; stock_return_120d -14.58% < 6.00%; excess_return_120d -19.17% < 6.00%; excess_return_240d -30.32% < 8.00%; drawdown_120d -38.64% < -28.00%; volatility_120d 49.08% > 42.00% |
| 301163.SZ | 宏德股份 | ok | 19.71 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.42% < 6.00%; excess_return_120d -16.00% < 6.00%; excess_return_240d -30.09% < 8.00%; drawdown_120d -31.63% < -28.00%; volatility_120d 43.74% > 42.00% |
| 002369.SZ | 卓翼科技 | ok | 19.71 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.70% < 6.00%; excess_return_120d -43.28% < 6.00%; excess_return_240d -62.64% < 8.00%; drawdown_120d -43.42% < -28.00% |
| 002609.SZ | 捷顺科技 | ok | 19.71 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.29% < 6.00%; excess_return_120d -23.87% < 6.00%; excess_return_240d -56.07% < 8.00%; drawdown_120d -39.13% < -28.00% |
| 603017.SH | 中衡设计 | ok | 19.71 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.09% < 6.00%; excess_return_120d -15.67% < 6.00%; excess_return_240d -16.06% < 8.00%; drawdown_120d -45.40% < -28.00%; volatility_120d 68.38% > 42.00% |
| 301633.SZ | 港迪技术 | ok | 19.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.22% < 6.00%; excess_return_120d -37.80% < 6.00%; excess_return_240d -55.88% < 8.00%; drawdown_120d -37.25% < -28.00% |
| 000059.SZ | 华锦股份 | ok | 19.70 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.19% < 6.00%; excess_return_120d -24.77% < 6.00%; excess_return_240d -41.28% < 8.00%; drawdown_120d -38.12% < -28.00% |
| 605218.SH | 伟时电子 | ok | 19.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.94% < 6.00%; excess_return_120d -18.52% < 6.00%; excess_return_240d -49.43% < 8.00%; drawdown_120d -29.04% < -28.00%; volatility_120d 47.25% > 42.00% |
| 600375.SH | 汉马科技 | ok | 19.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.31% < 6.00%; excess_return_120d -36.89% < 6.00%; excess_return_240d -64.96% < 8.00%; drawdown_120d -39.24% < -28.00% |
| 002827.SZ | 高争民爆 | ok | 19.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.09% < 6.00%; excess_return_120d -39.67% < 6.00%; excess_return_240d -52.46% < 8.00%; drawdown_120d -37.47% < -28.00% |
| 603810.SH | 丰山集团 | ok | 19.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.07% < 6.00%; excess_return_120d -30.65% < 6.00%; excess_return_240d -51.55% < 8.00%; drawdown_120d -34.72% < -28.00% |
| 301113.SZ | 雅艺科技 | ok | 19.70 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.20% < 6.00%; excess_return_120d -20.78% < 6.00%; excess_return_240d -27.47% < 8.00%; drawdown_120d -30.16% < -28.00% |
| 603027.SH | 千禾味业 | ok | 19.69 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.26% < 6.00%; excess_return_120d -31.84% < 6.00%; excess_return_240d -36.37% < 8.00%; drawdown_120d -36.89% < -28.00% |
| 002030.SZ | 达安基因 | ok | 19.69 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.26% < 6.00%; excess_return_120d -17.84% < 6.00%; excess_return_240d -39.81% < 8.00%; drawdown_120d -36.95% < -28.00%; volatility_120d 51.65% > 42.00% |
| 600262.SH | 北方股份 | ok | 19.69 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.79% < 6.00%; excess_return_120d -23.37% < 6.00%; excess_return_240d -27.28% < 8.00%; drawdown_120d -39.98% < -28.00%; volatility_120d 48.95% > 42.00% |
| 002094.SZ | 青岛金王 | ok | 19.69 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -41.57% < 6.00%; excess_return_120d -46.15% < 6.00%; excess_return_240d -74.49% < 8.00%; drawdown_120d -50.28% < -28.00% |
| 600969.SH | 郴电国际 | ok | 19.69 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.00% < 6.00%; excess_return_120d -27.58% < 6.00%; excess_return_240d -21.40% < 8.00%; drawdown_120d -37.53% < -28.00%; volatility_120d 49.02% > 42.00% |
| 300370.SZ | 安控科技 | ok | 19.69 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.61% < 6.00%; excess_return_120d -27.19% < 6.00%; excess_return_240d -56.35% < 8.00%; drawdown_120d -36.08% < -28.00% |
| 300008.SZ | 天海防务 | ok | 19.68 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.84% < 6.00%; excess_return_120d -25.43% < 6.00%; excess_return_240d -32.09% < 8.00%; drawdown_120d -40.52% < -28.00%; volatility_120d 44.91% > 42.00% |
| 600845.SH | 宝信软件 | ok | 19.68 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.23% < 6.00%; excess_return_120d -15.81% < 6.00%; excess_return_240d -44.00% < 8.00%; drawdown_120d -29.67% < -28.00%; volatility_120d 46.82% > 42.00% |
| 300807.SZ | 天迈科技 | ok | 19.67 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.00% < 6.00%; excess_return_120d -21.73% < 6.00%; excess_return_240d -29.23% < 8.00%; drawdown_120d -41.21% < -28.00%; volatility_120d 58.79% > 42.00% |
| 600916.SH | 中国黄金 | ok | 19.67 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.15% < 6.00%; excess_return_120d -14.73% < 6.00%; excess_return_240d -31.47% < 8.00%; drawdown_120d -51.10% < -28.00%; volatility_120d 53.10% > 42.00% |
| 600100.SH | 同方股份 | ok | 19.66 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.38% < 6.00%; excess_return_120d -27.96% < 6.00%; excess_return_240d -25.66% < 8.00%; drawdown_120d -33.50% < -28.00% |
| 002442.SZ | 龙星科技 | ok | 19.66 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.91% < 6.00%; excess_return_120d -21.49% < 6.00%; excess_return_240d -42.08% < 8.00%; drawdown_120d -42.15% < -28.00%; volatility_120d 56.04% > 42.00% |
| 300284.SZ | 苏交科 | ok | 19.66 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.89% < 6.00%; excess_return_120d -38.47% < 6.00%; excess_return_240d -63.67% < 8.00%; drawdown_120d -40.31% < -28.00% |
| 603596.SH | 伯特利 | ok | 19.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.35% < 6.00%; excess_return_120d -26.93% < 6.00%; excess_return_240d -41.23% < 8.00%; drawdown_120d -33.05% < -28.00%; volatility_120d 43.22% > 42.00% |
| 002666.SZ | 德联集团 | ok | 19.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.68% < 6.00%; excess_return_120d -31.26% < 6.00%; excess_return_240d -41.26% < 8.00%; drawdown_120d -35.87% < -28.00% |
| 600359.SH | 新农开发 | ok | 19.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.72% < 6.00%; excess_return_120d -24.30% < 6.00%; excess_return_240d -44.46% < 8.00%; drawdown_120d -32.07% < -28.00% |
| 600866.SH | 星湖科技 | ok | 19.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.51% < 6.00%; excess_return_120d -36.09% < 6.00%; excess_return_240d -54.71% < 8.00%; drawdown_120d -42.37% < -28.00% |
| 301552.SZ | 科力装备 | ok | 19.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.74% < 6.00%; excess_return_120d -21.32% < 6.00%; excess_return_240d -39.36% < 8.00%; drawdown_120d -30.61% < -28.00% |
| 600120.SH | 浙江东方 | ok | 19.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.07% < 6.00%; excess_return_120d -31.65% < 6.00%; excess_return_240d -46.70% < 8.00%; drawdown_120d -41.98% < -28.00% |
| 300664.SZ | 鹏鹞环保 | ok | 19.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.29% < 6.00%; excess_return_120d -19.87% < 6.00%; excess_return_240d -39.04% < 8.00%; drawdown_120d -30.47% < -28.00% |
| 000537.SZ | 绿发电力 | ok | 19.64 | close_below_ma200; stock_return_120d -6.67% < 6.00%; excess_return_120d -11.26% < 6.00%; excess_return_240d -30.73% < 8.00%; drawdown_120d -44.65% < -28.00%; volatility_120d 53.81% > 42.00% |
| 002045.SZ | 国光电器 | ok | 19.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -45.18% < 6.00%; excess_return_120d -49.76% < 6.00%; excess_return_240d -71.59% < 8.00%; drawdown_120d -52.58% < -28.00% |
| 000546.SZ | 金圆股份 | ok | 19.64 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.41% < 6.00%; excess_return_120d -26.99% < 6.00%; excess_return_240d -22.10% < 8.00%; drawdown_120d -40.15% < -28.00%; volatility_120d 57.41% > 42.00% |
| 600495.SH | 晋西车轴 | ok | 19.63 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.73% < 6.00%; excess_return_120d -30.31% < 6.00%; excess_return_240d -49.03% < 8.00%; drawdown_120d -34.50% < -28.00% |
| 600661.SH | 昂立教育 | ok | 19.63 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.24% < 6.00%; excess_return_120d -30.82% < 6.00%; excess_return_240d -51.61% < 8.00%; drawdown_120d -33.63% < -28.00% |
| 000965.SZ | 天保基建 | ok | 19.63 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.25% < 6.00%; excess_return_120d -26.83% < 6.00%; excess_return_240d -45.66% < 8.00% |
| 600728.SH | 佳都科技 | ok | 19.63 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.90% < 6.00%; excess_return_120d -41.48% < 6.00%; excess_return_240d -44.86% < 8.00%; drawdown_120d -43.88% < -28.00% |
| 003005.SZ | 竞业达 | ok | 19.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.27% < 6.00%; excess_return_120d -37.85% < 6.00%; excess_return_240d -51.34% < 8.00%; drawdown_120d -41.63% < -28.00% |
| 002223.SZ | 鱼跃医疗 | ok | 19.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.67% < 6.00%; excess_return_120d -34.25% < 6.00%; excess_return_240d -43.10% < 8.00%; drawdown_120d -42.14% < -28.00% |
| 002783.SZ | 凯龙股份 | ok | 19.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.96% < 6.00%; excess_return_120d -26.54% < 6.00%; excess_return_240d -36.35% < 8.00%; drawdown_120d -34.49% < -28.00% |
| 301275.SZ | 汉朔科技 | ok | 19.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.31% < 6.00%; excess_return_120d -25.89% < 6.00%; excess_return_240d -48.10% < 8.00%; drawdown_120d -49.80% < -28.00%; volatility_120d 60.17% > 42.00% |
| 000039.SZ | 中集集团 | ok | 19.62 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.83% < 6.00%; excess_return_120d -23.41% < 6.00%; excess_return_240d -17.24% < 8.00%; drawdown_120d -43.01% < -28.00%; volatility_120d 54.43% > 42.00% |
| 000881.SZ | 中广核技 | ok | 19.61 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.40% < 6.00%; excess_return_120d -32.98% < 6.00%; excess_return_240d -47.96% < 8.00%; drawdown_120d -33.13% < -28.00% |
| 300859.SZ | 西域旅游 | ok | 19.61 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.01% < 6.00%; excess_return_120d -29.59% < 6.00%; excess_return_240d -47.70% < 8.00%; drawdown_120d -32.98% < -28.00% |
| 000008.SZ | 神州高铁 | ok | 19.61 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.19% < 6.00%; excess_return_120d -21.77% < 6.00%; excess_return_240d -38.29% < 8.00%; drawdown_120d -34.44% < -28.00%; volatility_120d 42.75% > 42.00% |
| 600513.SH | 联环药业 | ok | 19.60 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.89% < 6.00%; excess_return_120d -17.47% < 6.00%; excess_return_240d 0.84% < 8.00%; drawdown_120d -50.57% < -28.00%; volatility_120d 57.48% > 42.00% |
| 600108.SH | 亚盛集团 | ok | 19.60 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -3.49% < 6.00%; excess_return_120d -8.07% < 6.00%; excess_return_240d -19.59% < 8.00%; drawdown_120d -57.60% < -28.00%; volatility_120d 63.07% > 42.00% |
| 300640.SZ | 德艺文创 | ok | 19.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.75% < 6.00%; excess_return_120d -27.33% < 6.00%; excess_return_240d -29.33% < 8.00%; drawdown_120d -31.53% < -28.00%; volatility_120d 42.86% > 42.00% |
| 603628.SH | 清源股份 | ok | 19.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.81% < 6.00%; excess_return_120d -33.39% < 6.00%; excess_return_240d -47.39% < 8.00%; drawdown_120d -45.03% < -28.00% |
| 301298.SZ | 东利机械 | ok | 19.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.28% < 6.00%; excess_return_120d -25.86% < 6.00%; excess_return_240d -45.73% < 8.00%; drawdown_120d -29.78% < -28.00% |
| 688750.SH | 金天钛业 | ok | 19.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.78% < 6.00%; excess_return_120d -24.36% < 6.00%; excess_return_240d -46.31% < 8.00%; drawdown_120d -30.47% < -28.00%; volatility_120d 46.70% > 42.00% |
| 001216.SZ | 华瓷股份 | ok | 19.59 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.22% < 6.00%; excess_return_120d -20.80% < 6.00%; excess_return_240d -15.14% < 8.00%; drawdown_120d -36.90% < -28.00%; volatility_120d 51.68% > 42.00% |
| 002093.SZ | 国脉科技 | ok | 19.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -43.97% < 6.00%; excess_return_120d -48.55% < 6.00%; excess_return_240d -73.55% < 8.00%; drawdown_120d -49.80% < -28.00% |
| 300128.SZ | 锦富技术 | ok | 19.59 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.47% < 6.00%; excess_return_120d -27.05% < 6.00%; excess_return_240d -18.75% < 8.00%; drawdown_120d -35.54% < -28.00%; volatility_120d 50.95% > 42.00% |
| 002572.SZ | 索菲亚 | ok | 19.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.86% < 6.00%; excess_return_120d -42.44% < 6.00%; excess_return_240d -60.52% < 8.00%; drawdown_120d -45.03% < -28.00% |
| 300927.SZ | 江天化学 | ok | 19.58 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -2.22% < 6.00%; excess_return_120d -6.80% < 6.00%; excess_return_240d -39.56% < 8.00%; drawdown_120d -42.92% < -28.00%; volatility_120d 74.36% > 42.00% |
| 300675.SZ | 建科院 | ok | 19.58 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.41% < 6.00%; excess_return_120d -26.99% < 6.00%; excess_return_240d -42.29% < 8.00%; drawdown_120d -28.87% < -28.00% |
| 600871.SH | 石化油服 | ok | 19.58 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.17% < 6.00%; excess_return_120d -8.75% < 6.00%; excess_return_240d -15.48% < 8.00%; drawdown_120d -53.17% < -28.00%; volatility_120d 57.43% > 42.00% |
| 600448.SH | 华纺股份 | ok | 19.58 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.19% < 6.00%; excess_return_120d -20.77% < 6.00%; excess_return_240d -46.31% < 8.00%; drawdown_120d -28.65% < -28.00% |
| 002899.SZ | 英派斯 | ok | 19.57 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.55% < 6.00%; excess_return_120d -22.13% < 6.00%; excess_return_240d -30.00% < 8.00%; drawdown_120d -37.88% < -28.00%; volatility_120d 45.30% > 42.00% |
| 301559.SZ | 中集环科 | ok | 19.57 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.35% < 6.00%; excess_return_120d -22.93% < 6.00%; excess_return_240d -41.62% < 8.00%; drawdown_120d -33.39% < -28.00% |
| 002923.SZ | 润都股份 | ok | 19.56 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.12% < 6.00%; excess_return_120d -14.70% < 6.00%; excess_return_240d -35.65% < 8.00%; drawdown_120d -42.41% < -28.00%; volatility_120d 50.48% > 42.00% |
| 605378.SH | 野马电池 | ok | 19.56 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.71% < 6.00%; excess_return_120d -42.29% < 6.00%; excess_return_240d -54.70% < 8.00%; drawdown_120d -42.87% < -28.00% |
| 300804.SZ | 广康生化 | ok | 19.56 | close_below_ma200; stock_return_120d -4.36% < 6.00%; excess_return_120d -8.94% < 6.00%; excess_return_240d -54.10% < 8.00%; drawdown_120d -40.74% < -28.00%; volatility_120d 66.23% > 42.00% |
| 603180.SH | 金牌家居 | ok | 19.55 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.86% < 6.00%; excess_return_120d -31.44% < 6.00%; excess_return_240d -44.53% < 8.00%; drawdown_120d -31.10% < -28.00% |
| 300793.SZ | 佳禾智能 | ok | 19.55 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.74% < 6.00%; excess_return_120d -37.32% < 6.00%; excess_return_240d -58.12% < 8.00%; drawdown_120d -41.83% < -28.00% |
| 300355.SZ | 蒙草生态 | ok | 19.54 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.69% < 6.00%; excess_return_120d -35.27% < 6.00%; excess_return_240d -55.92% < 8.00%; drawdown_120d -38.60% < -28.00% |
| 301335.SZ | 天元宠物 | ok | 19.54 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.65% < 6.00%; excess_return_120d -33.23% < 6.00%; excess_return_240d -59.24% < 8.00%; drawdown_120d -36.45% < -28.00% |
| 300217.SZ | 东方电热 | ok | 19.54 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.38% < 6.00%; excess_return_120d -19.96% < 6.00%; excess_return_240d -37.60% < 8.00%; drawdown_120d -32.18% < -28.00% |
| 300957.SZ | 贝泰妮 | ok | 19.54 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.00% < 6.00%; excess_return_120d -22.58% < 6.00%; excess_return_240d -47.76% < 8.00%; drawdown_120d -34.99% < -28.00% |
| 002259.SZ | 升达林业 | ok | 19.54 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 0.53% < 6.00%; excess_return_120d -4.05% < 6.00%; excess_return_240d -29.31% < 8.00%; drawdown_120d -40.72% < -28.00%; volatility_120d 55.29% > 42.00% |
| 300240.SZ | 飞力达 | ok | 19.53 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.79% < 6.00%; excess_return_120d -34.37% < 6.00%; excess_return_240d -65.05% < 8.00%; drawdown_120d -37.37% < -28.00% |
| 688217.SH | 睿昂基因 | ok | 19.53 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.36% < 6.00%; excess_return_120d -17.94% < 6.00%; excess_return_240d -35.24% < 8.00%; drawdown_120d -31.38% < -28.00% |
| 300056.SZ | 中创环保 | ok | 19.52 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -1.09% < 6.00%; excess_return_120d -5.68% < 6.00%; excess_return_240d -64.91% < 8.00%; drawdown_120d -34.96% < -28.00%; volatility_120d 46.29% > 42.00% |
| 600185.SH | 珠免集团 | ok | 19.52 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.48% < 6.00%; excess_return_120d -38.06% < 6.00%; excess_return_240d -44.06% < 8.00%; drawdown_120d -45.29% < -28.00% |
| 000786.SZ | 北新建材 | ok | 19.52 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.20% < 6.00%; excess_return_120d -27.78% < 6.00%; excess_return_240d -49.90% < 8.00%; drawdown_120d -35.99% < -28.00% |
| 000410.SZ | 沈阳机床 | ok | 19.52 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.31% < 6.00%; excess_return_120d -36.89% < 6.00%; excess_return_240d -46.17% < 8.00%; drawdown_120d -43.85% < -28.00% |
| 603326.SH | 我乐家居 | ok | 19.52 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.32% < 6.00%; excess_return_120d -29.90% < 6.00%; excess_return_240d -45.72% < 8.00%; drawdown_120d -36.98% < -28.00% |
| 001212.SZ | 中旗新材 | ok | 19.52 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.32% < 6.00%; excess_return_120d -21.90% < 6.00%; excess_return_240d -20.08% < 8.00%; drawdown_120d -30.47% < -28.00%; volatility_120d 50.84% > 42.00% |
| 301359.SZ | 东南电子 | ok | 19.52 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.65% < 6.00%; excess_return_120d -17.23% < 6.00%; excess_return_240d -43.59% < 8.00%; drawdown_120d -32.26% < -28.00% |
| 300374.SZ | 中铁装配 | ok | 19.51 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.04% < 6.00%; excess_return_120d -39.62% < 6.00%; excess_return_240d -59.10% < 8.00%; drawdown_120d -42.22% < -28.00% |
| 600622.SH | 光大嘉宝 | ok | 19.51 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.67% < 6.00%; excess_return_120d -33.25% < 6.00%; excess_return_240d -53.32% < 8.00%; drawdown_120d -32.67% < -28.00% |
| 603908.SH | 牧高笛 | ok | 19.51 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.51% < 6.00%; excess_return_120d -28.09% < 6.00%; excess_return_240d -50.81% < 8.00%; drawdown_120d -31.31% < -28.00% |
| 600149.SH | 廊坊发展 | ok | 19.50 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.61% < 6.00%; excess_return_120d -11.19% < 6.00%; excess_return_240d -36.52% < 8.00%; drawdown_120d -39.16% < -28.00%; volatility_120d 51.02% > 42.00% |
| 688318.SH | 财富趋势 | ok | 19.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.19% < 6.00%; excess_return_120d -24.77% < 6.00%; excess_return_240d -22.73% < 8.00%; drawdown_120d -35.49% < -28.00%; volatility_120d 58.09% > 42.00% |
| 000882.SZ | 华联股份 | ok | 19.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.95% < 6.00%; excess_return_120d -39.53% < 6.00%; excess_return_240d -54.10% < 8.00%; drawdown_120d -37.38% < -28.00% |
| 002660.SZ | 茂硕电源 | ok | 19.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.32% < 6.00%; excess_return_120d -33.90% < 6.00%; excess_return_240d -52.93% < 8.00%; drawdown_120d -34.31% < -28.00% |
| 600802.SH | 福建水泥 | ok | 19.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.76% < 6.00%; excess_return_120d -39.34% < 6.00%; excess_return_240d -37.83% < 8.00%; drawdown_120d -36.02% < -28.00% |
| 300641.SZ | 正丹股份 | ok | 19.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -9.62% < 6.00%; excess_return_120d -14.20% < 6.00%; excess_return_240d -52.01% < 8.00%; drawdown_120d -38.83% < -28.00%; volatility_120d 55.60% > 42.00% |
| 300575.SZ | 中旗股份 | ok | 19.49 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.32% < 6.00%; excess_return_120d -15.90% < 6.00%; excess_return_240d -43.24% < 8.00%; drawdown_120d -28.39% < -28.00%; volatility_120d 42.23% > 42.00% |
| 300660.SZ | 江苏雷利 | ok | 19.49 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.10% < 6.00%; excess_return_120d -31.68% < 6.00%; excess_return_240d -27.71% < 8.00%; drawdown_120d -32.51% < -28.00%; volatility_120d 45.80% > 42.00% |
| 600650.SH | 锦江在线 | ok | 19.49 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.21% < 6.00%; excess_return_120d -38.79% < 6.00%; excess_return_240d -55.65% < 8.00%; drawdown_120d -44.60% < -28.00% |
| 300631.SZ | 久吾高科 | ok | 19.49 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.84% < 6.00%; excess_return_120d -22.42% < 6.00%; excess_return_240d -24.78% < 8.00%; drawdown_120d -32.27% < -28.00% |
| 688695.SH | 中创股份 | ok | 19.49 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.68% < 6.00%; excess_return_120d -36.26% < 6.00%; excess_return_240d -57.14% < 8.00%; drawdown_120d -39.10% < -28.00% |
| 000702.SZ | 正虹科技 | ok | 19.49 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.51% < 6.00%; excess_return_120d -25.09% < 6.00%; excess_return_240d -49.73% < 8.00% |
| 300829.SZ | 金丹科技 | ok | 19.48 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.26% < 6.00%; excess_return_120d -14.84% < 6.00%; excess_return_240d -36.20% < 8.00%; drawdown_120d -32.43% < -28.00% |
| 600979.SH | 广安爱众 | ok | 19.48 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.02% < 6.00%; excess_return_120d -14.60% < 6.00%; excess_return_240d -46.57% < 8.00%; drawdown_120d -34.06% < -28.00%; volatility_120d 56.03% > 42.00% |
| 600960.SH | 渤海汽车 | ok | 19.48 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.09% < 6.00%; excess_return_120d -29.67% < 6.00%; excess_return_240d -34.37% < 8.00%; drawdown_120d -34.59% < -28.00%; volatility_120d 43.32% > 42.00% |
| 002612.SZ | 朗姿股份 | ok | 19.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.42% < 6.00%; excess_return_120d -42.00% < 6.00%; excess_return_240d -50.06% < 8.00%; drawdown_120d -40.98% < -28.00% |
| 002570.SZ | 贝因美 | ok | 19.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.84% < 6.00%; excess_return_120d -37.42% < 6.00%; excess_return_240d -56.88% < 8.00%; drawdown_120d -37.16% < -28.00% |
| 603960.SH | 克来机电 | ok | 19.47 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.51% < 6.00%; excess_return_120d -17.09% < 6.00%; excess_return_240d -28.85% < 8.00%; drawdown_120d -40.36% < -28.00%; volatility_120d 54.29% > 42.00% |
| 603218.SH | 日月股份 | ok | 19.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.55% < 6.00%; excess_return_120d -28.13% < 6.00%; excess_return_240d -39.50% < 8.00%; drawdown_120d -40.73% < -28.00% |
| 001323.SZ | 慕思股份 | ok | 19.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.35% < 6.00%; excess_return_120d -36.93% < 6.00%; excess_return_240d -57.49% < 8.00%; drawdown_120d -41.08% < -28.00% |
| 002517.SZ | 恺英网络 | ok | 19.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.58% < 6.00%; excess_return_120d -25.16% < 6.00%; excess_return_240d -34.56% < 8.00%; drawdown_120d -38.43% < -28.00%; volatility_120d 47.61% > 42.00% |
| 600218.SH | 全柴动力 | ok | 19.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.88% < 6.00%; excess_return_120d -31.46% < 6.00%; excess_return_240d -38.35% < 8.00%; drawdown_120d -36.72% < -28.00% |
| 300783.SZ | 三只松鼠 | ok | 19.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.32% < 6.00%; excess_return_120d -32.90% < 6.00%; excess_return_240d -58.43% < 8.00%; drawdown_120d -35.92% < -28.00% |
| 301616.SZ | 浙江华业 | ok | 19.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.83% < 6.00%; excess_return_120d -33.41% < 6.00%; excess_return_240d -34.45% < 8.00%; drawdown_120d -35.10% < -28.00% |
| 600258.SH | 首旅酒店 | ok | 19.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.30% < 6.00%; excess_return_120d -31.88% < 6.00%; excess_return_240d -35.23% < 8.00%; drawdown_120d -33.31% < -28.00% |
| 300832.SZ | 新产业 | ok | 19.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.58% < 6.00%; excess_return_120d -30.16% < 6.00%; excess_return_240d -45.02% < 8.00%; drawdown_120d -33.83% < -28.00% |
| 600692.SH | 亚通股份 | ok | 19.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.54% < 6.00%; excess_return_120d -24.12% < 6.00%; excess_return_240d -45.49% < 8.00%; drawdown_120d -33.80% < -28.00% |
| 000626.SZ | 远大控股 | ok | 19.46 | close_below_ma200; stock_return_120d -18.54% < 6.00%; excess_return_120d -23.12% < 6.00%; excess_return_240d -27.20% < 8.00%; drawdown_120d -32.99% < -28.00%; volatility_120d 45.15% > 42.00% |
| 301515.SZ | 港通医疗 | ok | 19.46 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.47% < 6.00%; excess_return_120d -13.05% < 6.00%; excess_return_240d -36.82% < 8.00%; drawdown_120d -32.99% < -28.00%; volatility_120d 50.48% > 42.00% |
| 603529.SH | 爱玛科技 | ok | 19.45 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.23% < 6.00%; excess_return_120d -35.81% < 6.00%; excess_return_240d -63.45% < 8.00%; drawdown_120d -39.66% < -28.00% |
| 301518.SZ | 长华化学 | ok | 19.45 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.61% < 6.00%; excess_return_120d -30.19% < 6.00%; excess_return_240d 1.29% < 8.00%; drawdown_120d -49.85% < -28.00%; volatility_120d 54.83% > 42.00% |
| 002398.SZ | 垒知集团 | ok | 19.45 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.52% < 6.00%; excess_return_120d -35.10% < 6.00%; excess_return_240d -42.70% < 8.00%; drawdown_120d -40.60% < -28.00% |
| 002893.SZ | 京能热力 | ok | 19.45 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.49% < 6.00%; excess_return_120d -20.07% < 6.00%; excess_return_240d -36.36% < 8.00%; drawdown_120d -29.36% < -28.00% |
| 301498.SZ | 乖宝宠物 | ok | 19.44 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.37% < 6.00%; excess_return_120d -41.95% < 6.00%; excess_return_240d -83.07% < 8.00%; drawdown_120d -45.07% < -28.00% |
| 000661.SZ | 长春高新 | ok | 19.44 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.82% < 6.00%; excess_return_120d -29.40% < 6.00%; excess_return_240d -52.38% < 8.00%; drawdown_120d -34.77% < -28.00% |
| 603839.SH | 安正时尚 | ok | 19.44 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.19% < 6.00%; excess_return_120d -30.77% < 6.00%; excess_return_240d -36.29% < 8.00%; drawdown_120d -29.64% < -28.00% |
| 301131.SZ | 聚赛龙 | ok | 19.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.76% < 6.00%; excess_return_120d -34.34% < 6.00%; excess_return_240d -47.02% < 8.00%; drawdown_120d -33.92% < -28.00% |
| 002172.SZ | 澳洋健康 | ok | 19.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.69% < 6.00%; excess_return_120d -29.27% < 6.00%; excess_return_240d -47.30% < 8.00%; drawdown_120d -35.84% < -28.00% |
| 002029.SZ | 七匹狼 | ok | 19.43 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.29% < 6.00%; excess_return_120d -29.87% < 6.00%; excess_return_240d -2.71% < 8.00%; drawdown_120d -44.51% < -28.00%; volatility_120d 49.32% > 42.00% |
| 600191.SH | 华资实业 | ok | 19.43 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -29.14% < 6.00%; excess_return_120d -33.72% < 6.00%; excess_return_240d -9.40% < 8.00%; drawdown_120d -36.07% < -28.00%; volatility_120d 47.65% > 42.00% |
| 300886.SZ | 华业香料 | ok | 19.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.87% < 6.00%; excess_return_120d -23.45% < 6.00%; excess_return_240d -49.76% < 8.00%; drawdown_120d -31.77% < -28.00% |
| 002133.SZ | 广宇集团 | ok | 19.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.37% < 6.00%; excess_return_120d -29.95% < 6.00%; excess_return_240d -36.23% < 8.00%; drawdown_120d -36.59% < -28.00% |
| 000768.SZ | 中航西飞 | ok | 19.42 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.39% < 6.00%; excess_return_120d -22.97% < 6.00%; excess_return_240d -45.12% < 8.00%; drawdown_120d -35.27% < -28.00%; volatility_120d 42.75% > 42.00% |
| 000425.SZ | 徐工机械 | ok | 19.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.67% < 6.00%; excess_return_120d -30.25% < 6.00%; excess_return_240d -16.08% < 8.00%; drawdown_120d -33.39% < -28.00%; volatility_120d 46.97% > 42.00% |
| 301558.SZ | 三态股份 | ok | 19.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.19% < 6.00%; excess_return_120d -27.77% < 6.00%; excess_return_240d -52.53% < 8.00%; drawdown_120d -38.33% < -28.00% |
| 300815.SZ | 玉禾田 | ok | 19.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.81% < 6.00%; excess_return_120d -24.39% < 6.00%; excess_return_240d -29.52% < 8.00%; drawdown_120d -33.87% < -28.00% |
| 688116.SH | 天奈科技 | ok | 19.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.58% < 6.00%; excess_return_120d -24.16% < 6.00%; excess_return_240d -34.08% < 8.00%; volatility_120d 46.10% > 42.00% |
| 002086.SZ | 东方海洋 | ok | 19.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.94% < 6.00%; excess_return_120d -27.52% < 6.00%; excess_return_240d -58.86% < 8.00%; drawdown_120d -33.33% < -28.00% |
| 300112.SZ | 万讯自控 | ok | 19.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.64% < 6.00%; excess_return_120d -32.22% < 6.00%; excess_return_240d -52.03% < 8.00%; drawdown_120d -33.79% < -28.00% |
| 603809.SH | 豪能股份 | ok | 19.41 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.80% < 6.00%; excess_return_120d -38.38% < 6.00%; excess_return_240d -53.03% < 8.00%; drawdown_120d -38.84% < -28.00% |
| 605050.SH | 福然德 | ok | 19.41 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.80% < 6.00%; excess_return_120d -29.38% < 6.00%; excess_return_240d -53.63% < 8.00%; drawdown_120d -33.69% < -28.00% |
| 688707.SH | 振华新材 | ok | 19.40 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -13.29% < 6.00%; excess_return_120d -17.87% < 6.00%; excess_return_240d -31.07% < 8.00%; drawdown_120d -36.29% < -28.00%; volatility_120d 51.30% > 42.00% |
| 301185.SZ | 鸥玛软件 | ok | 19.40 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.22% < 6.00%; excess_return_120d -26.80% < 6.00%; excess_return_240d -45.01% < 8.00%; drawdown_120d -38.03% < -28.00% |
| 688078.SH | 龙软科技 | ok | 19.40 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.67% < 6.00%; excess_return_120d -24.25% < 6.00%; excess_return_240d -50.57% < 8.00%; drawdown_120d -29.85% < -28.00% |
| 603208.SH | 江山欧派 | ok | 19.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.88% < 6.00%; excess_return_120d -29.46% < 6.00%; excess_return_240d -51.35% < 8.00%; drawdown_120d -32.53% < -28.00% |
| 002627.SZ | 三峡旅游 | ok | 19.39 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.83% < 6.00%; excess_return_120d -24.41% < 6.00%; excess_return_240d -11.08% < 8.00%; drawdown_120d -42.30% < -28.00%; volatility_120d 53.77% > 42.00% |
| 002968.SZ | 新大正 | ok | 19.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.87% < 6.00%; excess_return_120d -33.45% < 6.00%; excess_return_240d -37.79% < 8.00%; drawdown_120d -40.83% < -28.00% |
| 000002.SZ | 万科A | ok | 19.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.98% < 6.00%; excess_return_120d -38.56% < 6.00%; excess_return_240d -74.30% < 8.00%; drawdown_120d -40.73% < -28.00% |
| 601888.SH | 中国中免 | ok | 19.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -43.93% < 6.00%; excess_return_120d -48.51% < 6.00%; excess_return_240d -34.31% < 8.00%; drawdown_120d -46.88% < -28.00% |
| 300289.SZ | 利德曼 | ok | 19.38 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.36% < 6.00%; excess_return_120d -21.94% < 6.00%; excess_return_240d -13.43% < 8.00%; drawdown_120d -29.67% < -28.00%; volatility_120d 47.06% > 42.00% |
| 300872.SZ | 天阳科技 | ok | 19.38 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.23% < 6.00%; excess_return_120d -26.81% < 6.00%; excess_return_240d -61.98% < 8.00%; drawdown_120d -31.14% < -28.00%; volatility_120d 55.24% > 42.00% |
| 002671.SZ | 龙泉股份 | ok | 19.38 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.34% < 6.00%; excess_return_120d -30.92% < 6.00%; excess_return_240d -38.44% < 8.00%; drawdown_120d -36.82% < -28.00% |
| 301258.SZ | 富士莱 | ok | 19.37 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.32% < 6.00%; excess_return_120d -26.90% < 6.00%; excess_return_240d -51.21% < 8.00%; drawdown_120d -34.17% < -28.00% |
| 000068.SZ | 华控赛格 | ok | 19.37 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.68% < 6.00%; excess_return_120d -20.26% < 6.00%; excess_return_240d -38.96% < 8.00%; drawdown_120d -32.46% < -28.00%; volatility_120d 43.82% > 42.00% |
| 300507.SZ | 苏奥传感 | ok | 19.37 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.59% < 6.00%; excess_return_120d -25.17% < 6.00%; excess_return_240d -25.32% < 8.00%; drawdown_120d -32.31% < -28.00%; volatility_120d 43.44% > 42.00% |
| 600570.SH | 恒生电子 | ok | 19.37 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.92% < 6.00%; excess_return_120d -34.50% < 6.00%; excess_return_240d -57.91% < 8.00%; drawdown_120d -41.66% < -28.00% |
| 600318.SH | 新力金融 | ok | 19.37 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.47% < 6.00%; excess_return_120d -35.05% < 6.00%; excess_return_240d -58.55% < 8.00%; drawdown_120d -38.98% < -28.00% |
| 603686.SH | 福龙马 | ok | 19.37 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -54.93% < 6.00%; excess_return_120d -59.51% < 6.00%; excess_return_240d -38.59% < 8.00%; drawdown_120d -54.89% < -28.00% |
| 688246.SH | 嘉和美康 | ok | 19.37 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.32% < 6.00%; excess_return_120d -18.90% < 6.00%; excess_return_240d -53.91% < 8.00%; drawdown_120d -48.92% < -28.00%; volatility_120d 59.86% > 42.00% |
| 000573.SZ | 粤宏远A | ok | 19.37 | close_below_ma200; stock_return_120d -14.46% < 6.00%; excess_return_120d -19.04% < 6.00%; excess_return_240d -34.50% < 8.00%; drawdown_120d -30.89% < -28.00%; volatility_120d 45.04% > 42.00% |
| 601089.SH | 福元医药 | ok | 19.37 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.10% < 6.00%; excess_return_120d -27.68% < 6.00%; excess_return_240d -20.99% < 8.00%; drawdown_120d -40.35% < -28.00% |
| 300317.SZ | 珈伟新能 | ok | 19.37 | close_below_ma200; stock_return_120d -2.08% < 6.00%; excess_return_120d -6.66% < 6.00%; excess_return_240d -36.60% < 8.00%; drawdown_120d -47.85% < -28.00%; volatility_120d 71.55% > 42.00% |
| 301119.SZ | 正强股份 | ok | 19.37 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -31.85% < 6.00%; excess_return_120d -36.43% < 6.00%; excess_return_240d -18.18% < 8.00%; drawdown_120d -42.09% < -28.00%; volatility_120d 60.06% > 42.00% |
| 002037.SZ | 保利联合 | ok | 19.36 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.32% < 6.00%; excess_return_120d -38.90% < 6.00%; excess_return_240d -54.22% < 8.00%; drawdown_120d -38.28% < -28.00% |
| 300701.SZ | 森霸传感 | ok | 19.36 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.02% < 6.00%; excess_return_120d -29.60% < 6.00%; excess_return_240d -27.15% < 8.00%; drawdown_120d -32.30% < -28.00% |
| 600662.SH | 外服控股 | ok | 19.36 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.13% < 6.00%; excess_return_120d -21.71% < 6.00%; excess_return_240d -37.90% < 8.00%; drawdown_120d -39.53% < -28.00% |
| 002276.SZ | 万马股份 | ok | 19.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.53% < 6.00%; excess_return_120d -43.11% < 6.00%; excess_return_240d -47.49% < 8.00%; drawdown_120d -44.52% < -28.00% |
| 001335.SZ | 信凯科技 | ok | 19.35 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -26.17% < 6.00%; excess_return_120d -30.75% < 6.00%; excess_return_240d -26.84% < 8.00%; drawdown_120d -37.98% < -28.00%; volatility_120d 49.79% > 42.00% |
| 600121.SH | 郑州煤电 | ok | 19.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.27% < 6.00%; excess_return_120d -15.85% < 6.00%; excess_return_240d -30.41% < 8.00%; drawdown_120d -40.80% < -28.00%; volatility_120d 60.26% > 42.00% |
| 300796.SZ | 贝斯美 | ok | 19.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.68% < 6.00%; excess_return_120d -29.26% < 6.00%; excess_return_240d -60.07% < 8.00%; drawdown_120d -41.06% < -28.00% |
| 000875.SZ | 电投绿能 | ok | 19.34 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.96% < 6.00%; excess_return_120d -13.54% < 6.00%; excess_return_240d -22.50% < 8.00%; drawdown_120d -38.71% < -28.00%; volatility_120d 46.44% > 42.00% |
| 001260.SZ | 坤泰股份 | ok | 19.34 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.10% < 6.00%; excess_return_120d -20.68% < 6.00%; excess_return_240d -33.41% < 8.00%; drawdown_120d -37.61% < -28.00%; volatility_120d 47.13% > 42.00% |
| 003027.SZ | 同兴科技 | ok | 19.34 | close_below_ma200; stock_return_120d -21.61% < 6.00%; excess_return_120d -26.19% < 6.00%; excess_return_240d -23.94% < 8.00%; drawdown_120d -37.40% < -28.00%; volatility_120d 47.09% > 42.00% |
| 300085.SZ | 银之杰 | ok | 19.34 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.94% < 6.00%; excess_return_120d -20.52% < 6.00%; excess_return_240d -43.66% < 8.00%; drawdown_120d -33.57% < -28.00%; volatility_120d 80.99% > 42.00% |
| 000633.SZ | 合金投资 | ok | 19.34 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.79% < 6.00%; excess_return_120d -35.37% < 6.00%; excess_return_240d -39.16% < 8.00%; drawdown_120d -39.95% < -28.00% |
| 002941.SZ | 新疆交建 | ok | 19.34 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.04% < 6.00%; excess_return_120d -42.62% < 6.00%; excess_return_240d -32.95% < 8.00%; drawdown_120d -46.49% < -28.00% |
| 001236.SZ | 弘业期货 | ok | 19.33 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.79% < 6.00%; excess_return_120d -36.37% < 6.00%; excess_return_240d -70.89% < 8.00%; drawdown_120d -34.98% < -28.00% |
| 002065.SZ | 东华软件 | ok | 19.33 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.48% < 6.00%; excess_return_120d -29.06% < 6.00%; excess_return_240d -47.43% < 8.00%; drawdown_120d -38.25% < -28.00% |
| 600316.SH | 洪都航空 | ok | 19.33 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.15% < 6.00%; excess_return_120d -21.73% < 6.00%; excess_return_240d -40.48% < 8.00%; drawdown_120d -39.32% < -28.00%; volatility_120d 47.07% > 42.00% |
| 002074.SZ | 国轩高科 | ok | 19.33 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.60% < 6.00%; excess_return_120d -36.18% < 6.00%; excess_return_240d -32.61% < 8.00%; drawdown_120d -36.75% < -28.00% |
| 000889.SZ | 中嘉博创 | ok | 19.32 | close_below_ma200; stock_return_120d -13.06% < 6.00%; excess_return_120d -17.64% < 6.00%; excess_return_240d -39.80% < 8.00%; drawdown_120d -46.86% < -28.00%; volatility_120d 75.14% > 42.00% |
| 601969.SH | 海南矿业 | ok | 19.32 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.39% < 6.00%; excess_return_120d -23.39% < 6.00%; excess_return_240d -1.43% < 8.00%; drawdown_120d -40.08% < -28.00%; volatility_120d 51.80% > 42.00% |
| 000718.SZ | 苏宁环球 | ok | 19.32 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.14% < 6.00%; excess_return_120d -27.72% < 6.00%; excess_return_240d -39.99% < 8.00%; drawdown_120d -28.74% < -28.00% |
| 300350.SZ | 华鹏飞 | ok | 19.32 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.29% < 6.00%; excess_return_120d -40.87% < 6.00%; excess_return_240d -54.65% < 8.00%; drawdown_120d -41.14% < -28.00% |
| 301487.SZ | 盟固利 | ok | 19.32 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -11.81% < 6.00%; excess_return_120d -16.39% < 6.00%; excess_return_240d -28.56% < 8.00%; drawdown_120d -28.87% < -28.00%; volatility_120d 45.53% > 42.00% |
| 002389.SZ | 航天彩虹 | ok | 19.31 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -24.25% < 6.00%; excess_return_120d -28.83% < 6.00%; excess_return_240d -47.68% < 8.00%; drawdown_120d -39.17% < -28.00%; volatility_120d 45.41% > 42.00% |
| 000663.SZ | 永安林业 | ok | 19.31 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.78% < 6.00%; excess_return_120d -32.36% < 6.00%; excess_return_240d -44.41% < 8.00%; drawdown_120d -37.88% < -28.00% |
| 000757.SZ | 浩物股份 | ok | 19.31 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.59% < 6.00%; excess_return_120d -27.17% < 6.00%; excess_return_240d -40.02% < 8.00%; drawdown_120d -29.93% < -28.00% |
| 002765.SZ | 蓝黛科技 | ok | 19.31 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.09% < 6.00%; excess_return_120d -44.67% < 6.00%; excess_return_240d -58.86% < 8.00%; drawdown_120d -40.89% < -28.00% |
| 688296.SH | 和达科技 | ok | 19.31 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.19% < 6.00%; excess_return_120d -14.77% < 6.00%; excess_return_240d -31.15% < 8.00%; drawdown_120d -30.77% < -28.00%; volatility_120d 42.10% > 42.00% |
| 600668.SH | 尖峰集团 | ok | 19.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.42% < 6.00%; excess_return_120d -36.00% < 6.00%; excess_return_240d -56.51% < 8.00%; drawdown_120d -36.48% < -28.00% |
| 000952.SZ | 广济药业 | ok | 19.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.49% < 6.00%; excess_return_120d -23.07% < 6.00%; excess_return_240d -33.08% < 8.00%; drawdown_120d -34.06% < -28.00% |
| 600615.SH | 鑫源智造 | ok | 19.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -13.86% < 6.00%; excess_return_120d -18.44% < 6.00%; excess_return_240d -36.47% < 8.00%; drawdown_120d -28.08% < -28.00%; volatility_120d 45.83% > 42.00% |
| 300463.SZ | 迈克生物 | ok | 19.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.64% < 6.00%; excess_return_120d -25.22% < 6.00%; excess_return_240d -47.16% < 8.00%; drawdown_120d -37.46% < -28.00% |
| 002263.SZ | 大东南 | ok | 19.30 | close_below_ma200; stock_return_120d -7.51% < 6.00%; excess_return_120d -12.09% < 6.00%; excess_return_240d -53.70% < 8.00%; drawdown_120d -42.43% < -28.00%; volatility_120d 62.96% > 42.00% |
| 603291.SH | 联合水务 | ok | 19.29 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -7.52% < 6.00%; excess_return_120d -12.10% < 6.00%; excess_return_240d -45.12% < 8.00%; drawdown_120d -31.64% < -28.00%; volatility_120d 45.66% > 42.00% |
| 603151.SH | 邦基科技 | ok | 19.29 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.85% < 6.00%; excess_return_120d -39.43% < 6.00%; excess_return_240d -65.59% < 8.00%; drawdown_120d -42.45% < -28.00% |
| 300777.SZ | 中简科技 | ok | 19.29 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -28.32% < 6.00%; excess_return_120d -32.91% < 6.00%; excess_return_240d -40.68% < 8.00%; drawdown_120d -40.47% < -28.00%; volatility_120d 58.04% > 42.00% |
| 600032.SH | 浙江新能 | ok | 19.29 | close_below_ma200; stock_return_120d -6.54% < 6.00%; excess_return_120d -11.12% < 6.00%; excess_return_240d -31.67% < 8.00%; drawdown_120d -50.97% < -28.00%; volatility_120d 63.90% > 42.00% |
| 600057.SH | 厦门象屿 | ok | 19.29 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.17% < 6.00%; excess_return_120d -33.75% < 6.00%; excess_return_240d -36.82% < 8.00%; drawdown_120d -31.69% < -28.00% |
| 001277.SZ | 速达股份 | ok | 19.29 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.35% < 6.00%; excess_return_120d -31.93% < 6.00%; excess_return_240d -56.42% < 8.00%; drawdown_120d -42.71% < -28.00% |
| 000852.SZ | 石化机械 | ok | 19.29 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.81% < 6.00%; excess_return_120d -35.39% < 6.00%; excess_return_240d -46.80% < 8.00%; drawdown_120d -47.49% < -28.00% |
| 603192.SH | 汇得科技 | ok | 19.29 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.32% < 6.00%; excess_return_120d -35.90% < 6.00%; excess_return_240d -34.91% < 8.00%; drawdown_120d -37.21% < -28.00% |
| 300363.SZ | 博腾股份 | ok | 19.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.38% < 6.00%; excess_return_120d -26.96% < 6.00%; excess_return_240d -16.98% < 8.00%; drawdown_120d -40.71% < -28.00%; volatility_120d 52.19% > 42.00% |
| 300306.SZ | 远方信息 | ok | 19.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.43% < 6.00%; excess_return_120d -34.01% < 6.00%; excess_return_240d -47.63% < 8.00%; drawdown_120d -37.53% < -28.00% |
| 300447.SZ | 全信股份 | ok | 19.28 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.15% < 6.00%; excess_return_120d -25.73% < 6.00%; excess_return_240d -30.30% < 8.00%; drawdown_120d -41.45% < -28.00%; volatility_120d 57.89% > 42.00% |
| 000025.SZ | 特力A | ok | 19.27 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.51% < 6.00%; excess_return_120d -27.09% < 6.00%; excess_return_240d -42.53% < 8.00%; drawdown_120d -32.32% < -28.00% |
| 002105.SZ | 信隆健康 | ok | 19.27 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.64% < 6.00%; excess_return_120d -34.22% < 6.00%; excess_return_240d -55.07% < 8.00%; drawdown_120d -33.80% < -28.00% |
| 002523.SZ | 天桥起重 | ok | 19.27 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.57% < 6.00%; excess_return_120d -33.15% < 6.00%; excess_return_240d -38.22% < 8.00%; drawdown_120d -39.00% < -28.00% |
| 603848.SH | 好太太 | ok | 19.27 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.14% < 6.00%; excess_return_120d -24.72% < 6.00%; excess_return_240d -25.85% < 8.00%; drawdown_120d -31.87% < -28.00% |
| 600232.SH | 金鹰股份 | ok | 19.26 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.11% < 6.00%; excess_return_120d -25.69% < 6.00%; excess_return_240d -24.05% < 8.00%; drawdown_120d -35.34% < -28.00%; volatility_120d 43.58% > 42.00% |
| 300941.SZ | 创识科技 | ok | 19.26 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.43% < 6.00%; excess_return_120d -45.01% < 6.00%; excess_return_240d -74.86% < 8.00%; drawdown_120d -43.64% < -28.00% |
| 002978.SZ | 安宁股份 | ok | 19.26 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.46% < 6.00%; excess_return_120d -24.04% < 6.00%; excess_return_240d -37.57% < 8.00%; drawdown_120d -38.66% < -28.00%; volatility_120d 43.96% > 42.00% |
| 001380.SZ | 华纬科技 | ok | 19.26 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.87% < 6.00%; excess_return_120d -31.45% < 6.00%; excess_return_240d -40.26% < 8.00%; drawdown_120d -34.15% < -28.00% |
| 301089.SZ | 拓新药业 | ok | 19.26 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.07% < 6.00%; excess_return_120d -20.65% < 6.00%; excess_return_240d -53.37% < 8.00%; drawdown_120d -35.33% < -28.00%; volatility_120d 43.17% > 42.00% |
| 300466.SZ | 赛摩智能 | ok | 19.26 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.06% < 6.00%; excess_return_120d -31.64% < 6.00%; excess_return_240d -49.72% < 8.00%; drawdown_120d -36.04% < -28.00% |
| 002519.SZ | 银河电子 | ok | 19.25 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.43% < 6.00%; excess_return_120d -18.01% < 6.00%; excess_return_240d -17.21% < 8.00%; drawdown_120d -55.55% < -28.00%; volatility_120d 71.30% > 42.00% |
| 002930.SZ | 宏川智慧 | ok | 19.25 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.39% < 6.00%; excess_return_120d -17.97% < 6.00%; excess_return_240d -30.67% < 8.00%; drawdown_120d -42.89% < -28.00%; volatility_120d 56.20% > 42.00% |
| 300364.SZ | 中文在线 | ok | 19.25 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.47% < 6.00%; excess_return_120d -15.05% < 6.00%; excess_return_240d -31.96% < 8.00%; drawdown_120d -48.65% < -28.00%; volatility_120d 78.59% > 42.00% |
| 300523.SZ | 辰安科技 | ok | 19.25 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.40% < 6.00%; excess_return_120d -26.98% < 6.00%; excess_return_240d -41.14% < 8.00%; drawdown_120d -29.66% < -28.00%; volatility_120d 44.03% > 42.00% |
| 603258.SH | 电魂网络 | ok | 19.25 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.82% < 6.00%; excess_return_120d -40.40% < 6.00%; excess_return_240d -73.19% < 8.00%; drawdown_120d -43.43% < -28.00% |
| 002476.SZ | 宝莫股份 | ok | 19.25 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -34.25% < 6.00%; excess_return_120d -38.83% < 6.00%; excess_return_240d -22.34% < 8.00%; drawdown_120d -40.43% < -28.00% |
| 002908.SZ | 德生科技 | ok | 19.24 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.12% < 6.00%; excess_return_120d -41.70% < 6.00%; excess_return_240d -61.78% < 8.00%; drawdown_120d -42.55% < -28.00% |
| 603300.SH | 海南华铁 | ok | 19.24 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -41.53% < 6.00%; excess_return_120d -46.11% < 6.00%; excess_return_240d -79.01% < 8.00%; drawdown_120d -44.30% < -28.00% |
| 300994.SZ | 久祺股份 | ok | 19.24 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.04% < 6.00%; excess_return_120d -32.62% < 6.00%; excess_return_240d -48.71% < 8.00%; drawdown_120d -34.84% < -28.00% |
| 000665.SZ | 湖北广电 | ok | 19.24 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.60% < 6.00%; excess_return_120d -41.18% < 6.00%; excess_return_240d -51.08% < 8.00%; drawdown_120d -41.43% < -28.00% |
| 603598.SH | 引力传媒 | ok | 19.24 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -2.83% < 6.00%; excess_return_120d -7.41% < 6.00%; excess_return_240d -26.27% < 8.00%; drawdown_120d -52.12% < -28.00%; volatility_120d 75.36% > 42.00% |
| 600319.SH | 亚星化学 | ok | 19.24 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.93% < 6.00%; excess_return_120d -35.51% < 6.00%; excess_return_240d -15.57% < 8.00%; drawdown_120d -33.23% < -28.00% |
| 002623.SZ | 亚玛顿 | ok | 19.23 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -5.37% < 6.00%; excess_return_120d -9.96% < 6.00%; excess_return_240d -51.93% < 8.00%; drawdown_120d -50.06% < -28.00%; volatility_120d 53.80% > 42.00% |
| 603799.SH | 华友钴业 | ok | 19.23 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -30.77% < 6.00%; excess_return_120d -35.35% < 6.00%; excess_return_240d 1.10% < 8.00%; drawdown_120d -42.56% < -28.00%; volatility_120d 50.23% > 42.00% |
| 600456.SH | 宝钛股份 | ok | 19.23 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -29.76% < 6.00%; excess_return_120d -34.34% < 6.00%; excess_return_240d -29.86% < 8.00%; drawdown_120d -39.02% < -28.00%; volatility_120d 45.59% > 42.00% |
| 300822.SZ | 贝仕达克 | ok | 19.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.45% < 6.00%; excess_return_120d -32.03% < 6.00%; excess_return_240d -59.76% < 8.00%; drawdown_120d -34.70% < -28.00% |
| 300569.SZ | 天能重工 | ok | 19.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.37% < 6.00%; excess_return_120d -18.95% < 6.00%; excess_return_240d -35.18% < 8.00%; drawdown_120d -45.14% < -28.00% |
| 601999.SH | 出版传媒 | ok | 19.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.01% < 6.00%; excess_return_120d -20.59% < 6.00%; excess_return_240d -38.90% < 8.00%; drawdown_120d -34.06% < -28.00%; volatility_120d 43.83% > 42.00% |
| 688203.SH | 海正生材 | ok | 19.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.56% < 6.00%; excess_return_120d -24.14% < 6.00%; excess_return_240d -45.84% < 8.00%; drawdown_120d -31.28% < -28.00% |
| 300514.SZ | 友讯达 | ok | 19.22 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.07% < 6.00%; excess_return_120d -33.65% < 6.00%; excess_return_240d -52.05% < 8.00%; drawdown_120d -39.27% < -28.00% |
| 000985.SZ | 大庆华科 | ok | 19.22 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.56% < 6.00%; excess_return_120d -27.14% < 6.00%; excess_return_240d -41.77% < 8.00%; drawdown_120d -40.81% < -28.00% |
| 600571.SH | 信雅达 | ok | 19.22 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.22% < 6.00%; excess_return_120d -42.80% < 6.00%; excess_return_240d -71.41% < 8.00%; drawdown_120d -48.04% < -28.00% |
| 300335.SZ | 迪森股份 | ok | 19.22 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.66% < 6.00%; excess_return_120d -16.24% < 6.00%; excess_return_240d -44.76% < 8.00%; drawdown_120d -45.36% < -28.00%; volatility_120d 53.86% > 42.00% |
| 600657.SH | 信达地产 | ok | 19.22 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.30% < 6.00%; excess_return_120d -35.88% < 6.00%; excess_return_240d -61.55% < 8.00%; drawdown_120d -36.29% < -28.00% |
| 603069.SH | 海汽集团 | ok | 19.22 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -52.93% < 6.00%; excess_return_120d -57.51% < 6.00%; excess_return_240d -61.49% < 8.00%; drawdown_120d -51.39% < -28.00% |
| 002564.SZ | 天沃科技 | ok | 19.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -43.12% < 6.00%; excess_return_120d -47.70% < 6.00%; excess_return_240d -43.44% < 8.00%; drawdown_120d -47.04% < -28.00% |
| 002678.SZ | 珠江钢琴 | ok | 19.21 | close_below_ma200; stock_return_120d -18.95% < 6.00%; excess_return_120d -23.53% < 6.00%; excess_return_240d -35.72% < 8.00%; drawdown_120d -33.23% < -28.00%; volatility_120d 52.95% > 42.00% |
| 002847.SZ | 盐津铺子 | ok | 19.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.48% < 6.00%; excess_return_120d -34.06% < 6.00%; excess_return_240d -58.47% < 8.00%; drawdown_120d -37.03% < -28.00% |
| 002418.SZ | 康盛股份 | ok | 19.21 | close_below_ma200; stock_return_120d -16.56% < 6.00%; excess_return_120d -21.14% < 6.00%; excess_return_240d -10.23% < 8.00%; drawdown_120d -44.10% < -28.00%; volatility_120d 67.62% > 42.00% |
| 600594.SH | 益佰制药 | ok | 19.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.34% < 6.00%; excess_return_120d -21.92% < 6.00%; excess_return_240d -40.06% < 8.00%; drawdown_120d -37.57% < -28.00%; volatility_120d 49.19% > 42.00% |
| 600873.SH | 梅花生物 | ok | 19.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.43% < 6.00%; excess_return_120d -25.01% < 6.00%; excess_return_240d -47.42% < 8.00%; drawdown_120d -39.12% < -28.00% |
| 000637.SZ | 茂化实华 | ok | 19.20 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.12% < 6.00%; excess_return_120d -19.70% < 6.00%; excess_return_240d -34.40% < 8.00%; drawdown_120d -38.66% < -28.00% |
| 300650.SZ | 太龙股份 | ok | 19.20 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.17% < 6.00%; excess_return_120d -21.75% < 6.00%; excess_return_240d -31.14% < 8.00%; drawdown_120d -34.23% < -28.00%; volatility_120d 56.08% > 42.00% |
| 601566.SH | 九牧王 | ok | 19.20 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.61% < 6.00%; excess_return_120d -35.19% < 6.00%; excess_return_240d -16.81% < 8.00%; drawdown_120d -34.36% < -28.00%; volatility_120d 42.36% > 42.00% |
| 688696.SH | 极米科技 | ok | 19.20 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -41.08% < 6.00%; excess_return_120d -45.66% < 6.00%; excess_return_240d -58.98% < 8.00%; drawdown_120d -43.39% < -28.00% |
| 000731.SZ | 四川美丰 | ok | 19.20 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.89% < 6.00%; excess_return_120d -22.47% < 6.00%; excess_return_240d -43.18% < 8.00%; drawdown_120d -38.13% < -28.00% |
| 002670.SZ | 国盛证券 | ok | 19.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.67% < 6.00%; excess_return_120d -32.25% < 6.00%; excess_return_240d -38.30% < 8.00%; drawdown_120d -31.61% < -28.00% |
| 300950.SZ | 德固特 | ok | 19.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.52% < 6.00%; excess_return_120d -31.10% < 6.00%; excess_return_240d -43.20% < 8.00%; drawdown_120d -39.45% < -28.00% |
| 002268.SZ | 电科网安 | ok | 19.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.34% < 6.00%; excess_return_120d -36.92% < 6.00%; excess_return_240d -43.58% < 8.00%; drawdown_120d -41.57% < -28.00% |
| 301318.SZ | 维海德 | ok | 19.18 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.55% < 6.00%; excess_return_120d -30.13% < 6.00%; excess_return_240d -60.28% < 8.00%; drawdown_120d -35.13% < -28.00% |
| 002530.SZ | 金财互联 | ok | 19.18 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.58% < 6.00%; excess_return_120d -41.16% < 6.00%; excess_return_240d -56.96% < 8.00%; drawdown_120d -41.98% < -28.00% |
| 301586.SZ | 佳力奇 | ok | 19.18 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.95% < 6.00%; excess_return_120d -38.53% < 6.00%; excess_return_240d -62.56% < 8.00%; drawdown_120d -41.41% < -28.00% |
| 300616.SZ | 尚品宅配 | ok | 19.18 | close_below_ma200; stock_return_120d -20.41% < 6.00%; excess_return_120d -24.99% < 6.00%; excess_return_240d -39.49% < 8.00%; drawdown_120d -42.74% < -28.00%; volatility_120d 64.68% > 42.00% |
| 603909.SH | 建发合诚 | ok | 19.18 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.75% < 6.00%; excess_return_120d -24.33% < 6.00%; excess_return_240d -29.97% < 8.00%; drawdown_120d -35.91% < -28.00% |
| 688327.SH | 云从科技 | ok | 19.18 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.77% < 6.00%; excess_return_120d -21.35% < 6.00%; excess_return_240d -31.31% < 8.00%; drawdown_120d -37.61% < -28.00%; volatility_120d 54.29% > 42.00% |
| 002232.SZ | 启明信息 | ok | 19.18 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.72% < 6.00%; excess_return_120d -27.30% < 6.00%; excess_return_240d -40.38% < 8.00%; drawdown_120d -30.89% < -28.00% |
| 600266.SH | 城建发展 | ok | 19.18 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.34% < 6.00%; excess_return_120d -22.92% < 6.00%; excess_return_240d -33.76% < 8.00%; drawdown_120d -44.80% < -28.00%; volatility_120d 47.87% > 42.00% |
| 600249.SH | 两面针 | ok | 19.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.37% < 6.00%; excess_return_120d -24.74% < 6.00%; excess_return_240d -42.63% < 8.00%; drawdown_120d -38.65% < -28.00% |
| 300276.SZ | 三丰智能 | ok | 19.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.63% < 6.00%; excess_return_120d -32.21% < 6.00%; excess_return_240d -54.75% < 8.00%; drawdown_120d -33.27% < -28.00%; volatility_120d 57.70% > 42.00% |
| 688588.SH | 凌志软件 | ok | 19.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.20% < 6.00%; excess_return_120d -39.78% < 6.00%; excess_return_240d -57.27% < 8.00%; drawdown_120d -45.54% < -28.00% |
| 002873.SZ | 新天药业 | ok | 19.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.53% < 6.00%; excess_return_120d -25.11% < 6.00%; excess_return_240d -39.49% < 8.00%; drawdown_120d -39.82% < -28.00% |
| 300003.SZ | 乐普医疗 | ok | 19.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.00% < 6.00%; excess_return_120d -22.58% < 6.00%; excess_return_240d -38.15% < 8.00%; drawdown_120d -40.15% < -28.00% |
| 603178.SH | 圣龙股份 | ok | 19.17 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -21.25% < 6.00%; excess_return_120d -25.83% < 6.00%; excess_return_240d -41.46% < 8.00%; drawdown_120d -38.08% < -28.00%; volatility_120d 55.19% > 42.00% |
| 600882.SH | 妙可蓝多 | ok | 19.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.74% < 6.00%; excess_return_120d -36.32% < 6.00%; excess_return_240d -63.47% < 8.00%; drawdown_120d -32.81% < -28.00% |
| 600219.SH | 南山铝业 | ok | 19.16 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.10% < 6.00%; excess_return_120d -24.68% < 6.00%; excess_return_240d -0.28% < 8.00%; drawdown_120d -49.60% < -28.00%; volatility_120d 57.25% > 42.00% |
| 603236.SH | 移远通信 | ok | 19.16 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.55% < 6.00%; excess_return_120d -31.13% < 6.00%; excess_return_240d -39.63% < 8.00%; drawdown_120d -34.55% < -28.00%; volatility_120d 43.26% > 42.00% |
| 301229.SZ | 纽泰格 | ok | 19.16 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -43.98% < 6.00%; excess_return_120d -48.56% < 6.00%; excess_return_240d -55.50% < 8.00%; drawdown_120d -45.12% < -28.00% |
| 301032.SZ | 新柴股份 | ok | 19.16 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.20% < 6.00%; excess_return_120d -18.78% < 6.00%; excess_return_240d -42.13% < 8.00%; drawdown_120d -31.93% < -28.00%; volatility_120d 49.35% > 42.00% |
| 688299.SH | 长阳科技 | ok | 19.16 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -10.17% < 6.00%; excess_return_120d -14.75% < 6.00%; excess_return_240d -41.97% < 8.00%; drawdown_120d -29.14% < -28.00%; volatility_120d 50.50% > 42.00% |
| 001209.SZ | 洪兴股份 | ok | 19.16 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.78% < 6.00%; excess_return_120d -24.36% < 6.00%; excess_return_240d -27.47% < 8.00%; drawdown_120d -52.28% < -28.00%; volatility_120d 52.11% > 42.00% |
| 605056.SH | 咸亨国际 | ok | 19.16 | close_below_ma200; stock_return_120d -0.56% < 6.00%; excess_return_120d -5.14% < 6.00%; excess_return_240d -15.42% < 8.00%; drawdown_120d -47.20% < -28.00%; volatility_120d 54.13% > 42.00% |
| 300405.SZ | 科隆股份 | ok | 19.16 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.40% < 6.00%; excess_return_120d -21.98% < 6.00%; excess_return_240d -31.17% < 8.00%; drawdown_120d -30.47% < -28.00% |
| 300150.SZ | 世纪瑞尔 | ok | 19.15 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.95% < 6.00%; excess_return_120d -29.53% < 6.00%; excess_return_240d -44.16% < 8.00%; drawdown_120d -35.24% < -28.00% |
| 688161.SH | 威高骨科 | ok | 19.15 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.08% < 6.00%; excess_return_120d -23.66% < 6.00%; excess_return_240d -34.74% < 8.00%; drawdown_120d -30.95% < -28.00% |
| 688466.SH | 金科环境 | ok | 19.15 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.01% < 6.00%; excess_return_120d -22.59% < 6.00%; excess_return_240d -51.25% < 8.00%; drawdown_120d -31.38% < -28.00% |
| 002599.SZ | 盛通股份 | ok | 19.15 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.64% < 6.00%; excess_return_120d -40.22% < 6.00%; excess_return_240d -55.27% < 8.00%; drawdown_120d -43.63% < -28.00% |
| 300007.SZ | 汉威科技 | ok | 19.15 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.65% < 6.00%; excess_return_120d -29.23% < 6.00%; excess_return_240d -16.45% < 8.00%; drawdown_120d -40.51% < -28.00%; volatility_120d 49.23% > 42.00% |
| 600620.SH | 天宸股份 | ok | 19.14 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.69% < 6.00%; excess_return_120d -42.27% < 6.00%; excess_return_240d -48.32% < 8.00%; drawdown_120d -45.56% < -28.00% |
| 600506.SH | 统一股份 | ok | 19.14 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.04% < 6.00%; excess_return_120d -32.62% < 6.00%; excess_return_240d -27.59% < 8.00%; drawdown_120d -36.07% < -28.00%; volatility_120d 44.89% > 42.00% |
| 300517.SZ | 海波重科 | ok | 19.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.15% < 6.00%; excess_return_120d -19.73% < 6.00%; excess_return_240d -34.99% < 8.00%; drawdown_120d -30.60% < -28.00% |
| 301187.SZ | 欧圣电气 | ok | 19.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -41.97% < 6.00%; excess_return_120d -46.55% < 6.00%; excess_return_240d -66.52% < 8.00%; drawdown_120d -46.42% < -28.00% |
| 300261.SZ | 雅本化学 | ok | 19.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.65% < 6.00%; excess_return_120d -36.23% < 6.00%; excess_return_240d -57.21% < 8.00%; drawdown_120d -40.80% < -28.00% |
| 600754.SH | 锦江酒店 | ok | 19.13 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -24.35% < 6.00%; excess_return_120d -28.93% < 6.00%; excess_return_240d -33.16% < 8.00%; drawdown_120d -35.32% < -28.00% |
| 300220.SZ | 金运激光 | ok | 19.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.67% < 6.00%; excess_return_120d -32.25% < 6.00%; excess_return_240d -63.65% < 8.00%; drawdown_120d -37.09% < -28.00% |
| 600505.SH | 西昌电力 | ok | 19.12 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.30% < 6.00%; excess_return_120d -20.88% < 6.00%; excess_return_240d -53.52% < 8.00%; drawdown_120d -31.24% < -28.00%; volatility_120d 45.49% > 42.00% |
| 300647.SZ | 超频三 | ok | 19.12 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.03% < 6.00%; excess_return_120d -24.61% < 6.00%; excess_return_240d -36.97% < 8.00%; drawdown_120d -29.27% < -28.00%; volatility_120d 43.68% > 42.00% |
| 603023.SH | 威帝股份 | ok | 19.12 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -24.45% < 6.00%; excess_return_120d -29.03% < 6.00%; excess_return_240d -21.88% < 8.00%; drawdown_120d -41.98% < -28.00%; volatility_120d 53.06% > 42.00% |
| 300269.SZ | 联建光电 | ok | 19.11 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.51% < 6.00%; excess_return_120d -24.09% < 6.00%; excess_return_240d -28.47% < 8.00%; drawdown_120d -46.34% < -28.00%; volatility_120d 78.84% > 42.00% |
| 000975.SZ | 山金国际 | ok | 19.11 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.26% < 6.00%; excess_return_120d -19.84% < 6.00%; excess_return_240d -11.20% < 8.00%; drawdown_120d -51.66% < -28.00%; volatility_120d 64.30% > 42.00% |
| 301063.SZ | 海锅股份 | ok | 19.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.94% < 6.00%; excess_return_120d -32.52% < 6.00%; excess_return_240d -60.55% < 8.00%; drawdown_120d -46.50% < -28.00% |
| 300676.SZ | 华大基因 | ok | 19.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.24% < 6.00%; excess_return_120d -24.82% < 6.00%; excess_return_240d -48.05% < 8.00%; drawdown_120d -44.34% < -28.00% |
| 301503.SZ | 智迪科技 | ok | 19.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.04% < 6.00%; excess_return_120d -27.63% < 6.00%; excess_return_240d -49.24% < 8.00%; drawdown_120d -31.28% < -28.00% |
| 000151.SZ | 中成股份 | ok | 19.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.98% < 6.00%; excess_return_120d -19.56% < 6.00%; excess_return_240d -40.75% < 8.00%; drawdown_120d -34.12% < -28.00%; volatility_120d 46.33% > 42.00% |
| 301300.SZ | 远翔新材 | ok | 19.10 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.93% < 6.00%; excess_return_120d -28.51% < 6.00%; excess_return_240d -33.57% < 8.00%; drawdown_120d -35.24% < -28.00% |
| 000761.SZ | 本钢板材 | ok | 19.10 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.73% < 6.00%; excess_return_120d -38.31% < 6.00%; excess_return_240d -62.68% < 8.00%; drawdown_120d -43.51% < -28.00% |
| 002778.SZ | 中晟高科 | ok | 19.10 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.83% < 6.00%; excess_return_120d -29.41% < 6.00%; excess_return_240d -37.19% < 8.00%; drawdown_120d -32.24% < -28.00% |
| 600463.SH | 空港股份 | ok | 19.10 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.45% < 6.00%; excess_return_120d -36.03% < 6.00%; excess_return_240d -46.84% < 8.00%; drawdown_120d -38.51% < -28.00% |
| 600649.SH | 城投控股 | ok | 19.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.43% < 6.00%; excess_return_120d -23.01% < 6.00%; excess_return_240d -37.65% < 8.00%; drawdown_120d -37.20% < -28.00%; volatility_120d 42.17% > 42.00% |
| 000096.SZ | 广聚能源 | ok | 19.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.41% < 6.00%; excess_return_120d -33.99% < 6.00%; excess_return_240d -64.92% < 8.00%; drawdown_120d -45.37% < -28.00% |
| 600439.SH | 瑞贝卡 | ok | 19.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.66% < 6.00%; excess_return_120d -26.24% < 6.00%; excess_return_240d -60.65% < 8.00%; drawdown_120d -28.62% < -28.00% |
| 605155.SH | 西大门 | ok | 19.08 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.00% < 6.00%; excess_return_120d -27.58% < 6.00%; excess_return_240d -13.71% < 8.00%; drawdown_120d -39.34% < -28.00%; volatility_120d 47.74% > 42.00% |
| 600637.SH | 东方明珠 | ok | 19.08 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.07% < 6.00%; excess_return_120d -22.65% < 6.00%; excess_return_240d -10.55% < 8.00%; drawdown_120d -49.94% < -28.00%; volatility_120d 54.84% > 42.00% |
| 002144.SZ | 宏达高科 | ok | 19.08 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.35% < 6.00%; excess_return_120d -22.93% < 6.00%; excess_return_240d -33.34% < 8.00%; drawdown_120d -41.79% < -28.00% |
| 002791.SZ | 坚朗五金 | ok | 19.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.94% < 6.00%; excess_return_120d -39.52% < 6.00%; excess_return_240d -56.94% < 8.00%; drawdown_120d -48.58% < -28.00% |
| 300100.SZ | 双林股份 | ok | 19.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.87% < 6.00%; excess_return_120d -31.45% < 6.00%; excess_return_240d -57.23% < 8.00%; drawdown_120d -30.31% < -28.00%; volatility_120d 49.81% > 42.00% |
| 000968.SZ | 蓝焰控股 | ok | 19.06 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.42% < 6.00%; excess_return_120d -9.00% < 6.00%; excess_return_240d -32.79% < 8.00%; drawdown_120d -48.31% < -28.00%; volatility_120d 65.65% > 42.00% |
| 000403.SZ | 派林生物 | ok | 19.06 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.15% < 6.00%; excess_return_120d -33.73% < 6.00%; excess_return_240d -66.82% < 8.00%; drawdown_120d -34.28% < -28.00% |
| 002877.SZ | 智能自控 | ok | 19.06 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.70% < 6.00%; excess_return_120d -25.28% < 6.00%; excess_return_240d -34.53% < 8.00%; drawdown_120d -37.24% < -28.00%; volatility_120d 44.31% > 42.00% |
| 600075.SH | 新疆天业 | ok | 19.05 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.71% < 6.00%; excess_return_120d -15.29% < 6.00%; excess_return_240d -20.18% < 8.00%; drawdown_120d -45.63% < -28.00%; volatility_120d 59.75% > 42.00% |
| 601011.SH | 宝泰隆 | ok | 19.05 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.71% < 6.00%; excess_return_120d -24.29% < 6.00%; excess_return_240d -19.23% < 8.00%; drawdown_120d -33.58% < -28.00%; volatility_120d 50.99% > 42.00% |
| 002075.SZ | 沙钢股份 | ok | 19.05 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.09% < 6.00%; excess_return_120d -44.67% < 6.00%; excess_return_240d -62.66% < 8.00%; drawdown_120d -46.95% < -28.00% |
| 002486.SZ | 嘉麟杰 | ok | 19.05 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.70% < 6.00%; excess_return_120d -32.28% < 6.00%; excess_return_240d -38.99% < 8.00%; drawdown_120d -32.08% < -28.00% |
| 688177.SH | 百奥泰 | ok | 19.05 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.80% < 6.00%; excess_return_120d -23.38% < 6.00%; excess_return_240d -49.35% < 8.00%; drawdown_120d -28.64% < -28.00% |
| 601121.SH | 宝地矿业 | ok | 19.05 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.54% < 6.00%; excess_return_120d -24.12% < 6.00%; excess_return_240d -27.44% < 8.00%; drawdown_120d -36.14% < -28.00%; volatility_120d 42.23% > 42.00% |
| 000796.SZ | 凯撒旅业 | ok | 19.05 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -46.53% < 6.00%; excess_return_120d -51.11% < 6.00%; excess_return_240d -34.39% < 8.00%; drawdown_120d -45.70% < -28.00% |
| 603086.SH | 先达股份 | ok | 19.05 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.91% < 6.00%; excess_return_120d -35.49% < 6.00%; excess_return_240d -68.37% < 8.00%; drawdown_120d -37.67% < -28.00% |
| 000524.SZ | 岭南控股 | ok | 19.04 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.99% < 6.00%; excess_return_120d -35.04% < 6.00%; excess_return_240d -46.93% < 8.00%; drawdown_120d -34.33% < -28.00% |
| 300678.SZ | 中科信息 | ok | 19.04 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.72% < 6.00%; excess_return_120d -32.30% < 6.00%; excess_return_240d -54.72% < 8.00%; drawdown_120d -42.26% < -28.00% |
| 300403.SZ | 汉宇集团 | ok | 19.04 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.10% < 6.00%; excess_return_120d -30.68% < 6.00%; excess_return_240d -46.89% < 8.00%; drawdown_120d -30.05% < -28.00%; volatility_120d 48.22% > 42.00% |
| 001328.SZ | 登康口腔 | ok | 19.04 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.43% < 6.00%; excess_return_120d -34.01% < 6.00%; excess_return_240d -59.98% < 8.00%; drawdown_120d -37.33% < -28.00% |
| 002622.SZ | 皓宸医疗 | ok | 19.03 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.94% < 6.00%; excess_return_120d -31.52% < 6.00%; excess_return_240d -45.75% < 8.00%; drawdown_120d -35.03% < -28.00% |
| 301082.SZ | 久盛电气 | ok | 19.03 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.44% < 6.00%; excess_return_120d -40.02% < 6.00%; excess_return_240d -66.00% < 8.00%; drawdown_120d -44.42% < -28.00% |
| 300977.SZ | 深圳瑞捷 | ok | 19.03 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.57% < 6.00%; excess_return_120d -13.15% < 6.00%; excess_return_240d -37.11% < 8.00%; drawdown_120d -39.71% < -28.00%; volatility_120d 51.35% > 42.00% |
| 600131.SH | 国网信通 | ok | 19.03 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.06% < 6.00%; excess_return_120d -15.64% < 6.00%; excess_return_240d -39.37% < 8.00%; drawdown_120d -40.70% < -28.00%; volatility_120d 44.37% > 42.00% |
| 300841.SZ | 康华生物 | ok | 19.03 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.47% < 6.00%; excess_return_120d -37.05% < 6.00%; excess_return_240d -47.95% < 8.00%; drawdown_120d -37.23% < -28.00% |
| 000880.SZ | 潍柴重机 | ok | 19.03 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.97% < 6.00%; excess_return_120d -16.55% < 6.00%; excess_return_240d -26.76% < 8.00%; drawdown_120d -40.44% < -28.00%; volatility_120d 62.78% > 42.00% |
| 002664.SZ | 信质集团 | ok | 19.03 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.00% < 6.00%; excess_return_120d -24.58% < 6.00%; excess_return_240d -13.32% < 8.00%; drawdown_120d -32.46% < -28.00%; volatility_120d 50.36% > 42.00% |
| 300637.SZ | 扬帆新材 | ok | 19.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.38% < 6.00%; excess_return_120d -20.96% < 6.00%; excess_return_240d -40.06% < 8.00%; drawdown_120d -31.69% < -28.00%; volatility_120d 44.83% > 42.00% |
| 002819.SZ | 东方中科 | ok | 19.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.61% < 6.00%; excess_return_120d -29.19% < 6.00%; excess_return_240d -50.08% < 8.00%; drawdown_120d -35.41% < -28.00% |
| 300075.SZ | 数字政通 | ok | 19.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.92% < 6.00%; excess_return_120d -37.50% < 6.00%; excess_return_240d -61.82% < 8.00%; drawdown_120d -43.43% < -28.00% |
| 603590.SH | 康辰药业 | ok | 19.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.45% < 6.00%; excess_return_120d -21.03% < 6.00%; excess_return_240d -25.39% < 8.00%; volatility_120d 43.06% > 42.00% |
| 603583.SH | 捷昌驱动 | ok | 19.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.70% < 6.00%; excess_return_120d -40.28% < 6.00%; excess_return_240d -50.12% < 8.00%; drawdown_120d -39.13% < -28.00% |
| 002053.SZ | 云南能投 | ok | 19.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.15% < 6.00%; excess_return_120d -20.73% < 6.00%; excess_return_240d -33.16% < 8.00%; drawdown_120d -32.60% < -28.00%; volatility_120d 45.49% > 42.00% |
| 002219.SZ | 新里程 | ok | 19.02 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.62% < 6.00%; excess_return_120d -18.20% < 6.00%; excess_return_240d -35.12% < 8.00%; drawdown_120d -38.05% < -28.00%; volatility_120d 46.20% > 42.00% |
| 000681.SZ | 视觉中国 | ok | 19.02 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.14% < 6.00%; excess_return_120d -27.72% < 6.00%; excess_return_240d -27.62% < 8.00%; drawdown_120d -47.88% < -28.00%; volatility_120d 65.24% > 42.00% |
| 000978.SZ | 桂林旅游 | ok | 19.02 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -24.31% < 6.00%; excess_return_120d -28.89% < 6.00%; excess_return_240d -32.85% < 8.00%; drawdown_120d -36.87% < -28.00%; volatility_120d 42.69% > 42.00% |
| 603833.SH | 欧派家居 | ok | 19.01 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.45% < 6.00%; excess_return_120d -39.04% < 6.00%; excess_return_240d -57.82% < 8.00%; drawdown_120d -47.28% < -28.00% |
| 300926.SZ | 博俊科技 | ok | 19.01 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -41.89% < 6.00%; excess_return_120d -46.47% < 6.00%; excess_return_240d -48.91% < 8.00%; drawdown_120d -43.79% < -28.00% |
| 002583.SZ | 海能达 | ok | 19.01 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.24% < 6.00%; excess_return_120d -33.82% < 6.00%; excess_return_240d -53.90% < 8.00%; drawdown_120d -35.66% < -28.00% |
| 300314.SZ | 戴维医疗 | ok | 19.01 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.52% < 6.00%; excess_return_120d -26.10% < 6.00%; excess_return_240d -44.22% < 8.00%; drawdown_120d -35.63% < -28.00% |
| 300288.SZ | 朗玛信息 | ok | 19.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.76% < 6.00%; excess_return_120d -37.34% < 6.00%; excess_return_240d -61.04% < 8.00%; drawdown_120d -47.72% < -28.00% |
| 000777.SZ | 中核科技 | ok | 19.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -31.61% < 6.00%; excess_return_120d -36.19% < 6.00%; excess_return_240d -34.04% < 8.00%; drawdown_120d -43.50% < -28.00%; volatility_120d 54.77% > 42.00% |
| 300417.SZ | 南华仪器 | ok | 19.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.78% < 6.00%; excess_return_120d -29.36% < 6.00%; excess_return_240d -38.33% < 8.00%; drawdown_120d -33.35% < -28.00% |
| 002188.SZ | 中天服务 | ok | 19.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.61% < 6.00%; excess_return_120d -21.19% < 6.00%; excess_return_240d -31.84% < 8.00%; drawdown_120d -32.40% < -28.00% |
| 603758.SH | 秦安股份 | ok | 18.99 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.31% < 6.00%; excess_return_120d -44.89% < 6.00%; excess_return_240d -55.94% < 8.00%; drawdown_120d -41.52% < -28.00% |
| 688539.SH | 高华科技 | ok | 18.99 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -36.99% < 6.00%; excess_return_120d -41.57% < 6.00%; excess_return_240d -2.29% < 8.00%; drawdown_120d -46.99% < -28.00%; volatility_120d 58.27% > 42.00% |
| 688528.SH | 秦川物联 | ok | 18.99 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.88% < 6.00%; excess_return_120d -20.46% < 6.00%; excess_return_240d -34.48% < 8.00%; drawdown_120d -37.86% < -28.00% |
| 600626.SH | 申达股份 | ok | 18.99 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.30% < 6.00%; excess_return_120d -36.88% < 6.00%; excess_return_240d -32.00% < 8.00%; drawdown_120d -40.00% < -28.00% |
| 603680.SH | 今创集团 | ok | 18.99 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -31.72% < 6.00%; excess_return_120d -36.30% < 6.00%; excess_return_240d -28.31% < 8.00%; drawdown_120d -41.46% < -28.00%; volatility_120d 47.03% > 42.00% |
| 688687.SH | 凯因科技 | ok | 18.99 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.19% < 6.00%; excess_return_120d -33.77% < 6.00%; excess_return_240d -53.72% < 8.00%; drawdown_120d -36.12% < -28.00% |
| 003029.SZ | 吉大正元 | ok | 18.98 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.55% < 6.00%; excess_return_120d -42.13% < 6.00%; excess_return_240d -64.78% < 8.00%; drawdown_120d -44.48% < -28.00% |
| 002247.SZ | 聚力文化 | ok | 18.98 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.06% < 6.00%; excess_return_120d -26.64% < 6.00%; excess_return_240d -41.46% < 8.00%; drawdown_120d -30.25% < -28.00% |
| 300892.SZ | 品渥食品 | ok | 18.98 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.76% < 6.00%; excess_return_120d -38.35% < 6.00%; excess_return_240d -62.25% < 8.00%; drawdown_120d -45.04% < -28.00% |
| 002685.SZ | 华东重机 | ok | 18.98 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -17.62% < 6.00%; excess_return_120d -22.20% < 6.00%; excess_return_240d -39.16% < 8.00%; drawdown_120d -38.18% < -28.00%; volatility_120d 48.34% > 42.00% |
| 688567.SH | 孚能科技 | ok | 18.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.65% < 6.00%; excess_return_120d -40.24% < 6.00%; excess_return_240d -48.55% < 8.00%; drawdown_120d -40.76% < -28.00% |
| 603273.SH | 天元智能 | ok | 18.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.49% < 6.00%; excess_return_120d -37.07% < 6.00%; excess_return_240d -40.88% < 8.00%; drawdown_120d -33.54% < -28.00% |
| 300813.SZ | 泰林生物 | ok | 18.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.71% < 6.00%; excess_return_120d -17.29% < 6.00%; excess_return_240d -18.95% < 8.00%; drawdown_120d -31.91% < -28.00% |
| 002241.SZ | 歌尔股份 | ok | 18.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.75% < 6.00%; excess_return_120d -29.33% < 6.00%; excess_return_240d -24.80% < 8.00%; drawdown_120d -32.19% < -28.00% |
| 002114.SZ | 罗平锌电 | ok | 18.97 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.81% < 6.00%; excess_return_120d -22.39% < 6.00%; excess_return_240d -26.04% < 8.00%; drawdown_120d -42.14% < -28.00%; volatility_120d 56.70% > 42.00% |
| 600371.SH | 万向德农 | ok | 18.97 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.69% < 6.00%; excess_return_120d -26.27% < 6.00%; excess_return_240d -49.14% < 8.00%; drawdown_120d -33.76% < -28.00% |
| 000659.SZ | 珠海中富 | ok | 18.96 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -24.48% < 6.00%; excess_return_120d -28.85% < 6.00%; excess_return_240d -16.20% < 8.00%; drawdown_120d -42.32% < -28.00%; volatility_120d 53.06% > 42.00% |
| 600715.SH | 文投控股 | ok | 18.96 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.28% < 6.00%; excess_return_120d -34.86% < 6.00%; excess_return_240d -54.72% < 8.00%; drawdown_120d -42.21% < -28.00% |
| 300107.SZ | 建新股份 | ok | 18.95 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.69% < 6.00%; excess_return_120d -20.27% < 6.00%; excess_return_240d -48.13% < 8.00%; drawdown_120d -46.51% < -28.00%; volatility_120d 47.50% > 42.00% |
| 300862.SZ | 蓝盾光电 | ok | 18.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.61% < 6.00%; excess_return_120d -21.19% < 6.00%; excess_return_240d -44.39% < 8.00%; drawdown_120d -37.50% < -28.00%; volatility_120d 52.29% > 42.00% |
| 001379.SZ | 腾达科技 | ok | 18.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.71% < 6.00%; excess_return_120d -36.29% < 6.00%; excess_return_240d -43.14% < 8.00%; drawdown_120d -39.77% < -28.00% |
| 301048.SZ | 金鹰重工 | ok | 18.95 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.70% < 6.00%; excess_return_120d -25.28% < 6.00%; excess_return_240d -40.02% < 8.00%; drawdown_120d -33.38% < -28.00%; volatility_120d 43.70% > 42.00% |
| 002331.SZ | 皖通科技 | ok | 18.94 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.74% < 6.00%; excess_return_120d -25.32% < 6.00%; excess_return_240d -33.71% < 8.00%; drawdown_120d -34.54% < -28.00%; volatility_120d 44.39% > 42.00% |
| 300359.SZ | 全通教育 | ok | 18.94 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.92% < 6.00%; excess_return_120d -33.50% < 6.00%; excess_return_240d -57.91% < 8.00%; drawdown_120d -40.93% < -28.00% |
| 300644.SZ | 南京聚隆 | ok | 18.94 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.05% < 6.00%; excess_return_120d -36.63% < 6.00%; excess_return_240d -26.68% < 8.00%; drawdown_120d -36.50% < -28.00% |
| 300414.SZ | 中光防雷 | ok | 18.94 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.21% < 6.00%; excess_return_120d -31.79% < 6.00%; excess_return_240d -38.33% < 8.00%; drawdown_120d -45.58% < -28.00%; volatility_120d 49.66% > 42.00% |
| 002321.SZ | 华英农业 | ok | 18.93 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.87% < 6.00%; excess_return_120d -25.45% < 6.00%; excess_return_240d -45.58% < 8.00%; drawdown_120d -30.00% < -28.00% |
| 301567.SZ | 贝隆精密 | ok | 18.93 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.70% < 6.00%; excess_return_120d -28.28% < 6.00%; excess_return_240d -36.78% < 8.00%; drawdown_120d -39.21% < -28.00%; volatility_120d 44.48% > 42.00% |
| 000930.SZ | 中粮科技 | ok | 18.93 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.01% < 6.00%; excess_return_120d -26.59% < 6.00%; excess_return_240d -44.31% < 8.00%; drawdown_120d -44.72% < -28.00% |
| 300079.SZ | 数码视讯 | ok | 18.93 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.91% < 6.00%; excess_return_120d -27.49% < 6.00%; excess_return_240d -52.10% < 8.00%; drawdown_120d -42.18% < -28.00% |
| 300609.SZ | 汇纳科技 | ok | 18.93 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.06% < 6.00%; excess_return_120d -23.64% < 6.00%; excess_return_240d -36.03% < 8.00%; drawdown_120d -35.99% < -28.00%; volatility_120d 48.17% > 42.00% |
| 600212.SH | 绿能慧充 | ok | 18.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.02% < 6.00%; excess_return_120d -40.61% < 6.00%; excess_return_240d -58.60% < 8.00%; drawdown_120d -40.19% < -28.00% |
| 301038.SZ | 深水规院 | ok | 18.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.44% < 6.00%; excess_return_120d -28.02% < 6.00%; excess_return_240d -10.10% < 8.00%; drawdown_120d -32.10% < -28.00% |
| 600307.SH | 酒钢宏兴 | ok | 18.92 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.15% < 6.00%; excess_return_120d -19.73% < 6.00%; excess_return_240d -27.76% < 8.00%; drawdown_120d -44.22% < -28.00%; volatility_120d 51.71% > 42.00% |
| 300247.SZ | 融捷健康 | ok | 18.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.29% < 6.00%; excess_return_120d -31.87% < 6.00%; excess_return_240d -26.19% < 8.00%; drawdown_120d -35.02% < -28.00%; volatility_120d 42.01% > 42.00% |
| 001225.SZ | 和泰机电 | ok | 18.92 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -26.01% < 6.00%; excess_return_120d -30.59% < 6.00%; excess_return_240d 0.82% < 8.00%; drawdown_120d -52.59% < -28.00%; volatility_120d 64.30% > 42.00% |
| 002987.SZ | 京北方 | ok | 18.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -45.35% < 6.00%; excess_return_120d -49.93% < 6.00%; excess_return_240d -74.43% < 8.00%; drawdown_120d -47.98% < -28.00% |
| 603613.SH | 国联股份 | ok | 18.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.75% < 6.00%; excess_return_120d -37.33% < 6.00%; excess_return_240d -40.33% < 8.00%; drawdown_120d -41.58% < -28.00% |
| 003015.SZ | 日久光电 | ok | 18.92 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.85% < 6.00%; excess_return_120d -28.43% < 6.00%; excess_return_240d -53.03% < 8.00%; drawdown_120d -33.63% < -28.00% |
| 301601.SZ | 惠通科技 | ok | 18.91 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -41.91% < 6.00%; excess_return_120d -46.49% < 6.00%; excess_return_240d -76.23% < 8.00%; drawdown_120d -47.62% < -28.00% |
| 003010.SZ | 若羽臣 | ok | 18.91 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.97% < 6.00%; excess_return_120d -33.55% < 6.00%; excess_return_240d -58.33% < 8.00%; drawdown_120d -39.36% < -28.00% |
| 002686.SZ | 亿利达 | ok | 18.91 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.22% < 6.00%; excess_return_120d -22.52% < 6.00%; excess_return_240d -39.62% < 8.00%; drawdown_120d -35.89% < -28.00%; volatility_120d 43.37% > 42.00% |
| 600808.SH | 马钢股份 | ok | 18.90 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.52% < 6.00%; excess_return_120d -45.10% < 6.00%; excess_return_240d -47.49% < 8.00%; drawdown_120d -44.71% < -28.00% |
| 000045.SZ | 深纺织A | ok | 18.90 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.16% < 6.00%; excess_return_120d -23.74% < 6.00%; excess_return_240d -33.02% < 8.00%; drawdown_120d -33.79% < -28.00% |
| 002679.SZ | 福建金森 | ok | 18.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.76% < 6.00%; excess_return_120d -34.34% < 6.00%; excess_return_240d -35.70% < 8.00%; drawdown_120d -42.92% < -28.00% |
| 600383.SH | 金地集团 | ok | 18.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.10% < 6.00%; excess_return_120d -32.68% < 6.00%; excess_return_240d -64.69% < 8.00%; drawdown_120d -39.73% < -28.00% |
| 002269.SZ | 美邦服饰 | ok | 18.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.57% < 6.00%; excess_return_120d -33.15% < 6.00%; excess_return_240d -50.04% < 8.00%; drawdown_120d -34.78% < -28.00% |
| 002813.SZ | 路畅科技 | ok | 18.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.41% < 6.00%; excess_return_120d -37.99% < 6.00%; excess_return_240d -37.85% < 8.00%; drawdown_120d -42.07% < -28.00% |
| 002852.SZ | 道道全 | ok | 18.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.52% < 6.00%; excess_return_120d -32.10% < 6.00%; excess_return_240d -45.22% < 8.00%; drawdown_120d -37.37% < -28.00% |
| 002953.SZ | 日丰股份 | ok | 18.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.10% < 6.00%; excess_return_120d -25.68% < 6.00%; excess_return_240d -36.39% < 8.00%; drawdown_120d -37.38% < -28.00% |
| 600279.SH | 重庆港 | ok | 18.89 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.11% < 6.00%; excess_return_120d -31.69% < 6.00%; excess_return_240d -49.90% < 8.00%; drawdown_120d -33.67% < -28.00% |
| 603168.SH | 莎普爱思 | ok | 18.88 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.66% < 6.00%; excess_return_120d -36.24% < 6.00%; excess_return_240d -56.28% < 8.00%; drawdown_120d -35.92% < -28.00% |
| 002104.SZ | 恒宝股份 | ok | 18.88 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -53.08% < 6.00%; excess_return_120d -57.66% < 6.00%; excess_return_240d -73.42% < 8.00%; drawdown_120d -51.94% < -28.00% |
| 000913.SZ | 钱江摩托 | ok | 18.88 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.15% < 6.00%; excess_return_120d -33.73% < 6.00%; excess_return_240d -51.05% < 8.00%; drawdown_120d -34.66% < -28.00% |
| 603599.SH | 广信股份 | ok | 18.88 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.46% < 6.00%; excess_return_120d -17.04% < 6.00%; excess_return_240d -28.64% < 8.00%; drawdown_120d -39.64% < -28.00%; volatility_120d 46.18% > 42.00% |
| 603059.SH | 倍加洁 | ok | 18.88 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.96% < 6.00%; excess_return_120d -18.54% < 6.00%; excess_return_240d -21.06% < 8.00%; drawdown_120d -40.41% < -28.00%; volatility_120d 47.07% > 42.00% |
| 601118.SH | 海南橡胶 | ok | 18.88 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.70% < 6.00%; excess_return_120d -19.28% < 6.00%; excess_return_240d -17.33% < 8.00%; drawdown_120d -41.50% < -28.00%; volatility_120d 54.79% > 42.00% |
| 301539.SZ | 宏鑫科技 | ok | 18.88 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.82% < 6.00%; excess_return_120d -36.40% < 6.00%; excess_return_240d -46.80% < 8.00%; drawdown_120d -39.10% < -28.00% |
| 605188.SH | 国光连锁 | ok | 18.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.55% < 6.00%; excess_return_120d -42.13% < 6.00%; excess_return_240d -10.54% < 8.00%; drawdown_120d -48.67% < -28.00% |
| 600533.SH | 栖霞建设 | ok | 18.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.44% < 6.00%; excess_return_120d -28.02% < 6.00%; excess_return_240d -47.13% < 8.00%; drawdown_120d -30.74% < -28.00% |
| 002526.SZ | 山东矿机 | ok | 18.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.67% < 6.00%; excess_return_120d -31.25% < 6.00%; excess_return_240d -52.88% < 8.00%; drawdown_120d -35.61% < -28.00% |
| 603383.SH | 顶点软件 | ok | 18.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.26% < 6.00%; excess_return_120d -27.84% < 6.00%; excess_return_240d -54.99% < 8.00%; drawdown_120d -34.96% < -28.00% |
| 000099.SZ | 中信海直 | ok | 18.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.40% < 6.00%; excess_return_120d -33.99% < 6.00%; excess_return_240d -52.61% < 8.00%; drawdown_120d -36.81% < -28.00% |
| 605162.SH | 新中港 | ok | 18.87 | close_below_ma200; stock_return_120d -7.40% < 6.00%; excess_return_120d -11.98% < 6.00%; excess_return_240d -44.79% < 8.00%; drawdown_120d -49.35% < -28.00%; volatility_120d 65.00% > 42.00% |
| 688591.SH | 泰凌微 | ok | 18.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.54% < 6.00%; excess_return_120d -25.12% < 6.00%; excess_return_240d -55.77% < 8.00%; drawdown_120d -34.24% < -28.00%; volatility_120d 48.00% > 42.00% |
| 301590.SZ | 优优绿能 | ok | 18.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.32% < 6.00%; excess_return_120d -20.90% < 6.00%; excess_return_240d -25.49% < 8.00%; drawdown_120d -37.92% < -28.00%; volatility_120d 62.78% > 42.00% |
| 300642.SZ | 透景生命 | ok | 18.87 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.08% < 6.00%; excess_return_120d -34.66% < 6.00%; excess_return_240d -35.21% < 8.00%; drawdown_120d -43.83% < -28.00% |
| 300272.SZ | 开能健康 | ok | 18.87 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.44% < 6.00%; excess_return_120d -30.02% < 6.00%; excess_return_240d -37.28% < 8.00%; drawdown_120d -38.24% < -28.00% |
| 300695.SZ | 兆丰股份 | ok | 18.86 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.01% < 6.00%; excess_return_120d -38.59% < 6.00%; excess_return_240d -43.14% < 8.00%; drawdown_120d -35.77% < -28.00%; volatility_120d 58.20% > 42.00% |
| 603220.SH | 中贝通信 | ok | 18.86 | close_below_ma200; stock_return_120d -6.48% < 6.00%; excess_return_120d -11.06% < 6.00%; excess_return_240d -28.14% < 8.00%; drawdown_120d -42.41% < -28.00%; volatility_120d 65.51% > 42.00% |
| 000932.SZ | 华菱钢铁 | ok | 18.86 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.62% < 6.00%; excess_return_120d -39.20% < 6.00%; excess_return_240d -50.40% < 8.00%; drawdown_120d -46.72% < -28.00% |
| 000558.SZ | 天府文旅 | ok | 18.86 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.92% < 6.00%; excess_return_120d -40.50% < 6.00%; excess_return_240d -51.62% < 8.00%; drawdown_120d -41.18% < -28.00% |
| 300500.SZ | 启迪设计 | ok | 18.86 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.44% < 6.00%; excess_return_120d -39.02% < 6.00%; excess_return_240d -49.99% < 8.00%; drawdown_120d -31.47% < -28.00% |
| 600115.SH | 中国东航 | ok | 18.85 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.83% < 6.00%; excess_return_120d -40.41% < 6.00%; excess_return_240d -20.57% < 8.00%; drawdown_120d -40.59% < -28.00%; volatility_120d 46.83% > 42.00% |
| 002840.SZ | 华统股份 | ok | 18.85 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -14.35% < 6.00%; excess_return_120d -18.93% < 6.00%; excess_return_240d -42.17% < 8.00%; drawdown_120d -41.68% < -28.00%; volatility_120d 47.95% > 42.00% |
| 605003.SH | 众望布艺 | ok | 18.85 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -38.66% < 6.00%; excess_return_120d -43.24% < 6.00%; excess_return_240d -17.58% < 8.00%; drawdown_120d -42.14% < -28.00%; volatility_120d 49.33% > 42.00% |
| 301380.SZ | 挖金客 | ok | 18.84 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.70% < 6.00%; excess_return_120d -31.28% < 6.00%; excess_return_240d -46.43% < 8.00%; drawdown_120d -39.44% < -28.00%; volatility_120d 47.37% > 42.00% |
| 600635.SH | 大众公用 | ok | 18.84 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.87% < 6.00%; excess_return_120d -37.45% < 6.00%; excess_return_240d -12.54% < 8.00%; drawdown_120d -40.51% < -28.00% |
| 000993.SZ | 闽东电力 | ok | 18.84 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.78% < 6.00%; excess_return_120d -21.36% < 6.00%; excess_return_240d -27.57% < 8.00%; drawdown_120d -42.27% < -28.00%; volatility_120d 56.90% > 42.00% |
| 603392.SH | 万泰生物 | ok | 18.83 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.00% < 6.00%; excess_return_120d -40.58% < 6.00%; excess_return_240d -73.11% < 8.00%; drawdown_120d -41.03% < -28.00% |
| 002115.SZ | 三维通信 | ok | 18.83 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.57% < 6.00%; excess_return_120d -25.15% < 6.00%; excess_return_240d -5.44% < 8.00%; drawdown_120d -51.81% < -28.00%; volatility_120d 65.41% > 42.00% |
| 300882.SZ | 万胜智能 | ok | 18.83 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.98% < 6.00%; excess_return_120d -18.56% < 6.00%; excess_return_240d -25.35% < 8.00%; drawdown_120d -41.71% < -28.00%; volatility_120d 53.85% > 42.00% |
| 000736.SZ | 中交地产 | ok | 18.83 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.56% < 6.00%; excess_return_120d -26.66% < 6.00%; excess_return_240d -35.56% < 8.00%; drawdown_120d -31.67% < -28.00% |
| 000523.SZ | 红棉股份 | ok | 18.83 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -29.71% < 6.00%; excess_return_120d -34.29% < 6.00%; excess_return_240d -40.79% < 8.00%; drawdown_120d -39.91% < -28.00% |
| 688212.SH | 澳华内镜 | ok | 18.82 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.41% < 6.00%; excess_return_120d -38.99% < 6.00%; excess_return_240d -58.91% < 8.00%; drawdown_120d -41.67% < -28.00% |
| 688132.SH | 邦彦技术 | ok | 18.82 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.36% < 6.00%; excess_return_120d -31.94% < 6.00%; excess_return_240d -50.53% < 8.00%; drawdown_120d -37.48% < -28.00% |
| 300608.SZ | 思特奇 | ok | 18.81 | close_below_ma200; stock_return_120d -11.47% < 6.00%; excess_return_120d -16.05% < 6.00%; excess_return_240d -39.02% < 8.00%; drawdown_120d -49.90% < -28.00%; volatility_120d 69.23% > 42.00% |
| 000526.SZ | 学大教育 | ok | 18.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.66% < 6.00%; excess_return_120d -33.24% < 6.00%; excess_return_240d -61.57% < 8.00%; drawdown_120d -34.92% < -28.00% |
| 002410.SZ | 广联达 | ok | 18.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.89% < 6.00%; excess_return_120d -37.47% < 6.00%; excess_return_240d -57.39% < 8.00%; drawdown_120d -48.61% < -28.00% |
| 300025.SZ | 华星创业 | ok | 18.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.26% < 6.00%; excess_return_120d -31.84% < 6.00%; excess_return_240d -60.02% < 8.00%; drawdown_120d -34.53% < -28.00% |
| 002238.SZ | 天威视讯 | ok | 18.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.47% < 6.00%; excess_return_120d -37.05% < 6.00%; excess_return_240d -57.99% < 8.00%; drawdown_120d -44.60% < -28.00% |
| 301006.SZ | 迈拓股份 | ok | 18.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.74% < 6.00%; excess_return_120d -25.32% < 6.00%; excess_return_240d -37.49% < 8.00%; drawdown_120d -32.49% < -28.00% |
| 000554.SZ | 泰山石油 | ok | 18.81 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.57% < 6.00%; excess_return_120d -14.15% < 6.00%; excess_return_240d -35.02% < 8.00%; drawdown_120d -50.92% < -28.00%; volatility_120d 52.09% > 42.00% |
| 600640.SH | 国脉文化 | ok | 18.81 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.11% < 6.00%; excess_return_120d -23.69% < 6.00%; excess_return_240d -37.48% < 8.00%; drawdown_120d -38.42% < -28.00% |
| 300978.SZ | 东箭科技 | ok | 18.80 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.43% < 6.00%; excess_return_120d -35.01% < 6.00%; excess_return_240d -43.01% < 8.00%; drawdown_120d -34.42% < -28.00% |
| 301126.SZ | 达嘉维康 | ok | 18.80 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.47% < 6.00%; excess_return_120d -30.05% < 6.00%; excess_return_240d -40.45% < 8.00%; drawdown_120d -36.74% < -28.00% |
| 603095.SH | 越剑智能 | ok | 18.80 | close_below_ma200; stock_return_120d -21.36% < 6.00%; excess_return_120d -25.94% < 6.00%; excess_return_240d -29.58% < 8.00%; drawdown_120d -49.48% < -28.00%; volatility_120d 57.67% > 42.00% |
| 000505.SZ | 京粮控股 | ok | 18.80 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.49% < 6.00%; excess_return_120d -42.07% < 6.00%; excess_return_240d -39.38% < 8.00%; drawdown_120d -36.97% < -28.00% |
| 601992.SH | 金隅集团 | ok | 18.80 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.77% < 6.00%; excess_return_120d -21.35% < 6.00%; excess_return_240d -31.99% < 8.00%; drawdown_120d -41.60% < -28.00%; volatility_120d 49.60% > 42.00% |
| 600273.SH | 嘉化能源 | ok | 18.79 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.23% < 6.00%; excess_return_120d -23.81% < 6.00%; excess_return_240d -40.19% < 8.00%; drawdown_120d -42.85% < -28.00%; volatility_120d 43.11% > 42.00% |
| 300543.SZ | 朗科智能 | ok | 18.79 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.08% < 6.00%; excess_return_120d -38.66% < 6.00%; excess_return_240d -54.94% < 8.00%; drawdown_120d -39.18% < -28.00% |
| 000530.SZ | 冰山冷热 | ok | 18.79 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.23% < 6.00%; excess_return_120d -33.82% < 6.00%; excess_return_240d -49.15% < 8.00%; drawdown_120d -32.64% < -28.00%; volatility_120d 44.49% > 42.00% |
| 600702.SH | 舍得酒业 | ok | 18.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.01% < 6.00%; excess_return_120d -40.59% < 6.00%; excess_return_240d -51.38% < 8.00%; drawdown_120d -41.26% < -28.00% |
| 301129.SZ | 瑞纳智能 | ok | 18.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -12.49% < 6.00%; excess_return_120d -17.07% < 6.00%; excess_return_240d -39.84% < 8.00%; drawdown_120d -36.94% < -28.00%; volatility_120d 52.33% > 42.00% |
| 603879.SH | 永悦科技 | ok | 18.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.17% < 6.00%; excess_return_120d -39.75% < 6.00%; excess_return_240d -53.60% < 8.00%; drawdown_120d -39.29% < -28.00% |
| 000701.SZ | 厦门信达 | ok | 18.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.05% < 6.00%; excess_return_120d -35.63% < 6.00%; excess_return_240d -48.62% < 8.00%; drawdown_120d -36.73% < -28.00% |
| 603106.SH | 恒银科技 | ok | 18.78 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.18% < 6.00%; excess_return_120d -37.76% < 6.00%; excess_return_240d -53.06% < 8.00%; drawdown_120d -41.65% < -28.00% |
| 603215.SH | 比依股份 | ok | 18.77 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.81% < 6.00%; excess_return_120d -36.39% < 6.00%; excess_return_240d -39.32% < 8.00%; drawdown_120d -34.85% < -28.00% |
| 688060.SH | 云涌科技 | ok | 18.77 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.81% < 6.00%; excess_return_120d -25.39% < 6.00%; excess_return_240d -29.34% < 8.00%; drawdown_120d -35.25% < -28.00% |
| 601865.SH | 福莱特 | ok | 18.77 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.76% < 6.00%; excess_return_120d -40.34% < 6.00%; excess_return_240d -63.53% < 8.00%; drawdown_120d -45.07% < -28.00% |
| 002537.SZ | 海联金汇 | ok | 18.77 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.62% < 6.00%; excess_return_120d -44.20% < 6.00%; excess_return_240d -72.30% < 8.00%; drawdown_120d -43.95% < -28.00% |
| 300981.SZ | 中红医疗 | ok | 18.77 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.50% < 6.00%; excess_return_120d -19.08% < 6.00%; excess_return_240d -33.59% < 8.00%; drawdown_120d -41.74% < -28.00%; volatility_120d 55.25% > 42.00% |
| 600825.SH | 新华传媒 | ok | 18.77 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.73% < 6.00%; excess_return_120d -24.31% < 6.00%; excess_return_240d -51.05% < 8.00%; drawdown_120d -34.93% < -28.00%; volatility_120d 46.72% > 42.00% |
| 000802.SZ | 北京文化 | ok | 18.76 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -20.66% < 6.00%; excess_return_120d -25.24% < 6.00%; excess_return_240d -47.42% < 8.00%; drawdown_120d -34.36% < -28.00%; volatility_120d 47.84% > 42.00% |
| 301221.SZ | 光庭信息 | ok | 18.76 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -26.60% < 6.00%; excess_return_120d -31.18% < 6.00%; excess_return_240d -40.01% < 8.00%; drawdown_120d -36.14% < -28.00% |
| 002909.SZ | 集泰股份 | ok | 18.76 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.17% < 6.00%; excess_return_120d -31.75% < 6.00%; excess_return_240d -42.24% < 8.00%; drawdown_120d -35.92% < -28.00% |
| 301255.SZ | 通力科技 | ok | 18.75 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.43% < 6.00%; excess_return_120d -27.01% < 6.00%; excess_return_240d -47.07% < 8.00%; drawdown_120d -35.13% < -28.00%; volatility_120d 52.38% > 42.00% |
| 002284.SZ | 亚太股份 | ok | 18.75 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -31.76% < 6.00%; excess_return_120d -36.34% < 6.00%; excess_return_240d -28.76% < 8.00%; drawdown_120d -45.47% < -28.00% |
| 002334.SZ | 英威腾 | ok | 18.75 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.21% < 6.00%; excess_return_120d -25.79% < 6.00%; excess_return_240d -32.51% < 8.00%; drawdown_120d -31.98% < -28.00%; volatility_120d 47.11% > 42.00% |
| 002825.SZ | 纳尔股份 | ok | 18.75 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.57% < 6.00%; excess_return_120d -31.15% < 6.00%; excess_return_240d -44.15% < 8.00%; drawdown_120d -29.06% < -28.00% |
| 300384.SZ | 三联虹普 | ok | 18.75 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.97% < 6.00%; excess_return_120d -30.55% < 6.00%; excess_return_240d -52.08% < 8.00%; drawdown_120d -38.93% < -28.00% |
| 002707.SZ | 众信旅游 | ok | 18.75 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.27% < 6.00%; excess_return_120d -36.85% < 6.00%; excess_return_240d -58.90% < 8.00%; drawdown_120d -46.42% < -28.00% |
| 000400.SZ | 许继电气 | ok | 18.74 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.18% < 6.00%; excess_return_120d -21.76% < 6.00%; excess_return_240d -23.23% < 8.00%; drawdown_120d -38.69% < -28.00% |
| 603816.SH | 顾家家居 | ok | 18.74 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -24.86% < 6.00%; excess_return_120d -29.44% < 6.00%; excess_return_240d -25.68% < 8.00%; drawdown_120d -39.08% < -28.00% |
| 600299.SH | 安迪苏 | ok | 18.74 | close_below_ma200; stock_return_120d -5.48% < 6.00%; excess_return_120d -10.06% < 6.00%; excess_return_240d -33.73% < 8.00%; drawdown_120d -48.85% < -28.00%; volatility_120d 53.10% > 42.00% |
| 688597.SH | 煜邦电力 | ok | 18.74 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.10% < 6.00%; excess_return_120d -19.68% < 6.00%; excess_return_240d -35.05% < 8.00%; drawdown_120d -34.86% < -28.00%; volatility_120d 52.41% > 42.00% |
| 000801.SZ | 四川九洲 | ok | 18.74 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.10% < 6.00%; excess_return_120d -33.68% < 6.00%; excess_return_240d -42.19% < 8.00%; drawdown_120d -35.19% < -28.00%; volatility_120d 43.19% > 42.00% |
| 603486.SH | 科沃斯 | ok | 18.74 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.43% < 6.00%; excess_return_120d -39.01% < 6.00%; excess_return_240d -26.83% < 8.00%; drawdown_120d -38.84% < -28.00% |
| 688357.SH | 建龙微纳 | ok | 18.74 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.17% < 6.00%; excess_return_120d -22.75% < 6.00%; excess_return_240d -23.29% < 8.00%; drawdown_120d -31.07% < -28.00% |
| 605577.SH | 龙版传媒 | ok | 18.74 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.04% < 6.00%; excess_return_120d -32.62% < 6.00%; excess_return_240d -47.72% < 8.00%; drawdown_120d -37.27% < -28.00% |
| 601717.SH | 中创智领 | ok | 18.74 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.41% < 6.00%; excess_return_120d -39.99% < 6.00%; excess_return_240d -16.51% < 8.00%; drawdown_120d -39.53% < -28.00% |
| 002590.SZ | 万安科技 | ok | 18.72 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.81% < 6.00%; excess_return_120d -36.39% < 6.00%; excess_return_240d -49.75% < 8.00%; drawdown_120d -37.47% < -28.00% |
| 600765.SH | 中航重机 | ok | 18.72 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -30.76% < 6.00%; excess_return_120d -35.34% < 6.00%; excess_return_240d -40.50% < 8.00%; drawdown_120d -39.81% < -28.00% |
| 300413.SZ | 芒果超媒 | ok | 18.72 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.04% < 6.00%; excess_return_120d -42.62% < 6.00%; excess_return_240d -49.86% < 8.00%; drawdown_120d -49.53% < -28.00% |
| 002184.SZ | 海得控制 | ok | 18.71 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.52% < 6.00%; excess_return_120d -30.10% < 6.00%; excess_return_240d -45.69% < 8.00%; drawdown_120d -32.06% < -28.00% |
| 301102.SZ | 兆讯传媒 | ok | 18.71 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.63% < 6.00%; excess_return_120d -20.21% < 6.00%; excess_return_240d -41.15% < 8.00%; drawdown_120d -39.26% < -28.00%; volatility_120d 43.81% > 42.00% |
| 002416.SZ | 爱施德 | ok | 18.71 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.00% < 6.00%; excess_return_120d -29.58% < 6.00%; excess_return_240d -44.83% < 8.00%; drawdown_120d -35.29% < -28.00% |
| 300552.SZ | 万集科技 | ok | 18.71 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.99% < 6.00%; excess_return_120d -30.57% < 6.00%; excess_return_240d -38.21% < 8.00%; drawdown_120d -45.86% < -28.00%; volatility_120d 54.85% > 42.00% |
| 601012.SH | 隆基绿能 | ok | 18.70 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.14% < 6.00%; excess_return_120d -36.72% < 6.00%; excess_return_240d -46.11% < 8.00%; drawdown_120d -38.40% < -28.00% |
| 600638.SH | 新黄浦 | ok | 18.70 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -29.37% < 6.00%; excess_return_120d -33.95% < 6.00%; excess_return_240d -43.94% < 8.00%; drawdown_120d -40.03% < -28.00% |
| 002506.SZ | 协鑫集成 | ok | 18.69 | close_below_ma200; ma60_not_above_ma120; stock_return_120d 0.00% < 6.00%; excess_return_120d -4.58% < 6.00%; excess_return_240d -15.04% < 8.00%; drawdown_120d -55.97% < -28.00%; volatility_120d 72.94% > 42.00% |
| 002649.SZ | 博彦科技 | ok | 18.69 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.21% < 6.00%; excess_return_120d -41.79% < 6.00%; excess_return_240d -66.32% < 8.00%; drawdown_120d -48.81% < -28.00% |
| 001979.SZ | 招商蛇口 | ok | 18.69 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.22% < 6.00%; excess_return_120d -26.80% < 6.00%; excess_return_240d -44.53% < 8.00%; drawdown_120d -39.46% < -28.00% |
| 603160.SH | 汇顶科技 | ok | 18.69 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.30% < 6.00%; excess_return_120d -31.88% < 6.00%; excess_return_240d -39.54% < 8.00%; drawdown_120d -33.43% < -28.00% |
| 601933.SH | 永辉超市 | ok | 18.68 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.90% < 6.00%; excess_return_120d -38.48% < 6.00%; excess_return_240d -57.05% < 8.00%; drawdown_120d -47.01% < -28.00% |
| 301061.SZ | 匠心家居 | ok | 18.68 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -51.28% < 6.00%; excess_return_120d -55.86% < 6.00%; excess_return_240d -68.77% < 8.00%; drawdown_120d -52.53% < -28.00% |
| 300549.SZ | 优德精密 | ok | 18.68 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.18% < 6.00%; excess_return_120d -27.76% < 6.00%; excess_return_240d -42.14% < 8.00%; drawdown_120d -28.64% < -28.00%; volatility_120d 42.46% > 42.00% |
| 601003.SH | 柳钢股份 | ok | 18.68 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.86% < 6.00%; excess_return_120d -34.86% < 6.00%; excess_return_240d -19.46% < 8.00%; drawdown_120d -38.60% < -28.00% |
| 002703.SZ | 浙江世宝 | ok | 18.68 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -31.80% < 6.00%; excess_return_120d -36.38% < 6.00%; excess_return_240d -9.59% < 8.00%; drawdown_120d -51.13% < -28.00%; volatility_120d 61.79% > 42.00% |
| 002696.SZ | 百洋股份 | ok | 18.68 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.93% < 6.00%; excess_return_120d -28.51% < 6.00%; excess_return_240d -35.11% < 8.00%; drawdown_120d -32.32% < -28.00%; volatility_120d 42.45% > 42.00% |
| 600725.SH | 云维股份 | ok | 18.68 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.97% < 6.00%; excess_return_120d -27.55% < 6.00%; excess_return_240d -22.63% < 8.00%; drawdown_120d -41.98% < -28.00%; volatility_120d 44.80% > 42.00% |
| 601579.SH | 会稽山 | ok | 18.68 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.08% < 6.00%; excess_return_120d -30.66% < 6.00%; excess_return_240d -45.04% < 8.00%; drawdown_120d -35.13% < -28.00% |
| 002642.SZ | 荣联科技 | ok | 18.68 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.03% < 6.00%; excess_return_120d -29.61% < 6.00%; excess_return_240d -41.10% < 8.00%; drawdown_120d -35.35% < -28.00% |
| 003019.SZ | 宸展光电 | ok | 18.67 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -18.95% < 6.00%; excess_return_120d -23.53% < 6.00%; excess_return_240d -37.38% < 8.00%; drawdown_120d -43.12% < -28.00%; volatility_120d 53.85% > 42.00% |
| 002743.SZ | 富煌钢构 | ok | 18.67 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.18% < 6.00%; excess_return_120d -29.76% < 6.00%; excess_return_240d -53.94% < 8.00%; drawdown_120d -38.43% < -28.00% |
| 300787.SZ | 海能实业 | ok | 18.67 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.90% < 6.00%; excess_return_120d -26.48% < 6.00%; excess_return_240d -52.87% < 8.00%; drawdown_120d -31.87% < -28.00% |
| 301110.SZ | 青木科技 | ok | 18.66 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.57% < 6.00%; excess_return_120d -23.15% < 6.00%; excess_return_240d -20.41% < 8.00%; drawdown_120d -49.23% < -28.00%; volatility_120d 64.44% > 42.00% |
| 002373.SZ | 千方科技 | ok | 18.66 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.49% < 6.00%; excess_return_120d -44.07% < 6.00%; excess_return_240d -44.68% < 8.00%; drawdown_120d -48.58% < -28.00% |
| 002085.SZ | 万丰奥威 | ok | 18.66 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.14% < 6.00%; excess_return_120d -33.72% < 6.00%; excess_return_240d -49.47% < 8.00%; drawdown_120d -37.58% < -28.00% |
| 300846.SZ | 首都在线 | ok | 18.66 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.92% < 6.00%; excess_return_120d -17.50% < 6.00%; excess_return_240d -18.20% < 8.00%; drawdown_120d -49.06% < -28.00%; volatility_120d 81.07% > 42.00% |
| 688013.SH | 天臣医疗 | ok | 18.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -44.96% < 6.00%; excess_return_120d -49.54% < 6.00%; excess_return_240d -35.00% < 8.00%; drawdown_120d -50.31% < -28.00% |
| 301036.SZ | 双乐股份 | ok | 18.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.57% < 6.00%; excess_return_120d -39.15% < 6.00%; excess_return_240d -60.57% < 8.00%; drawdown_120d -41.12% < -28.00% |
| 603955.SH | 大千生态 | ok | 18.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.54% < 6.00%; excess_return_120d -37.12% < 6.00%; excess_return_240d -60.17% < 8.00%; drawdown_120d -39.64% < -28.00% |
| 300746.SZ | 汉嘉数智 | ok | 18.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.15% < 6.00%; excess_return_120d -22.73% < 6.00%; excess_return_240d -54.75% < 8.00%; drawdown_120d -32.57% < -28.00%; volatility_120d 44.02% > 42.00% |
| 301320.SZ | 豪江智能 | ok | 18.65 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.00% < 6.00%; excess_return_120d -29.58% < 6.00%; excess_return_240d -55.59% < 8.00%; drawdown_120d -33.07% < -28.00% |
| 300808.SZ | 久量股份 | ok | 18.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.01% < 6.00%; excess_return_120d -30.59% < 6.00%; excess_return_240d -44.16% < 8.00%; drawdown_120d -37.22% < -28.00%; volatility_120d 48.33% > 42.00% |
| 600231.SH | 凌钢股份 | ok | 18.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.23% < 6.00%; excess_return_120d -29.81% < 6.00%; excess_return_240d -40.69% < 8.00%; drawdown_120d -38.93% < -28.00% |
| 000564.SZ | 供销大集 | ok | 18.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -45.60% < 6.00%; excess_return_120d -50.18% < 6.00%; excess_return_240d -61.71% < 8.00%; drawdown_120d -47.49% < -28.00% |
| 603325.SH | 博隆技术 | ok | 18.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.23% < 6.00%; excess_return_120d -33.81% < 6.00%; excess_return_240d -46.49% < 8.00%; drawdown_120d -40.03% < -28.00% |
| 301327.SZ | 华宝新能 | ok | 18.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.20% < 6.00%; excess_return_120d -20.78% < 6.00%; excess_return_240d -30.73% < 8.00%; drawdown_120d -41.72% < -28.00%; volatility_120d 43.05% > 42.00% |
| 002490.SZ | 山东墨龙 | ok | 18.64 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -1.54% < 6.00%; excess_return_120d -6.12% < 6.00%; excess_return_240d -11.32% < 8.00%; drawdown_120d -55.92% < -28.00%; volatility_120d 76.01% > 42.00% |
| 603533.SH | 掌阅科技 | ok | 18.64 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.09% < 6.00%; excess_return_120d -21.67% < 6.00%; excess_return_240d -35.44% < 8.00%; drawdown_120d -51.25% < -28.00%; volatility_120d 66.60% > 42.00% |
| 300942.SZ | 易瑞生物 | ok | 18.64 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.98% < 6.00%; excess_return_120d -37.56% < 6.00%; excess_return_240d -56.62% < 8.00%; drawdown_120d -43.05% < -28.00% |
| 601808.SH | 中海油服 | ok | 18.63 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.43% < 6.00%; excess_return_120d -22.01% < 6.00%; excess_return_240d -36.37% < 8.00%; drawdown_120d -47.33% < -28.00%; volatility_120d 42.45% > 42.00% |
| 300621.SZ | 维业股份 | ok | 18.63 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.28% < 6.00%; excess_return_120d -25.86% < 6.00%; excess_return_240d -48.27% < 8.00%; drawdown_120d -30.39% < -28.00% |
| 300375.SZ | 鹏翎股份 | ok | 18.63 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.19% < 6.00%; excess_return_120d -27.77% < 6.00%; excess_return_240d -39.55% < 8.00%; drawdown_120d -35.36% < -28.00%; volatility_120d 43.72% > 42.00% |
| 600415.SH | 小商品城 | ok | 18.63 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.26% < 6.00%; excess_return_120d -35.84% < 6.00%; excess_return_240d -63.47% < 8.00%; drawdown_120d -42.63% < -28.00% |
| 002316.SZ | 亚联发展 | ok | 18.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -11.84% < 6.00%; excess_return_120d -16.42% < 6.00%; excess_return_240d -43.43% < 8.00%; drawdown_120d -33.60% < -28.00%; volatility_120d 50.92% > 42.00% |
| 300451.SZ | 创业慧康 | ok | 18.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.06% < 6.00%; excess_return_120d -37.64% < 6.00%; excess_return_240d -66.26% < 8.00%; drawdown_120d -53.65% < -28.00% |
| 002659.SZ | 凯文教育 | ok | 18.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.76% < 6.00%; excess_return_120d -37.34% < 6.00%; excess_return_240d -44.14% < 8.00%; drawdown_120d -46.83% < -28.00% |
| 300893.SZ | 松原安全 | ok | 18.62 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.13% < 6.00%; excess_return_120d -31.71% < 6.00%; excess_return_240d -20.90% < 8.00%; drawdown_120d -34.69% < -28.00% |
| 600257.SH | 大湖股份 | ok | 18.62 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.39% < 6.00%; excess_return_120d -31.97% < 6.00%; excess_return_240d -33.57% < 8.00%; drawdown_120d -43.00% < -28.00% |
| 601798.SH | 蓝科高新 | ok | 18.61 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.17% < 6.00%; excess_return_120d -23.75% < 6.00%; excess_return_240d -30.22% < 8.00%; drawdown_120d -30.72% < -28.00% |
| 000503.SZ | 国新健康 | ok | 18.61 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.17% < 6.00%; excess_return_120d -33.75% < 6.00%; excess_return_240d -60.85% < 8.00%; drawdown_120d -49.84% < -28.00% |
| 601068.SH | 中铝国际 | ok | 18.61 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.20% < 6.00%; excess_return_120d -21.78% < 6.00%; excess_return_240d -25.67% < 8.00%; drawdown_120d -38.40% < -28.00%; volatility_120d 46.91% > 42.00% |
| 301522.SZ | 上大股份 | ok | 18.61 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -32.07% < 6.00%; excess_return_120d -36.65% < 6.00%; excess_return_240d -46.17% < 8.00%; drawdown_120d -47.67% < -28.00%; volatility_120d 48.12% > 42.00% |
| 300271.SZ | 华宇软件 | ok | 18.61 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.64% < 6.00%; excess_return_120d -37.22% < 6.00%; excess_return_240d -60.35% < 8.00%; drawdown_120d -45.42% < -28.00% |
| 301091.SZ | 深城交 | ok | 18.61 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.91% < 6.00%; excess_return_120d -44.49% < 6.00%; excess_return_240d -64.68% < 8.00%; drawdown_120d -46.94% < -28.00% |
| 600778.SH | 友好集团 | ok | 18.61 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.79% < 6.00%; excess_return_120d -27.37% < 6.00%; excess_return_240d -41.74% < 8.00%; drawdown_120d -40.94% < -28.00% |
| 002343.SZ | 慈文传媒 | ok | 18.60 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.17% < 6.00%; excess_return_120d -40.75% < 6.00%; excess_return_240d -64.54% < 8.00%; drawdown_120d -47.71% < -28.00% |
| 001382.SZ | 新亚电缆 | ok | 18.60 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.66% < 6.00%; excess_return_120d -26.24% < 6.00%; excess_return_240d -46.28% < 8.00%; drawdown_120d -38.90% < -28.00% |
| 002846.SZ | 英联股份 | ok | 18.60 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.60% < 6.00%; excess_return_120d -39.18% < 6.00%; excess_return_240d -56.53% < 8.00%; drawdown_120d -43.59% < -28.00% |
| 002296.SZ | 辉煌科技 | ok | 18.60 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.51% < 6.00%; excess_return_120d -24.09% < 6.00%; excess_return_240d -41.47% < 8.00%; drawdown_120d -40.76% < -28.00%; volatility_120d 42.88% > 42.00% |
| 002146.SZ | 荣盛发展 | ok | 18.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.10% < 6.00%; excess_return_120d -35.68% < 6.00%; excess_return_240d -42.08% < 8.00%; drawdown_120d -42.64% < -28.00% |
| 002724.SZ | 海洋王 | ok | 18.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.15% < 6.00%; excess_return_120d -29.73% < 6.00%; excess_return_240d -55.99% < 8.00%; drawdown_120d -40.12% < -28.00% |
| 002187.SZ | 广百股份 | ok | 18.59 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.54% < 6.00%; excess_return_120d -40.12% < 6.00%; excess_return_240d -46.48% < 8.00%; drawdown_120d -49.11% < -28.00% |
| 002357.SZ | 富临运业 | ok | 18.58 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -8.44% < 6.00%; excess_return_120d -12.93% < 6.00%; excess_return_240d -28.76% < 8.00%; drawdown_120d -45.59% < -28.00%; volatility_120d 54.62% > 42.00% |
| 000955.SZ | 欣龙控股 | ok | 18.58 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.06% < 6.00%; excess_return_120d -34.64% < 6.00%; excess_return_240d -31.59% < 8.00%; drawdown_120d -30.40% < -28.00%; volatility_120d 45.35% > 42.00% |
| 603786.SH | 科博达 | ok | 18.58 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -43.07% < 6.00%; excess_return_120d -47.65% < 6.00%; excess_return_240d -40.72% < 8.00%; drawdown_120d -48.03% < -28.00% |
| 300188.SZ | 国投智能 | ok | 18.58 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.29% < 6.00%; excess_return_120d -38.87% < 6.00%; excess_return_240d -51.28% < 8.00%; drawdown_120d -46.01% < -28.00% |
| 688365.SH | 光云科技 | ok | 18.58 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.03% < 6.00%; excess_return_120d -16.61% < 6.00%; excess_return_240d -20.14% < 8.00%; drawdown_120d -56.61% < -28.00%; volatility_120d 88.10% > 42.00% |
| 300168.SZ | 万达信息 | ok | 18.58 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.02% < 6.00%; excess_return_120d -32.60% < 6.00%; excess_return_240d -59.18% < 8.00%; drawdown_120d -43.91% < -28.00% |
| 301025.SZ | 读客文化 | ok | 18.58 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.04% < 6.00%; excess_return_120d -20.62% < 6.00%; excess_return_240d -47.77% < 8.00%; drawdown_120d -50.56% < -28.00%; volatility_120d 57.81% > 42.00% |
| 688169.SH | 石头科技 | ok | 18.57 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.89% < 6.00%; excess_return_120d -40.47% < 6.00%; excess_return_240d -57.77% < 8.00%; drawdown_120d -40.99% < -28.00% |
| 002244.SZ | 滨江集团 | ok | 18.57 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.15% < 6.00%; excess_return_120d -22.73% < 6.00%; excess_return_240d -35.46% < 8.00%; drawdown_120d -33.43% < -28.00%; volatility_120d 45.27% > 42.00% |
| 603703.SH | 盛洋科技 | ok | 18.57 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -29.70% < 6.00%; excess_return_120d -34.28% < 6.00%; excess_return_240d -23.20% < 8.00%; drawdown_120d -48.75% < -28.00%; volatility_120d 51.85% > 42.00% |
| 603366.SH | 日出东方 | ok | 18.57 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.20% < 6.00%; excess_return_120d -28.78% < 6.00%; excess_return_240d -48.85% < 8.00%; drawdown_120d -34.60% < -28.00%; volatility_120d 44.70% > 42.00% |
| 300177.SZ | 中海达 | ok | 18.57 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.88% < 6.00%; excess_return_120d -44.46% < 6.00%; excess_return_240d -64.18% < 8.00%; drawdown_120d -47.37% < -28.00% |
| 002800.SZ | 天顺股份 | ok | 18.57 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.05% < 6.00%; excess_return_120d -20.63% < 6.00%; excess_return_240d -25.30% < 8.00%; drawdown_120d -48.62% < -28.00%; volatility_120d 52.77% > 42.00% |
| 301368.SZ | 丰立智能 | ok | 18.57 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.33% < 6.00%; excess_return_120d -30.91% < 6.00%; excess_return_240d -44.22% < 8.00%; drawdown_120d -37.61% < -28.00%; volatility_120d 57.96% > 42.00% |
| 600293.SH | 三峡新材 | ok | 18.57 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.46% < 6.00%; excess_return_120d -22.04% < 6.00%; excess_return_240d -43.02% < 8.00%; drawdown_120d -40.37% < -28.00%; volatility_120d 55.67% > 42.00% |
| 000035.SZ | 中国天楹 | ok | 18.57 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.13% < 6.00%; excess_return_120d -18.71% < 6.00%; excess_return_240d -11.02% < 8.00%; drawdown_120d -44.88% < -28.00%; volatility_120d 43.01% > 42.00% |
| 300296.SZ | 利亚德 | ok | 18.57 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.70% < 6.00%; excess_return_120d -17.28% < 6.00%; excess_return_240d -29.53% < 8.00%; drawdown_120d -43.44% < -28.00%; volatility_120d 53.08% > 42.00% |
| 300772.SZ | 运达股份 | ok | 18.56 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.30% < 6.00%; excess_return_120d -41.88% < 6.00%; excess_return_240d -30.84% < 8.00%; drawdown_120d -45.66% < -28.00% |
| 002225.SZ | 濮耐股份 | ok | 18.56 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.02% < 6.00%; excess_return_120d -27.60% < 6.00%; excess_return_240d -46.37% < 8.00%; drawdown_120d -37.42% < -28.00%; volatility_120d 58.33% > 42.00% |
| 002096.SZ | 易普力 | ok | 18.56 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.13% < 6.00%; excess_return_120d -36.71% < 6.00%; excess_return_240d -48.43% < 8.00%; drawdown_120d -38.25% < -28.00% |
| 601106.SH | 中国一重 | ok | 18.56 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.55% < 6.00%; excess_return_120d -26.13% < 6.00%; excess_return_240d -9.71% < 8.00%; drawdown_120d -52.58% < -28.00%; volatility_120d 55.84% > 42.00% |
| 688377.SH | 迪威尔 | ok | 18.55 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.24% < 6.00%; excess_return_120d -22.82% < 6.00%; excess_return_240d -1.77% < 8.00%; drawdown_120d -44.00% < -28.00%; volatility_120d 59.44% > 42.00% |
| 600779.SH | 水井坊 | ok | 18.55 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.68% < 6.00%; excess_return_120d -31.26% < 6.00%; excess_return_240d -52.56% < 8.00%; drawdown_120d -38.50% < -28.00% |
| 300484.SZ | 蓝海华腾 | ok | 18.55 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.90% < 6.00%; excess_return_120d -32.48% < 6.00%; excess_return_240d -57.54% < 8.00%; drawdown_120d -34.27% < -28.00% |
| 002553.SZ | 南方精工 | ok | 18.55 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.77% < 6.00%; excess_return_120d -43.35% < 6.00%; excess_return_240d -42.84% < 8.00%; drawdown_120d -46.08% < -28.00% |
| 600418.SH | 江淮汽车 | ok | 18.55 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -49.70% < 6.00%; excess_return_120d -54.28% < 6.00%; excess_return_240d -61.48% < 8.00%; drawdown_120d -57.65% < -28.00% |
| 301208.SZ | 中亦科技 | ok | 18.55 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.76% < 6.00%; excess_return_120d -32.34% < 6.00%; excess_return_240d -64.15% < 8.00%; drawdown_120d -33.82% < -28.00% |
| 002992.SZ | 宝明科技 | ok | 18.55 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.52% < 6.00%; excess_return_120d -20.10% < 6.00%; excess_return_240d -64.11% < 8.00%; drawdown_120d -30.89% < -28.00%; volatility_120d 43.69% > 42.00% |
| 000816.SZ | 智慧农业 | ok | 18.54 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.15% < 6.00%; excess_return_120d -37.73% < 6.00%; excess_return_240d -42.50% < 8.00%; drawdown_120d -44.34% < -28.00% |
| 603028.SH | 赛福天 | ok | 18.54 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.79% < 6.00%; excess_return_120d -32.37% < 6.00%; excess_return_240d -31.12% < 8.00%; drawdown_120d -37.16% < -28.00%; volatility_120d 45.07% > 42.00% |
| 002425.SZ | 凯撒文化 | ok | 18.54 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.73% < 6.00%; excess_return_120d -28.31% < 6.00%; excess_return_240d -37.21% < 8.00%; drawdown_120d -39.19% < -28.00% |
| 601020.SH | 华钰矿业 | ok | 18.54 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.49% < 6.00%; excess_return_120d -20.98% < 6.00%; excess_return_240d -0.81% < 8.00%; drawdown_120d -46.24% < -28.00%; volatility_120d 60.99% > 42.00% |
| 600389.SH | 江山股份 | ok | 18.53 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.41% < 6.00%; excess_return_120d -24.99% < 6.00%; excess_return_240d -16.56% < 8.00%; drawdown_120d -39.64% < -28.00%; volatility_120d 50.48% > 42.00% |
| 300318.SZ | 博晖创新 | ok | 18.53 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.59% < 6.00%; excess_return_120d -32.17% < 6.00%; excess_return_240d -49.60% < 8.00%; drawdown_120d -44.43% < -28.00% |
| 600686.SH | 金龙汽车 | ok | 18.53 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -31.40% < 6.00%; excess_return_120d -35.98% < 6.00%; excess_return_240d -26.24% < 8.00%; drawdown_120d -45.18% < -28.00%; volatility_120d 52.93% > 42.00% |
| 002295.SZ | 精艺股份 | ok | 18.53 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.51% < 6.00%; excess_return_120d -40.09% < 6.00%; excess_return_240d -35.23% < 8.00%; drawdown_120d -36.75% < -28.00% |
| 600658.SH | 电子城 | ok | 18.53 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.87% < 6.00%; excess_return_120d -32.45% < 6.00%; excess_return_240d -34.82% < 8.00%; drawdown_120d -36.64% < -28.00% |
| 300788.SZ | 中信出版 | ok | 18.53 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.66% < 6.00%; excess_return_120d -17.24% < 6.00%; excess_return_240d -44.18% < 8.00%; drawdown_120d -49.91% < -28.00%; volatility_120d 63.83% > 42.00% |
| 002760.SZ | 凤形股份 | ok | 18.52 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.42% < 6.00%; excess_return_120d -26.00% < 6.00%; excess_return_240d -32.93% < 8.00%; drawdown_120d -35.62% < -28.00%; volatility_120d 47.24% > 42.00% |
| 600633.SH | 浙数文化 | ok | 18.52 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.28% < 6.00%; excess_return_120d -22.86% < 6.00%; excess_return_240d -45.07% < 8.00%; drawdown_120d -41.15% < -28.00%; volatility_120d 53.50% > 42.00% |
| 002607.SZ | 中公教育 | ok | 18.52 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.72% < 6.00%; excess_return_120d -28.30% < 6.00%; excess_return_240d -52.57% < 8.00%; drawdown_120d -40.11% < -28.00%; volatility_120d 46.37% > 42.00% |
| 300659.SZ | 中孚信息 | ok | 18.52 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.09% < 6.00%; excess_return_120d -42.67% < 6.00%; excess_return_240d -54.50% < 8.00%; drawdown_120d -45.34% < -28.00% |
| 301152.SZ | 天力锂能 | ok | 18.51 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.81% < 6.00%; excess_return_120d -27.39% < 6.00%; excess_return_240d -40.31% < 8.00%; drawdown_120d -34.98% < -28.00% |
| 300036.SZ | 超图软件 | ok | 18.51 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.50% < 6.00%; excess_return_120d -44.08% < 6.00%; excess_return_240d -48.31% < 8.00%; drawdown_120d -51.82% < -28.00% |
| 603528.SH | 多伦科技 | ok | 18.51 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.88% < 6.00%; excess_return_120d -43.46% < 6.00%; excess_return_240d -49.37% < 8.00%; drawdown_120d -48.92% < -28.00% |
| 603279.SH | 景津装备 | ok | 18.51 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.36% < 6.00%; excess_return_120d -27.94% < 6.00%; excess_return_240d -31.22% < 8.00%; drawdown_120d -40.74% < -28.00%; volatility_120d 42.70% > 42.00% |
| 600983.SH | 惠而浦 | ok | 18.51 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.38% < 6.00%; excess_return_120d -19.48% < 6.00%; excess_return_240d -55.45% < 8.00%; drawdown_120d -38.44% < -28.00%; volatility_120d 43.58% > 42.00% |
| 002891.SZ | 中宠股份 | ok | 18.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -45.29% < 6.00%; excess_return_120d -49.87% < 6.00%; excess_return_240d -74.10% < 8.00%; drawdown_120d -47.07% < -28.00% |
| 000723.SZ | 美锦能源 | ok | 18.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.02% < 6.00%; excess_return_120d -31.60% < 6.00%; excess_return_240d -42.79% < 8.00%; drawdown_120d -39.61% < -28.00% |
| 002462.SZ | 嘉事堂 | ok | 18.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.02% < 6.00%; excess_return_120d -29.50% < 6.00%; excess_return_240d -37.84% < 8.00%; drawdown_120d -42.00% < -28.00%; volatility_120d 45.90% > 42.00% |
| 603968.SH | 醋化股份 | ok | 18.50 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.68% < 6.00%; excess_return_120d -19.26% < 6.00%; excess_return_240d -40.27% < 8.00%; drawdown_120d -46.31% < -28.00%; volatility_120d 49.30% > 42.00% |
| 300513.SZ | 恒实科技 | ok | 18.50 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.34% < 6.00%; excess_return_120d -30.92% < 6.00%; excess_return_240d -46.10% < 8.00%; drawdown_120d -38.09% < -28.00% |
| 002212.SZ | 天融信 | ok | 18.49 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.93% < 6.00%; excess_return_120d -42.51% < 6.00%; excess_return_240d -47.98% < 8.00%; drawdown_120d -47.73% < -28.00% |
| 001311.SZ | 多利科技 | ok | 18.48 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.54% < 6.00%; excess_return_120d -32.12% < 6.00%; excess_return_240d -8.64% < 8.00%; drawdown_120d -50.51% < -28.00%; volatility_120d 45.05% > 42.00% |
| 300011.SZ | 鼎汉技术 | ok | 18.48 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.67% < 6.00%; excess_return_120d -33.25% < 6.00%; excess_return_240d -40.46% < 8.00%; drawdown_120d -37.99% < -28.00% |
| 605338.SH | 巴比食品 | ok | 18.48 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.11% < 6.00%; excess_return_120d -42.69% < 6.00%; excess_return_240d -16.96% < 8.00%; drawdown_120d -43.34% < -28.00% |
| 300183.SZ | 东软载波 | ok | 18.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.79% < 6.00%; excess_return_120d -35.37% < 6.00%; excess_return_240d -60.51% < 8.00%; drawdown_120d -40.05% < -28.00% |
| 600478.SH | 科力远 | ok | 18.47 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.14% < 6.00%; excess_return_120d -31.72% < 6.00%; excess_return_240d -34.69% < 8.00%; drawdown_120d -41.29% < -28.00% |
| 688007.SH | 光峰科技 | ok | 18.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.89% < 6.00%; excess_return_120d -39.48% < 6.00%; excess_return_240d -36.61% < 8.00%; drawdown_120d -40.47% < -28.00% |
| 002681.SZ | 奋达科技 | ok | 18.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.38% < 6.00%; excess_return_120d -37.96% < 6.00%; excess_return_240d -55.95% < 8.00%; drawdown_120d -37.69% < -28.00% |
| 688122.SH | 西部超导 | ok | 18.47 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -24.51% < 6.00%; excess_return_120d -29.09% < 6.00%; excess_return_240d -8.43% < 8.00%; drawdown_120d -48.82% < -28.00%; volatility_120d 61.13% > 42.00% |
| 300579.SZ | 数字认证 | ok | 18.47 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.40% < 6.00%; excess_return_120d -44.98% < 6.00%; excess_return_240d -60.31% < 8.00%; drawdown_120d -44.45% < -28.00% |
| 000818.SZ | 航锦科技 | ok | 18.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.16% < 6.00%; excess_return_120d -24.74% < 6.00%; excess_return_240d -51.74% < 8.00%; drawdown_120d -40.50% < -28.00%; volatility_120d 66.42% > 42.00% |
| 600839.SH | 四川长虹 | ok | 18.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.15% < 6.00%; excess_return_120d -30.73% < 6.00%; excess_return_240d -51.53% < 8.00%; drawdown_120d -40.32% < -28.00% |
| 603312.SH | 西典新能 | ok | 18.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.67% < 6.00%; excess_return_120d -32.25% < 6.00%; excess_return_240d -27.74% < 8.00%; drawdown_120d -36.60% < -28.00% |
| 300182.SZ | 捷成股份 | ok | 18.46 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.40% < 6.00%; excess_return_120d -19.98% < 6.00%; excess_return_240d -35.64% < 8.00%; drawdown_120d -50.63% < -28.00%; volatility_120d 65.69% > 42.00% |
| 002510.SZ | 天汽模 | ok | 18.46 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.71% < 6.00%; excess_return_120d -30.00% < 6.00%; excess_return_240d -41.00% < 8.00%; drawdown_120d -39.27% < -28.00%; volatility_120d 45.63% > 42.00% |
| 600684.SH | 珠江股份 | ok | 18.46 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.50% < 6.00%; excess_return_120d -35.08% < 6.00%; excess_return_240d -51.92% < 8.00%; drawdown_120d -44.81% < -28.00% |
| 300299.SZ | 富春股份 | ok | 18.45 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.99% < 6.00%; excess_return_120d -35.57% < 6.00%; excess_return_240d -57.13% < 8.00%; drawdown_120d -45.31% < -28.00% |
| 688489.SH | 三未信安 | ok | 18.45 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.22% < 6.00%; excess_return_120d -32.80% < 6.00%; excess_return_240d -40.58% < 8.00%; drawdown_120d -35.46% < -28.00% |
| 300906.SZ | 日月明 | ok | 18.45 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -28.04% < 6.00%; excess_return_120d -32.62% < 6.00%; excess_return_240d -33.97% < 8.00%; drawdown_120d -36.80% < -28.00% |
| 603602.SH | 纵横通信 | ok | 18.44 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.56% < 6.00%; excess_return_120d -28.14% < 6.00%; excess_return_240d -47.92% < 8.00%; drawdown_120d -37.30% < -28.00% |
| 300099.SZ | 尤洛卡 | ok | 18.44 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.73% < 6.00%; excess_return_120d -22.31% < 6.00%; excess_return_240d -34.09% < 8.00%; drawdown_120d -40.10% < -28.00%; volatility_120d 54.43% > 42.00% |
| 600354.SH | 敦煌种业 | ok | 18.44 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.57% < 6.00%; excess_return_120d -27.15% < 6.00%; excess_return_240d -46.21% < 8.00%; drawdown_120d -39.93% < -28.00%; volatility_120d 42.69% > 42.00% |
| 300542.SZ | 新晨科技 | ok | 18.44 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -46.12% < 6.00%; excess_return_120d -50.70% < 6.00%; excess_return_240d -75.98% < 8.00%; drawdown_120d -49.12% < -28.00% |
| 300074.SZ | 华平股份 | ok | 18.44 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.95% < 6.00%; excess_return_120d -29.53% < 6.00%; excess_return_240d -52.31% < 8.00%; drawdown_120d -35.08% < -28.00% |
| 300213.SZ | 佳讯飞鸿 | ok | 18.44 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.76% < 6.00%; excess_return_120d -41.34% < 6.00%; excess_return_240d -52.38% < 8.00%; drawdown_120d -44.21% < -28.00% |
| 002162.SZ | 悦心健康 | ok | 18.44 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.53% < 6.00%; excess_return_120d -27.11% < 6.00%; excess_return_240d -37.73% < 8.00%; drawdown_120d -44.03% < -28.00%; volatility_120d 44.66% > 42.00% |
| 001206.SZ | 依依股份 | ok | 18.44 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.17% < 6.00%; excess_return_120d -43.75% < 6.00%; excess_return_240d -33.67% < 8.00%; drawdown_120d -42.64% < -28.00% |
| 600438.SH | 通威股份 | ok | 18.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -45.04% < 6.00%; excess_return_120d -50.77% < 6.00%; excess_return_240d -48.83% < 8.00%; drawdown_120d -47.80% < -28.00% |
| 300348.SZ | 长亮科技 | ok | 18.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -43.77% < 6.00%; excess_return_120d -48.35% < 6.00%; excess_return_240d -75.91% < 8.00%; drawdown_120d -48.44% < -28.00% |
| 600507.SH | 方大特钢 | ok | 18.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.71% < 6.00%; excess_return_120d -31.29% < 6.00%; excess_return_240d -30.84% < 8.00%; drawdown_120d -42.00% < -28.00% |
| 600536.SH | 中国软件 | ok | 18.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.06% < 6.00%; excess_return_120d -44.64% < 6.00%; excess_return_240d -60.04% < 8.00%; drawdown_120d -47.61% < -28.00% |
| 300266.SZ | 兴源环境 | ok | 18.43 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.96% < 6.00%; excess_return_120d -34.54% < 6.00%; excess_return_240d -59.03% < 8.00%; drawdown_120d -38.98% < -28.00% |
| 000014.SZ | 沙河股份 | ok | 18.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.38% < 6.00%; excess_return_120d -35.96% < 6.00%; excess_return_240d -45.38% < 8.00%; drawdown_120d -42.28% < -28.00% |
| 300525.SZ | 博思软件 | ok | 18.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -46.80% < 6.00%; excess_return_120d -51.38% < 6.00%; excess_return_240d -68.27% < 8.00%; drawdown_120d -54.23% < -28.00% |
| 301135.SZ | 瑞德智能 | ok | 18.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.28% < 6.00%; excess_return_120d -27.86% < 6.00%; excess_return_240d -41.43% < 8.00%; drawdown_120d -32.08% < -28.00% |
| 300897.SZ | 山科智能 | ok | 18.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.85% < 6.00%; excess_return_120d -24.43% < 6.00%; excess_return_240d -25.58% < 8.00%; drawdown_120d -34.18% < -28.00%; volatility_120d 54.53% > 42.00% |
| 002427.SZ | 尤夫股份 | ok | 18.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.59% < 6.00%; excess_return_120d -29.17% < 6.00%; excess_return_240d -61.57% < 8.00%; drawdown_120d -38.81% < -28.00%; volatility_120d 56.78% > 42.00% |
| 688185.SH | 康希诺 | ok | 18.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -15.66% < 6.00%; excess_return_120d -20.24% < 6.00%; excess_return_240d -32.23% < 8.00%; drawdown_120d -33.57% < -28.00%; volatility_120d 45.25% > 42.00% |
| 601702.SH | 华峰铝业 | ok | 18.42 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -26.33% < 6.00%; excess_return_120d -30.91% < 6.00%; excess_return_240d -25.60% < 8.00%; drawdown_120d -46.41% < -28.00%; volatility_120d 53.58% > 42.00% |
| 601086.SH | 国芳集团 | ok | 18.42 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.68% < 6.00%; excess_return_120d -36.26% < 6.00%; excess_return_240d -60.48% < 8.00%; drawdown_120d -37.79% < -28.00% |
| 002596.SZ | 海南瑞泽 | ok | 18.41 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -45.08% < 6.00%; excess_return_120d -49.66% < 6.00%; excess_return_240d -43.61% < 8.00%; drawdown_120d -43.51% < -28.00% |
| 300591.SZ | 万里马 | ok | 18.41 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.07% < 6.00%; excess_return_120d -38.65% < 6.00%; excess_return_240d -69.60% < 8.00%; drawdown_120d -34.53% < -28.00% |
| 002639.SZ | 雪人集团 | ok | 18.41 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -29.84% < 6.00%; excess_return_120d -34.42% < 6.00%; excess_return_240d -3.95% < 8.00%; drawdown_120d -55.32% < -28.00%; volatility_120d 59.79% > 42.00% |
| 600271.SH | 航天信息 | ok | 18.41 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -43.46% < 6.00%; excess_return_120d -48.04% < 6.00%; excess_return_240d -48.70% < 8.00%; drawdown_120d -52.75% < -28.00% |
| 600250.SH | 南京商旅 | ok | 18.41 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.58% < 6.00%; excess_return_120d -35.16% < 6.00%; excess_return_240d -61.51% < 8.00%; drawdown_120d -45.65% < -28.00% |
| 300094.SZ | 国联水产 | ok | 18.41 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.25% < 6.00%; excess_return_120d -31.83% < 6.00%; excess_return_240d -55.86% < 8.00%; drawdown_120d -38.19% < -28.00% |
| 300535.SZ | 达威股份 | ok | 18.41 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.04% < 6.00%; excess_return_120d -24.62% < 6.00%; excess_return_240d -37.73% < 8.00%; drawdown_120d -39.49% < -28.00% |
| 688819.SH | 天能股份 | ok | 18.41 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.27% < 6.00%; excess_return_120d -34.85% < 6.00%; excess_return_240d -35.91% < 8.00%; drawdown_120d -38.25% < -28.00% |
| 002265.SZ | 建设工业 | ok | 18.41 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.69% < 6.00%; excess_return_120d -35.27% < 6.00%; excess_return_240d -53.13% < 8.00%; drawdown_120d -34.47% < -28.00% |
| 300510.SZ | 金冠股份 | ok | 18.40 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.97% < 6.00%; excess_return_120d -28.55% < 6.00%; excess_return_240d -54.99% < 8.00%; drawdown_120d -40.30% < -28.00% |
| 300578.SZ | 会畅科技 | ok | 18.40 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.80% < 6.00%; excess_return_120d -26.38% < 6.00%; excess_return_240d -45.71% < 8.00%; drawdown_120d -51.62% < -28.00%; volatility_120d 68.04% > 42.00% |
| 603101.SH | 汇嘉时代 | ok | 18.40 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.98% < 6.00%; excess_return_120d -33.56% < 6.00%; excess_return_240d -30.33% < 8.00%; drawdown_120d -40.33% < -28.00% |
| 688426.SH | 康为世纪 | ok | 18.40 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.72% < 6.00%; excess_return_120d -29.30% < 6.00%; excess_return_240d -41.96% < 8.00%; drawdown_120d -38.44% < -28.00% |
| 300043.SZ | 星辉娱乐 | ok | 18.40 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.11% < 6.00%; excess_return_120d -23.69% < 6.00%; excess_return_240d -29.02% < 8.00%; drawdown_120d -42.66% < -28.00%; volatility_120d 44.60% > 42.00% |
| 603079.SH | 圣达生物 | ok | 18.40 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.95% < 6.00%; excess_return_120d -36.53% < 6.00%; excess_return_240d -52.89% < 8.00%; drawdown_120d -45.25% < -28.00% |
| 300598.SZ | 诚迈科技 | ok | 18.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.50% < 6.00%; excess_return_120d -45.08% < 6.00%; excess_return_240d -55.93% < 8.00%; drawdown_120d -47.23% < -28.00% |
| 688499.SH | 利元亨 | ok | 18.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.25% < 6.00%; excess_return_120d -26.83% < 6.00%; excess_return_240d -6.84% < 8.00%; drawdown_120d -37.54% < -28.00%; volatility_120d 54.27% > 42.00% |
| 002067.SZ | 景兴纸业 | ok | 18.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.71% < 6.00%; excess_return_120d -30.29% < 6.00%; excess_return_240d -15.29% < 8.00%; drawdown_120d -32.09% < -28.00%; volatility_120d 43.12% > 42.00% |
| 300546.SZ | 雄帝科技 | ok | 18.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -42.63% < 6.00%; excess_return_120d -47.21% < 6.00%; excess_return_240d -74.72% < 8.00%; drawdown_120d -45.25% < -28.00% |
| 002294.SZ | 信立泰 | ok | 18.39 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.71% < 6.00%; excess_return_120d -23.29% < 6.00%; excess_return_240d -31.49% < 8.00%; drawdown_120d -43.46% < -28.00%; volatility_120d 57.57% > 42.00% |
| 000565.SZ | 渝三峡A | ok | 18.38 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.95% < 6.00%; excess_return_120d -21.53% < 6.00%; excess_return_240d -55.37% < 8.00%; drawdown_120d -34.27% < -28.00%; volatility_120d 42.26% > 42.00% |
| 688561.SH | 奇安信 | ok | 18.37 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.90% < 6.00%; excess_return_120d -38.48% < 6.00%; excess_return_240d -50.02% < 8.00%; drawdown_120d -47.59% < -28.00% |
| 000409.SZ | 云鼎科技 | ok | 18.37 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.04% < 6.00%; excess_return_120d -29.63% < 6.00%; excess_return_240d -47.07% < 8.00%; drawdown_120d -41.93% < -28.00% |
| 600844.SH | 金煤科技 | ok | 18.36 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -11.81% < 6.00%; excess_return_120d -16.39% < 6.00%; excess_return_240d -49.35% < 8.00%; drawdown_120d -53.73% < -28.00%; volatility_120d 55.13% > 42.00% |
| 300155.SZ | 安居宝 | ok | 18.36 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.51% < 6.00%; excess_return_120d -43.09% < 6.00%; excess_return_240d -41.73% < 8.00%; drawdown_120d -50.00% < -28.00% |
| 600486.SH | 扬农化工 | ok | 18.36 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.48% < 6.00%; excess_return_120d -27.06% < 6.00%; excess_return_240d -26.58% < 8.00%; drawdown_120d -40.18% < -28.00%; volatility_120d 45.79% > 42.00% |
| 300126.SZ | 锐奇股份 | ok | 18.36 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.72% < 6.00%; excess_return_120d -35.30% < 6.00%; excess_return_240d -39.30% < 8.00%; drawdown_120d -40.52% < -28.00% |
| 603712.SH | 七一二 | ok | 18.36 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.01% < 6.00%; excess_return_120d -44.59% < 6.00%; excess_return_240d -61.93% < 8.00%; drawdown_120d -49.10% < -28.00% |
| 600325.SH | 华发股份 | ok | 18.36 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -44.08% < 6.00%; excess_return_120d -48.66% < 6.00%; excess_return_240d -73.23% < 8.00%; drawdown_120d -50.21% < -28.00% |
| 300949.SZ | 奥雅股份 | ok | 18.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.77% < 6.00%; excess_return_120d -27.35% < 6.00%; excess_return_240d -53.02% < 8.00%; drawdown_120d -34.01% < -28.00% |
| 002095.SZ | 生意宝 | ok | 18.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.90% < 6.00%; excess_return_120d -32.48% < 6.00%; excess_return_240d -60.49% < 8.00%; drawdown_120d -39.93% < -28.00% |
| 688162.SH | 巨一科技 | ok | 18.35 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.48% < 6.00%; excess_return_120d -24.06% < 6.00%; excess_return_240d -29.06% < 8.00%; drawdown_120d -32.50% < -28.00%; volatility_120d 42.61% > 42.00% |
| 688638.SH | 誉辰智能 | ok | 18.34 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.04% < 6.00%; excess_return_120d -18.62% < 6.00%; excess_return_240d -40.61% < 8.00%; drawdown_120d -33.81% < -28.00%; volatility_120d 43.30% > 42.00% |
| 603289.SH | 泰瑞机器 | ok | 18.34 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.55% < 6.00%; excess_return_120d -22.13% < 6.00%; excess_return_240d -33.74% < 8.00%; drawdown_120d -35.88% < -28.00%; volatility_120d 43.30% > 42.00% |
| 300968.SZ | 格林精密 | ok | 18.33 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.68% < 6.00%; excess_return_120d -42.26% < 6.00%; excess_return_240d -57.05% < 8.00%; drawdown_120d -42.82% < -28.00% |
| 002875.SZ | 安奈儿 | ok | 18.33 | close_below_ma200; stock_return_120d -13.29% < 6.00%; excess_return_120d -17.87% < 6.00%; excess_return_240d -30.55% < 8.00%; drawdown_120d -46.42% < -28.00%; volatility_120d 50.35% > 42.00% |
| 002779.SZ | 中坚科技 | ok | 18.33 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.30% < 6.00%; excess_return_120d -33.88% < 6.00%; excess_return_240d -9.22% < 8.00%; drawdown_120d -32.23% < -28.00%; volatility_120d 49.32% > 42.00% |
| 603815.SH | 交建股份 | ok | 18.33 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.88% < 6.00%; excess_return_120d -22.46% < 6.00%; excess_return_240d -38.48% < 8.00%; volatility_120d 50.54% > 42.00% |
| 600477.SH | 杭萧钢构 | ok | 18.32 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.79% < 6.00%; excess_return_120d -25.37% < 6.00%; excess_return_240d -31.89% < 8.00%; drawdown_120d -50.36% < -28.00%; volatility_120d 53.47% > 42.00% |
| 002981.SZ | 朝阳科技 | ok | 18.32 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.35% < 6.00%; excess_return_120d -27.93% < 6.00%; excess_return_240d -41.54% < 8.00%; drawdown_120d -29.80% < -28.00%; volatility_120d 44.94% > 42.00% |
| 000576.SZ | 甘化科工 | ok | 18.32 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.97% < 6.00%; excess_return_120d -31.55% < 6.00%; excess_return_240d -41.49% < 8.00%; drawdown_120d -35.86% < -28.00%; volatility_120d 44.48% > 42.00% |
| 002307.SZ | 北新路桥 | ok | 18.32 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.40% < 6.00%; excess_return_120d -44.98% < 6.00%; excess_return_240d -44.31% < 8.00%; drawdown_120d -45.77% < -28.00% |
| 300789.SZ | 唐源电气 | ok | 18.31 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.22% < 6.00%; excess_return_120d -28.80% < 6.00%; excess_return_240d -55.05% < 8.00%; drawdown_120d -32.96% < -28.00% |
| 603579.SH | 荣泰健康 | ok | 18.31 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.49% < 6.00%; excess_return_120d -23.07% < 6.00%; excess_return_240d -49.40% < 8.00%; drawdown_120d -35.26% < -28.00%; volatility_120d 42.68% > 42.00% |
| 603787.SH | 新日股份 | ok | 18.31 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.23% < 6.00%; excess_return_120d -34.81% < 6.00%; excess_return_240d -43.05% < 8.00%; drawdown_120d -42.74% < -28.00% |
| 300645.SZ | 正元智慧 | ok | 18.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.65% < 6.00%; excess_return_120d -40.23% < 6.00%; excess_return_240d -65.92% < 8.00%; drawdown_120d -44.41% < -28.00% |
| 600094.SH | 大名城 | ok | 18.30 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.11% < 6.00%; excess_return_120d -20.69% < 6.00%; excess_return_240d -11.69% < 8.00%; drawdown_120d -38.01% < -28.00%; volatility_120d 42.60% > 42.00% |
| 688236.SH | 春立医疗 | ok | 18.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.49% < 6.00%; excess_return_120d -36.07% < 6.00%; excess_return_240d -35.39% < 8.00%; drawdown_120d -46.09% < -28.00% |
| 300662.SZ | 科锐国际 | ok | 18.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.21% < 6.00%; excess_return_120d -32.79% < 6.00%; excess_return_240d -59.24% < 8.00%; drawdown_120d -45.01% < -28.00% |
| 003002.SZ | 壶化股份 | ok | 18.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -44.98% < 6.00%; excess_return_120d -49.56% < 6.00%; excess_return_240d -57.75% < 8.00%; drawdown_120d -46.85% < -28.00% |
| 001296.SZ | 长江材料 | ok | 18.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.84% < 6.00%; excess_return_120d -31.42% < 6.00%; excess_return_240d -28.43% < 8.00%; drawdown_120d -37.70% < -28.00%; volatility_120d 42.10% > 42.00% |
| 002855.SZ | 捷荣技术 | ok | 18.30 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -42.74% < 6.00%; excess_return_120d -47.32% < 6.00%; excess_return_240d -70.67% < 8.00%; drawdown_120d -45.31% < -28.00% |
| 600815.SH | 厦工股份 | ok | 18.30 | close_below_ma200; stock_return_120d -21.74% < 6.00%; excess_return_120d -26.32% < 6.00%; excess_return_240d -25.35% < 8.00%; drawdown_120d -47.16% < -28.00%; volatility_120d 56.42% > 42.00% |
| 603586.SH | 金麒麟 | ok | 18.29 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.07% < 6.00%; excess_return_120d -32.65% < 6.00%; excess_return_240d -47.95% < 8.00%; drawdown_120d -33.86% < -28.00% |
| 600313.SH | 农发种业 | ok | 18.28 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.12% < 6.00%; excess_return_120d -21.70% < 6.00%; excess_return_240d -37.83% < 8.00%; drawdown_120d -45.56% < -28.00%; volatility_120d 50.12% > 42.00% |
| 600199.SH | 金种子酒 | ok | 18.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.71% < 6.00%; excess_return_120d -36.30% < 6.00%; excess_return_240d -58.68% < 8.00%; drawdown_120d -41.50% < -28.00% |
| 600281.SH | 华阳新材 | ok | 18.28 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.86% < 6.00%; excess_return_120d -36.44% < 6.00%; excess_return_240d -64.32% < 8.00%; drawdown_120d -40.62% < -28.00% |
| 301270.SZ | 汉仪股份 | ok | 18.27 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.35% < 6.00%; excess_return_120d -29.93% < 6.00%; excess_return_240d -60.32% < 8.00%; drawdown_120d -46.04% < -28.00%; volatility_120d 52.43% > 42.00% |
| 002799.SZ | 环球印务 | ok | 18.27 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.32% < 6.00%; excess_return_120d -31.90% < 6.00%; excess_return_240d -49.25% < 8.00%; drawdown_120d -38.86% < -28.00% |
| 002912.SZ | 中新赛克 | ok | 18.27 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.59% < 6.00%; excess_return_120d -42.17% < 6.00%; excess_return_240d -40.92% < 8.00%; drawdown_120d -46.36% < -28.00% |
| 301078.SZ | 孩子王 | ok | 18.27 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.34% < 6.00%; excess_return_120d -39.92% < 6.00%; excess_return_240d -69.69% < 8.00%; drawdown_120d -44.25% < -28.00% |
| 603881.SH | 数据港 | ok | 18.27 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.32% < 6.00%; excess_return_120d -13.90% < 6.00%; excess_return_240d -14.68% < 8.00%; drawdown_120d -38.86% < -28.00%; volatility_120d 63.55% > 42.00% |
| 605555.SH | 德昌股份 | ok | 18.26 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.30% < 6.00%; excess_return_120d -32.59% < 6.00%; excess_return_240d -40.45% < 8.00%; drawdown_120d -33.94% < -28.00%; volatility_120d 47.26% > 42.00% |
| 301262.SZ | 海看股份 | ok | 18.25 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.69% < 6.00%; excess_return_120d -27.27% < 6.00%; excess_return_240d -47.30% < 8.00%; drawdown_120d -51.54% < -28.00%; volatility_120d 50.42% > 42.00% |
| 300072.SZ | 海新能科 | ok | 18.25 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.70% < 6.00%; excess_return_120d -28.28% < 6.00%; excess_return_240d -19.94% < 8.00%; drawdown_120d -43.48% < -28.00%; volatility_120d 55.78% > 42.00% |
| 000676.SZ | 智度股份 | ok | 18.24 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.40% < 6.00%; excess_return_120d -43.98% < 6.00%; excess_return_240d -63.50% < 8.00%; drawdown_120d -52.45% < -28.00% |
| 000655.SZ | 金岭矿业 | ok | 18.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.91% < 6.00%; excess_return_120d -34.49% < 6.00%; excess_return_240d -36.15% < 8.00%; drawdown_120d -44.81% < -28.00% |
| 001278.SZ | 一彬科技 | ok | 18.23 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.67% < 6.00%; excess_return_120d -23.25% < 6.00%; excess_return_240d -30.59% < 8.00%; drawdown_120d -41.89% < -28.00%; volatility_120d 52.74% > 42.00% |
| 688522.SH | 纳睿雷达 | ok | 18.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.09% < 6.00%; excess_return_120d -31.67% < 6.00%; excess_return_240d -61.31% < 8.00%; drawdown_120d -39.43% < -28.00%; volatility_120d 48.80% > 42.00% |
| 600072.SH | 中船科技 | ok | 18.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.39% < 6.00%; excess_return_120d -29.97% < 6.00%; excess_return_240d -54.91% < 8.00%; drawdown_120d -40.25% < -28.00% |
| 301011.SZ | 华立科技 | ok | 18.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -43.42% < 6.00%; excess_return_120d -48.00% < 6.00%; excess_return_240d -69.02% < 8.00%; drawdown_120d -51.49% < -28.00% |
| 001300.SZ | 三柏硕 | ok | 18.23 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.24% < 6.00%; excess_return_120d -27.82% < 6.00%; excess_return_240d -35.28% < 8.00%; drawdown_120d -38.20% < -28.00% |
| 300494.SZ | 盛天网络 | ok | 18.23 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.99% < 6.00%; excess_return_120d -36.57% < 6.00%; excess_return_240d -61.98% < 8.00%; drawdown_120d -45.26% < -28.00% |
| 000572.SZ | 海马汽车 | ok | 18.22 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -53.55% < 6.00%; excess_return_120d -58.13% < 6.00%; excess_return_240d -39.94% < 8.00%; drawdown_120d -52.92% < -28.00% |
| 603556.SH | 海兴电力 | ok | 18.22 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -37.06% < 6.00%; excess_return_120d -41.64% < 6.00%; excess_return_240d -32.50% < 8.00%; drawdown_120d -47.07% < -28.00% |
| 600855.SH | 航天长峰 | ok | 18.22 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -34.98% < 6.00%; excess_return_120d -39.56% < 6.00%; excess_return_240d -19.69% < 8.00%; drawdown_120d -54.40% < -28.00%; volatility_120d 54.53% > 42.00% |
| 002920.SZ | 德赛西威 | ok | 18.22 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.97% < 6.00%; excess_return_120d -33.55% < 6.00%; excess_return_240d -36.78% < 8.00%; drawdown_120d -40.25% < -28.00% |
| 002313.SZ | 日海智能 | ok | 18.22 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.75% < 6.00%; excess_return_120d -28.33% < 6.00%; excess_return_240d -42.53% < 8.00%; drawdown_120d -29.81% < -28.00%; volatility_120d 44.77% > 42.00% |
| 300148.SZ | 天舟文化 | ok | 18.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.33% < 6.00%; excess_return_120d -31.92% < 6.00%; excess_return_240d -57.55% < 8.00%; drawdown_120d -48.05% < -28.00% |
| 605500.SH | 森林包装 | ok | 18.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.24% < 6.00%; excess_return_120d -30.82% < 6.00%; excess_return_240d -61.01% < 8.00%; drawdown_120d -47.30% < -28.00% |
| 605169.SH | 洪通燃气 | ok | 18.21 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.30% < 6.00%; excess_return_120d -31.88% < 6.00%; excess_return_240d -33.48% < 8.00%; drawdown_120d -40.27% < -28.00% |
| 600619.SH | 海立股份 | ok | 18.20 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.04% < 6.00%; excess_return_120d -36.62% < 6.00%; excess_return_240d -2.96% < 8.00%; drawdown_120d -35.96% < -28.00% |
| 002248.SZ | 华东数控 | ok | 18.20 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.21% < 6.00%; excess_return_120d -24.79% < 6.00%; excess_return_240d -17.84% < 8.00%; drawdown_120d -40.95% < -28.00%; volatility_120d 49.57% > 42.00% |
| 002362.SZ | 汉王科技 | ok | 18.20 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.36% < 6.00%; excess_return_120d -34.94% < 6.00%; excess_return_240d -52.57% < 8.00%; drawdown_120d -40.34% < -28.00% |
| 600229.SH | 城市传媒 | ok | 18.20 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.92% < 6.00%; excess_return_120d -29.50% < 6.00%; excess_return_240d -53.67% < 8.00%; drawdown_120d -34.44% < -28.00% |
| 000536.SZ | 华映科技 | ok | 18.20 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.02% < 6.00%; excess_return_120d -30.60% < 6.00%; excess_return_240d -40.34% < 8.00%; drawdown_120d -32.90% < -28.00%; volatility_120d 53.25% > 42.00% |
| 000065.SZ | 北方国际 | ok | 18.20 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.31% < 6.00%; excess_return_120d -27.89% < 6.00%; excess_return_240d -34.98% < 8.00%; drawdown_120d -41.79% < -28.00%; volatility_120d 54.11% > 42.00% |
| 002451.SZ | 摩恩电气 | ok | 18.19 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -30.34% < 6.00%; excess_return_120d -34.92% < 6.00%; excess_return_240d -22.22% < 8.00%; drawdown_120d -47.11% < -28.00% |
| 601218.SH | 吉鑫科技 | ok | 18.19 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.83% < 6.00%; excess_return_120d -19.41% < 6.00%; excess_return_240d -25.03% < 8.00%; drawdown_120d -47.65% < -28.00%; volatility_120d 49.75% > 42.00% |
| 300947.SZ | 德必集团 | ok | 18.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.00% < 6.00%; excess_return_120d -39.59% < 6.00%; excess_return_240d -70.71% < 8.00%; drawdown_120d -41.01% < -28.00% |
| 002548.SZ | 金新农 | ok | 18.19 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -32.24% < 6.00%; excess_return_120d -36.82% < 6.00%; excess_return_240d -14.36% < 8.00%; drawdown_120d -43.02% < -28.00%; volatility_120d 49.95% > 42.00% |
| 002434.SZ | 万里扬 | ok | 18.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.65% < 6.00%; excess_return_120d -36.23% < 6.00%; excess_return_240d -31.35% < 8.00%; drawdown_120d -42.45% < -28.00% |
| 002862.SZ | 实丰文化 | ok | 18.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.82% < 6.00%; excess_return_120d -37.40% < 6.00%; excess_return_240d -51.68% < 8.00%; drawdown_120d -40.98% < -28.00% |
| 600682.SH | 南京新百 | ok | 18.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.81% < 6.00%; excess_return_120d -40.39% < 6.00%; excess_return_240d -34.44% < 8.00%; drawdown_120d -41.44% < -28.00% |
| 600792.SH | 云煤能源 | ok | 18.19 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -14.69% < 6.00%; excess_return_120d -19.27% < 6.00%; excess_return_240d -33.99% < 8.00%; drawdown_120d -39.15% < -28.00%; volatility_120d 59.43% > 42.00% |
| 600775.SH | 南京熊猫 | ok | 18.18 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.07% < 6.00%; excess_return_120d -24.65% < 6.00%; excess_return_240d -30.73% < 8.00%; drawdown_120d -51.27% < -28.00%; volatility_120d 54.45% > 42.00% |
| 688701.SH | 卓锦股份 | ok | 18.18 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.20% < 6.00%; excess_return_120d -13.78% < 6.00%; excess_return_240d -31.94% < 8.00%; drawdown_120d -39.49% < -28.00%; volatility_120d 47.86% > 42.00% |
| 600758.SH | 辽宁能源 | ok | 18.18 | close_below_ma200; stock_return_120d -13.19% < 6.00%; excess_return_120d -17.77% < 6.00%; excess_return_240d -40.65% < 8.00%; drawdown_120d -49.76% < -28.00%; volatility_120d 66.03% > 42.00% |
| 601606.SH | 长城军工 | ok | 18.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.81% < 6.00%; excess_return_120d -45.39% < 6.00%; excess_return_240d -22.10% < 8.00%; drawdown_120d -46.14% < -28.00% |
| 301299.SZ | 卓创资讯 | ok | 18.17 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.41% < 6.00%; excess_return_120d -20.99% < 6.00%; excess_return_240d -48.71% < 8.00%; drawdown_120d -38.71% < -28.00%; volatility_120d 52.21% > 42.00% |
| 300674.SZ | 宇信科技 | ok | 18.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.36% < 6.00%; excess_return_120d -41.94% < 6.00%; excess_return_240d -70.42% < 8.00%; drawdown_120d -44.57% < -28.00% |
| 603677.SH | 奇精机械 | ok | 18.17 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.59% < 6.00%; excess_return_120d -31.17% < 6.00%; excess_return_240d -54.33% < 8.00%; drawdown_120d -29.26% < -28.00% |
| 300098.SZ | 高新兴 | ok | 18.16 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.21% < 6.00%; excess_return_120d -31.79% < 6.00%; excess_return_240d -33.52% < 8.00%; drawdown_120d -42.19% < -28.00%; volatility_120d 43.00% > 42.00% |
| 688080.SH | 映翰通 | ok | 18.16 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.90% < 6.00%; excess_return_120d -25.48% < 6.00%; excess_return_240d -38.54% < 8.00%; drawdown_120d -42.25% < -28.00%; volatility_120d 59.91% > 42.00% |
| 300443.SZ | 金雷股份 | ok | 18.16 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.90% < 6.00%; excess_return_120d -27.48% < 6.00%; excess_return_240d -24.58% < 8.00%; drawdown_120d -36.81% < -28.00% |
| 002866.SZ | 传艺科技 | ok | 18.15 | close_below_ma200; stock_return_120d -14.48% < 6.00%; excess_return_120d -19.06% < 6.00%; excess_return_240d -42.66% < 8.00%; drawdown_120d -48.83% < -28.00%; volatility_120d 53.05% > 42.00% |
| 301083.SZ | 百胜智能 | ok | 18.15 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.94% < 6.00%; excess_return_120d -33.52% < 6.00%; excess_return_240d -35.79% < 8.00%; drawdown_120d -40.54% < -28.00% |
| 000158.SZ | 常山北明 | ok | 18.15 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.45% < 6.00%; excess_return_120d -41.03% < 6.00%; excess_return_240d -61.80% < 8.00%; drawdown_120d -42.42% < -28.00% |
| 002777.SZ | 久远银海 | ok | 18.14 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.01% < 6.00%; excess_return_120d -36.59% < 6.00%; excess_return_240d -53.18% < 8.00%; drawdown_120d -49.18% < -28.00% |
| 300132.SZ | 青松股份 | ok | 18.14 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -30.88% < 6.00%; excess_return_120d -35.46% < 6.00%; excess_return_240d -20.93% < 8.00%; drawdown_120d -39.07% < -28.00%; volatility_120d 42.21% > 42.00% |
| 001306.SZ | 夏厦精密 | ok | 18.14 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.17% < 6.00%; excess_return_120d -36.75% < 6.00%; excess_return_240d -38.74% < 8.00%; drawdown_120d -35.42% < -28.00% |
| 002562.SZ | 兄弟科技 | ok | 18.13 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.62% < 6.00%; excess_return_120d -33.20% < 6.00%; excess_return_240d -42.14% < 8.00%; drawdown_120d -42.68% < -28.00% |
| 300597.SZ | 吉大通信 | ok | 18.13 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.05% < 6.00%; excess_return_120d -27.63% < 6.00%; excess_return_240d -47.23% < 8.00%; drawdown_120d -41.24% < -28.00% |
| 600981.SH | 苏豪汇鸿 | ok | 18.12 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.03% < 6.00%; excess_return_120d -32.61% < 6.00%; excess_return_240d -43.17% < 8.00%; drawdown_120d -36.34% < -28.00% |
| 605077.SH | 华康股份 | ok | 18.12 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.14% < 6.00%; excess_return_120d -27.72% < 6.00%; excess_return_240d -51.58% < 8.00%; drawdown_120d -41.85% < -28.00% |
| 600159.SH | 大龙地产 | ok | 18.12 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.33% < 6.00%; excess_return_120d -21.91% < 6.00%; excess_return_240d -41.03% < 8.00%; drawdown_120d -34.20% < -28.00% |
| 600173.SH | 卧龙新能 | ok | 18.12 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -16.27% < 6.00%; excess_return_120d -20.85% < 6.00%; excess_return_240d -22.26% < 8.00%; drawdown_120d -35.81% < -28.00%; volatility_120d 50.21% > 42.00% |
| 603409.SH | 汇通控股 | ok | 18.11 | close_below_ma200; stock_return_120d -23.18% < 6.00%; excess_return_120d -27.76% < 6.00%; excess_return_240d -38.07% < 8.00%; drawdown_120d -37.88% < -28.00%; volatility_120d 42.06% > 42.00% |
| 600721.SH | 百花医药 | ok | 18.11 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.95% < 6.00%; excess_return_120d -38.67% < 6.00%; excess_return_240d -27.06% < 8.00%; drawdown_120d -44.11% < -28.00%; volatility_120d 52.20% > 42.00% |
| 002300.SZ | 太阳电缆 | ok | 18.11 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.72% < 6.00%; excess_return_120d -32.30% < 6.00%; excess_return_240d -24.86% < 8.00%; drawdown_120d -46.59% < -28.00%; volatility_120d 57.24% > 42.00% |
| 600416.SH | 湘电股份 | ok | 18.10 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.35% < 6.00%; excess_return_120d -43.93% < 6.00%; excess_return_240d -50.52% < 8.00%; drawdown_120d -45.90% < -28.00% |
| 002868.SZ | 绿康生化 | ok | 18.10 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.12% < 6.00%; excess_return_120d -24.22% < 6.00%; excess_return_240d -11.46% < 8.00%; drawdown_120d -41.21% < -28.00%; volatility_120d 47.92% > 42.00% |
| 601599.SH | 浙文影业 | ok | 18.10 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.89% < 6.00%; excess_return_120d -32.47% < 6.00%; excess_return_240d -45.57% < 8.00%; drawdown_120d -49.11% < -28.00% |
| 688660.SH | 电气风电 | ok | 18.10 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -51.56% < 6.00%; excess_return_120d -56.14% < 6.00%; excess_return_240d -26.60% < 8.00%; drawdown_120d -54.42% < -28.00% |
| 600280.SH | 中央商场 | ok | 18.10 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.87% < 6.00%; excess_return_120d -34.45% < 6.00%; excess_return_240d -46.30% < 8.00%; drawdown_120d -40.66% < -28.00%; volatility_120d 52.94% > 42.00% |
| 688063.SH | 派能科技 | ok | 18.10 | close_below_ma200; stock_return_120d -11.32% < 6.00%; excess_return_120d -15.90% < 6.00%; excess_return_240d -13.01% < 8.00%; drawdown_120d -43.11% < -28.00%; volatility_120d 53.05% > 42.00% |
| 000819.SZ | 岳阳兴长 | ok | 18.10 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.48% < 6.00%; excess_return_120d -32.06% < 6.00%; excess_return_240d -45.70% < 8.00%; drawdown_120d -38.31% < -28.00% |
| 300254.SZ | 仟源医药 | ok | 18.10 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.61% < 6.00%; excess_return_120d -20.19% < 6.00%; excess_return_240d -39.14% < 8.00%; drawdown_120d -43.82% < -28.00%; volatility_120d 53.07% > 42.00% |
| 600328.SH | 中盐化工 | ok | 18.10 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -24.28% < 6.00%; excess_return_120d -28.87% < 6.00%; excess_return_240d -39.74% < 8.00%; drawdown_120d -41.40% < -28.00% |
| 300389.SZ | 艾比森 | ok | 18.09 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.09% < 6.00%; excess_return_120d -24.67% < 6.00%; excess_return_240d -7.62% < 8.00%; drawdown_120d -41.05% < -28.00%; volatility_120d 57.87% > 42.00% |
| 000599.SZ | 青岛双星 | ok | 18.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.44% < 6.00%; excess_return_120d -39.02% < 6.00%; excess_return_240d -36.00% < 8.00%; drawdown_120d -46.42% < -28.00% |
| 603900.SH | 莱绅通灵 | ok | 18.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.31% < 6.00%; excess_return_120d -33.89% < 6.00%; excess_return_240d -68.04% < 8.00%; drawdown_120d -47.50% < -28.00% |
| 002702.SZ | 海欣食品 | ok | 18.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.81% < 6.00%; excess_return_120d -40.39% < 6.00%; excess_return_240d -15.31% < 8.00%; drawdown_120d -43.72% < -28.00% |
| 300973.SZ | 立高食品 | ok | 18.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.60% < 6.00%; excess_return_120d -43.18% < 6.00%; excess_return_240d -66.31% < 8.00%; drawdown_120d -44.43% < -28.00% |
| 600807.SH | 济高发展 | ok | 18.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.05% < 6.00%; excess_return_120d -27.63% < 6.00%; excess_return_240d -49.28% < 8.00%; drawdown_120d -37.47% < -28.00% |
| 300135.SZ | 宝利国际 | ok | 18.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.52% < 6.00%; excess_return_120d -26.10% < 6.00%; excess_return_240d -43.79% < 8.00%; drawdown_120d -42.59% < -28.00%; volatility_120d 44.32% > 42.00% |
| 300879.SZ | 大叶股份 | ok | 18.09 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -43.45% < 6.00%; excess_return_120d -48.03% < 6.00%; excess_return_240d -80.55% < 8.00%; drawdown_120d -46.10% < -28.00% |
| 603759.SH | 海天股份 | ok | 18.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.63% < 6.00%; excess_return_120d -33.21% < 6.00%; excess_return_240d -33.52% < 8.00%; drawdown_120d -44.00% < -28.00%; volatility_120d 42.05% > 42.00% |
| 002163.SZ | 海南发展 | ok | 18.08 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -65.02% < 6.00%; excess_return_120d -69.60% < 6.00%; excess_return_240d -35.03% < 8.00%; drawdown_120d -63.02% < -28.00% |
| 000905.SZ | 厦门港务 | ok | 18.07 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -37.69% < 6.00%; excess_return_120d -42.27% < 6.00%; excess_return_240d -21.77% < 8.00%; drawdown_120d -45.20% < -28.00% |
| 300722.SZ | 新余国科 | ok | 18.07 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.41% < 6.00%; excess_return_120d -41.99% < 6.00%; excess_return_240d -57.61% < 8.00%; drawdown_120d -44.37% < -28.00% |
| 600756.SH | 浪潮软件 | ok | 18.06 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.68% < 6.00%; excess_return_120d -37.26% < 6.00%; excess_return_240d -37.43% < 8.00%; drawdown_120d -42.30% < -28.00% |
| 300937.SZ | 药易购 | ok | 18.06 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.60% < 6.00%; excess_return_120d -45.18% < 6.00%; excess_return_240d -50.39% < 8.00%; drawdown_120d -54.37% < -28.00% |
| 002578.SZ | 闽发铝业 | ok | 18.05 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -30.29% < 6.00%; excess_return_120d -34.87% < 6.00%; excess_return_240d -29.84% < 8.00%; drawdown_120d -42.67% < -28.00%; volatility_120d 54.37% > 42.00% |
| 600643.SH | 爱建集团 | ok | 18.05 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.66% < 6.00%; excess_return_120d -34.24% < 6.00%; excess_return_240d -63.98% < 8.00%; drawdown_120d -33.84% < -28.00% |
| 603117.SH | 万林物流 | ok | 18.05 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.85% < 6.00%; excess_return_120d -30.43% < 6.00%; excess_return_240d -63.25% < 8.00%; drawdown_120d -42.81% < -28.00% |
| 603138.SH | 海量数据 | ok | 18.04 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -6.54% < 6.00%; excess_return_120d -11.12% < 6.00%; excess_return_240d -31.78% < 8.00%; drawdown_120d -46.63% < -28.00%; volatility_120d 68.38% > 42.00% |
| 301330.SZ | 熵基科技 | ok | 18.04 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.31% < 6.00%; excess_return_120d -27.89% < 6.00%; excess_return_240d -30.07% < 8.00%; drawdown_120d -50.06% < -28.00%; volatility_120d 58.70% > 42.00% |
| 002324.SZ | 普利特 | ok | 18.04 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -28.21% < 6.00%; excess_return_120d -32.79% < 6.00%; excess_return_240d -21.24% < 8.00%; drawdown_120d -55.32% < -28.00%; volatility_120d 53.39% > 42.00% |
| 300459.SZ | 汤姆猫 | ok | 18.03 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.58% < 6.00%; excess_return_120d -31.16% < 6.00%; excess_return_240d -60.05% < 8.00%; drawdown_120d -49.02% < -28.00% |
| 605136.SH | 丽人丽妆 | ok | 18.03 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.69% < 6.00%; excess_return_120d -37.27% < 6.00%; excess_return_240d -53.36% < 8.00%; drawdown_120d -48.03% < -28.00% |
| 300724.SZ | 捷佳伟创 | ok | 18.03 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.98% < 6.00%; excess_return_120d -32.56% < 6.00%; excess_return_240d 0.03% < 8.00%; drawdown_120d -54.99% < -28.00%; volatility_120d 64.66% > 42.00% |
| 600992.SH | 贵绳股份 | ok | 18.03 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.56% < 6.00%; excess_return_120d -39.14% < 6.00%; excess_return_240d -62.44% < 8.00%; drawdown_120d -41.07% < -28.00% |
| 300134.SZ | 大富科技 | ok | 18.03 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.40% < 6.00%; excess_return_120d -38.98% < 6.00%; excess_return_240d -54.16% < 8.00%; drawdown_120d -39.17% < -28.00% |
| 300002.SZ | 神州泰岳 | ok | 18.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.25% < 6.00%; excess_return_120d -37.83% < 6.00%; excess_return_240d -60.96% < 8.00%; drawdown_120d -45.08% < -28.00% |
| 605499.SH | 东鹏饮料 | ok | 18.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.23% < 6.00%; excess_return_120d -41.81% < 6.00%; excess_return_240d -64.97% < 8.00%; drawdown_120d -40.41% < -28.00% |
| 301153.SZ | 中科江南 | ok | 18.02 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -33.43% < 6.00%; excess_return_120d -38.01% < 6.00%; excess_return_240d -57.92% < 8.00%; drawdown_120d -41.73% < -28.00% |
| 002469.SZ | 三维化学 | ok | 18.02 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.73% < 6.00%; excess_return_120d -32.31% < 6.00%; excess_return_240d -47.47% < 8.00%; drawdown_120d -44.17% < -28.00% |
| 002721.SZ | 金一文化 | ok | 18.01 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.57% < 6.00%; excess_return_120d -33.15% < 6.00%; excess_return_240d -73.73% < 8.00%; drawdown_120d -47.06% < -28.00% |
| 300399.SZ | 天利科技 | ok | 18.01 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.55% < 6.00%; excess_return_120d -29.13% < 6.00%; excess_return_240d -64.82% < 8.00%; drawdown_120d -40.64% < -28.00%; volatility_120d 58.10% > 42.00% |
| 688651.SH | 盛邦安全 | ok | 18.01 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -28.33% < 6.00%; excess_return_120d -32.91% < 6.00%; excess_return_240d -27.50% < 8.00%; drawdown_120d -47.76% < -28.00%; volatility_120d 61.35% > 42.00% |
| 002879.SZ | 长缆科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.35% < 6.00%; excess_return_120d -26.93% < 6.00%; excess_return_240d -27.06% < 8.00%; drawdown_120d -42.51% < -28.00%; volatility_120d 46.50% > 42.00% |
| 000862.SZ | 银星能源 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.29% < 6.00%; excess_return_120d -21.87% < 6.00%; excess_return_240d -38.53% < 8.00%; drawdown_120d -48.83% < -28.00%; volatility_120d 53.03% > 42.00% |
| 601777.SH | 千里科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.64% < 6.00%; excess_return_120d -26.22% < 6.00%; excess_return_240d -20.49% < 8.00%; drawdown_120d -35.43% < -28.00%; volatility_120d 45.38% > 42.00% |
| 300130.SZ | 新国都 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.82% < 6.00%; excess_return_120d -34.40% < 6.00%; excess_return_240d -67.19% < 8.00%; drawdown_120d -37.52% < -28.00%; volatility_120d 48.06% > 42.00% |
| 301004.SZ | 嘉益股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.83% < 6.00%; excess_return_120d -40.41% < 6.00%; excess_return_240d -74.00% < 8.00%; drawdown_120d -47.62% < -28.00% |
| 300063.SZ | 天龙集团 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -4.78% < 6.00%; excess_return_120d -9.36% < 6.00%; excess_return_240d -25.77% < 8.00%; drawdown_120d -55.63% < -28.00%; volatility_120d 87.09% > 42.00% |
| 600800.SH | 渤海化学 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.25% < 6.00%; excess_return_120d -13.83% < 6.00%; excess_return_240d -48.73% < 8.00%; drawdown_120d -43.42% < -28.00%; volatility_120d 57.91% > 42.00% |
| 301658.SZ | 首航新能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.71% < 6.00%; excess_return_120d -14.29% < 6.00%; excess_return_240d -49.51% < 8.00%; drawdown_120d -61.53% < -28.00%; volatility_120d 74.07% > 42.00% |
| 300798.SZ | 锦鸡股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.85% < 6.00%; excess_return_120d -14.43% < 6.00%; excess_return_240d -53.34% < 8.00%; drawdown_120d -52.24% < -28.00%; volatility_120d 73.79% > 42.00% |
| 002195.SZ | 岩山科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.85% < 6.00%; excess_return_120d -14.43% < 6.00%; excess_return_240d -4.24% < 8.00%; drawdown_120d -51.55% < -28.00%; volatility_120d 59.75% > 42.00% |
| 300792.SZ | 壹网壹创 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -9.90% < 6.00%; excess_return_120d -14.48% < 6.00%; excess_return_240d -16.74% < 8.00%; drawdown_120d -50.68% < -28.00%; volatility_120d 75.13% > 42.00% |
| 603103.SH | 横店影视 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -10.92% < 6.00%; excess_return_120d -15.50% < 6.00%; excess_return_240d -30.48% < 8.00%; drawdown_120d -63.49% < -28.00%; volatility_120d 68.27% > 42.00% |
| 300651.SZ | 金陵体育 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.83% < 6.00%; excess_return_120d -17.41% < 6.00%; excess_return_240d -53.65% < 8.00%; drawdown_120d -53.83% < -28.00%; volatility_120d 79.71% > 42.00% |
| 601616.SH | 广电电气 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -12.95% < 6.00%; excess_return_120d -17.53% < 6.00%; excess_return_240d -36.25% < 8.00%; drawdown_120d -49.78% < -28.00%; volatility_120d 56.77% > 42.00% |
| 301291.SZ | 明阳电气 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -13.41% < 6.00%; excess_return_120d -17.99% < 6.00%; excess_return_240d -31.85% < 8.00%; drawdown_120d -51.15% < -28.00%; volatility_120d 65.53% > 42.00% |
| 603393.SH | 新天然气 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.07% < 6.00%; excess_return_120d -18.65% < 6.00%; excess_return_240d -41.78% < 8.00%; drawdown_120d -48.07% < -28.00%; volatility_120d 51.90% > 42.00% |
| 300113.SZ | 顺网科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.12% < 6.00%; excess_return_120d -18.70% < 6.00%; excess_return_240d -33.60% < 8.00%; drawdown_120d -45.59% < -28.00%; volatility_120d 74.50% > 42.00% |
| 002218.SZ | 拓日新能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.29% < 6.00%; excess_return_120d -18.87% < 6.00%; excess_return_240d -20.83% < 8.00%; drawdown_120d -54.52% < -28.00%; volatility_120d 70.35% > 42.00% |
| 600986.SH | 浙文互联 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -14.83% < 6.00%; excess_return_120d -19.41% < 6.00%; excess_return_240d -41.62% < 8.00%; drawdown_120d -59.59% < -28.00%; volatility_120d 73.04% > 42.00% |
| 688737.SH | 中自科技 | ok | 18.00 | close_below_ma200; stock_return_120d -15.24% < 6.00%; excess_return_120d -19.82% < 6.00%; excess_return_240d -30.57% < 8.00%; drawdown_120d -41.11% < -28.00%; volatility_120d 57.29% > 42.00% |
| 688316.SH | 青云科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.26% < 6.00%; excess_return_120d -19.84% < 6.00%; excess_return_240d -40.42% < 8.00%; drawdown_120d -48.16% < -28.00%; volatility_120d 85.67% > 42.00% |
| 600644.SH | 乐山电力 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.36% < 6.00%; excess_return_120d -19.94% < 6.00%; excess_return_240d -70.78% < 8.00%; drawdown_120d -41.04% < -28.00%; volatility_120d 52.83% > 42.00% |
| 301636.SZ | 泽润新能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -15.75% < 6.00%; excess_return_120d -20.33% < 6.00%; excess_return_240d -51.71% < 8.00%; drawdown_120d -63.80% < -28.00%; volatility_120d 73.52% > 42.00% |
| 601015.SH | 陕西黑猫 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.02% < 6.00%; excess_return_120d -20.60% < 6.00%; excess_return_240d -30.89% < 8.00%; drawdown_120d -48.30% < -28.00%; volatility_120d 63.11% > 42.00% |
| 301378.SZ | 通达海 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.23% < 6.00%; excess_return_120d -20.81% < 6.00%; excess_return_240d -40.73% < 8.00%; drawdown_120d -56.42% < -28.00%; volatility_120d 74.65% > 42.00% |
| 300157.SZ | 新锦动力 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.30% < 6.00%; excess_return_120d -20.88% < 6.00%; excess_return_240d -45.25% < 8.00%; drawdown_120d -62.26% < -28.00%; volatility_120d 74.42% > 42.00% |
| 600691.SH | 潞化科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.30% < 6.00%; excess_return_120d -20.88% < 6.00%; excess_return_240d -26.04% < 8.00%; drawdown_120d -52.57% < -28.00%; volatility_120d 55.15% > 42.00% |
| 002165.SZ | 红宝丽 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.33% < 6.00%; excess_return_120d -20.91% < 6.00%; excess_return_240d -57.52% < 8.00%; drawdown_120d -57.89% < -28.00%; volatility_120d 73.79% > 42.00% |
| 603421.SH | 鼎信通讯 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.48% < 6.00%; excess_return_120d -21.06% < 6.00%; excess_return_240d -34.81% < 8.00%; drawdown_120d -47.36% < -28.00%; volatility_120d 53.94% > 42.00% |
| 301278.SZ | 快可电子 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -16.74% < 6.00%; excess_return_120d -21.32% < 6.00%; excess_return_240d -41.76% < 8.00%; drawdown_120d -45.87% < -28.00%; volatility_120d 47.99% > 42.00% |
| 688189.SH | 南新制药 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -17.55% < 6.00%; excess_return_120d -21.65% < 6.00%; excess_return_240d -40.69% < 8.00%; drawdown_120d -42.67% < -28.00%; volatility_120d 65.58% > 42.00% |
| 603619.SH | 中曼石油 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.11% < 6.00%; excess_return_120d -21.69% < 6.00%; excess_return_240d -21.74% < 8.00%; drawdown_120d -60.47% < -28.00%; volatility_120d 69.33% > 42.00% |
| 600602.SH | 云赛智联 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.28% < 6.00%; excess_return_120d -21.86% < 6.00%; excess_return_240d -43.82% < 8.00%; drawdown_120d -40.08% < -28.00%; volatility_120d 59.49% > 42.00% |
| 688159.SH | 有方科技 | ok | 18.00 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -17.52% < 6.00%; excess_return_120d -22.10% < 6.00%; excess_return_240d -53.26% < 8.00%; drawdown_120d -45.81% < -28.00%; volatility_120d 67.92% > 42.00% |
| 002092.SZ | 中泰化学 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.87% < 6.00%; excess_return_120d -22.45% < 6.00%; excess_return_240d -33.70% < 8.00%; drawdown_120d -54.45% < -28.00%; volatility_120d 56.62% > 42.00% |
| 688560.SH | 明冠新材 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -17.98% < 6.00%; excess_return_120d -22.56% < 6.00%; excess_return_240d -43.27% < 8.00%; drawdown_120d -51.02% < -28.00%; volatility_120d 62.39% > 42.00% |
| 601226.SH | 华电科工 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.25% < 6.00%; excess_return_120d -22.83% < 6.00%; excess_return_240d -23.87% < 8.00%; drawdown_120d -49.77% < -28.00%; volatility_120d 58.70% > 42.00% |
| 002575.SZ | 群兴玩具 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -18.45% < 6.00%; excess_return_120d -23.03% < 6.00%; excess_return_240d -63.30% < 8.00%; drawdown_120d -47.45% < -28.00%; volatility_120d 70.39% > 42.00% |
| 000912.SZ | 泸天化 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.55% < 6.00%; excess_return_120d -23.13% < 6.00%; excess_return_240d -49.03% < 8.00%; drawdown_120d -49.55% < -28.00%; volatility_120d 52.31% > 42.00% |
| 688032.SH | 禾迈股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.85% < 6.00%; excess_return_120d -23.43% < 6.00%; excess_return_240d -42.66% < 8.00%; drawdown_120d -42.68% < -28.00%; volatility_120d 52.06% > 42.00% |
| 300785.SZ | 值得买 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.05% < 6.00%; excess_return_120d -23.63% < 6.00%; excess_return_240d -6.32% < 8.00%; drawdown_120d -57.80% < -28.00%; volatility_120d 80.12% > 42.00% |
| 301159.SZ | 三维天地 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.17% < 6.00%; excess_return_120d -23.75% < 6.00%; excess_return_240d -31.20% < 8.00%; drawdown_120d -51.90% < -28.00%; volatility_120d 68.06% > 42.00% |
| 300048.SZ | 合康新能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.33% < 6.00%; excess_return_120d -23.91% < 6.00%; excess_return_240d -41.63% < 8.00%; drawdown_120d -45.95% < -28.00%; volatility_120d 43.32% > 42.00% |
| 688599.SH | 天合光能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.46% < 6.00%; excess_return_120d -24.04% < 6.00%; excess_return_240d -36.46% < 8.00%; drawdown_120d -41.20% < -28.00%; volatility_120d 55.27% > 42.00% |
| 001255.SZ | 博菲电气 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.57% < 6.00%; excess_return_120d -24.15% < 6.00%; excess_return_240d -42.07% < 8.00%; drawdown_120d -56.34% < -28.00%; volatility_120d 54.89% > 42.00% |
| 601615.SH | 明阳智能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -18.19% < 6.00%; excess_return_120d -24.19% < 6.00%; excess_return_240d -18.78% < 8.00%; drawdown_120d -57.88% < -28.00%; volatility_120d 61.02% > 42.00% |
| 300279.SZ | 和晶科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.67% < 6.00%; excess_return_120d -24.25% < 6.00%; excess_return_240d -38.59% < 8.00%; drawdown_120d -50.00% < -28.00%; volatility_120d 58.89% > 42.00% |
| 301560.SZ | 众捷汽车 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -19.72% < 6.00%; excess_return_120d -24.30% < 6.00%; excess_return_240d -44.70% < 8.00%; drawdown_120d -45.35% < -28.00%; volatility_120d 54.28% > 42.00% |
| 002857.SZ | 三晖电气 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -19.86% < 6.00%; excess_return_120d -24.45% < 6.00%; excess_return_240d -37.07% < 8.00%; drawdown_120d -39.32% < -28.00%; volatility_120d 53.31% > 42.00% |
| 003042.SZ | 中农联合 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.17% < 6.00%; excess_return_120d -24.75% < 6.00%; excess_return_240d -45.95% < 8.00%; drawdown_120d -54.13% < -28.00%; volatility_120d 56.42% > 42.00% |
| 688393.SH | 安必平 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.22% < 6.00%; excess_return_120d -24.80% < 6.00%; excess_return_240d -56.00% < 8.00%; drawdown_120d -51.57% < -28.00%; volatility_120d 51.02% > 42.00% |
| 300055.SZ | 万邦达 | ok | 18.00 | close_below_ma200; stock_return_120d -20.22% < 6.00%; excess_return_120d -24.80% < 6.00%; excess_return_240d -16.00% < 8.00%; drawdown_120d -50.48% < -28.00%; volatility_120d 53.88% > 42.00% |
| 301388.SZ | 欣灵电气 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.28% < 6.00%; excess_return_120d -24.86% < 6.00%; excess_return_240d -57.60% < 8.00%; drawdown_120d -44.78% < -28.00%; volatility_120d 44.31% > 42.00% |
| 600746.SH | 江苏索普 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.35% < 6.00%; excess_return_120d -24.93% < 6.00%; excess_return_240d -53.20% < 8.00%; drawdown_120d -49.35% < -28.00%; volatility_120d 44.15% > 42.00% |
| 600303.SH | 曙光股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.55% < 6.00%; excess_return_120d -25.13% < 6.00%; excess_return_240d -49.55% < 8.00%; drawdown_120d -35.25% < -28.00%; volatility_120d 45.28% > 42.00% |
| 300991.SZ | 创益通 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.65% < 6.00%; excess_return_120d -25.23% < 6.00%; excess_return_240d -14.13% < 8.00%; drawdown_120d -49.90% < -28.00%; volatility_120d 58.19% > 42.00% |
| 603000.SH | 人民网 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.68% < 6.00%; excess_return_120d -25.26% < 6.00%; excess_return_240d -44.66% < 8.00%; drawdown_120d -50.99% < -28.00%; volatility_120d 56.25% > 42.00% |
| 000995.SZ | 皇台酒业 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.78% < 6.00%; excess_return_120d -25.36% < 6.00%; excess_return_240d -51.50% < 8.00%; drawdown_120d -53.25% < -28.00%; volatility_120d 58.54% > 42.00% |
| 300982.SZ | 苏文电能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -20.80% < 6.00%; excess_return_120d -25.38% < 6.00%; excess_return_240d -50.63% < 8.00%; drawdown_120d -44.21% < -28.00%; volatility_120d 62.92% > 42.00% |
| 300315.SZ | 掌趣科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.85% < 6.00%; excess_return_120d -25.43% < 6.00%; excess_return_240d -54.60% < 8.00%; drawdown_120d -49.87% < -28.00%; volatility_120d 50.92% > 42.00% |
| 688004.SH | 博汇科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.97% < 6.00%; excess_return_120d -25.55% < 6.00%; excess_return_240d -25.89% < 8.00%; drawdown_120d -34.67% < -28.00%; volatility_120d 46.73% > 42.00% |
| 301190.SZ | 善水科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.07% < 6.00%; excess_return_120d -25.66% < 6.00%; excess_return_240d -48.53% < 8.00%; drawdown_120d -37.70% < -28.00%; volatility_120d 42.66% > 42.00% |
| 000020.SZ | 深华发A | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.12% < 6.00%; excess_return_120d -25.70% < 6.00%; excess_return_240d -41.76% < 8.00%; drawdown_120d -57.37% < -28.00%; volatility_120d 50.78% > 42.00% |
| 300004.SZ | 南风股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.22% < 6.00%; excess_return_120d -25.80% < 6.00%; excess_return_240d -4.83% < 8.00%; drawdown_120d -46.63% < -28.00%; volatility_120d 71.37% > 42.00% |
| 688317.SH | 之江生物 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.27% < 6.00%; excess_return_120d -25.85% < 6.00%; excess_return_240d -39.83% < 8.00%; drawdown_120d -44.44% < -28.00%; volatility_120d 52.36% > 42.00% |
| 688223.SH | 晶科能源 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.28% < 6.00%; excess_return_120d -25.86% < 6.00%; excess_return_240d -40.95% < 8.00%; drawdown_120d -54.04% < -28.00%; volatility_120d 70.07% > 42.00% |
| 688552.SH | 航天南湖 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.36% < 6.00%; excess_return_120d -25.94% < 6.00%; excess_return_240d -44.85% < 8.00%; drawdown_120d -47.89% < -28.00%; volatility_120d 71.16% > 42.00% |
| 301266.SZ | 宇邦新材 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.39% < 6.00%; excess_return_120d -25.97% < 6.00%; excess_return_240d -40.68% < 8.00%; drawdown_120d -48.07% < -28.00%; volatility_120d 62.84% > 42.00% |
| 300169.SZ | 天晟新材 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.61% < 6.00%; excess_return_120d -26.10% < 6.00%; excess_return_240d -71.22% < 8.00%; drawdown_120d -37.85% < -28.00%; volatility_120d 42.15% > 42.00% |
| 000822.SZ | 山东海化 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.52% < 6.00%; excess_return_120d -26.10% < 6.00%; excess_return_240d -52.66% < 8.00%; drawdown_120d -45.14% < -28.00%; volatility_120d 48.51% > 42.00% |
| 300454.SZ | 深信服 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.63% < 6.00%; excess_return_120d -26.21% < 6.00%; excess_return_240d -19.65% < 8.00%; drawdown_120d -52.01% < -28.00%; volatility_120d 71.14% > 42.00% |
| 002088.SZ | 鲁阳节能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.83% < 6.00%; excess_return_120d -26.41% < 6.00%; excess_return_240d -45.81% < 8.00%; drawdown_120d -41.67% < -28.00%; volatility_120d 45.46% > 42.00% |
| 300614.SZ | 百川畅银 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.85% < 6.00%; excess_return_120d -26.43% < 6.00%; excess_return_240d -49.75% < 8.00%; drawdown_120d -42.78% < -28.00%; volatility_120d 49.18% > 42.00% |
| 300827.SZ | 上能电气 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -21.85% < 6.00%; excess_return_120d -26.43% < 6.00%; excess_return_240d -10.29% < 8.00%; drawdown_120d -43.27% < -28.00%; volatility_120d 59.62% > 42.00% |
| 002309.SZ | 中利集团 | ok | 18.00 | close_below_ma200; stock_return_120d -22.12% < 6.00%; excess_return_120d -26.70% < 6.00%; excess_return_240d -50.37% < 8.00%; drawdown_120d -51.38% < -28.00%; volatility_120d 66.36% > 42.00% |
| 688118.SH | 普元信息 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.20% < 6.00%; excess_return_120d -26.78% < 6.00%; excess_return_240d -32.16% < 8.00%; drawdown_120d -51.30% < -28.00%; volatility_120d 70.94% > 42.00% |
| 603381.SH | 永臻股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.21% < 6.00%; excess_return_120d -26.79% < 6.00%; excess_return_240d -50.71% < 8.00%; drawdown_120d -52.05% < -28.00%; volatility_120d 56.82% > 42.00% |
| 002663.SZ | 普邦股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.22% < 6.00%; excess_return_120d -26.80% < 6.00%; excess_return_240d -44.53% < 8.00%; drawdown_120d -40.73% < -28.00%; volatility_120d 51.49% > 42.00% |
| 301141.SZ | 中科磁业 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.34% < 6.00%; excess_return_120d -26.92% < 6.00%; excess_return_240d -59.35% < 8.00%; drawdown_120d -43.33% < -28.00%; volatility_120d 57.93% > 42.00% |
| 600503.SH | 华丽家族 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.39% < 6.00%; excess_return_120d -26.97% < 6.00%; excess_return_240d -42.01% < 8.00%; drawdown_120d -32.25% < -28.00%; volatility_120d 45.80% > 42.00% |
| 300153.SZ | 科泰电源 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.41% < 6.00%; excess_return_120d -26.99% < 6.00%; excess_return_240d -52.14% < 8.00%; drawdown_120d -45.56% < -28.00%; volatility_120d 60.98% > 42.00% |
| 688085.SH | 三友医疗 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.45% < 6.00%; excess_return_120d -27.03% < 6.00%; excess_return_240d -34.05% < 8.00%; drawdown_120d -41.42% < -28.00%; volatility_120d 50.34% > 42.00% |
| 600868.SH | 梅雁吉祥 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.46% < 6.00%; excess_return_120d -27.04% < 6.00%; excess_return_240d -32.40% < 8.00%; drawdown_120d -52.30% < -28.00%; volatility_120d 58.15% > 42.00% |
| 603322.SH | 超讯通信 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.55% < 6.00%; excess_return_120d -27.13% < 6.00%; excess_return_240d -43.30% < 8.00%; drawdown_120d -30.67% < -28.00%; volatility_120d 50.71% > 42.00% |
| 688058.SH | 宝兰德 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.59% < 6.00%; excess_return_120d -27.17% < 6.00%; excess_return_240d -45.89% < 8.00%; drawdown_120d -38.69% < -28.00%; volatility_120d 42.78% > 42.00% |
| 002339.SZ | 积成电子 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.61% < 6.00%; excess_return_120d -27.19% < 6.00%; excess_return_240d -38.65% < 8.00%; drawdown_120d -49.67% < -28.00%; volatility_120d 59.29% > 42.00% |
| 000607.SZ | 华媒控股 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.65% < 6.00%; excess_return_120d -27.23% < 6.00%; excess_return_240d -56.25% < 8.00%; drawdown_120d -43.39% < -28.00%; volatility_120d 44.70% > 42.00% |
| 300253.SZ | 卫宁健康 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.68% < 6.00%; excess_return_120d -27.26% < 6.00%; excess_return_240d -52.97% < 8.00%; drawdown_120d -57.61% < -28.00%; volatility_120d 60.01% > 42.00% |
| 300603.SZ | 立昂技术 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.74% < 6.00%; excess_return_120d -27.32% < 6.00%; excess_return_240d -54.16% < 8.00%; drawdown_120d -40.40% < -28.00%; volatility_120d 55.54% > 42.00% |
| 601360.SH | 三六零 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.76% < 6.00%; excess_return_120d -27.34% < 6.00%; excess_return_240d -34.03% < 8.00%; drawdown_120d -41.36% < -28.00%; volatility_120d 43.66% > 42.00% |
| 600468.SH | 百利电气 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -22.82% < 6.00%; excess_return_120d -27.40% < 6.00%; excess_return_240d -46.03% < 8.00%; drawdown_120d -47.31% < -28.00%; volatility_120d 51.62% > 42.00% |
| 600645.SH | 中源协和 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.86% < 6.00%; excess_return_120d -27.44% < 6.00%; excess_return_240d -48.42% < 8.00%; drawdown_120d -41.07% < -28.00%; volatility_120d 42.16% > 42.00% |
| 301268.SZ | 铭利达 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.87% < 6.00%; excess_return_120d -27.45% < 6.00%; excess_return_240d -48.51% < 8.00%; drawdown_120d -47.85% < -28.00%; volatility_120d 53.08% > 42.00% |
| 600751.SH | 海航科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -22.88% < 6.00%; excess_return_120d -27.46% < 6.00%; excess_return_240d -41.03% < 8.00%; drawdown_120d -33.36% < -28.00%; volatility_120d 42.17% > 42.00% |
| 301022.SZ | 海泰科 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -21.80% < 6.00%; excess_return_120d -27.52% < 6.00%; excess_return_240d -53.40% < 8.00%; drawdown_120d -39.91% < -28.00%; volatility_120d 57.27% > 42.00% |
| 000031.SZ | 大悦城 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.05% < 6.00%; excess_return_120d -27.63% < 6.00%; excess_return_240d -43.60% < 8.00%; drawdown_120d -47.07% < -28.00%; volatility_120d 45.00% > 42.00% |
| 301231.SZ | 荣信文化 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.17% < 6.00%; excess_return_120d -27.75% < 6.00%; excess_return_240d -17.09% < 8.00%; drawdown_120d -60.74% < -28.00%; volatility_120d 90.41% > 42.00% |
| 300232.SZ | 洲明科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.20% < 6.00%; excess_return_120d -27.78% < 6.00%; excess_return_240d -43.75% < 8.00%; drawdown_120d -38.37% < -28.00%; volatility_120d 44.62% > 42.00% |
| 300565.SZ | 科信技术 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.24% < 6.00%; excess_return_120d -27.82% < 6.00%; excess_return_240d -44.27% < 8.00%; drawdown_120d -40.58% < -28.00%; volatility_120d 45.92% > 42.00% |
| 603105.SH | 芯能科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.25% < 6.00%; excess_return_120d -27.83% < 6.00%; excess_return_240d -38.26% < 8.00%; drawdown_120d -51.48% < -28.00%; volatility_120d 45.81% > 42.00% |
| 600603.SH | 广汇物流 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.31% < 6.00%; excess_return_120d -27.89% < 6.00%; excess_return_240d -58.93% < 8.00%; drawdown_120d -42.32% < -28.00%; volatility_120d 44.74% > 42.00% |
| 603098.SH | 森特股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.32% < 6.00%; excess_return_120d -27.90% < 6.00%; excess_return_240d -19.37% < 8.00%; drawdown_120d -42.94% < -28.00%; volatility_120d 42.83% > 42.00% |
| 301001.SZ | 凯淳股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.32% < 6.00%; excess_return_120d -27.90% < 6.00%; excess_return_240d -48.83% < 8.00%; drawdown_120d -47.18% < -28.00%; volatility_120d 59.79% > 42.00% |
| 300170.SZ | 汉得信息 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.46% < 6.00%; excess_return_120d -28.04% < 6.00%; excess_return_240d -33.11% < 8.00%; drawdown_120d -57.04% < -28.00%; volatility_120d 74.78% > 42.00% |
| 002395.SZ | 双象股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.53% < 6.00%; excess_return_120d -28.11% < 6.00%; excess_return_240d -55.09% < 8.00%; drawdown_120d -39.81% < -28.00%; volatility_120d 49.69% > 42.00% |
| 300378.SZ | 鼎捷数智 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.65% < 6.00%; excess_return_120d -28.23% < 6.00%; excess_return_240d -20.35% < 8.00%; drawdown_120d -51.91% < -28.00%; volatility_120d 60.79% > 42.00% |
| 600880.SH | 博瑞传播 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.68% < 6.00%; excess_return_120d -28.26% < 6.00%; excess_return_240d -52.30% < 8.00%; drawdown_120d -51.85% < -28.00%; volatility_120d 46.75% > 42.00% |
| 001234.SZ | 泰慕士 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.74% < 6.00%; excess_return_120d -28.32% < 6.00%; excess_return_240d -23.44% < 8.00%; drawdown_120d -46.17% < -28.00%; volatility_120d 45.31% > 42.00% |
| 300891.SZ | 惠云钛业 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.75% < 6.00%; excess_return_120d -28.33% < 6.00%; excess_return_240d -50.47% < 8.00%; drawdown_120d -39.98% < -28.00%; volatility_120d 42.44% > 42.00% |
| 603585.SH | 苏利股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -23.81% < 6.00%; excess_return_120d -28.39% < 6.00%; excess_return_240d -52.77% < 8.00%; drawdown_120d -47.63% < -28.00%; volatility_120d 51.35% > 42.00% |
| 600158.SH | 中体产业 | ok | 18.00 | close_below_ma200; stock_return_120d -23.83% < 6.00%; excess_return_120d -28.41% < 6.00%; excess_return_240d -42.02% < 8.00%; drawdown_120d -55.34% < -28.00%; volatility_120d 60.27% > 42.00% |
| 300339.SZ | 润和软件 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.85% < 6.00%; excess_return_120d -28.43% < 6.00%; excess_return_240d -45.52% < 8.00%; drawdown_120d -38.02% < -28.00%; volatility_120d 50.71% > 42.00% |
| 002712.SZ | 思美传媒 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -23.92% < 6.00%; excess_return_120d -28.50% < 6.00%; excess_return_240d -49.28% < 8.00%; drawdown_120d -45.56% < -28.00%; volatility_120d 45.63% > 42.00% |
| 601155.SH | 新城控股 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.01% < 6.00%; excess_return_120d -28.59% < 6.00%; excess_return_240d -45.38% < 8.00%; drawdown_120d -42.23% < -28.00%; volatility_120d 43.56% > 42.00% |
| 688349.SH | 三一重能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.06% < 6.00%; excess_return_120d -28.64% < 6.00%; excess_return_240d -43.16% < 8.00%; drawdown_120d -39.00% < -28.00%; volatility_120d 42.70% > 42.00% |
| 688339.SH | 亿华通 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.07% < 6.00%; excess_return_120d -28.65% < 6.00%; excess_return_240d -27.41% < 8.00%; drawdown_120d -43.11% < -28.00%; volatility_120d 57.04% > 42.00% |
| 300913.SZ | 兆龙互连 | ok | 18.00 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -24.11% < 6.00%; excess_return_120d -28.69% < 6.00%; excess_return_240d -38.35% < 8.00%; drawdown_120d -39.92% < -28.00%; volatility_120d 59.36% > 42.00% |
| 300634.SZ | 彩讯股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -24.14% < 6.00%; excess_return_120d -28.72% < 6.00%; excess_return_240d -47.88% < 8.00%; drawdown_120d -47.66% < -28.00%; volatility_120d 67.13% > 42.00% |
| 002574.SZ | 明牌珠宝 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.20% < 6.00%; excess_return_120d -28.78% < 6.00%; excess_return_240d -51.03% < 8.00%; drawdown_120d -44.60% < -28.00%; volatility_120d 44.91% > 42.00% |
| 600540.SH | 新赛股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.29% < 6.00%; excess_return_120d -28.87% < 6.00%; excess_return_240d -55.19% < 8.00%; drawdown_120d -42.24% < -28.00%; volatility_120d 48.61% > 42.00% |
| 601908.SH | 京运通 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.30% < 6.00%; excess_return_120d -28.88% < 6.00%; excess_return_240d -38.87% < 8.00%; drawdown_120d -44.67% < -28.00%; volatility_120d 52.16% > 42.00% |
| 300332.SZ | 天壕能源 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -20.07% < 6.00%; excess_return_120d -28.93% < 6.00%; excess_return_240d -42.01% < 8.00%; drawdown_120d -45.22% < -28.00%; volatility_120d 56.55% > 42.00% |
| 603177.SH | 德创环保 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.44% < 6.00%; excess_return_120d -29.02% < 6.00%; excess_return_240d -29.78% < 8.00%; drawdown_120d -37.24% < -28.00%; volatility_120d 47.96% > 42.00% |
| 300987.SZ | 川网传媒 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.48% < 6.00%; excess_return_120d -29.06% < 6.00%; excess_return_240d -55.96% < 8.00%; drawdown_120d -52.69% < -28.00%; volatility_120d 57.93% > 42.00% |
| 300141.SZ | 和顺电气 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -24.50% < 6.00%; excess_return_120d -29.08% < 6.00%; excess_return_240d -21.93% < 8.00%; drawdown_120d -55.24% < -28.00%; volatility_120d 59.67% > 42.00% |
| 300830.SZ | 金现代 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -24.56% < 6.00%; excess_return_120d -29.14% < 6.00%; excess_return_240d -36.24% < 8.00%; drawdown_120d -51.61% < -28.00%; volatility_120d 72.22% > 42.00% |
| 002366.SZ | 融发核电 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.63% < 6.00%; excess_return_120d -29.21% < 6.00%; excess_return_240d -61.64% < 8.00%; drawdown_120d -40.79% < -28.00%; volatility_120d 44.62% > 42.00% |
| 002973.SZ | 侨银股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.80% < 6.00%; excess_return_120d -29.38% < 6.00%; excess_return_240d -45.56% < 8.00%; drawdown_120d -35.75% < -28.00%; volatility_120d 42.63% > 42.00% |
| 600208.SH | 衢州发展 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.81% < 6.00%; excess_return_120d -29.39% < 6.00%; excess_return_240d -18.21% < 8.00%; drawdown_120d -47.19% < -28.00%; volatility_120d 58.07% > 42.00% |
| 300457.SZ | 赢合科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.85% < 6.00%; excess_return_120d -29.43% < 6.00%; excess_return_240d -22.67% < 8.00%; drawdown_120d -33.72% < -28.00%; volatility_120d 43.81% > 42.00% |
| 300231.SZ | 银信科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.86% < 6.00%; excess_return_120d -29.44% < 6.00%; excess_return_240d -56.42% < 8.00%; drawdown_120d -38.58% < -28.00%; volatility_120d 48.83% > 42.00% |
| 600569.SH | 安阳钢铁 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.89% < 6.00%; excess_return_120d -29.47% < 6.00%; excess_return_240d -43.57% < 8.00%; drawdown_120d -40.70% < -28.00%; volatility_120d 43.16% > 42.00% |
| 300887.SZ | 谱尼测试 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -24.90% < 6.00%; excess_return_120d -29.48% < 6.00%; excess_return_240d -38.41% < 8.00%; drawdown_120d -57.06% < -28.00%; volatility_120d 67.49% > 42.00% |
| 688429.SH | 时创能源 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -24.98% < 6.00%; excess_return_120d -29.56% < 6.00%; excess_return_240d -55.72% < 8.00%; drawdown_120d -48.34% < -28.00%; volatility_120d 56.16% > 42.00% |
| 002291.SZ | 遥望科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.04% < 6.00%; excess_return_120d -29.62% < 6.00%; excess_return_240d -46.49% < 8.00%; drawdown_120d -47.01% < -28.00%; volatility_120d 51.11% > 42.00% |
| 600586.SH | 金晶科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.04% < 6.00%; excess_return_120d -29.62% < 6.00%; excess_return_240d -42.80% < 8.00%; drawdown_120d -47.05% < -28.00%; volatility_120d 55.96% > 42.00% |
| 300092.SZ | 科新机电 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.05% < 6.00%; excess_return_120d -29.63% < 6.00%; excess_return_240d -35.63% < 8.00%; drawdown_120d -42.49% < -28.00%; volatility_120d 42.25% > 42.00% |
| 002478.SZ | 常宝股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.05% < 6.00%; excess_return_120d -29.63% < 6.00%; excess_return_240d -4.38% < 8.00%; drawdown_120d -54.65% < -28.00%; volatility_120d 61.66% > 42.00% |
| 300520.SZ | 科大国创 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.08% < 6.00%; excess_return_120d -29.66% < 6.00%; excess_return_240d -12.99% < 8.00%; drawdown_120d -52.70% < -28.00%; volatility_120d 74.33% > 42.00% |
| 002692.SZ | 远程股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.10% < 6.00%; excess_return_120d -29.68% < 6.00%; excess_return_240d -45.75% < 8.00%; drawdown_120d -47.65% < -28.00%; volatility_120d 49.68% > 42.00% |
| 300118.SZ | 东方日升 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.10% < 6.00%; excess_return_120d -29.68% < 6.00%; excess_return_240d -17.51% < 8.00%; drawdown_120d -57.75% < -28.00%; volatility_120d 72.75% > 42.00% |
| 688793.SH | 倍轻松 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.18% < 6.00%; excess_return_120d -29.76% < 6.00%; excess_return_240d -70.08% < 8.00%; drawdown_120d -43.52% < -28.00%; volatility_120d 52.43% > 42.00% |
| 301010.SZ | 晶雪节能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.28% < 6.00%; excess_return_120d -29.86% < 6.00%; excess_return_240d -32.12% < 8.00%; drawdown_120d -33.27% < -28.00%; volatility_120d 44.44% > 42.00% |
| 300226.SZ | 上海钢联 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.28% < 6.00%; excess_return_120d -29.86% < 6.00%; excess_return_240d -39.97% < 8.00%; drawdown_120d -43.93% < -28.00%; volatility_120d 50.94% > 42.00% |
| 002161.SZ | 远望谷 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.31% < 6.00%; excess_return_120d -29.89% < 6.00%; excess_return_240d -35.78% < 8.00%; drawdown_120d -41.67% < -28.00%; volatility_120d 49.28% > 42.00% |
| 601515.SH | 衢州东峰 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.35% < 6.00%; excess_return_120d -29.93% < 6.00%; excess_return_240d -41.64% < 8.00%; drawdown_120d -38.27% < -28.00%; volatility_120d 48.85% > 42.00% |
| 688613.SH | 奥精医疗 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.41% < 6.00%; excess_return_120d -29.99% < 6.00%; excess_return_240d -38.49% < 8.00%; drawdown_120d -41.93% < -28.00%; volatility_120d 45.26% > 42.00% |
| 000712.SZ | 锦龙股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.62% < 6.00%; excess_return_120d -30.20% < 6.00%; excess_return_240d -52.01% < 8.00%; drawdown_120d -33.03% < -28.00%; volatility_120d 44.34% > 42.00% |
| 300047.SZ | 天源迪科 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.73% < 6.00%; excess_return_120d -30.31% < 6.00%; excess_return_240d -63.32% < 8.00%; drawdown_120d -44.86% < -28.00%; volatility_120d 54.63% > 42.00% |
| 300582.SZ | 英飞特 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.74% < 6.00%; excess_return_120d -30.32% < 6.00%; excess_return_240d -26.97% < 8.00%; drawdown_120d -40.70% < -28.00%; volatility_120d 59.25% > 42.00% |
| 300809.SZ | 华辰装备 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.74% < 6.00%; excess_return_120d -30.32% < 6.00%; excess_return_240d -39.49% < 8.00%; drawdown_120d -35.01% < -28.00%; volatility_120d 57.13% > 42.00% |
| 603999.SH | 读者传媒 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.75% < 6.00%; excess_return_120d -30.33% < 6.00%; excess_return_240d -42.95% < 8.00%; drawdown_120d -41.28% < -28.00%; volatility_120d 43.00% > 42.00% |
| 603239.SH | 浙江仙通 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.78% < 6.00%; excess_return_120d -30.36% < 6.00%; excess_return_240d -22.41% < 8.00%; drawdown_120d -42.84% < -28.00%; volatility_120d 47.74% > 42.00% |
| 603612.SH | 索通发展 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.79% < 6.00%; excess_return_120d -30.37% < 6.00%; excess_return_240d -25.77% < 8.00%; drawdown_120d -52.11% < -28.00%; volatility_120d 52.04% > 42.00% |
| 600604.SH | 市北高新 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.81% < 6.00%; excess_return_120d -30.39% < 6.00%; excess_return_240d -39.55% < 8.00%; drawdown_120d -35.38% < -28.00%; volatility_120d 42.06% > 42.00% |
| 300615.SZ | 欣天科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.85% < 6.00%; excess_return_120d -30.43% < 6.00%; excess_return_240d -48.05% < 8.00%; drawdown_120d -43.59% < -28.00%; volatility_120d 45.33% > 42.00% |
| 603282.SH | 亚光股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.86% < 6.00%; excess_return_120d -30.44% < 6.00%; excess_return_240d -36.42% < 8.00%; drawdown_120d -39.85% < -28.00%; volatility_120d 42.59% > 42.00% |
| 603829.SH | 洛凯股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -25.91% < 6.00%; excess_return_120d -30.49% < 6.00%; excess_return_240d -25.40% < 8.00%; drawdown_120d -46.87% < -28.00%; volatility_120d 56.27% > 42.00% |
| 300080.SZ | 易成新能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -25.93% < 6.00%; excess_return_120d -30.51% < 6.00%; excess_return_240d -37.96% < 8.00%; drawdown_120d -46.90% < -28.00%; volatility_120d 50.92% > 42.00% |
| 000525.SZ | 红太阳 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.01% < 6.00%; excess_return_120d -30.59% < 6.00%; excess_return_240d -65.53% < 8.00%; drawdown_120d -46.13% < -28.00%; volatility_120d 46.70% > 42.00% |
| 000856.SZ | 冀东装备 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.03% < 6.00%; excess_return_120d -30.61% < 6.00%; excess_return_240d -51.48% < 8.00%; drawdown_120d -40.33% < -28.00%; volatility_120d 45.18% > 42.00% |
| 300875.SZ | 捷强装备 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.06% < 6.00%; excess_return_120d -30.64% < 6.00%; excess_return_240d -53.54% < 8.00%; drawdown_120d -48.38% < -28.00%; volatility_120d 52.67% > 42.00% |
| 300369.SZ | 绿盟科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.07% < 6.00%; excess_return_120d -30.65% < 6.00%; excess_return_240d -50.47% < 8.00%; drawdown_120d -53.53% < -28.00%; volatility_120d 54.17% > 42.00% |
| 300584.SZ | 海辰药业 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.14% < 6.00%; excess_return_120d -30.72% < 6.00%; excess_return_240d -18.38% < 8.00%; drawdown_120d -35.70% < -28.00%; volatility_120d 55.54% > 42.00% |
| 300753.SZ | 爱朋医疗 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -26.16% < 6.00%; excess_return_120d -30.74% < 6.00%; excess_return_240d -57.34% < 8.00%; drawdown_120d -53.56% < -28.00%; volatility_120d 66.61% > 42.00% |
| 300902.SZ | 国安达 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.16% < 6.00%; excess_return_120d -30.74% < 6.00%; excess_return_240d -41.20% < 8.00%; drawdown_120d -34.44% < -28.00%; volatility_120d 46.49% > 42.00% |
| 600831.SH | 广电网络 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.19% < 6.00%; excess_return_120d -30.77% < 6.00%; excess_return_240d -46.13% < 8.00%; drawdown_120d -36.73% < -28.00%; volatility_120d 43.99% > 42.00% |
| 002513.SZ | 蓝丰生化 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.19% < 6.00%; excess_return_120d -30.77% < 6.00%; excess_return_240d -31.08% < 8.00%; drawdown_120d -37.22% < -28.00%; volatility_120d 44.55% > 42.00% |
| 300563.SZ | 神宇股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.21% < 6.00%; excess_return_120d -30.79% < 6.00%; excess_return_240d -55.33% < 8.00%; drawdown_120d -39.36% < -28.00%; volatility_120d 54.93% > 42.00% |
| 688501.SH | 青达环保 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.26% < 6.00%; excess_return_120d -30.84% < 6.00%; excess_return_240d -51.61% < 8.00%; drawdown_120d -36.10% < -28.00%; volatility_120d 49.81% > 42.00% |
| 688369.SH | 致远互联 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.27% < 6.00%; excess_return_120d -30.85% < 6.00%; excess_return_240d -45.06% < 8.00%; drawdown_120d -47.80% < -28.00%; volatility_120d 54.57% > 42.00% |
| 002672.SZ | 东江环保 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.41% < 6.00%; excess_return_120d -30.99% < 6.00%; excess_return_240d -50.12% < 8.00%; drawdown_120d -34.87% < -28.00%; volatility_120d 47.36% > 42.00% |
| 002858.SZ | 力盛体育 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.47% < 6.00%; excess_return_120d -31.05% < 6.00%; excess_return_240d -37.15% < 8.00%; drawdown_120d -38.62% < -28.00%; volatility_120d 47.57% > 42.00% |
| 600774.SH | 汉商集团 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.48% < 6.00%; excess_return_120d -31.06% < 6.00%; excess_return_240d -45.34% < 8.00%; drawdown_120d -42.27% < -28.00%; volatility_120d 45.97% > 42.00% |
| 301180.SZ | 万祥科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -26.59% < 6.00%; excess_return_120d -31.17% < 6.00%; excess_return_240d -38.54% < 8.00%; drawdown_120d -47.70% < -28.00%; volatility_120d 49.08% > 42.00% |
| 600481.SH | 双良节能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -26.61% < 6.00%; excess_return_120d -31.19% < 6.00%; excess_return_240d -39.33% < 8.00%; drawdown_120d -58.48% < -28.00%; volatility_120d 72.09% > 42.00% |
| 300713.SZ | 英可瑞 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.71% < 6.00%; excess_return_120d -31.29% < 6.00%; excess_return_240d -54.54% < 8.00%; drawdown_120d -38.18% < -28.00%; volatility_120d 42.53% > 42.00% |
| 300775.SZ | 三角防务 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -26.77% < 6.00%; excess_return_120d -31.35% < 6.00%; excess_return_240d -35.32% < 8.00%; drawdown_120d -54.89% < -28.00%; volatility_120d 68.29% > 42.00% |
| 002809.SZ | 红墙股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.82% < 6.00%; excess_return_120d -31.40% < 6.00%; excess_return_240d -60.88% < 8.00%; drawdown_120d -51.26% < -28.00%; volatility_120d 58.93% > 42.00% |
| 300781.SZ | 因赛集团 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.88% < 6.00%; excess_return_120d -31.46% < 6.00%; excess_return_240d -48.65% < 8.00%; drawdown_120d -56.20% < -28.00%; volatility_120d 65.42% > 42.00% |
| 688573.SH | 信宇人 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -26.90% < 6.00%; excess_return_120d -31.48% < 6.00%; excess_return_240d -65.49% < 8.00%; drawdown_120d -35.43% < -28.00%; volatility_120d 47.55% > 42.00% |
| 002160.SZ | 常铝股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.06% < 6.00%; excess_return_120d -31.55% < 6.00%; excess_return_240d -36.70% < 8.00%; drawdown_120d -50.07% < -28.00%; volatility_120d 58.21% > 42.00% |
| 601608.SH | 中信重工 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.01% < 6.00%; excess_return_120d -31.59% < 6.00%; excess_return_240d -11.80% < 8.00%; drawdown_120d -43.28% < -28.00%; volatility_120d 42.15% > 42.00% |
| 000799.SZ | 酒鬼酒 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.06% < 6.00%; excess_return_120d -31.64% < 6.00%; excess_return_240d -32.98% < 8.00%; drawdown_120d -35.27% < -28.00%; volatility_120d 44.61% > 42.00% |
| 603037.SH | 凯众股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.07% < 6.00%; excess_return_120d -31.65% < 6.00%; excess_return_240d -35.63% < 8.00%; drawdown_120d -48.72% < -28.00%; volatility_120d 55.80% > 42.00% |
| 688579.SH | 地纬智能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.31% < 6.00%; excess_return_120d -31.89% < 6.00%; excess_return_240d -52.37% < 8.00%; drawdown_120d -41.96% < -28.00%; volatility_120d 43.69% > 42.00% |
| 688232.SH | 新点软件 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.31% < 6.00%; excess_return_120d -31.89% < 6.00%; excess_return_240d -59.96% < 8.00%; drawdown_120d -49.74% < -28.00%; volatility_120d 44.66% > 42.00% |
| 002285.SZ | 世联行 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.37% < 6.00%; excess_return_120d -31.95% < 6.00%; excess_return_240d -35.91% < 8.00%; drawdown_120d -43.60% < -28.00%; volatility_120d 46.01% > 42.00% |
| 600126.SH | 杭钢股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.41% < 6.00%; excess_return_120d -31.99% < 6.00%; excess_return_240d -59.27% < 8.00%; drawdown_120d -47.21% < -28.00%; volatility_120d 57.30% > 42.00% |
| 002467.SZ | 二六三 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.42% < 6.00%; excess_return_120d -32.00% < 6.00%; excess_return_240d -53.92% < 8.00%; drawdown_120d -45.36% < -28.00%; volatility_120d 58.52% > 42.00% |
| 002420.SZ | 毅昌科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.44% < 6.00%; excess_return_120d -32.02% < 6.00%; excess_return_240d -35.24% < 8.00%; drawdown_120d -38.68% < -28.00%; volatility_120d 43.48% > 42.00% |
| 300471.SZ | 厚普股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.46% < 6.00%; excess_return_120d -32.04% < 6.00%; excess_return_240d -33.63% < 8.00%; drawdown_120d -46.77% < -28.00%; volatility_120d 46.49% > 42.00% |
| 603630.SH | 拉芳家化 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.58% < 6.00%; excess_return_120d -32.16% < 6.00%; excess_return_240d -53.82% < 8.00%; drawdown_120d -42.92% < -28.00%; volatility_120d 44.54% > 42.00% |
| 600435.SH | 北方导航 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.64% < 6.00%; excess_return_120d -32.22% < 6.00%; excess_return_240d -41.95% < 8.00%; drawdown_120d -50.54% < -28.00%; volatility_120d 47.97% > 42.00% |
| 601116.SH | 三江购物 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.65% < 6.00%; excess_return_120d -32.23% < 6.00%; excess_return_240d -32.64% < 8.00%; drawdown_120d -56.76% < -28.00%; volatility_120d 56.39% > 42.00% |
| 688208.SH | 道通科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.69% < 6.00%; excess_return_120d -32.27% < 6.00%; excess_return_240d -38.26% < 8.00%; drawdown_120d -37.72% < -28.00%; volatility_120d 45.49% > 42.00% |
| 301062.SZ | 上海艾录 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.72% < 6.00%; excess_return_120d -32.30% < 6.00%; excess_return_240d -52.42% < 8.00%; drawdown_120d -43.83% < -28.00%; volatility_120d 45.16% > 42.00% |
| 000560.SZ | 我爱我家 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.74% < 6.00%; excess_return_120d -32.32% < 6.00%; excess_return_240d -52.37% < 8.00%; drawdown_120d -42.19% < -28.00%; volatility_120d 44.13% > 42.00% |
| 300933.SZ | 中辰股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.74% < 6.00%; excess_return_120d -32.32% < 6.00%; excess_return_240d -43.61% < 8.00%; drawdown_120d -40.69% < -28.00%; volatility_120d 45.50% > 42.00% |
| 002677.SZ | 浙江美大 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.77% < 6.00%; excess_return_120d -32.35% < 6.00%; excess_return_240d -35.76% < 8.00%; drawdown_120d -42.25% < -28.00%; volatility_120d 48.87% > 42.00% |
| 002624.SZ | 完美世界 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -27.77% < 6.00%; excess_return_120d -32.35% < 6.00%; excess_return_240d -43.19% < 8.00%; drawdown_120d -50.32% < -28.00%; volatility_120d 59.97% > 42.00% |
| 600876.SH | 凯盛新能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.89% < 6.00%; excess_return_120d -32.47% < 6.00%; excess_return_240d -66.82% < 8.00%; drawdown_120d -39.13% < -28.00%; volatility_120d 48.08% > 42.00% |
| 300600.SZ | 国瑞科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -27.99% < 6.00%; excess_return_120d -32.57% < 6.00%; excess_return_240d -52.23% < 8.00%; drawdown_120d -34.89% < -28.00%; volatility_120d 44.50% > 42.00% |
| 301505.SZ | 苏州规划 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.02% < 6.00%; excess_return_120d -32.60% < 6.00%; excess_return_240d -44.68% < 8.00%; drawdown_120d -46.83% < -28.00%; volatility_120d 43.00% > 42.00% |
| 301100.SZ | 风光股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.06% < 6.00%; excess_return_120d -32.64% < 6.00%; excess_return_240d -35.50% < 8.00%; drawdown_120d -39.02% < -28.00%; volatility_120d 45.05% > 42.00% |
| 603716.SH | 塞力医疗 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.08% < 6.00%; excess_return_120d -32.66% < 6.00%; excess_return_240d -51.35% < 8.00%; drawdown_120d -53.61% < -28.00%; volatility_120d 54.87% > 42.00% |
| 002405.SZ | 四维图新 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -28.30% < 6.00%; excess_return_120d -32.88% < 6.00%; excess_return_240d -43.17% < 8.00%; drawdown_120d -44.93% < -28.00%; volatility_120d 43.31% > 42.00% |
| 300380.SZ | 安硕信息 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.35% < 6.00%; excess_return_120d -32.93% < 6.00%; excess_return_240d -59.56% < 8.00%; drawdown_120d -38.72% < -28.00%; volatility_120d 42.63% > 42.00% |
| 002314.SZ | 南山控股 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.42% < 6.00%; excess_return_120d -33.00% < 6.00%; excess_return_240d -59.84% < 8.00%; drawdown_120d -35.44% < -28.00%; volatility_120d 44.40% > 42.00% |
| 300287.SZ | 飞利信 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.43% < 6.00%; excess_return_120d -33.01% < 6.00%; excess_return_240d -59.80% < 8.00%; drawdown_120d -42.24% < -28.00%; volatility_120d 52.16% > 42.00% |
| 003038.SZ | 鑫铂股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.48% < 6.00%; excess_return_120d -33.06% < 6.00%; excess_return_240d -58.94% < 8.00%; drawdown_120d -41.81% < -28.00%; volatility_120d 43.49% > 42.00% |
| 300365.SZ | 恒华科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.48% < 6.00%; excess_return_120d -33.06% < 6.00%; excess_return_240d -53.23% < 8.00%; drawdown_120d -38.67% < -28.00%; volatility_120d 42.32% > 42.00% |
| 002031.SZ | 巨轮智能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.50% < 6.00%; excess_return_120d -33.08% < 6.00%; excess_return_240d -49.96% < 8.00%; drawdown_120d -36.28% < -28.00%; volatility_120d 56.17% > 42.00% |
| 688136.SH | 科兴制药 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.59% < 6.00%; excess_return_120d -33.17% < 6.00%; excess_return_240d -67.22% < 8.00%; drawdown_120d -38.10% < -28.00%; volatility_120d 56.08% > 42.00% |
| 600556.SH | 天下秀 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -28.61% < 6.00%; excess_return_120d -33.19% < 6.00%; excess_return_240d -34.58% < 8.00%; drawdown_120d -54.16% < -28.00%; volatility_120d 55.32% > 42.00% |
| 000710.SZ | 贝瑞基因 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.70% < 6.00%; excess_return_120d -33.28% < 6.00%; excess_return_240d -64.72% < 8.00%; drawdown_120d -48.50% < -28.00%; volatility_120d 45.96% > 42.00% |
| 300837.SZ | 浙矿股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -28.74% < 6.00%; excess_return_120d -33.32% < 6.00%; excess_return_240d -20.22% < 8.00%; drawdown_120d -64.72% < -28.00%; volatility_120d 75.32% > 42.00% |
| 000006.SZ | 深振业A | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.74% < 6.00%; excess_return_120d -33.32% < 6.00%; excess_return_240d -10.66% < 8.00%; drawdown_120d -36.98% < -28.00%; volatility_120d 48.83% > 42.00% |
| 300448.SZ | 浩云科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -28.83% < 6.00%; excess_return_120d -33.41% < 6.00%; excess_return_240d -37.07% < 8.00%; drawdown_120d -51.41% < -28.00%; volatility_120d 63.21% > 42.00% |
| 688023.SH | 安恒信息 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.87% < 6.00%; excess_return_120d -33.45% < 6.00%; excess_return_240d -51.01% < 8.00%; drawdown_120d -45.07% < -28.00%; volatility_120d 54.14% > 42.00% |
| 002453.SZ | 华软科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -28.91% < 6.00%; excess_return_120d -33.49% < 6.00%; excess_return_240d -45.59% < 8.00%; drawdown_120d -33.82% < -28.00%; volatility_120d 48.29% > 42.00% |
| 600399.SH | 抚顺特钢 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -28.94% < 6.00%; excess_return_120d -33.52% < 6.00%; excess_return_240d -41.69% < 8.00%; drawdown_120d -49.76% < -28.00%; volatility_120d 46.88% > 42.00% |
| 603655.SH | 朗博科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -28.95% < 6.00%; excess_return_120d -33.53% < 6.00%; excess_return_240d -17.95% < 8.00%; drawdown_120d -42.85% < -28.00%; volatility_120d 60.18% > 42.00% |
| 300690.SZ | 双一科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.07% < 6.00%; excess_return_120d -33.65% < 6.00%; excess_return_240d -25.19% < 8.00%; drawdown_120d -44.87% < -28.00%; volatility_120d 50.47% > 42.00% |
| 300995.SZ | 奇德新材 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.08% < 6.00%; excess_return_120d -33.66% < 6.00%; excess_return_240d -54.64% < 8.00%; drawdown_120d -35.32% < -28.00%; volatility_120d 43.52% > 42.00% |
| 600654.SH | 中安科 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.18% < 6.00%; excess_return_120d -33.76% < 6.00%; excess_return_240d -31.80% < 8.00%; drawdown_120d -44.83% < -28.00%; volatility_120d 51.88% > 42.00% |
| 000798.SZ | 中水渔业 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -29.21% < 6.00%; excess_return_120d -33.79% < 6.00%; excess_return_240d -24.33% < 8.00%; drawdown_120d -41.85% < -28.00%; volatility_120d 44.65% > 42.00% |
| 002355.SZ | 兴民智通 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -29.21% < 6.00%; excess_return_120d -33.79% < 6.00%; excess_return_240d -65.16% < 8.00%; drawdown_120d -46.31% < -28.00%; volatility_120d 50.74% > 42.00% |
| 603113.SH | 金能科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.23% < 6.00%; excess_return_120d -33.81% < 6.00%; excess_return_240d -59.87% < 8.00%; drawdown_120d -50.42% < -28.00%; volatility_120d 42.38% > 42.00% |
| 002632.SZ | 道明光学 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -29.23% < 6.00%; excess_return_120d -33.81% < 6.00%; excess_return_240d -23.89% < 8.00%; drawdown_120d -39.27% < -28.00%; volatility_120d 47.99% > 42.00% |
| 300778.SZ | 新城市 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.25% < 6.00%; excess_return_120d -33.83% < 6.00%; excess_return_240d -55.10% < 8.00%; drawdown_120d -41.06% < -28.00%; volatility_120d 47.58% > 42.00% |
| 002918.SZ | 蒙娜丽莎 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.33% < 6.00%; excess_return_120d -33.91% < 6.00%; excess_return_240d -2.33% < 8.00%; drawdown_120d -46.09% < -28.00%; volatility_120d 64.02% > 42.00% |
| 002298.SZ | 中电鑫龙 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.41% < 6.00%; excess_return_120d -33.99% < 6.00%; excess_return_240d -14.13% < 8.00%; drawdown_120d -45.81% < -28.00%; volatility_120d 50.56% > 42.00% |
| 603171.SH | 税友股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -29.47% < 6.00%; excess_return_120d -34.05% < 6.00%; excess_return_240d -18.61% < 8.00%; drawdown_120d -57.15% < -28.00%; volatility_120d 55.88% > 42.00% |
| 605398.SH | 新炬网络 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.51% < 6.00%; excess_return_120d -34.09% < 6.00%; excess_return_240d -60.91% < 8.00%; drawdown_120d -45.31% < -28.00%; volatility_120d 52.10% > 42.00% |
| 600088.SH | 中视传媒 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.54% < 6.00%; excess_return_120d -34.12% < 6.00%; excess_return_240d -49.47% < 8.00%; drawdown_120d -43.03% < -28.00%; volatility_120d 48.75% > 42.00% |
| 002130.SZ | 沃尔核材 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.64% < 6.00%; excess_return_120d -34.22% < 6.00%; excess_return_240d -48.55% < 8.00%; drawdown_120d -45.97% < -28.00%; volatility_120d 52.17% > 42.00% |
| 300251.SZ | 光线传媒 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.64% < 6.00%; excess_return_120d -34.22% < 6.00%; excess_return_240d -62.08% < 8.00%; drawdown_120d -61.59% < -28.00%; volatility_120d 66.71% > 42.00% |
| 300805.SZ | 电声股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.67% < 6.00%; excess_return_120d -34.25% < 6.00%; excess_return_240d -55.78% < 8.00%; drawdown_120d -53.91% < -28.00%; volatility_120d 51.87% > 42.00% |
| 600748.SH | 上实发展 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.70% < 6.00%; excess_return_120d -34.28% < 6.00%; excess_return_240d -3.87% < 8.00%; drawdown_120d -43.97% < -28.00%; volatility_120d 47.60% > 42.00% |
| 002356.SZ | 赫美集团 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.80% < 6.00%; excess_return_120d -34.38% < 6.00%; excess_return_240d -29.95% < 8.00%; drawdown_120d -42.80% < -28.00%; volatility_120d 44.88% > 42.00% |
| 300635.SZ | 中达安 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.82% < 6.00%; excess_return_120d -34.40% < 6.00%; excess_return_240d -27.11% < 8.00%; drawdown_120d -36.40% < -28.00%; volatility_120d 45.28% > 42.00% |
| 300707.SZ | 威唐工业 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -29.84% < 6.00%; excess_return_120d -34.42% < 6.00%; excess_return_240d -37.10% < 8.00%; drawdown_120d -51.93% < -28.00%; volatility_120d 54.02% > 42.00% |
| 002459.SZ | 晶澳科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.87% < 6.00%; excess_return_120d -34.45% < 6.00%; excess_return_240d -47.63% < 8.00%; drawdown_120d -40.03% < -28.00%; volatility_120d 48.69% > 42.00% |
| 600067.SH | 冠城新材 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -29.87% < 6.00%; excess_return_120d -34.45% < 6.00%; excess_return_240d -17.70% < 8.00%; drawdown_120d -38.78% < -28.00%; volatility_120d 44.11% > 42.00% |
| 002279.SZ | 久其软件 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -29.91% < 6.00%; excess_return_120d -34.49% < 6.00%; excess_return_240d -36.12% < 8.00%; drawdown_120d -50.49% < -28.00%; volatility_120d 50.71% > 42.00% |
| 688399.SH | 硕世生物 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.93% < 6.00%; excess_return_120d -34.51% < 6.00%; excess_return_240d -24.23% < 8.00%; drawdown_120d -48.94% < -28.00%; volatility_120d 57.09% > 42.00% |
| 688088.SH | 虹软科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -29.96% < 6.00%; excess_return_120d -34.54% < 6.00%; excess_return_240d -46.83% < 8.00%; drawdown_120d -43.65% < -28.00%; volatility_120d 45.43% > 42.00% |
| 000635.SZ | 英力特 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.03% < 6.00%; excess_return_120d -34.61% < 6.00%; excess_return_240d -52.44% < 8.00%; drawdown_120d -43.09% < -28.00%; volatility_120d 44.47% > 42.00% |
| 300493.SZ | 润欣科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.04% < 6.00%; excess_return_120d -34.63% < 6.00%; excess_return_240d -52.36% < 8.00%; drawdown_120d -41.18% < -28.00%; volatility_120d 47.33% > 42.00% |
| 688157.SH | 松井股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.10% < 6.00%; excess_return_120d -34.68% < 6.00%; excess_return_240d -31.51% < 8.00%; drawdown_120d -43.49% < -28.00%; volatility_120d 46.63% > 42.00% |
| 001330.SZ | 博纳影业 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -30.13% < 6.00%; excess_return_120d -34.71% < 6.00%; excess_return_240d -8.12% < 8.00%; drawdown_120d -61.30% < -28.00%; volatility_120d 72.31% > 42.00% |
| 300910.SZ | 瑞丰新材 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.13% < 6.00%; excess_return_120d -34.71% < 6.00%; excess_return_240d -53.01% < 8.00%; drawdown_120d -40.64% < -28.00%; volatility_120d 44.34% > 42.00% |
| 000785.SZ | 居然智家 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.14% < 6.00%; excess_return_120d -34.72% < 6.00%; excess_return_240d -54.43% < 8.00%; drawdown_120d -45.89% < -28.00%; volatility_120d 45.03% > 42.00% |
| 300349.SZ | 金卡智能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -30.17% < 6.00%; excess_return_120d -34.75% < 6.00%; excess_return_240d -29.85% < 8.00%; drawdown_120d -48.93% < -28.00%; volatility_120d 66.29% > 42.00% |
| 300207.SZ | 欣旺达 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.20% < 6.00%; excess_return_120d -34.78% < 6.00%; excess_return_240d -28.01% < 8.00%; drawdown_120d -40.38% < -28.00%; volatility_120d 43.63% > 42.00% |
| 000716.SZ | 黑芝麻 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.34% < 6.00%; excess_return_120d -34.92% < 6.00%; excess_return_240d -51.54% < 8.00%; drawdown_120d -36.92% < -28.00%; volatility_120d 44.99% > 42.00% |
| 000829.SZ | 天音控股 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.34% < 6.00%; excess_return_120d -34.92% < 6.00%; excess_return_240d -47.02% < 8.00%; drawdown_120d -40.11% < -28.00%; volatility_120d 43.70% > 42.00% |
| 300333.SZ | 兆日科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.35% < 6.00%; excess_return_120d -34.93% < 6.00%; excess_return_240d -70.78% < 8.00%; drawdown_120d -36.68% < -28.00%; volatility_120d 54.85% > 42.00% |
| 003006.SZ | 百亚股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.36% < 6.00%; excess_return_120d -34.94% < 6.00%; excess_return_240d -64.37% < 8.00%; drawdown_120d -34.23% < -28.00%; volatility_120d 42.90% > 42.00% |
| 300310.SZ | 宜通世纪 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.46% < 6.00%; excess_return_120d -35.04% < 6.00%; excess_return_240d -58.06% < 8.00%; drawdown_120d -44.23% < -28.00%; volatility_120d 48.85% > 42.00% |
| 600588.SH | 用友网络 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.69% < 6.00%; excess_return_120d -35.27% < 6.00%; excess_return_240d -50.89% < 8.00%; drawdown_120d -51.66% < -28.00%; volatility_120d 47.80% > 42.00% |
| 002725.SZ | 跃岭股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.70% < 6.00%; excess_return_120d -35.28% < 6.00%; excess_return_240d -29.13% < 8.00%; drawdown_120d -38.69% < -28.00%; volatility_120d 50.58% > 42.00% |
| 605068.SH | 明新旭腾 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.71% < 6.00%; excess_return_120d -35.29% < 6.00%; excess_return_240d -23.79% < 8.00%; drawdown_120d -41.87% < -28.00%; volatility_120d 44.66% > 42.00% |
| 301073.SZ | 君亭酒店 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -30.78% < 6.00%; excess_return_120d -35.36% < 6.00%; excess_return_240d -47.25% < 8.00%; drawdown_120d -48.46% < -28.00%; volatility_120d 46.33% > 42.00% |
| 603887.SH | 城地香江 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.84% < 6.00%; excess_return_120d -35.42% < 6.00%; excess_return_240d -66.51% < 8.00%; drawdown_120d -49.10% < -28.00%; volatility_120d 53.85% > 42.00% |
| 002194.SZ | 武汉凡谷 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.88% < 6.00%; excess_return_120d -35.46% < 6.00%; excess_return_240d -59.27% < 8.00%; drawdown_120d -40.50% < -28.00%; volatility_120d 58.01% > 42.00% |
| 300437.SZ | 清水源 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -30.93% < 6.00%; excess_return_120d -35.51% < 6.00%; excess_return_240d -4.62% < 8.00%; drawdown_120d -52.04% < -28.00%; volatility_120d 64.84% > 42.00% |
| 002264.SZ | 新华都 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -30.94% < 6.00%; excess_return_120d -35.52% < 6.00%; excess_return_240d -25.88% < 8.00%; drawdown_120d -51.69% < -28.00%; volatility_120d 52.43% > 42.00% |
| 300530.SZ | 领湃科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -30.94% < 6.00%; excess_return_120d -35.52% < 6.00%; excess_return_240d -68.26% < 8.00%; drawdown_120d -45.59% < -28.00%; volatility_120d 50.01% > 42.00% |
| 300589.SZ | 江龙船艇 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -30.97% < 6.00%; excess_return_120d -35.55% < 6.00%; excess_return_240d -34.93% < 8.00%; drawdown_120d -47.16% < -28.00%; volatility_120d 50.52% > 42.00% |
| 688288.SH | 鸿泉技术 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.04% < 6.00%; excess_return_120d -35.62% < 6.00%; excess_return_240d -54.07% < 8.00%; drawdown_120d -41.49% < -28.00%; volatility_120d 52.64% > 42.00% |
| 002153.SZ | 石基信息 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.05% < 6.00%; excess_return_120d -35.63% < 6.00%; excess_return_240d -41.14% < 8.00%; drawdown_120d -55.52% < -28.00%; volatility_120d 46.18% > 42.00% |
| 300479.SZ | 神思电子 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.07% < 6.00%; excess_return_120d -35.65% < 6.00%; excess_return_240d -60.22% < 8.00%; drawdown_120d -46.83% < -28.00%; volatility_120d 44.69% > 42.00% |
| 300711.SZ | 广哈通信 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -31.10% < 6.00%; excess_return_120d -35.68% < 6.00%; excess_return_240d -49.27% < 8.00%; drawdown_120d -54.61% < -28.00%; volatility_120d 62.05% > 42.00% |
| 002315.SZ | 焦点科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.11% < 6.00%; excess_return_120d -35.69% < 6.00%; excess_return_240d -55.05% < 8.00%; drawdown_120d -50.54% < -28.00%; volatility_120d 43.14% > 42.00% |
| 300624.SZ | 万兴科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -31.18% < 6.00%; excess_return_120d -35.76% < 6.00%; excess_return_240d -46.50% < 8.00%; drawdown_120d -60.41% < -28.00%; volatility_120d 63.11% > 42.00% |
| 300945.SZ | 曼卡龙 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.28% < 6.00%; excess_return_120d -35.86% < 6.00%; excess_return_240d -68.99% < 8.00%; drawdown_120d -59.30% < -28.00%; volatility_120d 60.54% > 42.00% |
| 688608.SH | 恒玄科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.35% < 6.00%; excess_return_120d -35.93% < 6.00%; excess_return_240d -53.38% < 8.00%; drawdown_120d -39.47% < -28.00%; volatility_120d 51.01% > 42.00% |
| 300922.SZ | 天秦装备 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.45% < 6.00%; excess_return_120d -36.03% < 6.00%; excess_return_240d -61.81% < 8.00%; drawdown_120d -40.80% < -28.00%; volatility_120d 51.83% > 42.00% |
| 600963.SH | 岳阳林纸 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -31.48% < 6.00%; excess_return_120d -36.06% < 6.00%; excess_return_240d -50.46% < 8.00%; drawdown_120d -52.02% < -28.00%; volatility_120d 44.01% > 42.00% |
| 600611.SH | 大众交通 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.50% < 6.00%; excess_return_120d -36.08% < 6.00%; excess_return_240d -60.18% < 8.00%; drawdown_120d -43.33% < -28.00%; volatility_120d 49.48% > 42.00% |
| 300423.SZ | 昇辉科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -31.50% < 6.00%; excess_return_120d -36.08% < 6.00%; excess_return_240d -37.67% < 8.00%; drawdown_120d -52.33% < -28.00%; volatility_120d 60.30% > 42.00% |
| 688070.SH | 纵横股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.52% < 6.00%; excess_return_120d -36.10% < 6.00%; excess_return_240d -42.02% < 8.00%; drawdown_120d -44.61% < -28.00%; volatility_120d 50.77% > 42.00% |
| 688472.SH | 阿特斯 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.52% < 6.00%; excess_return_120d -36.10% < 6.00%; excess_return_240d -13.51% < 8.00%; drawdown_120d -44.81% < -28.00%; volatility_120d 50.23% > 42.00% |
| 600810.SH | 神马股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.59% < 6.00%; excess_return_120d -36.17% < 6.00%; excess_return_240d -56.10% < 8.00%; drawdown_120d -35.40% < -28.00%; volatility_120d 43.09% > 42.00% |
| 603109.SH | 神驰机电 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.61% < 6.00%; excess_return_120d -36.19% < 6.00%; excess_return_240d -57.37% < 8.00%; drawdown_120d -38.88% < -28.00%; volatility_120d 44.13% > 42.00% |
| 002178.SZ | 延华智能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.61% < 6.00%; excess_return_120d -36.19% < 6.00%; excess_return_240d -50.95% < 8.00%; drawdown_120d -40.46% < -28.00%; volatility_120d 42.91% > 42.00% |
| 603988.SH | 中电电机 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.68% < 6.00%; excess_return_120d -36.26% < 6.00%; excess_return_240d -55.64% < 8.00%; drawdown_120d -58.50% < -28.00%; volatility_120d 54.00% > 42.00% |
| 600819.SH | 耀皮玻璃 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.81% < 6.00%; excess_return_120d -36.39% < 6.00%; excess_return_240d -43.07% < 8.00%; drawdown_120d -39.78% < -28.00%; volatility_120d 48.92% > 42.00% |
| 301325.SZ | 曼恩斯特 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.81% < 6.00%; excess_return_120d -36.39% < 6.00%; excess_return_240d -63.85% < 8.00%; drawdown_120d -40.40% < -28.00%; volatility_120d 46.80% > 42.00% |
| 300340.SZ | 科恒股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.82% < 6.00%; excess_return_120d -36.40% < 6.00%; excess_return_240d -75.64% < 8.00%; drawdown_120d -43.59% < -28.00%; volatility_120d 50.47% > 42.00% |
| 002121.SZ | 科陆电子 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.82% < 6.00%; excess_return_120d -36.40% < 6.00%; excess_return_240d -19.55% < 8.00%; drawdown_120d -51.12% < -28.00%; volatility_120d 50.01% > 42.00% |
| 688408.SH | 中信博 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.85% < 6.00%; excess_return_120d -36.43% < 6.00%; excess_return_240d -60.73% < 8.00%; drawdown_120d -46.83% < -28.00%; volatility_120d 52.27% > 42.00% |
| 002869.SZ | 金溢科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.86% < 6.00%; excess_return_120d -36.44% < 6.00%; excess_return_240d -52.54% < 8.00%; drawdown_120d -40.84% < -28.00%; volatility_120d 45.79% > 42.00% |
| 002949.SZ | 华阳国际 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.92% < 6.00%; excess_return_120d -36.50% < 6.00%; excess_return_240d -44.26% < 8.00%; drawdown_120d -38.67% < -28.00%; volatility_120d 43.40% > 42.00% |
| 688500.SH | 慧辰股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -31.96% < 6.00%; excess_return_120d -36.54% < 6.00%; excess_return_240d -36.97% < 8.00%; drawdown_120d -49.77% < -28.00%; volatility_120d 71.30% > 42.00% |
| 002400.SZ | 省广集团 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -31.98% < 6.00%; excess_return_120d -36.56% < 6.00%; excess_return_240d -42.21% < 8.00%; drawdown_120d -56.60% < -28.00%; volatility_120d 59.25% > 42.00% |
| 688111.SH | 金山办公 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.04% < 6.00%; excess_return_120d -36.63% < 6.00%; excess_return_240d -44.36% < 8.00%; drawdown_120d -49.77% < -28.00%; volatility_120d 44.83% > 42.00% |
| 603030.SH | 全筑股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.09% < 6.00%; excess_return_120d -36.67% < 6.00%; excess_return_240d -46.65% < 8.00%; drawdown_120d -38.53% < -28.00%; volatility_120d 44.24% > 42.00% |
| 605388.SH | 均瑶健康 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.12% < 6.00%; excess_return_120d -36.70% < 6.00%; excess_return_240d -60.11% < 8.00%; drawdown_120d -44.51% < -28.00%; volatility_120d 46.76% > 42.00% |
| 688778.SH | 厦钨新能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.13% < 6.00%; excess_return_120d -36.71% < 6.00%; excess_return_240d -8.56% < 8.00%; drawdown_120d -48.86% < -28.00%; volatility_120d 46.72% > 42.00% |
| 300925.SZ | 法本信息 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.14% < 6.00%; excess_return_120d -36.72% < 6.00%; excess_return_240d -66.73% < 8.00%; drawdown_120d -47.23% < -28.00%; volatility_120d 49.69% > 42.00% |
| 688166.SH | 博瑞医药 | ok | 18.00 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -32.14% < 6.00%; excess_return_120d -36.72% < 6.00%; excess_return_240d -61.84% < 8.00%; drawdown_120d -54.33% < -28.00%; volatility_120d 61.71% > 42.00% |
| 600838.SH | 上海九百 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -32.16% < 6.00%; excess_return_120d -36.74% < 6.00%; excess_return_240d -30.79% < 8.00%; drawdown_120d -52.52% < -28.00%; volatility_120d 46.96% > 42.00% |
| 688656.SH | 浩欧博 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.20% < 6.00%; excess_return_120d -36.78% < 6.00%; excess_return_240d -37.65% < 8.00%; drawdown_120d -37.19% < -28.00%; volatility_120d 44.60% > 42.00% |
| 002221.SZ | 东华能源 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.22% < 6.00%; excess_return_120d -36.80% < 6.00%; excess_return_240d -63.91% < 8.00%; drawdown_120d -45.86% < -28.00%; volatility_120d 45.62% > 42.00% |
| 601519.SH | 大智慧 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.25% < 6.00%; excess_return_120d -36.83% < 6.00%; excess_return_240d -53.76% < 8.00%; drawdown_120d -45.09% < -28.00%; volatility_120d 44.82% > 42.00% |
| 300541.SZ | 先进数通 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.29% < 6.00%; excess_return_120d -36.87% < 6.00%; excess_return_240d -58.94% < 8.00%; drawdown_120d -39.58% < -28.00%; volatility_120d 44.69% > 42.00% |
| 002243.SZ | 力合科创 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.32% < 6.00%; excess_return_120d -36.90% < 6.00%; excess_return_240d -37.87% < 8.00%; drawdown_120d -45.08% < -28.00%; volatility_120d 44.37% > 42.00% |
| 300032.SZ | 金龙机电 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.40% < 6.00%; excess_return_120d -36.98% < 6.00%; excess_return_240d -55.69% < 8.00%; drawdown_120d -44.41% < -28.00%; volatility_120d 45.55% > 42.00% |
| 300916.SZ | 朗特智能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.42% < 6.00%; excess_return_120d -37.00% < 6.00%; excess_return_240d -44.35% < 8.00%; drawdown_120d -46.41% < -28.00%; volatility_120d 50.85% > 42.00% |
| 000532.SZ | 华金资本 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.52% < 6.00%; excess_return_120d -37.10% < 6.00%; excess_return_240d -48.98% < 8.00%; drawdown_120d -42.86% < -28.00%; volatility_120d 43.01% > 42.00% |
| 300195.SZ | 长荣股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.58% < 6.00%; excess_return_120d -37.16% < 6.00%; excess_return_240d -45.78% < 8.00%; drawdown_120d -44.33% < -28.00%; volatility_120d 55.40% > 42.00% |
| 002209.SZ | 达意隆 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.67% < 6.00%; excess_return_120d -37.25% < 6.00%; excess_return_240d -35.52% < 8.00%; drawdown_120d -38.91% < -28.00%; volatility_120d 47.58% > 42.00% |
| 300509.SZ | 新美星 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -32.71% < 6.00%; excess_return_120d -37.29% < 6.00%; excess_return_240d -20.75% < 8.00%; drawdown_120d -49.18% < -28.00%; volatility_120d 44.83% > 42.00% |
| 603159.SH | 上海亚虹 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -32.85% < 6.00%; excess_return_120d -37.33% < 6.00%; excess_return_240d -21.83% < 8.00%; drawdown_120d -42.99% < -28.00%; volatility_120d 52.21% > 42.00% |
| 603313.SH | 梦百合 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.81% < 6.00%; excess_return_120d -37.39% < 6.00%; excess_return_240d -56.10% < 8.00%; drawdown_120d -44.48% < -28.00%; volatility_120d 49.08% > 42.00% |
| 688152.SH | 麒麟信安 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -32.94% < 6.00%; excess_return_120d -37.52% < 6.00%; excess_return_240d -59.79% < 8.00%; drawdown_120d -44.84% < -28.00%; volatility_120d 44.93% > 42.00% |
| 600860.SH | 京城股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.01% < 6.00%; excess_return_120d -37.59% < 6.00%; excess_return_240d -48.31% < 8.00%; drawdown_120d -49.34% < -28.00%; volatility_120d 47.82% > 42.00% |
| 003001.SZ | 中岩大地 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.03% < 6.00%; excess_return_120d -37.61% < 6.00%; excess_return_240d -70.94% < 8.00%; drawdown_120d -43.27% < -28.00%; volatility_120d 43.92% > 42.00% |
| 301383.SZ | 天键股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.05% < 6.00%; excess_return_120d -37.63% < 6.00%; excess_return_240d -59.81% < 8.00%; drawdown_120d -40.34% < -28.00%; volatility_120d 42.81% > 42.00% |
| 600610.SH | 中毅达 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.13% < 6.00%; excess_return_120d -37.71% < 6.00%; excess_return_240d -77.27% < 8.00%; drawdown_120d -50.78% < -28.00%; volatility_120d 57.48% > 42.00% |
| 300062.SZ | 中能电气 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -33.13% < 6.00%; excess_return_120d -37.71% < 6.00%; excess_return_240d -22.16% < 8.00%; drawdown_120d -49.73% < -28.00%; volatility_120d 49.04% > 42.00% |
| 300402.SZ | 宝色股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.24% < 6.00%; excess_return_120d -37.82% < 6.00%; excess_return_240d -50.91% < 8.00%; drawdown_120d -45.61% < -28.00%; volatility_120d 44.72% > 42.00% |
| 603633.SH | 徕木股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.27% < 6.00%; excess_return_120d -37.85% < 6.00%; excess_return_240d -44.65% < 8.00%; drawdown_120d -36.82% < -28.00%; volatility_120d 44.79% > 42.00% |
| 600547.SH | 山东黄金 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -33.35% < 6.00%; excess_return_120d -37.93% < 6.00%; excess_return_240d -40.21% < 8.00%; drawdown_120d -60.64% < -28.00%; volatility_120d 56.37% > 42.00% |
| 300581.SZ | 晨曦航空 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.35% < 6.00%; excess_return_120d -37.93% < 6.00%; excess_return_240d -67.62% < 8.00%; drawdown_120d -40.91% < -28.00%; volatility_120d 51.09% > 42.00% |
| 300818.SZ | 耐普矿机 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -33.42% < 6.00%; excess_return_120d -38.00% < 6.00%; excess_return_240d -4.91% < 8.00%; drawdown_120d -57.98% < -28.00%; volatility_120d 64.73% > 42.00% |
| 300904.SZ | 威力传动 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.46% < 6.00%; excess_return_120d -38.04% < 6.00%; excess_return_240d -42.80% < 8.00%; drawdown_120d -47.16% < -28.00%; volatility_120d 43.00% > 42.00% |
| 600698.SH | 湖南天雁 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.52% < 6.00%; excess_return_120d -38.10% < 6.00%; excess_return_240d -69.73% < 8.00%; drawdown_120d -36.20% < -28.00%; volatility_120d 44.05% > 42.00% |
| 300682.SZ | 朗新科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.56% < 6.00%; excess_return_120d -38.14% < 6.00%; excess_return_240d -76.76% < 8.00%; drawdown_120d -51.34% < -28.00%; volatility_120d 52.90% > 42.00% |
| 300229.SZ | 拓尔思 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.62% < 6.00%; excess_return_120d -38.20% < 6.00%; excess_return_240d -48.07% < 8.00%; drawdown_120d -57.39% < -28.00%; volatility_120d 63.39% > 42.00% |
| 002251.SZ | 步步高 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.71% < 6.00%; excess_return_120d -38.29% < 6.00%; excess_return_240d -51.67% < 8.00%; drawdown_120d -39.83% < -28.00%; volatility_120d 46.57% > 42.00% |
| 002123.SZ | 梦网科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.72% < 6.00%; excess_return_120d -38.30% < 6.00%; excess_return_240d -65.74% < 8.00%; drawdown_120d -45.02% < -28.00%; volatility_120d 44.84% > 42.00% |
| 300035.SZ | 中科电气 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.75% < 6.00%; excess_return_120d -38.33% < 6.00%; excess_return_240d -36.10% < 8.00%; drawdown_120d -44.68% < -28.00%; volatility_120d 48.67% > 42.00% |
| 603863.SH | 松炀资源 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.78% < 6.00%; excess_return_120d -38.36% < 6.00%; excess_return_240d -31.66% < 8.00%; drawdown_120d -39.63% < -28.00%; volatility_120d 53.98% > 42.00% |
| 301192.SZ | 泰祥股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.86% < 6.00%; excess_return_120d -38.44% < 6.00%; excess_return_240d -44.14% < 8.00%; drawdown_120d -43.90% < -28.00%; volatility_120d 44.58% > 42.00% |
| 688348.SH | 昱能科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -33.90% < 6.00%; excess_return_120d -38.48% < 6.00%; excess_return_240d -45.43% < 8.00%; drawdown_120d -52.02% < -28.00%; volatility_120d 51.91% > 42.00% |
| 300533.SZ | 冰川网络 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.05% < 6.00%; excess_return_120d -38.63% < 6.00%; excess_return_240d -61.33% < 8.00%; drawdown_120d -46.86% < -28.00%; volatility_120d 56.75% > 42.00% |
| 688590.SH | 新致软件 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.08% < 6.00%; excess_return_120d -38.66% < 6.00%; excess_return_240d -59.95% < 8.00%; drawdown_120d -54.63% < -28.00%; volatility_120d 59.78% > 42.00% |
| 688789.SH | 宏华数科 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.12% < 6.00%; excess_return_120d -38.70% < 6.00%; excess_return_240d -43.51% < 8.00%; drawdown_120d -40.33% < -28.00%; volatility_120d 42.44% > 42.00% |
| 300622.SZ | 博士眼镜 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.25% < 6.00%; excess_return_120d -38.83% < 6.00%; excess_return_240d -60.38% < 8.00%; drawdown_120d -47.58% < -28.00%; volatility_120d 46.38% > 42.00% |
| 688186.SH | 广大特材 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.26% < 6.00%; excess_return_120d -38.84% < 6.00%; excess_return_240d -66.14% < 8.00%; drawdown_120d -51.83% < -28.00%; volatility_120d 52.02% > 42.00% |
| 300078.SZ | 思创智联 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -34.31% < 6.00%; excess_return_120d -38.89% < 6.00%; excess_return_240d -46.29% < 8.00%; drawdown_120d -55.57% < -28.00%; volatility_120d 51.70% > 42.00% |
| 301551.SZ | 无线传媒 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.39% < 6.00%; excess_return_120d -38.97% < 6.00%; excess_return_240d -78.02% < 8.00%; drawdown_120d -49.31% < -28.00%; volatility_120d 44.34% > 42.00% |
| 688095.SH | 福昕软件 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.42% < 6.00%; excess_return_120d -39.00% < 6.00%; excess_return_240d -34.91% < 8.00%; drawdown_120d -56.42% < -28.00%; volatility_120d 57.47% > 42.00% |
| 603636.SH | 南威软件 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.46% < 6.00%; excess_return_120d -39.04% < 6.00%; excess_return_240d -60.19% < 8.00%; drawdown_120d -43.85% < -28.00%; volatility_120d 51.97% > 42.00% |
| 300795.SZ | 米奥会展 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.51% < 6.00%; excess_return_120d -39.09% < 6.00%; excess_return_240d -62.68% < 8.00%; drawdown_120d -40.37% < -28.00%; volatility_120d 44.78% > 42.00% |
| 688615.SH | 合合信息 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -34.63% < 6.00%; excess_return_120d -39.21% < 6.00%; excess_return_240d -27.07% < 8.00%; drawdown_120d -59.76% < -28.00%; volatility_120d 54.78% > 42.00% |
| 300810.SZ | 中科海讯 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.71% < 6.00%; excess_return_120d -39.29% < 6.00%; excess_return_240d -67.82% < 8.00%; drawdown_120d -45.04% < -28.00%; volatility_120d 46.03% > 42.00% |
| 688568.SH | 中科星图 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -34.73% < 6.00%; excess_return_120d -39.31% < 6.00%; excess_return_240d -15.15% < 8.00%; drawdown_120d -61.48% < -28.00%; volatility_120d 73.19% > 42.00% |
| 688631.SH | 莱斯信息 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.78% < 6.00%; excess_return_120d -39.36% < 6.00%; excess_return_240d -69.72% < 8.00%; drawdown_120d -49.21% < -28.00%; volatility_120d 49.71% > 42.00% |
| 002402.SZ | 和而泰 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.79% < 6.00%; excess_return_120d -39.37% < 6.00%; excess_return_240d -4.25% < 8.00%; drawdown_120d -40.96% < -28.00%; volatility_120d 42.25% > 42.00% |
| 002640.SZ | 跨境通 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.88% < 6.00%; excess_return_120d -39.46% < 6.00%; excess_return_240d -61.50% < 8.00%; drawdown_120d -42.61% < -28.00%; volatility_120d 52.33% > 42.00% |
| 603363.SH | 傲农生物 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.92% < 6.00%; excess_return_120d -39.50% < 6.00%; excess_return_240d -37.53% < 8.00%; drawdown_120d -35.62% < -28.00%; volatility_120d 43.91% > 42.00% |
| 002988.SZ | 豪美新材 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.95% < 6.00%; excess_return_120d -39.53% < 6.00%; excess_return_240d -64.50% < 8.00%; drawdown_120d -43.62% < -28.00%; volatility_120d 51.94% > 42.00% |
| 300426.SZ | 华智数媒 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.97% < 6.00%; excess_return_120d -39.55% < 6.00%; excess_return_240d -68.64% < 8.00%; drawdown_120d -53.86% < -28.00%; volatility_120d 50.75% > 42.00% |
| 300377.SZ | 赢时胜 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -34.99% < 6.00%; excess_return_120d -39.57% < 6.00%; excess_return_240d -64.03% < 8.00%; drawdown_120d -45.62% < -28.00%; volatility_120d 60.64% > 42.00% |
| 002836.SZ | 新宏泽 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -35.00% < 6.00%; excess_return_120d -39.58% < 6.00%; excess_return_240d -19.66% < 8.00%; drawdown_120d -46.29% < -28.00%; volatility_120d 45.99% > 42.00% |
| 001217.SZ | 华尔泰 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.00% < 6.00%; excess_return_120d -39.58% < 6.00%; excess_return_240d -44.23% < 8.00%; drawdown_120d -45.80% < -28.00%; volatility_120d 44.37% > 42.00% |
| 300956.SZ | 英力股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.01% < 6.00%; excess_return_120d -39.59% < 6.00%; excess_return_240d -55.02% < 8.00%; drawdown_120d -45.87% < -28.00%; volatility_120d 57.21% > 42.00% |
| 300803.SZ | 指南针 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.01% < 6.00%; excess_return_120d -39.59% < 6.00%; excess_return_240d -16.18% < 8.00%; drawdown_120d -44.92% < -28.00%; volatility_120d 48.66% > 42.00% |
| 603767.SH | 中马传动 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.09% < 6.00%; excess_return_120d -39.67% < 6.00%; excess_return_240d -27.51% < 8.00%; drawdown_120d -38.78% < -28.00%; volatility_120d 46.59% > 42.00% |
| 301535.SZ | 浙江华远 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -35.23% < 6.00%; excess_return_120d -39.81% < 6.00%; excess_return_240d -52.39% < 8.00%; drawdown_120d -53.93% < -28.00%; volatility_120d 53.50% > 42.00% |
| 300122.SZ | 智飞生物 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.24% < 6.00%; excess_return_120d -39.82% < 6.00%; excess_return_240d -59.54% < 8.00%; drawdown_120d -41.50% < -28.00%; volatility_120d 43.06% > 42.00% |
| 002657.SZ | 中科金财 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.26% < 6.00%; excess_return_120d -39.84% < 6.00%; excess_return_240d -51.84% < 8.00%; drawdown_120d -42.86% < -28.00%; volatility_120d 50.40% > 42.00% |
| 300850.SZ | 新强联 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.26% < 6.00%; excess_return_120d -39.84% < 6.00%; excess_return_240d -49.59% < 8.00%; drawdown_120d -52.13% < -28.00%; volatility_120d 43.32% > 42.00% |
| 300952.SZ | 恒辉安防 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -35.40% < 6.00%; excess_return_120d -39.98% < 6.00%; excess_return_240d -23.92% < 8.00%; drawdown_120d -52.90% < -28.00%; volatility_120d 60.83% > 42.00% |
| 301600.SZ | 慧翰股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.44% < 6.00%; excess_return_120d -40.02% < 6.00%; excess_return_240d -31.54% < 8.00%; drawdown_120d -42.94% < -28.00%; volatility_120d 49.46% > 42.00% |
| 300719.SZ | 安达维尔 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.45% < 6.00%; excess_return_120d -40.03% < 6.00%; excess_return_240d -57.98% < 8.00%; drawdown_120d -44.04% < -28.00%; volatility_120d 55.68% > 42.00% |
| 688435.SH | 英方软件 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -35.45% < 6.00%; excess_return_120d -40.03% < 6.00%; excess_return_240d -26.64% < 8.00%; drawdown_120d -53.95% < -28.00%; volatility_120d 70.97% > 42.00% |
| 002229.SZ | 鸿博股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.47% < 6.00%; excess_return_120d -40.05% < 6.00%; excess_return_240d -66.26% < 8.00%; drawdown_120d -50.59% < -28.00%; volatility_120d 58.05% > 42.00% |
| 301050.SZ | 雷电微力 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.49% < 6.00%; excess_return_120d -40.07% < 6.00%; excess_return_240d -55.48% < 8.00%; drawdown_120d -55.07% < -28.00%; volatility_120d 54.46% > 42.00% |
| 600446.SH | 金证股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.55% < 6.00%; excess_return_120d -40.13% < 6.00%; excess_return_240d -66.17% < 8.00%; drawdown_120d -43.87% < -28.00%; volatility_120d 46.39% > 42.00% |
| 688658.SH | 悦康药业 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.56% < 6.00%; excess_return_120d -40.14% < 6.00%; excess_return_240d -56.63% < 8.00%; drawdown_120d -54.64% < -28.00%; volatility_120d 62.61% > 42.00% |
| 300698.SZ | 万马科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.58% < 6.00%; excess_return_120d -40.16% < 6.00%; excess_return_240d -60.23% < 8.00%; drawdown_120d -43.52% < -28.00%; volatility_120d 49.89% > 42.00% |
| 601929.SH | 吉视传媒 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.76% < 6.00%; excess_return_120d -40.34% < 6.00%; excess_return_240d -2.28% < 8.00%; drawdown_120d -53.47% < -28.00%; volatility_120d 52.99% > 42.00% |
| 603737.SH | 三棵树 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.77% < 6.00%; excess_return_120d -40.35% < 6.00%; excess_return_240d -41.69% < 8.00%; drawdown_120d -49.10% < -28.00%; volatility_120d 44.38% > 42.00% |
| 002683.SZ | 广东宏大 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -35.82% < 6.00%; excess_return_120d -40.40% < 6.00%; excess_return_240d -34.92% < 8.00%; drawdown_120d -44.29% < -28.00%; volatility_120d 45.06% > 42.00% |
| 300278.SZ | 华昌达 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.90% < 6.00%; excess_return_120d -40.48% < 6.00%; excess_return_240d -48.69% < 8.00%; drawdown_120d -43.00% < -28.00%; volatility_120d 44.81% > 42.00% |
| 002379.SZ | 宏桥控股 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -35.91% < 6.00%; excess_return_120d -40.49% < 6.00%; excess_return_240d -1.84% < 8.00%; drawdown_120d -54.29% < -28.00%; volatility_120d 51.21% > 42.00% |
| 300291.SZ | 百纳千成 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -35.91% < 6.00%; excess_return_120d -40.49% < 6.00%; excess_return_240d -40.79% < 8.00%; drawdown_120d -57.75% < -28.00%; volatility_120d 72.42% > 42.00% |
| 002629.SZ | 仁智股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.03% < 6.00%; excess_return_120d -40.52% < 6.00%; excess_return_240d -46.85% < 8.00%; drawdown_120d -43.53% < -28.00%; volatility_120d 63.70% > 42.00% |
| 605286.SH | 同力天启 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.98% < 6.00%; excess_return_120d -40.56% < 6.00%; excess_return_240d -52.51% < 8.00%; drawdown_120d -53.49% < -28.00%; volatility_120d 52.11% > 42.00% |
| 600797.SH | 浙大网新 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.23% < 6.00%; excess_return_120d -40.81% < 6.00%; excess_return_240d -54.78% < 8.00%; drawdown_120d -47.29% < -28.00%; volatility_120d 47.86% > 42.00% |
| 688225.SH | 亚信安全 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.24% < 6.00%; excess_return_120d -40.82% < 6.00%; excess_return_240d -56.57% < 8.00%; drawdown_120d -53.27% < -28.00%; volatility_120d 50.87% > 42.00% |
| 300779.SZ | 惠城环保 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.24% < 6.00%; excess_return_120d -40.82% < 6.00%; excess_return_240d -81.77% < 8.00%; drawdown_120d -38.50% < -28.00%; volatility_120d 71.83% > 42.00% |
| 002928.SZ | 华夏航空 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.29% < 6.00%; excess_return_120d -40.87% < 6.00%; excess_return_240d -35.97% < 8.00%; drawdown_120d -41.14% < -28.00%; volatility_120d 50.54% > 42.00% |
| 000936.SZ | 华西股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.33% < 6.00%; excess_return_120d -40.91% < 6.00%; excess_return_240d -44.71% < 8.00%; drawdown_120d -43.53% < -28.00%; volatility_120d 42.76% > 42.00% |
| 002558.SZ | 巨人网络 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.34% < 6.00%; excess_return_120d -40.92% < 6.00%; excess_return_240d -13.55% < 8.00%; drawdown_120d -48.38% < -28.00%; volatility_120d 48.76% > 42.00% |
| 002905.SZ | 金逸影视 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.37% < 6.00%; excess_return_120d -40.95% < 6.00%; excess_return_240d -46.43% < 8.00%; drawdown_120d -52.19% < -28.00%; volatility_120d 49.23% > 42.00% |
| 300844.SZ | 山水比德 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.38% < 6.00%; excess_return_120d -40.96% < 6.00%; excess_return_240d -68.54% < 8.00%; drawdown_120d -54.53% < -28.00%; volatility_120d 49.15% > 42.00% |
| 002190.SZ | 成飞集成 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.43% < 6.00%; excess_return_120d -41.01% < 6.00%; excess_return_240d -56.31% < 8.00%; drawdown_120d -44.12% < -28.00%; volatility_120d 43.39% > 42.00% |
| 000917.SZ | 电广传媒 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -36.48% < 6.00%; excess_return_120d -41.06% < 6.00%; excess_return_240d -34.72% < 8.00%; drawdown_120d -54.81% < -28.00%; volatility_120d 52.24% > 42.00% |
| 300755.SZ | 华致酒行 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.55% < 6.00%; excess_return_120d -41.13% < 6.00%; excess_return_240d -60.10% < 8.00%; drawdown_120d -42.49% < -28.00%; volatility_120d 58.50% > 42.00% |
| 002036.SZ | 联创电子 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.57% < 6.00%; excess_return_120d -41.15% < 6.00%; excess_return_240d -57.30% < 8.00%; drawdown_120d -46.15% < -28.00%; volatility_120d 55.96% > 42.00% |
| 300652.SZ | 雷迪克 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.58% < 6.00%; excess_return_120d -41.16% < 6.00%; excess_return_240d -58.13% < 8.00%; drawdown_120d -53.14% < -28.00%; volatility_120d 53.44% > 42.00% |
| 002625.SZ | 光启技术 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.60% < 6.00%; excess_return_120d -41.18% < 6.00%; excess_return_240d -43.80% < 8.00%; drawdown_120d -46.69% < -28.00%; volatility_120d 44.88% > 42.00% |
| 001376.SZ | 百通能源 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -36.70% < 6.00%; excess_return_120d -41.28% < 6.00%; excess_return_240d -34.92% < 8.00%; drawdown_120d -57.73% < -28.00%; volatility_120d 68.09% > 42.00% |
| 000923.SZ | 河钢资源 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -36.75% < 6.00%; excess_return_120d -41.33% < 6.00%; excess_return_240d -24.73% < 8.00%; drawdown_120d -50.68% < -28.00%; volatility_120d 46.70% > 42.00% |
| 600192.SH | 长城电工 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.79% < 6.00%; excess_return_120d -41.37% < 6.00%; excess_return_240d -66.12% < 8.00%; drawdown_120d -46.54% < -28.00%; volatility_120d 47.85% > 42.00% |
| 688303.SH | 大全能源 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.80% < 6.00%; excess_return_120d -41.38% < 6.00%; excess_return_240d -57.13% < 8.00%; drawdown_120d -41.02% < -28.00%; volatility_120d 53.24% > 42.00% |
| 002676.SZ | 顺威股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.94% < 6.00%; excess_return_120d -41.52% < 6.00%; excess_return_240d -54.56% < 8.00%; drawdown_120d -43.15% < -28.00%; volatility_120d 43.92% > 42.00% |
| 002882.SZ | 金龙羽 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.96% < 6.00%; excess_return_120d -41.54% < 6.00%; excess_return_240d -67.26% < 8.00%; drawdown_120d -49.49% < -28.00%; volatility_120d 42.02% > 42.00% |
| 601567.SH | 三星电气 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -36.96% < 6.00%; excess_return_120d -41.54% < 6.00%; excess_return_240d -56.99% < 8.00%; drawdown_120d -56.98% < -28.00%; volatility_120d 48.52% > 42.00% |
| 000766.SZ | 通化金马 | ok | 18.00 | close_below_ma200; ma120_not_above_ma200; stock_return_120d -37.00% < 6.00%; excess_return_120d -41.58% < 6.00%; excess_return_240d -48.35% < 8.00%; drawdown_120d -39.10% < -28.00%; volatility_120d 49.12% > 42.00% |
| 002217.SZ | 合力泰 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.50% < 6.00%; excess_return_120d -41.60% < 6.00%; excess_return_240d -48.75% < 8.00%; drawdown_120d -49.47% < -28.00%; volatility_120d 61.96% > 42.00% |
| 002878.SZ | 元隆雅图 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.05% < 6.00%; excess_return_120d -41.63% < 6.00%; excess_return_240d -65.61% < 8.00%; drawdown_120d -48.29% < -28.00%; volatility_120d 49.24% > 42.00% |
| 300324.SZ | 旋极信息 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.12% < 6.00%; excess_return_120d -41.70% < 6.00%; excess_return_240d -44.21% < 8.00%; drawdown_120d -47.12% < -28.00%; volatility_120d 48.54% > 42.00% |
| 300248.SZ | 新开普 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.15% < 6.00%; excess_return_120d -41.73% < 6.00%; excess_return_240d -69.84% < 8.00%; drawdown_120d -51.26% < -28.00%; volatility_120d 51.77% > 42.00% |
| 300917.SZ | 特发服务 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.29% < 6.00%; excess_return_120d -41.87% < 6.00%; excess_return_240d -66.92% < 8.00%; drawdown_120d -43.90% < -28.00%; volatility_120d 42.13% > 42.00% |
| 300965.SZ | 恒宇信通 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -35.55% < 6.00%; excess_return_120d -41.90% < 6.00%; excess_return_240d -27.58% < 8.00%; drawdown_120d -55.16% < -28.00%; volatility_120d 68.41% > 42.00% |
| 002052.SZ | 同洲电子 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.33% < 6.00%; excess_return_120d -41.91% < 6.00%; excess_return_240d -56.66% < 8.00%; drawdown_120d -42.89% < -28.00%; volatility_120d 43.17% > 42.00% |
| 002017.SZ | 东信和平 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.35% < 6.00%; excess_return_120d -41.93% < 6.00%; excess_return_240d -42.17% < 8.00%; drawdown_120d -53.49% < -28.00%; volatility_120d 42.70% > 42.00% |
| 300766.SZ | 每日互动 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.38% < 6.00%; excess_return_120d -41.96% < 6.00%; excess_return_240d -62.18% < 8.00%; drawdown_120d -59.41% < -28.00%; volatility_120d 70.14% > 42.00% |
| 301209.SZ | 联合化学 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.50% < 6.00%; excess_return_120d -42.08% < 6.00%; excess_return_240d -53.43% < 8.00%; drawdown_120d -40.47% < -28.00%; volatility_120d 43.07% > 42.00% |
| 603232.SH | 格尔软件 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -37.52% < 6.00%; excess_return_120d -42.10% < 6.00%; excess_return_240d -36.40% < 8.00%; drawdown_120d -49.51% < -28.00%; volatility_120d 61.57% > 42.00% |
| 603108.SH | 润达医疗 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.59% < 6.00%; excess_return_120d -42.17% < 6.00%; excess_return_240d -67.20% < 8.00%; drawdown_120d -55.08% < -28.00%; volatility_120d 54.94% > 42.00% |
| 688292.SH | 浩瀚深度 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -37.60% < 6.00%; excess_return_120d -42.18% < 6.00%; excess_return_240d -26.44% < 8.00%; drawdown_120d -55.75% < -28.00%; volatility_120d 71.55% > 42.00% |
| 300876.SZ | 蒙泰高新 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.63% < 6.00%; excess_return_120d -42.21% < 6.00%; excess_return_240d -33.74% < 8.00%; drawdown_120d -41.18% < -28.00%; volatility_120d 44.28% > 42.00% |
| 002492.SZ | 恒基达鑫 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.64% < 6.00%; excess_return_120d -42.22% < 6.00%; excess_return_240d -28.88% < 8.00%; drawdown_120d -45.45% < -28.00%; volatility_120d 43.55% > 42.00% |
| 688244.SH | 永信至诚 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.73% < 6.00%; excess_return_120d -42.31% < 6.00%; excess_return_240d -59.78% < 8.00%; drawdown_120d -46.26% < -28.00%; volatility_120d 46.64% > 42.00% |
| 300960.SZ | 通业科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.73% < 6.00%; excess_return_120d -42.31% < 6.00%; excess_return_240d -59.61% < 8.00%; drawdown_120d -45.27% < -28.00%; volatility_120d 43.53% > 42.00% |
| 688280.SH | 精进电动 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -37.82% < 6.00%; excess_return_120d -42.40% < 6.00%; excess_return_240d -47.29% < 8.00%; drawdown_120d -55.29% < -28.00%; volatility_120d 68.30% > 42.00% |
| 600996.SH | 贵广网络 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -37.95% < 6.00%; excess_return_120d -42.53% < 6.00%; excess_return_240d -48.06% < 8.00%; drawdown_120d -43.87% < -28.00%; volatility_120d 57.29% > 42.00% |
| 600828.SH | 茂业商业 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -38.01% < 6.00%; excess_return_120d -42.59% < 6.00%; excess_return_240d -29.68% < 8.00%; drawdown_120d -58.20% < -28.00%; volatility_120d 60.14% > 42.00% |
| 688562.SH | 航天软件 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -38.15% < 6.00%; excess_return_120d -42.73% < 6.00%; excess_return_240d -38.35% < 8.00%; drawdown_120d -52.15% < -28.00%; volatility_120d 51.14% > 42.00% |
| 002278.SZ | 神开股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -38.21% < 6.00%; excess_return_120d -42.79% < 6.00%; excess_return_240d -39.91% < 8.00%; drawdown_120d -52.49% < -28.00%; volatility_120d 53.20% > 42.00% |
| 600408.SH | 安泰集团 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.21% < 6.00%; excess_return_120d -42.79% < 6.00%; excess_return_240d -6.35% < 8.00%; drawdown_120d -49.60% < -28.00%; volatility_120d 56.77% > 42.00% |
| 300071.SZ | 福石控股 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.44% < 6.00%; excess_return_120d -43.02% < 6.00%; excess_return_240d -41.96% < 8.00%; drawdown_120d -59.19% < -28.00%; volatility_120d 76.73% > 42.00% |
| 300612.SZ | 宣亚国际 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.46% < 6.00%; excess_return_120d -43.04% < 6.00%; excess_return_240d -49.93% < 8.00%; drawdown_120d -56.78% < -28.00%; volatility_120d 52.15% > 42.00% |
| 603918.SH | 金桥信息 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.50% < 6.00%; excess_return_120d -43.08% < 6.00%; excess_return_240d -72.94% < 8.00%; drawdown_120d -56.47% < -28.00%; volatility_120d 46.30% > 42.00% |
| 300918.SZ | 南山智尚 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.55% < 6.00%; excess_return_120d -43.13% < 6.00%; excess_return_240d -58.02% < 8.00%; drawdown_120d -46.91% < -28.00%; volatility_120d 45.41% > 42.00% |
| 300587.SZ | 天铁科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.66% < 6.00%; excess_return_120d -43.24% < 6.00%; excess_return_240d -71.49% < 8.00%; drawdown_120d -45.66% < -28.00%; volatility_120d 46.77% > 42.00% |
| 300275.SZ | 梅安森 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.68% < 6.00%; excess_return_120d -43.26% < 6.00%; excess_return_240d -58.36% < 8.00%; drawdown_120d -45.31% < -28.00%; volatility_120d 51.11% > 42.00% |
| 688196.SH | 卓越新能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -38.70% < 6.00%; excess_return_120d -43.28% < 6.00%; excess_return_240d -45.33% < 8.00%; drawdown_120d -62.12% < -28.00%; volatility_120d 58.17% > 42.00% |
| 300963.SZ | 中洲特材 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.74% < 6.00%; excess_return_120d -43.32% < 6.00%; excess_return_240d -71.51% < 8.00%; drawdown_120d -51.54% < -28.00%; volatility_120d 47.12% > 42.00% |
| 603169.SH | 兰石重装 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -38.84% < 6.00%; excess_return_120d -43.42% < 6.00%; excess_return_240d -38.98% < 8.00%; drawdown_120d -54.02% < -28.00%; volatility_120d 52.96% > 42.00% |
| 002210.SZ | 飞马国际 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -38.89% < 6.00%; excess_return_120d -43.47% < 6.00%; excess_return_240d -48.01% < 8.00%; drawdown_120d -38.89% < -28.00%; volatility_120d 49.23% > 42.00% |
| 600990.SH | 四创电子 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.18% < 6.00%; excess_return_120d -43.76% < 6.00%; excess_return_240d -51.20% < 8.00%; drawdown_120d -49.71% < -28.00%; volatility_120d 43.09% > 42.00% |
| 300411.SZ | 金盾股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.44% < 6.00%; excess_return_120d -43.93% < 6.00%; excess_return_240d -66.49% < 8.00%; drawdown_120d -47.65% < -28.00%; volatility_120d 63.48% > 42.00% |
| 688084.SH | 晶品特装 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.48% < 6.00%; excess_return_120d -44.06% < 6.00%; excess_return_240d -65.51% < 8.00%; drawdown_120d -52.72% < -28.00%; volatility_120d 57.93% > 42.00% |
| 000561.SZ | 烽火电子 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.53% < 6.00%; excess_return_120d -44.11% < 6.00%; excess_return_240d -47.20% < 8.00%; drawdown_120d -49.14% < -28.00%; volatility_120d 46.81% > 42.00% |
| 000555.SZ | 神州信息 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.54% < 6.00%; excess_return_120d -44.12% < 6.00%; excess_return_240d -50.67% < 8.00%; drawdown_120d -50.74% < -28.00%; volatility_120d 51.60% > 42.00% |
| 300638.SZ | 广和通 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.91% < 6.00%; excess_return_120d -44.49% < 6.00%; excess_return_240d -54.51% < 8.00%; drawdown_120d -51.10% < -28.00%; volatility_120d 54.21% > 42.00% |
| 301556.SZ | 托普云农 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.97% < 6.00%; excess_return_120d -44.55% < 6.00%; excess_return_240d -57.34% < 8.00%; drawdown_120d -65.00% < -28.00%; volatility_120d 56.13% > 42.00% |
| 600284.SH | 浦东建设 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.98% < 6.00%; excess_return_120d -44.56% < 6.00%; excess_return_240d -43.82% < 8.00%; drawdown_120d -47.20% < -28.00%; volatility_120d 43.30% > 42.00% |
| 301052.SZ | 果麦文化 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.98% < 6.00%; excess_return_120d -44.56% < 6.00%; excess_return_240d -66.20% < 8.00%; drawdown_120d -52.56% < -28.00%; volatility_120d 50.03% > 42.00% |
| 300250.SZ | 初灵信息 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -39.99% < 6.00%; excess_return_120d -44.57% < 6.00%; excess_return_240d -32.52% < 8.00%; drawdown_120d -53.23% < -28.00%; volatility_120d 47.42% > 42.00% |
| 600850.SH | 电科数字 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.04% < 6.00%; excess_return_120d -44.62% < 6.00%; excess_return_240d -47.14% < 8.00%; drawdown_120d -50.65% < -28.00%; volatility_120d 53.33% > 42.00% |
| 300680.SZ | 隆盛科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.13% < 6.00%; excess_return_120d -44.71% < 6.00%; excess_return_240d -25.86% < 8.00%; drawdown_120d -47.33% < -28.00%; volatility_120d 52.80% > 42.00% |
| 000678.SZ | 襄阳轴承 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.25% < 6.00%; excess_return_120d -44.83% < 6.00%; excess_return_240d -62.79% < 8.00%; drawdown_120d -45.58% < -28.00%; volatility_120d 47.39% > 42.00% |
| 300911.SZ | 亿田智能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.30% < 6.00%; excess_return_120d -44.88% < 6.00%; excess_return_240d -75.04% < 8.00%; drawdown_120d -60.17% < -28.00%; volatility_120d 76.75% > 42.00% |
| 002766.SZ | 索菱股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.33% < 6.00%; excess_return_120d -44.91% < 6.00%; excess_return_240d -52.85% < 8.00%; drawdown_120d -55.21% < -28.00%; volatility_120d 52.04% > 42.00% |
| 002535.SZ | 林州重机 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.46% < 6.00%; excess_return_120d -45.04% < 6.00%; excess_return_240d -63.63% < 8.00%; drawdown_120d -44.74% < -28.00%; volatility_120d 43.22% > 42.00% |
| 301066.SZ | 万事利 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.58% < 6.00%; excess_return_120d -45.16% < 6.00%; excess_return_240d -48.93% < 8.00%; drawdown_120d -54.82% < -28.00%; volatility_120d 55.17% > 42.00% |
| 603696.SH | 安记食品 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -40.67% < 6.00%; excess_return_120d -45.25% < 6.00%; excess_return_240d -14.71% < 8.00%; drawdown_120d -57.83% < -28.00%; volatility_120d 44.95% > 42.00% |
| 300605.SZ | 恒锋信息 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -40.70% < 6.00%; excess_return_120d -45.28% < 6.00%; excess_return_240d -57.40% < 8.00%; drawdown_120d -48.64% < -28.00%; volatility_120d 43.70% > 42.00% |
| 688326.SH | 经纬恒润 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -40.71% < 6.00%; excess_return_120d -45.29% < 6.00%; excess_return_240d -38.16% < 8.00%; drawdown_120d -57.47% < -28.00%; volatility_120d 54.65% > 42.00% |
| 300189.SZ | 神农种业 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -40.99% < 6.00%; excess_return_120d -45.57% < 6.00%; excess_return_240d -28.87% < 8.00%; drawdown_120d -55.79% < -28.00%; volatility_120d 58.83% > 42.00% |
| 300180.SZ | 华峰超纤 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -41.08% < 6.00%; excess_return_120d -45.66% < 6.00%; excess_return_240d -80.05% < 8.00%; drawdown_120d -44.45% < -28.00%; volatility_120d 43.33% > 42.00% |
| 603200.SH | 上海洗霸 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -41.13% < 6.00%; excess_return_120d -45.71% < 6.00%; excess_return_240d -37.06% < 8.00%; drawdown_120d -53.98% < -28.00%; volatility_120d 47.32% > 42.00% |
| 300061.SZ | 旗天科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -41.16% < 6.00%; excess_return_120d -45.74% < 6.00%; excess_return_240d -75.52% < 8.00%; drawdown_120d -48.20% < -28.00%; volatility_120d 64.52% > 42.00% |
| 000997.SZ | 新大陆 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -41.30% < 6.00%; excess_return_120d -45.88% < 6.00%; excess_return_240d -70.16% < 8.00%; drawdown_120d -47.44% < -28.00%; volatility_120d 43.57% > 42.00% |
| 603131.SH | 上海沪工 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -41.45% < 6.00%; excess_return_120d -46.03% < 6.00%; excess_return_240d -23.57% < 8.00%; drawdown_120d -49.66% < -28.00%; volatility_120d 52.59% > 42.00% |
| 300045.SZ | 华力创通 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -41.51% < 6.00%; excess_return_120d -46.09% < 6.00%; excess_return_240d -31.05% < 8.00%; drawdown_120d -56.19% < -28.00%; volatility_120d 58.76% > 42.00% |
| 601595.SH | 上海电影 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -41.56% < 6.00%; excess_return_120d -46.14% < 6.00%; excess_return_240d -61.27% < 8.00%; drawdown_120d -54.98% < -28.00%; volatility_120d 43.55% > 42.00% |
| 688051.SH | 佳华科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -41.58% < 6.00%; excess_return_120d -46.16% < 6.00%; excess_return_240d -28.64% < 8.00%; drawdown_120d -54.49% < -28.00%; volatility_120d 61.28% > 42.00% |
| 300386.SZ | 飞天诚信 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -41.77% < 6.00%; excess_return_120d -46.35% < 6.00%; excess_return_240d -74.05% < 8.00%; drawdown_120d -43.86% < -28.00%; volatility_120d 48.19% > 42.00% |
| 301357.SZ | 北方长龙 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -42.28% < 6.00%; excess_return_120d -46.86% < 6.00%; excess_return_240d -25.20% < 8.00%; drawdown_120d -49.94% < -28.00%; volatility_120d 49.20% > 42.00% |
| 002474.SZ | 榕基软件 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -42.39% < 6.00%; excess_return_120d -46.97% < 6.00%; excess_return_240d -41.10% < 8.00%; drawdown_120d -49.73% < -28.00%; volatility_120d 47.93% > 42.00% |
| 002177.SZ | 御银股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -42.40% < 6.00%; excess_return_120d -46.98% < 6.00%; excess_return_240d -46.99% < 8.00%; drawdown_120d -47.38% < -28.00%; volatility_120d 56.93% > 42.00% |
| 002197.SZ | 证通电子 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -42.98% < 6.00%; excess_return_120d -47.56% < 6.00%; excess_return_240d -44.56% < 8.00%; drawdown_120d -48.89% < -28.00%; volatility_120d 49.06% > 42.00% |
| 300551.SZ | 古鳌科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -43.09% < 6.00%; excess_return_120d -47.67% < 6.00%; excess_return_240d -32.27% < 8.00%; drawdown_120d -54.88% < -28.00%; volatility_120d 51.26% > 42.00% |
| 300101.SZ | 振芯科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -43.23% < 6.00%; excess_return_120d -47.81% < 6.00%; excess_return_240d -48.36% < 8.00%; drawdown_120d -55.04% < -28.00%; volatility_120d 52.01% > 42.00% |
| 688776.SH | 国光电气 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -43.27% < 6.00%; excess_return_120d -47.85% < 6.00%; excess_return_240d -64.25% < 8.00%; drawdown_120d -61.90% < -28.00%; volatility_120d 58.68% > 42.00% |
| 300997.SZ | 欢乐家 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -43.30% < 6.00%; excess_return_120d -47.88% < 6.00%; excess_return_240d -33.26% < 8.00%; drawdown_120d -55.93% < -28.00%; volatility_120d 53.89% > 42.00% |
| 688648.SH | 中邮科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -43.38% < 6.00%; excess_return_120d -47.96% < 6.00%; excess_return_240d -40.63% < 8.00%; drawdown_120d -52.39% < -28.00%; volatility_120d 56.28% > 42.00% |
| 002769.SZ | 普路通 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -43.41% < 6.00%; excess_return_120d -47.99% < 6.00%; excess_return_240d -54.60% < 8.00%; drawdown_120d -56.07% < -28.00%; volatility_120d 46.30% > 42.00% |
| 603121.SH | 华培动力 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -42.73% < 6.00%; excess_return_120d -48.46% < 6.00%; excess_return_240d -72.20% < 8.00%; drawdown_120d -52.78% < -28.00%; volatility_120d 60.16% > 42.00% |
| 301136.SZ | 招标股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -44.23% < 6.00%; excess_return_120d -48.81% < 6.00%; excess_return_240d -32.47% < 8.00%; drawdown_120d -54.60% < -28.00%; volatility_120d 55.35% > 42.00% |
| 300774.SZ | 倍杰特 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -44.24% < 6.00%; excess_return_120d -48.82% < 6.00%; excess_return_240d -2.15% < 8.00%; drawdown_120d -63.33% < -28.00%; volatility_120d 74.43% > 42.00% |
| 600592.SH | 龙溪股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -44.61% < 6.00%; excess_return_120d -49.19% < 6.00%; excess_return_240d -49.46% < 8.00%; drawdown_120d -46.15% < -28.00%; volatility_120d 46.03% > 42.00% |
| 603878.SH | 武进不锈 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -44.63% < 6.00%; excess_return_120d -49.21% < 6.00%; excess_return_240d -28.87% < 8.00%; drawdown_120d -47.58% < -28.00%; volatility_120d 51.99% > 42.00% |
| 002383.SZ | 合众思壮 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -44.72% < 6.00%; excess_return_120d -49.30% < 6.00%; excess_return_240d -54.49% < 8.00%; drawdown_120d -55.01% < -28.00%; volatility_120d 46.42% > 42.00% |
| 002829.SZ | 星网宇达 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -45.07% < 6.00%; excess_return_120d -49.65% < 6.00%; excess_return_240d -38.71% < 8.00%; drawdown_120d -51.64% < -28.00%; volatility_120d 51.60% > 42.00% |
| 002368.SZ | 太极股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -45.16% < 6.00%; excess_return_120d -49.74% < 6.00%; excess_return_240d -62.37% < 8.00%; drawdown_120d -51.36% < -28.00%; volatility_120d 43.10% > 42.00% |
| 605365.SH | 立达信 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -45.45% < 6.00%; excess_return_120d -50.03% < 6.00%; excess_return_240d -22.13% < 8.00%; drawdown_120d -56.93% < -28.00%; volatility_120d 58.25% > 42.00% |
| 000980.SZ | 众泰汽车 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -45.61% < 6.00%; excess_return_120d -50.19% < 6.00%; excess_return_240d -28.34% < 8.00%; drawdown_120d -48.53% < -28.00%; volatility_120d 55.52% > 42.00% |
| 600363.SH | 联创光电 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -45.64% < 6.00%; excess_return_120d -50.22% < 6.00%; excess_return_240d -61.58% < 8.00%; drawdown_120d -56.48% < -28.00%; volatility_120d 52.25% > 42.00% |
| 301155.SZ | 海力风电 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -45.72% < 6.00%; excess_return_120d -50.30% < 6.00%; excess_return_240d -61.00% < 8.00%; drawdown_120d -53.27% < -28.00%; volatility_120d 56.42% > 42.00% |
| 300086.SZ | 康芝药业 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -45.89% < 6.00%; excess_return_120d -50.47% < 6.00%; excess_return_240d -4.85% < 8.00%; drawdown_120d -47.50% < -28.00%; volatility_120d 51.82% > 42.00% |
| 000892.SZ | 欢瑞世纪 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -46.13% < 6.00%; excess_return_120d -50.71% < 6.00%; excess_return_240d -41.10% < 8.00%; drawdown_120d -61.90% < -28.00%; volatility_120d 66.65% > 42.00% |
| 600113.SH | 浙江东日 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -46.30% < 6.00%; excess_return_120d -50.88% < 6.00%; excess_return_240d -1.78% < 8.00%; drawdown_120d -48.50% < -28.00%; volatility_120d 47.31% > 42.00% |
| 300703.SZ | 创源股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -46.47% < 6.00%; excess_return_120d -51.05% < 6.00%; excess_return_240d -62.47% < 8.00%; drawdown_120d -55.78% < -28.00%; volatility_120d 46.39% > 42.00% |
| 603567.SH | 珍宝岛 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -46.58% < 6.00%; excess_return_120d -51.16% < 6.00%; excess_return_240d -80.19% < 8.00%; drawdown_120d -52.06% < -28.00%; volatility_120d 46.77% > 42.00% |
| 300465.SZ | 高伟达 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -47.29% < 6.00%; excess_return_120d -51.87% < 6.00%; excess_return_240d -61.22% < 8.00%; drawdown_120d -53.83% < -28.00%; volatility_120d 48.68% > 42.00% |
| 300368.SZ | 汇金股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -47.49% < 6.00%; excess_return_120d -52.07% < 6.00%; excess_return_240d -58.71% < 8.00%; drawdown_120d -51.23% < -28.00%; volatility_120d 56.14% > 42.00% |
| 300468.SZ | 四方精创 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -47.51% < 6.00%; excess_return_120d -52.09% < 6.00%; excess_return_240d -79.68% < 8.00%; drawdown_120d -48.88% < -28.00%; volatility_120d 50.34% > 42.00% |
| 600865.SH | 百大集团 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -48.17% < 6.00%; excess_return_120d -52.75% < 6.00%; excess_return_240d -27.90% < 8.00%; drawdown_120d -54.86% < -28.00%; volatility_120d 43.51% > 42.00% |
| 688639.SH | 华恒生物 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -48.21% < 6.00%; excess_return_120d -52.79% < 6.00%; excess_return_240d -67.30% < 8.00%; drawdown_120d -61.35% < -28.00%; volatility_120d 55.23% > 42.00% |
| 300427.SZ | 红相股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -48.24% < 6.00%; excess_return_120d -52.83% < 6.00%; excess_return_240d -30.78% < 8.00%; drawdown_120d -67.87% < -28.00%; volatility_120d 78.25% > 42.00% |
| 002544.SZ | 普天科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -48.71% < 6.00%; excess_return_120d -53.29% < 6.00%; excess_return_240d -44.16% < 8.00%; drawdown_120d -57.93% < -28.00%; volatility_120d 43.84% > 42.00% |
| 300940.SZ | 南极光 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -48.77% < 6.00%; excess_return_120d -53.35% < 6.00%; excess_return_240d -61.54% < 8.00%; drawdown_120d -56.81% < -28.00%; volatility_120d 47.05% > 42.00% |
| 600501.SH | 航天晨光 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -48.79% < 6.00%; excess_return_120d -53.37% < 6.00%; excess_return_240d -44.41% < 8.00%; drawdown_120d -61.40% < -28.00%; volatility_120d 47.10% > 42.00% |
| 002682.SZ | 龙洲股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -49.47% < 6.00%; excess_return_120d -54.06% < 6.00%; excess_return_240d -32.91% < 8.00%; drawdown_120d -51.89% < -28.00%; volatility_120d 44.22% > 42.00% |
| 603360.SH | 百傲化学 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -50.03% < 6.00%; excess_return_120d -54.61% < 6.00%; excess_return_240d -42.83% < 8.00%; drawdown_120d -58.70% < -28.00%; volatility_120d 66.80% > 42.00% |
| 300111.SZ | 向日葵 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -50.08% < 6.00%; excess_return_120d -54.66% < 6.00%; excess_return_240d -31.30% < 8.00%; drawdown_120d -60.21% < -28.00%; volatility_120d 69.55% > 42.00% |
| 603185.SH | 弘元绿能 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -50.21% < 6.00%; excess_return_120d -54.79% < 6.00%; excess_return_240d -28.06% < 8.00%; drawdown_120d -52.91% < -28.00%; volatility_120d 48.01% > 42.00% |
| 300492.SZ | 华图山鼎 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -50.74% < 6.00%; excess_return_120d -55.32% < 6.00%; excess_return_240d -64.17% < 8.00%; drawdown_120d -61.33% < -28.00%; volatility_120d 52.15% > 42.00% |
| 603123.SH | 翠微股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -51.16% < 6.00%; excess_return_120d -55.74% < 6.00%; excess_return_240d -65.74% < 8.00%; drawdown_120d -50.36% < -28.00%; volatility_120d 49.34% > 42.00% |
| 688089.SH | 嘉必优 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -52.41% < 6.00%; excess_return_120d -56.99% < 6.00%; excess_return_240d -76.58% < 8.00%; drawdown_120d -54.40% < -28.00%; volatility_120d 46.54% > 42.00% |
| 002347.SZ | 泰尔股份 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; stock_return_120d -52.75% < 6.00%; excess_return_120d -57.33% < 6.00%; excess_return_240d -40.30% < 8.00%; drawdown_120d -59.77% < -28.00%; volatility_120d 42.12% > 42.00% |
| 300087.SZ | 荃银高科 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -55.23% < 6.00%; excess_return_120d -59.53% < 6.00%; excess_return_240d -65.29% < 8.00%; drawdown_120d -55.91% < -28.00%; volatility_120d 52.22% > 42.00% |
| 300255.SZ | 常山药业 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -60.05% < 6.00%; excess_return_120d -64.63% < 6.00%; excess_return_240d -59.87% < 8.00%; drawdown_120d -61.53% < -28.00%; volatility_120d 64.30% > 42.00% |
| 300663.SZ | 科蓝软件 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -62.76% < 6.00%; excess_return_120d -67.34% < 6.00%; excess_return_240d -90.37% < 8.00%; drawdown_120d -68.28% < -28.00%; volatility_120d 50.58% > 42.00% |
| 300290.SZ | 荣科科技 | ok | 18.00 | close_below_ma200; ma60_not_above_ma120; ma120_not_above_ma200; stock_return_120d -83.78% < 6.00%; excess_return_120d -87.89% < 6.00%; excess_return_240d -95.84% < 8.00%; drawdown_120d -84.98% < -28.00%; volatility_120d 70.75% > 42.00% |
| 688820.SH | 盛合晶微 | ok | 0.00 | history_days 51 < 260 |
| 688818.SH | 电科蓝天 | ok | 0.00 | history_days 94 < 260 |
| 688816.SH | 易思维 | ok | 0.00 | history_days 93 < 260 |
| 688813.SH | 泰金新能 | ok | 0.00 | history_days 65 < 260 |
| 688811.SH | 有研复材 | ok | 0.00 | history_days 58 < 260 |
| 688809.SH | 强一股份 | ok | 0.00 | history_days 122 < 260 |
| 688808.SH | 联讯仪器 | ok | 0.00 | history_days 48 < 260 |
| 688807.SH | 优迅股份 | ok | 0.00 | history_days 129 < 260 |
| 688805.SH | 健信超导 | ok | 0.00 | history_days 126 < 260 |
| 688802.SH | 沐曦股份 | ok | 0.00 | history_days 131 < 260 |
| 688797.SH | 臻宝科技 | ok | 0.00 | history_days 9 < 260 |
| 688796.SH | 百奥赛图 | ok | 0.00 | history_days 136 < 260 |
| 688795.SH | 摩尔线程 | ok | 0.00 | history_days 139 < 260 |
| 688790.SH | 昂瑞微 | ok | 0.00 | history_days 132 < 260 |
| 688785.SH | 恒运昌 | ok | 0.00 | history_days 103 < 260 |
| 688783.SH | 西安奕材 | ok | 0.00 | history_days 167 < 260 |
| 688781.SH | 视涯科技 | ok | 0.00 | history_days 69 < 260 |
| 688765.SH | 禾元生物 | ok | 0.00 | history_days 167 < 260 |
| 688759.SH | 必贝特 | ok | 0.00 | history_days 167 < 260 |
| 688729.SH | 屹唐股份 | ok | 0.00 | history_days 241 < 260 |
| 688727.SH | 恒坤新材 | ok | 0.00 | history_days 152 < 260 |
| 688712.SH | 北芯生命 | ok | 0.00 | history_days 97 < 260 |
| 688635.SH | 长进光子 | ok | 0.00 | history_days 28 < 260 |
| 603459.SH | 红板科技 | ok | 0.00 | history_days 60 < 260 |
| 603435.SH | 嘉德利 | ok | 0.00 | history_days 31 < 260 |
| 603418.SH | 友升股份 | ok | 0.00 | history_days 186 < 260 |
| 603407.SH | 长裕集团 | ok | 0.00 | history_days 40 < 260 |
| 603406.SH | 天富龙 | ok | 0.00 | history_days 218 < 260 |
| 603402.SH | 陕西旅游 | ok | 0.00 | history_days 119 < 260 |
| 603400.SH | 华之杰 | ok | 0.00 | history_days 253 < 260 |
| 603382.SH | 海阳科技 | ok | 0.00 | history_days 259 < 260 |
| 603376.SH | 大明电子 | ok | 0.00 | history_days 160 < 260 |
| 603370.SH | 华新精科 | ok | 0.00 | history_days 198 < 260 |
| 603361.SH | 浙江国祥 | ok | 0.00 | history_days 0 < 260 |
| 603352.SH | 至信股份 | ok | 0.00 | history_days 112 < 260 |
| 603334.SH | 丰倍生物 | ok | 0.00 | history_days 161 < 260 |
| 603293.SH | 埃泰克 | ok | 0.00 | history_days 54 < 260 |
| 603284.SH | 林平发展 | ok | 0.00 | history_days 94 < 260 |
| 603262.SH | 技源集团 | ok | 0.00 | history_days 230 < 260 |
| 603175.SH | 超颖电子 | ok | 0.00 | history_days 169 < 260 |
| 603092.SH | 德力佳 | ok | 0.00 | history_days 159 < 260 |
| 601112.SH | 振石股份 | ok | 0.00 | history_days 102 < 260 |
| 601026.SH | 道生天合 | ok | 0.00 | history_days 174 < 260 |
| 600930.SH | 华电新能 | ok | 0.00 | history_days 235 < 260 |
| 301696.SZ | 三瑞智能 | ok | 0.00 | history_days 58 < 260 |
| 301687.SZ | 新广益 | ok | 0.00 | history_days 121 < 260 |
| 301683.SZ | 慧谷新材 | ok | 0.00 | history_days 64 < 260 |
| 301682.SZ | 宏明电子 | ok | 0.00 | history_days 69 < 260 |
| 301680.SZ | 固德电材 | ok | 0.00 | history_days 82 < 260 |
| 301678.SZ | 新恒汇 | ok | 0.00 | history_days 253 < 260 |
| 301669.SZ | 高特电子 | ok | 0.00 | history_days 19 < 260 |
| 301668.SZ | 昊创瑞通 | ok | 0.00 | history_days 183 < 260 |
| 301667.SZ | 纳百川 | ok | 0.00 | history_days 127 < 260 |
| 301666.SZ | 大普微 | ok | 0.00 | history_days 51 < 260 |
| 301656.SZ | 联合动力 | ok | 0.00 | history_days 184 < 260 |
| 301638.SZ | 南网数字 | ok | 0.00 | history_days 152 < 260 |
| 301632.SZ | 广东建科 | ok | 0.00 | history_days 216 < 260 |
| 301630.SZ | 同宇新材 | ok | 0.00 | history_days 239 < 260 |
| 301609.SZ | 山大电力 | ok | 0.00 | history_days 230 < 260 |
| 301599.SZ | 理奇智能 | ok | 0.00 | history_days 44 < 260 |
| 301584.SZ | 建发致新 | ok | 0.00 | history_days 184 < 260 |
| 301575.SZ | 艾芬达 | ok | 0.00 | history_days 195 < 260 |
| 301563.SZ | 云汉芯城 | ok | 0.00 | history_days 181 < 260 |
| 301531.SZ | 春光集团 | ok | 0.00 | history_days 40 < 260 |
| 301513.SZ | 尚水智能 | ok | 0.00 | history_days 53 < 260 |
| 301491.SZ | 汉桑科技 | ok | 0.00 | history_days 220 < 260 |
| 301449.SZ | 天溯计量 | ok | 0.00 | history_days 127 < 260 |
| 001399.SZ | 惠科股份 | ok | 0.00 | history_days 7 < 260 |
| 001396.SZ | 誉帆科技 | ok | 0.00 | history_days 122 < 260 |
| 001393.SZ | 维通利 | ok | 0.00 | history_days 36 < 260 |
| 001388.SZ | 信通电子 | ok | 0.00 | history_days 246 < 260 |
| 001386.SZ | 马可波罗 | ok | 0.00 | history_days 171 < 260 |
| 001369.SZ | 双欣材料 | ok | 0.00 | history_days 122 < 260 |
| 001365.SZ | 天海电子 | ok | 0.00 | history_days 35 < 260 |
| 001325.SZ | 元创股份 | ok | 0.00 | history_days 130 < 260 |
| 001312.SZ | 福恩股份 | ok | 0.00 | history_days 51 < 260 |
| 001285.SZ | 瑞立科密 | ok | 0.00 | history_days 171 < 260 |
| 001280.SZ | 中国铀业 | ok | 0.00 | history_days 141 < 260 |
| 001257.SZ | 盛龙股份 | ok | 0.00 | history_days 65 < 260 |
| 001237.SZ | 惠康科技 | ok | 0.00 | history_days 31 < 260 |
| 001235.SZ | 里得电科 | ok | 0.00 | history_days 0 < 260 |
| 001233.SZ | 海安集团 | ok | 0.00 | history_days 147 < 260 |
| 001221.SZ | 悍高集团 | ok | 0.00 | history_days 225 < 260 |
| 001220.SZ | 世盟股份 | ok | 0.00 | history_days 99 < 260 |

This is a research scanner for paper trading. It does not place orders or guarantee returns.
