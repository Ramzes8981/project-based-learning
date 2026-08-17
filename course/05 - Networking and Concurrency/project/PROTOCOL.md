# KV protocol v1 — wire specification

Этот файл делает wire contract автономным и фиксированным для public tools/tests.

## Byte order

Все multi-byte integers — **big-endian**.

## Envelope

```text
u32 body_len       # bytes after this prefix
u8  version        # exactly 1
u8  opcode
u16 flags_or_status
payload...
```

Maximum `body_len`: **1 MiB (1_048_576 bytes)**. Server может выбрать меньшие key/value domain limits, но обязан ответить documented error, а не читать за frame.

Request `flags` в core v1 должен быть `0`.

## Opcodes

```text
0x01 GET
0x02 SET
0x03 DELETE   # transfer feature; tool supports it
```

Response opcode = request opcode OR `0x80`.

## Status values in response u16

```text
0 OK
1 NOT_FOUND
2 BAD_REQUEST
3 TOO_LARGE
4 BUSY
5 INTERNAL_ERROR
```

Unknown status is protocol error for reference client.

## GET request

```text
header
u16 key_len
key bytes
```

`key_len > 0` in core. Payload must contain exactly declared bytes.

### GET OK response

```text
header(status=OK)
u32 value_len
value bytes
```

### GET NOT_FOUND

Header only, no payload.

## SET request

```text
header
u16 key_len
u32 value_len
key bytes
value bytes
```

Core treats key/value as arbitrary bytes; application may impose stricter domain policy but must document it. No NUL terminator is sent.

SET OK response: header only.

## DELETE request

Same key payload as GET. OK/NOT_FOUND response header only.

## Malformed frame policy

Structural violations (wrong version, flags, length mismatch, unknown opcode) produce `BAD_REQUEST` when enough data exists to respond, then connection may be closed according to server policy.

Oversize prefix may be rejected/connection closed without allocating body.

EOF mid-frame: discard partial request and close connection; never execute partial data.

## Resource contract

Length validation happens before allocation. A client may not force allocation proportional to an unchecked 32-bit length.
