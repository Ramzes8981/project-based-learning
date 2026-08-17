# Persistent KV Service — Acceptance

## Behavior

- GET/SET/DELETE соответствуют `PROTOCOL.md`;
- несколько клиентов не повреждают state;
- malformed/oversized input вызывает controlled error;
- clean restart и shutdown соответствуют `RECOVERY.md`.

## Resource safety

- frame/key/value limits explicit;
- connection/work queue bounded;
- overload policy observable;
- repeated workload не показывает необъяснимого роста fd/thread/memory;
- all size/offset arithmetic around untrusted lengths checked before allocation/access.

## Concurrency/shutdown

- shared mutable state имеет явного owner/synchronization contract;
- workers корректно wake/stop/join;
- storage не закрывается пока worker ещё может его использовать;
- shutdown time проверяется на определённом workload.

## Persistence/recovery

- acknowledgement guarantee записана точно;
- clean restart воспроизводим;
- forced kill/corrupt copy дают поведение, соответствующее documented limitations;
- parser persistent format не доверяет lengths/offsets слепо.

## Evidence

- workload/environment записаны;
- throughput и p50/p95/p99 воспроизводимы;
- queue latency отличима от service latency;
- overload experiment фиксирует rejects/backpressure;
- минимум 5 controlled failure scenarios.

## Architecture

- boundaries + state ownership diagram;
- минимум 3 ADR;
- protocol/retry semantics;
- metric definitions/SLO hypothesis;
- security/resource review;
- 10×/second-node analysis от измеренного bottleneck.

## Code quality

- no unexplained compiler/linter warnings;
- relevant sanitizers/tests clean;
- no known UB/resource leaks in happy/error paths;
- README позволяет воспроизвести build/test/benchmark;
- implementation milestone code написан студентом, не solution из курса.