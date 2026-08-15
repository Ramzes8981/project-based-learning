# 8.4 — Registers и tracee memory

**Теория:** ~80 мин  
**Project slice:** ~4–6 часов  
**С телефона:** да

← [`03-ptrace-debugger-lifecycle.md`](03-ptrace-debugger-lifecycle.md) · → [`05-software-breakpoints.md`](05-software-breakpoints.md)

## Цель

Инспектировать x86-64 register state и safely read/patch tracee words, понимая architecture/errno constraints.

## Register state

Для x86-64 нас интересуют:

```text
RIP instruction pointer
RSP stack pointer
RBP optional frame/base convention
RAX,RBX,RCX,RDX,RSI,RDI,R8..R15
RFLAGS
```

Linux ptrace exposes architecture-specific user register structure/interfaces. Это deliberately non-portable layer.

## RIP

`RIP` указывает architectural current/next instruction position according to stop event semantics. После breakpoint trap особая correction появится Lesson 8.5.

## Read memory

`PTRACE_PEEKDATA`/related request читает machine word at tracee address. Linux не разделяет text/data address spaces для этих requests. citeturn857293search1

Returned `long` может быть `-1` как data. Pattern:

```text
errno = 0
word = ptrace(PEEK..., ...)
if word == -1 && errno != 0 -> error
else word valid
```

## Write memory

`PTRACE_POKEDATA` пишет machine word. Для изменения одного byte debugger обычно:

1. read containing word;
2. modify нужный byte in local copy;
3. write whole word back.

Endianness matters when masking byte positions.

## Memory validation

Debugger может попытаться читать unmapped/protected address → error. `maps` помогает context, но mapping can change; API result remains authority.

## Register command design

Commands:

```text
regs
reg rip
mem ADDRESS
```

Parsing address must detect invalid text/overflow; do not `atoi` arbitrary hex into narrow int.

## Project slice

Добавь:

- `regs` key registers;
- `reg NAME`;
- `mem ADDRESS` word;
- helpful errno errors;
- target fixtures with known global/stack values.

## Exercise

Сравни GDB register values и minidbg at same non-PIE breakpoint/initial stop. Объясни differences due stop location rather than demanding identical arbitrary state.

## Exit check

Почему reading `-1` from PEEK needs errno check?
