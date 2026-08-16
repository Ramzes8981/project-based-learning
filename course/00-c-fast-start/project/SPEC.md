# MiniKV v0 — staged SPEC

## Behavior — можно читать с 0.1

Поведение полностью задано в [`README.md`](README.md). Оно важнее выбранных имён функций и файлов.

## Unlocked after 0.3 — операции как функции

Раздели как минимум поиск/чтение/изменение на функции с понятными return results. Конкретные signatures выбери сам и опиши в project README.

Не возвращай «магические» значения, если они могут быть обычным пользовательским value. Для результата операции допустим `enum` status.

## Unlocked after 0.4 — фиксированное число элементов

Используй заранее выделенное конечное место для небольшого числа записей. Отдельно храни:

```text
сколько элементов может поместиться
сколько элементов сейчас занято
```

На этом этапе не требуется термин `capacity`; в коде можешь выбрать понятное имя вроде `max_entries`.

Каждое имя имеет фиксированный максимальный размер. Слишком длинное имя отклоняется до копирования.

## Unlocked after 0.5 — одна запись и несколько файлов

Одна запись объединяет имя и значение в `struct`.

Рекомендуемое разделение responsibility:

```text
store.h   public types/declarations
store.c   operations on records
main.c    CLI/demo only
```

API не должен требовать знания internal array layout от `main.c`.

## Unlocked after 0.6 — reproducible build/test

Нужны:

```text
make
make test
make clean
```

Owned code собирается с:

```text
-std=c17 -Wall -Wextra -Wpedantic
```

без необъяснённых warnings.

## Explicit non-goals

Module 0 запрещает усложнять проект механизмами будущих уроков:

- `malloc/calloc/realloc/free`;
- pointer arithmetic;
- hash table;
- linked list;
- file persistence;
- threads/sockets.

Если фиксированное число записей кажется ограничением — отлично. Именно эта проблема позже создаст естественную причину изучить dynamic allocation.