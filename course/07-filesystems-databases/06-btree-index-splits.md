# 7.5 — Как искать запись на диске, не сканируя весь файл

**Теория:** ~100 мин · **Практика/project:** ~5–7 часов · **С телефона:** теория — да

← [`05-pager-records-cursor.md`](05-pager-records-cursor.md) · → [`07-buffering-query-costs.md`](07-buffering-query-costs.md)

## Проблема

Sorted in-memory BST lesson assumed pointer-rich nodes. On disk every random page read is expensive, so tree should have **high fanout**: many keys/children per page, reducing height.

## B-tree family intuition

A **B-tree** stores many sorted keys per node/page and child ranges between them.

```text
[key 10 | key 30 | key 70]
 child0  child1  child2  child3
```

Search first finds position within page, then follows one child page.

Height roughly logarithmic with large branching factor, often very small compared with binary tree for same record count.

## Page invariant

Each node page must maintain:

- keys sorted;
- child/key count relation according to chosen variant;
- occupancy bounds (except special root rules);
- all children in correct key ranges;
- page references valid.

Exact SimpleDB variant is defined by project format/spec, not generic “all B-trees are identical”.

## Split

When target page full, insert may split node into two and promote separator to parent. Parent itself may overflow, propagating split upward; root split increases height.

Commit order matters for crash consistency. Core SimpleDB without WAL cannot claim atomic multi-page split under power loss; [`RECOVERY_LIMITATIONS.md`](project/RECOVERY_LIMITATIONS.md) must say so.

## Search cost

Big-O comparisons matter, but disk/cache pages matter more:

```text
height → number of page visits
in-page binary/linear search → CPU/cache work
```

## Project slice

Implement leaf/index stage exactly within project scope. Tests force split at smallest threshold and verify all old/new keys, boundaries and reopen behavior.

## Exit check

Why is a high-fanout tree generally better disk index than pointer-based binary search tree even though both are “trees”?