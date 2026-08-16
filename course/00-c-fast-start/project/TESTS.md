# MiniKV v0 — test scenarios

Пиши собственный harness. Ниже — semantic oracle, а не готовый test implementation.

1. **empty** — `GET missing` → `NOT_FOUND`.
2. **insert** — `SET a 10`, затем `GET a` → `10`.
3. **replace** — `SET a 10`, `SET a 20`; занята всё ещё одна запись, `GET a` → `20`.
4. **two names** — `a` и `b` не мешают друг другу.
5. **delete existing** — после удаления `a` → `NOT_FOUND`, `b` остаётся.
6. **delete missing** — безопасный status, state не меняется.
7. **full** — заполнить все доступные slots; следующий новый `SET` → `FULL`; старые значения не меняются.
8. **replace while full** — заменить уже существующее имя можно даже когда нового места нет.
9. **name boundary** — максимально допустимое имя работает; имя на один символ длиннее отклоняется.
10. **repeated operations** — несколько insert/update/delete cycles не рассинхронизируют `used`.

Для каждого failure case проверяй не только status, но и **state after failure**.