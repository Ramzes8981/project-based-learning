# Module 4 — Virtual Memory, Performance & Allocators

**Цель:** связать process address space, page translation, cache locality, measurement discipline и custom allocation policy.

**Оценка:** ~38–55 часов.  
**Core milestone:** Arena Allocator.

## Prerequisites

- C ownership/heap/UB из Module 1;
- Testing Engineering: invariants, fault paths, regression tests;
- architecture basics: addresses, caches, machine representation.

## Уроки

1. [`01-virtual-address-space-mmap.md`](01-virtual-address-space-mmap.md)
2. [`02-page-tables-tlb-faults.md`](02-page-tables-tlb-faults.md)
3. [`03-cache-locality-working-set.md`](03-cache-locality-working-set.md)
4. [`04-measurement-profiling.md`](04-measurement-profiling.md)
5. [`05-allocator-design.md`](05-allocator-design.md)
6. [`06-module-checkpoint.md`](06-module-checkpoint.md)

## Проект

[`project/SPEC.md`](project/SPEC.md) · [`project/README.md`](project/README.md)

Allocator управляет sub-blocks **внутри заранее полученной arena**. API проекта выбираешь сам; поэтому executable public harness не навязывает signatures. Вместо этого `make test` обязан запускать твои unit/property tests из `TESTS.md`, а review добавляет unseen operation sequences.
