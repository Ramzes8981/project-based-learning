# Vector — Hints

## Hint 1

Сначала зафиксируй invariant `size <= capacity` и ownership `data`.

## Hint 2

`push` имеет два paths:

```text
space exists -> write
no space -> grow safely -> write
```

## Hint 3

Growth должен сначала успешно получить new allocation, и только потом менять metadata.

## Hint 4

Проверяй обе арифметики: `new_capacity` и `new_capacity * sizeof(element)`.
