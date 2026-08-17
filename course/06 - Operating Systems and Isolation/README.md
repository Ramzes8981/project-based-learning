# Module 6 — Как ОС делит конечные ресурсы между программами и изолирует их

**Оценка:** ~30–45 часов.  
**Prerequisite:** process/thread/concurrency, virtual memory, networking basics.

Здесь мы не преподаём mutex/condition variable второй раз. Module 5 уже дал synchronization mechanics; теперь смотрим на ОС как на manager конечных CPU/memory/process/network resources.

## Уроки

1. [`01-scheduling-process-states.md`](01-scheduling-process-states.md) — **Почему runnable process всё равно может не получать CPU прямо сейчас**.
2. [`02-memory-pressure-page-replacement.md`](02-memory-pressure-page-replacement.md) — **Что делает ОС, когда активных страниц больше, чем физической памяти**.
3. [`03-deadlocks-semaphores-condvars.md`](03-deadlocks-semaphores-condvars.md) — **Как ожидание нескольких ресурсов превращается в deadlock и как это диагностировать**.
4. [`04-ipc-models.md`](04-ipc-models.md) — **Как процессы обмениваются данными, не разделяя всё адресное пространство**.
5. [`05-proc-process-inspection.md`](05-proc-process-inspection.md) — **Как наблюдать process state через `/proc`, а не гадать**.
6. [`06-linux-namespaces.md`](06-linux-namespaces.md) — **Как разным процессам показать разные представления системных ресурсов**.
7. [`07-cgroup-v2-capabilities-isolation.md`](07-cgroup-v2-capabilities-isolation.md) — **Как ограничить ресурсы и privileges, не называя это “полной песочницей”**.
8. [`08-module-checkpoint.md`](08-module-checkpoint.md) — checkpoint.

## Проект

[`project/README.md`](project/README.md) — Modern Linux Isolation Lab. Изменения namespace/cgroup/capability выполняются только в disposable/delegated environment согласно [`project/ENVIRONMENT_CHECKLIST.md`](project/ENVIRONMENT_CHECKLIST.md).

## Ключевая граница безопасности

```text
namespace changes view
cgroup limits/accounts resources
capability splits root privilege
```

Ни один механизм по отдельности не равен production container security boundary.