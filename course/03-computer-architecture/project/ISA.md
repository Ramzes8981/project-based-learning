# Tiny16 ISA v1

Собственная учебная 16-bit ISA курса. Она специально небольшая, чтобы focus был на encoding/state, а не на огромной instruction manual.

## Machine

- word: 16 bits;
- 8 general registers: `R0..R7`, каждый 16-bit;
- `PC`: 16-bit instruction index/address;
- memory: 65536 words conceptually, но emulator может конфигурировать меньший test size, если documented;
- arithmetic wraps modulo `2^16` на ISA-level.

## Instruction word formats

### R-format

```text
15..12 opcode
11..9  rd
8..6   rs
5..3   rt
2..0   000/reserved
```

### I-format

```text
15..12 opcode
11..9  rd
8..0   imm9
```

`imm9` semantics зависят от instruction: unsigned or signed two's complement according to table.

## Opcodes

```text
0x0 NOP
0x1 ADD   rd, rs, rt
0x2 SUB   rd, rs, rt
0x3 AND   rd, rs, rt
0x4 OR    rd, rs, rt
0x5 XOR   rd, rs, rt
0x6 LOADI rd, imm9       ; sign-extended imm9
0x7 LOAD  rd, [rs]       ; rd = mem[rs]
0x8 STORE rd, [rs]       ; mem[rs] = rd
0x9 JZ    rd, imm9       ; if rd==0 PC = PC + signext(imm9), else next
0xA JMP   imm12 variant  ; see below
0xF HALT
```

## JMP special format

```text
15..12 = 0xA
11..0  = absolute 12-bit code address
```

Это ограничивает assembler-visible `JMP` target диапазоном `0..4095`: assembler обязан отклонять label/address, который не представим в 12 bits. Emulator после decode дополнительно проверяет, что encoded target попадает в configured instruction memory.

## PC semantics

Обычная instruction:

```text
next_pc = PC + 1
```

`JZ` offset считается относительно **next instruction PC** (`PC + 1`).

`JMP` устанавливает absolute target.

`HALT` останавливает machine без дальнейшего fetch.

## Invalid encoding

Unknown opcode или reserved-field violation (если implementation решит проверять strict reserved bits) должен давать controlled emulator error, не UB host program.

## Assembly syntax

```text
label:
MNEMONIC operand, operand
; comment
```

Registers `R0..R7`, integer literals decimal или `0x` hex. Labels разрешены для `JMP/JZ` targets; assembler вычисляет offset/range.
