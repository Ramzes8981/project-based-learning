# 2.2 — Почему terminal — не просто окно с текстом

**Теория:** ~65 мин · **Лаб:** ~70 мин · **С телефона:** теория — да

← [`01-file-descriptors-io.md`](01-file-descriptors-io.md) · → [`03-fork-exec-wait.md`](03-fork-exec-wait.md)

## Проблема

`stdin` can refer to a regular file, pipe, or terminal. Interactive behavior like line editing, echo and Ctrl-C clearly does not belong to ordinary file bytes alone.

## TTY mental model

A **terminal/TTY** is an OS interface for interactive byte streams plus terminal-specific state.

Modern terminal emulator roughly:

```text
keyboard/window
↕
pseudo-terminal pair (PTY)
↕
shell/process
```

The shell does not read GUI key events directly; it interacts with a terminal device through file descriptors.

## Canonical mode

In typical canonical mode the terminal driver buffers/edit lines before delivering them to `read`. This is why application often receives a completed line rather than every keystroke.

## Echo

Terminal settings can echo typed bytes back for display. Turning echo off is useful for password-like input, but code must restore settings even on failure.

## `termios`

Unix exposes terminal settings through `termios` APIs such as `tcgetattr`/`tcsetattr`.

Course scope: observe and temporarily modify one flag in a disposable program, then restore original state.

## Why restoration matters

Terminal state belongs to the terminal, not just local variable. If program exits after disabling echo/raw behavior without restoration, user's shell can feel “broken”.

Use cleanup path and save original configuration first.

## `isatty`

`isatty(fd)` asks whether fd refers to terminal-like device. Interactive prompts should often depend on this rather than assuming stdin/stdout are terminals.

## Практика

Write tiny program:

1. check `isatty(STDIN_FILENO)`;
2. if not terminal, report and exit without terminal API;
3. save termios;
4. disable echo temporarily;
5. read a line;
6. restore original settings on normal/error paths.

Разбор: [`02-terminal-termios.solution.md`](02-terminal-termios.solution.md).

## Exit check

Why can redirecting stdin from a file change interactive behavior even though your C code still calls `read(0, ...)`?