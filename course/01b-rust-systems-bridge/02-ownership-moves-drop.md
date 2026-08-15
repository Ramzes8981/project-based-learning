# 1B.2 — Ownership, move и `Drop`

**Теория:** ~60 мин  
**Упражнение:** ~45 мин  
**Project slice:** ~40 мин  
**С телефона:** да

← [`01-cargo-rust-model.md`](01-cargo-rust-model.md) · → [`03-borrowing-references.md`](03-borrowing-references.md)

## Цель

Связать ручной C ownership contract с Rust ownership rules: один owner value, move semantics и deterministic cleanup через `Drop`.

## C-проблема, которую мы уже видели

В C:

```c
char *p = malloc(...);
```

тип `char *` не говорит compiler:

- кто owner;
- кто должен `free`;
- можно ли передать ownership;
- какие aliases существуют.

В Rust ownership является частью semantic model языка.

## `String` как owned value

```rust
let s = String::from("hello");
```

`String` владеет heap-backed buffer. Когда owner выходит из scope, вызывается cleanup (`Drop`).

Conceptually:

```text
String value
  owns
    ↓
heap allocation
```

Не нужно вручную писать `free`.

## Move

```rust
let a = String::from("hello");
let b = a;
```

Для `String` ownership **moves** в `b`. Использовать `a` после move нельзя.

Почему compiler запрещает?

Если бы обе переменные считались независимыми owners одного buffer и обе cleanup'или его, возник бы аналог C double free.

Rust делает старый binding недоступным вместо implicit deep copy.

## `Copy`

Простые scalar types вроде `i32` обычно implement `Copy`:

```rust
let a = 5;
let b = a;
println!("{a} {b}");
```

Здесь значение дешёво копируется, ownership resource не требует уникального cleanup.

Не пытайся запоминать список `Copy`; смотри semantic: type с resource ownership/`Drop` обычно не должен иметь trivially duplicated ownership.

## `Clone`

Если нужен explicit duplicate owned data:

```rust
let a = String::from("hello");
let b = a.clone();
```

Теперь две независимые `String` allocations/owners.

`clone()` может быть дорогой операцией. Явность — плюс: code review видит, где попросили duplication.

## Function ownership

```rust
fn consume(s: String) {
    println!("{s}");
}

let s = String::from("x");
consume(s);
// s moved
```

Function parameter by value принимает ownership.

Можно вернуть ownership обратно, но обычно для временного доступа лучше borrow — следующий урок.

## `Drop`

Types могут выполнять cleanup при завершении lifetime owner value.

RAII-модель:

```text
resource acquisition tied to object construction
resource release tied to Drop/end of lifetime
```

Это работает не только для memory: files, locks, sockets wrappers тоже могут cleanup через destructors/Drop guards.

## Causal questions

1. Как move предотвращает класс double-free bugs?
2. Почему `clone()` не эквивалентен move?
3. Почему `i32` удобно Copy, а `String` — нет?
4. Какие C ownership comments становятся compiler-enforced в Rust, а какие нет?

## Упражнение

Создай последовательность с `String`:

1. `a` owns string;
2. move в `b`;
3. попробуй использовать `a`, прочитай error;
4. измени программу так, чтобы нужны были две независимые strings через `clone`;
5. передай одну `String` by value в function и объясни ownership после call.

Разбор: [`02-ownership-moves-drop.solution.md`](02-ownership-moves-drop.solution.md).

## Project slice

В Rust MiniKV реши ownership policy:

- store owns keys/values как `String`;
- insertion принимает ownership или borrowed input и копирует?

Пока только задокументируй два варианта и выбери один. В следующем уроке borrow model позволит сформулировать API лучше.

## Exit check

Сравни:

```text
C: malloc pointer + ownership convention + free
Rust: owned value + move rules + Drop
```

Не говори «Rust не имеет heap» — `String`/`Vec` активно используют heap, просто cleanup управляется иначе.
