# Module 4 — Virtual Memory, Performance & Allocators

**Цель:** связать process address space, page translation, cache locality и custom allocation policy.

**Оценка:** ~35–50 часов.  
**Core milestone:** Arena Allocator.

## Уроки

1. [`01-virtual-address-space-mmap.md`](01-virtual-address-space-mmap.md)
2. [`02-page-tables-tlb-faults.md`](02-page-tables-tlb-faults.md)
3. [`03-cache-locality-working-set.md`](03-cache-locality-working-set.md)
4. [`04-measurement-profiling.md`](04-measurement-profiling.md)
5. [`05-allocator-design.md`](05-allocator-design.md)
6. [`06-module-checkpoint.md`](06-module-checkpoint.md)

## Проект

[`project/SPEC.md`](project/SPEC.md)

Allocator управляет памятью **внутри заранее полученной arena**, а не пытается повторить production `malloc` целиком.
