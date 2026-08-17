# 7.8 — Checkpoint: trace one record from pathname to crash recovery boundary

**Время:** ~4–6 часов · **С телефона:** review — да; project — ПК

← [`08-transactions-wal-recovery.md`](08-transactions-wal-recovery.md) · ↑ [`README`](README.md)

## Explain

1. pathname/directory entry vs inode/file object;
2. open fd after unlink;
3. page cache and dirty data;
4. `write` vs `fsync` durability;
5. durable same-filesystem replace including directory sync;
6. explicit serialization vs raw struct;
7. database page vs OS virtual-memory page;
8. pager offset/short-I/O contract;
9. B-tree high fanout and split invariant;
10. page visits/cache effects on query cost;
11. WAL ordering and crash recovery concept;
12. why current SimpleDB cannot claim full ACID.

## Project gate

SimpleDB passes project acceptance and format fixtures. Reopen tests verify persistence semantics promised; corruption/truncation tests fail safely.

## Transfer

Design one version migration or redo-log extension on paper first: exact old/new bytes, compatibility rule, failure points and tests.

## Optional

FUSE lab does not affect core gate.

## Exit check

Given “record disappeared after crash”, you can ask whether failure was namespace/directory durability, page-cache writeback, format corruption, multi-page atomicity or recovery policy.