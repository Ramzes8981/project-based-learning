#!/usr/bin/env python3
"""Independent read-only inspector for SimpleDB v1 course format.

It validates structural header facts and prints common page headers. It does not implement tree search/insert.
"""

from __future__ import annotations

import argparse
import pathlib
import struct

PAGE_SIZE = 4096
MAGIC = b"SDBv1\x00\x00\x00"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("db", type=pathlib.Path)
    ap.add_argument("--pages", action="store_true")
    args = ap.parse_args()

    data = args.db.read_bytes()
    if len(data) < PAGE_SIZE or len(data) % PAGE_SIZE:
        raise SystemExit(f"invalid file length {len(data)}; expected whole {PAGE_SIZE}-byte pages")

    magic = data[:8]
    version, page_size, root_page, page_count = struct.unpack_from("<HHII", data, 8)
    (records,) = struct.unpack_from("<Q", data, 20)

    actual_pages = len(data) // PAGE_SIZE
    print(f"magic={magic!r} version={version} page_size={page_size}")
    print(f"root_page={root_page} page_count={page_count} records={records} actual_pages={actual_pages}")

    errors: list[str] = []
    if magic != MAGIC:
        errors.append("bad magic")
    if version != 1:
        errors.append("unsupported version")
    if page_size != PAGE_SIZE:
        errors.append("unexpected page size")
    if page_count != actual_pages:
        errors.append("page_count/file-length mismatch")
    if page_count < 2:
        errors.append("expected header + root page")
    if root_page == 0 or root_page >= page_count:
        errors.append("root page out of range")

    if args.pages:
        for page_no in range(1, actual_pages):
            off = page_no * PAGE_SIZE
            page_type, flags, cell_count = struct.unpack_from("<BBH", data, off)
            parent, next_leaf = struct.unpack_from("<II", data, off + 4)
            print(f"page={page_no} type={page_type} flags={flags} cells={cell_count} parent={parent} next_leaf={next_leaf}")

    if errors:
        for error in errors:
            print("ERROR:", error)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
