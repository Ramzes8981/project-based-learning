# Rust MiniKV — рабочий README

## Status

## Cargo

Зафиксируй edition/toolchain и команды:

```text
cargo fmt
cargo clippy --all-targets --all-features
cargo test
```

## API

Какие методы используют `&self`, какие `&mut self`? Где `Option`, где `Result`?

## Ownership

- кто владеет key/value `String`;
- что `get` возвращает borrowed;
- какие mutations invalidated/blocked while borrow lives;
- где cloning действительно нужен, а где нет.

## Text contract

Keys/values — UTF-8 text или bytes? Текущий bridge ожидает text; запиши limits в bytes или characters и не путай units.

## Error model

Перечисли variants собственного error enum и что считается `None`, `Err`, panic-worthy invariant.

## Unsafe

Основная Store implementation должна быть safe Rust. Если добавляешь unsafe эксперимент, документируй invariant отдельно и не смешивай его с core path.

## Tests

Boundary/error cases и regression tests.

## C ↔ Rust comparison

Сравни cleanup, aliasing, nullability, errors, invalidation и оставшиеся bug classes.

## Debugging story

Compiler/runtime symptom → hypothesis → evidence → root cause → fix → regression.
