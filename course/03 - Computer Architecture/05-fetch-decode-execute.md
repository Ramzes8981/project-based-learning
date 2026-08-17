# 3.6 — Как CPU шаг за шагом исполняет machine code

**Теория:** ~75 мин · **Практика/project:** ~2–3 часа · **С телефона:** теория — да

← [`04-isa-machine-code.md`](04-isa-machine-code.md) · → [`06-assembler.md`](06-assembler.md)

## Проблема

We have state and encoded instructions. Need repeated transition rule that turns program bytes into behavior.

## Fetch → decode → execute

Toy single-step model:

```text
FETCH:   instruction = memory[PC]
DECODE:  extract opcode/fields
EXECUTE: compute effects
COMMIT:  update registers/memory/PC
REPEAT
```

Real CPUs overlap/reorder internally but must preserve ISA-observable behavior subject to architecture rules. Tiny16 intentionally executes sequentially.

## PC discipline

Define whether PC counts bytes or instruction words. Tiny16 spec must be explicit. Branch offset must be relative to documented base (e.g. next instruction), not guessed by assembler/emulator independently.

A strong emulator computes candidate target in a wider/checked host type, validates target is within program memory/range, then commits PC. Toy-machine wrap should happen only where ISA explicitly says wrap.

## State transition debugging

Add optional trace:

```text
PC | instruction | decoded op | registers changed | memory changed
```

Trace is observability, not correctness itself, but makes wrong decode/PC update visible.

## Project slice

Implement emulator step for a small subset first: HALT, LOADI, ADD/SUB, then memory, then branches. Test each instruction before full programs.

## Exit check

Why should invalid branch target be detected before changing emulator PC?