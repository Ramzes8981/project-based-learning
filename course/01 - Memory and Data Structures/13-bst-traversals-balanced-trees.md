# 1.13 — Как дерево поддерживает упорядоченный поиск

**Теория:** ~75 мин  
**Практика:** ~90 мин  
**С телефона:** теория — да; практика — ПК

← [`12-recursion-recurrences.md`](12-recursion-recurrences.md) · → [`14-heap-priority-queue.md`](14-heap-priority-queue.md)

## Проблема

Sorted array даёт binary search, но insertion в середину может требовать сдвига многих elements. Хотим поддерживать order через links, чтобы insertion не всегда двигал contiguous suffix.

## Binary search tree

В **бинарном дереве поиска (binary search tree, BST)** каждый node имеет до двух children.

Один возможный duplicate policy:

```text
all keys in left subtree  < node.key
all keys in right subtree >= node.key
```

Policy должна быть явной и одинаковой для insert/find/traversal.

## Почему search может быть быстрым

На каждом node comparison выбирает только одну subtree. Если дерево имеет небольшую высоту `h`, поиск делает `O(h)` steps.

Но BST **не гарантирует** `h = O(log n)` сам по себе.

Sorted insertion sequence может дать:

```text
1
 \
  2
   \
    3
     \
      4
```

Тогда height `O(n)`, и search деградирует до linear.

## Traversals

Recursive structure естественно даёт traversals:

- inorder: left → node → right;
- preorder: node → left → right;
- postorder: left → right → node.

Для BST inorder produces keys in sorted order under the chosen duplicate policy.

Postorder удобно для destruction: сначала освободить children, затем owner node.

## Зачем balanced trees существуют

AVL/Red-Black trees добавляют invariants/rotations, чтобы height оставалась logarithmic. Core не требует реализовать полноценный balanced tree: важно понять **проблему, которую balancing решает**.

## Практика

Реализуй простую BST с fixed duplicate policy:

- insert;
- find;
- inorder traversal;
- destroy.

Сравни height для random-like и sorted insertion orders.

Разбор: [`13-bst-traversals-balanced-trees.solution.md`](13-bst-traversals-balanced-trees.solution.md).

## Exit check

Почему название «binary search tree» не гарантирует `O(log n)` search без дополнительного balance invariant?