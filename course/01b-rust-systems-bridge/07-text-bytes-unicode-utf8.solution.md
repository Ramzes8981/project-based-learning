# Разбор упражнения 1B.7

Standard boundary выглядит так:

```rust
use std::str;

fn decode(input: &[u8]) -> Result<&str, str::Utf8Error> {
    str::from_utf8(input)
}
```

`str::from_utf8` не меняет bytes: либо возвращает borrowed `&str`, либо error. Это отличается от lossy conversion, которая может подменить invalid sequences.

Для `"Ж"`: UTF-8 использует 2 bytes, но `chars().count()` равен 1. Для некоторых визуальных emoji/combining sequences даже `chars().count()` не равно числу grapheme clusters.
