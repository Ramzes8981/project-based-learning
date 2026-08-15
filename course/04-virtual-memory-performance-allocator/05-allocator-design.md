# 4.5 — Allocator design: alignment, free list, fragmentation

**Теория:** ~85 мин  
**Project:** ~10–16 часов суммарно  
**С телефона:** теория — да

← [`04-measurement-profiling.md`](04-measurement-profiling.md) · → [`06-module-checkpoint.md`](06-module-checkpoint.md)

## Цель

Самостоятельно управлять blocks внутри одной arena, сохраняя layout invariants и измеряя fragmentation.

## Scope

Мы **не** пишем замену glibc malloc.

```text
mmap -> one arena
course allocator manages sub-blocks inside arena
```

Это изолирует allocator algorithms от сложности OS allocator implementation.

## Alignment

Некоторые object types требуют address, кратный alignment.

Если allocator возвращает misaligned pointer для type — использование может быть UB/slow/fault depending architecture.

Для power-of-two alignment `a` полезна идея:

```text
aligned = ceil(n / a) * a
```

Bit trick допустим только после доказательства `a` power-of-two и overflow safety.

## Block metadata

Conceptual block:

```text
[ header | payload ........ ]
```

Header может хранить:

- block size;
- free/used state;
- next free block offset/pointer;
- debugging magic/checksum optionally.

Metadata сама занимает arena space и должна учитываться в arithmetic.

## Bump allocator

Самая простая policy:

```text
next = aligned cursor
cursor += block size
```

Allocate быстро, individual free отсутствует. Хорош для temporary arena workloads.

Это first milestone slice.

## Free list

Для reuse нужен список свободных blocks.

First-fit:

- пройти free list;
- взять первый достаточный block.

Best-fit:

- найти smallest sufficient block.

Нет универсально лучшей policy: разные fragmentation/search costs.

## Splitting

Если free block намного больше request, его можно разделить:

```text
[allocated part][remaining free block]
```

Но remainder должен быть достаточно большим для metadata + meaningful aligned payload. Иначе создаётся unusable fragment.

## Coalescing

Adjacent free blocks можно объединять.

Важно: объединяются **физически соседние в arena** blocks, а не просто соседние nodes free list.

Нужен способ определить adjacency через offsets/sizes.

## Fragmentation

Internal fragmentation: wasted bytes **внутри** allocated block из-за alignment/rounding/policy.

External fragmentation: free space разбито на куски; total free может быть большим, но largest free block мал.

Leak: память всё ещё считается allocated/достижимой allocator metadata, но application потеряла ownership/reference или забыла free.

Не смешивай эти понятия.

## Required metrics

Allocator должен уметь сообщить:

- arena bytes;
- active requested bytes;
- allocated block bytes;
- free bytes;
- free block count;
- largest free block;
- allocation/free counts.

## Double free

Allocator должен иметь defined debug behavior. Core может detect очевидный repeated free через block state/assert/error. Production security-hardening allocator значительно сложнее.

## Project progression

[`project/SPEC.md`](project/SPEC.md):

1. arena mapping;
2. bump allocate;
3. alignment;
4. metadata;
5. free list;
6. reuse;
7. split;
8. coalesce;
9. metrics;
10. compare policies.

## Causal questions

1. Почему total free bytes не гарантируют успешный large allocation?
2. Почему free-list neighbor не обязательно physical neighbor?
3. Где возникает internal fragmentation?
4. Почему allocator bug часто проявляется далеко от места corruption?

## Exit check

Нарисуй arena до/после `alloc A`, `alloc B`, `free A`, `free B`, coalesce.
