# 3.5 — Fetch → Decode → Execute

**Теория:** ~65 мин  
**Project slice:** ~4–6 часов  
**С телефона:** теория — да

← [`04-isa-machine-code.md`](04-isa-machine-code.md) · → [`06-assembler.md`](06-assembler.md)

## Цель

Построить emulator loop, который явно разделяет machine state, instruction decode и state mutation.

## Architectural state

Tiny16 emulator хранит:

```text
registers
PC
memory
halted/error state
```

## Fetch

```text
instruction = memory/code[PC]
```

Перед fetch проверяется valid PC range согласно machine model.

## Decode

Bit fields извлекаются masks/shifts:

```text
opcode = ...
dst = ...
src = ...
imm = ...
```

Decode не должен случайно менять machine state.

## Execute

На основании decoded instruction:

- read operands;
- compute ALU result;
- update destination/memory/PC;
- handle errors/halt.

## PC policy

Удобная model:

```text
next_pc = PC + 1 by default
branch instruction overrides next_pc
commit next_pc
```

Так branch logic становится явной.

## Invalid instructions

Не превращай unknown opcode в silent no-op. Emulator должен иметь controlled error: адрес, raw word, opcode.

## Trace mode

Для debugging сделай optional trace:

```text
PC=0003 WORD=0x... OP=ADD R0=...
```

Это важнее красивого UI.

## Project slice

Реализуй emulator stages постепенно:

1. machine state init;
2. fetch;
3. decode;
4. `LOADI`;
5. arithmetic;
6. memory load/store;
7. branch;
8. halt/error;
9. trace.

После каждой новой instruction добавляй маленький machine-code test program.

## Causal questions

1. Почему decode лучше отделять от mutation?
2. Что должен делать invalid PC?
3. Почему trace содержит raw word и PC?
4. Где именно branch меняет normal sequential flow?

## Exit check

Вручную пройди 5 instruction steps и сравни с trace emulator.
