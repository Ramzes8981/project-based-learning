# MiniKV v0 — Public test scenarios

Это известные заранее сценарии. Они не заменяют дополнительные edge cases на review.

## 1. Empty store

После initialization:

- lookup любого key → not found;
- размер/счётчик, если он есть, согласован с пустым состоянием.

## 2. Insert one

```text
SET alpha = one
GET alpha -> one
```

## 3. Multiple keys

Добавь минимум 3 keys в разном порядке и проверь каждый.

## 4. Update

```text
SET alpha = one
SET alpha = two
GET alpha -> two
```

Проверь, что логическое число записей не увеличилось из-за update.

## 5. Missing key

После добавления нескольких записей `GET missing` должен вернуть явный not-found результат без изменения store.

## 6. Full capacity

Заполни все slots, сохрани snapshot нескольких existing values, затем попробуй добавить новый key.

Проверь:

- операция сообщает full;
- старые значения не изменились.

## 7. Key boundaries

Проверь:

- пустой key согласно выбранному контракту;
- key максимально разрешённой длины;
- key на один символ длиннее лимита.

## 8. Value boundaries

То же для value.

## 9. Duplicate-looking strings

Создай два отдельных char arrays с одинаковым текстом и убедись, что lookup сравнивает **содержимое**, а не identity/address.

## 10. Transfer feature

Добавь минимум 2 проверки для выбранного расширения.

## Review-only edge cases

Преподаватель может предложить дополнительные случаи, которых здесь нет.
