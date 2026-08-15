# 7.8 — Transactions, WAL, crash recovery и isolation

**Теория:** ~100 мин  
**Design exercise:** ~90 мин  
**С телефона:** да

← [`07-buffering-query-costs.md`](07-buffering-query-costs.md) · → [`09-module-checkpoint.md`](09-module-checkpoint.md)

## Цель

Понять, какие guarantees отсутствуют у SimpleDB и из каких механизмов строится transactional storage engine.

## Transaction

Transaction группирует operations в logical unit с desired guarantees.

ACID — не одна feature:

- **Atomicity** — all-or-nothing effects transaction;
- **Consistency** — application/DB invariants preserved when transaction transitions valid states;
- **Isolation** — concurrent transactions observe constrained interference;
- **Durability** — committed result survives defined failures.

Термин consistency здесь не означает distributed consistency model; context важен.

## Crash problem

B+tree split может требовать:

```text
write new leaf
update old leaf
update parent
maybe update root/header
```

Crash после шага 2 оставляет partial structural change.

Individual page `fsync` не даёт atomic multi-page update.

## WAL idea

Write-Ahead Log:

> information needed for recovery is made durable in log **before** corresponding data pages are allowed to become durable in a way that depends on it.

Simplified redo-style flow:

```text
append log record describing change
flush WAL to required durability point
mark transaction committed in WAL
later write dirty data pages
```

Recovery replays committed changes/ignores or undoes incomplete work depending WAL design.

Real algorithms use LSNs, checkpoints, physiological logging, checksums etc.; core only builds mental model.

## Undo journal alternative

Rollback journal copies old page contents before overwriting main DB. On crash unfinished transaction restores originals.

WAL and rollback journal solve similar atomicity/recovery goals with different read/write/concurrency trade-offs.

## Checkpoint

WAL cannot grow forever. Checkpoint propagates log-covered state into main storage and advances truncation/reuse point according to recovery rules.

## Isolation anomalies

Concurrent transactions can cause:

- dirty read;
- non-repeatable read;
- lost update;
- write skew/phantom-like effects depending model.

Isolation levels/MVCC/locking constrain which schedules are visible.

## Locking vs MVCC intuition

Locking prevents/conflicts operations by locks.

MVCC keeps multiple versions so readers/writers may overlap more, but version visibility/garbage collection/conflict detection become complex.

## Durability boundary

Transaction commit response must define what failure model it survives. If system returns success before required log/data sync, durability promise is weaker.

## SimpleDB limitation artifact

Напиши `RECOVERY_LIMITATIONS.md`:

- which writes can corrupt after process/machine crash;
- whether single insert is atomic;
- concurrent writers supported?;
- what WAL/journal would need;
- what fsync points would exist conceptually;
- what is **not implemented**.

## Design exercise

Для operation `insert` that may split leaf + root:

1. list pages modified;
2. design conceptual WAL records;
3. state ordering constraints;
4. simulate crash before/after commit record;
5. explain recovery outcome.

No fake WAL code required.

## Causal questions

1. Why durable page write != atomic transaction?
2. Why WAL must be written ahead of dependent data pages?
3. Why isolation is independent from durability?
4. Why transaction `Consistency` is not automatically guaranteed by DB engine without application constraints?

## Exit check

Given corruption after power loss, separate file durability, multi-page atomicity, recovery metadata and concurrent isolation.
