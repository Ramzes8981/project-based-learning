# 1B.7 — Почему Rust не позволяет индексировать UTF-8 строку как массив символов

**Теория:** ~50 мин · **Практика:** ~45 мин · **С телефона:** да

← [`06-vec-string-collections.md`](06-vec-string-collections.md) · → [`08-unsafe-raw-pointers-ffi.md`](08-unsafe-raw-pointers-ffi.md)

## Что уже известно

Из 1.3B: bytes ≠ Unicode code points; UTF-8 code point занимает 1–4 bytes; user-visible grapheme может быть сложнее code point.

Этот урок **не впервые объясняет Unicode**. Он показывает, как Rust types защищают тот же contract.

## `String` / `str` guarantee

Rust `String` и `str` содержат valid UTF-8. Поэтому arbitrary byte index не обязан попадать на character boundary.

Именно поэтому `s[0]` для `String`/`str` не предоставляется как «первый символ».

## Что считать

```rust
s.len()          // bytes
s.chars()        // Unicode scalar values/code points-like iteration
s.bytes()        // raw UTF-8 bytes
```

`chars().count()` всё ещё не равно универсальному «количеству видимых graphemes».

## Byte protocol boundary

Network/file binary protocol should parse `&[u8]`. Только field, который protocol объявляет UTF-8 text, преобразуется через validation вроде `std::str::from_utf8`.

Так invalid bytes не превращаются случайно в text assumption.

## Практика

Для `"AЖ€"` сравни `len`, `chars().count()`, `bytes()`; затем попробуй `from_utf8` на valid/invalid byte slices и обработай `Result`.

Разбор: [`07-text-bytes-unicode-utf8.solution.md`](07-text-bytes-unicode-utf8.solution.md).

## Exit check

Почему отсутствие `s[0]` — следствие UTF-8 representation, а не произвольная прихоть Rust?