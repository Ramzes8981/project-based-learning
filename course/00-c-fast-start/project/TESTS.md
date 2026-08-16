# MiniKV v0 — Public test scenarios

Это **известные заранее сценарии**, а не готовый test harness. Тестовый C-код пишешь ты и подключаешь его к `make test`.

Сценарии определяют observable behavior и не требуют конкретных имён функций/struct fields.

## 0. Build/test contract

Перед функциональными cases проверь:

```bash
make
make test
make clean
```

Ожидания:

- build без unexplained warnings;
- failing assertion/test приводит к ненулевому exit status и провалу `make test`;
- после `make clean` source, README и project specs остаются на месте.

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

Проверь согласно своему documented contract:

- пустой key;
- key максимально разрешённой логической длины;
- key на один символ длиннее лимита.

Если key хранится как C string в buffer capacity `C`, помни: maximum logical length должна оставлять место для `\0`.

## 8. Value boundaries

То же для value.

## 9. Duplicate-looking strings

Создай два отдельных `char` arrays с одинаковым текстом и убедись, что lookup сравнивает **содержимое**, а не identity/address.

## 10. State preservation after failure

Для минимум двух rejected operations проверь, что ранее сохранённые entries не изменились.

Подходящие случаи:

- insert в full store;
- слишком длинный key/value.

## 11. Transfer feature

Добавь минимум 2 проверки для выбранного расширения:

- обычный happy path;
- boundary/error case.

## Review-only edge cases

На review преподаватель может предложить дополнительные случаи, которых здесь нет. Реализация должна соответствовать documented contract, а не только известным test values.
