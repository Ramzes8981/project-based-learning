# 7.4 — Binary formats, pages и serialization

**Теория:** ~95 мин  
**Упражнение:** ~60 мин  
**Project slice:** ~2–3 часа  
**С телефона:** да

← [`03-fuse-userspace-filesystem.md`](03-fuse-userspace-filesystem.md) · → [`05-pager-records-cursor.md`](05-pager-records-cursor.md)

## Цель

Спроектировать stable on-disk format без raw `fwrite(struct)`/pointer-cast assumptions.

## Page-oriented storage

Fixed-size page — удобная единица I/O/cache/index layout:

```text
page_offset = page_number * PAGE_SIZE
```

Но multiplication проверяется до syscall: malformed page number не должен wrap `off_t`/size arithmetic.

SimpleDB использует 4096-byte pages и полностью course-owned format из [`project/FORMAT.md`](project/FORMAT.md).

## Почему raw struct dump плохой format

Compiler может вставлять padding/alignment. Host endianness и ABI влияют на integer/layout. Pointer fields вообще являются process addresses, бессмысленными после restart.

Stable format задаёт **offset + width + byte order + semantic meaning** каждого field.

## Header

Magic/version/page size/root page/page count позволяют отличить valid supported DB от random/incompatible bytes.

Validation order важен:

```text
file at least one header page
magic exact
version supported
page_size expected
page_count consistent with actual file length
root_page within allowed range
only then traverse pages
```

## Canonical endianness

SimpleDB v1 использует explicit little-endian multi-byte integers. Host endianness не должен менять file bytes.

## Safe decode/encode

Избегай:

```c
*(uint32_t *)(buf + off)
```

Проблемы: alignment, aliasing, out-of-bounds, host byte order.

Лучше explicit byte helpers, например conceptually:

```text
decode_u32_le(p[0..4])
encode_u32_le(value, p[0..4])
```

или `memcpy` в suitably sized integer + explicit endian conversion после bounds check. Никогда не dereference unaligned cast pointer.

## Decoder rule

Каждая функция получает buffer length. До чтения width `w`:

```text
offset <= len
w <= len - offset
```

Subtract-from-remaining pattern избегает overflow `offset + w`.

## Determinism

Reserved bytes и unused cell tail в course format обнуляются. Это облегчает hex fixtures/reproducibility и уменьшает accidental leakage старого memory contents на диск.

## Checksums

Checksum обнаруживает часть случайной corruption, но не даёт transaction atomicity или authentication. Core v1 не требует checksum; transfer feature может добавить page checksum с version bump/flag.

## Exercise

Спроектируй 32-byte toy header: magic/version/count/payload-size/reserved. Нарисуй offsets/widths и вручную encode one sample in hex. Затем напиши encode/decode helpers с boundary tests.

Разбор: [`04-binary-format-pages-serialization.solution.md`](04-binary-format-pages-serialization.solution.md).

## Project slice

Создай SimpleDB header + empty root page согласно `FORMAT.md`; проверь file через [`project/tools/inspect_db.py`](project/tools/inspect_db.py) и собственный hex dump.

## Exit check

On-disk format — protocol между версиями программы; private C layout не является protocol.
