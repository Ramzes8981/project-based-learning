# 3.4 — Почему машине нужно состояние между шагами

**Теория:** ~65 мин · **Практика:** ~60 мин · **С телефона:** да

← [`02-boolean-logic-alu.md`](02-boolean-logic-alu.md) · → [`04-isa-machine-code.md`](04-isa-machine-code.md)

## Проблема

Program is sequence. To execute step 2, machine must remember results and where it is in sequence. Pure combinational logic forgets immediately when inputs change.

## State

A **stateful** element retains information across steps/clocks until updated.

CPU exposes small fast named storage locations called **registers**. A special register/state field tracks next instruction location — program counter (PC) concept.

```text
state before step
  registers
  PC
  memory
↓ instruction transition
state after step
```

This “state transition” model is more useful than memorizing block diagrams.

## Registers vs memory

Registers are few CPU-visible fast state slots. Main memory stores far more data/instructions and is addressed differently. Exact cache hierarchy comes later.

Do not model register as “tiny RAM cell with address in normal process memory”. It is architectural CPU state named by ISA.

## Clock intuition

Synchronous digital design updates state around clock transitions while combinational logic computes next values between them. Real CPUs pipeline/speculate, but toy machine can use one-instruction-at-a-time model.

## Практика

Given tiny machine state `R0,R1,PC,mem`, manually simulate 5 steps from instruction descriptions and write state after each step.

Разбор: [`03-state-registers-memory.solution.md`](03-state-registers-memory.solution.md).

## Exit check

What state must machine retain to distinguish “same ADD instruction executed now” from “next instruction later”?