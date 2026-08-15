# Shell — Acceptance

- empty input does not crash;
- external command + arguments;
- nonexistent command reports error and shell continues;
- `cd` changes parent shell cwd;
- `exit` works;
- `<` input redirection;
- `>` output redirection;
- two-command pipeline;
- no leaked pipe ends causing hang;
- child statuses reaped;
- Ctrl-C model works according to documented scope;
- no known sanitizer errors in parser/memory code;
- no unexplained warnings;
- README documents grammar and non-goals;
- transfer feature + tests.
