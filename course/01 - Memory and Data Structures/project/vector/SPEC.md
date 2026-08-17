# Vector in C — SPEC

## Prerequisites

1.1–1.7: pointer, bounds/one-past, checked `size_t`, lifetime/ownership, dynamic allocation, UB diagnostics, `len/capacity` model.

## Observable behavior

- initialized vector is empty;
- push preserves insertion order;
- get only succeeds for `index < len`;
- repeated pushes grow storage transparently;
- allocation failure returns failure and preserves prior logical state;
- destroy releases resources and may be called on an initialized empty vector.

## Required state

Conceptually:

```text
owned data pointer
len
capacity
```

Names/types may differ if contract remains clear.

## Invariants

```text
len <= capacity
valid elements are [0, len)
capacity == 0 permits data == NULL
if data != NULL, vector owns that allocation
```

## Growth

- use geometric growth, not `+1` every push;
- calculate new byte size with overflow checks before multiplication;
- use temporary pointer for `realloc`;
- zero-size growth via `realloc(ptr, 0)` is not used;
- only commit new pointer/capacity after successful allocation.

## Pointer validity contract

Any successful operation that grows storage may invalidate previously borrowed pointers to elements. Document this in README.

## Error/resource policy

- no write occurs outside allocated range;
- no leak/double free/UAF;
- failure leaves vector destructible and prior elements intact;
- `destroy` makes the chosen postcondition explicit, preferably `{data=NULL,len=0,capacity=0}`.

## Transfer task

Add one operation not directly specified here, e.g. `pop`, `reserve`, or `remove_at`, and write its invariant-preservation argument before implementation.