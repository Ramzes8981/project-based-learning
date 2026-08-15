# Arena Allocator — SPEC

## Environment

Одна arena создаётся через `mmap` или course-approved backing buffer.

## Required API behavior

- create arena;
- allocate aligned block;
- free block;
- destroy arena;
- stats;
- allocation failure explicit.

Exact function signatures/student files не задаются курсом.

## Progression

1. bump allocator;
2. alignment;
3. headers;
4. free list;
5. first-fit;
6. reuse;
7. split;
8. coalesce adjacent blocks;
9. metrics;
10. second placement policy for comparison.

## Invariants

- blocks do not overlap;
- every block lies inside arena;
- payload aligned to chosen contract;
- metadata arithmetic cannot wrap silently;
- free/used state consistent;
- no block appears twice in free structure;
- coalescing only physical neighbors.

## Non-goals

- thread-safe allocator;
- replacing libc `malloc` globally;
- multiple arenas;
- production hardening.
