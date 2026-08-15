# Isolation Lab — Public scenarios

1. host vs isolated UTS hostname differs;
2. namespace identifiers demonstrate separation;
3. PID view experiment matches documented model;
4. mount created inside private mount namespace does not unexpectedly alter host view (where supported);
5. child termination/reaping;
6. `/proc/<pid>/cgroup` inspected;
7. controlled resource-limit behavior or documented inability due delegation;
8. cleanup repeated twice without stale resources;
9. transfer feature.
