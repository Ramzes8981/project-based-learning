# 5.4 — Как поверх TCP восстановить границы сообщений

**Теория:** ~90 мин · **Практика/project:** ~4–6 часов · **С телефона:** теория — да

← [`03-socket-api-getaddrinfo.md`](03-socket-api-getaddrinfo.md) · → [`05-threads-races-sync.md`](05-threads-races-sync.md)

## Проблема

TCP gives ordered bytes, not records. Server needs know where one request ends before decoding command/key/value.

This requires **framing**: protocol rule for message boundaries.

## Length-prefixed frame

Course protocol uses explicit fixed-width length field:

```text
+----------------+-------------------+
| payload_len    | payload bytes     |
+----------------+-------------------+
```

Exact fields are normative in [`project/PROTOCOL.md`](project/PROTOCOL.md).

## Parser state machine

Receiver cannot assume header arrives at once.

```text
NEED_HEADER
  accumulate until complete
  decode length
  validate length <= MAX_FRAME
  allocate/prepare payload safely
↓
NEED_PAYLOAD
  accumulate until payload_len bytes
↓
PROCESS_FRAME
↓
NEED_HEADER
```

EOF in `NEED_PAYLOAD` means truncated/incomplete frame, not valid shorter message.

## Validate before arithmetic/allocation

Untrusted length can cause overflow or memory exhaustion.

Order:

```text
decode fixed-width unsigned length
→ compare against protocol MAX_FRAME
→ convert to size_t only if representable/allowed
→ check any header+payload arithmetic before addition
→ allocate/read
```

Never allocate arbitrary peer-provided length first and reject later.

## Endianness

Wire format chooses byte order independently of host. Encode/decode field bytes explicitly. Do not send raw C struct: padding/layout/endianness are not wire contract.

## Error response policy

Malformed/oversized/truncated input needs deterministic policy: send error if enough state remains safe, or close connection. Avoid protocol parser trying to “resynchronize” arbitrary corrupted stream unless format explicitly supports it.

## Project stage 1

Implement protocol codec/parser and single-client server before concurrency. Tests must feed every frame split at many byte boundaries and multiple frames concatenated in one read.

## Exit check

Why is a parser that only passes “one full frame per read” tests not actually a TCP parser?