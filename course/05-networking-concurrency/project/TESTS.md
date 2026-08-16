# Concurrent KV Server — public scenarios

## Protocol

1. SET then GET round-trip;
2. update existing key;
3. GET missing -> NOT_FOUND;
4. minimum/maximum documented key/value;
5. prefix split across multiple sends;
6. body split at every interesting boundary;
7. two frames in one TCP send;
8. EOF mid-prefix/body;
9. unknown version/opcode/nonzero flags;
10. inconsistent key/value lengths;
11. frame > MAX_FRAME rejected before body allocation.

## Concurrency

12. many clients read/write distinct keys;
13. same-key concurrent updates produce valid whole value, never torn/corrupt state;
14. bounded queue reaches capacity under slow workers;
15. full-queue policy observable/metric consistent;
16. disconnect during response doesn't kill process;
17. graceful shutdown wakes waiting workers and terminates;
18. repeated connect/disconnect does not leak descriptors/tasks.

## Metrics

19. accepted/completed/error counters reconcile for controlled run;
20. latency samples produce p50/p95/p99 from harness with clearly documented population.
