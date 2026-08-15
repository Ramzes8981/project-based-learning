# Vector in C — SPEC

Реализуй growable contiguous collection одного выбранного типа (для core удобно `int`).

## Required state

Conceptually vector должен хранить:

- pointer на allocation;
- logical `size`;
- `capacity`.

Точные имена/struct design выбираешь сам.

## Required operations

- init/create;
- destroy;
- get;
- set;
- push;
- pop или эквивалентная маленькая transfer operation;
- reserve/grow internal capacity.

## Contracts

- out-of-range access обрабатывается явно;
- allocation failure не теряет old data;
- `size <= capacity` всегда;
- destroy освобождает owned storage ровно один раз;
- growth multiplication проверяется на overflow.

## Forbidden shortcut

Не использовать готовый dynamic-array library/container. Цель — реализовать механизм самостоятельно.
