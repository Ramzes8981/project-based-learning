# 1.16 — Поиск подстроки: naive, KMP intuition, Rabin–Karp

**Теория:** ~90 мин  
**Упражнение:** ~75 мин  
**С телефона:** да

← [`15-dynamic-programming.md`](15-dynamic-programming.md) · → [`17-trie.md`](17-trie.md)

## Цель

Понять, как алгоритм использует структуру pattern, чтобы не начинать сравнение заново после каждого mismatch.

> В этом уроке C string рассматривается как последовательность bytes до `\0`. Unicode/text semantics будут отдельным уроком в Rust Bridge.

## Naive search

Для каждой possible start position сравниваем pattern слева направо.

Worst case `O(n*m)` для text length `n`, pattern length `m`.

## Prefix function / KMP intuition

Если часть pattern уже совпала, mismatch не всегда заставляет забыть всё совпадение. Нужно знать длину крупнейшего proper prefix pattern, который одновременно suffix уже совпавшей части.

Prefix table строит эту информацию заранее.

```text
pattern: a b a b a c
prefix:  0 0 1 2 3 0
```

Во время search pointer по text не откатывается назад; pattern state переходит по prefix information. Итоговая complexity `O(n+m)`.

Не заучивай код префикс-функции как заклинание: на каждом fallback спрашивай, какой prefix уже гарантированно совпадает.

## Rabin–Karp

Сравнивает rolling hash окон длины pattern.

```text
hash(window) == hash(pattern)
```

не означает равенство: hash collision возможен, поэтому candidate обычно подтверждается byte comparison.

Преимущество — быстрое обновление hash при сдвиге окна и естественная связь с hashing/probability.

## Упражнение

Обязательно реализуй naive substring search для byte strings с явными lengths (не полагайся только на `strlen`).

Затем на бумаге построи prefix table для нескольких patterns и проследи KMP transitions. Полная KMP implementation — transfer task, если базовая логика понятна.

Для Rabin–Karp посчитай toy rolling hash на маленьком modulus и специально найди collision, чтобы не спутать hash с proof equality.

Разбор: [`16-string-searching.solution.md`](16-string-searching.solution.md).

## Edge cases

- empty pattern — заранее выбери contract;
- pattern longer than text;
- repeated characters;
- binary bytes с `0` требуют length-based API, не C-string API;
- arithmetic overflow в rolling hash должен быть частью выбранной unsigned/modular модели.

## Exit check

Почему KMP умеет не откатывать text index, а Rabin–Karp обязан подтверждать совпавший hash?
