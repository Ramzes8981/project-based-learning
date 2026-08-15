# 5.9 — Load testing, latency percentiles и saturation

**Теория:** ~65 мин  
**Project lab:** ~3–5 часов  
**С телефона:** теория — да

← [`08-graphs-bfs-dijkstra.md`](08-graphs-bfs-dijkstra.md) · → [`10-module-checkpoint.md`](10-module-checkpoint.md)

## Цель

Отличать network/protocol bug, lock contention, queue saturation и resource exhaustion через измерения.

## Service metrics

Минимум:

- requests/s throughput;
- p50/p95/p99 request latency;
- error/reject rate;
- active connections;
- queue depth;
- worker busy/saturation proxy;
- CPU/memory observations.

## Offered load vs completed throughput

Load generator может пытаться отправлять 20k req/s, а server завершать 5k req/s. Называть 20k «throughput server» неверно.

Отделяй:

```text
offered load
accepted work
completed successful work
errors/rejections
```

## Queue latency

Request latency может состоять из:

```text
network/read
queue waiting
lock waiting
service work
response write
```

Одного total latency недостаточно для root cause, но queue depth/worker metrics помогают.

## Closed-loop vs open-loop intuition

Closed-loop client отправляет следующий request после response; когда server slow, generation rate падает сама.

Open-loop tries arrivals независимо от completion и лучше показывает overload, но требует аккуратного generator design.

Для core достаточно понимать bias и описывать используемый method.

## Python load generator

Здесь Python разрешён как готовый/самописный auxiliary tool. Цель — server systems behavior, а не C load-test framework.

## Experiment

Три нагрузки:

- low;
- near saturation;
- beyond sustainable throughput.

Для каждой измерь throughput/latency/queue/rejects.

Затем измени **одну** policy: worker count или queue capacity/backpressure, повтори.

Не делай вывод «больше workers всегда лучше».

## Causal questions

1. Почему average latency скрывает tail?
2. Почему queue depth растёт до того, как CPU обязательно станет 100%?
3. Почему unbounded queue может временно показывать меньше rejects, но быть хуже system design?
4. Как отличить malformed-frame errors от overload rejects?

## Exit check

Дай diagnosis framework для фразы «server тормозит» минимум из четырёх классов causes.
