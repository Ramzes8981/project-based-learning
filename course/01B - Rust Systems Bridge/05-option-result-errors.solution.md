# Разбор 1B.5

```rust
#[derive(Debug, PartialEq)]
enum ParsePositiveError {
    NotANumber,
    NotPositive,
}

fn parse_positive(s: &str) -> Result<u32, ParsePositiveError> {
    let value: u32 = s.parse().map_err(|_| ParsePositiveError::NotANumber)?;
    if value == 0 {
        return Err(ParsePositiveError::NotPositive);
    }
    Ok(value)
}
```

`map_err` переводит чужой parser error в domain-specific error текущего API. Это лучше, чем заставлять caller зависеть от случайного внутреннего error type, если domain contract проще.
