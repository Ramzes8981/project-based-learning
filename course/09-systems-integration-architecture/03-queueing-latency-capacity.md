# 9.3 — Latency, utilization, queueing и Little's Law

**Теория:** ~85 мин  
**Exercise:** ~60 мин  
**Project slice:** ~90 мин  
**С телефона:** да

← [`02-protocol-idempotency-contracts.md`](02-protocol-idempotency-contracts.md) · → [`04-backpressure-timeouts-overload.md`](04-backpressure-timeouts-overload.md)

## Цель

Рассуждать о capacity через arrival/service rates, queue time и measured saturation.

## Service time vs response time

Request latency:

```text
network/input wait
+ queue wait
+ service/lock/storage work
+ output wait
```

Если optimization ускоряет storage, но request 90% времени стоит в queue, p99 почти не улучшится.

## Utilization

Для одного idealized server resource:

```text
rho = arrival_rate / service_capacity
```

Когда utilization приближается к 1, queueing delay обычно растёт резко. Exact curve зависит arrival/service distributions и model.

Не нужно считать «80% CPU всегда предел» — важна measured workload/saturation.

## Little's Law

Для стабильной системы в steady-state:

```text
L = lambda * W
```

где:

- `L` — average number items in system;
- `lambda` — average throughput/arrival rate for stable flow;
- `W` — average time in system.

Example:

```text
throughput = 1000 req/s
average latency = 20 ms = 0.020 s
L ≈ 20 requests in system on average
```

Это не формула для arbitrary transient/unbounded overload; assumptions matter.

## Concurrency != throughput automatically

More workers help если workload waits on I/O/parallel cores are available. Но могут ухудшить:

- lock contention;
- context switching;
- cache locality;
- DB serialization;
- queue competition.

## Tail latency

p99 может расти из-за rare storage flush, lock convoy, page fault, GC in auxiliary components, scheduler delay, slow client.

Нужно correlate metrics/traces, а не оптимизировать median only.

## Capacity test

Build load steps:

```text
low
medium
near saturation
overload
```

Для каждого:

- offered rate/concurrency;
- completed throughput;
- p50/p95/p99;
- errors/rejects;
- queue depth;
- CPU/memory;
- storage metrics.

## Exercise

1. Используй Little's Law на трёх toy cases.
2. Найди inconsistent measurements (например reported throughput/latency/concurrency impossible under stable assumptions).
3. Предложи metric, distinguishing service time vs queue time.

Разбор: [`03-queueing-latency-capacity.solution.md`](03-queueing-latency-capacity.solution.md).

## Project slice

Добавь instrumentation timestamps минимум:

```text
enqueue time
start service
finish service
```

Теперь измеряй queue latency отдельно от service latency.

## Exit check

При high p99 сначала спроси «где время?» прежде чем добавлять threads.
