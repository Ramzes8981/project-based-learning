# 2.1 — File descriptors и надёжный byte-stream I/O

**Теория:** ~60 мин  
**Упражнение:** ~60 мин  
**Project slice:** ~20 мин  
**С телефона:** теория — да

← [`README`](README.md) · → [`02-terminal-termios.md`](02-terminal-termios.md)

## Цель

Понять file descriptor как process-local handle и научиться писать loops, корректно обрабатывающие partial `read`/`write`, EOF и ошибки.

## Prerequisite check

1. Чем pointer отличается от integer handle?
2. Кто владеет heap allocation и когда её освобождают?
3. Что такое exit status?

## Kernel vs user space

Программа выполняется в user space и не может напрямую управлять kernel resources как обычной памятью. Для операций с files, processes, sockets и устройствами она обращается к kernel через system calls.

Не каждая C library function обязательно является syscall один-в-один, но `read`, `write`, `open`, `close` — хороший учебный интерфейс системного I/O.

## File descriptor

File descriptor (**fd**) — маленькое целое число в process-local descriptor table.

Традиционно:

```text
0 stdin
1 stdout
2 stderr
```

FD — не «сам файл». Он ссылается на kernel-managed open-file state.

```text
process fd table
  fd 3 ──────> open file description ──────> underlying file/device/pipe
```

Несколько descriptors/processes могут ссылаться на связанное underlying open state; позже это станет критично после `fork`/`dup2`.

## `open` / `close`

```c
#include <fcntl.h>
#include <unistd.h>

int fd = open("data.bin", O_RDONLY);
if (fd == -1) {
    /* error, errno set */
}
```

Успех `open` даёт fd. Owner процесса/компонента должен затем `close(fd)` ровно когда resource больше не нужен.

Descriptor leak похож по структуре на memory leak: resource acquired, cleanup потерян.

## `read`

Conceptual signature:

```c
ssize_t read(int fd, void *buf, size_t count);
```

Return:

- `> 0` — столько bytes реально прочитано;
- `0` — EOF для подходящего stream/file context;
- `-1` — error, смотри `errno`.

Критично: успешный `read` не обязан вернуть весь requested `count`.

## `write`

```c
ssize_t write(int fd, const void *buf, size_t count);
```

Успешный return может быть меньше `count`. Надёжная программа должна продвигать offset и дописывать оставшиеся bytes, если её контракт требует полного transfer.

## `ssize_t` vs `size_t`

`size_t` unsigned и описывает sizes. `ssize_t` signed, потому что системный I/O должен вернуть и byte count, и `-1` error sentinel.

Нельзя бездумно сохранять return `read()` в `size_t`: `-1` превратится в огромное unsigned value.

## `errno`

После syscall/library failure некоторые APIs устанавливают thread-local `errno`.

Правило:

> проверяй `errno` только после API, которое сигнализировало failure согласно своему контракту.

`errno` не обязан сбрасываться в 0 после successful operation.

`perror("read")` удобно печатает context + текущий errno message.

## `EINTR`

Некоторые blocking operations могут завершиться `-1`/`EINTR`, если обработан signal до завершения операции. Для соответствующих loops нужно решить, retry операция безопасно или signal должен изменить control flow.

Не пиши «retry любой error бесконечно».

## Full write loop

Псевдокод:

```text
offset = 0
while offset < total:
    n = write(fd, buf + offset, total - offset)
    if n > 0:
        offset += n
    else if n < 0 and errno == EINTR:
        retry
    else:
        fail
```

Для `write` return 0 при положительном remaining count — unusual condition; robust abstraction не должна spin бесконечно.

## EOF != error

`read == 0` означает конец stream/file, а не failure. Это отдельное normal control-flow состояние.

## Exercise — file copy

Напиши `copy_fd.c`, который копирует source file в destination через `open/read/write/close`.

Требования:

- fixed-size buffer;
- loop до EOF;
- partial write loop;
- error cleanup;
- destination open flags/permissions осознанны;
- empty file;
- файл больше buffer;
- никаких `fread/fwrite` — сейчас изучаем descriptor I/O.

Разбор: [`01-file-descriptors-io.solution.md`](01-file-descriptors-io.solution.md).

## Project slice

Shell пока не запускаем. В [`project/README.md`](project/SPEC.md) нарисуй будущую ownership map descriptors:

```text
shell process owns stdin/stdout/stderr
child may inherit descriptors
redirection/pipes create temporary fds
unused ends must close
```

## Exit check

Объясни, почему один successful `write(fd, buf, 4096)` не является универсальной гарантией записи всех 4096 bytes.
