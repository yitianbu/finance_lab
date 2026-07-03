const assert = require("node:assert/strict");
const test = require("node:test");

const { applyStoredOrder, moveAfter, moveBefore } = require("../dashboard/static/strategy_order.js");

const catalog = [
  { id: "hold5-tail", name: "14:50 尾盘5日持有" },
  { id: "dynamic-execution", name: "动态执行模式" },
  { id: "crowding-warning", name: "拥挤度预警" },
  { id: "ten-billion-turnover", name: "10亿增量策略" },
];

test("applyStoredOrder puts saved strategy ids first and keeps new strategies visible", () => {
  const ordered = applyStoredOrder(catalog, [
    "crowding-warning",
    "missing-strategy",
    "hold5-tail",
  ]);

  assert.deepEqual(
    ordered.map((item) => item.id),
    ["crowding-warning", "hold5-tail", "dynamic-execution", "ten-billion-turnover"]
  );
});

test("moveBefore reorders a dragged strategy before the target strategy", () => {
  assert.deepEqual(
    moveBefore(["hold5-tail", "dynamic-execution", "crowding-warning"], "crowding-warning", "hold5-tail"),
    ["crowding-warning", "hold5-tail", "dynamic-execution"]
  );
  assert.deepEqual(
    moveBefore(["hold5-tail", "dynamic-execution", "crowding-warning"], "hold5-tail", "crowding-warning"),
    ["dynamic-execution", "hold5-tail", "crowding-warning"]
  );
});

test("moveAfter reorders a dragged strategy after the target strategy", () => {
  assert.deepEqual(
    moveAfter(["hold5-tail", "dynamic-execution", "crowding-warning"], "hold5-tail", "crowding-warning"),
    ["dynamic-execution", "crowding-warning", "hold5-tail"]
  );
});
