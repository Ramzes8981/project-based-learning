# Module 1B — Rust Systems Bridge

**Статус:** CORE BRIDGE  
**Оценка:** ~30–40 часов  
**Проект:** idiomatic Rust-порт MiniKV с `Vec<Entry>`, `String`, `Option`, `Result` и tests.

## Зачем этот модуль здесь

Rust вводится **после** ручной памяти C, а не до неё. Поэтому ownership/borrow checker не являются абстрактными правилами языка: мы уже видели dangling pointers, use-after-free, allocation ownership и aliasing вручную.

Цель — понять, какие C-инварианты Rust переносит в type system/borrow checker, а какие всё равно остаются ответственностью инженера.

## Уроки

1. [`01-cargo-rust-model.md`](01-cargo-rust-model.md)
2. [`02-ownership-moves-drop.md`](02-ownership-moves-drop.md)
3. [`03-borrowing-references.md`](03-borrowing-references.md)
4. [`04-lifetimes-slices.md`](04-lifetimes-slices.md)
5. [`05-option-result-errors.md`](05-option-result-errors.md)
6. [`06-vec-string-collections.md`](06-vec-string-collections.md)
7. [`07-unsafe-raw-pointers-ffi.md`](07-unsafe-raw-pointers-ffi.md)
8. [`08-send-sync-concurrency-preview.md`](08-send-sync-concurrency-preview.md)
9. [`09-module-checkpoint.md`](09-module-checkpoint.md)

## Проект

[`project/SPEC.md`](project/SPEC.md)

Мы **не** переписываем всю C Hash Table на Rust. Bridge-проект использует стандартные collections там, где они не являются целью урока, и концентрируется на ownership/borrowing/error handling/API design.
