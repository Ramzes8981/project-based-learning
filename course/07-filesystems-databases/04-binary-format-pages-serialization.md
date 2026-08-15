# 7.4 — Binary formats, pages и serialization

**Теория:** ~90 мин  
**Упражнение:** ~60 мин  
**Project slice:** ~2–3 часа  
**С телефона:** да

← [`03-fuse-userspace-filesystem.md`](03-fuse-userspace-filesystem.md) · → [`05-pager-records-cursor.md`](05-pager-records-cursor.md)

## Цель

Спроектировать stable on-disk format без raw `fwrite(struct)` assumptions.

## Почему page-oriented storage

Storage engines обычно группируют bytes fixed-size pages:

```text
file offset = page_number * PAGE_SIZE
```

Плюсы:

- единица I/O/cache;
- predictable offsets;
- index nodes fit pages;
- dirty/eviction bookkeeping удобно page-based.

SQLite — реальный пример page-oriented DB; его официальный формат хранит main DB как последовательность pages и использует interior/leaf B-tree pages. citeturn526026search0turn526026search1

Наш SimpleDB format проще и полностью определён в `project/FORMAT.md`.

## Почему нельзя dump C struct

```c
struct Header {
    uint8_t type;
    uint32_t count;
};
```

Compiler может вставить padding между fields. Endianness host также влияет на byte order multi-byte integers.

Кроме того:

- type sizes/ABI могут различаться;
- struct layout меняется между versions;
- pointers нельзя persist как process addresses.

Поэтому disk format использует explicit offsets + encoded integer widths.

## Magic и version

File header должен позволить отличить:

- наш DB от random file;
- supported version от incompatible format.

Например conceptual:

```text
magic[8]
format_version u16
page_size u16/u32
root_page u32
...
```

Exact course format в project spec.

## Endianness

Выбирается один canonical byte order независимо от host. Course SimpleDB использует little-endian explicit encoding, потому что так указано в FORMAT — выбор мог быть и другим.

Важно не «little лучше», а reproducible contract.

## Serialization helpers

Вместо casts вроде:

```c
*(uint32_t *)(buf + offset)
```

которые могут нарушить alignment/aliasing, course code должен использовать explicit encode/decode bytes или `memcpy` + endian conversion with proven preconditions.

## Bounds

Decoder всегда получает:

```text
buffer + buffer_len
```

и до чтения field проверяет, что bytes существуют.

Это тот же pattern, что network framing.

## Checksums preview

Checksum может обнаруживать случайное corruption, но не делает storage transactional/authenticated. Core format checksum не требует; можно добавить transfer feature.

## Exercise

Спроектируй 32-byte header для toy file:

- 4-byte magic;
- version;
- record count;
- payload size;
- reserved bytes.

Нарисуй offset/width каждого field и manually encode one example as hex bytes.

Разбор: [`04-binary-format-pages-serialization.solution.md`](04-binary-format-pages-serialization.solution.md).

## Project slice

Реализуй SimpleDB file header + empty root page according to [`project/FORMAT.md`](project/FORMAT.md). Добавь hex-dump test fixture.

## Exit check

Почему stable file format является protocol между версиями программы, а не private `struct` layout?
