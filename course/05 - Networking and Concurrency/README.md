# Module 5 — Как bytes доходят до другой программы и что ломается при параллельной обработке

**Оценка:** ~45–65 часов.  
**Prerequisite:** Unix fd/process model, checked byte lengths, graphs/priority queue from Module 1.

Модуль состоит из двух причинных дуг:

```text
как отправить bytes другой машине
→ какие гарантии нужны приложению
→ socket
→ TCP stream
→ framing

один handler не успевает обслуживать workload
→ threads/shared state
→ race
→ synchronization
→ ожидание без busy loop
→ bounded queue
→ backpressure
→ event loop alternative
→ measurement
```

## Уроки

1. [`01-link-ip-routing.md`](01-link-ip-routing.md) — **Как пакет выбирает следующий шаг к другой машине**.
2. [`02-udp-tcp-stream.md`](02-udp-tcp-stream.md) — **Какие гарантии приложению дают UDP и TCP и почему TCP не передаёт сообщения**.
3. [`03-socket-api-getaddrinfo.md`](03-socket-api-getaddrinfo.md) — **Как процесс получает сетевой endpoint через socket API**.
4. [`04-framing-protocol-design.md`](04-framing-protocol-design.md) — **Как поверх TCP восстановить границы сообщений**.
5. [`05-threads-races-sync.md`](05-threads-races-sync.md) — **Почему два потока ломают общий mutable state**.
6. [`05b-condvars-bounded-queue.md`](05b-condvars-bounded-queue.md) — **Как ждать работу без busy loop и зачем очереди нужен предел**.
7. [`06-thread-pool-backpressure.md`](06-thread-pool-backpressure.md) — **Почему перегруженный server должен замедлять или отклонять работу**.
8. [`07-poll-event-loop.md`](07-poll-event-loop.md) — **Как один thread ждёт много sockets без thread-per-connection**.
9. [`09-load-testing-metrics.md`](09-load-testing-metrics.md) — **Как измерять throughput и хвост latency, не обманывая себя генератором нагрузки**.
10. [`10-module-checkpoint.md`](10-module-checkpoint.md) — checkpoint.

Graph/BFS/Dijkstra больше не живут внутри networking: prerequisite вынесен в [`20b-graphs-paths.md`](<../01 - Memory and Data Structures/20b-graphs-paths.md>).

## Проект

[`project/README.md`](project/README.md) — Concurrent KV Server. Milestones раскрываются после framing, thread safety, bounded queue и overload lessons.

## Boundary

Core не реализует TCP stack, TLS, HTTP, distributed consensus или production authentication. Цель — понять byte-stream protocol, resource bounds, concurrency correctness и overload behavior.