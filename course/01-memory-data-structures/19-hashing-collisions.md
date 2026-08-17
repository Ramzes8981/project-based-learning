# 1.16 — Как находить запись по ключу без полного просмотра массива

**Теория:** ~85 мин  
**Практика:** ~90 мин  
**С телефона:** теория — да; практика — ПК

← [`14-heap-priority-queue.md`](14-heap-priority-queue.md) · → [`20-resize-rehash.md`](20-resize-rehash.md)

## Проблема

MiniKV делает linear lookup:

```text
compare key 0
compare key 1
...
```

При `n` records worst-case `O(n)` comparisons. Хотим использовать сам key, чтобы быстро выбрать небольшую область поиска.

## Hash function

**Хеш-функция (hash function)** превращает key bytes в fixed-size integer hash value:

```text
key bytes → hash → integer
```

Затем table size позволяет выбрать initial slot, например:

```text
index = hash % slot_count
```

Hash value — не «уникальный ID». Разных keys больше, чем возможных hash values/slots.

## Collision неизбежна

Когда два разных keys претендуют на один hash/slot, это **коллизия (collision)**.

Correctness rule:

> hash match или same initial slot никогда не доказывает equality keys.

Нужно сравнить actual keys и иметь collision-resolution policy.

## Probability intuition — достаточно для core

При хорошем distribution slots используются примерно равномерно. Но по мере роста occupancy шанс столкновения увеличивается. Нельзя проектировать table на надежде «collisions почти не будет».

Формальная birthday-style intuition вынесена в optional 1D; correctness от неё не зависит.

## Open addressing + linear probing

Одна простая implementation:

```text
start = hash(key) % slot_count
если slot занят другим key:
    try next slot
    continue until key found / truly empty slot / full cycle
```

Probe sequence must be bounded: нельзя infinite-loop на full table.

## Empty / occupied / deleted — три состояния

Удаление в open addressing сложнее, чем поставить slot в `EMPTY`.

Почему: поиск другого key мог пройти через этот slot из-за earlier collision. Если сделать его truly empty, future lookup остановится слишком рано.

Нужен третий state — **tombstone/deleted marker**.

```text
EMPTY      → probe may stop: key not in later part of this chain
OCCUPIED   → compare key
DELETED    → lookup continues; insert may reuse later
```

## Invariants

- every occupied slot has a valid owned key/value;
- lookup never treats hash equality as key equality;
- probe count is bounded by slot_count;
- tombstone does not terminate search;
- item count excludes tombstones.

## Hash function for course

Можно использовать небольшой documented non-cryptographic byte hash (например FNV-1a style) с unsigned arithmetic. Это **не security hash** и не защита от adversarial collision attacks.

## Практика

До project milestone реализуй table с fixed slot count:

- put/update;
- get;
- delete with tombstone;
- collision fixture, где разные keys имеют один initial slot;
- full-table bounded failure.

Разбор: [`19-hashing-collisions.solution.md`](19-hashing-collisions.solution.md).

## Exit check

Почему удалённый slot нельзя всегда превратить в `EMPTY`, и почему hash equality требует key comparison?