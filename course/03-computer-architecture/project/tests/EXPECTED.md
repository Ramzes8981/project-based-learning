# Tiny16 sample program expectations

Формат вывода emulator ты выбираешь сам; этот файл задаёт semantic oracle.

## `add.asm`

After HALT:

```text
R0 = 20
R1 = 22
R2 = 42
```

## `branch.asm`

After HALT:

```text
R0 = 0
R1 = 7
```

`JZ` target must be resolved according to ISA relative-to-next-PC rule.

## `memory.asm`

After HALT:

```text
R0 = 10
R1 = 55
R2 = 55
mem[10] = 55
```

Добавь собственные programs для SUB wrap, negative LOADI, JZ not-taken и invalid/bounds cases.
