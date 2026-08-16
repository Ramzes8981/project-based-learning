# 1C.1 — Откуда тест знает правильный ответ

**Теория:** ~55 мин · **Практика:** ~60 мин · **С телефона:** теория — да

← [`README`](README.md) · → [`02-invariants-properties-regressions.md`](02-invariants-properties-regressions.md)

## Проблема

Программа завершилась без crash. Это ещё не означает, что результат правильный.

Тесту нужен критерий, позволяющий различить correct/incorrect behavior. Такой критерий называют **оракулом (test oracle)**.

## Простой oracle

Для `clamp_score`:

```text
input -1  → 0
input 50  → 50
input 101 → 100
```

Expected values — oracle.

## Уровни тестов — разные boundaries

Названия не важны сами по себе; важен scope evidence.

### Unit

Проверяет небольшой component/function in isolation enough to diagnose logic quickly.

### Integration

Проверяет, что несколько real components правильно договариваются о contract.

### System/end-to-end

Проверяет observable behavior всей программы через внешний interface.

Один end-to-end test не заменяет unit tests: он может сказать «что-то сломано», но не локализует механизм.

## Arrange → Act → Assert

Полезная структура:

```text
prepare known state
perform one behavior
compare result/state with oracle
```

Не обязательно использовать framework, чтобы мыслить так.

## Determinism

Если test зависит от текущего времени, random input, global mutable state или ordering, который contract не обещает, failure трудно воспроизвести.

Первый вопрос flaky test:

> какая скрытая dependency меняется между runs?

## Практика

Для C Vector придумай по одному unit/integration-like/system-like check. Для каждого напиши:

- boundary;
- oracle;
- failure, который он ловит;
- failure, который он **не** ловит.

Разбор: [`01-test-levels-oracles.solution.md`](01-test-levels-oracles.solution.md).

## Exit check

Почему test without oracle может успешно запускаться и почти ничего не доказывать?