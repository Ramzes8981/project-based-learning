# 4.6 — Как вернуть свободный блок и снова использовать его без потери соседнего места

**Теория:** ~85 мин · **Практика/project:** ~4–6 часов · **С телефона:** theory — да

← [`05-allocator-design.md`](05-allocator-design.md) · → [`06-module-checkpoint.md`](06-module-checkpoint.md)

## Проблема

Bump allocator eventually reaches end even if earlier objects no longer needed. Need track reusable holes.

## Free list

A collection of currently free regions is a **список свободных блоков (free list)**. It may be linked/array/tree; core project can choose simple address-ordered linked metadata.

Each free block needs at least:

```text
offset/address within arena
size
next free block
```

## Finding a block

Policies:

- first-fit: first block large enough;
- best-fit: smallest suitable block;
- others.

Course requires explicit policy + measurement/fragmentation discussion, not “best” claim.

## Split

If free block is larger than request, allocator may return part and keep remainder as smaller free block.

Invariant: resulting allocated/free ranges stay inside arena, non-overlapping, and metadata arithmetic checked.

## External fragmentation

Free bytes can be sufficient in total but split into nonadjacent holes, so large request fails. This is **external fragmentation**.

**Internal fragmentation** is waste inside allocated block due rounding/alignment/size classes.

## Coalescing

If two free blocks are physically adjacent in arena, merge into larger block — **coalescing**.

Critical condition is physical adjacency:

```text
left_offset + left_size == right_offset
```

after overflow-safe arithmetic. Being adjacent in free-list order is not enough unless list is address-ordered and adjacency still explicitly checked.

## Invalid/double free policy

Toy allocator must not silently corrupt metadata. Choose deterministic policy:

- return error status for pointer not exact start of live block;
- return error for already-free block;
- `free(NULL)` policy documented (can be no-op to mirror C `free`, if desired).

Never dereference user pointer before proving it belongs to arena/live allocation metadata.

## Project stage 2

Add free/reuse/split/coalesce + metrics to [`project/SPEC.md`](project/SPEC.md).

## Exit check

Why “neighbor in free list” and “physically adjacent memory block” are different facts, and why only the second justifies coalescing?