# Module 2 — Unix, Processes & Shell

**Цель:** понять системный интерфейс процесса и самостоятельно построить ограниченный Unix shell на C.

**Оценка:** ~45–60 часов.  
**Core milestone:** Unix Shell.  
**Guided lab:** terminal/raw mode.

## Prerequisites

- Module 1 закрыт: pointers/memory/ownership и Hash Table уверенно используются;
- Module 1B Rust Bridge закрыт;
- Module 1C Testing Engineering закрыт;
- bit masks, callbacks и Make знакомы.

## Уроки

1. [`01-file-descriptors-io.md`](01-file-descriptors-io.md)
2. [`02-terminal-termios.md`](02-terminal-termios.md)
3. [`03-fork-exec-wait.md`](03-fork-exec-wait.md)
4. [`04-shell-repl-parser.md`](04-shell-repl-parser.md)
5. [`05-redirection-dup2.md`](05-redirection-dup2.md)
6. [`06-pipes-fd-topology.md`](06-pipes-fd-topology.md)
7. [`07-signals-process-groups.md`](07-signals-process-groups.md)
8. [`08-module-checkpoint.md`](08-module-checkpoint.md)

## Проект

[`project/SPEC.md`](project/SPEC.md) · [`project/README.md`](project/README.md)

Курс строит **ограниченный shell grammar**, а не POSIX-complete shell. В `project/tests/` есть black-box harness для внешнего поведения; parser/unit tests и сам shell пишешь ты.
