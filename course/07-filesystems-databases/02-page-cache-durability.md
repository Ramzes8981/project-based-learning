# 7.2 — Почему успешный `write()` ещё не означает “переживёт питание off”

**Теория:** ~95 мин · **Лаб:** ~90 мин · **С телефона:** теория — да

← [`01-filesystem-names-inodes.md`](01-filesystem-names-inodes.md) · → [`04-binary-format-pages-serialization.md`](04-binary-format-pages-serialization.md)

## Проблема

`write(fd, buf, n)` returns success. Application can read new bytes back. Are they guaranteed on durable storage after sudden crash/power loss?

Not from `write` return alone.

## Page cache

Linux normally caches file data in memory. The kernel's **page cache** lets reads/writes operate through memory-backed cached pages and later schedules writeback to storage.

```text
application bytes
→ kernel page cache (dirty)
→ later writeback
→ storage device/controller
```

This creates performance and durability separation.

## Dirty page

Modified cached data not yet persisted to backing storage is often called **dirty**. Kernel may write it later; timing is policy, not application crash-consistency guarantee.

## `fsync`

For regular file on Unix/Linux, `fsync(fd)` asks kernel to flush file data and required metadata to storage according to filesystem/device semantics. Success is stronger durability evidence than `write`, though hardware/filesystem failures remain possible.

Always check `fsync` errors. Error can appear later than original write.

## Atomic replace pattern

To update config/db snapshot without exposing half-written new file:

```text
create temp in same directory/filesystem
→ write all bytes
→ fsync(temp)
→ close as appropriate
→ rename(temp, final)
→ fsync(parent directory)
```

Why same filesystem: `rename` atomic replacement guarantees are not general cross-filesystem copy semantics.

Why directory fsync: rename changes directory metadata; persistence of the new name itself is separate durability concern.

Do not claim universal “this survives every hardware failure”; state target filesystem/OS assumptions.

## Append is not a transaction

`O_APPEND` helps choose write offset atomically for individual write operation semantics, but does not make multi-record transaction, ensure full write, or guarantee crash durability.

## Practice

Build tiny durable-replace helper for a small file, with injected failure points after write/fsync/rename. For real power-loss semantics use reasoning/controlled VM rather than unplugging host.

## Exit check

Why do file `fsync` before rename and directory `fsync` after rename protect different pieces of state?