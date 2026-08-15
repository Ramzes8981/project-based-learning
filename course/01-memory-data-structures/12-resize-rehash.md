# 1.12 — Resize, rehash и завершение Hash Table

**Теория:** ~50 мин  
**Project slice:** ~4–8 часов  
**С телефона:** теория — да

← [`11-hashing-collisions.md`](11-hashing-collisions.md) · → [`13-module-checkpoint.md`](13-module-checkpoint.md)

## Цель

Добавить growth policy и понять, почему при изменении capacity недостаточно просто memcpy старый bucket array.

## Почему resize нужен заранее

Open-addressed table деградирует при высоком load factor. Если дождаться `size == capacity`, insertion может вообще не найти empty slot.

Поэтому table выбирает threshold, например conceptual:

```text
resize when active/taken load exceeds policy threshold
```

Конкретное число — design policy. Его нужно измерять/обосновывать, а не считать математической константой природы.

## Почему нужен rehash

Old index:

```text
hash % old_capacity
```

New index:

```text
hash % new_capacity
```

Если capacity изменилась, bucket mapping почти наверняка меняется. Поэтому active entries нужно **вставить заново** в новую empty table согласно новой probe policy.

Простой byte-copy bucket array нарушит lookup invariants.

## Resize algorithm

Высокоуровнево:

```text
allocate new bucket array
if allocation failed:
    old table remains valid
    return failure

for each OCCUPIED old bucket:
    insert entry into new array using new capacity

swap table metadata to new storage
free old bucket storage
```

Очень важно не потерять old table при allocation/reinsert failure.

## Tombstones и rebuild

Rehash естественно не обязан переносить tombstones: переносим только active entries. Это одновременно очищает накопившиеся deleted markers.

Следовательно, иногда rebuild полезен не только из-за роста capacity, но и для cleanup probe pollution.

## Growth arithmetic

Перед `capacity * growth_factor` проверяй overflow. Также проверяй bytes allocation multiplication.

## Shrink

Automatic shrink добавляет complexity и churn. Для core milestone shrink не обязателен.

Если реализуешь как transfer feature, нужна hysteresis policy, чтобы table не oscillate grow/shrink около одного threshold.

## Instrumentation

Добавь минимум:

- capacity;
- active size;
- tombstone count;
- resize count;
- total probes;
- max probes for one operation или histogram-like metric.

Это позволит обсуждать performance evidence, а не верить слову «быстро».

## Causal questions

1. Почему memcpy buckets после capacity change ломает lookup?
2. Почему tombstones можно не переносить в fresh table?
3. Что должно произойти, если allocation новой table провалилась?
4. Зачем отдельно считать active entries и tombstones?

## Project slice

Заверши [`project/hash-table/SPEC.md`](project/hash-table/SPEC.md):

- growth threshold;
- allocate new storage;
- reinsert active entries;
- atomic-ish failure behavior: old table остаётся usable, если новый allocation не получен;
- tests boundary around resize;
- instrumentation.

### Transfer feature

Выбери одну:

- configurable load-factor threshold;
- quadratic/double-hash probing experiment;
- iterator;
- shrink with hysteresis;
- collision/probe histogram.

## Exit check

Объясни resize как смену hash-to-index mapping, а не как «увеличение массива».
