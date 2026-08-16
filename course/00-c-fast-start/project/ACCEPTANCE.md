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
- никакая операция не полагается на signed overflow;
- нет unexplained compiler warnings.

На этом модуле sanitizers ещё не являются обязательным gate: они вводятся в Module 1 вместе с dynamic memory и memory-debugging workflow.

## Build contract

В project-папке есть созданный учеником `Makefile`.

Работают и задокументированы в [`README.md`](README.md):

```bash
make
make test
make clean
```

Требования:

- warning flags курса используются последовательно;
- `make test` возвращает failure status, если тестовый executable/runner провалился;
- `make clean` удаляет generated artifacts, но не source/spec/docs;
- dependency graph позволяет incremental rebuild и учитывает public headers.

## Tests

`TESTS.md` — **спецификация известных заранее сценариев**, а не готовый test harness.

В своей реализации ученик создаёт автоматические или `assert`-based проверки этих сценариев и подключает их к `make test`.

Обязательны минимум:

- happy path;
- missing key;
- update existing key;
- full capacity;
- key/value boundary cases;
- отдельные buffers с одинаковым string content;
- минимум два теста transfer feature.

На review могут быть предложены дополнительные неизвестные заранее edge cases.

## Design

[`README.md`](README.md) проекта объясняет:

- representation `Entry/Store`;
- capacity и string limits;
- status/error semantics;
- build/test commands;
- почему lookup сейчас `O(n)`;
- что версия пока не умеет.

## Transfer

Есть одна маленькая функция/возможность сверх минимального SPEC и тесты для неё.

## Debugging evidence

В README записан хотя бы один debugging story:

```text
symptom
hypothesis
diagnostic step / evidence
root cause
fix
regression test
```

## Review questions

Перед переходом к Module 1 ученик может объяснить:

1. какой C object владеет fixed storage;
2. где задаются string/capacity limits;
3. почему update existing key не должен увеличивать logical size;
4. что пересобирается после изменения implementation `.c` и public header;
5. почему следующий шаг проекта требует pointers и dynamic memory.
