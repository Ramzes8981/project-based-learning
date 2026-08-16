# 1B.2 — Как язык выбирает одного ответственного за resource

**Теория:** ~65 мин · **Практика:** ~60 мин · **С телефона:** теория — да

← [`01-cargo-rust-model.md`](01-cargo-rust-model.md) · → [`03-borrowing-references.md`](03-borrowing-references.md)

## Проблема из C

Для dynamic allocation мы сами писали contract:

```text
кто owner?
кто free?
можно ли копировать pointer?
```

Ошибки owner convention давали leak/double free/UAF.

## Ownership

В Rust каждое значение имеет **владельца (owner)** — binding/object context, ответственный за cleanup согласно типу. Когда owner уходит из scope, cleanup вызывается автоматически через `Drop` semantics.

Для owning type вроде `String` простое присваивание обычно не делает независимую копию heap data:

```rust
let a = String::from("hello");
let b = a;
```

Ownership переходит к `b`. Это **перемещение (move)**. Использовать `a` после move compiler не разрешает.

## Почему это не «Rust странно копирует переменные»

Если бы два independent owners считали один allocation своим, оба попытались бы cleanup. Move invalidates old binding at type-check level and preserves single-owner contract.

## `Copy`

Небольшие types без ownership resource, например многие integers, реализуют `Copy`:

```rust
let a = 10i32;
let b = a;
```

После этого оба доступны, потому что независимое bitwise copy безопасно для данного type contract.

Не выводи правило «маленькое = Copy»; это trait/semantic property type-а.

## `clone()` — явная стоимость

Если действительно нужен независимый owned duplicate:

```rust
let b = a.clone();
```

Для `String` это обычно означает новую owned allocation/copy data. `clone()` не должен быть рефлексом для борьбы с compiler errors: сначала уточни desired ownership.

## Drop

Когда owning value заканчивает lifetime, Rust вызывает destructor logic. Это снижает риск forgotten cleanup, но не означает, что любой resource lifetime автоматически идеален: можно держать owner слишком долго или создавать reference cycles через advanced smart pointers.

## Практика

Возьми `String`, покажи move compiler error, затем реши две разные задачи:

1. ownership должен перейти — без clone;
2. нужны две независимые строки — explicit clone.

Разбор: [`02-ownership-moves-drop.solution.md`](02-ownership-moves-drop.solution.md).

## Exit check

Почему move решает именно проблему double ownership, а не просто является синтаксическим ограничением?