# 1.14 — Binary Heap и Priority Queue

**Теория:** ~80 мин  
**Упражнение:** ~75 мин  
**С телефона:** да

← [`13-bst-traversals-balanced-trees.md`](13-bst-traversals-balanced-trees.md) · → [`15-dynamic-programming.md`](15-dynamic-programming.md)

## Цель

Понять heap как complete binary tree в contiguous array и реализовать priority queue operations без pointer-based nodes.

## Array representation

Для 0-based index:

```text
left(i)  = 2*i + 1
right(i) = 2*i + 2
parent(i)= (i-1)/2   только при i > 0
```

Последняя оговорка критична для `size_t`: `0 - 1` wraps как unsigned.

Перед вычислением `2*i+2` в generic huge container также нужен overflow reasoning; учебный heap ограничивается реально выделенной capacity.

## Min-heap invariant

Для каждой node:

```text
parent key <= child keys
```

Это **не sorted array**. Гарантируется только отношение parent/children.

## Push / sift-up

Добавить в конец, затем пока invariant нарушен — swap с parent.

Height `O(log n)` → push `O(log n)`.

## Pop-min / sift-down

Root — minimum `O(1)` lookup. Для удаления root переносим последний element наверх, уменьшаем size и восстанавливаем invariant вниз → `O(log n)`.

## Build heap

Последовательные pushes дают `O(n log n)`. Bottom-up heapify имеет `O(n)` total work; это хороший пример, где «каждая операция до log n» не означает автоматически `n log n` для более умного batch algorithm.

## Priority Queue abstraction

Heap — representation. Priority Queue — API/abstract data type: insert item with priority, inspect/pop highest/lowest priority.

Dijkstra позже использует Priority Queue, а не «heap ради heap».

## Упражнение

Реализуй min-heap для `int`:

- init/free через свой Vector или отдельный dynamic array;
- push;
- peek;
- pop;
- invariant checker для tests.

Проверки: empty policy, one item, ascending/descending insert, duplicates, repeated push/pop.

Разбор: [`14-heap-priority-queue.solution.md`](14-heap-priority-queue.solution.md).

## Exit check

Почему inorder traversal heap не даёт sorted order, а repeated pop-min даёт?
