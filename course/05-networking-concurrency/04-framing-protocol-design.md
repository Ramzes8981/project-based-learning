# 5.4 — Framing и binary application protocol

**Теория:** ~90 мин  
**Project slice:** ~4–7 часов  
**С телефона:** теория — да

← [`03-socket-api-getaddrinfo.md`](03-socket-api-getaddrinfo.md) · → [`05-threads-races-sync.md`](05-threads-races-sync.md)

## Цель

Спроектировать bounded length-prefixed KV protocol и parser state machine, корректный при произвольном TCP chunking.

## Frame envelope

Course protocol v1 подробно зафиксирован в [`project/PROTOCOL.md`](project/PROTOCOL.md). Общий envelope:

```text
u32 body_len (big-endian; bytes after prefix)
u8  version
u8  opcode
u16 flags/status
operation-specific payload
```

Никакой raw `send(struct Request)`: C padding, host endianness, ABI layout и pointer fields делают такой wire format непереносимым.

## Bounds before allocation

Для untrusted `body_len`:

```text
read exactly 4-byte prefix
parse u32
validate MIN <= body_len <= MAX_FRAME
only then allocate/read body
```

Даже 4-byte prefix может прийти несколькими `recv` calls.

## Integer arithmetic

Нельзя сначала бездумно вычислить:

```text
header + key_len + value_len
```

на untrusted lengths и только потом проверить. Используй checked/add-subtract-from-remaining logic:

```text
remaining >= key_len
remaining - key_len >= value_len
```

и protocol-specific maximums.

## Parser phases

```text
READ_PREFIX
VALIDATE_LENGTH
READ_BODY
PARSE_FIXED_HEADER
VALIDATE_VERSION/OPCODE/FLAGS
PARSE_LENGTH FIELDS
VALIDATE PAYLOAD BOUNDS
EXECUTE
ENCODE RESPONSE
```

Blocking helper `read_exact` может скрыть transport chunks, но обязан корректно обрабатывать EOF/error. Event loop позже сохранит эти phases как persistent connection state.

## Bytes vs text

Wire payload — bytes. Если project contract определяет keys/values как UTF-8 text, validation выполняется **после** structural lengths. C core server может считать payload arbitrary bytes до NUL-free/string conversion policy; exact project v1 contract описан в `PROTOCOL.md`.

## Security/error cases

- overlarge frame;
- too-small body;
- unknown version/opcode;
- reserved flags nonzero;
- inconsistent lengths;
- EOF mid-prefix/body;
- allocation failure;
- slow peer;
- response length overflow.

## Project slice

Сначала sequential single-client KV protocol на собственной Hash Table. Concurrency добавляется только после deterministic protocol tests.

Course-provided `tools/client.py` — reference peer для wire contract, не server solution.

## Exit check

Почему transport `recv` result нельзя напрямую трактовать как one request или C struct?
