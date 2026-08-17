# Vector — Hints

## Hint 1

Write invariants at the top of `vector.c` before implementation.

## Hint 2

`push` is easier to reason about as two phases:

```text
ensure room
commit element
```

Do not increment `len` before the write is guaranteed possible.

## Hint 3

For growth, compute `new_capacity`, validate it and its byte multiplication, call `realloc` into temporary pointer, then commit fields.

## Hint 4

A deterministic failing allocator makes failure-state tests possible without dangerous resource exhaustion.

## Hint 5

If you store a pointer to `data[i]`, then call an operation that may grow the vector, assume that pointer is invalid until reacquired.