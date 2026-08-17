# Hash Table — test scenarios

## Basic

1. empty get → not found;
2. put/get;
3. update existing keeps count;
4. delete existing;
5. delete missing leaves state unchanged.

## Collision correctness

6. deterministic fixture forces same initial slot for at least two different keys;
7. both keys retrieved;
8. delete first; second remains retrievable;
9. tombstone reused by later insert without hiding chain;
10. full-table probe terminates with controlled result.

## Resize

11. insert through several grow thresholds;
12. verify every live pair after each grow;
13. verify tombstones do not count as live copied entries;
14. injected allocation failure before new table creation preserves old table;
15. injected failure during rebuild follows documented rollback/ownership policy.

## Resource safety

16. repeated put/update/delete/destroy under ASan/UBSan;
17. long/boundary key lengths according to API;
18. impossible size/growth arithmetic rejected before allocation.

## Transfer

19. dedicated tests for chosen transfer feature.