# Hash Table — Public scenarios

1. empty table lookup;
2. insert/get;
3. update same key;
4. many keys;
5. deliberately force collisions using selected test keys or small capacity;
6. delete head/middle of probe chain;
7. lookup item after tombstone;
8. insert after tombstone;
9. fill until resize threshold;
10. verify every key after resize;
11. trigger multiple resizes;
12. long/invalid key/value according to contract;
13. create/destroy many times under sanitizers;
14. metrics remain internally consistent;
15. transfer feature tests.

Review may add unseen collision/order cases.
