# 4.3 — Почему одинаковое число C-операций может стоить очень по-разному

**Теория:** ~80 мин · **Лаб:** ~90 мин · **С телефона:** theory — да

← [`02-page-tables-tlb-faults.md`](02-page-tables-tlb-faults.md) · → [`04-measurement-profiling.md`](04-measurement-profiling.md)

## Проблема

Two loops can perform same number of additions but have very different runtime depending on memory access pattern. Arithmetic count alone misses memory hierarchy.

## CPU cache

Fast small storage close to CPU keeps recently/frequently accessed memory data in blocks called cache lines. These stores are **CPU caches** (commonly L1/L2/L3 levels).

We introduce term now because performance observation created need; it was not a prerequisite Module 3.

## Spatial locality

If code accesses nearby addresses, fetching one cache line may bring bytes needed soon.

Contiguous array traversal typically has better **spatial locality** than pointer-chasing nodes scattered across allocations.

## Temporal locality

If same data is reused soon, it may remain in faster level — **temporal locality**.

## Cache line and false confidence

Exact line size/hierarchy is hardware property. Do not hard-code “64 bytes everywhere” as language truth. Measure/query target docs when optimization depends on exact number.

## Working set

The **working set** is roughly data actively needed during interval. If it fits fast cache levels, reuse is cheap; if much larger, accesses incur more misses/memory traffic.

This is a model, not one exact universal formula.

## Array vs linked list revisited

Earlier DS trade-off now gains hardware layer:

```text
Vector:
  contiguous → predictable prefetch/cache lines
Linked list:
  per-node pointer chase → dependency + scattered addresses
```

Big-O can be same while constant/hardware cost differs dramatically.

## Stride experiment

Traverse large array with stride 1, then larger strides. Keep total useful work controlled enough to avoid misleading comparison. Use multiple runs/warmup and prevent compiler removing work.

## False sharing preview

Threads later: two cores modifying independent variables on same cache line can interfere due coherence. Name **false sharing** can be previewed only as future phenomenon; no concurrency mechanics required now.

## Практика

Benchmark contiguous array vs linked traversal and at least two strides. Record compiler flags, data size, run count, median—not one lucky timing.

## Exit check

Why can linked list and array traversal both be `O(n)` yet differ strongly in measured time?