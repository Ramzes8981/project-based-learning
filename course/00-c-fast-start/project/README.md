# MiniKV v0 — рабочий README проекта

Этот файл заполняет **ученик по мере разработки**. Курс задаёт вопросы и критерии, но не принимает design decisions за тебя.

Перед началом прочитай:

- [`SPEC.md`](SPEC.md) — обязательное поведение;
- [`TESTS.md`](TESTS.md) — известные заранее сценарии;
- [`ACCEPTANCE.md`](ACCEPTANCE.md) — критерии завершения;
- [`HINTS.md`](HINTS.md) — подсказки, открывать по необходимости.

## Status

Запиши текущий этап проекта своими словами.

Пример формата статуса, не готовый ответ:

```text
Contract defined / storage started / tests incomplete / ready for review
```

## Product limits

Зафиксируй выбранные тобой значения:

```text
maximum entries:
maximum key length:
maximum value length:
empty key policy:
empty value policy:
```

Не меняй лимиты посреди теста только ради прохождения конкретного case. Если контракт меняется — обнови README и tests осознанно.

## Operations and error semantics

Опиши поведение:

```text
SET existing key:
SET new key:
SET when full:
GET existing key:
GET missing key:
invalid/too-long input:
```

Не обязательно фиксировать точные C signatures до соответствующего урока.

## Representation

После появления кода опиши собственную структуру данных:

```text
Entry:
Store:
how an empty slot is represented:
how active entry count is represented, if present:
```

## Build

После урока про Make запиши команды, которыми реально собирается проект:

```text
make
make test
make clean
```

Если выбрал другие targets — задокументируй их.

## Tests

Запиши:

- где находятся твои tests;
- как они запускаются;
- какие boundary/error cases уже покрыты;
- какие известные scenarios из `TESTS.md` ещё не проверены.

## Complexity

Для v0 объясни своими словами, почему lookup имеет линейный worst-case growth относительно числа занятых entries.

## Known limitations

Версия v0 намеренно ограничена. Запиши реальные ограничения своей реализации, а не общий список из SPEC.

## Transfer feature

Перед Module 1 выбери одно небольшое расширение сверх минимального SPEC и опиши:

```text
feature:
why it was chosen:
new edge cases:
```

## Debugging story

Минимум один раз за модуль зафиксируй реальную или специально внесённую ошибку:

```text
Symptom:
Hypothesis:
Diagnostic step / evidence:
Root cause:
Fix:
Regression test:
```

Цель — тренировать воспроизводимый debugging process, а не составлять отчёт ради отчёта.
