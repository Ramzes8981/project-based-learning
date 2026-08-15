# 1B.7 — `unsafe`, raw pointers и FFI

**Теория:** ~75 мин  
**Lab:** ~60 мин  
**С телефона:** теория — да; lab — ПК

← [`06-vec-string-collections.md`](06-vec-string-collections.md) · → [`08-send-sync-concurrency-preview.md`](08-send-sync-concurrency-preview.md)

## Цель

Понять, что `unsafe` не отключает Rust полностью, а открывает ограниченный набор операций, correctness которых programmer обязан обосновать invariants.

## Safe Rust не может выразить всё systems programming

OS/kernel APIs, custom allocators, intrusive structures, SIMD, FFI и некоторые performance abstractions требуют raw pointers или иных unsafe operations.

Rust предоставляет `unsafe` как явную boundary.

## Что разрешает `unsafe`

Среди основных возможностей:

- dereference raw pointer `*const T` / `*mut T`;
- call unsafe function;
- access mutable static;
- implement unsafe trait;
- access union fields.

Это не означает, что внутри `unsafe` block можно игнорировать обычные types/borrow rules для safe constructs.

## Raw pointers

```rust
let x = 10;
let p: *const i32 = &x;
```

Создать raw pointer можно safe; dereference требует `unsafe`:

```rust
unsafe {
    println!("{}", *p);
}
```

Compiler не гарантирует lifetime/alignment/non-null/alias validity raw pointer. Ответственность похожа на C.

## Unsafe invariant

Перед unsafe code запиши утверждение, которое должно быть истинно.

Например:

```text
p non-null
p aligned for T
p points to initialized live T
read does not violate aliasing rules
memory remains valid for duration
```

Если invariant нельзя сформулировать, unsafe code ещё рано писать.

## Safe abstraction around unsafe core

Цель хорошего Rust systems code — минимальная unsafe boundary с safe public API.

```text
safe caller
   ↓
checked preconditions
   ↓
small unsafe operation
   ↓
restored invariant
   ↓
safe result
```

## FFI

Rust может вызывать C ABI functions и экспортировать C-compatible API.

Conceptually:

```text
Rust types/API
  ↓ explicit FFI boundary
C ABI types/layout
  ↓
C function/library
```

Не каждый Rust type ABI-compatible с C. На FFI boundary используют C-compatible primitive types/`#[repr(C)]` structs и explicit ownership rules.

Strings особенно требуют conversion: Rust `String/&str` не являются C null-terminated `char *` напрямую. Для C strings используются `CString/CStr`.

## Panic across FFI

Не проектируй API так, чтобы Rust panic бесконтрольно пересекал C ABI boundary. Error behavior должен быть явно определён.

## `unsafe` не равно «плохо»

Плохо — не `unsafe` keyword, а неподдерживаемый invariant и oversized unsafe surface.

Standard library сама содержит unsafe internals, чтобы expose safe abstractions вроде `Vec`.

## Causal questions

1. Почему raw pointer creation safe, а dereference unsafe?
2. Что именно borrow checker перестаёт гарантировать для raw pointer?
3. Почему FFI требует layout/ownership contract?
4. Как уменьшение unsafe surface повышает auditability?

## Lab

### Part A — raw pointer observation

Создай живой `i32`, получи `*const i32`, безопасно сформулируй invariant и прочитай value внутри маленького `unsafe` block.

Не создавай намеренно dangling pointer dereference.

### Part B — tiny C FFI

Напиши отдельную C function, например:

```text
int add_two(int a, int b)
```

и вызови её из Rust через C ABI/build integration. Основная цель — пройти boundary, а не написать сложную library.

В README lab опиши types, ownership (здесь ownership ресурсов нет) и build/link steps.

Разбор: [`07-unsafe-raw-pointers-ffi.solution.md`](07-unsafe-raw-pointers-ffi.solution.md).

## Exit check

Для любого unsafe block можешь ли ты назвать invariant до входа и что гарантируется после выхода?
