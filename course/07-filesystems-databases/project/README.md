# SimpleDB — рабочий README

## Status / Build

Executable name, `make`, `make test`, create/open command.

## File format

[`FORMAT.md`](FORMAT.md) — fixed contract. Документируй выбранный internal-page separator variant A/B и любые разрешённые limits.

## Pager

Who owns page buffers? Cache policy? Dirty state? Robust `pread/pwrite` loops? Page-number/offset overflow checks?

## Tree invariants

- keys sorted within node;
- separator invariant chosen once;
- child/parent references valid;
- leaves same depth;
- leaf chain ordered/no cycles;
- cell_count fits page capacity;
- every reachable record appears exactly once.

## Serialization

List encode/decode helpers; no raw struct persistence. Reserved bytes deterministic.

## Tests

- `TESTS.md`;
- reopen/persistence;
- split boundary cases;
- corruption fixtures;
- `tools/inspect_db.py` independent header/page inspection;
- sanitizer run.

## Metrics

Page reads/writes/cache hits/splits/tree height or other chosen counters.

## Recovery/durability

Complete [`RECOVERY_LIMITATIONS.md`](RECOVERY_LIMITATIONS.md). Core v1 has no WAL/transaction/crash-atomic multi-page commit.

## Known limitations / transfer / debugging story

