# Hash Table in C — staged SPEC

## Prerequisites

- memory/lifetime/allocation from Phase A;
- complexity/invariants;
- hashing/collision/probing lesson 1.16;
- resize/rehash lesson 1.17 for final milestone.

## Stage 1 — fixed slots after 1.16

Behavior:

```text
put(key,value)
get(key)
delete(key)
```

Technical constraints:

- open addressing with documented probe policy;
- distinguish EMPTY/OCCUPIED/DELETED;
- bound every probe by slot_count;
- equality uses key comparison, never hash alone;
- duplicate put updates, does not increase item count;
- deletion preserves lookup through collision chain;
- table-full returns controlled failure.

## Stage 2 — resize after 1.17

- explicit load/grow policy;
- allocate new slot array separately;
- check slot-count and byte arithmetic before operations;
- reinsert OCCUPIED entries under new slot count;
- do not copy tombstones as live history;
- commit replacement only after successful rebuild;
- allocation/rebuild failure leaves old table usable.

## Ownership

Choose key policy and document it. Recommended learning policy: table owns copies of keys and frees them exactly once on delete/destroy/rehash transfer.

Rehash must not accidentally double-own or double-free key storage. Either move ownership safely or create a fresh representation with clear rollback.

## Hash contract

A small non-cryptographic hash is enough. README must explicitly state it is not adversarial/security hardening.

## Transfer task

Choose one:

- iterator/callback over occupied entries;
- reserve API;
- tombstone cleanup policy;
- string value with explicit ownership.

Write invariant/failure plan before code.