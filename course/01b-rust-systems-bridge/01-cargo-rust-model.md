# 1B.1 — Как собрать и запустить Rust-программу без магии IDE

**Теория:** ~35 мин · **Практика:** ~35 мин · **С телефона:** теория — да

← [`README`](README.md) · → [`02-ownership-moves-drop.md`](02-ownership-moves-drop.md)

## Проблема

В C мы уже различаем source, compiler, executable и build rules. Rust добавляет удобный стандартный build tool, но не отменяет эту модель.

## Cargo

`cargo` управляет package metadata, build/test commands и dependencies. Для course project:

```bash
cargo new rust_minikv
cd rust_minikv
cargo build
cargo run
cargo test
cargo check
```

`cargo check` проверяет program/type/borrow rules без финального code generation executable и обычно быстрее full build.

## `rustc` и Cargo

Rust compiler называется `rustc`. Cargo обычно вызывает его за нас с нужными arguments.

```text
Cargo.toml + source
→ cargo
→ rustc invocations
→ artifacts
```

Не делай mental model «Cargo = язык». Это orchestration/build layer.

## Expression-oriented syntax

Rust block может возвращать последнее expression без `;`:

```rust
fn bigger(a: i32, b: i32) -> i32 {
    if a > b { a } else { b }
}
```

С `;` expression превращается в statement returning unit `()`.

## Mutability explicit

```rust
let x = 10;      // immutable binding
let mut y = 10;  // mutable binding
y += 1;
```

Это ещё не ownership. Сначала только замечаем: mutation надо разрешить явно.

## Практика

Создай package, добавь маленькую function + unit test, запусти `cargo check`, `cargo test`, `cargo run`. Намеренно сделай type mismatch и прочитай compiler diagnostic целиком до исправления.

Разбор: [`01-cargo-rust-model.solution.md`](01-cargo-rust-model.solution.md).

## Exit check

Чем `cargo` отличается от `rustc`, и зачем `cargo check`, если есть `cargo build`?