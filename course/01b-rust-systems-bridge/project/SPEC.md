# Rust MiniKV — SPEC

Bridge-проект переносит **поведение** MiniKV в idiomatic Rust, но не требует повторной реализации hash table.

## Storage

Используй стандартный `Vec<Entry>` для хранения небольшого числа entries. Линейный lookup допустим и намерен.

Цель проекта — ownership/API/error design.

## Entry

Каждая entry владеет key/value как `String` или другим осмысленным owned representation.

## Required operations

- create empty Store;
- set/insert/update;
- get;
- delete или другая небольшая transfer feature;
- len/is_empty;
- tests.

## API goals

- read-only methods используют `&self`;
- mutation — `&mut self`;
- lookup input принимает borrowed text (`&str`) без обязательной allocation;
- missing lookup моделируется `Option`;
- constraint/input errors — `Result` с собственным error enum;
- lookup result по возможности borrowed, а не clone по умолчанию.

## Constraints

Можно сохранить maximum key/value length из C MiniKV как domain limits, даже несмотря на growable `String`. Это полезно для error-contract comparison.

## Forbidden shortcuts

- не использовать `HashMap` как способ скрыть цель bridge;
- не `clone()` всё подряд, чтобы «успокоить borrow checker»;
- не использовать `unsafe` в основной Store implementation без отдельного обоснования.
