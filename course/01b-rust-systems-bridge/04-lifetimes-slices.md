# 1B.4 — Lifetimes и slices

**Теория:** ~70 мин  
**Упражнение:** ~50 мин  
**Project slice:** ~45 мин  
**С телефона:** да

← [`03-borrowing-references.md`](03-borrowing-references.md) · → [`05-option-result-errors.md`](05-option-result-errors.md)

## Цель

Понять lifetime как статическое отношение между references и owner data, а slices — как borrowed region с длиной.

## Lifetime не runtime timer

Lifetime annotation не продлевает жизнь объекта. Она описывает relation, которую compiler должен проверить.

## Почему reference на local нельзя вернуть

Неправильная идея:

```rust
fn local_view<'a>() -> &'a str {
    let s = String::from("abc");
    &s
}
```

Caller пытается выбрать произвольный `'a`, но локальный `s` уничтожается при return. Никакой annotation не способна создать owner, который живёт дольше.

Правильные варианты зависят от цели:

- вернуть owned `String`;
- вернуть reference на input data;
- хранить data в более долгоживущем owner.

Например relation между input/output:

```rust
fn prefix<'a>(input: &'a str, n: usize) -> &'a str {
    &input[..n]
}
```

Такая функция может вернуть borrow, потому что source lifetime приходит от caller. Для `str` `n` обязан быть UTF-8 character boundary; позже разберём это отдельно.

## Несколько input references

```rust
fn longer<'a>(a: &'a str, b: &'a str) -> &'a str {
    if a.len() >= b.len() { a } else { b }
}
```

`'a` не заставляет объекты иметь одинаковую физическую жизнь. Returned reference ограничивается временем, безопасным для выбранного input.

## Lifetime elision

Common cases compiler выводит сам:

```rust
fn first(s: &str) -> &str
```

Explicit lifetimes нужны для выражения relation, а не для украшения signatures.

## Slice

C часто использует:

```text
T *ptr + size_t len
```

Rust связывает это в type:

```rust
&[T]
&mut [T]
```

Reference добавляет lifetime/aliasing contract, slice — length/bounds model.

## `String` / `&str` / `&[u8]`

- `String` — owner growable valid UTF-8 bytes;
- `&str` — borrowed valid UTF-8 view;
- `&[u8]` — arbitrary bytes, text validity не обещается.

Для binary protocols почти всегда начинать нужно с bytes, а превращать в `&str` только после validation.

## Упражнение

Напиши `first_word(&str) -> &str`, который возвращает slice до первого ASCII space или весь input без allocation.

Tests: empty, leading space, no spaces, ordinary ASCII phrase, non-ASCII text before ASCII space.

Разбор: [`04-lifetimes-slices.solution.md`](04-lifetimes-slices.solution.md).

## Project slice

Rust MiniKV:

- lookup input: `&str`;
- storage: owned `String`;
- lookup result: borrowed reference/view;
- mutation требует `&mut self`, поэтому compiler не даст мутировать Store пока жив borrow из `&self`.

## Exit check

Объясни, почему lifetime annotation описывает связь с owner, но не может сделать local `String` вечным.
