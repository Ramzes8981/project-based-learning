# 6.1 — Почему runnable process всё равно может не получать CPU прямо сейчас

**Теория:** ~70 мин · **Лаб:** ~60 мин · **С телефона:** теория — да

← [`README`](README.md) · → [`02-memory-pressure-page-replacement.md`](02-memory-pressure-page-replacement.md)

## Проблема

Processes/threads can all be ready to execute, but CPU cores are finite. OS must choose who runs and who waits.

## States as scheduling facts

Useful simplified process/thread states:

```text
running   — currently executing on a CPU
runnable  — ready, waiting for CPU time
sleeping  — waiting for event/resource/timer
stopped   — intentionally suspended
zombie    — process exited; parent has not reaped status yet
```

Names/details vary by OS; the causal distinction is **waiting for CPU** vs **waiting for something else**.

## Scheduler

The **scheduler** chooses runnable execution entities for CPU. Context switch saves/restores execution state. Scheduling policy balances fairness, priorities, latency and throughput; there is no universal “round-robin every N ms” model.

## CPU utilization can mislead

Low CPU with high latency can mean threads sleep on I/O/locks. High runnable queue can mean CPU contention. Always pair metric with state/wait reason.

## Observe on Linux

Use `ps`, `/proc`, `top`/`pidstat` if available. Create one CPU-bound child and one sleeping child; predict states before observing.

## Causal questions

1. Why is runnable not same as running?
2. Why can 100% CPU be healthy for a CPU-bound batch job but alarming for latency-sensitive service?
3. Why does zombie consume little CPU yet still represent resource/accounting bug?

## Exit check

Given “service slow, CPU 20%”, you can name evidence needed before blaming scheduler.