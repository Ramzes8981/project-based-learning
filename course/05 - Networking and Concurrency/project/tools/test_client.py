#!/usr/bin/env python3
"""Regression checks for the course KV protocol reference client."""

from __future__ import annotations

import struct
import unittest

from client import read_response


class BytesSocket:
    def __init__(self, data: bytes) -> None:
        self._data = bytearray(data)

    def recv(self, n: int) -> bytes:
        chunk = bytes(self._data[:n])
        del self._data[:n]
        return chunk


def response_frame(op: int, status: int, payload: bytes = b"") -> bytes:
    body = struct.pack("!BBH", 1, op | 0x80, status) + payload
    return struct.pack("!I", len(body)) + body


class ClientProtocolTests(unittest.TestCase):
    def test_unknown_status_is_protocol_error(self) -> None:
        sock = BytesSocket(response_frame(0x01, 0xFFFF))
        with self.assertRaisesRegex(ValueError, "unknown response status"):
            read_response(sock, 0x01)

    def test_known_not_found_status_is_accepted(self) -> None:
        sock = BytesSocket(response_frame(0x01, 1))
        status, payload = read_response(sock, 0x01)
        self.assertEqual(status, 1)
        self.assertEqual(payload, b"")


if __name__ == "__main__":
    unittest.main()
