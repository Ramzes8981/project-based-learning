# Разбор 1.4

A. Возврат address local `int`: после return lifetime local закончился, pointer dangling.

B. Caller local struct → read-only function → return до конца caller scope: нормальный short borrow, если function не сохраняет pointer.

C. Global сохраняет pointer на caller local string: если caller storage заканчивается, global pointer становится dangling. Нужно копировать данные в owned storage или гарантировать более длинный lifetime.

D. String literal имеет static storage duration, но попытка модификации literal через pointer приводит к undefined behavior. Правильнее использовать `const char *`.

Главный шаблон проверки:

```text
object создан где?
→ lifetime до какого события?
→ кто хранит pointer?
→ может ли pointer пережить object?
→ кто отвечает за cleanup, если ресурс требует cleanup?
```
