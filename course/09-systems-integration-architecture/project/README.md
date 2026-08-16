# Persistent KV Service — рабочий README

## Status / Build / Run

## Requirements

Links to `WORKLOAD.md`, `ARCHITECTURE.md`, `PROTOCOL.md`, `RECOVERY.md`, `METRICS.md`, ADRs and security limitations.

## Reused components

Что действительно reused/adapted из Hash Table/KV Server/SimpleDB и какие contracts изменились. Не copy-paste без ownership review.

## State ownership

Connections/tasks/index/storage/metrics/shutdown state.

## Resource bounds

Connections, frame size, queue, worker count, memory/storage growth.

## Test strategy

Unit/property/integration/system/load/failure injection/regressions.

## Benchmark evidence

Exact build, hardware/environment, workload, warmup/run duration, sample count, p50/p95/p99, throughput, CPU/memory/disk observations.

## Failure evidence

Overload, malformed input, forced process stop on disposable data copy, storage corruption copy, injected I/O failure boundary, restart/recovery.

## 10× / second-node conclusion

What breaks first? Can vertical/design change solve it? What new failure modes would second node introduce?

## Debugging story / transfer / limitations

