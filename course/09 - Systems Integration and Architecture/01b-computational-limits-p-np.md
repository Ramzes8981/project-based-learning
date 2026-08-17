# Optional — Когда проблема медленная не из-за плохой реализации

**Статус:** optional CS deepening · **Теория:** ~60–75 мин · **С телефона:** да

← [`README`](README.md)

Этот материал не нужен для выполнения capstone.

## Проблема

Иногда программу можно ускорить лучшей структурой данных. Иногда точный поиск решения растёт комбинаторно, и «добавить threads» не меняет главную природу задачи.

## Минимальная модель

В complexity theory удобно рассматривать задачи с ответом yes/no — **decision problems**.

**P**: задачи, для которых известен deterministic polynomial-time algorithm.

**NP**: задачи, где предложенный certificate/solution можно проверить за polynomial time.

`P ⊆ NP`.

**NP-complete** problem находится в NP и не легче остальных NP problems в смысле polynomial reductions.

Равенство `P = NP` не доказано и не опровергнуто.

## Зачем инженеру

Если exact optimization problem имеет известную NP-hard форму, реальные стратегии могут быть такими:

- ограничить input/domain;
- использовать special-case dynamic programming;
- approximation;
- heuristic;
- exact exponential search только для маленького n;
- изменить requirement.

Это **не** означает «задачу невозможно решить».

## Контраст

```text
linear scan в KV → смена data structure способна изменить O(n) на ожидаемый O(1)

combinatorial placement optimization → ещё один CPU не превращает exponential growth в polynomial
```

## Exit check

Почему утверждения «NP означает медленно» и «NP-complete невозможно решить» оба некорректны?