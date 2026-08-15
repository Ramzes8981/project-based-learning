# Module 7 — Checkpoint

## Explain

- pathname/directory entry/inode/open file state;
- hard vs symlink;
- page cache/dirty data/durability;
- FUSE callback boundary;
- explicit serialization/file versioning;
- pager/page/cursor;
- B+tree fanout/search/split;
- logical page access vs physical I/O;
- index read/write trade-off;
- transaction atomicity/isolation/durability;
- WAL/recovery/checkpoint concepts.

## Guided FUSE lab

Должен быть пройден scope Lesson 7.3 либо documented environment limitation.

## Core milestone

Проверь [`project/ACCEPTANCE.md`](project/ACCEPTANCE.md).

## Required artifacts

- `FORMAT.md` actual chosen layout deviations;
- page-access metrics;
- tree visualization/debug output;
- `RECOVERY_LIMITATIONS.md`;
- debugging story for one corruption/split bug.

## Exit gate

Для проблемы «DB slow/corrupt» ты можешь разнести причины по parser/query, tree/index, page layout, cache/I/O, durability и transaction/recovery layers.
