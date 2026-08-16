# Tiny16 — рабочий README

## Status

## Build

Документируй assembler/emulator executables и команды `make`, `make test`.

## ISA assumptions

Ссылка на [`ISA.md`](ISA.md), плюс любые **implementation choices**, которые спецификация оставляет свободными.

## Assembler design

Lexer/parser representation, two-pass symbol table, range/error handling, output format.

## Emulator design

Registers/PC/memory representation, fetch/decode/execute boundary, HALT/error state, trace mode.

## Invariants

- PC указывает на valid fetch либо machine halted/error;
- register indices validated;
- memory accesses bounded;
- ISA 16-bit arithmetic wraps согласно ISA, но host C code не полагается на signed UB;
- invalid opcode/encoding превращается в controlled error.

## Tests

Используй `TESTS.md` и sample programs в `tests/programs/`. Для каждого program запиши expected final registers/memory/exit state.

## Debugging story

## Performance/limitations

Эмулятор не обязан быть быстрым; correctness/traceability важнее premature optimization.

## Transfer feature

