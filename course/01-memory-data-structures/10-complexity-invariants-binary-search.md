# 1.10 — Complexity, invariants и binary search

**Теория:** ~75 мин  
**Упражнение:** ~60 мин  
**С телефона:** да

← [`09-function-pointers-callbacks.md`](09-function-pointers-callbacks.md) · → [`11-sorting.md`](11-sorting.md)

## Цель

Оценивать рост работы/памяти, отличать worst/average/best case и доказывать корректность цикла через invariant.

## Размер входа

Сначала определить `n`: число элементов, bytes, vertices/edges — в зависимости от задачи. Big-O без определения размера входа часто превращается в лозунг.

## O, Ω, Θ

- `O(f(n))` — асимптотическая верхняя граница роста;
- `Ω(f(n))` — нижняя граница;
- `Θ(f(n))` — обе границы одного порядка.

Для инженерной практики чаще используем Big-O как язык верхнего порядка роста, но полезно знать, что формально это не знак равенства.

Примеры:

```text
linear scan: Θ(n) worst case
binary search sorted array: O(log n)
nested full n×n traversal: Θ(n²)
```

## Константы и реальное время

`O(n)` алгоритм может быть медленнее другого `O(n)` из-за cache misses, дорогой операции внутри цикла или allocations. Complexity отвечает про масштабирование, не заменяет benchmark.

## Логарифм

Binary search каждый шаг оставляет примерно половину кандидатов:

```text
n -> n/2 -> n/4 -> ... -> 1
```

Число делений пополам порядка `log2(n)`.

## Loop invariant

Invariant — утверждение, истинное до/после каждой итерации и помогающее доказать корректность.

Для binary search удобно использовать half-open interval `[lo, hi)`:

```text
если target существует, он находится только внутри [lo, hi)
0 <= lo <= hi <= n
```

Каждый шаг уменьшает диапазон, не выбрасывая возможный target.

## Overflow-safe midpoint

Не обязательно писать:

```c
mid = (lo + hi) / 2;
```

С unsigned sizes `lo + hi` теоретически может wrap. Надёжнее:

```c
mid = lo + (hi - lo) / 2;
```

при invariant `lo <= hi`.

## Binary search precondition

Массив должен быть отсортирован по тому же ordering, который использует search. Без этого `O(log n)` алгоритм просто быстро выдаёт ненадёжный ответ.

## Упражнение

Реализуй binary search на sorted `int[]` с half-open interval.

Contract на выбор:

- вернуть `bool`;
- либо `size_t`, где `n` означает not found.

Tests: `n=0`, один элемент, first/last, missing below/inside/above range, duplicates (задокументируй, обещаешь ли конкретный duplicate index).

Разбор: [`10-complexity-invariants-binary-search.solution.md`](10-complexity-invariants-binary-search.solution.md).

## Causal questions

1. Почему fast benchmark на `n=100` не доказывает хорошую asymptotic complexity?
2. Почему `lo + (hi-lo)/2` лучше `(lo+hi)/2`?
3. Что именно гарантирует invariant `[lo, hi)`?
4. Почему binary search и linked list плохо сочетаются, хотя оба могут хранить sorted values?

## Exit check

Для своего Vector и MiniKV назови `n`, worst-case time основных операций и memory growth.
