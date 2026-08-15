# 7.5 — Pager, records и cursor abstraction

**Теория:** ~80 мин  
**Project slice:** ~6–10 часов  
**С телефона:** да

← [`04-binary-format-pages-serialization.md`](04-binary-format-pages-serialization.md) · → [`06-btree-index-splits.md`](06-btree-index-splits.md)

## Цель

Разделить storage engine на logical records и physical page I/O.

## Layers

```text
command/API
  ↓
record/index operations
  ↓
cursor/navigation
  ↓
pager
  ↓
pread/pwrite/fsync-ish file layer
```

Каждый layer имеет contract.

## Pager

Pager отвечает:

- открыть DB file;
- validate header;
- read page N;
- write dirty page N;
- allocate new page number;
- track file page count;
- close/flush according to current non-transactional policy.

Core pager может иметь небольшой in-memory page cache, но сначала synchronous page reads проще для correctness.

## Positional I/O

`pread/pwrite` удобны: operation получает explicit offset и не зависит от shared current file offset.

Page offset:

```text
file_header_bytes + page_no * PAGE_SIZE
```

Проверь multiplication/addition overflow before converting to `off_t`/API range.

## Record

SimpleDB record:

```text
u32 key
u16 value_len
value bytes up to MAX_VALUE
```

Disk pages не хранят host pointer.

## Cursor

Cursor описывает logical position внутри tree/page:

```text
page number
cell/index position
end flag
```

Это отделяет traversal от REPL/command parsing.

## REPL/API

Для учебного interface достаточно:

```text
insert <key> <value>
get <key>
scan
.stats
.exit
```

Parser не является SQL parser. Не называй SimpleDB «SQL database».

## Page allocation

Пока нет free-page manager/delete reclaim, новые pages append at end. Это limitation, которую нужно документировать.

## Failure handling

Если page read short/corrupt:

- не interpreting uninitialized bytes;
- report corruption/I/O error;
- current operation aborts cleanly.

## Project slice

Реализуй:

1. open/create;
2. format header;
3. page read/write helpers;
4. leaf root page;
5. insert few records sequentially;
6. get/scan before splits;
7. reopen persistence test.

## Causal questions

1. Почему pager не должен знать CLI syntax?
2. Почему page offset arithmetic требует overflow checks?
3. Что cursor abstraction даст после появления internal nodes?
4. Почему append-only page allocation пока допустима, но это limitation?

## Exit check

Проследи `get 42` от command до exact page read.
