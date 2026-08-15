# 2.7 — Signals и foreground process model

**Теория:** ~70 мин  
**Project slice:** ~3–5 часов  
**С телефона:** теория — да

← [`06-pipes-fd-topology.md`](06-pipes-fd-topology.md) · → [`08-module-checkpoint.md`](08-module-checkpoint.md)

## Цель

Понять signals как asynchronous process events и сделать так, чтобы Ctrl-C не убивал shell вместе с foreground command.

## Signal model

Signal — механизм доставки process/thread события.

Нас интересуют:

- `SIGINT` — interactive interrupt;
- `SIGTERM` — termination request convention;
- `SIGCHLD` — child state changed;
- `SIGPIPE` — write to pipe with no reader;
- `SIGTSTP`/job control — conceptual/stretch.

## Default, ignore, handler

Для signal process может иметь disposition:

- default action;
- ignore;
- user handler (кроме несменяемых signals вроде `SIGKILL`/`SIGSTOP`).

Используй `sigaction`, а не старый `signal()` как основной учебный API.

## Async-signal-safety

Handler может прервать обычный code в неудобный момент. Большинство library functions нельзя безопасно вызывать из handler.

Core правило:

> handler делает минимум: устанавливает atomic-ish flag подходящего типа или выполняет async-signal-safe operation по ясному contract; сложную работу выполняет normal control flow.

`printf` внутри arbitrary handler — плохой default.

## Shell и Ctrl-C

Terminal driver обычно посылает foreground process group signal при Ctrl-C.

Полноценный job-control shell управляет process groups/controlling terminal. Core project вводит достаточно модели, чтобы shell не погибал вместе с foreground child.

Минимальный учебный вариант может:

- shell игнорирует `SIGINT` в prompt state;
- child перед `exec` возвращает default `SIGINT` disposition;
- parent waits child.

Для pipelines/process groups лучше создать отдельную foreground group — это transfer/stretch depending pace.

## `SIGCHLD`

Synchronous shell, который сразу `waitpid` foreground children, может не требовать сложного SIGCHLD handler.

Background jobs уже требуют систематического reaping design.

Не добавляй async complexity до необходимости.

## `EINTR` снова

Signals могут прерывать blocking syscalls. Некоторые вызовы с `SA_RESTART` автоматически restart в определённых условиях, но robust code не должен строиться на vague assumption «signals никогда не прерывают read».

## Project slice

Core:

- Ctrl-C во время foreground command завершает/прерывает child according to default behavior;
- shell process остаётся alive и возвращает prompt;
- wait status сообщает signal termination;
- handler/disposition не содержит unsafe random library work.

## Causal questions

1. Почему handler должен быть минимальным?
2. Почему shell и child могут хотеть разные SIGINT dispositions?
3. Почему background support резко усложняет lifecycle/reaping?
4. Чем process group отличается от одного PID в контексте pipeline?

## Exercise

Нарисуй signal flow для:

```text
shell -> pipeline A|B
user presses Ctrl-C
```

Сначала для naive individual PIDs, затем conceptual foreground process group.

Разбор: [`07-signals-process-groups.solution.md`](07-signals-process-groups.solution.md).

## Exit check

Сможешь ли ты объяснить, почему «поймать Ctrl-C handler'ом и вызвать там всё что угодно» — небезопасная модель?
