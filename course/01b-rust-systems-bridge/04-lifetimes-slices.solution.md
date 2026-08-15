# Разбор 1B.4

```rust
fn first_word(s: &str) -> &str {
    match s.as_bytes().iter().position(|&b| b == b' ') {
        Some(i) => &s[..i],
        None => s,
    }
}
```

Для ASCII space byte boundary одновременно является valid UTF-8 boundary. Если бы delimiter/search работал по arbitrary bytes внутри multibyte character, slice boundary требовал бы отдельной проверки.

Function возвращает borrow в исходный `s`, а не новый owned String.
