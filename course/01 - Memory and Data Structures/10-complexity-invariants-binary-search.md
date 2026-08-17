# 1.10 — Как сравнивать способы решения и не ломать главный invariant

**Теория:** ~75 мин  
**Практика:** ~70 мин  
**С телефона:** теория — да; практика — ПК

← [`09-function-pointers-callbacks.md`](09-function-pointers-callbacks.md) · → [`11-sorting.md`](11-sorting.md)

## Проблема 1: «работает» ещё не значит «масштабируется»

MiniKV искал имя последовательным просмотром. Для 5 records это незаметно. Для миллиона — уже инженерный выбор.

Нам нужен язык, который описывает, как растёт количество работы при росте input.

## Считаем рост, а не наносекунды

Если поиск в худшем случае смотрит каждый элемент:

```text
N records → до N сравнений
```

Говорят, что работа растёт линейно: **`O(n)`**.

Если операция делает примерно одинаковое число шагов независимо от `n`, говорим `O(1)`. Если каждое действие сокращает оставшийся диапазон примерно вдвое — часто появляется `O(log n)`.

**Big-O** здесь — модель роста, а не точное время. `O(1)` не означает «мгновенно», а `O(n)` не означает «плохо всегда».

## Проблема 2: быстрый алгоритм легко написать неправильно

Для отсортированного массива можно не смотреть каждое значение. Сравниваем середину и отбрасываем половину кандидатов — **binary search**.

Но корректность держится на условии:

```text
если target существует, он остаётся внутри текущего диапазона кандидатов
```

Такое условие, которое мы обязаны сохранять после каждого шага, называется **инвариантом (invariant)**.

## Half-open range

Удобный вариант диапазона:

```text
[lo, hi)
```

`lo` включён, `hi` не включён.

Empty range:

```text
lo == hi
```

Midpoint без `lo + hi` overflow:

```c
size_t mid = lo + (hi - lo) / 2;
```

## Почему sortedness — prerequisite, а не деталь

Binary search использует факт порядка. Если array не отсортирован, сравнение с middle не даёт права выбросить половину кандидатов.

Это хороший пример причинного contract:

```text
precondition: sorted data
→ operation can discard half
→ O(log n) comparisons
```

## Cost model шире CPU

В systems работе стоимость может означать:

- comparisons;
- memory accesses;
- bytes copied;
- allocations;
- syscalls;
- disk I/O;
- network round trips.

Big-O полезен только вместе с тем, **какую операцию мы считаем**.

## Практика

1. Реализуй binary search по sorted `int` array с range `[lo, hi)`.
2. Проверь empty, one element, first, last, missing-between, missing-outside.
3. Для размеров 8, 16, 32 вручную оцени maximum comparisons.
4. Напиши invariant одной фразой и покажи, почему обе ветви update его сохраняют.

Разбор: [`10-complexity-invariants-binary-search.solution.md`](10-complexity-invariants-binary-search.solution.md).

## Causal questions

1. Почему binary search не работает на произвольно перемешанном массиве?
2. Почему `mid = lo + (hi - lo)/2` безопаснее `mid = (lo + hi)/2` для unsigned sizes?
3. Почему `O(n)` linear scan может быть лучшим выбором для очень маленького `n`?

## Exit check

Ты умеешь назвать operation count, precondition и invariant, а не просто сказать «binary search = O(log n)».