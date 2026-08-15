# 2.5 — Redirection и `dup2`

**Теория:** ~65 мин  
**Project slice:** ~3–5 часов  
**С телефона:** теория — да

← [`04-shell-repl-parser.md`](04-shell-repl-parser.md) · → [`06-pipes-fd-topology.md`](06-pipes-fd-topology.md)

## Цель

Понять redirection как изменение descriptor topology child process перед `exec`.

## Что значит `command > out.txt`

Shell не просит external program «писать в файл». Программа по-прежнему пишет в fd `1` stdout.

Shell до `exec` делает так, чтобы fd `1` у child ссылался на открытый `out.txt`.

```text
before:
child fd 1 -> terminal

after redirection:
child fd 1 -> out.txt open-file state
```

Программа может вообще не знать, что stdout теперь file.

## `dup2`

Conceptually:

```c
dup2(source_fd, target_fd)
```

заставляет `target_fd` ссылаться на то же open file description, что `source_fd`, atomically replacing existing target mapping по contract API.

После:

```c
dup2(file_fd, STDOUT_FILENO);
```

`write(1, ...)` идёт в file.

Temporary `file_fd` после успешного duplication обычно закрывается, если больше не нужен. fd `1` остаётся отдельным descriptor reference.

## Input redirection

`command < input.txt` аналогично заменяет fd `0`.

## Parent vs child

Делай redirection в child **после fork и до exec**, чтобы не сломать stdout самого shell prompt.

```text
parent shell stdout -> terminal
child fork inherits -> terminal
child dup2 -> file
parent remains -> terminal
```

## Open flags

Для `>` обычно нужен create/truncate write path. Точные flags и permissions должны соответствовать course contract.

Не делай security-sensitive permissions случайными: mode проходит через umask.

## Failure path

Если open redirection file fail:

- child не должен exec command с неправильным stdout;
- error должен быть виден;
- shell parent должен продолжить REPL.

## Project slice

Grammar v1 добавляет:

```text
command > file
command < file
```

Ограничения:

- один input и один output redirection максимум;
- operator должен быть отдельным token согласно текущему tokenizer contract;
- malformed syntax выдаёт parser error.

## Causal questions

1. Почему shell parent не должен делать permanent `dup2` на свой stdout для external command?
2. Почему после `dup2(file_fd, 1)` можно закрыть `file_fd`?
3. Чем descriptor number отличается от underlying open file description?
4. Что произойдёт, если `open` failed, а child всё равно `exec`?

## Exercise

До кода нарисуй fd table parent/child для:

```text
cat < in.txt > out.txt
```

Разбор: [`05-redirection-dup2.solution.md`](05-redirection-dup2.solution.md).

## Exit check

Можешь ли ты объяснить redirection без фразы «shell перенаправляет текст» — только через descriptors/open-file references?
