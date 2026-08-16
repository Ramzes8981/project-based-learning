# Tiny16 — public test scenarios

## Assembler

1. empty/comment-only source;
2. one instruction per core opcode;
3. decimal/hex immediates;
4. labels forward/backward;
5. duplicate label rejected;
6. unknown label rejected;
7. register/immediate out of range rejected;
8. malformed operand count rejected;
9. deterministic machine-word output.

## Emulator

1. NOP/HALT;
2. ADD/SUB wrap according to 16-bit ISA;
3. bitwise ops;
4. LOADI sign extension;
5. LOAD/STORE bounds;
6. JZ taken/not taken and relative-to-next-PC semantics;
7. JMP absolute range;
8. unknown opcode controlled error;
9. step limit prevents accidental infinite-test hang;
10. trace state matches executed instructions.

## Integration

Assemble every program in `tests/programs/`, run emulator, compare expected final state documented in `tests/EXPECTED.md`.
