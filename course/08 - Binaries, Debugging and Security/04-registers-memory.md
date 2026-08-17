# 8.4 — Как прочитать registers/memory, не путая `-1` с ptrace error

**Теория:** ~95 мин · **Практика/project:** ~3–5 часов · **С телефона:** theory — да

← [`03-ptrace-debugger-lifecycle.md`](03-ptrace-debugger-lifecycle.md) · → [`05-software-breakpoints.md`](05-software-breakpoints.md)

## Problem

Once tracee is stopped, debugger needs CPU state and process memory.

## Registers

On Linux x86-64, `PTRACE_GETREGS`/`SETREGS` commonly expose general-purpose register set in target-specific structure such as `user_regs_struct`.

This is not portable POSIX debugger API. Course project pins Linux x86-64 and checks build target.

Important fields include RIP/RSP/RBP/general registers/flags. Read them according to ABI/ISA meanings learned earlier.

## Memory read with `PTRACE_PEEKDATA`

Classic ptrace reads machine-word-sized data and returns a `long`. Problem: valid memory word can itself equal `-1` bits, while API also reports error with `-1` and sets `errno`.

Correct pattern:

```c
errno = 0;
long word = ptrace(PTRACE_PEEKDATA, pid, addr, 0);
if (word == -1 && errno != 0) {
    /* actual error */
}
```

Never test only `word == -1`.

## Unaligned/arbitrary-length reads

A helper that reads bytes across machine-word boundaries must:

- avoid overflow in `addr + len` arithmetic;
- read covering words;
- copy only requested bytes;
- not assume tracee address is aligned;
- stop/report partial failure deterministically.

Pointer in tracer and numeric virtual address in tracee are different address spaces. Never dereference tracee address directly in tracer.

## Writing memory

`PTRACE_POKEDATA` writes word. To modify one byte, debugger must read original word, change targeted byte, write full word, while preserving neighbors. This creates breakpoint lesson.

## Project stage

Implement register dump + exact byte-range memory read on stopped fixture. Add test where read word bits equal all ones to ensure errno handling doesn't misclassify valid data.

## Exit check

Why must `errno` be reset before `PTRACE_PEEKDATA`, and why can tracer not simply cast tracee RIP to pointer and dereference it?