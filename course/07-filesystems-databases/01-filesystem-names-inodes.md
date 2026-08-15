# 7.1 — Pathnames, directory entries, inodes и open-file state

**Теория:** ~75 мин  
**Lab:** ~60 мин  
**С телефона:** теория — да

← [`README`](README.md) · → [`02-page-cache-durability.md`](02-page-cache-durability.md)

## Цель

Перестать считать filename самим file object и понять identity/link/open-handle модель Unix-like filesystem.

## Pathname — способ найти object

Строка:

```text
/home/user/data.txt
```

не является «файлом внутри kernel». Pathname resolution проходит components directory tree и находит filesystem object.

Упрощённо:

```text
pathname component
  ↓ directory lookup
name -> inode-like object identifier
  ↓
metadata + file data mapping
```

Точные on-disk structures зависят от filesystem; inode — удобная Unix abstraction, а не требование ко всем файловым системам мира.

## Directory entry

Directory связывает **name** с object/inode identity.

Следовательно, один object может иметь несколько names через hard links.

```text
a.txt ─┐
       ├─> inode 123
b.txt ─┘
```

Удаление одного name (`unlink`) не обязано уничтожать file data, если существуют другие links или открытые references.

## Hard link

Hard link — ещё одна directory entry на тот же inode-like object.

Обычно нельзя hard-link directory обычным пользователем; hard links также не пересекают filesystem boundaries.

## Symbolic link

Symlink — отдельный filesystem object, содержимое которого задаёт pathname target.

Он может быть dangling, если target исчез.

Hard link и symlink — принципиально разные semantics.

## Metadata

Inode-like metadata содержит, например:

- file type;
- permissions;
- owner/group;
- size;
- timestamps;
- link count;
- data-block mapping information.

Имя обычно хранится в directory, а не «в inode как единственное имя».

## Open file state

`open()` создаёт descriptor reference на open-file state. После:

```text
open("data") -> fd
unlink("data")
```

process всё ещё может читать/писать через уже открытый fd, пока underlying object жив благодаря open reference. Name исчез из directory namespace, но object не обязан исчезнуть немедленно.

Это важный pattern для temp files/atomic replacement.

## File offset

Sequential `read/write` используют current file offset в open-file description. `dup`/`fork` могут привести descriptors к shared offset state.

`pread/pwrite` conceptually работают по explicit offset и не двигают shared current offset — полезно для pager.

## Permissions

Permissions участвуют в pathname/open/access checks, но authorization сложнее mode bits: ACLs, capabilities, mount options и LSM могут добавлять policy.

Core требует понимать `rwx` + owner/group/other и directory execute/search semantics.

## Lab

На отдельной test directory:

1. создай file;
2. `stat`/`ls -li`;
3. создай hard link;
4. сравни inode numbers/link count;
5. создай symlink;
6. открой file маленькой программой, затем unlink pathname и продолжи чтение через fd;
7. inspect `/proc/<pid>/fd` при необходимости.

## Causal questions

1. Почему два pathnames могут быть одним file object?
2. Почему unlink открытого file не обязан немедленно освобождать data?
3. Чем symlink отличается от hard link при удалении target?
4. Почему pathname не является стабильным object identity?

## Exit check

Объясни цепочку `path -> directory entry -> inode/object -> open fd`, не называя все четыре одним «файлом».
