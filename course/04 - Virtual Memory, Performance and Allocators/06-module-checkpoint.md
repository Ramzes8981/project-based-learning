# 4.7 — Checkpoint: адрес, translation cost и allocator invariants

**Время:** ~3–5 часов · **С телефона:** review — да; project — ПК

← [`05b-free-lists-coalescing.md`](05b-free-lists-coalescing.md) · ↑ [`README`](README.md)

## Explain

1. virtual address vs physical storage;
2. page + offset;
3. why page tables exist;
4. why TLB exists;
5. recoverable page fault vs invalid access;
6. CPU cache/locality/working set;
7. why Big-O can miss locality cost;
8. measurement protocol before optimization;
9. alignment;
10. bump allocation;
11. free list/split/coalesce;
12. internal vs external fragmentation.

## Project gate

Arena Allocator passes project acceptance including forced invalid/double-free cases and coalescing only true physical neighbors.

## Transfer

Compare first-fit vs one alternative on a defined allocation/free workload. Measure fragmentation/search work, not vibes.

## Exit check

Given a failed large allocation with lots of total free bytes, you can distinguish capacity exhaustion, external fragmentation, alignment waste and metadata bug.