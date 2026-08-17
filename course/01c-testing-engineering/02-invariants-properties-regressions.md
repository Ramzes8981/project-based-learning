# 1C.2 — Как проверять правило для целого класса входов

**Теория:** ~60 мин · **Практика:** ~70 мин · **С телефона:** теория — да

← [`01-test-levels-oracles.md`](01-test-levels-oracles.md) · → [`03-testability-dependencies-doubles.md`](03-testability-dependencies-doubles.md)

## Проблема

Несколько hand-picked examples не покрывают пространство states. Но у структуры часто есть правило, которое должно быть истинно **после любой допустимой последовательности операций**.

У нас уже есть слово — invariant.

## Property

**Property-based thinking** формулирует общее свойство и генерирует/перебирает много inputs/sequences.

Примеры:

```text
Vector: len <= capacity always
sort: output sorted AND multiset unchanged
Hash Table: put(k,v) then get(k) == v unless later delete/update
encode/decode: decode(encode(x)) == x for valid x
```

Это сильнее списка примеров, но property тоже может быть неполной. `sorted(output)` alone не замечает, что sort потерял половину values.

## Regression test

После найденного bug сохрани минимальный input/sequence, который его воспроизводит. Такой test называют **регрессионным (regression test)**: future change не должен вернуть старый failure.

```text
bug
→ minimize reproducer
→ fix root cause
→ save reproducer as test
```

## Metamorphic relation

Иногда точный expected output дорог, но известна связь между outputs. Например sorting twice should equal sorting once. Это supplementary oracle, не replacement всех semantics.

## Практика

Для Hash Table:

1. напиши 3 invariants/properties;
2. сгенерируй deterministic sequence из put/update/delete/get using fixed seed or explicit list;
3. сравни behavior с простой reference model (например маленький array map);
4. сохрани один искусственно найденный edge case как regression.

Разбор: [`02-invariants-properties-regressions.solution.md`](02-invariants-properties-regressions.solution.md).

## Exit check

Почему property `lookup returns something after insert` слабее `lookup returns the latest value for this exact key after arbitrary collision/delete sequence`?