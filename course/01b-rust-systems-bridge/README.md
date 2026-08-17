# Module 1B — Как Rust заставляет явно описывать владение ресурсами

**Core:** ~25–35 часов.  
**Prerequisite:** C memory-safety phase + Vector/Hash Table mental models.

## Зачем Rust именно сейчас

В C мы уже столкнулись с реальными проблемами:

```text
кто освобождает allocation?
может ли borrowed pointer пережить owner?
что инвалидирует reference?
как вернуть failure без двусмысленного sentinel?
```

Только теперь Rust ownership/borrowing имеют естественную мотивацию. Это не второй beginner-language course и не замена пониманию C.

## Core lessons

1. [`01-cargo-rust-model.md`](01-cargo-rust-model.md) — **Как собрать и запустить Rust-программу без магии IDE**.
2. [`02-ownership-moves-drop.md`](02-ownership-moves-drop.md) — **Как язык выбирает одного ответственного за resource**.
3. [`03-borrowing-references.md`](03-borrowing-references.md) — **Как временно дать доступ, не передавая владение**.
4. [`04-lifetimes-slices.md`](04-lifetimes-slices.md) — **Почему reference не может пережить данные**.
5. [`05-option-result-errors.md`](05-option-result-errors.md) — **Как сделать отсутствие и failure частью типа**.
6. [`06-vec-string-collections.md`](06-vec-string-collections.md) — **Как знакомые dynamic collections выглядят при compiler-checked ownership**.
7. [`07-text-bytes-unicode-utf8.md`](07-text-bytes-unicode-utf8.md) — **Почему Rust не позволяет индексировать UTF-8 строку как массив символов**.
8. [`08-unsafe-raw-pointers-ffi.md`](08-unsafe-raw-pointers-ffi.md) — **Где заканчиваются гарантии safe Rust и начинается внешний contract**.
9. [`10-module-checkpoint.md`](10-module-checkpoint.md) — checkpoint.

Concurrency-specific Rust contracts сознательно отложены до того места курса, где появится реальная проблема параллельного shared state.

## Project

[`project/README.md`](project/README.md) — Rust MiniKV bridge. Он проверяет перенос mental model из C, а не знание framework-ов.

## Не нужно сейчас

- async runtime;
- macros internals;
- trait-object design;
- pinning;
- deep `unsafe` optimization;
- custom allocators;
- concurrency-specific marker traits до соответствующей systems-задачи.