# 1B.6 — Как знакомые dynamic collections выглядят при compiler-checked ownership

**Теория:** ~65 мин · **Практика/project:** ~90 мин · **С телефона:** теория — да

← [`05-option-result-errors.md`](05-option-result-errors.md) · → [`07-text-bytes-unicode-utf8.md`](07-text-bytes-unicode-utf8.md)

## Vector bridge

C Vector явно хранил `data/len/capacity` и вручную управлял `realloc`. Rust `Vec<T>` инкапсулирует тот же общий класс задачи, но ownership и destruction encoded in type.

```rust
let mut v = Vec::new();
v.push(10);
```

`len()` — logical elements; `capacity()` — storage available before grow. Growth may invalidate references exactly по той же физической причине, что C `realloc`; borrow rules не позволяют safe code держать incompatible reference через mutation.

## `String`

`String` — owned growable UTF-8 text. `&str` — borrowed UTF-8 string slice.

Не путай `String` с arbitrary byte buffer. Для bytes обычно `Vec<u8>` / `&[u8]`.

## HashMap bridge

`std::collections::HashMap<K,V>` владеет inserted keys/values according to operations/types. Lookup может использовать borrowed form when traits support it, например `HashMap<String, V>` обычно читается по `&str` without allocating new `String`.

## Не клонируй key ради каждого GET

Если API lookup принимает borrowed key, unnecessary `to_string()`/`clone()` создаёт лишнюю allocation/copy и маскирует understanding borrowing.

## Project slice

После этого урока можно начать [`project/SPEC.md`](project/SPEC.md): behavior-first map, borrowed lookup, explicit results. Не добавляй FFI/unsafe.

## Практика

Сделай tiny map `String -> i32`, вставь owned keys, выполни lookup по `&str`, update/delete, объясни, кто owns key/value после insert/remove.

Разбор: [`06-vec-string-collections.solution.md`](06-vec-string-collections.solution.md).

## Exit check

Почему `Vec` growth и C `realloc` создают одну и ту же reference-invalidation проблему, хотя Rust чаще ловит её compile-time?