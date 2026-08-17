# 1C.4 — Почему неправильный input нужно генерировать намеренно

**Теория:** ~65 мин · **Практика:** ~80 мин · **С телефона:** теория — да

← [`03-testability-dependencies-doubles.md`](03-testability-dependencies-doubles.md) · → [`05-module-checkpoint.md`](05-module-checkpoint.md)

## Проблема

Happy-path tests доказывают только happy path. Systems/security code особенно часто ломается на длинах, malformed states и sequences, которые «нормальный пользователь не введёт».

## Negative testing

Мы намеренно подаём invalid/boundary input и проверяем controlled failure:

- zero/maximum lengths;
- one beyond maximum;
- empty input;
- duplicate operations;
- truncated representation;
- impossible enum/tag;
- forced dependency failure.

Rule:

> invalid input must not silently corrupt owned state.

## Fuzzing intuition

**Fuzzing** автоматически генерирует/мутирует inputs и ищет crashes, sanitizer findings, hangs или violated assertions.

Fuzzer особенно полезен, если есть:

```text
cheap parser/operation
clear oracle/invariant
fast reset
sanitizers
```

Fuzzing не доказывает absence of bugs; он исследует large input space efficiently.

## Seed corpus

Начинай с meaningful small seeds: empty, smallest valid, boundary valid, one-past invalid, collision sequence. Pure random bytes without structure иногда плохо проходят parser front door.

## Minimize

Найденный failure полезнее после minimization: smallest input makes root cause/debugging/regression clearer.

## Практика

Для одной pure function/parser из уже пройденного:

1. define validity boundary;
2. add deterministic negative cases;
3. make a tiny mutation loop or use available fuzzer if environment supports it;
4. run with sanitizers;
5. save minimized reproducer as regression.

Разбор: [`04-negative-testing-fuzzing.solution.md`](04-negative-testing-fuzzing.solution.md).

## Exit check

Почему «10 000 random inputs without crash» слабее, чем «property + sanitizer + minimized boundary corpus»?