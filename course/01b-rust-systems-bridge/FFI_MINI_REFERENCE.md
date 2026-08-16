# Rust 2024 ↔ C FFI mini reference

Этот файл — достаточный локальный reference для учебных labs. Внешняя документация нужна только для platform-specific details за пределами scope.

## 1. Cargo package

Создай normal binary/library package и установи в `Cargo.toml`:

```toml
[package]
edition = "2024"
```

## 2. C source

Храни lab source, например `native/add.c`.

## 3. `build.rs` без внешних crates

Build script может вызвать system `cc` и `ar`:

```rust
use std::process::Command;

fn run(mut cmd: Command) {
    let status = cmd.status().expect("failed to start tool");
    assert!(status.success(), "native build failed");
}

fn main() {
    let out = std::env::var("OUT_DIR").expect("OUT_DIR");
    let obj = format!("{out}/add.o");
    let lib = format!("{out}/libtinyffi.a");

    let mut cc = Command::new("cc");
    cc.args(["-std=c17", "-Wall", "-Wextra", "-Wpedantic", "-c", "native/add.c", "-o", &obj]);
    run(cc);

    let mut ar = Command::new("ar");
    ar.args(["rcs", &lib, &obj]);
    run(ar);

    println!("cargo:rustc-link-search=native={out}");
    println!("cargo:rustc-link-lib=static=tinyffi");
    println!("cargo:rerun-if-changed=native/add.c");
}
```

В реальном portable crate обычно используют специализированный build crate/tooling. Здесь внешний dependency не нужен: цель — увидеть link boundary.

## 4. Declaration

Rust 2024:

```rust
unsafe extern "C" {
    fn add_two(a: i32, b: i32) -> i32;
}
```

Declaration обязана совпадать с C ABI contract.

## 5. C-compatible layout

Если struct действительно пересекает FFI boundary:

```rust
#[repr(C)]
struct Point {
    x: i32,
    y: i32,
}
```

`repr(C)` задаёт C-compatible layout rules для данного type, но **не решает** ownership, pointer validity или semantic compatibility.

## 6. Strings

- Rust text: `&str`/`String` — UTF-8 + length;
- C string: `char *` convention + `\0` terminator;
- Rust boundary helpers: `CString`, `CStr`.

## 7. Checklist

Перед call проверь:

```text
signature/layout
integer width
pointer nullability
alignment
lifetime
ownership/free function
mutability/aliasing
string encoding/termination
error convention
thread-safety
```
