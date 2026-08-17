# 6.6 — Как разным process показать разные представления системных ресурсов

**Теория:** ~90 мин · **Лаб:** ~100 мин · **С телефона:** theory — да

← [`05-proc-process-inspection.md`](05-proc-process-inspection.md) · → [`07-cgroup-v2-capabilities-isolation.md`](07-cgroup-v2-capabilities-isolation.md)

## Проблема

Process isolation by address space does not hide all OS-wide names/views. Container-like environments need separate views of PIDs, mounts, hostname, network stack and more.

Linux **namespace** isolates a category of system resources/identifiers for member processes.

Examples:

- PID namespace — process ID view;
- mount namespace — mount table view;
- UTS — hostname/domain identifiers;
- network — interfaces/routes/socket namespace;
- IPC — certain SysV/POSIX IPC objects;
- user namespace — UID/GID mapping and capability scope;
- cgroup namespace — cgroup path view.

## Important mental model

Namespace usually changes **view/naming context**, not resource quantity limit.

```text
PID namespace: can hide/re-number processes
≠ CPU quota
≠ memory limit
```

Resource limits belong largely to cgroups/rlimits/other mechanisms.

## PID namespace subtlety

First process in new PID namespace has special init-like responsibilities for descendants, including reaping. “PID 1” has behavioral implications; do not create namespace and ignore child cleanup.

## Mount propagation caution

Mount namespace experiments can affect host if propagation/setup misunderstood. Course project requires disposable VM/user namespace/delegated environment and explicit checklist before write operations.

## Lab

Start read-only by comparing `/proc/self/ns/*`. Only then use safe environment to create selected UTS/PID/mount namespace, observe changed hostname/PID view, and exit cleanly.

## Exit check

Why does hiding host PIDs not stop process from consuming all CPU/RAM?