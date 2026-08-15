# Concurrent KV Server — Acceptance

- address-independent listen/connect path;
- multiple sequential and concurrent clients;
- framed protocol correct under split/coalesced TCP chunks;
- oversized/malformed frame rejected safely;
- GET/SET correctness;
- fixed worker count;
- bounded queue + documented backpressure;
- shared store synchronized;
- no known data races in supported checks;
- connections/fds cleaned on errors;
- graceful shutdown does not silently abandon resources;
- reproducible benchmark with throughput + p50/p95/p99;
- transfer feature;
- README documents protocol/concurrency/limits.
