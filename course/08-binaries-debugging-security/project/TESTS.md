# minidbg-c — Public scenarios

1. target exits 0;
2. target exits nonzero;
3. target terminates by signal;
4. read key registers at initial/function stop;
5. valid memory read;
6. invalid address controlled error;
7. breakpoint at known non-PIE function;
8. breakpoint inside loop hit multiple times;
9. disable/remove restores original code;
10. duplicate breakpoint request;
11. single-step advances execution;
12. breakpoint step-over then re-hit;
13. PIE address resolution exercise;
14. quit while tracee stopped — documented detach/terminate policy;
15. transfer feature.
