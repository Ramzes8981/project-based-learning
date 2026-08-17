# Unix Shell — acceptance scenarios

Use automated non-interactive tests where deterministic, plus small PTY/manual script for terminal/job-control behavior.

1. blank line;
2. `/bin/echo hello` or portable equivalent;
3. command with multiple args;
4. unknown command;
5. repeated commands leave no zombies;
6. `cd` then external `pwd` observes changed parent cwd;
7. `exit` returns documented status;
8. overlong line rejected safely;
9. too many args rejected safely;
10. output redirection truncates/creates according to contract;
11. input redirection reads file;
12. failed redirection does not poison shell descriptors;
13. one pipeline transforms bytes correctly;
14. pipeline producer with enough output does not deadlock due parent wait ordering;
15. EOF arrives when expected; leaked-writer regression;
16. repeated pipelines show stable fd count within expected baseline;
17. foreground Ctrl-C behavior in PTY/manual environment;
18. child terminated by signal reported/reaped;
19. transfer feature tests.

Test harness must use timeouts only as deadlock guards, not as proof of correct ordering by itself.