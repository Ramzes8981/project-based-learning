# 2.5 — Как `>` меняет stdout без изменения самой программы

**Теория:** ~75 мин · **Практика/project:** ~3–5 часов · **С телефона:** теория — да

← [`04-shell-repl-parser.md`](04-shell-repl-parser.md) · → [`06-pipes-fd-topology.md`](06-pipes-fd-topology.md)

## Проблема

Program writes to fd 1. Yet:

```bash
printf hello > out.txt
```

same program bytes end up in file. Program itself did not learn file path.

So shell changes **descriptor topology before exec**.

## `dup2`

`dup2(oldfd, newfd)` makes `newfd` refer to same open resource description as `oldfd` (closing previous `newfd` if necessary, subject to API rules).

Redirection flow in child:

```text
open output file → fd X
↓
dup2(X, STDOUT_FILENO)
↓
close X if X != STDOUT_FILENO
↓
exec program
```

New program inherits fd 1 already pointing to file.

## Why setup in child

If parent shell permanently redirects its own stdout, future prompts/output also go to file. For an external command, perform redirection in child between fork and exec.

## Input redirection

`< file` similarly opens read fd and maps it to `STDIN_FILENO`.

## Open flags are part of semantics

For `>` typical behavior is create-if-needed + truncate existing file. Append `>>` is different contract and should not accidentally use same flags.

Specify mode when `O_CREAT` is present.

## Failure path

If `open` or `dup2` fails in child:

- report safely;
- close any opened extra fd;
- `_exit(nonzero)`;
- never continue to exec with unintended descriptors.

## Практика

Add one output redirection and one input redirection to shell grammar. Use fixture that proves child output goes to file while shell prompt remains terminal.

Разбор: [`05-redirection-dup2.solution.md`](05-redirection-dup2.solution.md).

## Exit check

Why can arbitrary program keep writing fd 1 while shell decides whether those bytes reach terminal, file or later a pipe?