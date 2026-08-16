# 8.5 — Как один byte `INT3` превращается в breakpoint и почему RIP надо откатить

**Теория:** ~105 мин · **Практика/project:** ~5–7 часов · **С телефона:** theory — да

← [`04-registers-memory.md`](04-registers-memory.md) · → [`06-single-step-stack-unwinding.md`](06-single-step-stack-unwinding.md)

## Проблема

Debugger wants process stop when execution reaches chosen instruction address.

On x86, one common **software breakpoint** replaces first byte of instruction with `INT3` opcode byte `0xCC`, which triggers trap.

## Install breakpoint

For address `A`:

```text
read word containing A
save original byte at A
replace only that byte with 0xCC
write word back preserving neighbors
mark breakpoint enabled
```

Do not assume address is word-aligned or overwrite entire word with breakpoint pattern.

## Trap position

When CPU executes `INT3`, reported RIP in stopped tracee normally points **after** one-byte breakpoint instruction. To execute original instruction:

```text
tracee stops with RIP = A + 1
→ restore original byte at A
→ set RIP = A
→ single-step original instruction
→ wait for step trap
→ reinsert 0xCC at A
→ continue
```

If you simply restore byte and continue with RIP=A+1, original instruction is skipped.

## Distinguish trap reasons

`SIGTRAP` may arise from breakpoint, single-step, exec/ptrace events, etc. Debugger must use its own breakpoint table + current RIP/event info; not every SIGTRAP means “our breakpoint hit”.

## Breakpoint ownership

Store:

```text
runtime address
original byte
enabled state
optional source/symbol label
```

Duplicate breakpoint at same address needs explicit policy. Remove breakpoint restores byte only if tracee state/address still corresponds and breakpoint enabled.

## PIE address

User may specify symbol; debugger resolves ELF coordinate to runtime address using supported load-bias logic from 8.2 before patch.

## Project stage

Implement set/hit/continue/reinsert/remove on controlled non-self-modifying fixture. Tests include adjacent bytes preserved and repeated hits in loop.

## Exit check

Why does correct continue-from-breakpoint require a single-step cycle rather than simply replacing `0xCC` with original byte and issuing CONT?