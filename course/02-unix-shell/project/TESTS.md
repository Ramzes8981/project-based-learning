# Course Shell — public scenarios

`TESTS.md` задаёт contract. `tests/run_cases.py` покрывает только часть black-box поведения; свои parser/unit tests обязательны.

## Core scenarios

1. empty line не crash;
2. one external command with args;
3. unknown command -> explicit failure, shell continues;
4. `cd` changes shell working directory (builtin runs in parent);
5. `exit` terminates shell;
6. `>` writes expected file;
7. `<` feeds file to command;
8. malformed redirection is parser error, not undefined behavior;
9. `printf abc | wc -c`-like two-command pipeline completes;
10. no hang from leaked pipe write-end;
11. command exit status vs signal termination distinguished;
12. Ctrl-C foreground child leaves shell alive;
13. repeated commands do not accumulate unreaped children/descriptors;
14. EOF on stdin exits according to documented policy.

## Review-only

- leading/trailing/repeated whitespace;
- missing filename around redirect;
- multiple pipe syntax errors;
- exec failure inside pipeline;
- interrupted wait/read;
- long input under documented limits.
