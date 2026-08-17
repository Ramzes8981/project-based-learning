# 6.5 — Как наблюдать process state через `/proc`, а не гадать

**Теория:** ~65 мин · **Лаб:** ~75 мин · **С телефона:** theory — да

← [`04-ipc-models.md`](04-ipc-models.md) · → [`06-linux-namespaces.md`](06-linux-namespaces.md)

## Problem

Before changing isolation, need inspect what process currently sees: ids, mappings, descriptors, limits, namespaces.

Linux exposes process/kernel information through **procfs**, normally mounted at `/proc`.

## Useful views

For a PID:

```text
/proc/<pid>/status   identifiers/state/memory summary/capabilities fields
/proc/<pid>/maps     virtual mappings
/proc/<pid>/fd/      descriptor symlinks
/proc/<pid>/limits   resource limits
/proc/<pid>/ns/      namespace handles
/cgroup info via /proc/<pid>/cgroup
```

These are kernel interfaces with version/permission differences. Parse only fields you need; do not treat human formatting as eternal stable database schema.

## `/proc/self`

`/proc/self` resolves to caller's current process, useful for tiny observation tools.

## Observation discipline

Predict first, inspect second:

```text
I expect fd 0/1/2 + one opened file
→ inspect /proc/self/fd
→ explain discrepancy
```

This turns `/proc` into debugging evidence, not sightseeing.

## Lab

For a controlled child process record PID, state, fd set, selected mappings, namespace links and cgroup path. Then change one thing in later lab and compare.

## Exit check

Which `/proc` evidence would distinguish “process has file open” from “path merely exists in filesystem”?