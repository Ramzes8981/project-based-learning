# 7.3 — Как записать bytes так, чтобы будущая версия программы могла их прочитать

**Теория:** ~95 мин · **Практика/project:** ~4–6 часов · **С телефона:** теория — да

← [`02-page-cache-durability.md`](02-page-cache-durability.md) · → [`05-pager-records-cursor.md`](05-pager-records-cursor.md)

## Проблема

`fwrite(&my_struct, sizeof my_struct, 1, f)` looks easy but file becomes hostage to host layout: padding, type sizes, endianness, compiler/ABI changes.

A persistent database needs explicit **binary format**.

## Serialization

**Serialization** converts logical values into specified byte representation; deserialization reverses it after validation.

Normative format must state:

```text
magic/version
field widths
byte order
offsets/lengths
reserved bytes
maximum sizes
error policy
```

## Fixed-width fields

If disk field is 32-bit unsigned little-endian, use `uint32_t` value + explicit encode/decode bytes. Host struct alignment must not leak into file.

## Length arithmetic

Untrusted/corrupted file field is attacker-like input.

Before:

```text
offset + length
count * record_size
page_no * page_size
```

check representability and file/page bounds. Reject impossible state before pointer arithmetic/read allocation.

## Versioning

Magic catches wrong file type; version tells parser which contract applies. Unknown future version should fail explicitly rather than be interpreted as current layout.

## Page

SimpleDB divides file into fixed-size **database pages**. This is a storage-format page, conceptually similar in size batching motivation to OS pages but not the same mechanism and need not equal OS page size.

## Practice

Implement encode/decode of one page header/record fixture from [`project/FORMAT.md`](project/FORMAT.md). Test exact golden bytes, truncated input, wrong magic/version and maximal length fields.

Разбор: [`04-binary-format-pages-serialization.solution.md`](04-binary-format-pages-serialization.solution.md).

## Exit check

Why does “same compiler on my laptop” not make raw struct persistence a stable format?