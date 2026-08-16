# 1C.3 — Как отделить логику от зависимости, которая мешает воспроизводимому тесту

**Теория:** ~65 мин · **Практика:** ~75 мин · **С телефона:** теория — да

← [`02-invariants-properties-regressions.md`](02-invariants-properties-regressions.md) · → [`04-negative-testing-fuzzing.md`](04-negative-testing-fuzzing.md)

## Проблема

Vector grow должен правильно вести себя при allocation failure. Но «надеяться, что `malloc` случайно вернёт NULL`» — плохой test: он опасен и невоспроизводим.

Нужна controlled boundary.

## Testability

Code **тестопригоден (testable)**, когда важные decisions можно проверить без недетерминированного внешнего мира.

Один способ — передать dependency явно.

Для allocator-like boundary можно концептуально иметь:

```c
typedef void *(*AllocFn)(size_t bytes, void *ctx);
typedef void (*FreeFn)(void *ptr, void *ctx);
```

Production передаёт wrappers around normal allocator; test передаёт deterministic fake that fails on N-th call.

Function pointer/callback уже знаком из 1.9, поэтому hidden prerequisite нет.

## Double

Controlled replacement dependency в тесте часто называют **test double**. Это umbrella term; mock/stub/fake имеют более узкие meanings, но core не требует taxonomy ради taxonomy.

Главное:

```text
production contract and test replacement must obey same interface assumptions
```

## Не делай internal implementation public только ради теста

Лучше вынести meaningful boundary, чем expose private fields и проверять каждую строку implementation. Тест должен защищать behavior/invariant.

## Пример: deterministic allocation failure

State double-а:

```text
call_count
fail_on_call
```

Он возвращает failure exactly on configured call. Теперь можно проверить:

```text
Vector grow fails
→ old data/len/capacity remain valid
→ destroy still safe
```

Никаких `fd`, socket, syscall или short I/O здесь ещё не нужно. Они получат собственные seams после соответствующих lessons.

## Практика

Добавь test allocator seam в Vector или Hash Table только настолько, насколько нужно для deterministic failure injection. Не усложняй production API без причины.

Разбор: [`03-testability-dependencies-doubles.solution.md`](03-testability-dependencies-doubles.solution.md).

## Exit check

Почему controlled allocator failure даёт более сильное evidence, чем попытка «забить всю RAM и посмотреть»?