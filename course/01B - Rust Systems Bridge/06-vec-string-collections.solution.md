# Разбор 1B.6

Хорошая архитектура exercise:

```text
Inventory owns Vec<Item>
add(&mut self, Item) transfers Item ownership
find(&self, name: &str) returns Option<&Item>
```

Ключевой момент — `find` не должен клонировать Item только ради lookup, если caller достаточно временного read-only borrow.

Если mutation Inventory нужна, пока caller держит `&Item`, compiler может запретить конфликтующую mutation. Это не проблема API, а явная lifetime semantics результата.
