# 1C.3 — Testability, dependency boundaries и test doubles

**Теория:** ~70 мин  
**Упражнение:** ~50 мин  
**С телефона:** да

← [`02-invariants-properties-regressions.md`](02-invariants-properties-regressions.md) · → [`04-negative-testing-fuzzing.md`](04-negative-testing-fuzzing.md)

## Цель

Понимать, когда зависимость мешает тесту, и отделять core logic от I/O/time/randomness без архитектуры «ради mock».

## Hard-coded dependency

Если parser сам читает stdin, сам пишет файл и сам вызывает clock, unit test вынужден поднимать весь мир.

Лучше разделить:

```text
I/O boundary -> bytes/data -> pure-ish core -> result -> I/O boundary
```

Не всё обязано быть pure, но side effects должны иметь понятные boundaries.

## Dependency injection — идея

Dependency передаётся компоненту вместо жёсткого создания внутри.

В C это может быть function pointer + context struct. В Rust — trait/reference/closure или простой параметр.

Цель — не framework, а возможность заменить expensive/nondeterministic boundary контролируемой реализацией.

## Test doubles

**Stub:** возвращает заранее заданные данные.  
**Fake:** упрощённая рабочая implementation, например in-memory storage вместо file.  
**Spy:** записывает, что было вызвано.  
**Mock:** test задаёт expected interactions и проверяет их.

Термины в индустрии иногда смешивают. Важнее описывать поведение double, чем спорить о названии.

## Не mock everything

Если тест знает каждый внутренний function call, рефакторинг ломает tests без изменения behavior. Предпочитай public state/output, а interaction checks используй там, где само взаимодействие является contract (например `fsync` policy abstraction в специальном test).

## C example pattern

```c
typedef ssize_t (*ReadFn)(void *ctx, void *buf, size_t n);
```

Core reader получает `ReadFn + ctx`; production context вызывает real fd, test context отдаёт chunked fixture. Это позже поможет тестировать partial I/O.

## Rust example pattern

Функция может принимать `impl Read`/`&mut dyn Read` или generic parameter, а test использовать byte slice/cursor.

## Упражнение

Возьми функцию, которая сейчас напрямую читает/пишет внешний ресурс, или спроектируй маленькую parser function. Раздели:

1. acquisition of bytes;
2. parsing/validation;
3. side effect/result.

Покажи, какой тест теперь можно выполнить без real file/network.

Разбор: [`03-testability-dependencies-doubles.solution.md`](03-testability-dependencies-doubles.solution.md).

## Exit check

Можешь ли ты объяснить, почему dependency injection — это прежде всего control over dependency, а не обязательный OOP container?
