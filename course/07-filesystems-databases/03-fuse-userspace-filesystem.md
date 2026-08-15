# 7.3 — FUSE: filesystem interface в userspace

**Теория:** ~65 мин  
**Guided lab:** ~2–4 часа  
**С телефона:** теория — да

← [`02-page-cache-durability.md`](02-page-cache-durability.md) · → [`04-binary-format-pages-serialization.md`](04-binary-format-pages-serialization.md)

## Цель

Увидеть filesystem как набор операций/contracts, которые kernel VFS может делегировать userspace process через FUSE.

## Зачем FUSE

Обычный application вызывает:

```text
open/read/stat/readdir/...
```

Kernel VFS выбирает filesystem implementation.

FUSE позволяет части filesystem logic жить userspace:

```text
application syscall
   ↓
VFS/FUSE kernel interface
   ↓
userspace FUSE daemon callbacks
   ↓
response to kernel/application
```

## High-level API model

Для учебного read-only filesystem нас интересуют callbacks вроде:

- `getattr` — metadata/path type;
- `readdir` — directory entries;
- `open` — validate open request;
- `read` — вернуть requested byte range.

Точные signatures зависят от libfuse 3 API version. Mandatory conceptual theory находится здесь; перед сборкой конкретного lab допустимо открыть current official API docs.

Официальные libfuse examples по-прежнему используют `fuse3` build metadata и отдельные high/low-level examples. citeturn259580search8turn526026search3

## Callback != syscall one-to-one

Kernel/page cache может объединять/изменять pattern requests. Не предполагай «один user `cat` = ровно один `read` callback».

## Path and metadata

Virtual filesystem может вообще не иметь backing disk file. Callback сам synthesizes metadata/content.

Пример:

```text
/course/status
```

может при каждом read генерировать current process statistics.

## Offset и size

`read` callback получает offset + requested size. Нужно вернуть correct slice:

```text
if offset >= content_len -> EOF/0
else return min(size, content_len-offset) bytes
```

Нельзя всегда копировать полный content regardless buffer/request.

## Errors

FUSE API представляет filesystem errors через errno-style codes according to interface conventions. `ENOENT`, `EACCES` и др. должны отражать contract, а не random `-1`.

## Guided lab

Не пиши full filesystem.

1. Собери current libfuse 3 minimal high-level example или собственный equivalent по documented API.
2. Экспортируй root directory.
3. Добавь virtual read-only file `hello`.
4. Добавь `stats`, content generated at read time.
5. Логируй callback type/path/offset для наблюдения.
6. Корректно unmount/cleanup.

## What can go wrong

- stale mount после crash;
- неправильный `st_mode`/metadata;
- read ignores offset;
- callback возвращает wrong errno;
- lab запускается там, где FUSE unavailable/permissions blocked.

Environment failure не считается провалом CS-концепции.

## Exit check

Объясни, как `cat /mount/stats` превращается в kernel VFS operations и userspace callbacks.
