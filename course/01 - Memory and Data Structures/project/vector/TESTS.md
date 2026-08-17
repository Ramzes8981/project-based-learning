# Vector — test scenarios

1. initialize empty;
2. push one element;
3. push enough elements to trigger several grows;
4. verify all values and insertion order after each grow boundary;
5. get first/last valid index;
6. get `index == len` fails without access;
7. zero/near-zero initial policy according to API;
8. injected allocation failure during grow preserves old pointer/logical values/len/capacity;
9. checked-size helper rejects impossible byte count before multiplication;
10. destroy empty;
11. destroy populated;
12. transfer operation boundary cases.

For allocation-failure testing, route allocator calls through a tiny test seam rather than trying to exhaust machine memory.