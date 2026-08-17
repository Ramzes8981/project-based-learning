# 3.9 — Checkpoint: проведи одну инструкцию от bits до state change

**Время:** ~3–5 часов · **С телефона:** review — да; project — ПК

← [`07-x86-64-abi-bridge.md`](07-x86-64-abi-bridge.md) · ↑ [`README`](README.md)

## Explain

1. bit pattern vs interpretation;
2. two's-complement hardware vs C signed-overflow rule;
3. endianness and explicit serialization;
4. floating finite precision/rounding;
5. combinational logic vs state;
6. register/memory/PC;
7. ISA vs machine code;
8. fetch/decode/execute transition;
9. assembler two-pass label reason;
10. ISA vs ABI.

## Tiny16 gate

Assembler + emulator pass [`project/ACCEPTANCE.md`](project/ACCEPTANCE.md), including invalid/bounds cases and sample programs.

## Transfer

Add one instruction to ISA. Before code, update:

```text
semantic behavior
encoding
assembler syntax/range checks
emulator transition
positive + invalid tests
```

## Debug story

Capture one wrong PC/decode/endianness/sign-extension bug from symptom to minimal machine state and regression.

## Exit check

Given one Tiny16 word, you can decode fields, predict state transition and explain how assembler emitted that word.