# 5.4 — Framing и binary application protocol

**Теория:** ~80 мин  
**Project slice:** ~4–7 часов  
**С телефона:** теория — да

← [`03-socket-api-getaddrinfo.md`](03-socket-api-getaddrinfo.md) · → [`05-threads-races-sync.md`](05-threads-races-sync.md)

## Цель

Спроектировать bounded length-prefixed KV protocol и parser state machine, который корректен при произвольном TCP chunking.

## Frame format

Course protocol v1:

```text
4 bytes total_payload_length (network/big-endian)
1 byte  version
1 byte  opcode
2 bytes reserved/flags
payload...
```

`total_payload_length` описывает bytes **после** 4-byte prefix.

## Operations

Минимум:

```text
GET
SET
DELETE optional/transfer
```

Payload имеет explicit lengths, а не C `\0` contracts.

Например SET:

```text
u16 key_len
u32 value_len
key bytes
value bytes
```

## Network byte order

Multi-byte integers serializing protocol должны иметь fixed byte order. Используй big-endian/network order conversion functions или explicit encode/decode helpers.

Не `send(struct Request)` raw: padding, endianness, ABI layout и pointer fields делают такой формат непереносимым/опасным.

## Bounds first

До allocation payload:

```text
read length prefix fully
validate <= MAX_FRAME
validate >= minimum header
only then allocate/read remainder
```

Если peer объявляет 4 GiB length, server не должен blindly `malloc`.

## Partial prefix

Даже 4-byte prefix может прийти в нескольких `recv` calls. Parser/reader должен уметь собирать exact N bytes.

## EOF mid-frame

Peer может закрыться после половины frame. Это malformed/incomplete request, connection закрывается по policy без чтения uninitialized memory.

## Integer arithmetic

При проверке:

```text
header + key_len + value_len
```

нужно избежать overflow. Лучше проверять каждое component и subtract-from-available pattern, чем сначала складывать untrusted lengths без guard.

## Parser phases

```text
READ_LENGTH
↓
VALIDATE_LENGTH
↓
READ_FRAME_BYTES
↓
PARSE_HEADER
↓
VALIDATE_FIELDS
↓
EXECUTE
↓
ENCODE_RESPONSE
```

Для blocking per-client code helper `read_exact` может скрыть chunking. Event loop позже потребует explicit state between readiness events.

## Project slice

Перенеси C Hash Table из Module 1 как storage и реализуй single-client/sequential server protocol до concurrency.

## Security edge cases

- oversized frame;
- zero/minimum length;
- unknown version/opcode;
- duplicate/inconsistent lengths;
- non-terminated arbitrary bytes;
- peer close mid-frame;
- allocation failure;
- slow client.

## Exit check

Почему `recv` result нельзя напрямую трактовать как `Request struct`?
