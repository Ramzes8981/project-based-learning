# SimpleDB — public scenarios

## File/header

1. new database has exact magic/version/page-size/header zeros;
2. wrong magic/version/page-size rejected;
3. truncated page0 rejected;
4. page_count/root_page outside actual file range rejected;
5. deterministic empty DB bytes.

## Records/tree

6. insert/get one;
7. unsorted unique inserts, get all;
8. duplicate rejected;
9. ordered scan;
10. reopen preserves results;
11. fill leaf exactly to boundary;
12. first leaf split;
13. root becomes internal;
14. enough keys for internal split/multi-level tree;
15. all leaves same depth;
16. leaf chain produces every key once in order;
17. invalid page_type/cell_count/child page detected without OOB.

## I/O/error

18. short/error positional I/O path does not mark page successful silently;
19. invalid calculated page offset rejected before syscall;
20. failed write leaves explicit error state according to pager contract.

## Metrics

21. controlled point lookup reports fewer page visits than full scan on nontrivial tree;
22. split counters match known sequence.

## Recovery limitation evidence

23. corruption/truncation fixtures produce controlled rejection;
24. README/RECOVERY_LIMITATIONS makes no WAL/ACID claim.
