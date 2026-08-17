# Persistent KV Service — Test plan

Тесты должны проверять contract, а не внутренние имена функций.

## Functional

1. SET new / replace;
2. GET hit / miss;
3. DELETE hit / miss;
4. multiple sequential operations preserve semantics.

## Protocol/input

5. partial TCP delivery;
6. multiple frames in one read;
7. zero/min/max legal lengths;
8. oversized lengths rejected before allocation;
9. truncated/malformed frame;
10. unknown version/opcode/status handling.

## Concurrency/resources

11. concurrent clients against same/different keys;
12. queue saturation reaches documented BUSY/backpressure behavior;
13. slow client cannot create unbounded per-connection memory;
14. repeated connect/disconnect leaves no unexplained fd/thread growth.

## Shutdown

15. stop accepting new work;
16. drain/cancel policy executes;
17. blocked workers wake;
18. workers join before storage teardown;
19. process exits within documented target for defined workload.

## Persistence/recovery

20. clean restart;
21. forced kill on disposable data copy;
22. truncated copy;
23. bit-flipped/corrupted copy;
24. injected write/sync failure;
25. observed result compared to `RECOVERY.md` guarantee.

## Performance evidence

26. fixed workload definition;
27. warmup/run/sample method recorded;
28. throughput + p50/p95/p99;
29. queue/service latency split;
30. near-saturation and overload runs.

## Tooling discipline

Не заполняй реальный system disk, не повреждай единственную копию данных и не запускай hostile input за пределами controlled fixtures.