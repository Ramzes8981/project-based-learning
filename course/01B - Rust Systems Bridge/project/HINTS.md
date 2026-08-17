# Rust MiniKV — Hints

## Hint 1

Сначала спроектируй `Entry` и `Store` ownership. Не начинай с lifetimes annotations.

## Hint 2

Для lookup тебе достаточно borrowed input `&str` и iteration по `&self.entries`.

## Hint 3

Если method только читает Store, спроси, почему receiver должен быть `&mut self`.

## Hint 4

Если compiler ругается на borrow, не вставляй `clone()` автоматически. Нарисуй:

```text
кто owner?
какой borrow активен?
какая mutation нужна?
можно ли закончить borrow раньше?
```

## Hint 5

Error constraints и absence — разные ситуации: `Option` и `Result` не обязаны заменять друг друга.
