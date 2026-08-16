# Unix Shell — Hints

## 1. Separate parser from executor

A parser that produces a small command structure is easier to test without forking.

## 2. Draw ownership before close calls

For redirection/pipeline, draw fd topology per process. Then write close list from diagram.

## 3. Child has one job after fork

Setup descriptors/process group, then exec. On failure, report minimally and `_exit`. Never re-enter parent REPL path.

## 4. `cd` clue

Ask which process must retain changed current working directory after command returns.

## 5. Pipeline hang

If consumer waits forever, first inspect **all remaining write-end descriptors**, including parent copies.

## 6. Do not wait too early

Create/fork both pipeline sides before blocking wait. Otherwise pipe capacity can turn ordering bug into deadlock.

## 7. Signal handlers

Set a `volatile sig_atomic_t` flag or perform only explicitly async-signal-safe operation. Move normal logging/state changes outside handler.