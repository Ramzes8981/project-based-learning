# Tiny16 — Project SPEC

Нужно реализовать два executables/components:

1. assembler: Tiny16 assembly → 16-bit machine words;
2. emulator: machine words → execution согласно `ISA.md`.

## Assembler

- parser ограниченной grammar;
- labels;
- two passes;
- range validation;
- duplicate/unknown labels;
- line-number diagnostics;
- deterministic output format.

## Emulator

- registers/PC/memory state;
- fetch/decode/execute;
- all core opcodes;
- bounds/error handling;
- HALT;
- trace mode.

## No solution skeleton

Структуру C-файлов, structs и function boundaries выбирает ученик.

## Fixtures

Ученик создаёт sample assembly programs. Курс может добавлять review-only machine words/programs для проверки.
