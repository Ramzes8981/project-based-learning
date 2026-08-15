# 8.3 — `ptrace` и debugger state machine

**Теория:** ~100 мин  
**Project slice:** ~4–6 часов  
**С телефона:** теория — да

← [`02-loader-pie-aslr.md`](02-loader-pie-aslr.md) · → [`04-registers-memory.md`](04-registers-memory.md)

## Цель

Построить tracer/tracee lifecycle и никогда не путать `stopped`, `exited`, `signaled` states.

## Scope

`ptrace` — Linux-specific process/thread tracing API. Core debugger targeting **Linux x86-64**, single-threaded tracee first.

Linux `ptrace` позволяет tracer наблюдать/управлять tracee memory/registers; commands addressed to a specific tracee thread. Большинство operations требуют, чтобы tracee уже был в ptrace-stop. citeturn857293search1

## Launch model

Course uses:

```text
parent debugger forks
child:
    PTRACE_TRACEME
    exec target
parent:
    waitpid child stop
    debugger loop
```

Successful traced `exec` causes debugger-visible stop/event under normal ptrace setup before ordinary execution continues. Exact options/events must be handled deliberately.

## State machine

```text
NEW
 ↓ launch
RUNNING
 ↓ stop/event/signal
STOPPED ── inspect/modify ──┐
  │                         │
  ├─ PTRACE_CONT ─────────> RUNNING
  ├─ PTRACE_SINGLESTEP ───> RUNNING
  └─ detach -> RUNNING untraced

RUNNING -> EXITED/SIGNALED
```

Debugger commands that inspect memory/registers only valid in appropriate STOPPED state.

## `waitpid`

Wait status must be decoded:

```text
WIFEXITED
WEXITSTATUS
WIFSIGNALED
WTERMSIG
WIFSTOPPED
WSTOPSIG
```

Linux wait docs explicitly distinguish termination, signal stop and resumed state. citeturn857293search0

## Signal-delivery stop

Tracee can stop because of a signal. Tracer decides how to restart and whether to deliver/suppress signal in relevant ptrace stop.

Naively continuing with signal 0 always can change program semantics by swallowing real signals.

Core first handles SIGTRAP from debugger actions and reports other signals; deeper signal forwarding can be transfer.

## Errors

`ptrace` returns `-1` on error, but some read operations can legitimately return word value `-1`. Therefore check/reset `errno` according to specific request contract rather than equating value `-1` with error blindly.

## Project slice

Implement `minidbg-c v0`:

```text
minidbg ./target
```

- fork child;
- TRACEME;
- exec;
- parent waits initial stop;
- commands: `continue`, `quit`;
- reports exit/signal status;
- no zombie tracee left.

## Causal questions

1. Почему ptrace debugger — state machine, а не набор random functions?
2. Почему inspect while tracee running обычно invalid?
3. Почему `waitpid` status нельзя считать raw exit code?
4. Почему signal forwarding требует intent?

## Exit check

Нарисуй all allowed transitions твоего debugger core.
