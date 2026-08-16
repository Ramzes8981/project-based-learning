# 7.1 — Почему имя файла и сам файл — разные сущности

**Теория:** ~80 мин · **Лаб:** ~70 мин · **С телефона:** теория — да

← [`README`](README.md) · → [`02-page-cache-durability.md`](02-page-cache-durability.md)

## Проблема

Beginner model:

> `/tmp/a.txt` — это файл.

Но one filesystem object can have multiple hard-link names, and a name can disappear while already-open fd still accesses object. So path string is not object identity.

## Directory entry

A directory maps a name to filesystem object identifier. On common Unix filesystems that object is represented by an **inode**.

Useful mental model:

```text
directory path/name
→ directory entry
→ inode-like file object metadata
→ data blocks/extents
```

Exact on-disk implementation differs by filesystem; Linux VFS exposes inode abstraction even if storage details vary.

## Hard link

Hard link creates another directory entry referring to same underlying inode/object.

```text
a.txt ─┐
      ├→ inode X → data
b.txt ─┘
```

Deleting one name decreases link count; object can remain while another link or open reference exists.

## Open fd survives unlink

If process opens file then pathname is unlinked, fd may continue referring to open file description/object until last relevant reference closes. This is why temp-file patterns can safely unlink after open on Unix-like systems.

## Symlink differs

Symbolic link stores a path-like reference resolved later; it is a different filesystem object, not another hard-link name to same inode.

## Metadata

Mode/owner/timestamps/size/link count are metadata. Do not assume inode number is globally unique forever or across filesystems; it is context-dependent identifier.

## Practice

On disposable directory:

1. create file;
2. make hard link and symlink;
3. compare `stat` results;
4. open fd, unlink original name, read via fd;
5. explain which references keep object reachable.

## Exit check

Why can “path no longer exists” and “process can still read the opened file” both be true?