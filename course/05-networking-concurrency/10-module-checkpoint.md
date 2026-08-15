# Module 5 — Checkpoint

## Explain

- MAC/ARP/IP/subnet/gateway;
- TCP byte stream vs UDP datagram;
- socket/listen/accept/connect;
- getaddrinfo candidate model;
- framing/endianness/bounds;
- thread/data race/mutex/condvar;
- bounded queue/backpressure;
- poll/readiness/state machine;
- graph representations;
- BFS/DFS/Dijkstra assumptions;
- throughput/latency/saturation.

## Core milestone

Проверь [`project/ACCEPTANCE.md`](project/ACCEPTANCE.md).

## Debug evidence

Минимум один из:

- partial-frame parsing bug;
- data race;
- deadlock;
- fd leak;
- queue saturation issue.

## Transfer

Одна feature:

- timeouts;
- `poll` version;
- read/write lock experiment;
- connection limit;
- protocol versioning;
- richer instrumentation.

## Exit gate

Для медленного server ты можешь разделить проблему на network semantics, parser/protocol, concurrency, queueing и CPU/memory bottleneck, а не искать одну «оптимизацию» вслепую.
