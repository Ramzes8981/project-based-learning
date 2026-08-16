# Arena Allocator — test scenarios

1. initialize minimum/normal arena;
2. aligned allocations for several supported powers of two;
3. invalid align 0/non-power-of-two;
4. exact fit;
5. near-boundary failure without offset change;
6. synthetic huge size proving overflow-safe rejection;
7. zero-size policy;
8. free and reuse same/smaller request;
9. split free block;
10. free adjacent blocks in both orders then allocate combined size;
11. free nonadjacent blocks and prove they do not merge;
12. double free;
13. pointer outside arena;
14. interior pointer not allocation start;
15. repeated allocation/free pattern under ASan/UBSan;
16. metrics reconcile with known state;
17. policy comparison workload.

Where behavior depends on metadata overhead, tests use public contract values rather than hidden struct-size assumptions.