# Arena Allocator — Acceptance

Project is complete when:

## Correctness

- arena create/destroy is explicit;
- aligned allocations stay within arena;
- allocation failure is reported without state corruption;
- free-list reuse works;
- split/coalesce preserve physical layout invariants;
- second placement policy can be compared under same workload.

## Safety

- no pointer arithmetic before range/overflow validation;
- metadata arithmetic cannot silently wrap;
- no overlap, OOB, UAF or double free in valid client use;
- debug invalid-free policy is documented;
- ASan/UBSan or equivalent diagnostics run clean on test suite where compatible.

## Tests

- `make test` covers `TESTS.md`;
- at least one invariant/property checker;
- at least one regression test from an actual bug;
- repeated randomized/deterministic operation sequence.

## Engineering evidence

[`README.md`](README.md) documents ownership, block layout, metrics, known limitations and policy comparison with measured workload rather than intuition only.
