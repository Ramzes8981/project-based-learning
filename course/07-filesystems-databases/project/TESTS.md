# SimpleDB — Public scenarios

1. create empty DB;
2. reopen empty DB;
3. insert/get one;
4. insert keys in shuffled order;
5. duplicate key;
6. missing key;
7. fill one leaf to exact boundary;
8. next insert causes leaf split;
9. data survives root split/reopen;
10. enough inserts for internal split/height growth;
11. ordered scan after splits;
12. malformed magic/version;
13. truncated file/page;
14. invalid page type/cell count controlled failure;
15. page-access metrics GET vs scan;
16. transfer feature.

Review can mutate bytes in a copy of DB file for unseen corruption cases.
