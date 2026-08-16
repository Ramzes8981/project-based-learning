# 1B.8 — `unsafe`, raw pointers и C FFI

**Теория:** ~95 мин  
**Lab:** ~90 мин  
**С телефона:** теория — да; lab — ПК

← [`07-text-bytes-unicode-utf8.md`](07-text-bytes-unicode-utf8.md) · → [`09-send-sync-concurrency-preview.md`](09-send-sync-concurrency-preview.md)

## Цель

Уметь сформулировать safety invariant для raw-pointer/FFI boundary и собрать минимальную C ↔ Rust связку без скрытых build steps.

## `unsafe` — proof obligation

Safe Rust не может выразить все OS/FFI/custom allocator operations. `unsafe` разрешает операции, корректность которых compiler не может доказать.

Главная дисциплина:

```text
safe precondition checks
↓
маленький unsafe region
↓
unsafe operation
↓
восстановленный invariant
↓
safe API result
```

## Raw pointers

```rust
let x = 10i32;
let p: *const i32 = &x;
```

Получить raw pointer можно без dereference. Для чтения:

```rust
// SAFETY: p derived from live aligned x and x lives through this block.
let value = unsafe { *p };
```

Raw pointer не несёт обычных reference guarantees про lifetime/aliasing/non-null.

## Safety comment должен быть проверяемым

Плохо:

```text
SAFETY: seems fine
```

Хорошо:

```text
p points to initialized T allocated by owner X;
length validated <= allocation size;
owner cannot free/reallocate until call returns;
alignment is align_of::<T>().
```

## FFI ABI contract

На boundary нужно отдельно определить:

- symbol name;
- calling convention/ABI;
- integer widths/C-compatible types;
- struct layout (`#[repr(C)]` когда нужно);
- pointer nullability/alignment/lifetime;
- ownership transfer;
- error convention;
- string encoding/termination;
- thread-safety.

## Rust 2024 external declarations

Для курса используем Rust 2024 edition. External block объявляется как unsafe boundary:

```rust
unsafe extern "C" {
    fn add_two(a: i32, b: i32) -> i32;
}
```

Автор declaration отвечает за то, что signature действительно соответствует C symbol. Сам вызов foreign function по умолчанию рассматривается как unsafe, если он не объявлен `safe` с доказанным contract.

## Self-contained C → Rust lab

`add.c`:

```c
int add_two(int a, int b)
{
    return a + b;
}
```

Выбери маленькие test values, для которых C signed addition не overflow.

Собери static library:

```bash
cc -std=c17 -Wall -Wextra -Wpedantic -c add.c -o add.o
ar rcs libtinyffi.a add.o
```

`src/main.rs`:

```rust
unsafe extern "C" {
    fn add_two(a: i32, b: i32) -> i32;
}

fn main() {
    // SAFETY: declaration matches C `int add_two(int,int)` in our ABI lab;
    // chosen inputs cannot overflow C int.
    let value = unsafe { add_two(20, 22) };
    assert_eq!(value, 42);
}
```

Для разового запуска можно передать linker search/lib flags через rustc; для Cargo используй внутренний [`FFI_MINI_REFERENCE.md`](FFI_MINI_REFERENCE.md), где описан `build.rs` без стороннего crate.

## Strings across FFI

Rust `&str`/`String` не являются `char *` C strings. Для null-terminated C text standard library даёт `CString`/`CStr`.

`CString::new` может fail, если внутри bytes есть `\0`: interior null имеет специальный смысл для C string.

Кто освобождает returned `char *` — часть API contract, а не свойство `CString` само по себе.

## Panic/error boundary

Не делай panic обычным FFI error protocol. Переводи expected failures в documented status/result representation на boundary.

## Lab

A. raw pointer observation живого `i32` с SAFETY comment.  
B. собери `libtinyffi.a` и вызови `add_two`.  
C. измени signature намеренно **только текстом**, объясни почему declaration mismatch может привести к UB; не запускай заведомо неверный ABI experiment.

Разбор: [`08-unsafe-raw-pointers-ffi.solution.md`](08-unsafe-raw-pointers-ffi.solution.md).

## Exit check

Для каждого unsafe block назови proof obligation, а для FFI — кто определяет ABI, ownership и error semantics.
