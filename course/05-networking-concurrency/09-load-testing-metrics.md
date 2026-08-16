# 5.9 — Как измерять throughput и хвост latency, не обманывая себя генератором нагрузки

**Теория:** ~90 мин · **Лаб:** ~100 мин · **С телефона:** теория — да

← [`07-poll-event-loop.md`](07-poll-event-loop.md) · → [`10-module-checkpoint.md`](10-module-checkpoint.md)

## Проблема

Server “feels fast” locally. Need quantify behavior under concurrency/overload without hiding slow requests inside average.

## Throughput

**Throughput**: completed useful operations per unit time, e.g. requests/second. Always define what counts as completed (parsed response? successful status? connection setup included?).

## Latency distribution

One request latency varies. Average can look good while a small fraction waits far longer.

A **процентиль задержки (latency percentile)** answers: value below which a chosen fraction of observations falls.

Example:

```text
p50 = median-ish typical
p95 = 95% completed at or below this latency
p99 = 99% completed at or below this latency
```

Percentiles need enough samples and a clearly defined measurement interval/workload. Do not infer SLO yet; SLO appears in capstone when service objective exists.

## Queue wait vs service time

Instrument separately if possible:

```text
arrival/enqueue
→ queue wait
→ worker starts
→ service work
→ response completed
```

Tail latency can come from queueing even when service work itself stays stable.

## Closed-loop load generator limitation

Repository `project/tools/loadgen.py` is intentionally a **closed-loop concurrency driver**: each worker sends a request and waits for its response before generating the next on that connection/work item.

This means server slowdown automatically reduces offered request rate. It is useful for concurrency/regression comparisons but **cannot by itself prove open-loop overload capacity or maximum sustainable arrival rate**.

Do not write “server handles 50k RPS” from this tool unless measurement model actually generated/verified that arrival process.

## Coordinated omission intuition

If load generator waits for server before scheduling next intended request, it may under-sample waiting that would have occurred under independent arrival schedule. This bias family is often called coordinated omission.

Core requirement: state generator model and limitation; implementing perfect open-loop benchmark is optional.

## Benchmark protocol

Record:

- build/flags/commit;
- machine/OS;
- client/server placement;
- connections/concurrency;
- key/value sizes and operation mix;
- warmup/run duration;
- sample count;
- throughput and p50/p95/p99;
- queue depth/rejections/errors;
- CPU/memory relevant observations.

## Практика

Run at least three concurrency levels and one forced-overload/bounded-queue scenario. Explain whether throughput saturated, queue/rejection changed, and where latency tail grew. Do not compare runs with different workload silently.

## Exit check

Why can closed-loop driver report pleasant latency while failing to model a real arrival burst that exceeds service rate?