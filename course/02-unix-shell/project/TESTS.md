# Shell — Public scenarios

1. blank/whitespace line;
2. `/bin/echo hello`;
3. command with several args;
4. nonexistent command;
5. `pwd`, `cd /tmp`, `pwd`;
6. output redirection and file contents;
7. input redirection from known file;
8. `printf abc | wc -c`-like pipeline;
9. pipeline with producer output larger than trivial pipe capacity;
10. malformed `>`/`<`/`|` syntax;
11. Ctrl-C foreground sleep/long command;
12. repeated commands: no unbounded fd leak;
13. transfer feature.

Review adds unseen descriptor-order/EOF cases.
