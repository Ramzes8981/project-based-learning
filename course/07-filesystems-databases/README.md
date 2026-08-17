# Module 7 — Как данные получают имя на диске, переживают сбой и превращаются в базу данных

**Оценка core:** ~45–65 часов.  
**Prerequisite:** files/fd, virtual memory pages, checked binary representation, trees/complexity.

`page cache` **не prerequisite**: он впервые нормально вводится в 7.2, когда возникает вопрос «`write()` вернулся — где сейчас данные?».

## Core path

1. [`01-filesystem-names-inodes.md`](01-filesystem-names-inodes.md) — **Почему имя файла и сам файл — разные сущности**.
2. [`02-page-cache-durability.md`](02-page-cache-durability.md) — **Почему успешный `write()` ещё не означает “переживёт питание off”**.
3. [`04-binary-format-pages-serialization.md`](04-binary-format-pages-serialization.md) — **Как записать bytes так, чтобы будущая версия программы могла их прочитать**.
4. [`05-pager-records-cursor.md`](05-pager-records-cursor.md) — **Как работать с файлом базы страницами вместо случайных `read/write` по всему коду**.
5. [`06-btree-index-splits.md`](06-btree-index-splits.md) — **Как искать запись на диске, не сканируя весь файл**.
6. [`07-buffering-query-costs.md`](07-buffering-query-costs.md) — **Почему стоимость query определяется не только Big-O, но и I/O/locality**.
7. [`08-transactions-wal-recovery.md`](08-transactions-wal-recovery.md) — **Что должно быть записано до данных, чтобы recovery вообще был возможен**.
8. [`09-module-checkpoint.md`](09-module-checkpoint.md) — checkpoint.

## Optional systems lab

[`03-fuse-userspace-filesystem.md`](03-fuse-userspace-filesystem.md) — FUSE. Полезен для понимания VFS/callback interface, но **не блокирует** database storage path.

## Проект

[`project/README.md`](project/README.md) — SimpleDB. Core project intentionally stops before full ACID/WAL implementation; transaction/WAL lesson is conceptual bridge and optional extension. Limitations remain normative in [`project/RECOVERY_LIMITATIONS.md`](project/RECOVERY_LIMITATIONS.md).

## Главная causal chain

```text
path name
→ filesystem object/inode
→ page cache + durability boundary
→ stable binary format
→ page manager
→ records
→ disk index
→ query/I/O cost
→ crash consistency / WAL concept
```