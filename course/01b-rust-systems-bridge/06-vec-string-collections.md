# 1B.6 — `Vec`, `String`, iteration и idiomatic ownership

**Теория:** ~55 мин  
**Упражнение:** ~50 мин  
**Project slice:** ~2–4 часа  
**С телефона:** теория — да

← [`05-option-result-errors.md`](05-option-result-errors.md) · → [`07-unsafe-raw-pointers-ffi.md`](07-unsafe-raw-pointers-ffi.md)

## Цель

Использовать standard collections осознанно и увидеть связь с C Vector, который уже реализован вручную.

## `Vec<T>`

`Vec<T>` conceptually хранит те же три идеи, которые ты уже реализовывал:

```text
pointer to allocation
length
capacity
```

Но Rust encapsulates unsafe allocation machinery внутри standard library и exposes safe API при соблюдении её invariants.

```rust
let mut v = Vec::new();
v.push(10);
v.push(20);
```

Методы:

```text
len()
capacity()
push()
pop()
get()
iter()
```

`v[index]` может panic при invalid index; `v.get(index)` возвращает `Option<&T>`.

Выбор показывает error semantics API.

## Reallocation всё ещё существует

Safe Rust не отменяет physical reality. `Vec::push` может reallocate buffer.

Borrow checker защищает references от использования через mutation, которая потенциально invalidates их, как мы уже видели.

## `String`

`String` — owned UTF-8 collection bytes с string-specific invariants.

Это не `Vec<char>`: Unicode scalar values и UTF-8 bytes — разные уровни.

Для byte protocols используй `Vec<u8>`/`&[u8]`.

## Iteration ownership modes

```rust
for x in &v      // borrow items
for x in &mut v  // mutable borrow items
for x in v       // consume/move collection items
```

Очень важно понимать, какой ownership mode вызывает iteration.

Методы:

```text
iter()      -> shared borrows
iter_mut()  -> mutable borrows
into_iter() -> ownership/consuming semantics depending receiver context
```

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

`&self` — shared borrow receiver; `&mut self` — mutable borrow; `self` — consume/move receiver.

Это делает ownership частью public method signature.

## Causal questions

1. Какие invariants `Vec` скрывает внутри safe abstraction?
2. Почему `get()` и indexing имеют разные error contracts?
3. Что происходит с ownership в `for x in v`?
4. Почему `String` не равно `Vec<char>`?

## Упражнение

Создай `Inventory` с `Vec<Item>`.

Методы:

- add (`&mut self`);
- find by name (`&self -> Option<&Item>`);
- total count/value read-only;
- remove по выбранной semantics.

Добавь tests на borrow-friendly API.

Разбор архитектуры: [`06-vec-string-collections.solution.md`](06-vec-string-collections.solution.md).

## Project slice

Заверши Rust MiniKV basic implementation с `Vec<Entry>`. HashMap **не нужен**: цель bridge — ownership API, а hashing уже изучен в C.

Добавь tests и сравнение C/Rust в project README:

```text
allocation/cleanup
borrowed lookup result
error representation
mutation rules
pointer/reference invalidation
```

## Exit check

Сможешь ли ты объяснить, что Rust `Vec` не «убрал realloc», а спрятал unsafe machinery за safe contract?
