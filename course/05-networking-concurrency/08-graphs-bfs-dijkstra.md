# 5.8 — Graphs, BFS/DFS и Dijkstra

**Теория:** ~75 мин  
**Упражнения:** ~75 мин  
**С телефона:** да

← [`07-poll-event-loop.md`](07-poll-event-loop.md) · → [`09-load-testing-metrics.md`](09-load-testing-metrics.md)

## Цель

Закрыть обязательный graph algorithms checkpoint через network-topology model.

## Graph

Graph:

```text
G = (V, E)
```

Vertices — nodes; edges — connections/relations.

Может быть directed/undirected, weighted/unweighted.

## Representations

Adjacency matrix:

- `O(V^2)` memory;
- fast edge lookup;
- хороша для dense/small graphs.

Adjacency list:

- memory `O(V + E)`;
- естественна для sparse network graphs.

## BFS

Breadth-first search использует queue и исследует layers по числу edges.

На unweighted graph shortest path по edge count находится BFS.

Complexity adjacency-list implementation:

```text
O(V + E)
```

## DFS

Depth-first search через stack/recursion. Полезен для reachability, components, topological/cycle-related algorithms depending graph type.

Также `O(V+E)` при proper visited tracking.

## Dijkstra

Для non-negative edge weights ищет shortest distances.

С adjacency list + binary heap priority queue типичный complexity order:

```text
O((V + E) log V)
```

в common implementation.

Если есть negative edge weights, обычный Dijkstra correctness не гарантирует.

## Relaxation

Для edge `u -> v` weight `w`:

```text
if dist[u] + w < dist[v]:
    dist[v] = dist[u] + w
```

Priority queue выбирает next smallest tentative distance.

## Network analogy

Vertices = routers/sites, edge weight = latency/cost. Это **учебная модель**, а не реализация OSPF/BGP.

Real routing protocols имеют distributed state, policy, convergence и failure complexities.

## Exercises

1. Создай 8-node topology adjacency list.
2. BFS reachability/path по hop count.
3. DFS order/component.
4. Добавь non-negative weights и вручную проведи Dijkstra.
5. Добавь negative edge и объясни, почему assumptions нарушены.

Разбор: [`08-graphs-bfs-dijkstra.solution.md`](08-graphs-bfs-dijkstra.solution.md).

## Exit check

Почему BFS может давать shortest path в unweighted graph, но неверен для arbitrary weighted latency?
