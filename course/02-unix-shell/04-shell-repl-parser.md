# 2.4 — Как превратить строку команды в небольшой безопасный shell grammar

**Теория:** ~70 мин · **Практика/project:** ~3–5 часов · **С телефона:** теория — да

← [`03-fork-exec-wait.md`](03-fork-exec-wait.md) · → [`05-redirection-dup2.md`](05-redirection-dup2.md)

## Проблема

`fork/exec` запускают уже готовые `argv`. Shell сначала должен прочитать text and decide what command/arguments mean.

Нельзя сразу «поддержать Bash syntax»: uncontrolled grammar creates parser complexity unrelated to current OS learning.

## REPL

Shell core loop:

```text
read line
→ parse into bounded representation
→ decide built-in vs external
→ execute
→ report result
→ repeat
```

REPL = read-evaluate-print loop; term is useful only because it names this repeated interaction.

## Course grammar v1

Start intentionally small:

```text
command := word { whitespace word }
```

No quoting, globbing, variable expansion or command substitution in first milestone. Reject overlong line/too many args explicitly.

Later lessons add redirection and one pipeline as grammar extensions.

## `argv` contract

Exec-style functions expect:

```text
argv[0] = program name
argv[1..] = arguments
argv[last] = NULL
```

Parser must preserve NUL-terminated C strings and a final null pointer entry.

## Built-ins run in shell process when state must persist

Example `cd`: if child changes working directory and exits, parent shell directory does not change. Therefore stateful built-in runs in parent process.

This is not special syntax magic; it follows process isolation.

## Parsing safely

Keep explicit bounds:

```text
max input bytes
max args
max token bytes inherited from line
```

Do not call `strtok` blindly if its hidden mutation/state makes grammar hard to reason about. It is allowed if behavior is understood and tests cover empty/multiple delimiters; manual scanner often teaches boundaries more clearly.

## Project slice

Implement REPL + external foreground command + `exit` + `cd`. Technical milestone in [`project/SPEC.md`](project/SPEC.md).

## Exit check

Why must `cd` happen in parent shell, and why is deliberately small grammar an engineering advantage rather than missing feature?