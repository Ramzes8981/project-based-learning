# Hash Table — Hints

## Hint 1

Сначала fixed-size table. Если collision/delete semantics неверны, resize только размножит bug.

## Hint 2

Probe loop должен иметь explicit maximum iterations `slot_count`.

## Hint 3

Для lookup `DELETED` означает «продолжай», а `EMPTY` — «можно остановиться: key не найден дальше в этой probe chain».

## Hint 4

Resize проще reason about как transaction-like rebuild:

```text
prepare new table
populate completely
commit pointer/metadata swap
release old container storage
```

Не уничтожай единственный correct old state до commit.

## Hint 5

Отдельно нарисуй key ownership при rehash. Именно здесь легко создать double free или leak.

## Hint 6

Не оптимизируй hash function до collision fixtures и invariants. Correct collision handling важнее красивого distribution benchmark.