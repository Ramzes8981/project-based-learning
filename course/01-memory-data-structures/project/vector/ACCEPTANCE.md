# Vector — Acceptance

- starts empty in valid state;
- multiple pushes preserve order;
- growth happens beyond initial capacity;
- old values survive growth;
- get/set boundary behavior documented;
- pop/transfer feature works;
- allocation failure path does not corrupt previous state where it can be simulated;
- ASan/UBSan clean on public scenarios;
- README explains size/capacity/ownership and pointer invalidation after resize;
- no unexplained warnings.
