# 1.19 — Checkpoint: memory safety + data-structure trade-offs

**Время:** ~3–5 часов  
**С телефона:** explain/review — да; projects — ПК

← [`20b-graphs-paths.md`](20b-graphs-paths.md) · ↑ [`README`](README.md)

## Gate A — memory model

Без кода объясни:

1. object vs address vs pointer;
2. array-to-pointer conversion и потерю length на function boundary;
3. one-past rule;
4. почему `p != NULL` не доказывает validity;
5. lifetime и dangling pointer;
6. C ownership convention;
7. checked `size_t` arithmetic;
8. `malloc/realloc/free` ownership transitions;
9. почему successful `realloc` инвалидирует borrowed element pointers;
10. UB vs ordinary runtime error;
11. byte sequence vs C string vs UTF-8 text.

Vector должен проходить acceptance/sanitizers.

## Gate B — algorithmic thinking

Для Vector, linked list, sorted array, BST, heap, hash table назови:

```text
главные операции
инвариант
expected/worst cost where meaningful
memory/layout trade-off
failure/edge cases
systems use case
```

Hash Table должен проходить collision/delete/resize/failure tests.

## Graph transfer

Объясни, почему routing/dependency/deadlock relationships естественно моделируются graph, и когда BFS vs Dijkstra appropriate.

## Debugging story

Минимум одна история должна содержать memory-safety evidence (sanitizer/precise invariant failure), а не только «посмотрел на код и исправил».

## Optional does not block

DP/KMP/Trie/probability deep dive не входят в core gate. Их можно пройти сейчас или позже по возникновению задачи.

## Exit check

Ты готов к Rust bridge, если можешь сформулировать C ownership/lifetime contracts настолько точно, чтобы затем увидеть, **какие из них Rust заставит кодировать в типах/borrows**.