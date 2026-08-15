# Module 2 — Unix, Processes, and the Shell

**Status:** CORE  
**Estimated effort:** 40–55 hours (~6–8 weeks)  
**Core milestone:** Unix Shell in C  
**Guided lab:** selected Kilo terminal/raw-mode chapters

## Prerequisites

From Module 1:

- pointers, dynamic memory and arrays are usable;
- strings can be manipulated deliberately;
- bitwise operators/masks have been introduced;
- basic error handling and debugging are familiar.

This ordering removes a hidden prerequisite in Kilo: its `termios` work manipulates bit flags.

## Sources

- **PRIMARY:** Dive into Systems selected OS/Unix sections + current POSIX/man pages.
- **PROCESS COMPANION:** selected OSTEP Process / Process API chapters.
- **TOOLING COMPANION:** Missing Semester current notes/video; Russian translation where useful.
- **GUIDED LAB:** Kilo, only the terminal/raw-input subset: https://viewsourcecode.org/snaptoken/kilo/
- **PROJECT REFERENCE:** Stephen Brennan, *Write a Shell in C*: https://brennan.io/2015/01/16/write-a-shell-in-c/

For API behavior, current POSIX.1-2024/man pages override historical tutorials.

## Outcomes

The learner can:

- explain file descriptors and robust byte-stream I/O;
- inspect syscalls with `strace`;
- create/replace/wait for processes;
- use pipes and redirection;
- handle basic signals safely enough for the project scope;
- build a small shell with defined limitations;
- explain why a real POSIX shell parser is much more complex than splitting on spaces.

---

# Unit 2.1 — Files, descriptors, and robust I/O

### Learn

- kernel vs user space;
- syscall idea;
- file descriptor as process-local integer handle;
- `open`, `read`, `write`, `close`;
- `stdin/stdout/stderr`;
- `errno`/`perror`;
- short reads/writes;
- `EINTR` intuition;
- EOF.

### Practice

Build a small file-copy utility using a buffer and correct retry/partial-write logic.

Inspect it with `strace`.

### Industry case

A network/file loop assumes one `write()` sends the whole buffer. Explain why this assumption can corrupt application-level behavior and design a loop that tracks the remaining bytes.

### Self-check

- handles empty files;
- handles large files;
- closes descriptors on errors;
- no silent truncation;
- can explain each syscall observed by `strace`.

---

# Unit 2.2 — Terminal model and bit flags

### Learn

- terminal vs shell;
- canonical vs raw-ish input;
- `termios` at a practical level;
- flag masks;
- escape sequences;
- terminal restoration on exit/error.

### Guided lab — Kilo slice

Use only enough Kilo to:

- enter raw mode;
- read individual key presses;
- render basic terminal output;
- guarantee restoration on exit.

Full text editor, search and syntax highlighting are **Stretch**, not core.

### What can go wrong?

Leaving the terminal in a modified state is environment friction, not an intended challenge. Keep a documented recovery command (`reset`) and cleanup path.

---

# Unit 2.3 — Processes

### Learn

- program vs process;
- PID;
- `fork()` semantics;
- copy-on-write intuition only;
- `exec*()` family concept;
- `waitpid()` and child state;
- exit status;
- environment variables;
- `PATH` lookup.

### Practice

Build a process launcher that:

1. forks;
2. execs a chosen command;
3. waits;
4. reports exit/signal termination correctly.

### Situational questions

- What code runs twice after `fork()`?
- What resources are inherited by the child?
- Why does successful `exec()` not return?
- What happens if the parent never reaps terminated children?

---

# Unit 2.4 — Shell v0: parser scope and command execution

### Learn

Define a **course shell grammar** before coding.

Core grammar intentionally supports:

- command name;
- whitespace-separated arguments;
- no quoting/escaping initially.

Do not pretend this is a POSIX shell parser.

### Project slice

Build REPL → tokenize → execute one external command → wait → prompt again.

Add built-ins:

- `cd`;
- `exit`.

### Common mistake

`cd` cannot be implemented by `exec()` in a child if the goal is to change the shell process's working directory.

---

# Unit 2.5 — Redirection

### Learn

- descriptor duplication;
- `dup2()`;
- descriptor inheritance across `exec()`;
- open flags / permissions at a practical level.

### Project slice

Support a deliberately small syntax:

- `command > file`;
- `command < file`.

### Rubric

- parent shell descriptors are restored/unchanged;
- child closes unneeded descriptors;
- errors are visible and do not kill the shell.

---

# Unit 2.6 — Pipes

### Learn

- `pipe()` returns read/write descriptors;
- producer/consumer composition;
- EOF depends on **all** write ends being closed;
- process topology for a pipeline.

### Project slice

Support at least a two-command pipeline:

```text
A | B
```

Then generalize to N commands if progress is comfortable.

### What will go wrong if…?

- the parent keeps an extra pipe write end open?
- both children inherit every pipe descriptor?
- the shell waits for the first process before starting the second?

These are required reasoning questions, not optional trivia.

---

# Unit 2.7 — Signals and process cleanup

### Learn

- signal concept;
- `SIGINT`, `SIGTERM`, `SIGCHLD`;
- async-signal-safety intuition;
- foreground shell behavior;
- process groups/job control **conceptually**.

Full interactive job control is Stretch; it is not required for the core shell.

### Project slice

At minimum:

- Ctrl-C should not unintentionally kill the shell when a child command is running;
- child termination is reported/reaped correctly.

---

# Core milestone rubric — Unix Shell

### Required features

- REPL;
- external command launch;
- arguments;
- `cd` / `exit`;
- input/output redirection;
- one or more pipelines;
- basic signal behavior;
- useful error messages.

### Transfer feature

Choose one:

- N-stage pipeline;
- environment-variable expansion for a small defined syntax;
- command history;
- `pwd` builtin;
- basic background process support.

### Engineering review

Explain:

- process tree for a pipeline;
- descriptor ownership/closure;
- parser limitations;
- zombie prevention;
- failure behavior for nonexistent commands/files;
- why this shell is not POSIX-complete.

---

# Exit gate

The learner can draw the process/FD topology of `producer | filter > out.txt`, implement it for the course grammar, and debug at least one deadlock/EOF issue caused by descriptor lifetime.