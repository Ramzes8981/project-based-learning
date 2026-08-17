# Разбор 1.8

У stack есть как минимум две разумные реализации.

## Vector-backed

State:

```text
data pointer
size
capacity
```

`push` amortized O(1), `pop` O(1), data contiguous. Периодически resize.

## Linked

State:

```text
head -> node -> node -> ...
```

`push/pop` на head O(1), но каждый node обычно требует allocation и pointer field; locality хуже.

Для high-throughput stack с большим числом маленьких элементов vector обычно проще и cache-friendly. Linked вариант может быть удобен, если размер меняется непредсказуемо и нужны стабильные addresses nodes, но это не бесплатное преимущество.

Важнее уметь объяснить trade-off, чем выбрать «правильный» вариант навсегда.
