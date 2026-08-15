# 6.5 — `/proc` и process inspection

**Теория:** ~55 мин  
**Lab:** ~90 мин  
**С телефона:** теория — да

← [`04-ipc-models.md`](04-ipc-models.md) · → [`06-linux-namespaces.md`](06-linux-namespaces.md)

## Цель

Использовать `/proc` и инструменты как observability interface, а не меморизовать filenames.

## `/proc`

Linux procfs exposes kernel/process information через pseudo-filesystem.

Полезные paths:

```text
/proc/<pid>/status
/proc/<pid>/cmdline
/proc/<pid>/fd/
/proc/<pid>/maps
/proc/<pid>/ns/
/proc/<pid>/cgroup
```

Fields/API evolve; exact parsing for production tools должен следовать documented format, а не brittle whitespace assumptions.

## `/proc/<pid>/fd`

Directory entries — symlinks/handles representing process descriptors.

Это отличный способ диагностировать fd leaks:

```text
run workload
count/list fds
repeat
fds unbounded growth? investigate ownership
```

## `/proc/<pid>/maps`

Показывает virtual mappings: address ranges, permissions, offsets, file/backing information.

Связывает Module 4 VM с живым process.

## `/proc/<pid>/status`

Содержит identity/state/memory/signal/capability-like summary fields. Не делай вывод по одному number без понимания definition.

## `strace`

Прослеживает syscalls/signals process. Хорош для вопросов:

- какой file открылся?;
- где process blocks?;
- почему connect/open fail?;
- какие child syscalls происходят?

Но tracing меняет timing и может быть дорогим; concurrency race может исчезнуть/измениться.

## `ps/top`

Дают process/thread/resource observations на другом уровне. Metrics могут быть samples/averages; «100% CPU» semantics зависят от tool/core accounting.

## Lab

Запусти Concurrent KV Server и Shell из прошлых modules.

Ответь инструментами:

- сколько fds открыто idle/under load?;
- какие mappings есть?;
- сколько threads?;
- где process blocks при idle?;
- какие syscalls появляются при client connection?

Сделай маленький investigation report, не screenshot dump.

## Exit check

Для каждого observation укажи: какой question ты задавал и почему выбранный interface отвечает именно на него.
