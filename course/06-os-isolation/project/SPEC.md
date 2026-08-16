# Isolation Lab — SPEC

## Prerequisite gate

No state-changing isolation command before environment checklist identifies disposable VM/container/user namespace/delegated cgroup scope.

## Evidence baseline

Record for controlled target process:

```text
PID/state
selected /proc status
fds
namespace links
cgroup path/limits
capability summary if available
```

## Namespace experiment

Demonstrate at least two changed views, e.g. UTS + PID/mount/network according to environment. Explain exactly what each hides/renames and what it does **not** limit.

## Resource experiment

In delegated/disposable cgroup v2 subtree apply one bounded resource policy (pids/memory/CPU according to safe environment). Generate small controlled workload and capture event/behavior. Never exhaust host globally.

## Privilege experiment

Inspect capability sets. If safe tooling permits, remove/restrict one capability and demonstrate an operation changing from allowed→denied. If not, provide read-only evidence and documented platform limitation.

## Cleanup

All child processes reaped/terminated intentionally, namespace processes exited, delegated cgroup emptied/removed where owned, temporary mounts/files cleaned. Cleanup commands must target only resources created by lab.

## Transfer/threat model

Write short table in README:

```text
mechanism
what boundary it creates
what attack/resource it does not stop
what evidence demonstrated it
```

No claim “secure sandbox” without much broader threat model.