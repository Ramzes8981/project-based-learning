# Arena Allocator — Hints

## Hint 1

Сначала bump allocator. Не начинай с free list.

## Hint 2

Для каждого block умей вычислить:

```text
block_start
header_end/payload_start
payload_end
next_block_start
```

## Hint 3

Coalescing требует physical adjacency: `left_end == right_start`.

## Hint 4

Если stats расходятся, сформулируй conservation-like invariant bytes arena = metadata + allocated payload/padding + free regions.

## Hint 5

Policy comparison должен менять только placement choice при одинаковом request trace.
