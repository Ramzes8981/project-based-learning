# 3.3 — Как из простых логических операций получается arithmetic circuit

**Теория:** ~65 мин · **Практика:** ~60 мин · **С телефона:** да

← [`01b-floating-point-ieee754.md`](01b-floating-point-ieee754.md) · → [`03-state-registers-memory.md`](03-state-registers-memory.md)

## Проблема

Bits have values 0/1. How can hardware add numbers, compare values or choose one path?

## Boolean operations

At abstract logic level:

```text
AND: 1 only when both inputs 1
OR:  1 when any input 1
XOR: 1 when inputs differ
NOT: flips bit
```

Truth tables fully describe one-bit combinational operation.

## From XOR/AND to addition

Half-adder:

```text
sum   = a XOR b
carry = a AND b
```

Full adder includes incoming carry. Chaining bit positions builds multi-bit addition circuit.

We are not designing transistor implementation; we are seeing how arithmetic emerges from Boolean relationships.

## ALU

**Arithmetic Logic Unit (ALU)** is CPU component performing arithmetic/logic selected by control signals.

```text
inputs A/B
+ operation selector
→ result + flags
```

Flags may encode zero/carry/sign/overflow according to ISA. Do not map them directly to C semantics without instruction/ABI context.

## Combinational means no memory of past

Same current inputs → same current output. Circuit alone does not remember previous result. That missing property creates next lesson.

## Практика

Build truth table for 1-bit full adder, then manually add two 4-bit unsigned numbers carrying between positions.

Разбор: [`02-boolean-logic-alu.solution.md`](02-boolean-logic-alu.solution.md).

## Exit check

Why can combinational ALU compute a result but not by itself execute a sequence of instructions over time?