# Concurrent KV Server — staged SPEC

## Stage 1 — protocol + single client

- TCP listening socket on configured test address/port;
- `getaddrinfo`/candidate handling or explicitly scoped IPv4-only course variant documented;
- exact frame format from [`PROTOCOL.md`](PROTOCOL.md);
- no assumption `recv == frame` or `send == response`;
- reject length > `MAX_FRAME` before allocation/arithmetic;
- fixed-width fields encoded/decoded in protocol byte order;
- malformed/truncated frame has deterministic close/error policy;
- every accepted fd closed on all terminal paths.

## Stage 2 — shared KV concurrency

Choose and document synchronization granularity. Correctness requirement:

- concurrent SET/GET/DELETE preserve Hash Table invariants;
- no C data races;
- no lock held across blocking network I/O unless explicitly justified;
- lock ordering documented if >1 lock;
- disconnect/error cannot leave lock held.

## Stage 3 — bounded pool/backpressure

- fixed worker count;
- bounded queue with predicate+condvar loops;
- ownership of client fd transfers exactly at successful enqueue;
- full queue policy explicit: reject/close/wait with bounded semantics;
- shutdown wakes sleeping workers, stops accepting, drains or rejects queued work according to documented policy, joins workers, closes all descriptors.

No detached-worker leak as shortcut.

## Stage 4 — metrics

At minimum:

- successful/error request count;
- queue depth/high-water mark;
- rejection count;
- latency samples/report p50/p95/p99;
- throughput under documented closed-loop driver.

Metrics collection itself must be thread-safe and must not silently dominate benchmark.

## Non-goals

- TLS/auth;
- distributed state;
- unbounded values/connections;
- HTTP compatibility;
- security against adversarial hash-flood unless chosen as extension.

## Transfer

Choose event-loop alternative, protocol extension or overload-policy experiment. State invariants/resource bounds before code.