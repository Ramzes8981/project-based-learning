# 4.5 — Как выдавать выровненные блоки из собственного region

**Теория:** ~80 мин · **Практика/project:** ~3–5 часов · **С телефона:** theory — да

← [`04-measurement-profiling.md`](04-measurement-profiling.md) · → [`05b-free-lists-coalescing.md`](05b-free-lists-coalescing.md)

## Проблема

`malloc` hides allocator decisions. To understand them, build allocator over one fixed byte region. First milestone only moves forward; no reuse yet.

## Alignment

Many types require addresses divisible by certain power-of-two boundary. Requirement is **выравнивание (alignment)**.

C exposes `_Alignof(T)` / `alignof` with appropriate standard version/header spelling. Returning misaligned pointer and using it as `T *` can violate language/hardware requirements.

## Align-up with overflow check

For power-of-two `align`, conceptual:

```text
padding = (-offset) mod align
aligned = offset + padding
```

In C, check addition does not exceed region/`SIZE_MAX` before computing/committing. Avoid clever bit tricks until precondition “align is nonzero power of two” is validated.

## Bump allocator

State:

```text
base region
region_size
next_offset
```

Allocate:

```text
align next_offset
check requested size fits remaining region
return base + aligned_offset
advance next_offset
```

This **bump allocator** is fast and easy, but individual `free` cannot reclaim holes. That limitation creates next lesson.

## Metadata

Allocator needs enough **metadata** to validate/reclaim blocks later: size/state/links. Stage 1 may store metadata out-of-band in separate table for simplicity rather than invent in-band header arithmetic prematurely.

## Bounds arithmetic

Avoid unsafe check:

```text
if aligned + size <= region_size
```

if `aligned + size` itself can overflow.

Prefer subtraction form after `aligned <= region_size`:

```text
size <= region_size - aligned
```

Then pointer arithmetic occurs only after offset validated within actual region.

## Project stage 1

Implement init + aligned allocate + reset/destroy policy according to [`project/SPEC.md`](project/SPEC.md). No free-list yet.

## Exit check

Why must numeric bounds/alignment be validated before forming/using pointer to resulting location?