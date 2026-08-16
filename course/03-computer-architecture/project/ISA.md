# Tiny16 ISA — normative contract

Tiny16 is a course toy ISA. Emulator and assembler must implement **this file**, not infer behavior from sample code.

## Machine state

```text
8 general registers R0..R7, each 16-bit unsigned storage
PC: index of next 16-bit instruction word
memory: 4096 words of 16 bits
halted flag
```

Arithmetic instructions wrap modulo `2^16` because this is explicit Tiny16 ISA semantics. Host C code must implement wrap through unsigned fixed-width operations, not signed overflow.

## Instruction word

16 bits. Top 4 bits opcode. Remaining fields depend on opcode.

## Opcodes

```text
0x0 HALT
0x1 LOADI rd, imm9
0x2 ADD   rd, ra, rb
0x3 SUB   rd, ra, rb
0x4 LOAD  rd, [ra]
0x5 STORE rs, [ra]
0x6 JZ    rs, rel9
0x7 JMP   addr12
```

Unused encodings/opcodes are invalid and emulator must fail/trap deterministically.

## Fields

### LOADI

```text
[15:12]=1 [11:9]=rd [8:0]=signed imm9
```

`imm9` representable range: **-256..255**. Emulator sign-extends then stores low 16-bit two's-complement value in register.

### ADD/SUB

```text
[15:12]=op [11:9]=rd [8:6]=ra [5:3]=rb [2:0]=0
```

Reserved low bits must be zero; assembler emits zero, emulator may reject nonzero reserved bits according to project strict-mode policy (policy must be consistent/tests explicit).

### LOAD/STORE

Address comes from low 12 bits of address register value. Canonical policy: if full register value is >= 4096, treat as invalid address rather than silently masking. This makes bounds failure visible. `LOAD rd,[ra]`; `STORE rs,[ra]`.

### JZ

```text
[15:12]=6 [11:9]=rs [8:0]=signed rel9
```

If `R[rs] == 0`, target is:

```text
next_pc + sign_extend(rel9)
```

where `next_pc` is PC after fetching current instruction. `rel9` range **-256..255**.

Assembler must reject label offset outside range. Emulator computes target in a wider signed host type, validates `0 <= target < program_word_count` (or documented executable memory limit if program model differs), then commits PC. Host signed overflow must not be possible.

### JMP

```text
[15:12]=7 [11:0]=absolute addr12
```

Encoded field range **0..4095**. Assembler rejects label/address outside field. Emulator also validates target against loaded program/executable memory policy before commit.

## Fetch rule

Before fetch, PC must identify a loaded executable instruction word. Fetch obtains word at PC, then default `next_pc = PC + 1` using checked host arithmetic. Branch/JMP may replace next PC after target validation.

## HALT

Sets halted state. Re-stepping halted emulator is either no-op/status or explicit error; choose one documented API contract.

## Errors

At minimum deterministic error for:

- fetch outside loaded program;
- invalid opcode/encoding according to strict policy;
- invalid memory address;
- invalid jump target.

No invalid guest program may index host arrays out of bounds.