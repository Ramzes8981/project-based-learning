# Vector in C — рабочий milestone

Проект начинается **после 1.7**. До dynamic allocation/capacity он не должен быть prerequisite.

## Поведение

Vector хранит последовательность `int`:

- начинается пустым;
- `push` добавляет значение в конец;
- `get` читает существующий element;
- при необходимости internal storage растёт;
- allocation failure не портит старое содержимое;
- `destroy` освобождает owned resource и оставляет object в безопасном empty state.

## Документы

- [`SPEC.md`](SPEC.md) — technical contract;
- [`ACCEPTANCE.md`](ACCEPTANCE.md) — gate;
- [`TESTS.md`](TESTS.md) — semantic scenarios;
- [`HINTS.md`](HINTS.md) — hints без full solution.

Student writes implementation. Полного milestone solution в репозитории нет.