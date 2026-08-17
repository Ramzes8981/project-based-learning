# 5.3 — Как process получает network endpoint через socket API

**Теория:** ~90 мин · **Практика:** ~100 мин · **С телефона:** теория — да

← [`02-udp-tcp-stream.md`](02-udp-tcp-stream.md) · → [`04-framing-protocol-design.md`](04-framing-protocol-design.md)

## Проблема

We understand IP/transport contract, but application needs OS handle to send/receive. Unix already taught fd as handle to kernel resource.

Network endpoint becomes another fd-like resource through **socket API**.

## Socket

A **socket** is kernel-managed communication endpoint exposed to process through descriptor/handle API. On Unix a socket descriptor participates in `read/write`-like and socket-specific calls.

Do not define socket as “a TCP connection”: UDP sockets exist; listening socket is not an established connection.

## Server lifecycle

TCP server shape:

```text
socket
→ set options if needed
→ bind local address
→ listen
→ accept connection
→ handle connected socket
→ close connected socket
→ close listening socket
```

`accept` returns a **new** connected fd. Listening fd remains for future connections.

## Client lifecycle

```text
resolve address
→ socket
→ connect
→ send/recv
→ close
```

## Why `getaddrinfo`

Hostnames/services may resolve to IPv4 or IPv6 and multiple candidates. `getaddrinfo` returns candidate address structures; robust client/server loops candidates rather than hard-coding one family.

Resource ownership:

```text
getaddrinfo success → caller owns result list → freeaddrinfo
socket success      → caller owns fd          → close
accept success      → caller owns client fd   → close
```

## Network byte order

Protocol integer fields use explicit byte order. Socket address helpers such as `htons`/`ntohs` exist for standard integer fields. Custom protocol should encode/decode explicitly and validate lengths before arithmetic/allocation.

## Short I/O + EINTR

Apply Unix rules, now on socket descriptors. Retry policy also needs to consider blocking/nonblocking mode and errors like `EAGAIN/EWOULDBLOCK`; those become relevant in `poll` lesson.

## Практика

Write tiny single-connection loopback echo server/client using `getaddrinfo` candidate loop. Check every resource/error path and use a write-all helper.

Разбор: [`03-socket-api-getaddrinfo.solution.md`](03-socket-api-getaddrinfo.solution.md).

## Exit check

Why does `accept` return a different fd from listening socket, and who owns each after success?