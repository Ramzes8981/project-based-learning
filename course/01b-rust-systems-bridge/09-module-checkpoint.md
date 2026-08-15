# Module 1B — Checkpoint

**Время:** ~2–3 часа  
**С телефона:** conceptual review — да

← [`08-send-sync-concurrency-preview.md`](08-send-sync-concurrency-preview.md) · ↑ [`README`](README.md)

## Explain

1. Move vs Copy vs Clone.
2. `Drop` vs manual C `free`.
3. `&T` vs `&mut T`.
4. Почему borrow checker ограничивает aliasing + mutation.
5. Lifetime annotation: что описывает и чего не делает.
6. `String` vs `&str`.
7. `Vec<T>` vs собственный C Vector.
8. `Option` vs `Result`.
9. Когда `unwrap` приемлем и когда это smell.
10. Safe Rust vs `unsafe` boundary.
11. Raw pointers vs references.
12. Что требует FFI contract.
13. `Send`/`Sync`.
14. `Arc` vs `Mutex`.

## C ↔ Rust comparison table — заполни самостоятельно

```text
C concept               Rust analogue / difference
----------------------------------------------------
owned malloc allocation ?
borrowed T*              ?
T* + len                 ?
NULL optional result     ?
status code              ?
free                     ?
manual mutex cleanup     ?
```

## Core bridge project

Проверь [`project/ACCEPTANCE.md`](project/ACCEPTANCE.md).

Rust MiniKV должен демонстрировать:

- owned `String` data;
- borrowed lookup API;
- `&self`/`&mut self` receiver semantics;
- `Option/Result`;
- unit tests;
- no unjustified `unsafe`;
- no blanket clone-everything workaround.

## Transfer

Одно изменение:

- iterator по entries;
- delete;
- case-sensitive/case-normalized policy;
- configurable constraints;
- borrowed insertion API с controlled copying.

## Engineering review

README проекта сравнивает C и Rust по:

- ownership enforcement;
- allocation cleanup;
- aliasing;
- error representation;
- performance assumptions;
- remaining bug classes.

## Exit gate

Ты не должен выходить из bridge с выводом «Rust всегда безопасный, C всегда опасный». Правильная модель:

> Safe Rust переносит важную часть memory/alias/lifetime invariants в compiler-checked type system, но системная корректность, API contracts, resource bounds, deadlocks, protocol bugs и unsafe boundaries всё равно требуют инженерного reasoning.

После gate курс возвращается к Unix/processes, преимущественно на C, с Rust comparisons там, где они дают дополнительную ценность.
