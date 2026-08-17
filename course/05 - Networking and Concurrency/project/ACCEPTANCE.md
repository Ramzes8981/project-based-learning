# Concurrent KV Server — Acceptance

## Protocol

- exact protocol fixture interoperability;
- frame split at every boundary works;
- multiple frames in one receive buffer work;
- oversized length rejected before allocation;
- truncated EOF handled;
- unknown/malformed command has documented status/close policy;
- response status contract matches `PROTOCOL.md` and client tests.

## I/O/resources

- short read/write loops correct;
- `EINTR` handled where appropriate;
- accepted/listening descriptors closed exactly once;
- repeated connect/disconnect does not leak fds/memory.

## Concurrency

- concurrent operations preserve KV correctness;
- no known data race under supported sanitizer/race tooling;
- no lock held through ordinary blocking response send without documented reason;
- shutdown terminates all workers deterministically;
- queue full path preserves fd ownership.

## Overload

- worker count finite;
- queue capacity finite;
- full-queue behavior observable and tested;
- burst does not cause unbounded threads/queue allocation.

## Measurement

- workload/build/environment recorded;
- throughput + sample count + p50/p95/p99;
- queue/rejection evidence;
- README states bundled load generator is closed-loop and does not alone establish open-loop capacity.

## Quality

- warning-clean owned C code;
- sanitizer-clean owned memory paths;
- one concurrency/resource debugging story;
- transfer task complete.