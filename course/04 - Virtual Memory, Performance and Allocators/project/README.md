# Arena Allocator — staged project

Build allocator over one preallocated arena. Do **not** replace system `malloc` globally.

## Stage 1 after 4.5

Aligned bump allocation with checked offsets/bounds.

## Stage 2 after 4.6

Free/reuse/split/coalesce, invalid/double-free policy and fragmentation metrics.

Docs: [`SPEC.md`](SPEC.md) · [`ACCEPTANCE.md`](ACCEPTANCE.md) · [`TESTS.md`](TESTS.md) · [`HINTS.md`](HINTS.md).

Student owns implementation; no full solution.