# 1.18 — Probability intuition для hashing

**Теория:** ~70 мин  
**Упражнение:** ~45 мин  
**С телефона:** да

← [`17-trie.md`](17-trie.md) · → [`19-hashing-collisions.md`](19-hashing-collisions.md)

## Цель

Понимать слова `expected`, `uniform`, `collision probability` без отдельного курса теории вероятностей.

## Событие и вероятность

Вероятность — модель неопределённости, а не обещание конкретного run. Если шанс collision мал, collision всё равно возможен.

## Expected value intuition

Expected value — среднее значение при мысленном большом числе повторений по заданной distribution. Когда говорим «expected O(1) hash lookup», это не значит «каждая операция всегда один probe».

## Balls into bins

Модель: keys как balls, buckets как bins. Идеальная uniform hash function распределяет каждый key примерно равновероятно по `m` buckets, но collisions остаются неизбежны при достаточно большом числе keys.

## Birthday effect

Для `m` возможных hash outcomes шанс **какой-нибудь пары** совпасть становится заметным гораздо раньше, чем заполнены все `m` значений — примерно при масштабе порядка `sqrt(m)` при независимой uniform модели.

Это объясняет, почему «64-bit hash → collision практически невозможно» нельзя превращать в доказательство уникальности.

## Load factor vs collision

Hash table performance определяется не только raw hash width. Bucket mapping с capacity `m`, probe strategy и current load factor создают collisions на уровне table indices.

## Adversarial inputs

Expected analysis опирается на assumptions distribution. Если attacker может специально подбирать colliding keys под известную weak hash function, average-case модель может разрушиться. Security-hardened hashing — отдельная тема; здесь достаточно понимать границу assumption.

## Упражнение

1. Для table capacity 8 мысленно брось 6 keys по buckets и посчитай load factor.
2. Сравни два распределения: `[0,1,2,3,4,5]` и `[0,0,0,0,0,0]`.
3. Объясни, почему одинаковый load factor не означает одинаковую probe cost.
4. Напиши небольшой Python **или C** simulator как optional lab: random bucket assignment, collision count при разных `n/m`.

Разбор: [`18-probability-for-hashing.solution.md`](18-probability-for-hashing.solution.md).

## Exit check

Сформулируй разницу между worst-case guarantee и expected behavior hash table.
