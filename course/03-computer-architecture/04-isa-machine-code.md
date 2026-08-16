# 3.5 — Как договориться, что конкретные bits означают конкретную инструкцию

**Теория:** ~75 мин · **Практика:** ~70 мин · **С телефона:** теория — да

← [`03-state-registers-memory.md`](03-state-registers-memory.md) · → [`05-fetch-decode-execute.md`](05-fetch-decode-execute.md)

## Проблема

Memory contains bits. CPU needs deterministic rule: which bits select operation, registers, immediate value or address?

## ISA

**Instruction Set Architecture (ISA)** is contract between software-visible machine code and processor implementation: available instructions, registers, encoding, visible state/behavior.

Tiny16 course ISA is specified in [`project/ISA.md`](project/ISA.md).

## Instruction encoding

Toy fixed-width example:

```text
15          12 11                 0
+-------------+--------------------+
| opcode 4bit | operands/immediate |
+-------------+--------------------+
```

The same 16 bits mean one instruction only because ISA defines field interpretation.

## Machine code

Encoded instruction words/bytes that CPU decodes are **machine code**.

Assembly text is human representation introduced later; it is not what decoder directly executes.

## Signed immediates

If immediate field is signed two's-complement, decoder must sign-extend it to working width correctly. Do not rely on implementation-defined C shifts/casts accidentally reproducing desired target semantics; implement decode with unsigned masks and explicit sign extension logic.

## Illegal encodings

ISA should define behavior: invalid opcode/truncated program/out-of-range memory. Emulator must reject/trap deterministically rather than indexing arbitrary host memory.

## Практика

Using Tiny16 ISA, encode/decode several instructions by hand including negative immediate and branch offset. Verify exact bits with a small helper only after manual prediction.

## Exit check

Why is machine code meaningless without an ISA contract, and why is ISA not identical to one physical CPU implementation?