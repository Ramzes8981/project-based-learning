# 8.7 — DWARF и source-level debugging

**Теория:** ~80 мин  
**Guided lab:** ~60–90 мин  
**С телефона:** да

← [`06-single-step-stack-unwinding.md`](06-single-step-stack-unwinding.md) · → [`08-memory-corruption-mitigations.md`](08-memory-corruption-mitigations.md)

## Цель

Понять, какой дополнительный information layer нужен, чтобы перейти от addresses/registers к source lines/variables.

## Machine debugger уже работает без source

Breakpoints by address, registers, memory и step требуют process/architecture interfaces, но не source code.

Чтобы выполнить:

```text
break main.c:42
print local_variable
backtrace with function names/source lines
```

debugger должен связать machine state с source model.

## Debug information

Compiler with `-g` emits sections containing structured debug metadata. В Linux toolchains common format DWARF.

DWARF conceptually describes:

- compilation units;
- functions/scopes;
- types;
- variables and locations;
- source line program;
- call-frame/unwind information.

## Addresses may be ranges/expressions

Optimized variable может:

- live in register only часть function;
- move to stack;
- be optimized out;
- require expression to compute location.

Поэтому source variable ≠ fixed address for whole lifetime.

## Line table

Line program maps machine address ranges to source file/line. One source line may correspond to multiple instruction ranges; several source expressions may share line.

Stepping by source line therefore is higher-level policy over instruction addresses.

## DIE idea

Debugging Information Entries form typed tree of scopes/entities with attributes/references. Core не пишет DWARF parser.

## Guided lab

Используй existing tools:

```text
readelf --debug-dump=info
readelf --debug-dump=decodedline
GDB info line / disassemble
```

На маленьком C program найди:

- function metadata;
- line address range;
- one variable/type.

Сравни `-O0 -g` и `-O2 -g`.

## Why no core parser

Полный DWARF parser — отдельный significant project + format complexity. Он не нужен, чтобы проверить debugger fundamentals. Внешняя library/source-level support остаётся Stretch.

## Exit check

Объясни, почему ELF symbols недостаточны для reliable `print local_var at line 42`.
