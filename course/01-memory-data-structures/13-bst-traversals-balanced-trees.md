# 1.13 — Binary Search Tree, traversals и зачем balancing

**Теория:** ~90 мин  
**Упражнение:** ~90 мин  
**С телефона:** теория — да

← [`12-recursion-recurrences.md`](12-recursion-recurrences.md) · → [`14-heap-priority-queue.md`](14-heap-priority-queue.md)

## Цель

Построить mental model дерева как связанной структуры, реализовать BST search/insert/traversal и понять, почему `O(log n)` не гарантируется обычным BST.

## Node

```c
struct Node {
    int key;
    struct Node *left;
    struct Node *right;
};
```

Ownership policy надо задать отдельно: обычно tree владеет всеми nodes и уничтожает их один раз.

## BST invariant

Для выбранной duplicate policy:

```text
all keys in left subtree < node key
all keys in right subtree > node key
```

или иной явно документированный вариант с duplicates.

Search идёт только в одну subtree согласно сравнению.

## Height определяет cost

Cost search/insert порядка `O(h)`, где `h` — height.

Balanced-ish tree: `h ~ log n`.

Плохой порядок вставки:

```text
1, 2, 3, 4, 5
```

может дать chain height `n`, и операции становятся `O(n)`.

## Traversals

**Preorder:** node → left → right.  
**Inorder:** left → node → right. Для BST даёт sorted order.  
**Postorder:** left → right → node. Удобен для destroy: сначала children, потом owner node.  
**Level-order/BFS:** по уровням, требует queue.

Это связывает trees с ранее реализованными stack/queue.

## Delete concept

Три случая:

- leaf;
- один child;
- два children: заменить логически successor/predecessor и восстановить invariant.

Полная реализация delete — transfer/stretch; search/insert/traversal обязательны.

## Balanced trees

AVL и Red-Black trees добавляют metadata/invariants и rotations, чтобы ограничивать height. Не нужно сейчас реализовывать оба. Нужно понимать trade-off:

```text
больше complexity при mutation
↔
предсказуемая logarithmic height
```

Позже B-tree применит родственную идею balancing уже для page-oriented storage.

## Упражнение

Реализуй BST insert/search и минимум inorder + postorder traversal.

Tests:

- empty;
- one node;
- left/right branches;
- sorted insertion degenerates;
- documented duplicate policy;
- destroy without leaks под sanitizer.

Разбор: [`13-bst-traversals-balanced-trees.solution.md`](13-bst-traversals-balanced-trees.solution.md).

## Exit check

Объясни, почему `BST lookup = O(log n)` — неверное утверждение без дополнительного invariant о высоте.
