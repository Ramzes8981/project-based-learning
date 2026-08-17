# 8.3 — Как debugger останавливает tracee и получает право его наблюдать

**Теория:** ~100 мин · **Практика/project:** ~3–5 часов · **С телефона:** theory — да

← [`02-loader-pie-aslr.md`](02-loader-pie-aslr.md) · → [`04-registers-memory.md`](04-registers-memory.md)

## Проблема

Another process is normally isolated. Debugger needs OS-mediated interface to stop it, inspect/modify state and resume while receiving events.

On Linux course target this interface is **`ptrace`**.

## Roles

```text
tracer  — debugger process
tracee  — debugged process
```

ptrace permissions are constrained by UID/security policy, Yama, containers, namespaces and other controls. Course only traces own fixtures.

## Launch model

A simple controlled launch:

```text
fork
child: PTRACE_TRACEME
child: exec fixture
parent: waitpid for ptrace stop
parent: event loop
```

`exec` of traced child typically produces stop/event suitable for debugger synchronization. Exact stop causes/status must be decoded, not assumed from one signal number.

Alternative attach/seize exists; core can implement launch first.

## Stopped state is the safe inspection point

Debugger should read/change registers or memory when tracee is in ptrace-stop according to API. Maintain explicit debugger state:

```text
RUNNING
STOPPED(reason/status)
EXITED(code/signal)
```

Do not issue random ptrace requests after process exited.

## Wait loop

`waitpid` is debugger event source. Decode:

- normal exit;
- signal termination;
- stopped state + signal/event;
- continue events if enabled.

Retry wait on `EINTR`. Preserve/deliver signals according to debugger policy rather than swallowing every signal accidentally.

## Resume

`PTRACE_CONT` resumes; optional signal argument controls delivery of pending stop signal. A minimal debugger must distinguish breakpoint `SIGTRAP` from unrelated signal that should reach tracee.

## Project stage

Launch fixture, stop at exec, print state, continue, report exit. Only then add registers/memory.

## Exit check

Why is `waitpid` not merely “wait until debugger target exits”, and what state transition must occur before register inspection?