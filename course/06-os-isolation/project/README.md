# Modern Linux Isolation Lab — рабочий README

## Environment

Заполни [`ENVIRONMENT_CHECKLIST.md`](ENVIRONMENT_CHECKLIST.md): kernel/environment, WSL/VM/native, cgroup mount/delegation, permissions.

## Status / Build

Command-line experiments и C launcher build/run commands.

## Baseline

До isolation зафиксируй:

```text
PID / hostname
namespace identifiers from /proc/<pid>/ns
/proc/<pid>/cgroup
uid/gid/capability observations relevant to lab
```

## Namespace progression

UTS, PID, mount: что меняется для child, что остаётся общим с host.

## Child lifecycle

Who forks/clones/unshares, who reaps, what execs, cleanup paths.

## cgroup v2

Observed membership/controllers. Если есть delegated subtree — exact limits, workload и cleanup. Если нет — честно записать, что resource limit experiment не выполнялся на данном environment.

## Security / non-goals

Это **не** secure multi-tenant sandbox. Запиши shared kernel, capabilities, filesystem exposure, syscall surface и отсутствующие hardening mechanisms.

## Tests/evidence

Expected observations before/after namespace creation, process exit/reaping, cleanup, optional resource limit result.

## Debugging story / transfer

