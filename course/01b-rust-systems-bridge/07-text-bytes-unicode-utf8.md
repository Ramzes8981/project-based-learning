# 1B.7 — Bytes, Unicode и UTF-8: где заканчивается «строка»

**Теория:** ~80 мин  
**Упражнение:** ~60 мин  
**Project slice:** ~30 мин  
**С телефона:** да

← [`06-vec-string-collections.md`](06-vec-string-collections.md) · → [`08-unsafe-raw-pointers-ffi.md`](08-unsafe-raw-pointers-ffi.md)

## Цель

Не путать bytes, Unicode code points и визуальные символы; выбирать `&[u8]` или `&str` по контракту данных.

## Три уровня

```text
bytes -> encoding -> Unicode code points -> grapheme clusters on screen
```

**Byte** — 8-bit unit в нашем окружении.  
**Code point** — Unicode scalar/code point, например `U+0416`.  
**UTF-8** — encoding code points в 1–4 bytes.  
**Grapheme cluster** — то, что пользователь часто воспринимает как один «символ»; может состоять из нескольких code points.

## ASCII

ASCII bytes `0..127` совпадают с теми же Unicode code points в UTF-8. Поэтому ASCII-delimiters (`\n`, space, `:`) можно искать по bytes внутри valid UTF-8 без декодирования всех characters.

## `len()` в Rust string

```rust
let s = "Ж";
assert_eq!(s.len(), 2);
```

`str::len()` возвращает bytes, не количество displayed characters.

`chars().count()` считает Unicode scalar values, но всё ещё не grapheme clusters.

## Почему `s[0]` запрещено

UTF-8 variable-width. Arbitrary integer byte index может попасть внутрь encoded code point. Rust не обещает O(1) «character indexing» для `str`.

Slice `&s[a..b]` допустим только по valid UTF-8 boundaries, иначе panic.

## Binary data

Compressed payload, image, hash digest, length-prefixed protocol body — не text. Используй `&[u8]`/`Vec<u8>` и выполняй text decode только там, где protocol explicitly обещает encoding.

## Validation boundary

Типичная pipeline:

```text
network/file bytes
↓
length/bounds validation
↓
if field is text: UTF-8 validation
↓
&str / String domain logic
```

Не преобразовывай arbitrary bytes через lossy conversion, если protocol требует отклонять invalid text: это меняет данные и может скрыть malformed input.

## C comparison

`char *`/C string не кодирует encoding. `strlen` считает bytes до `\0`. Значит UTF-8 C string может иметь `strlen` больше числа Unicode characters.

## Упражнение

Напиши Rust функцию, принимающую `&[u8]` и возвращающую:

```text
Result<&str, Utf8Error-like result>
```

через standard UTF-8 validation. Проверь ASCII, Cyrillic, emoji и invalid byte sequence.

Затем для valid `&str` сравни `len()` и `chars().count()`.

Разбор: [`07-text-bytes-unicode-utf8.solution.md`](07-text-bytes-unicode-utf8.solution.md).

## Project slice

В Rust MiniKV зафиксируй: keys/values — именно UTF-8 text (`String`) или arbitrary bytes (`Vec<u8>`)? Текущий bridge использует text ради сравнения с C strings, но ты должен понимать ограничение.

## Exit check

Почему «длина строки» без уточнения units — неоднозначная инженерная фраза?
