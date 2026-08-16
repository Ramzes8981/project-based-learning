# 7.3 — FUSE 3: filesystem callbacks в userspace

**Теория:** ~75 мин  
**Guided lab:** ~2–4 часа  
**С телефона:** теория — да

← [`02-page-cache-durability.md`](02-page-cache-durability.md) · → [`04-binary-format-pages-serialization.md`](04-binary-format-pages-serialization.md)

## Цель

Увидеть filesystem как callback interface между kernel VFS и userspace daemon, применив function pointers из Module 1.

## Control flow

```text
application open/stat/read/readdir
↓
VFS path/inode logic
↓
FUSE kernel interface
↓
libfuse dispatch
↓
our callbacks in userspace process
↓
errno/data response
```

FUSE project состоит из kernel interface и userspace library/runtime. Мы используем **high-level synchronous libfuse 3 API**, где callbacks работают с paths.

## Version contract

Course lab использует:

```c
#define FUSE_USE_VERSION 31
#include <fuse.h>
```

и `pkg-config fuse3 --cflags --libs` для compile/link. Полный локальный contract/signatures находится в [`FUSE3_MINI_REFERENCE.md`](FUSE3_MINI_REFERENCE.md).

## Core callback table

`struct fuse_operations` содержит function pointers. Для read-only toy FS нужны:

```text
getattr
readdir
open
read
```

Это прямое применение callback-table model: library выбирает, когда вызвать функцию, а `user_data`/global state lifetime должен быть валиден всё время FUSE loop.

## Callback не равен user syscall one-to-one

Kernel/cache/VFS способны выполнять иной request pattern, чем наивная модель «один `cat` → один callback read». Поэтому implementation обязана корректно обрабатывать любой valid offset/size sequence.

## `getattr`

Заполняет `struct stat` для path. Unknown path → negative errno such as `-ENOENT`. Directory/file mode и size должны соответствовать тому, что затем делают `readdir/read`.

## `readdir`

Для root перечисляет минимум `.` и `..` плюс virtual files. `filler` — ещё один callback: FUSE передаёт function pointer твоему callback.

## `read`: offset/size

Для virtual content длины `len`:

```text
if offset < 0 -> EINVAL-style error
if offset >= len -> 0 (EOF)
available = len - offset
take = min(size, available)
copy exactly take bytes
return take
```

Не вычисляй `offset + size > len` бездумно: signed/unsigned conversion и overflow хуже, чем subtract-from-available pattern.

## Errors

High-level callbacks обычно возвращают `0`/positive byte count on success или **negative errno** (`-ENOENT`, `-EACCES`, ...). Не возвращай случайный `-1`, теряя semantic reason.

## Guided lab

1. root directory;
2. read-only `/hello`;
3. read-only `/stats`, content generated при read;
4. log path + offset + requested size;
5. test reads with `dd`/small buffers, not only `cat`;
6. unmount/cleanup.

Если FUSE недоступен в WSL/environment, выполняй lab в Ubuntu VM/native Linux. Environment limitation не является conceptual failure.

## Exit check

Объясни путь `cat mount/stats` через VFS → FUSE → callback table → offset-based read response.
