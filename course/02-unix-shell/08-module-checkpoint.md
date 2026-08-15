# Module 2 — Checkpoint

**Время:** ~2–4 часа  
**С телефона:** conceptual — да

← [`07-signals-process-groups.md`](07-signals-process-groups.md) · ↑ [`README`](README.md)

## Explain

1. fd vs underlying open file description.
2. partial read/write.
3. EOF vs error.
4. descriptor ownership/close.
5. terminal vs shell.
6. `fork` return paths.
7. `exec` replaces process image.
8. `waitpid`/zombie.
9. builtin `cd` in parent.
10. `dup2` redirection.
11. pipe EOF and leaked write ends.
12. why pipeline children run concurrently.
13. signal disposition/async-signal-safety.
14. process group intuition.

## Scenario exam

Нарисуй и объясни:

```text
producer | filter > result.txt
```

Нужно показать:

- processes;
- pipes;
- relevant fds;
- `dup2` mapping;
- what closes where;
- wait lifecycle;
- Ctrl-C behavior.

## Core milestone

Проверь [`project/ACCEPTANCE.md`](project/ACCEPTANCE.md).

## Debug story

Обязательно диагностируй один hang/EOF bug, вызванный descriptor lifetime, либо воспроизведи controlled seeded version.

## Transfer

Одна feature:

- N-stage pipeline;
- basic background job;
- small `$VAR` expansion;
- history;
- process-group foreground handling.

## Exit gate

Модуль закрыт, если shell больше не выглядит как магический интерпретатор строк: ты можешь разложить его на parser + process creation + fd graph + signals/lifecycle.
