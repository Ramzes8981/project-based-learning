# 1.10 — Trees, heaps и dynamic programming fundamentals

**Теория:** ~65 мин  
**Упражнения:** ~60 мин  
**С телефона:** да

← [`09-complexity-search-sort-recursion.md`](09-complexity-search-sort-recursion.md) · → [`11-hashing-collisions.md`](11-hashing-collisions.md)

## Цель

Закрыть минимальный обязательный CS-блок по trees/priority queues/DP, не превращая Module 1 в отдельный algorithms semester.

## Binary Search Tree

BST invariant:

```text
keys(left subtree) < node.key < keys(right subtree)
```

при выбранной политике unique keys.

Search cost зависит от height `h`: `O(h)`.

Если tree balanced, `h` порядка `log n`. Если inserts пришли в плохом порядке, обычный BST может выродиться в chain с `h = n`.

Поэтому фраза «BST search O(log n)» без условия balance — неточная.

## Tree traversal

Основные DFS orders:

- preorder;
- inorder;
- postorder.

Для BST inorder traversal выдаёт keys в sorted order при стандартном invariant.

## Heap

Binary heap — complete binary tree, обычно хранящийся в array.

Для zero-based indexing:

```text
left(i)  = 2*i + 1
right(i) = 2*i + 2
parent(i)= (i-1)/2
```

Min-heap invariant:

```text
parent <= children
```

Минимум находится в root `O(1)`, insert/extract-min требуют восстановить invariant по height → `O(log n)`.

Heap — основа priority queue и позже Dijkstra.

## Почему heap не sorted array

Heap гарантирует локальное parent/child отношение, а не глобальную сортировку. Произвольный search по value остаётся `O(n)`.

## Dynamic Programming

DP применим, когда:

- задача имеет overlapping subproblems;
- решение можно собрать из меньших subproblems.

Два основных стиля:

- memoization — top-down recursion + cache;
- tabulation — bottom-up table.

### Toy example: Fibonacci

Наивная recursion повторно вычисляет те же `F(k)` много раз → экспоненциальный рост вызовов.

Memoization хранит уже вычисленное и приводит работу к `O(n)` при соответствующей реализации.

Но не каждая recursion становится DP просто потому, что добавили array cache.

## Causal questions

1. Когда обычный BST деградирует до `O(n)` search?
2. Почему heap умеет быстро давать min, но не быстро искать arbitrary key?
3. Почему array representation heap не требует pointers между nodes?
4. Как overlapping subproblems превращают memoization в выигрыш?

## Упражнения

1. Для последовательности inserts нарисуй обычный BST и вычисли height.
2. Для array `[2, 5, 4, 9, 8, 7]` проверь min-heap invariant.
3. Вручную выполни один `extract-min` с swap/sift-down.
4. Сравни число повторных subproblems у naive Fibonacci и memoized version для маленького `n`.

Разбор: [`10-trees-heaps-dp.solution.md`](10-trees-heaps-dp.solution.md).

## Exit check

Для задачи «часто получать минимальный priority item» выбери heap, а не hash table/BST по привычке, и объясни operations contract.
