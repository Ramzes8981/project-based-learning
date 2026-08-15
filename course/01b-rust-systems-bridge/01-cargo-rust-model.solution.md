# Разбор 1B.1

Пример:

```rust
fn classify(x: i32) -> &'static str {
    match x {
        i32::MIN..=-1 => "negative",
        0 => "zero",
        1..=9 => "small",
        _ => "large",
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn boundaries() {
        assert_eq!(classify(-1), "negative");
        assert_eq!(classify(0), "zero");
        assert_eq!(classify(9), "small");
        assert_eq!(classify(10), "large");
    }
}
```

Важно не копировать exact ranges, а увидеть: tests встроены в normal Cargo workflow, а `match` позволяет compiler проверить exhaustive coverage pattern space.
