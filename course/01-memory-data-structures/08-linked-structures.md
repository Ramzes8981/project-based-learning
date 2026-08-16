# 1.8 — Linked list, stack и queue

**Теория:** ~50 мин  
**Упражнение:** ~60 мин  
**С телефона:** теория — да

← [`07-dynamic-array.md`](07-dynamic-array.md) · → [`09-function-pointers-callbacks.md`](09-function-pointers-callbacks.md)

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

Его можно реализовать dynamic array или linked list. ADT описывает behavior, data structure — representation.

## Queue ADT

Queue — FIFO:

```text
enqueue
dequeue
```

В linked representation полезно хранить head+tail для `O(1)` append. В array representation production queue часто использует ring buffer вместо постоянного shift.

## Causal questions

1. Почему linked list не даёт быстрый random access?
2. Почему `O(1)` insert не означает «всегда быстрее vector»?
3. Кто должен free removed node?
4. Почему array queue с постоянным shift — плохая идея?

## Упражнение

Реализуй маленький integer stack **одним** способом на выбор: vector-backed или singly-linked.

Требования: push/pop/peek, empty handling, deterministic cleanup, ASan clean. После реализации письменно опиши второй вариант и trade-offs.

Разбор архитектуры: [`08-linked-structures.solution.md`](08-linked-structures.solution.md).

## Exit check

Для workload «миллионы sequential scans + редкие appends» выбери vector или linked list через layout + operations, не только Big O.
