# 1B.1 — Rust toolchain и модель программы

**Теория:** ~35 мин  
**Упражнение:** ~30 мин  
**Project slice:** ~25 мин  
**С телефона:** теория — да

← [`README`](README.md) · → [`02-ownership-moves-drop.md`](02-ownership-moves-drop.md)

## Цель

Научиться собирать, тестировать и форматировать Rust-проект через Cargo и увидеть главное отличие от C: Rust compiler проверяет гораздо больше semantic invariants до запуска.

## Prerequisite check

1. Что такое ownership contract в C?
2. Почему C compiler не может автоматически запретить все dangling pointers?
3. Чем build-time diagnostics отличаются от sanitizer runtime diagnostics?

## Toolchain

Курс использует stable Rust и Cargo.

Проверь:

```bash
rustc --version
cargo --version
```

Создай проект:

```bash
cargo new rust_probe
cd rust_probe
cargo run
```

Основные команды:

```text
cargo check   — type/borrow checking без полного финального build
cargo build   — сборка
cargo run     — build + запуск binary
cargo test    — tests
cargo fmt     — formatting
cargo clippy  — дополнительные lint checks
```

## Crate и package

Cargo package описывается `Cargo.toml`. В package может быть library crate, binary crate или несколько targets.

Для bridge-проекта мы предпочитаем маленькую library с tests и отдельный binary только при необходимости.

## Variables и mutability

По умолчанию binding immutable:

```rust
let x = 10;
```

Для изменения binding/object через него:

```rust
let mut x = 10;
x += 1;
```

Это не просто stylistic preference: Rust заставляет mutability быть явной частью local reasoning.

## Expressions

Rust блоки являются expressions:

```rust
let y = {
    let x = 3;
    x + 1
};
```

Последнее выражение без `;` становится value блока.

## Functions

```rust
fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

Параметры имеют явные types, return type записывается после `->`.

## `match`

Rust `match` требует exhaustive reasoning по enum variants.

```rust
fn describe(x: Option<i32>) -> &'static str {
    match x {
        Some(_) => "value",
        None => "none",
    }
}
```

`Option` подробно разберём позже; сейчас важна идея compiler-checked variants.

## C vs Rust compiler

C:

```text
compiler checks types/syntax partially
runtime + sanitizers catch many memory violations
ownership mostly convention
```

Rust safe code:

```text
compiler additionally enforces ownership/borrowing rules
many lifetime/alias bugs rejected before executable exists
```

Но Rust не доказывает business correctness, protocol correctness или отсутствие deadlock/logic bugs.

## Упражнение

Создай маленький crate `rust_probe`:

- функция `classify(i32) -> &'static str`;
- минимум 4 unit tests;
- deliberately попробуй изменить immutable binding и прочитай compiler error;
- исправь через `mut` только там, где mutation действительно нужна;
- запусти `cargo fmt`, `cargo clippy`, `cargo test`.

Разбор: [`01-cargo-rust-model.solution.md`](01-cargo-rust-model.solution.md).

## Project slice

Создай в [`project/`](project/) свой Rust package для Rust MiniKV и README. Пока только зафиксируй operations/limits и C→Rust comparison goals, без storage implementation.

## Exit check

Объясни различие ролей `cargo check`, `cargo test`, compiler borrow checking и runtime tests.
