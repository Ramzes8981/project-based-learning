# 1.12 — Когда задача естественно содержит уменьшенную копию самой себя

**Теория:** ~60 мин  
**Практика:** ~60 мин  
**С телефона:** теория — да; практика — ПК

← [`11-sorting.md`](11-sorting.md) · → [`13-bst-traversals-balanced-trees.md`](13-bst-traversals-balanced-trees.md)

## Проблема

Некоторые структуры сами состоят из структур того же вида: дерево содержит поддеревья, directory содержит nested directories, divide-and-conquer делит задачу на меньшие версии.

Повторять вручную неизвестное число уровней неудобно.

## Recursion

Когда function решает задачу через вызов самой себя для меньшего input, это **рекурсия (recursion)**.

Нужны две вещи:

```text
base case      — где больше не рекурсируем
progress rule  — почему каждый call приближает к base case
```

Без progress recursion может не завершиться.

## Call stack cost

Каждый незавершённый recursive call добавляет состояние вызова. Очень глубокая recursion может исчерпать доступный call stack.

Поэтому recursion — не «всегда красивее loop». Нужно оценить maximum depth.

## Recurrence intuition

Для merge sort грубая cost model:

```text
T(n) = 2*T(n/2) + O(n)
```

Два subproblems половинного размера + linear merge. На каждом уровне суммарная merge-work порядка `n`, уровней порядка `log n`, поэтому возникает `O(n log n)`.

Не требуется формальный Master Theorem как gate; важно видеть связь structure → work.

## Практика

1. Напиши recursive sum для маленького array range `[lo, hi)`.
2. Назови base case и progress rule.
3. Перепиши его loop-ом и сравни state/cost.
4. Нарисуй call tree для `n=4` divide-and-conquer example.

Разбор: [`12-recursion-recurrences.solution.md`](12-recursion-recurrences.solution.md).

## Exit check

Для любой recursive function ты можешь показать, почему она terminates и какова worst-case depth.