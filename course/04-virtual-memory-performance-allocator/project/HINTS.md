# Arena Allocator — Hints

## Hint 1

Represent locations as checked offsets from arena base while doing arithmetic. Convert to pointer only after proving offset within region.

## Hint 2

For fit check prefer subtraction after validating start:

```text
requested <= arena_size - start
```

instead of unchecked `start + requested <= arena_size`.

## Hint 3

Get Stage 1 bump allocator fully tested before adding free-list state.

## Hint 4

Address-ordered free list makes candidate coalescing easier, but still verify physical adjacency explicitly.

## Hint 5

Invalid free detection needs live-allocation knowledge. Do not infer metadata by blindly reading bytes before arbitrary user pointer.

## Hint 6

A fragmentation metric without exact numerator/denominator is decoration. Define it first.