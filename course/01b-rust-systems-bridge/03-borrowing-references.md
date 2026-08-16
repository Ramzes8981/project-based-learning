# 1B.3 — Как временно дать доступ, не передавая владение

**Теория:** ~70 мин · **Практика:** ~65 мин · **С телефона:** теория — да

← [`02-ownership-moves-drop.md`](02-ownership-moves-drop.md) · → [`04-lifetimes-slices.md`](04-lifetimes-slices.md)

## Проблема

Function должна прочитать `String`, но caller хочет оставить ownership у себя. Передавать `String` by value означало бы move.

## Borrowing

Rust reference `&T` даёт временный borrowed access:

```rust
fn len_of(s: &String) -> usize {
    s.len()
}
```

Caller остаётся owner.

Чаще API принимает string slice `&str`, если ему нужны только text bytes/text operations, а не конкретный `String` container.

## Shared vs mutable borrow

```rust
&T      // shared borrow
&mut T  // exclusive mutable borrow
```

Ключевой rule в безопасной модели:

```text
many shared references
OR
one active mutable reference
```

Именно active/overlapping access matters; modern borrow checker often ends a borrow at last use, not necessarily lexical block end.

## Почему mutation требует exclusivity

Если один reference меняет object while другой считает его state stable, invariants могут ломаться. Для `Vec`, mutation вроде `push` ещё и способна reallocate storage и invalidates references to elements.

```rust
let mut v = vec![1, 2, 3];
let first = &v[0];
// v.push(4); // may need mutable borrow/reallocation while first is live
println!("{first}");
```

Compiler блокирует unsafe overlap на type/borrow level.

## Практика

Сделай functions:

```rust
fn count_bytes(s: &str) -> usize
fn append_suffix(s: &mut String, suffix: &str)
```

Затем намеренно создай overlapping borrow conflict, предскажи diagnostic и исправь **ownership design**, а не добавлением clone без причины.

Разбор: [`03-borrowing-references.solution.md`](03-borrowing-references.solution.md).

## Exit check

Почему `&mut T` — не просто «reference, через который разрешена запись», а exclusive access contract?