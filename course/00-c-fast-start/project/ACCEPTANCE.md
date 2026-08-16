# MiniKV v0 — Acceptance

## Behavior

- новое `SET` добавляет запись, пока есть место;
- повторный `SET` заменяет значение без создания duplicate record;
- `GET` различает найденное значение и `NOT_FOUND`;
- `DELETE` удаляет только нужную запись;
- после удаления оставшиеся records продолжают корректно находиться;
- попытка добавить запись при отсутствии места возвращает `FULL` и не меняет существующие records;
- слишком длинное имя отклоняется безопасно.

## Code contract

- одна record model через `struct`;
- public declarations отделены от implementation;
- число занятых records хранится явно;
- нет dynamic allocation/hashing;
- input copied only after length/bounds check;
- owned code builds with C17 + `-Wall -Wextra -Wpedantic` без необъяснённых warnings.

## Reproducibility

- `make` builds;
- `make test` returns zero only when scenarios pass;
- `make clean` removes generated files;
- README describes build/run/test and known fixed-size limitation.

## Understanding gate

Ученик способен объяснить, почему `FULL` существует именно в этой версии и какую будущую проблему оно создаёт, не предлагая пока implementation из Module 1.