# 6.7 — Как ограничить ресурсы и privileges, не называя это полной sandbox

**Теория:** ~100 мин · **Лаб:** ~100 мин · **С телефона:** theory — да

← [`06-linux-namespaces.md`](06-linux-namespaces.md) · → [`08-module-checkpoint.md`](08-module-checkpoint.md)

## Problem

Namespaces change view but do not answer:

```text
how much CPU/memory/process count may this workload consume?
which privileged kernel operations may it perform?
```

## cgroup v2

Linux control groups group processes and apply accounting/control policies through controllers. **cgroup v2** provides unified hierarchy model.

Relevant course observations/controllers may include:

- `cpu` / `cpu.max`;
- `memory` / `memory.max`, events;
- `pids` / `pids.max`.

Exact files/controllers depend on kernel/systemd/delegation. Do not write host cgroup tree blindly as root.

## Delegation

Modern systems often let service manager/user session own/delegate subtree. Course lab first checks current cgroup and write permissions. If no safe delegated subtree, run read-only observation and document limitation rather than escalating privileges randomly.

## Capabilities

Traditional Unix root privilege can be split into **Linux capabilities** such as network/admin-related powers. A process capability set changes which privileged operations kernel permits.

Capabilities are subtle across permitted/effective/inheritable/ambient/bounding sets and user namespaces. Core goal: understand “root is not one indivisible bit”, not memorize all capabilities.

## Isolation is composition

```text
namespaces  → view/naming isolation
cgroups     → resource accounting/limits
capabilities→ split privilege
rlimits     → per-process style limits
seccomp     → syscall filtering (optional extension)
LSM         → MAC policy such as SELinux/AppArmor (optional extension)
```

Container runtime composes several plus filesystem/device/security setup. Course lab is not production container runtime.

## Lab

Use project environment checklist. Observe cgroup limits, then in delegated/disposable setup apply one small pids or memory limit and collect resulting event/evidence. Inspect capabilities before/after safe restriction if tools/environment allow.

## Exit check

Why can a process be inside PID namespace, under memory cgroup limit and still have dangerous capabilities?