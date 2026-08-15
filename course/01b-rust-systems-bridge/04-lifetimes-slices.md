# 1B.4 — Lifetimes и slices

**Теория:** ~70 мин  
**Упражнение:** ~50 мин  
**Project slice:** ~45 мин  
**С телефона:** да

← [`03-borrowing-references.md`](03-borrowing-references.md) · → [`05-option-result-errors.md`](05-option-result-errors.md)

## Цель

Понять lifetime как отношение между references и owned data, а slices — как безопасную пару «address region + length».

## Lifetime не равно runtime timer

Lifetime в Rust — часть static reasoning о том, сколько reference может считаться валидной относительно owner data.

Compiler обычно выводит lifetimes сам. Annotation нужна, когда relation между input/output references неоднозначна.

## Dangling C function

В C:

```c
char *bad(void) {
    char local[4] = "abc";
    return local;
}
```

pointer переживает object lifetime.

Rust safe code не позволит вернуть reference на local owned data:

```rust
fn bad() -> &str {
    let s = String::from("abc");
    &s
}
```

такой код не компилируется, потому что `s` будет dropped.

## Lifetime relation

Пример функции, возвращающей один из двух references:

```rust
fn longer<'a>(a: &'a str, b: &'a str) -> &'a str {
    if a.len() >= b.len() { a } else { b }
}
```

`'a` не означает, что inputs живут «одинаково долго» физически. Контракт говорит: returned reference не может использоваться дольше lifetime, совместимого с обоими inputs.

## Lifetime elision

Во многих common signatures annotations не нужны:

```rust
fn first(s: &str) -> &str
```

compiler применяет elision rules.

Не добавляй explicit lifetimes просто «для серьёзности».

## Slice

C API часто передаёт:

```text
T *ptr + size_t len
```

Rust slice:

```rust
&[T]
&mut [T]
```

связывает borrowed region и length в одном type.

String slice:

```rust
&str
```

— borrowed UTF-8 text view.

Важно: индексирование Rust `str` по integer character index не поддерживается, потому что UTF-8 characters имеют variable byte length.

## `String` vs `&str`

- `String` — owned growable UTF-8 buffer;
- `&str` — borrowed view на valid UTF-8 bytes.

Хороший API часто принимает `&str`, если ownership не нужен.

## Slice boundaries

```rust
let s = String::from("hello");
let part = &s[0..2];
```

Для UTF-8 boundaries должны попадать на character boundaries; arbitrary byte split может panic.

Для binary data используй `&[u8]`, а не `&str`.

## Causal questions

1. Почему lifetime annotation не «продлевает жизнь» data?
2. Что slice добавляет к raw pointer сравнению с C?
3. Почему `&str` удобнее `&String` как read-only string parameter?
4. Почему text protocol parsing и binary parsing требуют разных типов/view assumptions?

## Упражнение

Напиши:

```text
first_word(&str) -> &str
```

которая возвращает slice до первого ASCII space или весь input.

Требования:

- empty string;
- no spaces;
- leading space;
- обычная ASCII phrase;
- не создаёт новый `String`.

Разбор: [`04-lifetimes-slices.solution.md`](04-lifetimes-slices.solution.md).

## Project slice

Для Rust MiniKV предпочти:

- input lookup key как `&str`;
- owned storage как `String`;
- return lookup как borrowed view/reference там, где это безопасно и удобно.

Зафиксируй invalidation semantics: если caller держит borrow результата, какие mutations Store compiler не позволит сделать одновременно?

## Exit check

Сравни:

```text
C: const char * + implicit terminator contract
Rust: &str + tracked length + UTF-8 validity + lifetime
```
