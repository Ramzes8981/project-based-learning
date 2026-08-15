# Разбор 1B.7

Минимальный raw pointer example:

```rust
fn main() {
    let x = 42_i32;
    let p: *const i32 = &x;

    // Invariant: x is alive; p came directly from &x; alignment/type valid.
    let value = unsafe { *p };
    assert_eq!(value, 42);
}
```

Для FFI exact Cargo build setup может различаться. Курс допускает маленький build helper/build script как инфраструктуру. Проверяемый навык — ABI boundary и contract, а не memorization build-script syntax.
