# Module 7 — Filesystems & Database Internals

**Цель:** понять путь `pathname → filesystem → page cache → storage` и построить маленький page-oriented database engine с B+tree-like index.

**Оценка:** ~60–80 часов.  
**Guided lab:** FUSE 3 virtual filesystem.  
**Core milestone:** SimpleDB.

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

## Проект

[`project/SPEC.md`](project/SPEC.md)  
Формат: [`project/FORMAT.md`](project/FORMAT.md)

Core SimpleDB **не** заявляет ACID/WAL guarantees, которые не реализованы. Transactions/recovery изучаются отдельно и отражаются в limitation review.
