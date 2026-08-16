# Module 1 — Checkpoint

**Время:** ~2–4 часа без доработки milestone  
**С телефона:** вопросы — да; review/build — ПК

← [`20-resize-rehash.md`](20-resize-rehash.md) · ↑ [`README`](README.md)

## A. Memory reasoning

Без поиска объясни:

1. array object vs pointer;
2. lifetime vs numerical address;
3. owner vs borrow;
4. `malloc` failure path;
5. почему `realloc` нужен temporary pointer;
6. use-after-free/double-free/leak;
7. что sanitizers доказывают и чего не доказывают;
8. pointer invalidation после Vector growth.

## B. Algorithms/DS

Объясни и сравни:

- linear vs binary search;
- insertion/merge/quick/heap sort trade-offs;
- recursion depth;
- BST height/degeneration;
- heap/Priority Queue;
- DP state/transition;
- Trie vs Hash Table;
- expected vs worst-case hashing.

## C. Situational checks

### 1
`size_t i = 0; parent = (i - 1) / 2;` — что происходит и каков precondition?

### 2
Callback API сохраняет `void *ctx`, который указывает на local caller variable. Что нужно знать до return?

### 3
Hash insert нашёл tombstone и сразу записал туда key, не проверив remainder chain. Какой bug возможен?

### 4
Resize сначала меняет `table->capacity`, потом allocation падает. Почему table может стать invalid?

### 5
BST содержит million keys и имеет height почти million. Что это говорит о complexity и recursion risk?

## D. Vector milestone

Проверь [`project/vector/ACCEPTANCE.md`](project/vector/ACCEPTANCE.md), свой README, `make test` и sanitizer run.

## E. Hash Table milestone

Проверь [`project/hash-table/ACCEPTANCE.md`](project/hash-table/ACCEPTANCE.md): ownership, collisions, tombstones, resize, failure paths, metrics, tests.

Обязательно добавь debugging story и transfer feature в project README.

## Gate

Module 1 закрыт, когда ты можешь не только написать структуры, но и объяснить:

```text
representation
+ invariants
+ ownership
+ complexity
+ failure behavior
+ tests
+ measurement
```

После этого Rust Bridge будет полезен: borrow checker станет ответом на проблемы, которые уже пришлось контролировать вручную в C.
