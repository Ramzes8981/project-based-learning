# Module 2 — Unix, Processes & Shell

**Цель:** понять системный интерфейс процесса и самостоятельно построить ограниченный Unix shell на C.

**Оценка:** ~40–55 часов.  
**Core milestone:** Unix Shell.  
**Guided lab:** terminal/raw mode.

## Prerequisites

- C pointers/memory уверенно используются;
- bit masks знакомы;
- Hash Table milestone закрыт;
- Rust Bridge закрыт, но основной код этого модуля C-first.

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

[`project/SPEC.md`](project/SPEC.md)

Курс сознательно строит **ограниченный shell grammar**, а не обещает POSIX-complete shell.
