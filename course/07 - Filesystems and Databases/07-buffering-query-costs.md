# 7.6 — Почему query cost определяется не только Big-O, но и I/O/locality

**Теория:** ~75 мин · **Лаб:** ~80 мин · **С телефона:** theory — да

← [`06-btree-index-splits.md`](06-btree-index-splits.md) · → [`08-transactions-wal-recovery.md`](08-transactions-wal-recovery.md)

## Проблема

Two queries can both be `O(log n)` but one hits cached index pages and another triggers storage reads. Need a cost model closer to storage system.

## Buffer cache / pager cache

Database may keep recently used pages in its own buffer pool/cache above OS page cache. This can avoid decode/syscall work and control eviction/dirty state, but creates two caching layers.

Core SimpleDB may use minimal page cache; concept matters more than production replacement algorithm.

## Query cost dimensions

Count at least:

- pages visited;
- cache hit/miss;
- bytes read/written;
- random vs sequential access;
- comparisons within pages;
- dirty pages generated;
- durability syncs.

## Sequential scan can beat index

For large fraction of table, sequential scan may exploit contiguous I/O/locality better than many random index→record lookups. “Index exists” does not imply optimizer should always use it.

## Measure

Instrument page reads/cache hits in SimpleDB. Compare exact-key lookup vs full scan under cold-ish/repeated conditions, without claiming OS cache state you did not control.

## Exit check

Why can adding an index make some write-heavy workload slower even while point lookup improves?