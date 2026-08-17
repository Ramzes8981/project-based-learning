# Разбор 1B.2

```rust
fn consume(s: String) {
    println!("consumed: {s}");
}

fn main() {
    let a = String::from("hello");
    let b = a;

    // println!("{a}"); // compile error: a moved

    let c = b.clone();
    println!("b={b}, c={c}");

    consume(c);
    // c moved into consume
}
```

Главное — compiler error является частью урока. Не нужно «бороться с borrow checker»: сначала сформулируй, кто должен владеть value после каждой операции.
