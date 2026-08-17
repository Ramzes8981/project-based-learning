# 2.8 — Checkpoint: можешь ли ты нарисовать process/fd topology shell-а

**Время:** ~3–5 часов · **С телефона:** review — да; project — ПК

← [`07-signals-process-groups.md`](07-signals-process-groups.md) · ↑ [`README`](README.md)

## Explain

1. executable file vs process;
2. syscall boundary;
3. fd as process-local handle;
4. short I/O and `EINTR`;
5. terminal/TTY vs ordinary file;
6. fork vs exec;
7. why wait/reap;
8. why `cd` runs in parent;
9. how `dup2` implements redirection;
10. why one leaked pipe writer prevents EOF;
11. why producer-before-consumer wait can deadlock;
12. signal handler restrictions;
13. process group reason for foreground job.

## Project gate

Shell passes [`project/ACCEPTANCE.md`](project/ACCEPTANCE.md) and [`project/TESTS.md`](project/TESTS.md).

## Required evidence

- one `strace` or equivalent observation tied to prediction;
- one fd topology drawing for pipeline;
- one debugging story with leaked descriptor, child status or parser boundary;
- no zombie leak after repeated commands.

## Exit check

Given `cat input | grep x > out`, you can describe which process owns which descriptors before/after exec and how parent eventually regains control.