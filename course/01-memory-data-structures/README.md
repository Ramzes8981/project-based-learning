# Module 1 — Memory, Pointers, Algorithms & Data Structures

**Цель:** понять память C, владение ресурсами и фундаментальные структуры/алгоритмы достаточно глубоко, чтобы самостоятельно реализовать Vector и Hash Table и объяснить их стоимость.

**Оценка:** ~85–110 часов.  
**Mini-milestone:** Dynamic Array / Vector.  
**Core milestone:** MiniKV → Hash Table in C.

## Prerequisites

Module 0 закрыт: MiniKV v0 работает, многофайловый C-проект собирается через Make, `make test` запускает твои проверки.

## Последовательность

1. [`01-addresses-pointers.md`](01-addresses-pointers.md) — адреса, `&`, `*`, pointer parameters.
2. [`02-arrays-pointer-arithmetic.md`](02-arrays-pointer-arithmetic.md) — массивы и pointer arithmetic.
3. [`03-const-types-bits.md`](03-const-types-bits.md) — `const`, `size_t`, fixed-width integers, bit masks.
4. [`04-lifetime-ownership.md`](04-lifetime-ownership.md) — lifetime и ownership contracts.
5. [`05-heap-allocation.md`](05-heap-allocation.md) — `malloc/calloc/realloc/free`.
6. [`06-undefined-behavior-debugging.md`](06-undefined-behavior-debugging.md) — UB, sanitizers, debugging.
7. [`07-dynamic-array.md`](07-dynamic-array.md) — Vector и amortized growth.
8. [`08-linked-structures.md`](08-linked-structures.md) — linked list, stack, queue, locality.
9. [`09-function-pointers-callbacks.md`](09-function-pointers-callbacks.md) — function pointers, callbacks, context pointers.
10. [`10-complexity-invariants-binary-search.md`](10-complexity-invariants-binary-search.md) — O/Ω/Θ, invariants, binary search.
11. [`11-sorting.md`](11-sorting.md) — insertion/selection/merge/quick/heap sort и trade-offs.
12. [`12-recursion-recurrences.md`](12-recursion-recurrences.md) — recursion, call stack, recurrence intuition.
13. [`13-bst-traversals-balanced-trees.md`](13-bst-traversals-balanced-trees.md) — BST, traversals, degeneration, balancing motivation.
14. [`14-heap-priority-queue.md`](14-heap-priority-queue.md) — binary heap и Priority Queue.
15. [`15-dynamic-programming.md`](15-dynamic-programming.md) — state, transition, memoization/tabulation.
16. [`16-string-searching.md`](16-string-searching.md) — naive search, prefix function/KMP, Rabin–Karp.
17. [`17-trie.md`](17-trie.md) — prefix tree и ownership/layout trade-offs.
18. [`18-probability-for-hashing.md`](18-probability-for-hashing.md) — probability intuition, expected value, birthday effect.
19. [`19-hashing-collisions.md`](19-hashing-collisions.md) — hash table, probing, tombstones.
20. [`20-resize-rehash.md`](20-resize-rehash.md) — resize, rehash, instrumentation.
21. [`21-module-checkpoint.md`](21-module-checkpoint.md) — gate Module 1.

## Проекты

- [`project/vector/SPEC.md`](project/vector/SPEC.md) — маленький интеграционный проект.
- [`project/hash-table/SPEC.md`](project/hash-table/SPEC.md) — основной milestone.

В каждом project-folder есть learner-owned `README.md`. Исходники, Makefile и unit tests создаёшь ты; курс задаёт SPEC, scenarios, acceptance и hints.

## Что считается прохождением

Недостаточно знать названия структур. Ты должен уметь:

- объяснить ownership/lifetime каждого pointer;
- назвать invariant структуры;
- оценить complexity и memory trade-off;
- написать и отладить реализацию;
- покрыть error/boundary paths;
- перенести идею на новый небольшой кейс.
