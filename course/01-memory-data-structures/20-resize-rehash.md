# 1.20 — Resize, rehash и завершение Hash Table

**Теория:** ~60 мин  
**Project slice:** ~4–8 часов  
**С телефона:** теория — да

← [`19-hashing-collisions.md`](19-hashing-collisions.md) · → [`21-module-checkpoint.md`](21-module-checkpoint.md)

## Цель

Добавить growth/rebuild policy без потери данных и понять resize как изменение hash-to-index mapping.

## Почему resize до полного заполнения

Open addressing резко деградирует при высокой used load. Поэтому growth threshold — design policy, например `< 0.8`, а не магический закон.

Нужно измерять probes и выбрать threshold осознанно.

## Rehash обязателен

```text
old index = hash % old_capacity
new index = hash % new_capacity
```

После изменения capacity простое `memcpy` buckets разрушает search invariant. Active entries надо вставить в fresh table заново.

Tombstones переносить не нужно: rebuild очищает их.

## Failure-safe progression

```text
validate new capacity arithmetic
allocate new buckets
if fail -> old table untouched
reinsert active entries into temporary new state
if unexpected failure -> clean temporary state, old stays valid
commit/swap table metadata
release old bucket array
```

Не обновляй `table->capacity` до успешной подготовки новой структуры: иначе failure path может оставить half-migrated state.

## Ownership during rehash

Если buckets содержат owned pointers на key/value, реши, переносишь ли ownership pointers без копирования payload или делаешь новые copies. Главное — после commit у каждого allocation должен быть ровно один owner и old bucket cleanup не должен double-free moved payload.

## Arithmetic

Перед growth:

```text
capacity * factor
new_capacity * sizeof(Bucket)
```

проверяй overflow. `realloc` не решает эту задачу автоматически.

## Metrics

Минимум:

- capacity;
- active size;
- tombstone count;
- resize/rebuild count;
- total probes;
- max probes/op или histogram buckets.

## Project slice

Заверши milestone:

- growth threshold;
- failure-safe new storage;
- reinsert active entries;
- tombstone cleanup;
- regression tests around boundary/resize;
- sanitizer run;
- instrumentation;
- одна transfer feature.

Transfer candidates: configurable threshold, second probing strategy experiment, iterator, shrink+hysteresis, probe histogram.

## Exit check

Ты должен уметь нарисовать ownership table **до allocation, во время temporary rehash и после commit** и показать, почему allocation failure не ломает старую table.
