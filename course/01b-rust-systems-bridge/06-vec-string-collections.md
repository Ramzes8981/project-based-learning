# 1B.6 — `Vec`, `String`, iteration и idiomatic ownership

**Теория:** ~55 мин  
**Упражнение:** ~50 мин  
**Project slice:** ~2–4 часа  
**С телефона:** теория — да

← [`05-option-result-errors.md`](05-option-result-errors.md) · → [`07-text-bytes-unicode-utf8.md`](07-text-bytes-unicode-utf8.md)

## Цель

Использовать standard collections осознанно и увидеть связь с C Vector, который уже реализован вручную.

## `Vec<T>`

`Vec<T>` conceptually хранит:

```text
pointer to allocation
length
capacity
```

Rust encapsulates unsafe allocation machinery внутри standard library и exposes safe API при соблюдении её invariants.

```rust
let mut v = Vec::new();
v.push(10);
v.push(20);
```

`v[index]` может panic при invalid index; `v.get(index)` возвращает `Option<&T>`. Выбор — часть error contract.

## Reallocation всё ещё существует

`Vec::push` может reallocate buffer. Borrow checker защищает references от использования через mutation, которая потенциально invalidates их.

## `String`

`String` — owned growable UTF-8 bytes с string-specific invariants. Это не `Vec<char>`: code points и UTF-8 bytes — разные уровни. Следующий урок разбирает это отдельно.

Для binary protocols используй `Vec<u8>`/`&[u8]`.

## Iteration ownership modes

```rust
for x in &v      // shared borrow items
for x in &mut v  // mutable borrow items
for x in v       // consume collection into iteration
```

Осознанно различай `iter`, `iter_mut`, `into_iter` и receiver ownership.

## Struct methods

```rust
struct Store {
    entries: Vec<Entry>,
}

impl Store {
    fn len(&self) -> usize {
        self.entries.len()
    }
}
```

`&self` — shared borrow, `&mut self` — exclusive mutable borrow, `self` — ownership-consuming receiver.

## Упражнение

Создай `Inventory` с `Vec<Item>`: add, find borrowed item, read-only aggregate, remove по документированной semantics. Добавь tests.

Разбор: [`06-vec-string-collections.solution.md`](06-vec-string-collections.solution.md).

## Project slice

Заверши Rust MiniKV basic implementation с `Vec<Entry>`; `HashMap` не нужен. README сравнивает C/Rust cleanup, borrowed lookup, errors, mutation/invalidation.

## Exit check

Rust `Vec` не убрал realloc: он спрятал memory invariants за safe API и borrow rules.
