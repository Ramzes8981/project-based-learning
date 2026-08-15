# Module 1 — Checkpoint

**Время:** 2–4 часа review + milestone evidence  
**С телефона:** conceptual часть — да

← [`12-resize-rehash.md`](12-resize-rehash.md) · ↑ [`README`](README.md)

## Explain

Без кода объясни:

1. pointer value vs pointed object;
2. array vs pointer;
3. one-past pointer;
4. lifetime и dangling pointer;
5. ownership vs borrow как C convention;
6. `malloc/free/realloc` failure semantics;
7. use-after-free vs leak vs double free;
8. size vs capacity;
9. amortized vector push;
10. vector vs linked list trade-offs;
11. `O/Ω/Θ`;
12. binary search invariant;
13. heap vs BST vs hash table;
14. collision/load factor;
15. tombstone;
16. resize/rehash.

## Scenario questions

### 1. `realloc`

Почему `p = realloc(p, bigger)` опаснее temporary-pointer pattern?

### 2. Borrow

Функция возвращает `const char *` внутрь hash-table entry. Затем caller вставляет новые entries и table resizes. Может ли старый pointer остаться валидным? Ответ зависит от representation — опиши контракт.

### 3. Complexity

Почему hash lookup expected `O(1)` не отменяет worst-case `O(n)`?

### 4. Memory layout

Почему contiguous vector может обгонять linked list даже там, где asymptotic order одной операции одинаков?

### 5. Delete

Почему превращение deleted bucket в EMPTY ломает linear probing search?

## Mini-milestone — Vector

Проверь [`project/vector/ACCEPTANCE.md`](project/vector/ACCEPTANCE.md).

## Core milestone — Hash Table

Проверь [`project/hash-table/ACCEPTANCE.md`](project/hash-table/ACCEPTANCE.md).

Обязательно:

- no known sanitizer errors;
- ownership documented;
- insert/update/get/delete;
- collisions;
- tombstones;
- resize/rehash;
- allocation failures have defined behavior;
- transfer feature;
- tests + instrumentation;
- debugging story.

## Exit gate

Module 1 закрыт, если pointers/manual memory уже не являются «синтаксисом со звёздочками», а образуют модель:

```text
object
→ address
→ pointer aliases
→ lifetime
→ ownership
→ allocation/cleanup
→ data layout
→ algorithmic cost
```

Следующий обязательный блок — **Rust Systems Bridge**. Его цель не забыть C, а увидеть, как Rust заставляет компилятор проверять часть ownership/lifetime contracts, которые здесь приходилось удерживать вручную.
