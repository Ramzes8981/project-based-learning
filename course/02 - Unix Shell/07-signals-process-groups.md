# 2.7 — Как shell переживает Ctrl-C, а foreground job — нет

**Теория:** ~95 мин · **Практика/project:** ~4–6 часов · **С телефона:** теория — да

← [`06-pipes-fd-topology.md`](06-pipes-fd-topology.md) · → [`08-module-checkpoint.md`](08-module-checkpoint.md)

## Проблема

Interactive terminal sends events like Ctrl-C as signals to foreground job context. If shell and command are treated identically, Ctrl-C can terminate the shell itself.

Need two concepts: asynchronous notification and group of related processes.

## Signal

**Signal** is asynchronous notification delivered to process/thread according to POSIX rules. Examples: `SIGINT`, `SIGTERM`, `SIGCHLD`.

Signal can have default action, be ignored, blocked, or handled (with restrictions).

## Signal handler restrictions

Handler interrupts normal execution. Most library functions are not async-signal-safe. Do not call `printf`, `malloc` or complex project logic from handler.

Course pattern:

```text
handler does minimal safe action / sets sig_atomic_t flag
normal control flow observes flag and performs complex work
```

## Process group

Pipeline may contain several processes that should receive terminal job signals together. POSIX groups processes using **process group** with PGID.

```text
shell process group
foreground job process group: producer + consumer + ...
```

Terminal tracks foreground process group.

## Minimal job-control scope

Core shell does not implement full Bash jobs table/background `fg/bg`. It should understand enough to:

- place foreground external command/pipeline in its own process group;
- arrange foreground terminal group where environment allows;
- avoid shell death on foreground Ctrl-C;
- wait/reap all children;
- restore shell terminal foreground ownership.

Exact interactive job-control APIs are platform-sensitive; project acceptance may allow documented reduced scope in non-interactive CI.

## `SIGCHLD` and reaping

A signal may notify that child changed state, but actual status still comes from `waitpid`. Beware race between signal arrival and normal wait logic; design one clear reaping policy.

## `EINTR` returns again

Signals explain why earlier blocking calls can be interrupted. Retry only where contract says operation was not completed and retry is appropriate.

## Практика

Add controlled foreground Ctrl-C behavior to shell. Test interactively in PTY/terminal and keep non-interactive automated tests for process exit/reaping.

Разбор: [`07-signals-process-groups.solution.md`](07-signals-process-groups.solution.md).

## Exit check

Why should shell and pipeline be different process groups, and why is `printf` inside arbitrary signal handler a bad baseline?