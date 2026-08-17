# Modern Linux Isolation Lab — evidence scenarios

Здесь tests часто являются observation/integration checks, потому что exact namespace/cgroup availability зависит от Linux environment.

1. baseline `/proc/self/ns` recorded;
2. child UTS namespace has distinct namespace id and hostname view;
3. parent hostname remains unchanged;
4. PID namespace experiment demonstrates different PID view according to chosen launch method;
5. mount namespace change does not leak into parent mount view;
6. launcher reaps child and leaves no accidental zombie;
7. exec failure path cleans/reports correctly;
8. `/proc/<pid>/cgroup` membership observed;
9. optional delegated cgroup: limit applied to only test workload and removed afterward;
10. process cannot escape parent-imposed cgroup restriction merely by creating child subtree;
11. README explicitly lists non-goals/security gaps;
12. cleanup script/manual checklist restores created mounts/cgroups/temp files.
