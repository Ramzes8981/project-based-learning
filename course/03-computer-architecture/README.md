# Module 3 — Computer Architecture & Machine Code

**Цель:** связать C-код с bits, integer/floating representation, logic, CPU state, instruction execution и ABI.

**Оценка:** ~55–72 часов.  
**Core milestone:** Tiny16 assembler + emulator.  
**Optional deep dive:** Nand2Tetris Projects 1–6.

## Уроки

1. [`01-bits-integers-endianness.md`](01-bits-integers-endianness.md)
2. [`01b-floating-point-ieee754.md`](01b-floating-point-ieee754.md) — floating point и IEEE 754.
3. [`02-boolean-logic-alu.md`](02-boolean-logic-alu.md)
4. [`03-state-registers-memory.md`](03-state-registers-memory.md)
5. [`04-isa-machine-code.md`](04-isa-machine-code.md)
6. [`05-fetch-decode-execute.md`](05-fetch-decode-execute.md)
7. [`06-assembler.md`](06-assembler.md)
8. [`07-x86-64-abi-bridge.md`](07-x86-64-abi-bridge.md)
9. [`08-module-checkpoint.md`](08-module-checkpoint.md)

## Проект

[`project/ISA.md`](project/ISA.md) задаёт небольшую учебную ISA. Ты пишешь assembler/emulator сам по [`project/SPEC.md`](project/SPEC.md), ведёшь [`project/README.md`](project/README.md) и проверяешь sample programs из `project/tests/`.

Nand2Tetris остаётся сильным optional hands-on, но обязательная теория и Tiny16 contract находятся внутри репозитория.
