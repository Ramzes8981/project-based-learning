# Arena Allocator — staged SPEC

## Common prerequisites

C ownership/lifetime/checked `size_t`, alignment lesson, sanitizer testing.

## Stage 1 — aligned allocation

Arena created from a caller-owned or internally allocated byte region according to documented policy.

`arena_alloc(size, align)` behavior:

- validate nonzero power-of-two alignment (or narrower documented allowed set);
- align current offset with overflow checks;
- prove `size <= arena_size - aligned_offset` before forming returned location;
- return suitably aligned block start;
- advance state only on success;
- failure leaves arena logical state unchanged.

Zero-size policy must be explicit. Recommended course policy: reject or return a stable non-owning sentinel only if carefully documented; simplest is return `NULL`/failure for size zero.

## Stage 2 — free/reuse

`arena_free(ptr)` accepts only exact starts of currently live allocations according to metadata.

- invalid pointer → controlled failure;
- double free → controlled failure;
- no metadata corruption;
- freed region enters reuse structure;
- suitable free block may split;
- physically adjacent free blocks may coalesce;
- coalescing uses validated offset/size arithmetic.

## Ownership

Arena owns its backing region if initialized via internal allocation; otherwise borrowed-region mode must not free caller memory. Pick one mode for core, not ambiguous mix.

Returned blocks are borrowed from arena and cannot outlive arena. `arena_destroy` invalidates all live block pointers.

## Metrics

Expose enough state to report:

- arena bytes;
- live allocated payload bytes;
- free bytes;
- largest free block;
- number of free blocks;
- alignment/internal waste estimate if feasible.

Metrics definitions documented; do not double-count metadata/payload without saying which.

## Transfer

Choose allocation policy experiment (first-fit vs best-fit/address-order/etc.) and justify with measured workload.