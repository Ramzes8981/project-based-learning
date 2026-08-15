# Module 6 — Checkpoint

## Explain

- process states/context switch/preemption;
- response/turnaround/fairness;
- resident set/page replacement/thrashing;
- deadlock/starvation/semaphore/condvar;
- IPC trade-offs;
- `/proc` investigation;
- UTS/PID/mount/network/user namespaces;
- cgroup v2;
- capabilities/seccomp role;
- namespace vs resource vs privilege isolation.

## Core milestone

Проверь [`project/ACCEPTANCE.md`](project/ACCEPTANCE.md).

## Required artifact

Isolation matrix:

```text
Resource/attack surface | isolated? | mechanism | limitation
PID view                | ...       | ...       | ...
filesystem mounts       | ...
network                 | ...
CPU/memory              | ...
privileges              | ...
kernel                  | ...
```

## Exit gate

Ты можешь объяснить container-style isolation как composition нескольких OS mechanisms и назвать shared-kernel boundary.
