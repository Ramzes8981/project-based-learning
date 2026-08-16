# 1.18 — Как представлять связи и искать путь между объектами

**Теория:** ~75 мин  
**Практика:** ~80 мин  
**С телефона:** теория — да; практика — ПК

← [`20-resize-rehash.md`](20-resize-rehash.md) · → [`21-module-checkpoint.md`](21-module-checkpoint.md)

## Проблема

Не все данные — sequence или key→value. Иногда главное — связи:

- host connected to networks;
- package depends on packages;
- process waits for resources;
- router links locations.

Нужна модель «объекты + связи между ними».

## Graph

**Граф (graph)** состоит из vertices/nodes и edges.

```text
A ─ B
│   │
C ─ D
```

Edges могут быть directed/undirected и иметь weight.

## Representation

### Adjacency list

Для каждого vertex храним neighbors. Space примерно `O(V + E)` для sparse graph.

### Adjacency matrix

`V × V` grid, где cell говорит о связи. Быстрая direct edge query, но space `O(V²)`.

Выбор representation зависит от density и операций.

## BFS: кратчайшее число шагов без weights

**Breadth-first search (BFS)** исследует graph слоями distance from start. Queue хранит frontier.

Invariant intuition:

> когда vertex впервые извлечён/отмечен по стандартной BFS policy, найдено минимальное число unweighted edges от start.

Нужен `visited`, иначе cycle может вызвать бесконечный обход.

## DFS

**Depth-first search (DFS)** идёт глубже по одной ветке и возвращается назад. Полезен для reachability, components, cycle/topology variants. Реализуется recursion или explicit stack.

## Dijkstra: positive/nonnegative weights

Если edges имеют nonnegative cost, **Dijkstra** repeatedly выбирает vertex с smallest known tentative distance — здесь естественно используется priority queue/min-heap из 1.14.

Negative weights ломают greedy guarantee; тогда нужен другой algorithm.

## Systems connection

Этот урок расположен здесь, а не внутри Networking: graph algorithms — самостоятельный data-structure dependency. Позже routing lesson сможет ссылаться на уже известную graph mental model, не преподавая BFS/Dijkstra посреди socket API.

## Практика

На небольшом adjacency-list graph:

1. BFS reachability + shortest edge count;
2. DFS traversal;
3. Dijkstra for nonnegative integer weights;
4. tests with disconnected vertex and cycle.

## Exit check

Почему BFS и Dijkstra решают разные shortest-path contracts, и какое prerequisite Dijkstra накладывает на edge weights?