# 1.11 — Когда выгодно сначала упорядочить данные

**Теория:** ~70 мин  
**Практика:** ~80 мин  
**С телефона:** теория — да; практика — ПК

← [`10-complexity-invariants-binary-search.md`](10-complexity-invariants-binary-search.md) · → [`12-recursion-recurrences.md`](12-recursion-recurrences.md)

## Проблема

Binary search быстрый, но требует sorted data. Значит, иногда мы платим стоимость сортировки заранее, чтобы будущие операции стали дешевле или проще.

## Что значит «sorted»

Для ascending integers invariant результата:

```text
a[i] <= a[i + 1] для каждого допустимого i
```

Это oracle, который можно проверить независимо от конкретного algorithm.

## Простые алгоритмы нужны как baseline

### Insertion sort

Идея:

```text
prefix [0, i) уже отсортирован
вставить a[i] в правильное место
расширить sorted prefix
```

Хорош для маленьких или почти sorted inputs; worst-case `O(n²)` moves/comparisons.

### Selection sort

На каждом шаге найти минимум в unsorted suffix и поставить его на границу. Простая mental model, но даже на почти sorted data продолжает делать квадратичное число comparisons.

## Divide-and-conquer sorting

### Merge sort

Разделить input, отсортировать части, затем слить sorted sequences. Typical time `O(n log n)`, но straightforward implementation требует дополнительного storage.

### Quicksort intuition

Разделить around pivot, затем сортировать parts. Average behavior часто хорош, но bad pivot/input может дать `O(n²)` without mitigation. Standard library implementation details не обязаны совпадать с учебным quicksort.

## `qsort` и comparator contract

C standard library даёт generic `qsort`. Comparator должен вернуть negative/zero/positive according to order.

Плохой pattern:

```c
return a - b;
```

Разность signed ints может overflow.

Безопаснее сравнить явно:

```c
return (a > b) - (a < b);
```

## Stability

**Stable sort** сохраняет relative order records с equal keys. Это важно, если данные уже были упорядочены по другому field.

Не все sorting algorithms/implementations stable; contract нужно проверять, а не угадывать по названию.

## Практика

1. Реализуй insertion sort для `int`.
2. После каждого outer step assert/check sorted-prefix invariant в test build.
3. Сравни number of comparisons/moves на sorted, reverse и random small arrays.
4. Отдельно используй `qsort` с overflow-safe comparator.

Разбор: [`11-sorting.solution.md`](11-sorting.solution.md).

## Exit check

Какое будущее workload оправдывает стоимость предварительной сортировки, и почему «`O(n log n)`» ещё не выбирает algorithm автоматически?