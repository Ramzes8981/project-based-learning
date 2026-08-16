#!/usr/bin/env python3
"""Reference client for course KV protocol v1."""

from __future__ import annotations

import argparse
import socket
import struct

MAX_FRAME = 1_048_576
VERSION = 1
OPS = {"get": 0x01, "set": 0x02, "delete": 0x03}
STATUS = {0: "OK", 1: "NOT_FOUND", 2: "BAD_REQUEST", 3: "TOO_LARGE", 4: "BUSY", 5: "INTERNAL_ERROR"}


def read_exact(sock: socket.socket, n: int) -> bytes:
    parts = bytearray()
    while len(parts) < n:
        chunk = sock.recv(n - len(parts))
        if not chunk:
            raise EOFError("connection closed mid-frame")
        parts.extend(chunk)
    return bytes(parts)


def frame(op: int, key: bytes, value: bytes | None = None) -> bytes:
    if not key or len(key) > 0xFFFF:
        raise ValueError("key length out of u16/core range")
    if op == 0x02:
        assert value is not None
        payload = struct.pack("!HI", len(key), len(value)) + key + value
    else:
        payload = struct.pack("!H", len(key)) + key
    body = struct.pack("!BBH", VERSION, op, 0) + payload
    if len(body) > MAX_FRAME:
        raise ValueError("frame too large")
    return struct.pack("!I", len(body)) + body


def read_response(sock: socket.socket, expected_op: int) -> tuple[int, bytes]:
    (n,) = struct.unpack("!I", read_exact(sock, 4))
    if n < 4 or n > MAX_FRAME:
        raise ValueError(f"invalid response body length {n}")
    body = read_exact(sock, n)
    version, op, status = struct.unpack("!BBH", body[:4])
    if version != VERSION or op != (expected_op | 0x80):
        raise ValueError("unexpected response header")
    if status not in STATUS:
        raise ValueError(f"unknown response status {status}")
    payload = body[4:]
    if expected_op == 0x01 and status == 0:
        if len(payload) < 4:
            raise ValueError("short GET response")
        (value_len,) = struct.unpack("!I", payload[:4])
        if len(payload[4:]) != value_len:
            raise ValueError("GET response length mismatch")
        payload = payload[4:]
    elif payload:
        raise ValueError("unexpected response payload")
    return status, payload


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("host")
    p.add_argument("port", type=int)
    p.add_argument("op", choices=OPS)
    p.add_argument("key")
    p.add_argument("value", nargs="?")
    args = p.parse_args()

    op = OPS[args.op]
    value = args.value.encode() if args.value is not None else None
    if op == 0x02 and value is None:
        p.error("set requires value")

    with socket.create_connection((args.host, args.port), timeout=3) as s:
        s.sendall(frame(op, args.key.encode(), value))
        status, payload = read_response(s, op)
    print(STATUS[status])
    if payload:
        print(payload.decode("utf-8", errors="backslashreplace"))


if __name__ == "__main__":
    main()
