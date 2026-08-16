# 7.7 — Что должно быть записано до данных, чтобы recovery вообще был возможен

**Теория:** ~100 мин · **Практика:** ~80 мин · **С телефона:** theory — да

← [`07-buffering-query-costs.md`](07-buffering-query-costs.md) · → [`09-module-checkpoint.md`](09-module-checkpoint.md)

## Проблема

One logical update can modify several pages. Crash between writes can leave structure half-updated. `fsync` each page does not by itself define which multi-page states are valid or how to recover.

Need transaction/recovery protocol.

## Transaction goal

A **transaction** groups operations under guarantees such as atomicity/consistency/isolation/durability (ACID), but exact isolation/durability contracts vary. Core focuses crash atomicity/durability intuition, not full database theory.

## WAL idea

**Write-ahead logging (WAL)** rule:

> recovery information describing a change must reach durable log before corresponding changed data page is allowed to become durably visible in a way that recovery depends on.

Simplified flow:

```text
append log record
→ make required log prefix durable
→ later write dirty data pages
→ after crash scan log/recovery state
```

This ordering is why it is “write-ahead”.

## Log sequence / commit record

Real systems use LSNs/checkpoints/redo/undo variants. Course mental model:

- each log record ordered;
- transaction commit becomes durable only after required commit/log records synced;
- recovery decides which operations redo/ignore/undo according to protocol.

Do not claim “WAL = append JSON then replay”. Checksums/torn writes/idempotent recovery/order all matter.

## SimpleDB boundary

Core project **does not implement full WAL/ACID**. This lesson exists so student can explain why current multi-page update is vulnerable and design a next milestone without pretending durability solved.

Optional transfer: design (not necessarily implement) minimal redo-log for one operation with exact crash points.

## Practice

For B-tree split changing child + parent, enumerate crash points:

```text
before log
log written not synced
log durable
child durable only
parent durable only
both durable
```

Then state what recovery evidence is needed in each state for chosen redo/undo protocol.

## Exit check

Why does “write log first” mean **durable ordering**, not merely calling `write(log_fd, ...)` before `write(data_fd, ...)`?