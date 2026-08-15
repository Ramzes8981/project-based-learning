# Arena Allocator — Public scenarios

1. tiny arena create/destroy;
2. allocation sizes 1, alignment-1, alignment, alignment+1;
3. fill arena to exhaustion;
4. free/reuse one block;
5. split large free block;
6. free adjacent blocks and allocate larger request after coalesce;
7. non-adjacent free blocks do not coalesce;
8. repeated alloc/free patterns;
9. metrics sum plausibility;
10. policy comparison workload;
11. transfer feature.
