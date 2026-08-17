# 5.7 — Почему перегруженный server должен замедлять или отклонять работу

**Теория:** ~85 мин · **Практика/project:** ~4–6 часов · **С телефона:** теория — да

← [`05b-condvars-bounded-queue.md`](05b-condvars-bounded-queue.md) · → [`07-poll-event-loop.md`](07-poll-event-loop.md)

## Проблема

Thread-per-connection looks simple but each connection consumes stack/scheduler/file-descriptor resources. Unbounded arrival can create unbounded threads.

## Thread pool

Create fixed worker count and bounded work queue:

```text
acceptor
→ bounded queue
→ worker 1
→ worker 2
→ ... fixed N
```

Worker count bounds active application work. Queue bounds waiting work.

## Backpressure

When downstream capacity is full, upstream must receive a signal/constraint. This is **обратное давление (backpressure)**.

For a server it can appear as:

- stop accepting temporarily;
- bounded enqueue wait;
- reject/close with protocol status;
- let kernel socket backlog fill, pushing pressure outward.

Backpressure is not “make system faster”. It prevents unlimited accumulation and makes overload behavior explicit.

## Queueing consequence

Even before CPU saturation, deeper queue increases waiting time. Latency = queue wait + service time + I/O/network components.

Thus “accept every request and eventually process” may maximize misery rather than usefulness.

## Choosing worker count

No universal `threads = cores` rule. CPU-bound vs blocking I/O workload differs. Measure throughput, queue wait, CPU utilization and tail latency under defined workload.

## Project stage

Concurrent KV Server now uses bounded worker pool. Define exact full-queue policy in README/PROTOCOL; tests must prove resource bounds and ownership on rejection/shutdown.

## Exit check

If queue grows from 10 to 10,000 while service rate unchanged, what happened to waiting time even before any request execution got slower?