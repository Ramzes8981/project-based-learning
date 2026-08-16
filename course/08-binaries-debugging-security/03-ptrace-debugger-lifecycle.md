# 8.3 — `ptrace` и debugger state machine

**Теория:** ~105 мин  
**Project slice:** ~4–6 часов  
**С телефона:** теория — да

← [`02-loader-pie-aslr.md`](02-loader-pie-aslr.md) · → [`04-registers-memory.md`](04-registers-memory.md)

## Цель

Построить Linux tracer/tracee lifecycle и правильно различать running/stopped/exited/signaled states.

## Scope

`ptrace` — Linux process/thread tracing API. `pid` в большинстве requests обозначает конкретный tracee thread ID. Большинство inspect/modify/restart operations требуют, чтобы tracee находился в **ptrace-stop**; attach/seize/interrupt имеют отдельные rules.

Это не portable POSIX debugger abstraction.

## Launch path

Course core:

```text
parent fork
├─ child:
│    PTRACE_TRACEME
│    execve/execvp target
└─ parent:
     waitpid initial traced stop
     inspect / command loop
```

`PTRACE_TRACEME` вызывается tracee. После traced `exec` parent получает debugger-visible stop (`SIGTRAP`-style event in this simple setup) и только после `waitpid` может безопасно считать child stopped.

## State machine

```text
NEW -> RUNNING -> STOPPED -> RUNNING ... -> EXITED
                          \              -> SIGNALED
                           -> DETACHED -> normal process
```

Debugger не вызывает memory/register requests «пока target вроде стоит»: у него должен быть explicit state derived from successful `waitpid` decode.

## `waitpid` decoding

Status — packed process state, не exit code.

```text
WIFEXITED    -> WEXITSTATUS valid
WIFSIGNALED  -> WTERMSIG valid
WIFSTOPPED   -> WSTOPSIG valid
```

Для traced child stop reports доступны даже без обычного job-control use of `WUNTRACED`.

## Restart и signals

`PTRACE_CONT`/`PTRACE_SINGLESTEP` переводят stopped tracee обратно в execution; tracer затем **снова** ждёт state change.

Некоторые stops соответствуют signal delivery. Restart request может передать signal tracee или подавить его. Поэтому «всегда continue с signal=0» способен менять semantics программы. Core обрабатывает собственные `SIGTRAP` stops и явно сообщает остальные; полноценная signal forwarding policy — transfer.

## Error nuance: peek result `-1`

Некоторые ptrace peek requests возвращают прочитанное machine word как return value. Data word сам может быть `-1`. Правильный pattern:

```text
errno = 0
value = ptrace(PEEK...)
if value == -1 AND errno != 0 -> error
otherwise value is legitimate data
```

## Project slice

`minidbg-c ./target [args...]`:

- fork/TRACEME/exec;
- wait initial stop;
- `continue`, `quit`;
- exact reporting exited/signaled/stopped;
- quit/detach/kill policy documented;
- no zombie tracee.

## Exit check

Каждая debugger command должна иметь допустимый source state и ожидаемый next state. Если такого mapping нет — implementation уже хрупкая.
