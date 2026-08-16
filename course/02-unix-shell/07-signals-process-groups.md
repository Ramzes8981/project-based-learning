# 2.7 — Signals и foreground process model

**Теория:** ~80 мин  
**Project slice:** ~3–5 часов  
**С телефона:** теория — да

← [`06-pipes-fd-topology.md`](06-pipes-fd-topology.md) · → [`08-module-checkpoint.md`](08-module-checkpoint.md)

## Цель

Понять signals как asynchronous events и сделать Ctrl-C предсказуемым для shell/foreground child без небезопасной работы внутри handler.

## Signal model

Нас интересуют:

- `SIGINT` — interactive interrupt;
- `SIGTERM` — conventional termination request;
- `SIGCHLD` — child state changed;
- `SIGPIPE` — write to pipe without reader;
- `SIGTSTP`/job control — conceptual/stretch.

Disposition может быть default, ignore или user handler, кроме несменяемых `SIGKILL`/`SIGSTOP`.

Основной API курса — `sigaction`.

## Async-signal-safety

Handler может прервать normal code в любой неудобной точке. Большинство library calls нельзя считать безопасными внутри handler. `printf`, allocation, arbitrary locks — плохой default.

Самая маленькая communication pattern для учебного single-threaded кода:

```c
#include <signal.h>

static volatile sig_atomic_t interrupted = 0;

static void on_signal(int signo)
{
    (void)signo;
    interrupted = 1;
}
```

### Что здесь означает `sig_atomic_t`

`sig_atomic_t` — integer type, доступ к которому предназначен для безопасной indivisible read/write communication с signal handler в пределах guarantees C/POSIX signal model.

`volatile` говорит compiler, что value может измениться вне обычного sequential flow и чтение/запись нельзя оптимизировать как обычную неизменяемую local state.

Важно:

> `volatile sig_atomic_t` **не является general-purpose thread atomic** и не заменяет C atomics/mutex. Он не превращает произвольные read-modify-write операции в atomic synchronization.

Handler должен по возможности только установить flag. Сложную работу делает normal control flow после возврата.

## Shell и Ctrl-C

Terminal обычно направляет interactive signals foreground process group.

Минимальная core model:

```text
shell at prompt: SIGINT ignored/handled minimally
child before exec: restore default SIGINT
parent: waitpid child
Ctrl-C: foreground command terminates; shell survives
```

Для pipeline полноценнее создать одну process group для children и передавать foreground terminal ей. Full job control остаётся stretch, но process-group concept должен быть понятен.

## `SIGCHLD`

Synchronous shell, который сразу waits foreground children, не обязан создавать сложный SIGCHLD handler. Background jobs потребуют asynchronous reaping и существенно большего lifecycle state.

## `EINTR`

Blocking syscall может завершиться с interruption. `SA_RESTART` влияет на некоторые calls, но robust code всё равно должен иметь явную policy: retry или обработать interruption.

## Project slice

Core acceptance:

- Ctrl-C на foreground command не завершает shell;
- child получает ожидаемую default interrupt behavior;
- `waitpid` различает exit vs signal termination;
- handler не выполняет небезопасную сложную работу;
- descriptor/process cleanup остаётся корректным после interruption.

## Exercise

Нарисуй signal flow для `shell -> A | B`, когда пользователь нажимает Ctrl-C. Отдельно покажи naive individual-PID model и foreground process-group model.

Разбор: [`07-signals-process-groups.solution.md`](07-signals-process-groups.solution.md).

## Causal questions

1. Почему `volatile sig_atomic_t` не эквивалентен mutex/atomic для threads?
2. Почему shell и child хотят разные SIGINT dispositions?
3. Почему handler должен быть минимальным?
4. Почему background jobs усложняют reaping?

## Exit check

Ты должен уметь объяснить: signal handler сообщает событие, а normal control flow обрабатывает состояние.
