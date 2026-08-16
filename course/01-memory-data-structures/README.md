# Module 1 — Как программа находит данные в памяти и выбирает структуру для них

**Core:** ~55–75 часов.  
**Optional advanced algorithms:** ~20–30 часов.  
**Prerequisite:** Module 0.

Старый модуль смешивал memory model, safety и почти весь академический DS&A в один 85–110-часовой блок. Теперь здесь две явные фазы с отдельными gates.

## Phase A — C memory safety

Проблема проекта Module 0: фиксированное место закончилось. Прежде чем просить больше памяти, нужно понять, **что значит сослаться на существующий объект и когда такая ссылка перестаёт быть допустимой**.

1. [`01-addresses-pointers.md`](01-addresses-pointers.md) — **Как функция может изменить уже существующее значение**.
2. [`02-arrays-pointer-arithmetic.md`](02-arrays-pointer-arithmetic.md) — **Почему массив и указатель связаны, но не являются одним и тем же**.
3. [`03-const-types-bits.md`](03-const-types-bits.md) — **Как безопасно считать размеры до работы с памятью**.
4. [`03b-text-bytes-utf8.md`](03b-text-bytes-utf8.md) — **Почему текст и bytes — не одно и то же**.
5. [`04-lifetime-ownership.md`](04-lifetime-ownership.md) — **Почему правильный адрес позже может стать недействительным**.
6. [`05-heap-allocation.md`](05-heap-allocation.md) — **Как программе попросить больше памяти и не потерять её**.
7. [`06-undefined-behavior-debugging.md`](06-undefined-behavior-debugging.md) — **Почему некоторые ошибки C нельзя понимать как обычный runtime exception**.
8. [`07-dynamic-array.md`](07-dynamic-array.md) — **Как сделать массив, который умеет расти**.
9. [`08-linked-structures.md`](08-linked-structures.md) — **Как хранить элементы, не требуя одного большого непрерывного блока**.
10. [`09-function-pointers-callbacks.md`](09-function-pointers-callbacks.md) — **Как передать программе само действие**.

**Project gate A:** [`project/vector/`](project/vector/README.md).

## Phase B — core algorithms & data structures

Теперь появляется другая проблема: корректная программа может быть слишком медленной или неудобной для конкретной операции.

11. [`10-complexity-invariants-binary-search.md`](10-complexity-invariants-binary-search.md) — **Как сравнивать способы решения и не ломать главный invariant**.
12. [`11-sorting.md`](11-sorting.md) — **Когда выгодно сначала упорядочить данные**.
13. [`12-recursion-recurrences.md`](12-recursion-recurrences.md) — **Когда задача естественно содержит уменьшенную копию самой себя**.
14. [`13-bst-traversals-balanced-trees.md`](13-bst-traversals-balanced-trees.md) — **Как дерево поддерживает упорядоченный поиск**.
15. [`14-heap-priority-queue.md`](14-heap-priority-queue.md) — **Как быстро получать самый приоритетный элемент**.
16. [`19-hashing-collisions.md`](19-hashing-collisions.md) — **Как находить запись по ключу без полного просмотра массива**.
17. [`20-resize-rehash.md`](20-resize-rehash.md) — **Почему hash table нельзя просто увеличить копированием slots**.
18. [`20b-graphs-paths.md`](20b-graphs-paths.md) — **Как представлять связи и искать путь между объектами**.
19. [`21-module-checkpoint.md`](21-module-checkpoint.md) — cumulative checkpoint.

**Project gate B:** [`project/hash-table/`](project/hash-table/README.md).

## Optional advanced algorithms

Эти файлы остаются полноценными материалами, но не блокируют core systems path:

- [`15-dynamic-programming.md`](15-dynamic-programming.md) — dynamic programming;
- [`16-string-searching.md`](16-string-searching.md) — KMP/Rabin–Karp;
- [`17-trie.md`](17-trie.md) — Trie;
- [`18-probability-for-hashing.md`](18-probability-for-hashing.md) — более формальная probability intuition.

Весь минимум вероятностной интуиции, нужный для Hash Table, теперь содержится непосредственно в уроке 1.16 (`19-hashing-collisions.md`).