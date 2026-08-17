# Unix Shell — staged SPEC

## Stage 0 after 2.3 — fixed launcher

Before parser, prove process mechanics with fixed argv:

- fork;
- child exec;
- child `_exit` on exec failure;
- parent `waitpid`/status decode;
- no zombie leak.

## Stage 1 after 2.4 — REPL

Behavior:

- read bounded line;
- whitespace-separated argv only;
- explicit max line/max args;
- external foreground command;
- `cd` + `exit` built-ins in parent;
- blank input safe;
- exec failure returns to prompt.

## Stage 2 after 2.5 — redirection

Support one `<` and one `>` per command according to documented grammar.

- child opens resource;
- `dup2` to stdin/stdout;
- closes extra fd;
- failure terminates child command, not shell;
- parent descriptors/prompts unaffected.

## Stage 3 after 2.6 — one pipeline

Support exactly:

```text
command | command
```

unless transfer extends it.

Requirements:

- create pipe before forks;
- fork both sides before waiting;
- map producer stdout and consumer stdin;
- close every unused pipe end in parent/children;
- reap both children;
- EOF/hang tests.

## Stage 4 after 2.7 — foreground signals

Interactive path documents process-group/terminal policy. Shell should survive Ctrl-C intended for foreground job. CI may test reduced process-group semantics without owning a real terminal; README states environment limitation.

## Error/resource rules

- check fork/open/dup2/pipe/exec/wait errors;
- retry `waitpid` on `EINTR` where appropriate;
- no descriptor leaks across repeated commands;
- no child falls through into parent REPL;
- parser never writes outside bounded arrays;
- child failure paths close owned extra descriptors.

## Transfer task

Choose one: append `>>`, arbitrary pipeline length, environment variable assignment subset, or better parser quoting subset. Write grammar/ownership changes before implementation.