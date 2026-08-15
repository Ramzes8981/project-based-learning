# SimpleDB File Format v1

Этот формат принадлежит курсу и намеренно проще production databases.

All multi-byte integers are **little-endian**.

## Global constants

```text
PAGE_SIZE      = 4096 bytes
FILE_HEADER    = one full page (page 0)
DATA/TREE PAGE numbers start at 1
MAX_VALUE      = 256 bytes core default
```

Если implementation меняет MAX_VALUE, это записывается в header/config and tests consistently.

## File header page (page 0)

```text
offset size field
0      8    magic = "SDBv1\0\0\0" exact bytes
8      2    format_version = 1
10     2    page_size = 4096
12     4    root_page
16     4    page_count including page0
20     8    user_record_count
28     ...  reserved zeros
```

Unknown magic/version/page size -> reject file.

## Common tree page header

```text
offset size field
0      1    page_type: 1=leaf, 2=internal
1      1    flags/reserved
2      2    cell_count
4      4    parent_page (0 means none/root)
8      4    next_leaf (leaf only; 0 if none)
12     4    reserved
16     ...  cells
```

## Leaf cell

Core fixed-size slot simplifies implementation:

```text
u32 key
u16 value_len
u16 reserved
u8  value[MAX_VALUE]
```

Only first `value_len` bytes are logical value. Remaining bytes zeroed for deterministic files/tests.

Leaf capacity:

```text
floor((PAGE_SIZE - HEADER_SIZE) / CELL_SIZE)
```

## Internal page

Internal page stores sorted separator entries:

```text
u32 child_page
u32 max_key_or_separator
```

plus one rightmost child according to chosen implementation. Exact separator invariant must be documented by student and used consistently.

Course accepts either:

A. each entry describes child + maximum key of that child, or
B. classic separator keys + n+1 child layout.

Choose **one** and update project README/tests. Do not mix them.

## Persistence limitations

Version 1 has no checksum, WAL, free-page list, transaction ID or crash-safe multi-page commit. These omissions are intentional learning points.
