# 1B.9 — Checkpoint: можешь ли ты перевести C ownership contract в Rust

**Время:** ~2–4 часа · **С телефона:** review — да; project — ПК

← [`08-unsafe-raw-pointers-ffi.md`](08-unsafe-raw-pointers-ffi.md) · ↑ [`README`](README.md)

## Explain

1. Почему `String` move защищает single-owner resource?
2. Когда нужен borrow вместо move?
3. Почему overlapping `&mut` + `&` запрещён?
4. Что lifetime annotation описывает и чего не делает?
5. Чем `Option` отличается от `Result` по semantics?
6. Почему `Vec` growth способен invalid references?
7. Почему `String` не индексируется как `char[]`?
8. Что programmer обязан доказать внутри `unsafe`?
9. Почему FFI должен использовать C-compatible types/layout и отдельный ownership contract?

## Project gate

Rust MiniKV проходит [`project/ACCEPTANCE.md`](project/ACCEPTANCE.md). Unnecessary cloning in lookup/update paths объяснено или устранено.

## Transfer

Возьми один C API из предыдущего модуля и опиши две версии Rust interface:

- direct raw/FFI-like boundary;
- safe wrapper, который делает invalid states труднее выразить.

## Gate

`Send`/`Sync` не входят в checkpoint. Они станут осмысленны только с настоящей concurrency-задачей.