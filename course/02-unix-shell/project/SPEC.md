# Course Shell — SPEC

Реализуй single-threaded educational shell на C.

## Grammar core

Поддерживается:

```text
command [arg ...]
command > file
command < file
command | command
```

Whitespace-tokenized syntax. Quotes/escaping/globbing/command substitution не поддерживаются core-версией.

## Builtins

- `cd`;
- `exit`.

## External commands

- `fork`;
- PATH-aware `exec` family choice;
- `waitpid`;
- normal/signal status.

## Redirection

- input `<`;
- output `>`;
- malformed syntax -> parser error;
- parent shell descriptors не повреждаются.

## Pipeline

Минимум двухкомандный `A | B`.

Все unused pipe ends закрываются в каждом process.

## Signals

Ctrl-C foreground child не должен убивать shell. Core implementation документирует chosen signal model.

## Explicit non-goals

- POSIX shell compliance;
- quotes/escapes;
- globbing;
- command substitution;
- full job control;
- scripting language.
