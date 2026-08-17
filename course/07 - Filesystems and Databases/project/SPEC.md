# SimpleDB — SPEC

SimpleDB is a single-process, single-writer educational storage engine in C.

It is **not SQL** and not transactional in core v1.

## User-facing commands/API

At minimum:

```text
insert KEY VALUE
get KEY
scan
.stats
.btree
.exit
```

KEY is `uint32_t`. VALUE is binary/text bytes up to course limit.

Duplicate key policy: reject duplicate in core v1. Transfer feature may add update.

## Storage

- single database file;
- explicit format from `FORMAT.md`;
- fixed page size;
- pager with explicit positional page I/O;
- B+tree-like primary index;
- all records in leaf pages;
- internal pages contain navigation only;
- leaf chain supports ordered scan.

## Required progression

1. create/open/validate header;
2. leaf root insert/get/scan;
3. persistence/reopen;
4. leaf binary search;
5. leaf split;
6. internal root;
7. multi-level internal search;
8. internal split;
9. page-access/split metrics;
10. corruption detection for obvious invalid page type/count/ranges.

## Concurrency

Core v1: one process/writer only. No claim of concurrent correctness.

## Durability

Core v1 flushes according to documented pager policy but does not guarantee atomic recovery from mid-split crash.

`RECOVERY_LIMITATIONS.md` mandatory.

## Non-goals

- SQL parser/planner;
- transactions/WAL implementation;
- MVCC;
- secondary indexes;
- variable-size overflow pages;
- free-page reuse;
- production compatibility.
