# Hash Table — Hints

## Hint 1 — separate concerns

Раздели conceptual operations:

```text
hash key
find start bucket
probe for existing key / insertion slot
copy/store entry
```

Не пытайся написать весь `set()` одним giant block.

## Hint 2 — termination

Любой probe loop должен иметь максимум bounded attempts относительно capacity. Даже full/corrupt-ish state не должен превращаться в infinite loop.

## Hint 3 — tombstone

Для lookup tombstone означает «продолжай». Для insertion он может быть candidate slot, но поиск existing duplicate key всё равно может требовать продолжения.

## Hint 4 — resize failure

Не освобождай old table, пока fresh table не построена успешно.

## Hint 5 — ownership

Если table копирует strings, продумай cleanup не только normal destroy, но и partial failure во время insertion/rehash.
