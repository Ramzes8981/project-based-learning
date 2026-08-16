# 5.7 — Non-blocking I/O, `poll` и event loop

**Теория:** ~90 мин  
**Guided lab:** ~3–5 часов  
**С телефона:** теория — да

← [`06-thread-pool-backpressure.md`](06-thread-pool-backpressure.md) · → [`08-graphs-bfs-dijkstra.md`](08-graphs-bfs-dijkstra.md)

## Цель

Понять альтернативную concurrency model: один/few event-loop threads + explicit per-connection state.

## Blocking vs nonblocking

Blocking `recv` может остановить worker до progress.

При `O_NONBLOCK` operation должна вернуть без обычного ожидания: если сейчас нельзя прочитать/записать, появляется `EAGAIN`/`EWOULDBLOCK` как **нормальное состояние**, а не broken connection.

## Readiness

`poll` получает array descriptors + requested events и возвращает descriptors с событиями/readiness/error/hangup indications.

Readiness означает «попытка соответствующей операции может сделать progress или обнаружить состояние». Она **не** означает:

- полный application frame готов;
- whole response запишется за один `send`;
- после readiness невозможно получить error/EOF.

## Per-connection state machine

Blocking code:

```text
read_exact prefix
read_exact body
process
write_all
```

Event loop:

```text
READ_PREFIX have 0..4
READ_BODY   have 0..body_len
PROCESS
WRITE_RESP  sent 0..response_len
CLOSING
```

State хранит input/output buffers, offsets и protocol phase между iterations.

## `pollfd` lifecycle

У каждого fd requested `events`, returned `revents`. Error/hangup bits надо рассматривать независимо от желаемого state; stale/closed descriptor нельзя оставлять в active set.

## Writable readiness и backpressure

Если output не помещается kernel send buffer, сохранить unsent suffix и ждать future write readiness. Busy-loop повторный `send` после `EAGAIN` сжигает CPU.

## Level vs edge preview

Linux `epoll` добавляет более scalable registration API и level/edge-triggered modes. Core использует `poll`, пока readiness/state model не стала прозрачной. Переход к `epoll` без state machine не устраняет protocol complexity.

## Guided lab

Multi-client nonblocking echo через `poll`:

- fixed maximum clients;
- per-client receive/send state;
- partial reads/writes;
- EOF/error cleanup;
- no busy loops;
- one slow client не блокирует progress других.

Не переписывай весь KV milestone второй раз: lab нужен для сравнения architectural models.

## Exit check

Нарисуй один connection, где 4-byte prefix приходит 2+1+1 bytes, body двумя reads, response двумя writes с `EAGAIN` между ними.
