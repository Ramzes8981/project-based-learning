# 9.5 — Persistence, graceful shutdown и recovery contracts

**Теория:** ~85 мин  
**Project/failure lab:** ~3–5 часов  
**С телефона:** да

← [`04-backpressure-timeouts-overload.md`](04-backpressure-timeouts-overload.md) · → [`06-observability-sli-slo.md`](06-observability-sli-slo.md)

## Цель

Определить, какие states должны пережить restart и что service обещает при graceful vs forced termination.

## Reuse vs rewrite

Capstone может переиспользовать SimpleDB concepts/code и KV server components, но interface boundaries должны быть пересмотрены.

Не copy-paste два проекта в один giant `main.c`.

## Persistence contract

Нужно определить:

```text
SET success response означает что?
- updated only in memory?
- written to page cache?
- fsync-complete?
```

Core capstone может выбрать modest durability policy, но она должна быть честно описана.

## Graceful shutdown phases

Typical sequence:

```text
1. mark shutting down
2. stop accepting new work
3. choose drain/reject queued work policy
4. wait/join workers
5. flush storage/metadata per durability contract
6. close resources
7. exit
```

Order matters. Closing DB while workers still use it creates use-after-close/race.

## Forced termination

SIGKILL/power loss bypass normal cleanup. Recovery depends persistent format/protocol, not destructor hope.

Core SimpleDB lacks WAL, so forced kill during multi-page mutation may corrupt. Capstone must either:

- accept/document this limitation;
- or implement a **small bounded persistence strategy** with simpler atomic snapshot/log contract as transfer.

Do not pretend WAL exists if it doesn't.

## Snapshot approach

For modest KV service one course option:

```text
in-memory state
→ periodic/full snapshot temp file
→ sync
→ atomic rename-style replacement
```

Trade-offs:

- simple recovery;
- expensive O(data size) snapshot;
- data since last snapshot may be lost;
- shutdown latency.

## Append-only log approach

Alternative:

```text
append mutation records
replay on startup
periodic compaction/snapshot
```

Trade-offs:

- faster incremental writes;
- log growth;
- record checksums/partial-tail handling;
- idempotent replay/sequence.

Core chooses one persistence approach and documents exact guarantee.

## Recovery validation

Startup must validate persistent bytes/version/lengths. Corrupt file should cause explicit safe failure/recovery policy, not OOB parsing.

## Failure lab

Test:

- clean restart;
- SIGTERM graceful;
- forced process kill between mutations;
- truncated/corrupted copy of storage file;
- full-like/write failure simulated via injected error or constrained temp environment.

Never intentionally fill system disk.

## Exit check

«Persistent across restart» должно быть заменено точным statement: после каких acknowledgements/failures какие writes guaranteed/lost/corruptible?
