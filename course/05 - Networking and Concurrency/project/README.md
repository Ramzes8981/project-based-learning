# Concurrent KV Server — staged project

Reuses **ideas/contracts** from Hash Table, not a pasted old `main()`.

## Stage 1 after 5.4

Single-client TCP server with exact binary framing/protocol and robust partial I/O.

## Stage 2 after 5.5

Concurrent handlers with shared KV synchronization correctness.

## Stage 3 after 5.6–5.7

Bounded worker queue, clean shutdown and explicit overload/backpressure policy.

## Stage 4 after 5.9

Measurement report with throughput + p50/p95/p99 and closed-loop tool limitations.

Normative protocol: [`PROTOCOL.md`](PROTOCOL.md).  
Other docs: [`SPEC.md`](SPEC.md) · [`ACCEPTANCE.md`](ACCEPTANCE.md) · [`TESTS.md`](TESTS.md) · [`HINTS.md`](HINTS.md).

Student owns server implementation.