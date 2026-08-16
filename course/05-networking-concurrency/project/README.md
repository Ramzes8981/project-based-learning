# Concurrent KV Server — рабочий README

## Status / Build

Executable, `make`, `make test`, run command.

## Protocol

Implementation conforms to [`PROTOCOL.md`](PROTOCOL.md). Document any intentionally smaller key/value limits.

## Architecture

```text
acceptor -> bounded queue -> workers -> shared Hash Table
```

Who owns accepted fds/tasks/buffers? When are they closed/freed?

## Queue invariants

Capacity, `not_empty`, `not_full`, shutdown state, wakeup policy.

## Shared store synchronization

Lock scope and why blocking socket I/O is/not inside store lock.

## Backpressure

What happens when queue full? Reject/close/block policy and metrics.

## Shutdown

Stop accepting, close/mark queue, wake workers, drain/cancel policy, join, destroy store.

## Tests

- parser/protocol unit tests;
- `tools/client.py` interoperability;
- `tools/loadgen.py` controlled workload;
- malformed/partial/slow-client cases;
- thread/race diagnostics when supported.

## Metrics

accepted/completed/errors/rejected, active, queue depth, latency distribution, throughput.

## Debugging story / known limitations / transfer

