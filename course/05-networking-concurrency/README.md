# Module 5 — Networking & Concurrency

**Цель:** понять TCP/IP ниже уровня HTTP library и построить bounded concurrent KV server с измеряемым поведением под нагрузкой.

**Оценка:** ~60–80 часов.  
**Core milestone:** Concurrent KV Server.

## Prerequisites

- Hash Table, heap/Priority Queue и graph basics из Module 1;
- Testing Engineering;
- Unix file descriptors/process model;
- performance measurement basics из Module 4.

## Уроки

1. [`01-link-ip-routing.md`](01-link-ip-routing.md)
2. [`02-udp-tcp-stream.md`](02-udp-tcp-stream.md)
3. [`03-socket-api-getaddrinfo.md`](03-socket-api-getaddrinfo.md)
4. [`04-framing-protocol-design.md`](04-framing-protocol-design.md)
5. [`05-threads-races-sync.md`](05-threads-races-sync.md)
6. [`06-thread-pool-backpressure.md`](06-thread-pool-backpressure.md)
7. [`07-poll-event-loop.md`](07-poll-event-loop.md)
8. [`08-graphs-bfs-dijkstra.md`](08-graphs-bfs-dijkstra.md)
9. [`09-load-testing-metrics.md`](09-load-testing-metrics.md)
10. [`10-module-checkpoint.md`](10-module-checkpoint.md)

## Проект

[`project/SPEC.md`](project/SPEC.md) · [`project/PROTOCOL.md`](project/PROTOCOL.md) · [`project/README.md`](project/README.md)

Course-provided `tools/client.py` и `tools/loadgen.py` проверяют внешний protocol contract, но не содержат server implementation.
