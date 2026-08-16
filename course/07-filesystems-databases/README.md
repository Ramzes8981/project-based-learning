# Module 7 — Filesystems & Database Internals

**Цель:** понять путь `pathname → VFS/filesystem → page cache → storage` и построить маленький page-oriented database engine с B+tree-like index.

**Оценка:** ~65–90 часов.  
**Guided lab:** FUSE 3 virtual filesystem.  
**Core milestone:** SimpleDB.

## Prerequisites

- function pointers/callback tables из Module 1;
- Unix file/path/descriptors;
- VM/page cache mental model;
- explicit binary serialization/endianness;
- Testing Engineering.

## Уроки

1. [`01-filesystem-names-inodes.md`](01-filesystem-names-inodes.md)
2. [`02-page-cache-durability.md`](02-page-cache-durability.md)
3. [`03-fuse-userspace-filesystem.md`](03-fuse-userspace-filesystem.md)
4. [`04-binary-format-pages-serialization.md`](04-binary-format-pages-serialization.md)
5. [`05-pager-records-cursor.md`](05-pager-records-cursor.md)
6. [`06-btree-index-splits.md`](06-btree-index-splits.md)
7. [`07-buffering-query-costs.md`](07-buffering-query-costs.md)
8. [`08-transactions-wal-recovery.md`](08-transactions-wal-recovery.md)
9. [`09-module-checkpoint.md`](09-module-checkpoint.md)

## FUSE reference

[`FUSE3_MINI_REFERENCE.md`](FUSE3_MINI_REFERENCE.md) содержит достаточные signatures/build conventions для guided lab на high-level libfuse 3 API. Внешняя документация нужна только для углубления/версий вне course scope.

## SimpleDB

[`project/SPEC.md`](project/SPEC.md) · [`project/FORMAT.md`](project/FORMAT.md) · [`project/README.md`](project/README.md)

Core SimpleDB **не** заявляет ACID/WAL/crash-atomic guarantees, которых не реализует. Урок про transactions/WAL объясняет production concepts; project обязан честно фиксировать их отсутствие в [`project/RECOVERY_LIMITATIONS.md`](project/RECOVERY_LIMITATIONS.md).
