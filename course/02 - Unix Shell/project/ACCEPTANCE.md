# Unix Shell — Acceptance

## Core behavior

- blank line safe;
- external command + args executes;
- command not found returns control to shell;
- `cd` changes parent shell cwd;
- `exit` terminates shell intentionally;
- child exit and signal statuses handled without raw-status confusion.

## Redirection

- `<`/`>` work for stated grammar;
- open/dup2 failure is controlled;
- shell's own stdin/stdout remain correct after command;
- extra descriptors closed.

## Pipeline

- producer→consumer bytes correct;
- both children started before parent waits;
- parent closes pipe ends;
- consumer receives EOF when producers close;
- repeated pipelines do not leak fds/zombies.

## Signals

- shell survives foreground Ctrl-C in supported interactive environment;
- foreground process(es) receive expected signal behavior;
- handlers contain only async-signal-safe/minimal actions;
- terminal foreground state restored/documented.

## Quality

- bounded parser;
- warning-clean C17 build;
- relevant sanitizer run clean for parser/owned memory;
- README documents grammar/non-goals/environment;
- one fd/process debugging story;
- transfer feature tested.