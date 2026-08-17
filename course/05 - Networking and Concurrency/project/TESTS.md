# Concurrent KV Server — test plan

## Codec/framing

1. encode/decode smallest valid frame;
2. maximum allowed frame;
3. one-byte-too-large length rejected before allocation;
4. split header at every byte;
5. split payload at many boundaries;
6. two+ frames concatenated in one stream chunk;
7. EOF after partial header/payload;
8. invalid opcode/status/length fixtures per protocol.

## KV semantics

9. SET/GET/DELETE/update;
10. forced hash collisions inherited from table tests;
11. concurrent same-key update workload with allowed final-state oracle;
12. concurrent independent keys preserve all values/count invariants.

## Resources

13. connect/disconnect loop, stable fd/memory baseline;
14. client abort mid-frame;
15. client abort before response;
16. server shutdown with idle connections;
17. shutdown while workers wait on empty queue;
18. shutdown with queued work according to documented drain/reject policy.

## Overload

19. fill queue deterministically;
20. next client/work gets exact full policy;
21. no fd leak on enqueue rejection;
22. burst does not create >configured workers;
23. queue high-water never exceeds capacity.

## Metrics/tooling

24. protocol client regression tests;
25. latency summary monotonic (`p50 <= p95 <= p99`);
26. load report includes sample count/errors/rejections/workload;
27. closed-loop driver limitation documented.

Timeouts guard hangs; they do not substitute for a semantic oracle.