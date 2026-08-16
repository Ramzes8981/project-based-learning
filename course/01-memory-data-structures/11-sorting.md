# 1.11 — Sorting: алгоритмы и инженерные trade-offs

**Теория:** ~90 мин  
**Упражнение:** ~90 мин  
**С телефона:** теория — да

← [`10-complexity-invariants-binary-search.md`](10-complexity-invariants-binary-search.md) · → [`12-recursion-recurrences.md`](12-recursion-recurrences.md)

## Цель

Не заучить пять сортировок, а понимать, почему одинаковая цель может иметь разные time/memory/stability trade-offs.

## Термины

**Stable sort:** равные по key элементы сохраняют относительный порядок.

**In-place:** требует только небольшую дополнительную память относительно input (точное определение зависит от модели).

**Adaptive:** может выигрывать на уже почти отсортированном input.

## Insertion sort

Поддерживает sorted prefix и вставляет следующий элемент в нужное место.

- worst: `O(n²)`;
- почти отсортированные данные: часто близко к линейному числу сдвигов;
- stable при аккуратной реализации;
- in-place.

Полезен для маленьких массивов и как building block гибридных сортировок.

## Selection sort

На каждом шаге ищет минимум remainder и ставит на позицию.

- `Θ(n²)` comparisons почти независимо от initial order;
- мало swaps;
- простой, но редко лучший general-purpose выбор.

## Merge sort

```text
split
sort left/right
merge sorted halves
```

- `O(n log n)`;
- легко сделать stable;
- array version обычно требует auxiliary buffer `O(n)`;
- predictable worst case.

## Quicksort

Выбирает pivot, partition и рекурсивно сортирует части.

- average `O(n log n)`;
- worst `O(n²)` при плохом pivot/partition sequence;
- хорошая locality и малые constants делают его практически важным;
- recursive stack depth тоже часть resource analysis.

## Heapsort

Строит binary heap и многократно извлекает extreme element.

- `O(n log n)` worst case;
- in-place;
- обычно unstable;
- access pattern часто менее cache-friendly, чем quicksort.

Heap подробно построим отдельным уроком.

## Почему library sort обычно лучше

Production sorting library учитывает тип данных, architecture, adversarial inputs и годы оптимизации. Учебная реализация нужна для модели, не для замены стандартной библиотеки.

## Comparator safety

Comparator должен задавать согласованный ordering. Нельзя писать `return a - b` для произвольных `int`: subtraction может overflow. Безопаснее сравнение по отношениям:

```c
return (a > b) - (a < b);
```

## Упражнение

Самостоятельно реализуй insertion sort и merge sort для `int[]`.

Для каждого запиши:

- invariant;
- worst-case time;
- extra memory;
- stability;
- boundary tests.

Затем на бумаге пройди один partition quicksort, но полный quicksort код пока не обязателен.

Разбор: [`11-sorting.solution.md`](11-sorting.solution.md).

## Ситуационные вопросы

1. Почему `O(n²)` insertion sort иногда выигрывает у `O(n log n)` на 12 почти sorted элементах?
2. Почему merge sort удобен, когда нужна stability?
3. Что плохой pivot делает quicksort?
4. Почему comparator overflow способен сломать сортировку, даже если массив небольшой?

## Exit check

Для каждого из пяти алгоритмов назови главную причину выбрать или не выбрать его.
