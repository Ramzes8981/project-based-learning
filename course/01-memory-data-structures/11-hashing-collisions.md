# 1.11 — Hashing, collisions и open addressing

**Теория:** ~70 мин  
**Упражнение:** ~45 мин  
**Project slice:** ~4–8 часов суммарно  
**С телефона:** теория — да

← [`10-trees-heaps-dp.md`](10-trees-heaps-dp.md) · → [`12-resize-rehash.md`](12-resize-rehash.md)

## Цель

Понять, как hash table превращает key в candidate bucket и почему collisions/load factor определяют реальную стоимость lookup.

## Hash function vs bucket index

Hash function преобразует key в integer-like hash value.

```text
key -> hash(key) -> hash value -> bucket mapping -> table index
```

Hash value и bucket index — не одно и то же. Table capacity ограничена, поэтому index часто получается через modulo или иной mapping.

```text
index = hash % capacity
```

## Требования к hash function

Для non-cryptographic hash table желательно:

- одинаковый key → одинаковый hash;
- небольшие изменения key хорошо распределяют outputs;
- вычисление быстрое;
- distribution по buckets достаточно равномерное для ожидаемых keys.

Cryptographic resistance — отдельная тема. Некоторые attacker-controlled workloads требуют защиты от collision DoS, но не превращай любой учебный hash в «криптографию».

## Collision неизбежен

Разных возможных keys намного больше, чем buckets. По pigeonhole principle collisions неизбежны.

Нужна collision strategy.

## Chaining

Bucket хранит collection/list entries.

Плюсы:

- delete сравнительно прямолинеен;
- load factor может быть >1.

Минусы:

- дополнительные allocations/pointers;
- хуже locality.

## Open addressing

Все entries находятся в bucket array. При collision пробуем другие positions.

### Linear probing

```text
start = hash % capacity
probe 0: start
probe 1: (start+1) % capacity
probe 2: (start+2) % capacity
...
```

Плюсы: простой layout, хорошая locality.

Минус: primary clustering и резкое ухудшение при высоком load factor.

## Load factor

Для open addressing:

```text
alpha = active_entries / capacity
```

Чем ближе table к заполнению, тем длиннее probe sequences в среднем.

Поэтому hash table должна resize **до** полного заполнения.

## Delete и tombstone

Наивно очистить bucket до `EMPTY` после delete опасно.

Пример:

```text
A hashed to 3 -> slot 3
B hashed to 3 -> collision -> slot 4
```

Если удалить A и сделать slot 3 полностью EMPTY, lookup B может остановиться на 3 и ошибочно решить, что B не существует.

Нужна промежуточная state `DELETED/TOMBSTONE`, которая говорит:

> здесь сейчас нет active entry, но probe chain мог продолжиться дальше.

Insert может позже переиспользовать tombstone по выбранной policy.

## Expected vs worst-case

При хорошем distribution и контролируемом load factor lookup expected около `O(1)`.

Worst-case остаётся `O(n)`: например pathological collisions/probe cluster.

Поэтому говорить «hash table lookup всегда O(1)» неверно.

## Modulo intuition

`hash % capacity` раскладывает integer hash по диапазону `[0, capacity-1]`.

Выбор capacity может влиять на interaction с конкретной hash function; course implementation должна иметь ясную, измеряемую policy, а не магические prime numbers без объяснения.

## Probability intuition

Даже хорошее равномерное распределение не означает «collisions не будет». Оно означает, что нет систематической концентрации, а expected behavior можно анализировать статистически.

## Causal questions

1. Почему collision не является ошибкой hash function сам по себе?
2. Почему delete в linear probing требует tombstone или другой специальной обработки?
3. Почему high load factor делает expected lookup хуже?
4. В каком смысле lookup `O(1)` и в каком `O(n)`?

## Exercise — probe simulation

На бумаге возьми table capacity 8 и придуманные hash starts:

```text
A -> 3
B -> 3
C -> 4
D -> 3
```

Вставь их linear probing. Затем удали A тремя способами:

1. оставить active (не delete);
2. сделать EMPTY;
3. сделать TOMBSTONE.

Проведи lookup B/D и объясни correctness.

Разбор: [`11-hashing-collisions.solution.md`](11-hashing-collisions.solution.md).

## Project slice — настоящая Hash Table

Выполни core части [`project/hash-table/SPEC.md`](project/hash-table/SPEC.md):

- hash function;
- bucket mapping;
- linear probing;
- EMPTY/OCCUPIED/TOMBSTONE states;
- insert/update/get/delete;
- load factor tracking.

Не добавляй resize до следующего урока. Но при опасно высокой заполненности операция должна fail контролируемо, а не уходить в бесконечный probe loop.

## Debugging targets

- infinite loop, если table full/tombstone logic неверна;
- duplicate keys из-за неправильного probe termination;
- lookup miss после delete;
- string ownership leaks;
- modulo by zero при invalid capacity.

## Exit check

Нарисуй probe chain с tombstone и объясни, в какой момент lookup может безопасно остановиться.
