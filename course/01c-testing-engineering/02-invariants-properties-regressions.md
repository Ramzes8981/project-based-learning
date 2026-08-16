# 1C.2 — Invariants, properties и regression tests

**Теория:** ~65 мин  
**Упражнение:** ~55 мин  
**С телефона:** да

← [`01-test-levels-oracles.md`](01-test-levels-oracles.md) · → [`03-testability-dependencies-doubles.md`](03-testability-dependencies-doubles.md)

## Цель

Проверять не только конкретные examples, но и общие свойства структуры.

## Example-based test

```text
push 10
get(0) == 10
```

Полезен и понятен, но охватывает одну точку input space.

## Invariant

Утверждение, которое обязано быть истинно для каждого valid state.

Vector:

```text
size <= capacity
if capacity > 0, backing storage соответствует capacity
indices [0,size) initialized по contract
```

Heap:

```text
parent <= children
```

Allocator:

```text
blocks do not overlap
```

Hash Table:

```text
каждый active key обнаруживается своей probe policy
active/tombstone counters согласованы с buckets
```

Test-only invariant checker очень полезен, даже если production API его не экспортирует.

## Property thinking

Property — отношение между действиями/результатами для множества inputs:

```text
get(set(store,k,v), k) == v
sort output is ordered AND is permutation of input
push then pop on heap preserves prior heap contents according to priority
```

Property testing не обязательно требует специальной library: сначала научись формулировать property и генерировать много inputs обычным loop/script.

## Regression test

После найденного bug:

```text
minimal reproducer -> test fails -> fix -> test passes -> keep forever
```

Regression test превращает debugging knowledge в автоматизированную память проекта.

## Metamorphic relation

Когда exact output трудно заранее посчитать, можно проверить relation. Например сортировка twice должна дать тот же результат; добавление независимого key не должно менять value другого key.

## Упражнение

Для одной своей структуры сформулируй:

- 4 invariants;
- 3 properties;
- 1 реальный/искусственный bug reproducer как regression.

Реализуй минимум один invariant checker, вызываемый в tests.

Разбор: [`02-invariants-properties-regressions.solution.md`](02-invariants-properties-regressions.solution.md).

## Exit check

Чем property `sorted(output)` слабее полной проверки сортировки? Ответ: нужно ещё доказать, что элементы не потерялись/не появились — например permutation/multiset property.
