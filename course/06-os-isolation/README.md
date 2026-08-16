# Module 6 — Operating Systems & Isolation

**Цель:** собрать coherent OS model: scheduling, VM under pressure, synchronization, IPC, process inspection, namespaces, cgroup v2 и ограничения container-style isolation.

**Оценка:** ~42–58 часов.  
**Core milestone:** Modern Linux Isolation Lab.

## Prerequisites

- Unix processes/signals/descriptors;
- virtual memory/performance;
- concurrency primitives;
- test/failure reasoning.

## Уроки

1. [`01-scheduling-process-states.md`](01-scheduling-process-states.md)
2. [`02-memory-pressure-page-replacement.md`](02-memory-pressure-page-replacement.md)
3. [`03-deadlocks-semaphores-condvars.md`](03-deadlocks-semaphores-condvars.md)
4. [`04-ipc-models.md`](04-ipc-models.md)
5. [`05-proc-process-inspection.md`](05-proc-process-inspection.md)
6. [`06-linux-namespaces.md`](06-linux-namespaces.md)
7. [`07-cgroup-v2-capabilities-isolation.md`](07-cgroup-v2-capabilities-isolation.md)
8. [`08-module-checkpoint.md`](08-module-checkpoint.md)

## Проект

[`project/SPEC.md`](project/SPEC.md) · [`project/ENVIRONMENT_CHECKLIST.md`](project/ENVIRONMENT_CHECKLIST.md) · [`project/README.md`](project/README.md)

Проект — учебный launcher/isolation lab, **не production container runtime и не security sandbox**. Если WSL/host не даёт безопасно выполнить kernel-specific часть, используй Ubuntu VM/native Linux fallback и зафиксируй различие.
