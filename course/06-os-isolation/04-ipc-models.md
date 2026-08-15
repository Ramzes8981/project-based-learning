# 6.4 — IPC: pipes, sockets, shared memory и signals

**Теория:** ~65 мин  
**Упражнение:** ~50 мин  
**С телефона:** да

← [`03-deadlocks-semaphores-condvars.md`](03-deadlocks-semaphores-condvars.md) · → [`05-proc-process-inspection.md`](05-proc-process-inspection.md)

## Цель

Выбирать IPC по semantics/failure boundaries, а не по одному критерию «быстрее».

## Pipe

Хорош для byte-stream composition related processes.

Плюсы:

- простой;
- kernel buffering;
- fd inheritance.

Минусы:

- byte stream framing нужен application;
- обычно local;
- topology ограничена descriptors/process relation.

## Unix domain socket

Local socket даёт bidirectional stream/datagram semantics, independent connection model и может передавать credentials/descriptors on supporting systems.

Полезен для client/server components на одном host.

## TCP socket

IPC становится network-transparent, но добавляет serialization, network failures, latency и security exposure.

## Shared memory

Processes map same memory pages.

Плюс: можно избежать repeated large payload copies через kernel socket path depending design.

Минусы:

- synchronization сложнее;
- lifetime coordination;
- corruption shared state;
- pointers внутри shared region нельзя бездумно интерпретировать в разных address spaces, если они absolute process virtual addresses.

Обычно shared structures используют offsets/relative references или controlled identical mapping assumptions.

## Signals

Маленький asynchronous notification channel, не transport для complex payloads.

## Files

File-based coordination persistent/simple, но locking/atomic update/crash semantics важны. Не использовать «оба процесса просто пишут JSON» без protocol.

## Serialization cost

IPC performance включает:

```text
encode
copy/map
kernel transitions
synchronization
decode
queueing
```

Поэтому «shared memory всегда быстрее» может проиграть из-за complex synchronization/cache bouncing при реальном workload.

## Failure isolation

Threads share process fate/address space.

Separate processes дают stronger fault boundary: segfault одного не обязательно corrupts address space другого, но IPC/control complexity выше.

## Exercise

Для трёх scenarios выбери IPC и объясни trade-offs:

1. shell pipeline;
2. local DB client ↔ daemon;
3. two processes exchange 1 GiB read-mostly dataset repeatedly.

Разбор: [`04-ipc-models.solution.md`](04-ipc-models.solution.md).

## Exit check

Выбор IPC должен включать semantics, data volume, latency, failure isolation и synchronization complexity.
