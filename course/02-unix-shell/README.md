# Module 2 — Как ОС запускает программы и соединяет их в shell

**Оценка:** ~35–50 часов.  
**Среда:** Linux/WSL2, см. [`../ENVIRONMENT.md`](../ENVIRONMENT.md).

## Главная проблема

До сих пор программы в основном меняли собственные данные. Но файл, terminal, новый process и pipe — ресурсы, которыми управляет ОС. Нужно понять boundary:

```text
user program
↓ request to OS
kernel-managed resource
↓ result/status/data
user program
```

## Уроки

1. [`01-file-descriptors-io.md`](01-file-descriptors-io.md) — **Что такое запущенная программа, как она просит ОС о работе и откуда берётся file descriptor**.
2. [`02-terminal-termios.md`](02-terminal-termios.md) — **Почему terminal — не просто “окно с текстом”**.
3. [`03-fork-exec-wait.md`](03-fork-exec-wait.md) — **Как shell создаёт новый процесс и запускает в нём другую программу**.
4. [`04-shell-repl-parser.md`](04-shell-repl-parser.md) — **Как превратить строку команды в небольшой безопасный shell grammar**.
5. [`05-redirection-dup2.md`](05-redirection-dup2.md) — **Как `>` меняет destination stdout без изменения самой программы**.
6. [`06-pipes-fd-topology.md`](06-pipes-fd-topology.md) — **Как две программы соединяются потоком bytes и почему лишний open end мешает EOF**.
7. [`07-signals-process-groups.md`](07-signals-process-groups.md) — **Как shell реагирует на Ctrl-C, не убивая себя вместе с foreground job**.
8. [`08-module-checkpoint.md`](08-module-checkpoint.md) — checkpoint.

## Проект

[`project/README.md`](project/README.md) — Unix Shell. SPEC раскрывается по milestones; весь `fork/exec/pipe/process group` contract не требуется в день первого знакомства с проектом.

## Не нужно сейчас

- threads;
- sockets;
- virtual memory/page tables;
- namespaces/cgroups;
- ptrace;
- job-control completeness production shell-а.