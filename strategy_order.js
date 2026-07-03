(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) {
    module.exports = api;
  }
  root.StrategyOrder = api;
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  function idsFromCatalog(catalog) {
    return (catalog || []).map((item) => item && item.id).filter(Boolean);
  }

  function normalizeStoredOrder(catalog, storedOrder) {
    const ids = idsFromCatalog(catalog);
    const knownIds = new Set(ids);
    const usedIds = new Set();
    const orderedIds = [];

    (storedOrder || []).forEach((id) => {
      if (!knownIds.has(id) || usedIds.has(id)) return;
      usedIds.add(id);
      orderedIds.push(id);
    });

    ids.forEach((id) => {
      if (!usedIds.has(id)) orderedIds.push(id);
    });

    return orderedIds;
  }

  function applyStoredOrder(catalog, storedOrder) {
    const rows = catalog || [];
    const byId = new Map(rows.map((item) => [item.id, item]));
    return normalizeStoredOrder(rows, storedOrder).map((id) => byId.get(id)).filter(Boolean);
  }

  function moveBefore(orderIds, draggedId, targetId) {
    if (!draggedId || !targetId || draggedId === targetId) return orderIds.slice();
    const withoutDragged = orderIds.filter((id) => id !== draggedId);
    const targetIndex = withoutDragged.indexOf(targetId);
    if (targetIndex === -1 || !orderIds.includes(draggedId)) return orderIds.slice();
    return [
      ...withoutDragged.slice(0, targetIndex),
      draggedId,
      ...withoutDragged.slice(targetIndex),
    ];
  }

  function moveAfter(orderIds, draggedId, targetId) {
    if (!draggedId || !targetId || draggedId === targetId) return orderIds.slice();
    const withoutDragged = orderIds.filter((id) => id !== draggedId);
    const targetIndex = withoutDragged.indexOf(targetId);
    if (targetIndex === -1 || !orderIds.includes(draggedId)) return orderIds.slice();
    return [
      ...withoutDragged.slice(0, targetIndex + 1),
      draggedId,
      ...withoutDragged.slice(targetIndex + 1),
    ];
  }

  return {
    applyStoredOrder,
    moveAfter,
    moveBefore,
    normalizeStoredOrder,
  };
});
