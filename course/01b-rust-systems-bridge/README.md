# Module 1B — Rust Systems Bridge

**Статус:** CORE BRIDGE  
**Оценка:** ~38–50 часов  
**Проект:** idiomatic Rust MiniKV с `Vec<Entry>`, `String`, `Option`, `Result` и tests.

## Зачем этот модуль здесь

Rust идёт после ручной памяти C. Поэтому ownership/borrow checker связываются с уже знакомыми dangling pointers, aliasing, cleanup и failure paths.

## Уроки

1. [`01-cargo-rust-model.md`](01-cargo-rust-model.md)
2. [`02-ownership-moves-drop.md`](02-ownership-moves-drop.md)
3. [`03-borrowing-references.md`](03-borrowing-references.md)
4. [`04-lifetimes-slices.md`](04-lifetimes-slices.md)
5. [`05-option-result-errors.md`](05-option-result-errors.md)
6. [`06-vec-string-collections.md`](06-vec-string-collections.md)
7. [`07-text-bytes-unicode-utf8.md`](07-text-bytes-unicode-utf8.md)
8. [`08-unsafe-raw-pointers-ffi.md`](08-unsafe-raw-pointers-ffi.md)
9. [`09-send-sync-concurrency-preview.md`](09-send-sync-concurrency-preview.md)
10. [`10-module-checkpoint.md`](10-module-checkpoint.md)

## Внутренний reference

[`FFI_MINI_REFERENCE.md`](FFI_MINI_REFERENCE.md) содержит минимальный build/link contract для C ↔ Rust без обязательного похода во внешнюю документацию.

## Проект

[`project/SPEC.md`](project/SPEC.md) · [`project/README.md`](project/README.md)

Мы не переписываем C Hash Table второй раз. Bridge концентрируется на ownership, borrowing, typed errors, UTF-8 boundaries и safe/unsafe API design.
