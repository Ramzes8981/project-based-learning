# 9.2 — Protocol contracts, request IDs и idempotency

**Теория:** ~75 мин  
**Design/project:** ~2–3 часа  
**С телефона:** да

← [`01-requirements-boundaries-state.md`](01-requirements-boundaries-state.md) · → [`03-queueing-latency-capacity.md`](03-queueing-latency-capacity.md)

## Цель

Спроектировать network API так, чтобы timeout/retry semantics были явными.

## Request/response contract

Protocol должен задавать:

- version;
- operation;
- request identifier where useful;
- size limits;
- encoding/byte order;
- success/error codes;
- malformed-input behavior.

Это продолжение Module 5 framing, но теперь API рассматривается как long-lived compatibility boundary.

## At-most-once illusion

Сценарий:

```text
client sends SET
server applies SET
response lost
client timeout
```

Client не знает, была operation applied или нет.

Network timeout означает **неизвестный outcome**, а не доказанный failure server operation.

## Idempotency

Operation idempotent, если повторение того же logical request не меняет final state сверх первого применения.

`SET key = value` обычно naturally idempotent по final state.

`INCREMENT key` — нет: retry может примениться дважды.

`DELETE key` может быть idempotent по state, но response semantics first/repeat могут различаться.

## Request ID / deduplication

Для non-idempotent operations server может хранить processed request IDs + result.

Trade-offs:

- memory/storage;
- retention window;
- client identity/scope;
- recovery after restart;
- collision/uniqueness contract.

Capstone core не обязан реализовывать dedup, но protocol design должен объяснить retry policy.

## Versioning

Protocol version должен позволять reject incompatible request cleanly. Не assume future fields can be inserted arbitrary into binary layout without framing/version rules.

## Errors

Различай:

```text
client input error
not found/conflict
server overload
server internal/storage error
protocol version error
```

Error taxonomy помогает retry decisions. Например malformed request retry без изменения бессмысленен; overload может быть retryable with backoff.

## Project slice

Зафиксируй `PROTOCOL.md`:

- wire format;
- operations;
- idempotency/retry table;
- errors;
- max sizes;
- version behavior.

## Exercise

Для `GET`, `SET`, `DELETE`, hypothetical `INCR` заполни:

```text
idempotent?
retry after timeout safe?
what ambiguity remains?
dedup needed?
```

## Exit check

Timeout — это observation клиента, не автоматический statement «server ничего не сделал».
