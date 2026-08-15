# 1B.5 — `Option`, `Result` и error contracts

**Теория:** ~60 мин  
**Упражнение:** ~45 мин  
**Project slice:** ~60 мин  
**С телефона:** да

← [`04-lifetimes-slices.md`](04-lifetimes-slices.md) · → [`06-vec-string-collections.md`](06-vec-string-collections.md)

## Цель

Перенести C status-code thinking в typed Rust errors без exceptions/magic sentinel values.

## `Option<T>`

Когда value может отсутствовать:

```rust
enum Option<T> {
    Some(T),
    None,
}
```

Lookup естественно может вернуть:

```rust
Option<&str>
```

вместо `NULL` pointer или magic index `-1`.

Compiler заставляет явно рассмотреть `Some/None`, если используешь exhaustive `match`.

## `Result<T, E>`

Операция может успешно вернуть `T` или ошибку `E`:

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

Для project API можно определить собственный enum errors:

```rust
enum StoreError {
    KeyTooLong,
    ValueTooLong,
}
```

В Rust strings grow dynamically, но course constraints всё равно могут существовать как business/protocol limits.

## `?` operator

Если функция сама возвращает совместимый `Result`/`Option`, `?` позволяет early-return error/None.

Это не «скрывает все ошибки». Хороший API всё равно должен иметь осмысленный error type и context.

## Panic vs recoverable error

`panic!` — не обычная замена `Err` для expected input failure.

Expected failures вроде malformed request/not found/io error обычно моделируются через `Result/Option`.

Panic уместнее для violated internal invariant/unrecoverable programming assumption, но даже это зависит от application context.

## `unwrap` anti-pattern

```rust
value.unwrap()
```

может быть допустим в test/prototype, когда invariant уже доказан. В production path слепые `unwrap()` часто превращают нормальную ошибку в process panic.

Правило курса: каждый `unwrap/expect` должен иметь объяснимый invariant или быть в test code.

## C comparison

C:

```text
return code
+ out parameter
+ errno sometimes
+ NULL sentinel sometimes
```

Rust:

```text
Option<T>
Result<T,E>
```

делают success/error variants частью return type.

Но semantic design ошибки всё равно делает инженер.

## Causal questions

1. Когда `Option` лучше `Result`?
2. Почему `Result` не отменяет необходимость продумывать error taxonomy?
3. Почему `unwrap` может быть симптомом плохо продуманного production path?
4. Что `?` делает с control flow?

## Упражнение

Напиши parser для integer setting:

```text
parse_positive("42") -> Ok(42)
parse_positive("0")  -> Err(...)
parse_positive("abc")-> Err(...)
```

Создай собственный error enum минимум с двумя variants.

Не возвращай stringly-typed error в core exercise.

Разбор: [`05-option-result-errors.solution.md`](05-option-result-errors.solution.md).

## Project slice

Реализуй базовые `set/get` Rust MiniKV согласно [`project/SPEC.md`](project/SPEC.md):

- `get` отсутствующего key — `Option`;
- invalid input/constraint failure — `Result`;
- не использовать panic как обычный control flow.

## Exit check

Для каждого failure в API сможешь объяснить: это `None`, `Err`, panic-worthy invariant или вообще невозможное состояние?
