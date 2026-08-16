# 6.7 — cgroup v2, capabilities и isolation composition

**Теория:** ~90 мин  
**Project:** ~6–10 часов  
**С телефона:** теория — да

← [`06-linux-namespaces.md`](06-linux-namespaces.md) · → [`08-module-checkpoint.md`](08-module-checkpoint.md)

## Цель

Отделить resource control от namespaces и собрать честную model container-style isolation без обещания security boundary, которого проект не создаёт.

## cgroup v2

Cgroup — kernel mechanism для группировки processes и resource accounting/control. В v2 используется единая hierarchy.

Полезная filesystem mental model:

```text
/sys/fs/cgroup/
├── cgroup.controllers
├── cgroup.subtree_control
├── cgroup.procs
├── memory.current / memory.max ...
├── cpu.stat / cpu.max ...
└── pids.current / pids.max ...
```

Набор controller files зависит от kernel/configuration/delegation.

## Membership

`cgroup.procs` перечисляет PIDs processes, принадлежащих cgroup. Process можно переместить записью PID в target `cgroup.procs`, если permissions/delegation это разрешают.

После `fork` child рождается в той cgroup, к которой принадлежит parent в момент fork. Это важно для launcher design: limit/group часто подготавливают до запуска workload либо явно мигрируют child.

`/proc/<pid>/cgroup` позволяет увидеть membership; для pure v2 entry имеет hierarchy id `0` и path.

## Namespace vs cgroup

```text
namespace -> какую часть/имена system state process видит
cgroup    -> accounting/limits/weight resources группы processes
```

UTS namespace не ограничивает RAM. `memory.max` не меняет hostname view. Это ортогональные механизмы.

## Controllers

### Memory

`memory.max` — hard limit interface v2, но это не «зарезервировать ровно X MiB физической RAM». Реальное поведение включает accounting, reclaim и OOM decisions. Для наблюдения также полезны `memory.current`/events, если доступны.

### PIDs

`pids.max` ограничивает количество tasks/process creation внутри subtree accounting model. Это защита resource availability, не permission sandbox.

### CPU

CPU controller может задавать weight/maximum bandwidth. Ограничение CPU не означает deterministic execution speed: host load/scheduler/measurement noise остаются.

## Delegation и безопасность lab

Не создавай/не меняй произвольные host cgroups от root только ради упражнения. Сначала выясни:

- cgroup v2 mounted ли;
- delegated ли тебе writable subtree;
- запускается ли lab в disposable VM/user session;
- какие controllers enabled;
- как cleanup вернуть system state.

Если writable delegation нет — **наблюдение membership считается достаточным core evidence**, а limit experiment переносится в VM/optional.

## Capabilities

Linux разбивает многие традиционные root powers на capabilities. Capability всегда нужно рассматривать в контексте user namespace и resource, которым он управляет.

UID 0 внутри нового user namespace не означает host root. Process может иметь capabilities внутри своего user namespace, не имея тех же privileges над resources parent/initial namespace.

Следствие: фраза «внутри container root» недостаточна для security reasoning.

## seccomp / LSM preview

Namespaces/cgroups сами по себе не фильтруют syscall surface shared kernel. Production isolation может дополнительно использовать seccomp, capability reduction, LSM policies, read-only mounts и другие controls.

Core lab не строит production seccomp policy — важно понимать место механизма в composition.

## Composition

```text
process lifecycle
+ namespaces (views/identities)
+ filesystem/mount view
+ cgroup resource controls
+ user namespace/capability model
+ optional syscall/LSM restrictions
+ shared host kernel
```

## Project slice

По [`project/SPEC.md`](project/SPEC.md):

1. baseline inspect `/proc/.../ns` + cgroup membership;
2. UTS + PID/mount namespace experiments;
3. C launcher child lifecycle;
4. observe cgroup v2 membership;
5. resource-limit experiment только если environment checklist говорит, что это безопасно/delegated;
6. README с threat/non-goal section.

## Causal questions

1. Почему memory cgroup не исправляет use-after-free?
2. Почему namespace root и host root — разные security contexts?
3. Почему pids limit полезен, но не запрещает чтение файла?
4. Как shared kernel влияет на claim «полная виртуальная машина»?

## Exit check

Для любого «container изолирует X» назови конкретный kernel mechanism и его non-goals.
