# Разбор 1.10

Для min-heap каждый parent должен быть `<=` children. Array representation экономит отдельные next/left/right pointers, потому что topology кодируется индексами.

После `extract-min` обычно:

1. root сохраняется как result;
2. последний element переносится в root;
3. logical size уменьшается;
4. root sift-down меняется с меньшим child до восстановления invariant.

Обычный BST становится chain, например, если вставлять уже sorted keys `1,2,3,4,5` без balancing.

У Fibonacci naive recursion повторяет `F(k)` во многих ветках. Memoization вычисляет каждое состояние примерно один раз.
