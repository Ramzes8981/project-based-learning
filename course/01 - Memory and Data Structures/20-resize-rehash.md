# 1.17 — Почему hash table нельзя просто увеличить копированием slots

**Теория:** ~70 мин  
**Практика/project:** ~4–6 часов  
**С телефона:** теория — да; project — ПК

← [`19-hashing-collisions.md`](19-hashing-collisions.md) · → [`20b-graphs-paths.md`](20b-graphs-paths.md)

## Проблема

Index зависит от table size:

```text
hash % slot_count
```

Если `slot_count` меняется, для того же key initial slot обычно меняется тоже. Поэтому raw-copy старого slot array в начало нового ломает lookup logic.

## Rehash

При росте table нужно создать новый slot array и **заново вставить (rehash)** каждую occupied entry по правилам нового `slot_count`.

```text
old occupied entries
→ compute position under new size
→ probe in new table
→ commit new table
```

Tombstones переносить не нужно: они описывали probe history старого table layout.

## Load factor

**Коэффициент заполнения (load factor)** — отношение числа occupied entries к number of slots (точная policy может отдельно учитывать tombstones).

Высокий load factor увеличивает probe chains. Grow threshold — performance policy, не correctness theorem.

## Failure-safe resize

Новый table строится отдельно. Если allocation или reinsertion fails:

```text
old table remains valid owner/source of truth
```

Commit replacement только после успешного полного rebuild.

## Arithmetic

При вычислении new slot count и bytes:

- check growth overflow;
- check `new_count * sizeof(slot)` before multiplication;
- не допускай zero slot count в hash/modulo path.

## Project

Теперь Hash Table milestone получает dynamic resize. Выполни [`project/hash-table/SPEC.md`](project/hash-table/SPEC.md).

## Causal questions

1. Почему `memcpy(old_slots, new_slots, ...)` не сохраняет lookup semantics после size change?
2. Почему tombstones не нужно переносить?
3. Почему resize лучше commit-ить целиком после успешного rebuild?

## Exit check

Ты можешь объяснить rehash через зависимость `index` от table size, а не как ритуальный шаг реализации.