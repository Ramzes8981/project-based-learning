# Optional 1A — Когда повторяющиеся подзадачи стоит запоминать

**Статус:** optional; не блокирует core systems path.  
**Теория:** ~70 мин · **Практика:** ~70 мин · **С телефона:** да

← [`21-module-checkpoint.md`](21-module-checkpoint.md) · optional next → [`23-string-searching.md`](23-string-searching.md)

Этот урок даёт дополнительную algorithm depth после обязательного gate. Hash Table/Unix/OS/networking от него не зависят.

## Проблема

Некоторые recursive formulations вычисляют один и тот же subproblem много раз. Если subproblem result зависит только от небольшого state, его можно сохранить и reused.

Это семейство техник называют **динамическим программированием (dynamic programming, DP)**.

## Две идеи

- **memoization**: recursive/top-down + cache computed states;
- **tabulation**: iterative/bottom-up table in dependency order.

DP нужен не потому, что «задача сложная», а когда есть overlapping subproblems + полезная state decomposition.

## Пример

Naive Fibonacci — учебный пример повторной работы, но не шаблон всех DP-задач. Более инженерный пример: минимальная стоимость пройти sequence states с локальными transitions.

## Checklist

Перед DP спроси:

1. Что является state?
2. Какие states нужны для вычисления текущего?
3. Есть ли overlapping work?
4. Какова table size?
5. Нужен ли весь table или только previous layer?

## Практика

Возьми небольшую shortest-cost-on-line задачу, сначала запиши recurrence, затем memoized и bottom-up versions. Сравни число вычисленных states.

Разбор: [`22-dynamic-programming.solution.md`](22-dynamic-programming.solution.md).