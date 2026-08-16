# Arena Allocator — public scenarios

Точные C signatures выбирает ученик; эти сценарии должны быть представлены в его `make test`.

1. create/destroy empty arena;
2. zero-size allocation policy documented/tested;
3. allocations of 1 byte and several alignments;
4. returned pointers satisfy chosen alignment;
5. fill until explicit allocation failure without corruption;
6. free then reuse block;
7. split leaves valid remainder only when it can hold metadata + aligned payload;
8. free adjacent blocks and coalesce;
9. non-adjacent free-list neighbors are not coalesced merely because they are list neighbors;
10. repeated alloc/free sequences preserve invariants;
11. double-free/invalid-free debug policy produces controlled failure or detection according to contract;
12. allocation-size/align arithmetic overflow is rejected before pointer arithmetic;
13. destroy releases arena exactly once;
14. stats match independently counted layout;
15. compare first-fit with second placement policy on same deterministic workload.

## Review-only

Unseen fragmentation patterns, awkward sizes near split threshold, many tiny blocks, alternating free pattern, randomized deterministic seed.
