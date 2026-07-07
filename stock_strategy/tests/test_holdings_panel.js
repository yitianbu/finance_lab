const assert = require("node:assert/strict");
const test = require("node:test");

const { buildUserHoldingRows } = require("../dashboard/static/holdings_panel.js");

test("buildUserHoldingRows shows current user holdings and ignores closed positions", () => {
  const rows = buildUserHoldingRows({
    user_positions: [
      {
        secucode: "300450.SZ",
        name: "先导智能",
        status: "closed",
        notes: "已清仓",
      },
      {
        secucode: "688002.SH",
        name: "睿创微纳",
        status: "holding",
        buy_date: "2026-06-30",
        buy_price: 154.85,
        quantity: 267,
        amount: 41344.95,
        check_date: "2026-07-07",
        notes: "用户记录买入",
      },
    ],
    holdings_alerts: [
      {
        secucode: "300450.SZ",
        name: "先导智能",
        action: "旧持仓检查",
      },
      {
        secucode: "688002.SH",
        name: "睿创微纳",
        close: 160.12,
        pct_change: 2.34,
        action: "继续观察 MA5",
        missing: "无",
      },
    ],
  });

  assert.deepEqual(rows.map((row) => row.secucode), ["688002.SH"]);
  assert.equal(rows[0].name, "睿创微纳");
  assert.equal(rows[0].action, "继续观察 MA5");
  assert.equal(rows[0].close, 160.12);
  assert.equal(rows[0].buy_price, 154.85);
  assert.equal(rows[0].quantity, 267);
});

test("buildUserHoldingRows uses position notes when no matching alert exists", () => {
  const rows = buildUserHoldingRows({
    user_positions: [
      {
        secucode: "600176.SH",
        name: "中国巨石",
        status: "holding",
        notes: "14:52 正式核心候选",
      },
    ],
    holdings_alerts: [],
  });

  assert.equal(rows[0].action, "14:52 正式核心候选");
  assert.equal(rows[0].missing, "");
});
