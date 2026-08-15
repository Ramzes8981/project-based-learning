# 5.7 — Non-blocking I/O, `poll` и event loop

**Теория:** ~85 мин  
**Guided lab:** ~3–5 часов  
**С телефона:** теория — да

← [`06-thread-pool-backpressure.md`](06-thread-pool-backpressure.md) · → [`08-graphs-bfs-dijkstra.md`](08-graphs-bfs-dijkstra.md)

## Цель

Понять alternative concurrency model: один/few event-loop threads + per-connection state machines.

## Blocking

Blocking `recv` может остановить thread до появления data.

Thread pool компенсирует это несколькими threads.

## Non-blocking

`O_NONBLOCK` заставляет I/O operations вернуть сразу столько, сколько возможно, либо EAGAIN/EWOULDBLOCK, если сейчас progress невозможен. POSIX socket model определяет такое поведение для nonblocking transfer. citeturn932665search2

## Readiness

`poll()` принимает set file descriptors/events и сообщает, где можно **попытаться** выполнить I/O без обычного blocking. citeturn932665search3

Readiness не означает:

- «полный application frame уже доступен»;
- «send всей response завершится за один вызов».

## Per-connection state

Blocking handler мог сделать:

```text
read_exact length
read_exact payload
process
write_all response
```

Event loop должен сохранять state между readiness events:

```text
READ_PREFIX (have 2/4 bytes)
READ_BODY   (have 800/2000)
WRITE_RESP  (sent 300/900)
```

Это главный complexity cost event-driven design.

## `pollfd`

Каждый fd имеет requested events и returned revents. Нужно обрабатывать errors/hangup независимо от desired read/write state.

## `epoll`

Linux `epoll` масштабирует large descriptor sets эффективнее определённых `poll` workloads и имеет свои level/edge-trigger semantics. Но core сначала учит `poll`, потому что model проще и portable POSIX-like.

## Guided lab

Сделай маленький nonblocking echo/multi-client server через `poll`.

Не нужно переписывать весь KV milestone второй раз.

Сравни:

```text
thread pool: control flow простой, OS threads/state stacks
poll loop: explicit state machines, меньше blocking threads
```

## Causal questions

1. Почему readability не означает complete frame?
2. Почему event loop требует output buffer state?
3. Что будет, если после EAGAIN считать connection broken?
4. Почему `epoll` не стоит учить до понимания readiness/state machine?

## Exit check

Для partial frame нарисуй state transitions через три `poll/read` events.
