# 6.6 — Linux namespaces

**Теория:** ~80 мин  
**Lab:** ~2–4 часа  
**С телефона:** теория — да

← [`05-proc-process-inspection.md`](05-proc-process-inspection.md) · → [`07-cgroup-v2-capabilities-isolation.md`](07-cgroup-v2-capabilities-isolation.md)

## Цель

Понять namespace как отдельный **view/isolation dimension**, а не как «контейнер целиком».

## Namespace idea

Linux namespace меняет, какую instance/view global-ish resource видит process.

Основные:

- PID;
- mount;
- UTS;
- network;
- IPC;
- user;
- cgroup;
- time (на современных Linux).

Course core подробно работает с UTS, PID, mount; network/user — concept + limited lab depending environment.

## UTS

Изолирует hostname/domain-name view.

Простой lab:

```bash
unshare --uts ...
```

в новом namespace изменить hostname и сравнить host/outside view.

## PID namespace

Processes внутри namespace видят отдельную PID hierarchy. Первый process внутри становится PID 1 **в namespace view** и имеет special lifecycle/reaping responsibilities.

Outside host всё равно имеет host PID для того же task.

```text
host sees pid 4200
namespace may see same task as pid 1
```

## Mount namespace

Изолирует mount table/view. Это основа separate filesystem view, но не автоматически secure root.

Можно создать private mount namespace, bind mount/rootfs и change root view (`pivot_root`/chroot-like pieces) with privileges/care.

## Network namespace

Separate network devices/routes/firewall state view. Чтобы реально соединить namespace наружу, нужны veth/routes/NAT/bridge-style config — Stretch для core.

## User namespace

Позволяет mapping UIDs/GIDs между inside/outside namespace. Это важный foundation rootless containers, но privilege rules сложные и environment-dependent.

Не объясняй «inside root = host root». Mapping/capabilities determine authority.

## `unshare`, `clone`, `setns`

- `unshare` отделяет calling process в новые namespaces;
- `clone` может создать child в namespaces;
- `setns` позволяет join existing namespace при permissions.

Сначала command-line experiments, потом C wrapper. Это уменьшает accidental complexity.

## `/proc/<pid>/ns`

Namespace handles представлены special symlink-like entries. Сравнение inode-like identifiers показывает, находятся ли processes в одной namespace instance.

## Security boundary nuance

Namespaces ограничивают views, но все containers share kernel. Для production security нужны также:

- capabilities;
- seccomp;
- LSM (SELinux/AppArmor etc.);
- filesystem permissions;
- cgroups/resource controls;
- kernel hardening/updates.

Namespace alone ≠ VM boundary.

## Lab

1. `unshare` UTS;
2. hostname change inside;
3. inspect `/proc/self/ns`;
4. PID namespace experiment with child;
5. mount namespace simple private mount if environment allows;
6. document failures due permissions/WSL limitations without random root escalation.

## Causal questions

1. Почему PID 1 inside всё ещё имеет host PID?
2. Почему mount namespace не даёт resource limits?
3. Почему network namespace без veth/routes может не иметь connectivity?
4. Почему namespaces не изолируют kernel vulnerabilities?

## Exit check

Для слова «container» перечисли конкретные isolation dimensions вместо одного binary yes/no.
