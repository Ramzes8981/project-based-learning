# Module 1B — Checkpoint

**Время:** ~2–3 часа  
**С телефона:** conceptual review — да

← [`09-send-sync-concurrency-preview.md`](09-send-sync-concurrency-preview.md) · ↑ [`README`](README.md)

## Explain

1. Move / Copy / Clone.
2. `Drop` vs C manual cleanup.
3. `&T` vs `&mut T`.
4. Lifetime annotation: relation, не lifetime extension.
5. Slice vs pointer+length.
6. `String`, `&str`, `Vec<u8>`, `&[u8]`.
7. bytes vs code points vs grapheme clusters.
8. `Option` vs `Result`.
9. почему blanket `clone()` — плохой borrow-checker workaround.
10. safe Rust vs raw pointer/unsafe boundary.
11. Rust 2024 C FFI contract.
12. `Send`/`Sync`, `Arc`/`Mutex`.

## Scenarios

### A
Parser получает network bytes и сразу делает `String::from_utf8_lossy`. Protocol требует reject invalid UTF-8. Что сломано в contract?

### B
Rust FFI declaration говорит `fn f(i64)`, C symbol реально `int f(int)`. Почему compiler Rust не спасает?

### C
Store `get()` возвращает `&str`; caller держит borrow и пытается вызвать `set(&mut self)`. Почему compiler блокирует это и какую C-проблему он предотвращает?

## Project

Проверь [`project/ACCEPTANCE.md`](project/ACCEPTANCE.md) и свой [`project/README.md`](project/README.md).

Rust MiniKV должен демонстрировать owned storage, borrowed lookup, typed errors, tests и отсутствие необоснованного `unsafe`.

## Gate

Правильный итог не «Rust безопасен автоматически», а:

> safe subset проверяет большой класс ownership/alias/lifetime invariants, но protocols, bounds, deadlocks, resource policies, FFI signatures и unsafe invariants остаются инженерной ответственностью.
