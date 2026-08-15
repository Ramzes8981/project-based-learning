# 1.9 — Complexity, search, sort и recursion

**Теория:** ~70 мин  
**Упражнения:** ~60–90 мин  
**С телефона:** теория/задачи — да

← [`08-linked-structures.md`](08-linked-structures.md) · → [`10-trees-heaps-dp.md`](10-trees-heaps-dp.md)

## Цель

Получить обязательный algorithms foundation: Big-O/Ω/Θ, binary search invariant, простые sorts и recursion.

## Зачем asymptotics

Runtime в миллисекундах зависит от CPU, compiler, cache и input. Asymptotic notation отвечает на другой вопрос: **как растёт resource cost при росте input size**.

## O, Ω, Θ

Упрощённо:

- `O(f(n))` — upper asymptotic bound;
- `Ω(f(n))` — lower bound;
- `Θ(f(n))` — tight bound того же порядка сверху и снизу.

Для обычного полного прохода массива:

```text
T(n) = a*n + b
```

по порядку роста `Θ(n)`.

Константы важны для реальной производительности, но asymptotics абстрагирует их, чтобы сравнивать масштабирование.

## Common growth rates

```text
O(1)
O(log n)
O(n)
O(n log n)
O(n^2)
O(2^n)
```

Это не рейтинг «хорошо/плохо» вне context. Для маленького `n` простой `O(n)` алгоритм может обогнать более сложный `O(log n)` из-за constants/locality.

## Linear vs binary search

Binary search требует sorted data.

Основной invariant:

> если target существует, он находится внутри текущего search interval.

Каждый шаг делит interval примерно пополам, поэтому число шагов порядка `log2(n)`.

Но если data unsorted — invariant не существует, и алгоритм неверен независимо от скорости.

## Off-by-one

Выбери один interval convention и не смешивай:

- inclusive `[lo, hi]`;
- half-open `[lo, hi)`.

Half-open intervals часто удобны, потому что length = `hi - lo`.

## Simple sorts

Insertion sort полезен для reasoning:

Invariant:

> prefix до текущей позиции уже отсортирован.

Worst-case `Θ(n^2)`, но на маленьких/nearly-sorted inputs может быть практичным.

Selection sort тоже `Θ(n^2)` comparisons; учебная ценность — простой анализ операций.

Production sorting обычно использует более сложные hybrid algorithms; мы не выдаём учебные sorts за оптимальный стандарт.

## Recursion

Recursive function вызывает себя на меньшей subproblem и должна иметь:

- base case;
- progress к base case.

Пример factorial математически прост, но systems-инженеру важнее понимать call stack cost и риск слишком глубокой recursion.

## Simple sums

Nested loop:

```text
for i=0..n-1
    for j=0..i-1
```

число inner iterations:

```text
0 + 1 + 2 + ... + (n-1) = n(n-1)/2
```

следовательно `Θ(n^2)`.

## Causal questions

1. Почему binary search быстрее asymptotically, но не применим к произвольному unsorted array?
2. Чем `O(n)` отличается от утверждения «ровно n операций»?
3. Как loop invariant помогает доказать correctness?
4. Почему recursion depth — systems concern?

## Упражнения

1. Реализуй binary search для sorted `int[]` с half-open interval.
2. Запиши invariant словами.
3. Проверь empty array, one element, first/last, missing target.
4. Реализуй insertion sort для маленького array.
5. Для трёх коротких nested loops выведи порядок роста через sums.

Разбор: [`09-complexity-search-sort-recursion.solution.md`](09-complexity-search-sort-recursion.solution.md).

## Exit check

Ты должен уметь отличить correctness requirement от performance requirement: быстрый неверный binary search остаётся неверным.
