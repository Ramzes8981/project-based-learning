# Capstone — Acceptance

## Functional

- GET/SET/DELETE;
- persistence according to documented contract;
- concurrent clients;
- malformed requests safe;
- clean restart;
- graceful shutdown.

## Resource control

- frame size bound;
- connection/work queue bound;
- backpressure/reject policy;
- no unexplained fd/thread/memory growth in repeated workload.

## Evidence

- reproducible load generator/config;
- completed throughput;
- p50/p95/p99;
- queue vs service latency;
- error/reject rate;
- saturation experiment.

## Reliability

- >= 5 controlled failure scenarios;
- recovery behavior documented;
- limitations honest.

## Architecture

- component/state diagram;
- three ADRs;
- protocol/retry semantics;
- metric definitions/SLO;
- security/resource review;
- 10×/second-node thought experiment.

## Quality

- no unexplained C/Rust warnings/lints in owned code;
- relevant sanitizers/tests clean;
- project README reproducible;
- one substantial transfer decision/feature designed from first principles.
