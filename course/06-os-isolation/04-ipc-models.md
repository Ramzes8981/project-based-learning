# 6.4 — Как процессы обмениваются данными, не разделяя всё адресное пространство

**Теория:** ~75 мин · **Практика:** ~65 мин · **С телефона:** теория — да

← [`03-deadlocks-semaphores-condvars.md`](03-deadlocks-semaphores-condvars.md) · → [`05-proc-process-inspection.md`](05-proc-process-inspection.md)

## Проблема

Processes are isolated by default address spaces, yet systems need cooperation. IPC chooses what to share and what failure/backpressure semantics follow.

**Inter-process communication (IPC)** is umbrella term, not one mechanism.

## Compare by contract

### Pipe

Byte stream, typically related processes, fd lifetime/EOF rules already known.

### Unix domain socket

Socket-style local IPC: stream or datagram semantics, filesystem/abstract naming depending platform, credentials/features possible. Still kernel-mediated message/byte transfer rather than shared pointers.

### Shared memory

Map same physical/backing pages into multiple processes. Very fast data sharing can avoid copying, but now synchronization/data layout/crash recovery become application responsibility.

### Signals

Tiny asynchronous notifications, not bulk data transport.

## Selection questions

```text
need byte stream/message/shared state?
who creates/owns endpoint?
what if peer crashes?
what bounds waiting/buffer growth?
how authenticate peer locally?
how clean up stale named resource?
```

## Practice

Take one small producer/consumer and sketch pipe vs Unix socket vs shared-memory design. Do not implement all three. Choose one and justify with failure/ownership needs.

## Exit check

Why is shared memory not automatically “better IPC because zero-copy”?