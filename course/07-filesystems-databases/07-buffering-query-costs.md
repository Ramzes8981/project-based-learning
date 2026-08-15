# 7.7 — Buffer cache, page access cost и index trade-offs

**Теория:** ~75 мин  
**Instrumentation lab:** ~3–5 часов  
**С телефона:** да

← [`06-btree-index-splits.md`](06-btree-index-splits.md) · → [`08-transactions-wal-recovery.md`](08-transactions-wal-recovery.md)

## Цель

Измерять storage algorithm через page accesses/cache behavior, а не только Big-O по records.

## Logical operation vs physical I/O

`GET key` может вызвать:

```text
root page lookup
→ internal child
→ leaf
```

Но если pages уже в OS/app cache, physical storage I/O может не произойти.

Поэтому instrumentation разделяет:

- logical page access;
- pager cache hit/miss;
- OS-visible read/write syscall optionally;
- durable flush operations.

## Buffer pool

DB buffer pool/cache хранит hot pages в memory и tracks dirty state.

Даже если OS page cache существует, application DB buffer pool useful для:

- page objects/pinning;
- replacement policy;
- dirty/transaction coordination;
- predictable DB-level metrics.

Core SimpleDB может иметь tiny fixed cache or just instrumentation; full buffer manager — Stretch.

## Full scan

Scan читает all leaf pages roughly `O(number_of_pages)`.

Index lookup читает tree path `O(height)` logical pages.

## Index trade-off

Extra index:

- ускоряет определённые reads;
- занимает storage/cache;
- увеличивает write/update work;
- создаёт consistency/recovery responsibilities.

«Добавь index» не бесплатная optimization.

## Read amplification

Один logical record lookup может читать multiple pages. Page layout/fanout/cache определяют amplification.

## Write amplification

Insert может изменить leaf + parent(s), split pages и later journal/WAL records.

## Instrumentation

Добавь counters:

```text
page_read_requests
page_cache_hits (if cache exists)
page_writes
page_allocations
leaf_splits
internal_splits
```

Сравни:

- `scan` N records;
- random indexed lookup;
- sequential inserts;
- insert around split boundary.

## Exercise

Сделай table measurements для DB sizes 100, 10k, 100k keys (если runtime reasonable): average logical pages per GET, tree height, splits.

Не обещай constant exact page count вне implemented tree/cache.

## Causal questions

1. Почему logical page access != disk I/O?
2. Почему high cache hit rate может скрыть poor on-disk layout benchmark?
3. Почему secondary index ухудшает writes?
4. Какие metrics понадобятся до оптимизации pager?

## Exit check

Performance SimpleDB объясняется через tree depth + page access + cache, а не «B-tree O(log n), значит всё быстро».
