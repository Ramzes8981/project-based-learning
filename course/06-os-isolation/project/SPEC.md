# Modern Linux Isolation Lab — SPEC

## Goal

Построить маленький educational launcher, который демонстрирует конкретные Linux isolation mechanisms.

## Required progression

1. inspect baseline process `/proc/.../ns` and cgroup membership;
2. UTS namespace + distinct hostname;
3. PID namespace or mount namespace (минимум один, лучше оба if environment permits);
4. child process launch/lifecycle/reaping;
5. optional controlled filesystem root/view;
6. cgroup v2 observation;
7. one resource limit experiment if delegated/safe;
8. capability/privilege limitations documented.

## Implementation

Сначала command-line `unshare/nsenter` experiments. Затем course-owned C launcher using `unshare`/`clone` where appropriate.

## Non-goals

- OCI runtime;
- image distribution;
- secure multi-tenant sandbox;
- full network namespace stack;
- overlayfs;
- production seccomp profile.
