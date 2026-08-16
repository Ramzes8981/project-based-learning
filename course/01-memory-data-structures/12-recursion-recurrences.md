# 1.12 — Recursion, call stack и recurrence intuition

**Теория:** ~70 мин  
**Упражнение:** ~60 мин  
**С телефона:** да

← [`11-sorting.md`](11-sorting.md) · → [`13-bst-traversals-balanced-trees.md`](13-bst-traversals-balanced-trees.md)

## Цель

Понимать рекурсию как обычные function calls со своими состояниями, уметь определить base case, progress measure и оценить depth/work.

## Три обязательных вопроса

Для recursive function:

1. **Base case:** когда вызовы прекращаются?
2. **Progress:** почему каждый recursive step приближает к base case?
3. **State:** какие данные нужны каждому frame после возврата дочернего вызова?

## Call stack

Каждый незавершённый вызов хранит свой execution state. Поэтому depth влияет на stack usage.

```text
f(4)
 └─ f(3)
     └─ f(2)
         └─ f(1)
```

`O(n)` recursive depth может быть опасен при большом `n`, даже если total work тоже `O(n)`.

## Recurrence intuition

Merge sort work можно описать приблизительно:

```text
T(n) = 2*T(n/2) + O(n)
```

На каждом уровне дерева суммарное merge-work порядка `n`, уровней порядка `log n` → `O(n log n)`.

Не требуется формально решать любые recurrence equations; цель — уметь нарисовать recursion tree и посчитать уровни/работу.

## Exponential recursion

Наивный Fibonacci:

```text
fib(n) -> fib(n-1) + fib(n-2)
```

повторно вычисляет одни и те же subproblems. Это подводка к dynamic programming.

## Recursion vs iteration

Recursion удобна, когда структура задачи сама рекурсивна: tree traversal, divide-and-conquer, parser. Iteration часто лучше контролирует stack и состояние для линейной задачи.

## Упражнение

1. Реализуй recursive sum для маленького массива, но явно ограничь размер теста и сравни с iterative version.
2. Нарисуй frames для `sum(a, 3)`.
3. Для merge sort нарисуй recursion tree для `n=8` и оцени число уровней.

Разбор: [`12-recursion-recurrences.solution.md`](12-recursion-recurrences.solution.md).

## Causal questions

1. Почему наличие base case не гарантирует termination?
2. Как `n -> n-1` доказывает progress при `n >= 0`?
3. Почему recursive traversal дерева естественнее recursive traversal гигантского линейного массива?
4. Что именно повторяет naive Fibonacci?

## Exit check

Для любой рекурсивной функции сначала назови base case, progress measure и maximum expected depth.
