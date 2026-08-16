# 5.2 — Какие гарантии дают UDP и TCP и почему TCP не передаёт сообщения

**Теория:** ~85 мин · **Практика:** ~70 мин · **С телефона:** теория — да

← [`01-link-ip-routing.md`](01-link-ip-routing.md) · → [`03-socket-api-getaddrinfo.md`](03-socket-api-getaddrinfo.md)

## Проблема

IP can move packets toward destination, but application still needs a contract:

- should loss be recovered?
- should bytes remain ordered?
- is each send a distinct message?
- how identify application endpoint on host?

Transport protocols choose different trade-offs.

## Ports

A host can run many networked processes/services. Transport protocols use **ports** as endpoint identifiers within IP/transport context.

`IP address + transport protocol + port` helps identify destination endpoint. Port alone is not globally unique service identity.

## UDP

User Datagram Protocol (UDP) gives datagram-oriented transport:

- preserves datagram boundaries;
- no built-in reliable delivery guarantee;
- no built-in ordering guarantee across datagrams;
- duplicates/loss/reordering must be acceptable or handled by application/protocol above.

A successful local `send` does not prove remote application received/processed datagram.

## TCP

Transmission Control Protocol (TCP) provides reliable ordered **byte stream** between endpoints, subject to connection failure semantics.

Core mental model:

```text
sender writes bytes: ABC | DEF
receiver may read: A | BCDE | F
```

The separators between application `send/write` calls are **not preserved as message boundaries**.

This is the key fact that creates framing lesson.

## What “reliable” does not mean

TCP can retransmit and order bytes, but cannot tell application whether peer business logic committed an operation before connection died. End-to-end retry/idempotency appears in capstone.

## Connection close

An orderly EOF tells receiver peer closed its sending direction after bytes already delivered to stream. Reset/error has different semantics. Treat network errors as normal state transitions, not impossible exceptions.

## Partial I/O returns again

Socket `send/recv` inherit byte-I/O lesson: one call may transfer fewer bytes than requested. TCP stream parser must handle arbitrary chunk boundaries.

## Практика

Using a local TCP pair/tool, deliberately write two chunks and read with different buffer sizes. Record observed chunking, then explain why any observed alignment is not guaranteed contract.

Разбор: [`02-udp-tcp-stream.solution.md`](02-udp-tcp-stream.solution.md).

## Exit check

Why is “one `send()` = one message” an invalid TCP protocol design even if it appears to work on localhost?