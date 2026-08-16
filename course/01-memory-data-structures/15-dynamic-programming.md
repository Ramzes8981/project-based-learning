# 1.15 — Dynamic Programming: state, transition, memoization

**Теория:** ~85 мин  
**Упражнение:** ~90 мин  
**С телефона:** да

← [`14-heap-priority-queue.md`](14-heap-priority-queue.md) · → [`16-string-searching.md`](16-string-searching.md)

## Цель

Уметь распознать повторяющиеся subproblems и превратить экспоненциальную recursion в вычисление каждого состояния ограниченное число раз.

## DP не равно «таблица»

Сначала определить:

1. **State:** какая минимальная информация описывает subproblem?
2. **Transition:** из каких меньших states получаем текущий?
3. **Base cases:** что известно без рекурсии?
4. **Order:** в каком порядке states становятся доступными?

Memoization и tabulation — способы вычисления, не сама идея.

## Example: climbing stairs

Если можно шагать на 1 или 2:

```text
ways(n) = ways(n-1) + ways(n-2)
```

Naive recursion повторяет states. Memoization хранит уже вычисленное. Bottom-up tabulation идёт от base cases вверх.

## Complexity

Если states `n`, а transition каждого `O(1)`, total `O(n)`. Memory может быть `O(n)` или `O(1)`, если transition зависит только от последних двух states.

## Example: coin change intuition

State может быть `best amount` или пара `(coin_index, amount)` — выбор state определяет correctness и complexity. Слишком мало state теряет информацию; слишком много делает алгоритм дорогим.

## Упражнение

Реши одну задачу двумя способами:

**minimum cost to reach position n**, где из `i` можно перейти в `i+1`/`i+2`, а каждая позиция имеет cost.

Сначала запиши recurrence и base cases **без кода**, затем memoized или bottom-up C implementation. Добавь tests для `n=0/1/2`, нескольких cost patterns.

Разбор: [`15-dynamic-programming.solution.md`](15-dynamic-programming.solution.md).

## Anti-patterns

- начинать с multidimensional array без определения state;
- путать greedy choice и DP;
- забыть invalid/unreachable states;
- arithmetic overflow в count-style задачах;
- memo table с sentinel, который может быть валидным результатом.

## Exit check

Объясни DP-задачу формулой `state + transition + base cases + computation order`, не словом «табличка».
