# SimpleDB — page-oriented storage project

Build a small persistent database to connect filesystem durability, explicit binary format, pager and disk index.

## Milestones

1. **Format** — exact header/page/record bytes from [`FORMAT.md`](FORMAT.md).
2. **Pager** — checked page offsets, complete/truncated/error distinction.
3. **Records** — insert/scan/reopen.
4. **Index** — B-tree-family lookup/split within project variant.
5. **Measurement** — page visits/cache/query evidence.
6. **Crash boundary** — document what current implementation does **not** guarantee in [`RECOVERY_LIMITATIONS.md`](RECOVERY_LIMITATIONS.md).

## Deliberate non-goals of core

- full SQL parser/planner;
- MVCC;
- concurrent transactions;
- production WAL/ACID;
- cross-platform arbitrary struct persistence;
- mmap-everything shortcut without durability model.

Lesson 7.7 teaches WAL concepts; implementation is optional extension, not hidden acceptance requirement.

Docs: [`SPEC.md`](SPEC.md) · [`ACCEPTANCE.md`](ACCEPTANCE.md) · [`TESTS.md`](TESTS.md) · [`HINTS.md`](HINTS.md) · [`FORMAT.md`](FORMAT.md).