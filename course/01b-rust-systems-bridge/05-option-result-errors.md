# 1B.5 — Как сделать отсутствие и failure частью типа

**Теория:** ~55 мин · **Практика:** ~60 мин · **С телефона:** теория — да

← [`04-lifetimes-slices.md`](04-lifetimes-slices.md) · → [`06-vec-string-collections.md`](06-vec-string-collections.md)

## Проблема

C API часто кодирует multiple meanings в одно число/pointer: `NULL`, `-1`, `errno`, special enum. Это может быть корректно, но caller обязан помнить convention.

Rust предлагает sum types, которые заставляют разобрать alternatives явно.

## `Option<T>`

Когда value может отсутствовать без «ошибки системы»:

```rust
Some(value)
None
```

Например lookup key.

## `Result<T, E>`

Когда operation может завершиться success/failure с reason:

```rust
Ok(value)
Err(error)
```

`?` распространяет compatible error из текущей function, но не «игнорирует ошибку».

## Почему не `unwrap()` everywhere

`unwrap` превращает `None/Err` в panic. Для маленького test fixture это иногда приемлемо; для normal service input это часто неверный error policy.

## Практика

Сделай parser integer command, который различает malformed input и valid value через `Result`; lookup через `Option`; caller обязан обработать оба уровня явно.

Разбор: [`05-option-result-errors.solution.md`](05-option-result-errors.solution.md).

## Exit check

Когда `None` лучше `Err`, и почему `?` не является скрытым exception catch?