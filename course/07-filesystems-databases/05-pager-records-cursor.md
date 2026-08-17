# 7.4 — Как работать с database file страницами вместо случайных `read/write` по всему коду

**Теория:** ~85 мин · **Практика/project:** ~4–6 часов · **С телефона:** теория — да

← [`04-binary-format-pages-serialization.md`](04-binary-format-pages-serialization.md) · → [`06-btree-index-splits.md`](06-btree-index-splits.md)

## Проблема

If every query computes raw offsets and calls `pread/pwrite`, format arithmetic/error handling spreads everywhere. Need one component owning page I/O contract.

## Pager

A **pager** maps database page number to fixed-size page bytes and hides file-offset I/O details.

```text
logical page id
→ checked offset = page_id * PAGE_SIZE
→ read/write exactly one page
→ validate short/truncated I/O
```

Offset multiplication must be checked against target `off_t`/file limits before syscall.

## Records

A record can be fixed-size or variable-size. Core SimpleDB uses exact format from `FORMAT.md`; do not let C struct size silently become record size.

For slotted/variable layouts, metadata must prevent overlapping/cross-page ranges. If project uses fixed-size records first, variable records remain extension.

## Cursor

A **cursor** is traversal state over logical records/pages. It avoids returning raw pointers to page buffers whose lifetime may end when pager evicts/reuses memory.

Even simple no-cache pager should define what invalidates record views.

## Short I/O

Regular-file reads can return short at EOF; a database page expected fully present must distinguish:

```text
new page/unallocated according to format
valid full page
truncated/corrupt file
I/O error
```

Never zero-fill unexpected truncation and silently call it valid old data unless format explicitly defines sparse/new-page semantics.

## Project slice

Implement pager + record scan/insert according to project format. Add deterministic I/O seam or truncated fixture for error paths.

## Exit check

Why is “short page read” a storage-format decision, not automatically equivalent to “remaining bytes are zero”?