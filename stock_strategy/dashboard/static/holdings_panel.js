(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) {
    module.exports = api;
  }
  root.HoldingsPanel = api;
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  function isCurrentHolding(position) {
    const status = String(position?.status || "").trim();
    return status === "" || status === "holding";
  }

  function bySecucode(rows) {
    const lookup = new Map();
    (rows || []).forEach((row) => {
      if (row && row.secucode) lookup.set(String(row.secucode), row);
    });
    return lookup;
  }

  function buildUserHoldingRows(data) {
    const alertByCode = bySecucode(data?.holdings_alerts || []);
    return (data?.user_positions || [])
      .filter(isCurrentHolding)
      .map((position) => {
        const secucode = String(position.secucode || "");
        const alert = alertByCode.get(secucode) || {};
        return {
          secucode,
          name: alert.name || position.name || "",
          close: alert.close,
          pct_change: alert.pct_change,
          action: alert.action || position.notes || "当前持仓，暂无动作提示。",
          missing: alert.missing || "",
          buy_date: position.buy_date || position.added_date || "",
          buy_price: position.buy_price,
          quantity: position.quantity,
          amount: position.amount,
          strategy: position.strategy || "",
          check_date: position.check_date || "",
          max_exit_date: position.max_exit_date || "",
          notes: position.notes || "",
        };
      });
  }

  return {
    buildUserHoldingRows,
    isCurrentHolding,
  };
});
