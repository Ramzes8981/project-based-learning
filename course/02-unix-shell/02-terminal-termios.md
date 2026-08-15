# 2.2 — Terminal, TTY и `termios`

**Теория:** ~60 мин  
**Guided lab:** ~60–90 мин  
**С телефона:** теория — да; lab — ПК

← [`01-file-descriptors-io.md`](01-file-descriptors-io.md) · → [`03-fork-exec-wait.md`](03-fork-exec-wait.md)

## Цель

Различить terminal и shell и понять, почему interactive text program может переключать terminal driver из canonical mode.

## Terminal != shell

Shell — программа, интерпретирующая команды.

Terminal/TTY — интерфейс ввода-вывода и kernel/driver semantics, через которые interactive process получает characters/signals/display control.

Окно terminal emulator запускает shell, но эти сущности не одно и то же.

## Canonical mode

Обычно terminal line discipline собирает input line, обрабатывает erase и отдаёт программе данные после line delimiter.

Для text editor/read-key lab нужен режим, где процесс получает keypresses раньше.

## `termios`

`tcgetattr` получает terminal attributes, `tcsetattr` меняет их.

Attributes содержат bit flags. Именно поэтому bit masks были prerequisite.

Core idea:

```text
original = current terminal settings
modified = copy(original)
clear/adjust selected flags
apply modified
...
restore original before exit
```

## Почему нужно сохранять original

Если process завершится, оставив terminal в modified mode, shell пользователя может выглядеть «сломавшимся»: input echo/line handling изменятся.

Это cleanup resource, аналогичный `free/close`.

## Signals и restoration

Core lab должен иметь normal cleanup path. Для аварийных scenarios recovery command вроде `reset` полезен.

Не пытайся сейчас написать полностью async-signal-safe framework restoration — signals разберём позже.

## Escape sequences

Terminal output может содержать control sequences для cursor movement/clear screen. Они являются protocol между program и terminal emulator.

Не предполагай, что любой arbitrary output device поддерживает ANSI-like sequences; наш lab ограничен обычным modern terminal environment.

## Exercise / guided lab

Напиши маленькую программу `keydump`:

1. убедиться, что stdin — terminal;
2. сохранить original attributes;
3. включить raw-ish mode минимально необходимыми flags;
4. читать по одному byte/key sequence;
5. печатать numeric byte values;
6. выйти по выбранной key;
7. восстановить terminal.

### Не делаем

- полноценный text editor;
- syntax highlighting;
- rendering engine;
- сложный terminal compatibility layer.

## Causal questions

1. Почему raw mode относится к terminal state, а не «режиму shell»?
2. Что произойдёт, если забыть restoration?
3. Почему bit masks естественны для terminal flags?
4. Почему arrow key может прийти как несколько bytes, а не один ASCII character?

## Разбор

[`02-terminal-termios.solution.md`](02-terminal-termios.solution.md) содержит architecture checklist, но не полный готовый keydump implementation.

## Exit check

Объясни terminal cleanup как resource-lifetime problem.
