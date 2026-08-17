# 1.8 — Как хранить элементы, не требуя одного большого непрерывного блока

**Теория:** ~60 мин  
**Практика:** ~70 мин  
**С телефона:** теория — да; практика — ПК

← [`07-dynamic-array.md`](07-dynamic-array.md) · → [`09-function-pointers-callbacks.md`](09-function-pointers-callbacks.md)

## Проблема

Vector хорош для random indexed access и cache locality, но рост иногда требует переместить весь block. Есть другой trade-off: выделять каждый element отдельно и связывать элементы pointers.

## Node и link

```c
typedef struct Node {
    int value;
    struct Node *next;
} Node;
```

Ментальная модель:

```text
head
 ↓
[value|next] → [value|next] → [value|NULL]
```

Это **связный список (linked list)**.

## Что мы выигрываем

При известном node insertion/removal не требует перемещать весь contiguous array.

## Что платим

- extra pointer per node;
- allocation overhead;
- чтобы найти element by index, обычно нужно пройти links от head;
- хуже locality;
- ownership/cleanup сложнее.

Структура данных — не «апгрейд» другой структуры. Это trade-off под операции/workload.

## Ownership map

Для singly linked list простая policy:

```text
list owns every reachable node
node owns no previous node
list_destroy walks nodes and frees each exactly once
```

При удалении сначала сохрани `next`, затем освободи current node; после `free(current)` читать `current->next` уже нельзя.

## Invariant preview

Всегда должно быть верно:

- `head == NULL` означает empty list;
- каждый reachable node принадлежит list ровно один раз;
- last node has `next == NULL`;
- cleanup не теряет remaining chain.

Слово **invariant** формально введём в 1.10; пока воспринимай как «условие, которое обязано оставаться истинным после каждой операции».

## Практика

Реализуй небольшой list с `push_front`, `find`, `remove_first`, `destroy`. Отдельно нарисуй ownership before/after removal.

Разбор: [`08-linked-structures.solution.md`](08-linked-structures.solution.md).

## Exit check

Почему linked list может упростить insertion, но ухудшить поиск `i`-го элемента и memory locality?