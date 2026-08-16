# Persistent KV Service — acceptance scenarios

## Functional/recovery

1. GET/SET/DELETE basic contract;
2. concurrent clients;
3. clean restart preserves acknowledged durable state according to RECOVERY contract;
4. malformed/oversized frames rejected without corrupting service;
5. storage corruption/truncation copy produces controlled startup/runtime error according to policy.

## Bounded resources / overload

6. connection/frame/queue limits are explicit;
7. overload reaches BUSY/reject/backpressure policy instead of unbounded allocation;
8. slow clients cannot create unbounded per-connection memory;
9. queue depth/reject metrics reconcile with workload.

## Shutdown

10. stop accepting new work;
11. queue drain/cancel policy executes;
12. workers wake/join;
13. storage flush/close policy executes;
14. process exits within documented target for defined workload.

## Observability/load

15. p50/p95/p99 + throughput generated from defined workload;
16. queue/service latency separated if instrumentation supports it;
17. active connections/storage errors/lifecycle events observable;
18. repeated benchmark records environment/build parameters.

## Failure experiments

19. forced process kill on disposable DB copy;
20. injected storage-error boundary;
21. truncated/corrupted copy;
22. restart/recovery result compared to documented guarantee.

## Architecture

23. at least 3 ADRs;
24. security limitations;
25. 10×/second-node analysis based on measured bottleneck.
