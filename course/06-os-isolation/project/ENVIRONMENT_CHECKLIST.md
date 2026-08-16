# Isolation Lab — environment checklist

Заполни до privileged/kernel-specific экспериментов.

## Platform

```text
uname -a:
WSL2 / VM / native Linux:
disposable environment available:
```

## Namespaces

Проверь наличие relevant namespace links:

```bash
ls -l /proc/self/ns
```

Запиши, какие `unshare` experiments разрешены обычному user и какие требуют user namespace/privileges.

## cgroup v2

Наблюдение без изменений:

```bash
cat /proc/self/cgroup
findmnt -t cgroup2 2>/dev/null || mount | grep cgroup
```

Не делай `sudo` write experiments автоматически.

Запиши:

```text
cgroup v2 mounted:
my membership:
writable delegated subtree known:
enabled controllers:
cleanup plan:
```

Если writable delegation не доказана, core lab ограничивается read-only observation. Resource-limit experiment выполняется в disposable VM/delegated environment позже.

## Safety boundary

Нельзя ради урока:

- менять host-wide cgroup/root settings без ясного rollback;
- запускать uncontrolled fork/resource exhaustion;
- считать `unshare` само по себе security sandbox;
- выполнять destructive mount operations на host paths.

## Evidence

Сохрани команды/outputs, которые подтверждают конкретный claim, а не только screenshot «вроде работает».
