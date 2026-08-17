#!/usr/bin/env python3
"""Create corrupted COPIES of a capstone storage file for recovery tests.

Never modifies the source file. Intended only for local course fixtures.
"""

from __future__ import annotations

import argparse
import pathlib


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=pathlib.Path)
    ap.add_argument("output", type=pathlib.Path)
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--truncate", type=int, metavar="BYTES")
    group.add_argument("--flip", type=int, metavar="OFFSET")
    args = ap.parse_args()

    source = args.source.read_bytes()
    data = bytearray(source)

    if args.truncate is not None:
        if args.truncate < 0 or args.truncate > len(data):
            raise SystemExit("truncate bytes must be inside source size")
        data = data[: len(data) - args.truncate]
    else:
        assert args.flip is not None
        if args.flip < 0 or args.flip >= len(data):
            raise SystemExit("flip offset outside file")
        data[args.flip] ^= 0x01

    if args.output.resolve() == args.source.resolve():
        raise SystemExit("output must differ from source")
    args.output.write_bytes(data)
    print(f"wrote corrupted copy: {args.output} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
