# Module 3 — Computer Architecture and Machine Code

**Status:** CORE  
**Estimated effort:** 50–65 hours (~8–10 weeks)  
**Core milestone:** Nand2Tetris Projects 1–6 + LC-3/CHIP-8 style VM/emulator

## Prerequisites

From Modules 0–2:

- bitwise operators and integer representation basics;
- arrays, pointers and structs;
- ability to compile/debug C;
- basic Unix terminal use.

No assembly knowledge is assumed.

## Sources

- **PRIMARY:** Nand2Tetris Part I, Projects 1–6: https://www.nand2tetris.org/
- **REFERENCE:** Dive into Systems — data representation, assembly and architecture chapters.
- **PROJECT REFERENCE:** one of the repository VM/emulator tutorials after the architecture basics are established.

## Outcomes

The learner can:

- convert between binary/hexadecimal and reason about two's complement;
- explain combinational vs sequential logic;
- explain ALU, registers, memory and CPU at a block level;
- trace a fetch/decode/execute cycle;
- read simple assembly;
- connect C functions/variables to registers, stack frames and memory;
- explain the idea of an ABI/calling convention;
- implement a small instruction interpreter/VM.

---

# Unit 3.1 — Data representation

### Learn

- bits, bytes, hexadecimal;
- unsigned binary;
- two's complement signed integers;
- overflow;
- shifts and masks;
- endianness;
- ASCII/byte representation.

### Exercises

- encode/decode representative values;
- predict overflow/shift behavior only where C semantics are well-defined;
- inspect object bytes with a small C program.

### Industry case

A binary protocol writes a 32-bit integer on a little-endian host and another system reads it as network byte order. Diagnose the mismatch and state where conversion belongs.

---

# Unit 3.2 — Boolean logic and combinational hardware

### Learn

- NAND as primitive;
- AND/OR/XOR/NOT;
- multiplexers/demultiplexers;
- half/full adders;
- ALU concept.

### Nand2Tetris

Complete Projects 1–2.

### Self-check

Do not just make supplied tests pass. Be able to explain the truth-table relationship for the components built.

---

# Unit 3.3 — State and memory

### Learn

- clocked state;
- bit/register abstraction;
- RAM hierarchy;
- address selection;
- distinction between storage and combinational computation.

### Nand2Tetris

Complete Project 3.

### Situational question

What would fail if every circuit in a computer were purely combinational and nothing stored state across clock cycles?

---

# Unit 3.4 — Machine language

### Learn

- instruction encoding;
- opcode/operands;
- registers;
- program counter;
- load/store idea;
- control flow;
- assembly as human-readable machine instructions.

### Nand2Tetris

Complete Project 4.

### Practice bridge to the real machine

Compile a tiny C function and inspect generated x86-64 assembly with `objdump`/compiler assembly output. Do not try to master x86 yet; identify:

- function boundary;
- loads/stores;
- arithmetic;
- branch;
- return.

---

# Unit 3.5 — CPU and fetch/decode/execute

### Learn

Trace:

```text
PC -> instruction memory -> decode -> registers/ALU -> memory/writeback -> next PC
```

### Nand2Tetris

Complete Project 5.

### Required explanation

Given one Hack instruction, explain which state can change and why.

---

# Unit 3.6 — Assembler

### Learn

- symbolic vs binary instruction;
- two-pass assembler idea;
- symbol table;
- forward references.

### Nand2Tetris

Complete Project 6.

### Algorithms connection

The assembler's symbol table deliberately revisits the hash-table concept from Module 1.

---

# Unit 3.7 — Real-world stack and ABI basics

Nand2Tetris is intentionally simple; now bridge to common real systems.

### Learn

- x86-64 register families at a high level;
- instruction pointer / stack pointer;
- stack frame concept;
- call / return;
- arguments/return values under the platform ABI;
- caller-saved vs callee-saved concept;
- stack alignment concept;
- debugging symbols vs machine code.

### Exercise

Trace one small C call chain through source → assembly → registers/stack using GDB.

This unit is a prerequisite for the later debugger/security module.

---

# Core milestone — Small VM / Emulator

Choose one course-approved target:

- LC-3 VM tutorial;
- CHIP-8 emulator;
- equivalent small bytecode machine with a defined instruction set.

The course should prefer a target that avoids unnecessary graphics/UI dependencies when the purpose is CPU-state reasoning.

## Required slices

1. memory representation;
2. registers + PC;
3. instruction fetch/decode;
4. arithmetic/logical instructions;
5. load/store;
6. branch/control flow;
7. minimal I/O;
8. tracing/debug mode.

## Transfer feature

Add one debugging/inspection feature not present in the basic walkthrough, e.g. instruction trace, register dump, breakpoint address or execution-step counter.

## Rubric

- known test programs execute correctly;
- invalid opcode/state produces a controlled error;
- learner can trace several instructions by hand;
- implementation clearly separates decode from state mutation;
- README documents instruction set scope and limitations.

---

# Exit gate

Without notes, explain the vertical chain:

```text
C expression -> compiler -> machine instructions -> registers/ALU/memory -> state change
```

and demonstrate the same model inside the course VM.