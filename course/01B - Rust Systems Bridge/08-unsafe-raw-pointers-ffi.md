# 1B.8 — Где заканчиваются гарантии safe Rust и начинается внешний contract

**Теория:** ~85 мин · **Лаб:** ~90 мин · **С телефона:** теория — да

← [`07-text-bytes-unicode-utf8.md`](07-text-bytes-unicode-utf8.md) · → [`10-module-checkpoint.md`](10-module-checkpoint.md)

## Проблема

ОС и C libraries не обязаны говорить на языке Rust references/ownership. На boundary приходится работать с raw pointers, C ABI и assumptions, которые compiler сам доказать не может.

## `unsafe` не выключает правила

`unsafe` означает: programmer вручную гарантирует дополнительные invariants для операции. Safe Rust guarantees вокруг блока остаются важны.

Raw pointers:

```rust
*const T
*mut T
```

могут быть null, dangling, misaligned или указывать на insufficient/incorrectly typed storage. Dereference требует `unsafe` и valid contract.

## FFI

**Foreign Function Interface (FFI)** — boundary между Rust и code с другим ABI, например C.

Для C layout struct:

```rust
#[repr(C)]
struct Pair {
    key: std::os::raw::c_int,
    value: std::os::raw::c_int,
}
```

Не учи универсальное правило «C `int` = Rust `i32`». Используй C-compatible alias `c_int`; точная width/ABI — property target platform.

## Ownership across FFI

Самый опасный вопрос:

```text
кто allocates?
кто frees?
каким allocator/deallocator pair?
может ли pointer быть retained after call?
```

Если C возвращает owned pointer, Rust не должен автоматически `Box::from_raw` без доказанного allocation/layout/deallocator contract.

## Strings across C boundary

C string pointer требует:

- non-null if contract says so;
- reachable terminating `\0`;
- valid readable bytes up to terminator;
- encoding contract separately.

`CStr` helps model nul-terminated bytes; it does not magically prove original pointer validity.

## Panic across boundary

Не позволяй Rust panic unwinding пересекать обычную C ABI boundary unless ABI/strategy explicitly supports required behavior. Course FFI functions catch/avoid panic and convert failures to documented status.

## Local reference

Перед лабой прочитай [`FFI_MINI_REFERENCE.md`](FFI_MINI_REFERENCE.md). Внешний tutorial не требуется.

## Практика

Сделай tiny C library `add_pair` + Rust caller:

- `#[repr(C)]` struct;
- C header and Rust declaration agree on C-compatible types;
- no ownership transfer;
- nullability contract explicit;
- build/test both sides.

Разбор: [`08-unsafe-raw-pointers-ffi.solution.md`](08-unsafe-raw-pointers-ffi.solution.md).

## Exit check

Назови минимум пять invariants, которые raw pointer type сам по себе не доказывает.