# 1.19 — Hashing, collisions и open addressing

**Теория:** ~75 мин  
**Упражнение:** ~45 мин  
**Project slice:** ~4–8 часов суммарно  
**С телефона:** теория — да

← [`18-probability-for-hashing.md`](18-probability-for-hashing.md) · → [`20-resize-rehash.md`](20-resize-rehash.md)

## Цель

Превратить MiniKV из linear lookup в hash table и уметь объяснить assumptions expected performance.

## Pipeline

```text
key bytes
↓
hash function
↓
integer hash value
↓
index mapping (например hash % capacity)
↓
probe sequence
```

Hash value и bucket index — разные уровни.

## Требования к non-cryptographic hash

Для ожидаемого workload желательно:

- одинаковый key → одинаковый hash;
- быстрое вычисление;
- хорошая distribution;
- изменение key не должно систематически сохранять плохие low bits для выбранного mapping.

Hash не обязан быть collision-free — это невозможно для неограниченного key space и конечного output.

## Collision strategies

**Chaining:** bucket содержит список/collection.  
**Open addressing:** entries живут прямо в bucket array, collision запускает probing.

Core milestone использует open addressing + linear probing, чтобы увидеть locality/tombstone проблемы.

## Linear probing

```text
start = hash % capacity
index(k) = (start + k) % capacity
```

Каждая операция обязана иметь termination condition. При full table нельзя бесконечно обходить buckets.

## States

Минимум:

```text
EMPTY
OCCUPIED
TOMBSTONE
```

`EMPTY` означает: probe chain для отсутствующего key может безопасно закончиться. `TOMBSTONE` означает: здесь entry удалена, но chain мог продолжиться дальше.

## Insert nuance

При поиске места для insert полезно помнить первый tombstone, **но продолжать probe**, пока не выяснишь, что key уже не существует позже в chain. Иначе можно создать duplicate key.

## Load factor

Для open addressing различай:

```text
active_load = active / capacity
used_load   = (active + tombstones) / capacity
```

Tombstones не являются active entries, но загрязняют probe paths.

## Complexity

При хорошей distribution и контролируемой load factor expected lookup/insert близки к `O(1)`. Worst case — `O(n)` probes.

Это expected claim, а не абсолютная гарантия.

## Exercise — probe simulation

Capacity 8, starts:

```text
A -> 3
B -> 3
C -> 4
D -> 3
```

Вставь, удали A через TOMBSTONE, затем выполни lookup B/D и insert нового E. Отдельно покажи ошибочный вариант, где A превращается в EMPTY.

Разбор: [`19-hashing-collisions.solution.md`](19-hashing-collisions.solution.md).

## Project slice

В [`project/hash-table/SPEC.md`](project/hash-table/SPEC.md) реализуй:

- hash function;
- mapping;
- linear probing;
- states;
- insert/update/get/delete;
- active/tombstone accounting;
- guaranteed termination на full/degenerate table.

Пока resize не добавляй. При невозможности вставки верни явный failure и не corrupt existing state.

## Debugging targets

- infinite probe loop;
- duplicate key after tombstone reuse;
- lookup miss after delete;
- lost key/value ownership;
- modulo by zero;
- counter inconsistency.

## Exit check

Объясни точный критерий, когда lookup absent key может остановиться на `EMPTY`, но не на `TOMBSTONE`.
