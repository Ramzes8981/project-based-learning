# 1B.3 — Borrowing: `&T` и `&mut T`

**Теория:** ~65 мин  
**Упражнение:** ~50 мин  
**Project slice:** ~60 мин  
**С телефона:** да

← [`02-ownership-moves-drop.md`](02-ownership-moves-drop.md) · → [`04-lifetimes-slices.md`](04-lifetimes-slices.md)

## Цель

Понять Rust borrowing как compiler-enforced правило aliasing/mutation, а не как «ссылки похожие на pointers».

## Shared borrow

```rust
fn len(s: &String) -> usize {
    s.len()
}
```

`&String` — shared reference. Function получает временный доступ и не становится owner.

После call original owner продолжает использовать `String`.

Чаще API лучше принимать `&str`, а не `&String`; к slices перейдём дальше.

## Mutable borrow

```rust
fn append_marker(s: &mut String) {
    s.push('!');
}
```

`&mut` даёт exclusive mutable access на время borrow.

## Главное правило aliasing

В safe Rust в один момент для одного region/value разрешено концептуально:

```text
много shared references (&T)
ИЛИ
одна mutable reference (&mut T)
```

Не одновременно shared readers + mutable writer к тому же state.

Это предотвращает большой класс iterator invalidation/data-race-like alias bugs ещё в single-threaded code.

## Почему это связано с C

В C:

```c
int *a = &x;
int *b = &x;
```

compiler обычно не запрещает менять `x` через один alias, пока другой code считает его стабильным. Нужно manually maintain invariants.

Rust делает aliasing discipline частью type/borrow checking.

## Borrow scope

Современный Rust использует non-lexical lifetimes: borrow часто заканчивается после последнего использования reference, а не обязательно в конце всего `{}` block.

```rust
let mut s = String::from("x");
let r = &s;
println!("{r}");
s.push('!'); // shared borrow уже больше не используется
```

## Reborrow

`&mut T` можно временно reborrow для вызова функции, после чего original mutable reference снова может использоваться при корректных lifetimes.

Не нужно рассматривать `&mut` как freely copyable raw address.

## Causal questions

1. Почему shared borrow не передаёт ownership?
2. Почему Rust запрещает `&mut` одновременно с active `&` к тому же state?
3. Как это связано с iterator invalidation?
4. Почему borrow checker не «мешает mutation», а требует доказать exclusive access?

## Упражнение

Создай `Vec<i32>`.

1. Возьми shared reference на первый element и используй его.
2. Попробуй `push` в vector до последнего использования reference — прочитай compiler error.
3. Перестрой code так, чтобы borrow закончился до `push`.
4. Напиши function `increment_all(&mut [i32])` позже через slice syntax (можно пока `&mut Vec<i32>`), которая изменяет collection без ownership transfer.

Разбор: [`03-borrowing-references.solution.md`](03-borrowing-references.solution.md).

## Project slice

Спроектируй Rust MiniKV API:

```text
set: нужна mutation Store -> &mut self
get: только чтение -> &self
```

Не копируй exact method signatures из solution. Сначала определи:

- принимает ли `set` owned `String` или `&str`;
- что возвращает `get`: cloned `String` или borrowed `&str`/`&String`;
- как это влияет на lifetime результата.

## Exit check

Объясни, почему `&mut` — это не просто «pointer, через который можно писать», а временное право exclusive access.
