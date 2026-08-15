# 7.6 — B+tree-like index, fan-out и splits

**Теория:** ~100 мин  
**Project slice:** ~12–20 часов  
**С телефона:** теория — да

← [`05-pager-records-cursor.md`](05-pager-records-cursor.md) · → [`07-buffering-query-costs.md`](07-buffering-query-costs.md)

## Цель

Реализовать multi-level balanced page tree и понять, почему high fan-out уменьшает storage I/O depth.

## Почему не ordinary BST

Pointer BST node может хранить 1 key + 2 pointers. На disk это ужасно: traversal мог бы требовать отдельный page/I/O на каждый level и fan-out 2 даёт большую height.

B-tree family node хранит **много keys/children в одной page**.

```text
[ k1 | k2 | k3 | ... ]
 /    |    |    \
children page numbers
```

## B-tree vs B+tree

В B-tree family details различаются. Course SimpleDB использует B+tree-like idea:

- internal pages: separator keys + child page numbers;
- leaf pages: actual key/value records;
- all records at leaves;
- leaves may have `next_leaf` pointer for scan.

Это собственная упрощённая спецификация, не SQLite exact format.

## Search invariant

Internal keys partition key space. Для key выбирается exactly one child range.

Leaf keys sorted. Внутри page binary search уменьшает CPU comparisons; главный storage benefit — fan-out/depth.

## Fan-out

Если internal page примерно имеет `b` children, balanced tree height порядка:

```text
log_b(N)
```

Чем больше b, тем меньше page levels/I/O для lookup.

## Leaf split

Когда leaf full:

1. create new leaf page;
2. merge/redistribute old + new record sorted;
3. left/right halves;
4. update leaf links if used;
5. propagate separator key to parent.

## Root split

Если root leaf splits, нельзя просто «потерять root page number». Course policy может:

- allocate two child pages and convert root to internal;
- либо allocate new root and update file header.

Выбери один contract in FORMAT/SPEC; tests expect documented course choice.

## Internal split

Когда parent full, split propagates upward recursively. Balanced property сохраняется: all leaves same depth.

## Parent pointers

Можно хранить parent page number для easier upward propagation, либо maintain path stack during descent. Course allows either if format documented.

Не store raw pointer.

## Duplicate keys

Core SimpleDB keys unique. Insert duplicate returns explicit status/update policy according to SPEC; нельзя создавать ambiguous duplicates silently.

## Crash caveat

Multi-page split modifies several pages. Without WAL/transaction protocol crash mid-operation может corrupt tree. **Core project принимает этот limitation**, а Lesson 7.8 объясняет, как real DB addresses it.

## Project slice

Последовательно:

1. leaf binary search;
2. leaf insert;
3. leaf split;
4. root becomes internal;
5. internal search;
6. insert through internal node;
7. internal split/height >2;
8. scan through leaves.

После каждого stage сохраняй on-disk validation/invariant tests.

## Causal questions

1. Почему high fan-out особенно важен на storage?
2. Что separator key гарантирует?
3. Почему split должен propagate parent?
4. Почему multi-page split без transaction protocol crash-unsafe?

## Exit check

Для миллиона keys оцени qualitatively разницу depth binary tree vs page B+tree с fanout 100.
