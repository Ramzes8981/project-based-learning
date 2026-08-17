# Unix Shell — рабочий проект

Project grows after each lesson. Do not start by reading full POSIX shell grammar.

## First behavior

```text
prompt/read line
run external command with arguments
wait for foreground command
run cd/exit as built-ins
continue shell loop
```

Then unlock redirection, one pipeline and minimal foreground signal behavior.

## Non-goals

- quotes/escaping parity with Bash;
- globbing;
- variables/substitution;
- background jobs/full job-control UI;
- scripting language;
- arbitrary pipeline length unless chosen as transfer.

Docs: [`SPEC.md`](SPEC.md) · [`ACCEPTANCE.md`](ACCEPTANCE.md) · [`TESTS.md`](TESTS.md) · [`HINTS.md`](HINTS.md).