# 5.10 — Checkpoint: trace one request from route to overload policy

**Время:** ~4–6 часов · **С телефона:** review — да; project — ПК

← [`09-load-testing-metrics.md`](09-load-testing-metrics.md) · ↑ [`README`](README.md)

## Explain

1. local link delivery vs IP routing;
2. UDP datagram vs TCP byte-stream guarantees;
3. why TCP does not preserve application write boundaries;
4. listening socket vs accepted socket;
5. framing state machine + untrusted length validation;
6. thread/shared state/data race;
7. mutex vs atomic suitability;
8. Rust `Send`/`Sync` at thread boundary;
9. condition predicate + condvar;
10. bounded queue/shutdown ownership;
11. backpressure vs unbounded buffering;
12. `poll` readiness vs full-message availability;
13. throughput vs latency percentiles;
14. closed-loop loadgen limitation.

## Project gate

Concurrent KV Server passes [`project/ACCEPTANCE.md`](project/ACCEPTANCE.md) and protocol tests.

## Evidence

- frame split/coalesce tests;
- forced collision/concurrent KV correctness tests;
- race detector where supported or strong synchronization tests;
- bounded queue overload behavior;
- descriptor/resource cleanup after disconnects;
- benchmark report with workload and generator model.

## Transfer

Choose one: thread pool ↔ event loop experiment, alternative rejection policy, or protocol extension. Predict trade-off before implementation and measure afterward.

## Exit check

Given one slow client plus a burst of normal clients, you can explain every place bytes/work may wait and which resource bound prevents infinite accumulation.