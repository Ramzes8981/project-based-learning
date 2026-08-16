# 8.4 — Registers и tracee memory

**Теория:** ~85 мин  
**Project slice:** ~4–6 часов  
**С телефона:** да

← [`03-ptrace-debugger-lifecycle.md`](03-ptrace-debugger-lifecycle.md) · → [`05-software-breakpoints.md`](05-software-breakpoints.md)

## Цель

Инспектировать x86-64 register state и read/patch tracee memory, учитывая architecture-specific layout и ptrace error semantics.

## Registers

Для x86-64 core:

```text
RIP  instruction pointer
RSP  stack pointer
RBP  frame/base register by convention, not guaranteed frame chain
RAX..R15 general-purpose
RFLAGS
```

Linux exposes architecture-specific register interfaces such as `PTRACE_GETREGS` on x86 and more general register-set interfaces. Course implementation may use x86-64 `struct user_regs_struct`; это deliberate non-portability.

## Memory peek

`PTRACE_PEEKDATA`/`PTRACE_PEEKTEXT` on Linux read a machine word from tracee address; Linux does not maintain a separate text/data address space for these two requests.

Because returned word can legitimately equal all-one-bits/`-1`, always clear/check `errno` as described in Lesson 8.3.

## Memory poke

`PTRACE_POKEDATA` writes a machine word. To patch one byte without losing neighbors:

```text
read containing word
modify selected byte in local unsigned representation
write whole word back
```

Address alignment/endianness and which word contains requested byte must be explicit. Simplest breakpoint course path uses the exact target address as ptrace word address and modifies its low-order byte on x86 little-endian; document this architecture assumption.

## Address parsing

Command `mem 0x...` parses an address-sized unsigned integer. Validate:

- complete string consumed;
- no negative input if grammar forbids;
- conversion not overflowed;
- value representable as pointer/address type used by ptrace wrapper.

`atoi` into `int` is not address parser.

## Project slice

Add `regs`, `reg NAME`, `mem ADDRESS`; use targets with known globals and stack computation. Compare with GDB only at equivalent stop locations.

## Exit check

Why can `PTRACE_PEEKDATA` return `-1` without failure, and how does `errno` distinguish the case?
