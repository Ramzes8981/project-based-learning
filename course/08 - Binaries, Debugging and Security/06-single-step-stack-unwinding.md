# 8.6 — Как выполнить одну instruction и восстановить call chain в ограниченной модели

**Теория:** ~100 мин · **Практика/project:** ~4–6 часов · **С телефона:** theory — да

← [`05-software-breakpoints.md`](05-software-breakpoints.md) · → [`07-dwarf-source-debugging.md`](07-dwarf-source-debugging.md)

## Single-step

`PTRACE_SINGLESTEP` resumes tracee until next instruction boundary/trap event. Parent must `waitpid` again; ptrace commands are state transitions, not synchronous function calls that return after tracee instruction automatically.

Single-step is essential for breakpoint dance: execute restored original instruction exactly once before reinserting `INT3`.

## Stack trace problem

User wants:

```text
current function
caller
caller of caller
...
```

Machine only guarantees ABI/register/memory state, not convenient call objects.

## Frame-pointer teaching mode

Compile fixture with:

```text
-O0/-Og as chosen
-fno-omit-frame-pointer
```

Under x86-64 SysV conventional frame-pointer chain, RBP can point to previous frame metadata/return address. This is **not universal unwinding algorithm**; optimized code may omit frame pointer, inline calls, tail-call, use DWARF CFI.

## Safe chain walk

For course fixture only:

- start current RIP/RBP;
- validate each candidate RBP address is readable/mapped and aligned enough for target ABI;
- read saved previous RBP + return address via ptrace helper;
- detect non-progress/cycles;
- cap maximum depth;
- stop on invalid memory rather than crash tracer.

Never trust tracee memory chain as safe pointer structure; corrupted program can contain arbitrary values.

## Symbolization

Return runtime address can be mapped to nearest supported ELF symbol when available; stripped binaries may only show addresses.

## Project stage

Implement `step` and frame-pointer backtrace for dedicated `target_stack` fixture. README states limitations loudly.

## Exit check

Why can a frame-pointer backtrace work perfectly on course fixture and fail on optimized production binary without debugger bug?