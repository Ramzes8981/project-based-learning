# Разбор упражнения 1.11

Ключевые invariants:

**Insertion sort:** перед итерацией `i` диапазон `[0, i)` отсортирован и содержит те же элементы, что исходный prefix.

**Merge:** два входных диапазона уже отсортированы; output после каждого шага содержит минимальные ещё не слитые элементы в правильном порядке.

При самостоятельной реализации проверь `n=0`, `n=1`, already sorted, reverse sorted, duplicates и значения `INT_MIN/INT_MAX`. Comparator на основе relational operators не имеет subtraction-overflow.
