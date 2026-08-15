# 6.7 — cgroup v2, capabilities и isolation composition

**Теория:** ~85 мин  
**Project:** ~6–10 часов  
**С телефона:** теория — да

← [`06-linux-namespaces.md`](06-linux-namespaces.md) · → [`08-module-checkpoint.md`](08-module-checkpoint.md)

## Цель

Отделить resource control от namespaces и собрать честный mini-container/isolation lab.

## cgroup v2

Cgroups группируют processes и позволяют accounting/control resources через controllers.

Current Linux cgroup v2 использует unified hierarchy. Process membership виден через `cgroup.procs`; child после `fork` рождается в cgroup parent на момент fork according to kernel cgroup v2 model. citeturn676423search1

Controllers могут управлять/учитывать:

- CPU;
- memory;
- pids;
- I/O;
- others depending kernel/config.

## Namespace vs cgroup

```text
namespace -> что process видит
cgroup    -> сколько/как resources process group использует
```

Они дополняют друг друга, но не заменяют.

## cgroup v2 hierarchy

Conceptually:

```text
root cgroup
├─ serviceA
│  ├─ workers
│  └─ maintenance
└─ serviceB
```

Process относится к hierarchy membership; controllers/delegation rules определяют allowed changes.

Не записывай arbitrary limits в host cgroup filesystem без controlled environment/permission understanding.

## Memory limit nuance

Memory cgroup limit — не «выделить process ровно X MB физической RAM». Это accounting/control механизм с reclaim/OOM behavior и деталями kernel controller.

## PID controller

Ограничение pids помогает защитить host/service от fork bomb-style resource exhaustion, но не заменяет permissions/security.

## Capabilities

Traditional root privileges Linux разбиты на capabilities: например network/admin/sys-admin-like powers.

Process с UID 0 внутри user namespace не обязательно имеет same effective capabilities на host resources.

Production container reduces capability set instead of давать blanket root power.

## seccomp preview

Seccomp filters syscall surface. Namespace/cgroup не запрещают автоматически dangerous syscalls, доступные через shared kernel.

Core проект только документирует место seccomp; полноценный policy — Stretch/security branch.

## Isolation composition

Учебный container-like stack:

```text
process
+ namespaces (views)
+ filesystem view
+ cgroup limits/accounting
+ reduced capabilities
+ optional seccomp/LSM
+ kernel boundary shared
```

## Project

Выполни [`project/SPEC.md`](project/SPEC.md).

Минимум:

- launcher child;
- UTS namespace;
- PID или mount namespace;
- inspect namespace IDs;
- observe cgroup v2 membership;
- если environment безопасно позволяет — controlled pids/memory/CPU experiment;
- explicit limitations.

C wrapper можно писать после `unshare` experiments.

## Causal questions

1. Что ограничивает namespace, а что cgroup?
2. Почему root inside user namespace не равен host root?
3. Почему cgroup memory limit не исправляет memory-corruption bug?
4. Почему production container всё равно разделяет host kernel?

## Exit check

Утверждение «процесс в container, значит host полностью защищён» должно вызывать список конкретных проверок, а не согласие.
