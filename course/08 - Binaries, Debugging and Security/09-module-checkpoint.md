# 8.9 — Checkpoint: от ELF byte до остановленного instruction

**Время:** ~4–6 часов · **С телефона:** review — да; project — ПК

← [`08-memory-corruption-mitigations.md`](08-memory-corruption-mitigations.md) · ↑ [`README`](README.md)

## Explain

1. ELF segment vs section;
2. symbol/debug info absence in stripped binary;
3. PIE/ASLR/load bias;
4. tracer/tracee lifecycle and wait states;
5. ptrace permission/environment limitations;
6. `PEEKDATA` `-1` + `errno` rule;
7. tracee address ≠ tracer pointer;
8. x86 `INT3` breakpoint byte preservation;
9. RIP rewind + single-step + reinsert;
10. why SIGTRAP reasons differ;
11. frame-pointer backtrace limitations;
12. DWARF role;
13. mitigations vs source bug.

## Project gate

`minidbg-c` passes project fixtures for launch/continue/registers/memory/breakpoint loop/single-step/limited stack trace and clean target exit.

## Transfer

Choose one: symbol breakpoint resolution for supported PIE layout, memory hexdump with bounds, or breakpoint disable/enable lifecycle. Add failure-path tests first.

## Exit check

Given a symbol name in PIE fixture, you can describe path ELF symbol → mapping/load bias → runtime address → INT3 patch → trap → restored instruction.