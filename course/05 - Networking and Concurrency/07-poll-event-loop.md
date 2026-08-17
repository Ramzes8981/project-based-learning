# 5.8 — Как один thread ждёт много sockets без thread-per-connection

**Теория:** ~90 мин · **Практика:** ~100 мин · **С телефона:** теория — да

← [`06-thread-pool-backpressure.md`](06-thread-pool-backpressure.md) · → [`09-load-testing-metrics.md`](09-load-testing-metrics.md)

## Проблема

Many connections spend most time waiting for bytes. One blocking `recv` cannot service others, while one thread per idle connection has resource/scheduling cost.

Need wait until **any** fd becomes ready.

## Readiness API

`poll()` lets process provide fd set/events and sleep until at least one becomes ready or timeout/signal occurs.

Core mental model:

```text
many nonblocking fds
↓ poll
ready subset
↓
perform only operations that can make progress
↓
update per-connection parser/output state
↓ poll again
```

This style is an **event loop**.

## Nonblocking mode

On nonblocking socket, operation that would block returns failure such as `EAGAIN/EWOULDBLOCK`. That means “no progress now; wait for readiness”, not fatal protocol error.

Still handle short reads/writes after readiness; readiness is not guarantee entire frame/buffer fits.

## Per-connection state

Framing parser must survive across events:

```text
header bytes accumulated
expected payload len
payload bytes accumulated
pending output offset
closing/error state
```

Event-driven code trades threads for explicit state machines.

## `POLLHUP` / errors

Readiness flags can coexist; peer close may still leave readable buffered bytes. Do not interpret one flag with simplistic `else if` chain without API contract.

## `poll` vs scalable APIs

Linux `epoll`, BSD/macOS `kqueue`, io_uring/async runtimes scale/differ in semantics. Core uses `poll` because model is portable enough and transparent. Advanced optimization starts only after measurement.

## Практика

Implement tiny multi-client echo or protocol reader with nonblocking sockets and `poll`, no thread pool. Compare state complexity/resources to thread-pool version.

## Exit check

Why does readiness not mean “one full frame can now be read”, and what state must survive between `poll` iterations?