# Arena Allocator — рабочий README

## Status

## API

Зафиксируй signatures allocate/free/stats/destroy и error semantics. `free(NULL)`/invalid pointer policy должна быть явной, а не случайной.

## Arena

```text
backing: mmap / approved buffer
arena bytes:
alignment contract:
```

## Block layout

Нарисуй физическую layout:

```text
header | payload | header | payload | ...
```

Какие bytes учитываются в block size? Где padding? Как проверить physical adjacency?

## Arithmetic safety

Документируй helpers/guards для:

- align-up;
- `header + payload`;
- `count * size`;
- offsets inside arena.

Никакое вычисление размера не должно молча wrap.

## Ownership

Arena owner, block ownership, lifetime returned pointers, invalidation after destroy.

## Free structure

First-fit/second policy, free-list ordering, split/coalesce rules.

## Invariants

- blocks не overlap;
- каждый block внутри arena;
- payload alignment;
- free block не появляется дважды;
- metadata chain/offsets valid;
- coalescing only physical neighbors;
- stats согласованы с actual layout.

## Tests

```text
make test
```

Добавь invariant checker и randomized operation sequence against a simple reference bookkeeping model, если это помогает.

## Metrics

Internal/external fragmentation, largest free block, active requested bytes, operations.

## Debugging story

## Policy comparison

Сравни минимум две placement/growth policy по одинаковому workload.
