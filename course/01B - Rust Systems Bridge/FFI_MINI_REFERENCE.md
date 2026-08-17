# Мини-справочник FFI: C ↔ Rust

Этого reference достаточно для course lab. Не рассматривай его как полный ABI standard.

## 1. C-compatible scalar types

Не предполагай, что C spelling автоматически равен fixed-width Rust type на любой platform.

Для обычных C types используй aliases из `std::os::raw`:

```rust
use std::os::raw::{c_char, c_int, c_uint, c_void};
```

Если C API itself uses `int32_t`/`uint32_t`, тогда matching Rust fixed-width `i32/u32` обычно является частью explicit width contract.

## 2. C layout

```rust
#[repr(C)]
struct Pair {
    a: c_int,
    b: c_int,
}
```

`#[repr(C)]` просит C-compatible field layout rules for target ABI. Это не проверяет, что C header действительно совпадает: обе стороны должны быть synchronized.

## 3. Function declarations

Пример C:

```c
struct Pair { int a; int b; };
int pair_sum(const struct Pair *p, int *out);
```

Rust declaration:

```rust
unsafe extern "C" {
    fn pair_sum(p: *const Pair, out: *mut c_int) -> c_int;
}
```

Exact syntax can depend on Rust edition/version; course environment should pin/check compiler. Semantic contract is stable: C ABI + compatible types + raw pointers.

## 4. Raw-pointer validity checklist

Before dereference/call requiring access, establish:

- nullability rule;
- alignment;
- correct pointee type/layout;
- readable/writable size;
- lifetime covers call/use;
- aliasing/mutability assumptions;
- ownership transfer or non-transfer.

`unsafe` block marks where these proofs become programmer responsibility.

## 5. C strings

`*const c_char` is not automatically a Rust `&str`.

Need separate contracts:

```text
pointer valid?
NUL terminator reachable?
bytes readable?
which encoding?
```

`CStr` models NUL-terminated bytes once pointer preconditions are satisfied. UTF-8 conversion may still fail.

## 6. Allocation ownership

Never mix allocators by assumption.

If C allocates, API should state how caller releases. If Rust allocates and passes temporary memory, C must not retain pointer past permitted lifetime unless ownership transfer is explicitly designed.

`Box::from_raw`, `Vec::from_raw_parts`, `CString::from_raw` require very specific origin/layout/ownership invariants. They are not generic «take ownership of any pointer» functions.

## 7. Panic/error boundary

Do not let ordinary Rust panic unwind into C caller under an ABI that does not guarantee it. Prefer non-panicking FFI body or catch panic on Rust side and translate into status/error contract.

## 8. Build sanity

Always compile both C header consumer and Rust declaration for the target environment; add a tiny integration test that catches signature/layout drift.