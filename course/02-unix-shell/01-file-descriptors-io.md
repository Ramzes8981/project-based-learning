# 2.1 — Что такое запущенная программа и как она просит ОС о работе

**Теория:** ~80 мин  
**Практика:** ~80 мин  
**С телефона:** теория — да; практика — Linux/WSL2

← [`README`](README.md) · → [`02-terminal-termios.md`](02-terminal-termios.md)

## Проблема

C function сама по себе не умеет вращать диск, читать keyboard device или создавать новый running program. Эти ресурсы контролирует operating system.

Нужна модель того, **кто именно выполняется** и как этот running code обращается к kernel.

## Program file vs running process

Executable file на диске — пассивные bytes. После запуска ОС создаёт живой execution context с собственным состоянием/resources.

Такой экземпляр выполняющейся программы называется **процессом (process)**.

```text
executable file
   ↓ start
process
  ├─ executing state
  ├─ memory/address space
  └─ OS-managed resources
```

Как ОС планирует выполнение и организует память, разберём позже. Сейчас важен факт: process — не то же самое, что executable file.

## User space и kernel boundary

Обычный application code выполняется с ограниченными privileges. Kernel управляет shared hardware/resources и проверяет requests.

Когда process просит kernel выполнить определённую operation через установленный OS interface, на низком уровне это **системный вызов (system call, syscall)**.

В C мы часто вызываем library wrapper, например `read()`, который уже организует соответствующий system interface.

Не нужно сейчас знать instruction-level calling convention для этого перехода.

## Проблема: как process ссылается на открытый resource

После `open("notes.txt", ...)` kernel должен вернуть process-у удобный handle. В Unix-like systems это небольшое integer value — **файловый дескриптор (file descriptor, fd)**.

```text
process
  fd 3 ─────→ kernel open-file state ─────→ file object/device/pipe/...
```

`fd` — не «адрес файла» и не сам файл. Это process-local handle.

## Standard descriptors

Обычно при запуске процесса уже открыты:

```text
0  stdin
1  stdout
2  stderr
```

Именно поэтому `write(1, ...)` может писать туда, куда shell настроил stdout.

## `read` / `write`: bytes, not “whole message”

Simplified signatures:

```c
ssize_t read(int fd, void *buf, size_t count);
ssize_t write(int fd, const void *buf, size_t count);
```

Return value:

- positive → сколько bytes реально обработано;
- `0` from `read` → EOF for stream/file semantics where applicable;
- `-1` → failure, details via `errno`.

Type `ssize_t` is signed because it must represent byte count **and** `-1` failure sentinel.

## Short I/O

Request `count = 4096` does **not** universally guarantee that one call transfers 4096 bytes. Successful `read/write` may process fewer bytes.

Correct “write all” logic loops until:

```text
all bytes written
OR error
```

## `EINTR`

Some blocking system calls can return `-1` with `errno == EINTR` when interrupted by a signal before completing work. For operations whose documented retry semantics are appropriate, wrapper retries.

Do not write generic rule «retry any errno». Error policy is operation-specific.

## Correct `write_all` pattern

```c
#include <errno.h>
#include <stddef.h>
#include <sys/types.h>
#include <unistd.h>

int write_all(int fd, const unsigned char *buf, size_t len)
{
    size_t off = 0;

    while (off < len) {
        ssize_t n = write(fd, buf + off, len - off);
        if (n > 0) {
            off += (size_t)n;
            continue;
        }
        if (n < 0 && errno == EINTR) {
            continue;
        }
        return 0;
    }
    return 1;
}
```

For regular `write` with non-zero request, `n == 0` is treated here as no-progress failure to avoid infinite loop.

## Descriptor lifetime

Successful `open` creates an fd that caller must eventually `close`. Early returns must not leak descriptors.

```text
open success
→ caller owns fd
→ use/borrow
→ close exactly once
```

This is the same ownership reasoning learned for allocations, now applied to OS resource.

## Практика

1. Open a temporary file for write/create/truncate.
2. Use your `write_all` to write bytes.
3. Close on every success/failure path.
4. Re-open for read and loop until EOF.
5. Use `strace` (if available) only after predicting which OS operations you expect.

Разбор: [`01-file-descriptors-io.solution.md`](01-file-descriptors-io.solution.md).

## Causal questions

1. Why is an fd process-local handle rather than file identity?
2. Why does one successful `write` not prove all requested bytes were written?
3. Why is `errno` meaningful only after an operation reports failure according to its contract?
4. How is `close` ownership analogous to `free`?

## Exit check

Explain: executable → process → syscall boundary → fd → byte I/O → close, without using future networking concepts.