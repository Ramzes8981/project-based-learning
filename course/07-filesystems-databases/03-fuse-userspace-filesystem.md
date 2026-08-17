# Optional 7A — Как userspace program отвечает на filesystem operations через FUSE

**Статус:** optional lab; не prerequisite SimpleDB.  
**Теория:** ~70 мин · **Лаб:** ~2–4 часа · **С телефона:** теория — да

↑ [`README`](README.md) · local ref → [`FUSE3_MINI_REFERENCE.md`](FUSE3_MINI_REFERENCE.md)

## Зачем этот optional lab

Filesystem API seems like ordinary `open/read/stat`, but kernel VFS dispatches operations to filesystem implementation. FUSE lets userspace program implement callbacks and observe this boundary without kernel module.

## Problem → mechanism

```text
process calls open/read/readdir
→ kernel VFS needs filesystem-specific answer
→ FUSE forwards request to userspace daemon
→ daemon callback returns result/error
```

**FUSE (Filesystem in Userspace)** is interface for implementing filesystem behavior in userspace with kernel mediation.

## What it teaches

- path lookup/callback boundaries;
- difference metadata lookup vs content read;
- errno-style error contracts;
- concurrency/reentrancy concerns in callbacks;
- why filesystem semantics are larger than “map path to byte array”.

## Scope

Implement read-only tiny filesystem only if environment supports FUSE safely. No required root tricks. If `/dev/fuse`/mount permission unavailable, read mini-reference and trace callback design on paper; core path continues to 7.3 (`04-...`).

## Exit check

Why is FUSE useful for VFS intuition but unnecessary for understanding database pages/indexes?