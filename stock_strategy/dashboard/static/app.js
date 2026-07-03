(function () {
  const appShell = document.querySelector(".app-shell");
  const apiUrl = appShell.dataset.api;
  const fileBase = appShell.dataset.fileBase || "/files";
  const refreshButton = document.getElementById("refresh-button");
  const chartCanvas = document.getElementById("market-chart");
  const strategyListElement = document.getElementById("strategy-list");
  const strategyOrder = window.StrategyOrder;
  const holdingsPanel = window.HoldingsPanel;
  const strategyOrderStorageKey = "finance_lab.strategy_order.v1";
  let latestDashboard = null;
  let selectedStrategyId = "";
  let draggedStrategyId = "";
  let dragClickGuard = false;
  let pointerDrag = null;

  function text(value, fallback = "--") {
    if (value === null || value === undefined || value === "") return fallback;
    return String(value);
  }

  function number(value, digits = 2) {
    const numeric = Number(value);
    if (!Number.isFinite(numeric)) return "--";
    return numeric.toFixed(digits);
  }

  function percent(value, digits = 1) {
    const numeric = Number(value);
    if (!Number.isFinite(numeric)) return "--";
    return `${(numeric * 100).toFixed(digits)}%`;
  }

  function signedPercent(value, digits = 1) {
    const numeric = Number(value);
    if (!Number.isFinite(numeric)) return "--";
    const sign = numeric > 0 ? "+" : "";
    return `${sign}${(numeric * 100).toFixed(digits)}%`;
  }

  function escapeHtml(value) {
    return text(value, "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function badge(label, tone) {
    return `<span class="badge ${tone || ""}">${escapeHtml(label)}</span>`;
  }

  function tone(value) {
    return ["bad", "good", "info", "warn"].includes(value) ? value : "";
  }

  function fileUrl(path) {
    const encodedPath = String(path).split("/").map(encodeURIComponent).join("/");
    const base = fileBase.endsWith("/") ? fileBase.slice(0, -1) : fileBase;
    return `${base}/${encodedPath}`;
  }

  function artifactLink(item) {
    if (!item || !item.path) return `<span class="muted">暂无</span>`;
    const label = escapeHtml(item.label || item.path);
    const path = escapeHtml(item.path);
    const kind = escapeHtml((item.kind || "file").toUpperCase());
    if (!item.exists) {
      return `<span class="artifact missing"><span class="artifact-label">${label}<small>${kind}</small></span><code>${path}</code></span>`;
    }
    return `<a class="artifact" href="${fileUrl(item.path)}" target="_blank" rel="noreferrer"><span class="artifact-label">${label}<small>${kind}</small></span><code>${path}</code></a>`;
  }

  function detailBlock(title, items) {
    const rows = (items || []).filter(Boolean);
    return `
      <div class="detail-block">
        <h3>${escapeHtml(title)}</h3>
        ${
          rows.length
            ? `<ul>${rows.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ul>`
            : `<div class="empty slim">暂无</div>`
        }
      </div>
    `;
  }

  function artifactBlock(title, items) {
    const rows = (items || []).filter(Boolean);
    return `
      <div class="detail-block artifact-block">
        <h3>${escapeHtml(title)}</h3>
        ${
          rows.length
            ? `<ul>${rows.map((item) => `<li>${artifactLink(item)}</li>`).join("")}</ul>`
            : `<div class="empty slim">暂无</div>`
        }
      </div>
    `;
  }

  function firstExistingArtifact(strategy) {
    const rows = [
      ...(strategy.reports || []),
      ...(strategy.docs || []),
      ...(strategy.scripts || []),
    ];
    return rows.find((item) => item && item.exists && item.path) || rows.find((item) => item && item.path);
  }

  function artifactCount(strategy) {
    return [
      ...(strategy.reports || []),
      ...(strategy.docs || []),
      ...(strategy.scripts || []),
    ].filter((item) => item && item.exists && item.path).length;
  }

  function readStrategyOrder() {
    try {
      const value = window.localStorage.getItem(strategyOrderStorageKey);
      const parsed = value ? JSON.parse(value) : [];
      return Array.isArray(parsed) ? parsed.filter((item) => typeof item === "string") : [];
    } catch {
      return [];
    }
  }

  function saveStrategyOrder(orderIds) {
    try {
      window.localStorage.setItem(strategyOrderStorageKey, JSON.stringify(orderIds));
    } catch {
      // Browsers can block localStorage in strict privacy modes; sorting still works until refresh.
    }
  }

  function orderedStrategyCatalog(catalog) {
    if (!strategyOrder) return catalog;
    return strategyOrder.applyStoredOrder(catalog, readStrategyOrder());
  }

  function renderedStrategyIds() {
    return Array.from(strategyListElement.querySelectorAll(".strategy-card"))
      .map((card) => card.dataset.strategyId)
      .filter(Boolean);
  }

  function strategyCardFromEvent(event) {
    const target = event.target instanceof Element ? event.target : null;
    return target ? target.closest(".strategy-card") : null;
  }

  function strategyCardFromPoint(clientX, clientY) {
    const target = document.elementFromPoint(clientX, clientY);
    return target ? target.closest(".strategy-card") : null;
  }

  function strategyCardById(strategyId) {
    return Array.from(strategyListElement.querySelectorAll(".strategy-card"))
      .find((card) => card.dataset.strategyId === strategyId);
  }

  function clearDragMarkers() {
    strategyListElement.classList.remove("dragging");
    strategyListElement.querySelectorAll(".strategy-card").forEach((card) => {
      card.classList.remove("dragging", "drag-before", "drag-after");
      card.removeAttribute("aria-grabbed");
    });
  }

  function shouldDropAfter(event, card) {
    const rect = card.getBoundingClientRect();
    const midX = rect.left + rect.width / 2;
    const midY = rect.top + rect.height / 2;
    const horizontalIntent = Math.abs(event.clientX - midX) > Math.abs(event.clientY - midY);
    return horizontalIntent ? event.clientX > midX : event.clientY > midY;
  }

  function previewDropTarget(card, event) {
    clearDragMarkers();
    strategyListElement.classList.add("dragging");
    const draggedCard = strategyCardById(draggedStrategyId);
    draggedCard?.classList.add("dragging");
    draggedCard?.setAttribute("aria-grabbed", "true");
    if (!card || card.dataset.strategyId === draggedStrategyId) return;
    card.classList.add(shouldDropAfter(event, card) ? "drag-after" : "drag-before");
  }

  function commitDraggedOrder(card, event) {
    if (!draggedStrategyId || !strategyOrder) return;
    const targetId = card?.dataset.strategyId || "";
    const orderIds = renderedStrategyIds();
    const lastId = orderIds.filter((id) => id !== draggedStrategyId).at(-1);
    const nextOrder = targetId
      ? shouldDropAfter(event, card)
        ? strategyOrder.moveAfter(orderIds, draggedStrategyId, targetId)
        : strategyOrder.moveBefore(orderIds, draggedStrategyId, targetId)
      : strategyOrder.moveAfter(orderIds, draggedStrategyId, lastId);

    saveStrategyOrder(nextOrder);
    guardNextClickAfterDrag();
    if (latestDashboard) renderStrategyCatalog(latestDashboard);
  }

  function guardNextClickAfterDrag() {
    dragClickGuard = true;
    window.setTimeout(() => {
      dragClickGuard = false;
    }, 250);
  }

  function selectStrategy(strategyId, shouldScroll) {
    selectedStrategyId = strategyId;
    if (latestDashboard) renderStrategyCatalog(latestDashboard);
    if (shouldScroll) {
      document.querySelector(".strategy-detail-panel")?.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }

  function renderStrategyCatalog(data) {
    const catalog = orderedStrategyCatalog(data.strategy_catalog || []);
    const statsTarget = document.getElementById("strategy-stats");
    const detailTarget = document.getElementById("strategy-detail");
    const matrixTarget = document.getElementById("strategy-matrix");

    if (!catalog.length) {
      statsTarget.innerHTML = "";
      strategyListElement.innerHTML = `<div class="empty">暂无策略目录。</div>`;
      detailTarget.innerHTML = `<div class="empty">暂无策略详情。</div>`;
      if (matrixTarget) matrixTarget.innerHTML = `<div class="empty">暂无策略矩阵。</div>`;
      return;
    }

    if (!selectedStrategyId || !catalog.some((item) => item.id === selectedStrategyId)) {
      selectedStrategyId = catalog[0].id;
    }
    const selected = catalog.find((item) => item.id === selectedStrategyId) || catalog[0];
    const reportCount = catalog.flatMap((item) => item.reports || []).filter((item) => item.exists).length;
    const productionCount = catalog.filter((item) => item.tone === "good").length;
    const researchCount = catalog.filter((item) => item.tone === "warn").length;

    statsTarget.innerHTML = [
      ["策略数量", catalog.length],
      ["生产/增强", productionCount],
      ["研究/纸面", researchCount],
      ["可点产物", reportCount],
    ]
      .map(([label, value]) => `<div class="strategy-stat"><span>${escapeHtml(label)}</span><strong>${escapeHtml(value)}</strong></div>`)
      .join("");

    strategyListElement.innerHTML = catalog
      .map(
        (item) => {
          const artifact = firstExistingArtifact(item);
          const outputs = item.outputs || [];
          const activeClass = item.id === selected.id ? "active" : "";
          return `
          <button class="strategy-card ${activeClass}" type="button" data-strategy-id="${escapeHtml(item.id)}" aria-label="${escapeHtml(item.name)}，拖动排序，点击查看详情">
            <span class="strategy-card-head">
              ${badge(item.status, tone(item.tone))}
              <span class="strategy-card-tools">
                <span class="strategy-card-grip" aria-hidden="true"></span>
                <span class="strategy-card-count">${artifactCount(item)} 个产物</span>
              </span>
            </span>
            <strong class="strategy-card-title">${escapeHtml(item.name)}</strong>
            <span class="strategy-card-mode">${escapeHtml(item.mode || item.cadence || "--")}</span>
            <span class="strategy-card-objective">${escapeHtml(item.objective || "暂无策略说明。")}</span>
            <span class="strategy-card-meta">
              <span><small>节奏</small><b>${escapeHtml(item.cadence || "--")}</b></span>
              <span><small>信号</small><b>${escapeHtml(String((item.signals || []).length))}</b></span>
              <span><small>输出</small><b>${escapeHtml(String(outputs.length))}</b></span>
            </span>
            <span class="strategy-card-footer">
              <span>${artifact ? escapeHtml(artifact.label || "最新产物") : "暂无产物"}</span>
              <em>查看详情</em>
            </span>
          </button>
        `;
        }
      )
      .join("");

    const metrics = (selected.metrics || [])
      .map((item) => `<div class="mini-metric"><span>${escapeHtml(item.label)}</span><strong>${escapeHtml(item.value)}</strong></div>`)
      .join("");
    const workflowNotes = new Map(
      (selected.workflow_notes || []).map((item) => [item.label, item.description])
    );
    const workflow = (selected.workflow || [])
      .map((item, index) => {
        const description = workflowNotes.get(item);
        return `
          <span>
            <small>${index + 1}</small>
            <strong>${escapeHtml(item)}</strong>
            ${description ? `<em>${escapeHtml(description)}</em>` : ""}
          </span>
        `;
      })
      .join("");

    detailTarget.innerHTML = `
      <section class="strategy-detail-module">
        <div class="strategy-detail-header">
          <div>
            <div class="strategy-badges">
              ${badge(selected.status, tone(selected.tone))}
              ${badge(selected.mode || "--", "info")}
              ${badge(selected.cadence || "--", "")}
            </div>
            <h2>${escapeHtml(selected.name)}</h2>
            <p>${escapeHtml(selected.objective)}</p>
          </div>
        </div>
        <div class="strategy-flow">${workflow}</div>
        <div class="mini-metric-grid">${metrics}</div>
        <div class="detail-grid">
          ${detailBlock("核心信号", selected.signals)}
          ${detailBlock("风控边界", selected.risk_controls)}
          ${detailBlock("输出结果", selected.outputs)}
          ${detailBlock("限制说明", selected.limits)}
          ${artifactBlock("报告产物", selected.reports)}
          ${artifactBlock("代码与文档", [...(selected.scripts || []), ...(selected.docs || [])])}
        </div>
      </section>
    `;

    if (matrixTarget) matrixTarget.innerHTML = "";
  }

  function setMetricList(elementId, rows) {
    const target = document.getElementById(elementId);
    target.innerHTML = rows
      .map(([label, value]) => `<div><dt>${escapeHtml(label)}</dt><dd>${value}</dd></div>`)
      .join("");
  }

  function renderActionPanel(data) {
    const market = data.market || {};
    const candidates = data.candidate_status || {};
    const tplus = data.t_plus_1 || {};
    const tradableTone = market.tradable ? "good" : "bad";
    const candidateTone = candidates.formal_count > 0 ? "good" : "warn";
    const alertTone = (data.holdings_alerts || []).length > 0 ? "warn" : "good";
    const noteTone = (data.data_notes || []).length > 0 ? "warn" : "good";

    document.getElementById("action-summary").innerHTML = [
      `<div class="signal ${tradableTone}"><strong>${market.tradable ? "可交易" : "暂停交易"}</strong><p>市场等级：${escapeHtml(market.grade || "unknown")}；3日均分：${number(market.score_avg3, 3)}</p></div>`,
      `<div class="signal ${candidateTone}"><strong>${Number(candidates.formal_count || 0)} 个正式候选</strong><p>${escapeHtml(candidates.block_reason || "暂无阻断原因。")}</p></div>`,
      `<div class="signal ${alertTone}"><strong>${(data.holdings_alerts || []).length} 条持仓提示</strong><p>最新本地报告日：${escapeHtml(data.report_date || "--")}</p></div>`,
      `<div class="signal ${noteTone}"><strong>${(data.data_notes || []).length} 条数据说明</strong><p>D1 买入日：${escapeHtml(tplus.d1_buy_date || "--")}；最早卖出：${escapeHtml(tplus.earliest_sell_date || "--")}</p></div>`,
    ].join("");
  }

  function renderMarket(data) {
    const market = data.market || {};
    const tone = market.tradable ? "good" : "bad";
    setMetricList("market-list", [
      ["可交易", badge(market.tradable ? "是" : "否", tone)],
      ["市场等级", badge(market.grade || "unknown", tone)],
      ["上涨家数占比", percent(market.adv_ratio)],
      ["涨停/跌停比", number(market.limit_ratio, 2)],
      ["上证收盘", number(market.sh_close, 2)],
      ["创业板收盘", number(market.cy_close, 2)],
    ]);
  }

  function renderTPlus(data) {
    const tplus = data.t_plus_1 || {};
    setMetricList("tplus-list", [
      ["D0 信号日", escapeHtml(tplus.d0_signal_date || data.report_date || "--")],
      ["D1 买入日", escapeHtml(tplus.d1_buy_date || "--")],
      ["最早卖出日", escapeHtml(tplus.earliest_sell_date || "--")],
      ["本地模式", badge("只读", "good")],
    ]);
  }

  function renderBacktestMetrics(data) {
    const summary = data.backtest_summary || {};
    const metrics = [
      ["交易笔数", text(summary.trade_count), "已成交回测样本"],
      ["胜率", percent(summary.win_rate), "盈利交易占比"],
      ["平均单笔", signedPercent(summary.avg_return), "net_return 均值"],
      ["最大回撤", signedPercent(summary.max_drawdown), "组合曲线回撤"],
      ["期末权益", number(summary.portfolio_cash_end, 3), "初始资金倍数"],
    ];
    document.getElementById("backtest-metrics").innerHTML = metrics
      .map(
        ([label, value, hint]) =>
          `<article class="metric-card"><span>${escapeHtml(label)}</span><strong>${escapeHtml(value)}</strong><small>${escapeHtml(hint)}</small></article>`
      )
      .join("");
  }

  function renderHold5Top3(data) {
    const hold5 = data.hold5_top3 || {};
    const picks = hold5.picks || [];
    document.getElementById("hold5-summary").innerHTML = [
      `<div class="signal ${picks.length ? "good" : "warn"}"><strong>${picks.length} / ${Number(hold5.formal_count || 0)} 只正式候选</strong><p>最新信号日：${escapeHtml(hold5.latest_date || "--")}；计划卖出日：${escapeHtml(hold5.sell_date || "--")}</p></div>`,
      `<div class="signal"><strong>${percent(hold5.adv_ratio)}</strong><p>全市场上涨家数占比；已验证样本：${escapeHtml(text(hold5.validated_count))}</p></div>`,
      `<div class="signal warn"><strong>板块线索</strong><p>${escapeHtml(hold5.top_industries || "暂无板块摘要。")}</p></div>`,
    ].join("");

    document.getElementById("hold5-picks").innerHTML = table(
      [
        { label: "代码", render: (row) => escapeHtml(row.secucode) },
        { label: "名称", render: (row) => escapeHtml(row.name) },
        { label: "行业", render: (row) => escapeHtml(row.industry) },
        { label: "5日胜率", numeric: true, render: (row) => percent(row.win_rate) },
        { label: "平均5日收益", numeric: true, render: (row) => signedPercent(row.avg_return) },
        { label: "买入区间", render: (row) => `${number(row.buy_low, 2)} - ${number(row.buy_high, 2)}` },
        { label: "5日目标", render: (row) => `${number(row.target_low, 2)} - ${number(row.target_high, 2)}` },
        { label: "评分", numeric: true, render: (row) => number(row.score, 1) },
      ],
      picks,
      "暂无 5日盈利前三正式候选。"
    );
  }

  function table(headers, rows, emptyText) {
    if (!rows.length) return `<div class="empty">${escapeHtml(emptyText)}</div>`;
    return `
      <table class="data-table">
        <thead><tr>${headers.map((header) => `<th>${escapeHtml(header.label)}</th>`).join("")}</tr></thead>
        <tbody>
          ${rows
            .map(
              (row) =>
                `<tr>${headers
                  .map((header) => `<td class="${header.numeric ? "number" : ""}">${header.render(row)}</td>`)
                  .join("")}</tr>`
            )
            .join("")}
        </tbody>
      </table>
    `;
  }

  function renderHoldings(data) {
    const rows = (data.holdings_alerts || []).slice(0, 12);
    document.getElementById("holdings-alerts").innerHTML = table(
      [
        { label: "代码", render: (row) => escapeHtml(row.secucode) },
        { label: "名称", render: (row) => escapeHtml(row.name) },
        { label: "涨跌", numeric: true, render: (row) => (row.pct_change === undefined || row.pct_change === null ? "--" : `${number(row.pct_change, 2)}%`) },
        { label: "动作", render: (row) => escapeHtml(row.action) },
        { label: "缺失项", render: (row) => escapeHtml(row.missing) },
      ],
      rows,
      "暂无持仓风险提示。"
    );
  }

  function renderTrades(data) {
    const rows = (data.trades || []).slice(-12).reverse();
    document.getElementById("trades-table").innerHTML = table(
      [
        { label: "信号日", render: (row) => escapeHtml(row.signal_date) },
        { label: "代码", render: (row) => escapeHtml(row.secucode) },
        { label: "名称", render: (row) => escapeHtml(row.stock_name) },
        { label: "层级", render: (row) => badge(row.tier || "--", row.tier === "core" ? "good" : "warn") },
        { label: "收益", numeric: true, render: (row) => signedPercent(row.net_return) },
      ],
      rows,
      "暂无回测交易明细。"
    );
  }

  function renderLiveTrading(data) {
    const live = data.live_trading || {};
    setMetricList("live-trading", [
      ["交易日", escapeHtml(live.trade_date || "--")],
      ["现金", number(live.cash, 2)],
      ["持仓市值", number(live.market_value, 2)],
      ["账户权益", number(live.equity, 2)],
      ["仓位", percent(live.exposure)],
      ["计划/成交/拒绝", `${text(live.planned_orders, "0")} / ${text(live.fills, "0")} / ${text(live.rejections, "0")}`],
    ]);
  }

  function renderUserHoldings(data) {
    const target = document.getElementById("user-holdings");
    if (!target) return;
    const rows = holdingsPanel ? holdingsPanel.buildUserHoldingRows(data) : [];
    if (!rows.length) {
      target.innerHTML = `<div class="empty">暂无当前持仓股。</div>`;
      return;
    }

    target.innerHTML = `
      <div class="user-holding-summary">
        <span>当前持仓</span>
        <strong>${rows.length}</strong>
        <small>来自 data/live_trading/user_positions.csv</small>
      </div>
      <div class="user-holding-grid">
        ${rows
          .map((row) => {
            const hasChange = row.pct_change !== undefined && row.pct_change !== null;
            const changeClass = hasChange ? (Number(row.pct_change) >= 0 ? "up" : "down") : "";
            return `
              <article class="user-holding-card">
                <div class="user-holding-head">
                  <div>
                    <strong>${escapeHtml(row.name || "--")}</strong>
                    <code>${escapeHtml(row.secucode || "--")}</code>
                  </div>
                  <span class="price-change ${changeClass}">${hasChange ? `${number(row.pct_change, 2)}%` : "--"}</span>
                </div>
                <div class="user-holding-metrics">
                  <span><small>买入</small><b>${number(row.buy_price, 2)}</b></span>
                  <span><small>数量</small><b>${text(row.quantity)}</b></span>
                  <span><small>成本</small><b>${number(row.amount, 2)}</b></span>
                  <span><small>现价</small><b>${number(row.close, 2)}</b></span>
                </div>
                <p>${escapeHtml(row.action)}</p>
                <dl>
                  <div><dt>买入日</dt><dd>${escapeHtml(row.buy_date || "--")}</dd></div>
                  <div><dt>复核日</dt><dd>${escapeHtml(row.check_date || "--")}</dd></div>
                  <div><dt>最晚退出</dt><dd>${escapeHtml(row.max_exit_date || "--")}</dd></div>
                </dl>
                ${row.missing ? `<small class="user-holding-note">${escapeHtml(row.missing)}</small>` : ""}
              </article>
            `;
          })
          .join("")}
      </div>
    `;
  }

  function renderNotes(data) {
    const notes = data.data_notes || [];
    document.getElementById("data-notes").innerHTML = notes.length
      ? `<ul>${notes.map((note) => `<li>${escapeHtml(note)}</li>`).join("")}</ul>`
      : `<div class="empty">暂无数据说明。</div>`;

    const sources = Object.entries(data.source_files || {});
    document.getElementById("source-files").innerHTML = sources.length
      ? `<ul>${sources.map(([key, value]) => `<li>${escapeHtml(key)}：${escapeHtml(value)}</li>`).join("")}</ul>`
      : `<div class="empty">暂无源文件记录。</div>`;
  }

  function renderChart(data) {
    const rows = (data.market_states || []).slice(-90);
    const canvas = chartCanvas;
    const context = canvas.getContext("2d");
    const ratio = window.devicePixelRatio || 1;
    const rect = canvas.getBoundingClientRect();
    canvas.width = Math.max(320, Math.floor(rect.width * ratio));
    canvas.height = Math.max(240, Math.floor(rect.height * ratio));
    context.setTransform(ratio, 0, 0, ratio, 0, 0);
    context.clearRect(0, 0, rect.width, rect.height);

    if (!rows.length) {
      context.fillStyle = "#68746f";
      context.font = "14px -apple-system, BlinkMacSystemFont, sans-serif";
      context.fillText("暂无市场状态曲线数据。", 18, 38);
      return;
    }

    const width = rect.width;
    const height = rect.height;
    const padding = { top: 22, right: 18, bottom: 34, left: 44 };
    const plotWidth = width - padding.left - padding.right;
    const plotHeight = height - padding.top - padding.bottom;
    const values = rows.map((row) => Number(row.score_avg3)).filter(Number.isFinite);
    const min = Math.min(-0.2, ...values);
    const max = Math.max(0.8, ...values);

    function x(index) {
      if (rows.length === 1) return padding.left + plotWidth / 2;
      return padding.left + (plotWidth * index) / (rows.length - 1);
    }

    function y(value) {
      const numeric = Number(value);
      if (!Number.isFinite(numeric)) return padding.top + plotHeight;
      return padding.top + plotHeight - ((numeric - min) / (max - min || 1)) * plotHeight;
    }

    context.strokeStyle = "#d8ded8";
    context.lineWidth = 1;
    context.beginPath();
    context.moveTo(padding.left, padding.top);
    context.lineTo(padding.left, padding.top + plotHeight);
    context.lineTo(padding.left + plotWidth, padding.top + plotHeight);
    context.stroke();

    const zeroY = y(0);
    context.strokeStyle = "#c7d0c9";
    context.setLineDash([4, 4]);
    context.beginPath();
    context.moveTo(padding.left, zeroY);
    context.lineTo(padding.left + plotWidth, zeroY);
    context.stroke();
    context.setLineDash([]);

    context.strokeStyle = "#2f6177";
    context.lineWidth = 2;
    context.beginPath();
    rows.forEach((row, index) => {
      const pointX = x(index);
      const pointY = y(row.score_avg3);
      if (index === 0) context.moveTo(pointX, pointY);
      else context.lineTo(pointX, pointY);
    });
    context.stroke();

    context.fillStyle = "#1f2823";
    context.font = "12px -apple-system, BlinkMacSystemFont, sans-serif";
    context.fillText(`score_avg3 ${number(rows[rows.length - 1].score_avg3, 3)}`, padding.left, 16);
    context.fillStyle = "#68746f";
    context.fillText(text(rows[0].trade_date, ""), padding.left, height - 10);
    context.textAlign = "right";
    context.fillText(text(rows[rows.length - 1].trade_date, ""), padding.left + plotWidth, height - 10);
    context.textAlign = "left";
  }

  function render(data) {
    latestDashboard = data;
    document.getElementById("report-date").textContent = `最新本地报告日：${text(data.report_date)}`;
    document.getElementById("loaded-at").textContent = `读取时间：${new Date(data.loaded_at).toLocaleString("zh-CN")}`;
    renderStrategyCatalog(data);
    renderActionPanel(data);
    renderMarket(data);
    renderTPlus(data);
    renderBacktestMetrics(data);
    renderHold5Top3(data);
    renderHoldings(data);
    renderTrades(data);
    renderUserHoldings(data);
    renderLiveTrading(data);
    renderNotes(data);
    renderChart(data);
  }

  async function loadDashboard() {
    refreshButton.disabled = true;
    refreshButton.textContent = "读取中";
    try {
      const response = await fetch(apiUrl, { cache: "no-store" });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      render(await response.json());
    } catch (error) {
      document.getElementById("action-summary").innerHTML = `<div class="empty">读取本地策略数据失败：${escapeHtml(error.message)}</div>`;
    } finally {
      refreshButton.disabled = false;
      refreshButton.textContent = "刷新";
    }
  }

  refreshButton.addEventListener("click", loadDashboard);
  strategyListElement.addEventListener("pointerdown", (event) => {
    if (event.button !== 0) return;
    const card = strategyCardFromEvent(event);
    if (!card || !card.dataset.strategyId) return;
    pointerDrag = {
      active: false,
      id: card.dataset.strategyId,
      pointerId: event.pointerId,
      startX: event.clientX,
      startY: event.clientY,
    };
    try {
      strategyListElement.setPointerCapture(event.pointerId);
    } catch {
      // Pointer capture is best-effort; sorting still works without it.
    }
  });
  document.addEventListener("pointermove", (event) => {
    if (!pointerDrag || event.pointerId !== pointerDrag.pointerId) return;
    const moved = Math.hypot(event.clientX - pointerDrag.startX, event.clientY - pointerDrag.startY);
    if (!pointerDrag.active && moved < 8) return;
    event.preventDefault();
    pointerDrag.active = true;
    draggedStrategyId = pointerDrag.id;
    previewDropTarget(strategyCardFromPoint(event.clientX, event.clientY), event);
  });
  document.addEventListener("pointerup", (event) => {
    if (!pointerDrag || event.pointerId !== pointerDrag.pointerId) return;
    const wasActive = pointerDrag.active;
    if (wasActive) {
      event.preventDefault();
      commitDraggedOrder(strategyCardFromPoint(event.clientX, event.clientY), event);
    }
    pointerDrag = null;
    draggedStrategyId = "";
    clearDragMarkers();
  });
  document.addEventListener("pointercancel", () => {
    pointerDrag = null;
    draggedStrategyId = "";
    clearDragMarkers();
  });
  strategyListElement.addEventListener("dragstart", (event) => {
    const card = strategyCardFromEvent(event);
    if (!card || !card.dataset.strategyId) return;
    draggedStrategyId = card.dataset.strategyId;
    card.classList.add("dragging");
    card.setAttribute("aria-grabbed", "true");
    strategyListElement.classList.add("dragging");
    if (event.dataTransfer) {
      event.dataTransfer.effectAllowed = "move";
      event.dataTransfer.setData("text/plain", draggedStrategyId);
    }
  });
  strategyListElement.addEventListener("dragover", (event) => {
    if (!draggedStrategyId) return;
    event.preventDefault();
    const card = strategyCardFromEvent(event);
    previewDropTarget(card, event);
  });
  strategyListElement.addEventListener("drop", (event) => {
    if (!draggedStrategyId || !strategyOrder) return;
    event.preventDefault();
    const card = strategyCardFromEvent(event);
    commitDraggedOrder(card, event);
    clearDragMarkers();
    draggedStrategyId = "";
  });
  strategyListElement.addEventListener("dragend", () => {
    draggedStrategyId = "";
    clearDragMarkers();
  });
  document.addEventListener("click", (event) => {
    if (dragClickGuard) {
      event.preventDefault();
      event.stopPropagation();
      return;
    }
    const target = event.target instanceof Element ? event.target : null;
    const button = target ? target.closest("[data-strategy-id]") : null;
    if (!button) return;
    selectStrategy(button.dataset.strategyId, Boolean(button.closest(".strategy-list")));
  });
  window.addEventListener("resize", () => {
    if (latestDashboard) renderChart(latestDashboard);
  });
  loadDashboard();
})();
