# MiniKV v0 — Acceptance criteria

Проект считается готовым к Module 1, если выполнены все пункты.

## Correctness

- пустой store создаётся в валидном состоянии;
- можно добавить минимум несколько разных keys;
- `GET` возвращает правильные values;
- повторный `SET` существующего key обновляет value, а не создаёт логический duplicate;
- отсутствующий key обрабатывается явно;
- при заполненном store новый key не повреждает существующие данные;
- слишком длинный key/value отклоняется или обрабатывается согласно документированному контракту.

## Safety baseline

- нет чтения/записи за fixed buffers по известным тестам;
- strings остаются null-terminated там, где API обещает C string;
- нет unexplained compiler warnings.

## Tests

Есть автоматические или `assert`-based проверки сценариев из `TESTS.md`.

## Design

README проекта объясняет:

- representation `Entry/Store`;
- capacity и string limits;
- status/error semantics;
- почему lookup сейчас `O(n)`;
- что версия пока не умеет.

## Transfer

Есть одна маленькая функция/возможность сверх минимального SPEC.

## Debugging evidence

В README записан хотя бы один debugging story: симптом → гипотеза → проверка → причина.
