# 6.8 — Checkpoint: какой ресурс виден, ограничен и кем управляется

**Время:** ~3–5 часов · **С телефона:** review — да; lab — ПК

← [`07-cgroup-v2-capabilities-isolation.md`](07-cgroup-v2-capabilities-isolation.md) · ↑ [`README`](README.md)

## Explain

1. runnable vs running vs sleeping;
2. resident page vs mapped virtual page;
3. memory pressure/thrashing without claiming one literal Linux replacement algorithm;
4. deadlock wait-for cycle and lock-order prevention;
5. semaphore vs mutex vs condition variable role;
6. IPC trade-offs;
7. `/proc` as evidence source;
8. namespace changes view;
9. cgroup changes resource accounting/limits;
10. capability changes privilege;
11. why composition still is not automatically secure container.

## Project gate

Isolation Lab passes [`project/ACCEPTANCE.md`](project/ACCEPTANCE.md), including environment safety evidence and read-only fallback where delegation is unavailable.

## Transfer

Given hypothetical untrusted build job, propose minimal composition of namespace/cgroup/capability/rlimit/seccomp-like controls and explicitly list what threats remain.

## Exit check

For each observed isolation effect you can point to exact mechanism responsible instead of saying “Docker/container does it”.