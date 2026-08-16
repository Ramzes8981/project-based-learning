# 9.1B — P, NP, NP-complete и инженерные границы алгоритмов

**Теория:** ~75 мин  
**Упражнение:** ~45 мин  
**С телефона:** да

← [`01-requirements-boundaries-state.md`](01-requirements-boundaries-state.md) · → [`02-protocol-idempotency-contracts.md`](02-protocol-idempotency-contracts.md)

## Цель

Понимать, почему некоторые performance-проблемы лечатся data structure/cache/parallelism, а некоторые имеют принципиально другой combinatorial growth.

## Decision problem

Complexity theory часто формулирует задачу как yes/no:

```text
«существует ли решение, удовлетворяющее условию?»
```

Это позволяет сравнивать классы задач независимо от UI/API.

## P

Грубо: decision problems, для которых существует deterministic algorithm с polynomial worst-case time относительно input size.

`O(n)`, `O(n log n)`, `O(n^3)` — polynomial. Это не означает «всегда быстро»: огромная степень/константа всё равно может быть непрактичной.

## NP

Decision problems, для которых **предложенное решение/certificate** можно проверить за polynomial time. NP не расшифровывается как «неполиномиальные».

Каждая P-задача входит в NP: если мы умеем быстро найти solution, его тем более можно быстро проверить.

## NP-hard / NP-complete

NP-hard problem не легче всех NP problems в смысле polynomial reductions; она не обязана сама быть decision problem/in NP.

NP-complete:

```text
problem ∈ NP
AND
каждая NP problem polynomially reducible to it
```

Если любой NP-complete problem получит polynomial exact algorithm, из reductions следует `P = NP`. На сегодня курс исходит из неизвестности равенства P/NP, а не утверждает доказанный ответ.

## Reduction intuition

Reduction — преобразовать instances A → B так, чтобы решение B отвечало на A, причём transformation polynomial. Это способ показать: «если B легко, то и A легко».

## Инженерное значение

Если exact optimization variant известна как NP-hard/NP-complete, варианты работы:

- ограничить input/domain;
- dynamic programming для special constraints;
- branch-and-bound;
- approximation с гарантией;
- heuristic/metaheuristic;
- accept exponential для маленького n;
- reformulate requirement.

**Не** значит: «ничего нельзя сделать».

## Systems example intuition

Не путай две ситуации:

```text
KV lookup медленный из-за O(n) linear scan -> Hash Table меняет algorithmic structure

combinatorial placement/scheduling optimization -> может не иметь known polynomial exact solution
```

Добавление threads не меняет complexity class, хотя способно уменьшить wall time в ограниченном диапазоне.

## Упражнение

Для ситуаций классифицируй response strategy, не complexity class формально:

1. exact brute-force search по 30 binary choices;
2. graph shortest path with nonnegative weights;
3. capacity planning с несколькими discrete constraints, где exact optimum необязателен;
4. Hash Table collision degeneration.

Для каждой спроси: улучшить DS/algorithm, parallelize, approximate, ограничить domain или измерить constants?

## Exit check

Почему «NP = очень медленно» и «NP-complete = невозможно решить» — обе плохие формулировки?
