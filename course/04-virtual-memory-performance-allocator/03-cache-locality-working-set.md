# 4.3 — Cache hierarchy, locality и working set

**Теория:** ~70 мин  
**Lab:** ~90 мин  
**С телефона:** теория — да

← [`02-page-tables-tlb-faults.md`](02-page-tables-tlb-faults.md) · → [`04-measurement-profiling.md`](04-measurement-profiling.md)

## Цель

Объяснить, почему два `O(n)` алгоритма могут различаться по runtime в разы из-за memory access pattern.

## Memory hierarchy

Conceptually:

```text
registers
L1 cache
L2 cache
L3/LLC
DRAM
storage
```

Чем ближе к CPU, тем меньше capacity и ниже latency/выше bandwidth.

Точные nanoseconds зависят от hardware — курс не требует заучивания одной таблицы latency.

## Cache line

Cache переносит данные блоками/lines, а не отдельными C objects. На common x86-64 line часто 64 bytes, но измеряй/проверяй platform details, если это важно.

## Spatial locality

Если после `a[i]` скоро читаем `a[i+1]`, соседние bytes уже могут быть в той же/следующей prefetched line.

Contiguous arrays используют spatial locality хорошо.

## Temporal locality

Если same data повторно используется скоро, оно может остаться в cache.

## Pointer chasing

Linked list nodes на heap могут быть разбросаны. Каждый `next` зависит от предыдущей memory load, что затрудняет prefetch и увеличивает cache misses.

Это объясняет, почему linked list с похожим Big-O может проигрывать vector.

## Stride

Traversal:

```text
stride 1: 0,1,2,3...
stride 16: 0,16,32...
```

может использовать cache lines по-разному.

## Matrix order

Для row-major C array последовательный проход по rows обычно cache-friendly. Column-wise traversal делает большие strides.

Это мост к NumPy: contiguous layout/order влияет на скорость vectorized/native kernels.

## Working set

Если active data значительно больше cache, повторное использование может не успевать попасть в cache hits.

Performance — свойство workload + data size, а не только function source.

## Lab

Создай большой contiguous integer array и сравни:

- sequential traversal;
- stride traversal;
- shuffled index traversal;
- linked pointer-chasing structure схожего объёма.

Повторяй runs, не делай вывод из одного измерения.

Запиши:

```text
input size
pattern
median-ish runtime
hypothesis
```

## Causal questions

1. Почему linked list может проиграть array при одинаковом `O(n)` scan?
2. Почему working set должен быть частью benchmark description?
3. Почему cache line делает чтение одного byte потенциально связанным с соседними bytes?
4. Как это связано с NumPy contiguous arrays?

## Exit check

Сначала объясняй memory access pattern, потом говори «CPU медленный».
