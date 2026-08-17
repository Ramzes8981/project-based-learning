# 3.7 — Зачем человеку assembler, если CPU понимает только bits

**Теория:** ~70 мин · **Практика/project:** ~3–5 часов · **С телефона:** теория — да

← [`05-fetch-decode-execute.md`](05-fetch-decode-execute.md) · → [`07-x86-64-abi-bridge.md`](07-x86-64-abi-bridge.md)

## Проблема

Writing raw 16-bit words is error-prone. Humans want mnemonic names and labels:

```text
LOADI R0, 10
loop:
SUB R0, R0, R1
JZ R0, done
JMP loop
```

Need translator from symbolic text to machine-code words — **assembler**.

## Mnemonic

Human name like `ADD` maps to opcode/encoding defined by ISA. Assembler does not invent semantics; it encodes contract.

## Labels create forward-reference problem

`JMP done` may appear before `done:` address known. Common simple solution: two passes.

```text
pass 1: parse lines, assign instruction positions, record labels
pass 2: encode instructions, resolve label operands/offsets
```

Now two-pass assembler arises from actual forward-reference problem rather than academic ritual.

## Parse narrowly

Define exact grammar: comments, commas, brackets, register names, integer syntax, labels. Reject malformed/out-of-range immediate before encoding; never silently truncate value to bit field.

## Round-trip tests

For sample assembly, expected machine words are stable oracle. Also decode encoded word in test helper to verify fields when useful.

## Project slice

Implement Tiny16 assembler separately from emulator. Shared ISA constants/helpers are okay; do not make assembler depend on emulator internal state.

## Exit check

Why are two passes useful for forward labels, and what bug appears if assembler silently masks an immediate that does not fit field?