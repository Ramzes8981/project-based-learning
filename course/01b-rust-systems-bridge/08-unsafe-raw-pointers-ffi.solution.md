# Разбор 1B.8

Minimal shape, not a project solution.

C header:

```c
struct Pair {
    int a;
    int b;
};

int pair_sum(const struct Pair *p, int *out);
```

C implementation validates pointers according to its contract and writes result only on success.

Rust side:

```rust
use std::os::raw::c_int;

#[repr(C)]
struct Pair {
    a: c_int,
    b: c_int,
}

unsafe extern "C" {
    fn pair_sum(p: *const Pair, out: *mut c_int) -> c_int;
}
```

The important correction is **not** hard-coding the teaching rule “C `int` always equals Rust `i32`”. `c_int` follows the target C ABI. For fixed-width C types, use matching fixed-width Rust types according to that explicit API contract.

No ownership transfer occurs in this lab: pointers are borrowed for the duration of the call only.