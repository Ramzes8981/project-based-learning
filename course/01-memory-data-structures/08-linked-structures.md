# 1.8 — Linked list, stack и queue

**Теория:** ~50 мин  
**Упражнение:** ~60 мин  
**С телефона:** теория — да

← [`07-dynamic-array.md`](07-dynamic-array.md) · → [`09-complexity-search-sort-recursion.md`](09-complexity-search-sort-recursion.md)

## Цель

Увидеть, как одна и та же abstract operation может иметь разные memory layouts и реальные costs.

## Singly linked list

Node:

```text
[value | next] -> [value | next] -> [value | NULL]
```

Каждый node обычно отдельный object/allocation. List хранит pointer на head.

## Ownership

Для owning linked list естественный контракт:

- list владеет nodes;
- removing node освобождает его;
- destroying list освобождает все nodes;
- external pointer на removed node становится invalid.

Если list хранит pointers на external payloads, ownership payloads нужно определить отдельно.

## Operations

При наличии head pointer:

- insert at front: `O(1)`;
- remove front: `O(1)`;
- search by value: `O(n)`;
- random index access: `O(n)`.

Dynamic array:

- indexed access: `O(1)`;
- append amortized `O(1)`;
- insert/remove middle требуют shifts `O(n)`.

## Но complexity — не вся история

Linked nodes часто разбросаны по heap. Это ухудшает spatial locality и добавляет pointer overhead.

Поэтому linked list с «красивым O(1) insert» может проигрывать contiguous vector на реальном workload.

Эту тему измерим глубже в performance module.

## Stack ADT

Stack — LIFO:

```text
push
pop
peek
```

Его можно реализовать:

- dynamic array;
- linked list.

ADT описывает поведение, data structure — конкретное representation.

## Queue ADT

Queue — FIFO:

```text
enqueue
 dequeue
```

В linked representation полезно хранить и head, и tail, чтобы append был `O(1)`.

В array representation production queue часто использует ring buffer вместо постоянного сдвига элементов.

## Causal questions

1. Почему linked list не даёт быстрый random access?
2. Почему `O(1)` insert не означает «всегда быстрее vector»?
3. Кто должен free removed node?
4. Почему array queue с постоянным shift — плохая идея?

## Упражнение

Реализуй маленький integer stack **одним** способом на выбор: vector-backed или singly-linked.

Требования:

- push/pop/peek;
- empty handling;
- deterministic cleanup;
- ASan clean;
- не превращать это в portfolio project.

После реализации письменно опиши, как выглядел бы второй вариант и какие trade-offs изменились бы.

Разбор архитектуры: [`08-linked-structures.solution.md`](08-linked-structures.solution.md).

## Exit check

Для workload «миллионы sequential scans + редкие appends» выбери между vector и linked list и объясни решение через layout + operations, а не только Big O.
