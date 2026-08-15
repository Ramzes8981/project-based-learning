# 4.1 — Virtual address space и `mmap`

**Теория:** ~65 мин  
**Lab:** ~60 мин  
**С телефона:** теория — да

← [`README`](README.md) · → [`02-page-tables-tlb-faults.md`](02-page-tables-tlb-faults.md)

## Цель

Понять, что pointer/address в process — виртуальный адрес, а наличие большого virtual range не означает немедленное выделение такого же объёма physical RAM.

## Virtual address space

Каждый обычный process работает в своём virtual address space.

Conceptual map:

```text
low addresses
  code / mappings
  data
  heap-like regions
  mapped libraries/files
  ...
  stack
high addresses
```

Точный layout зависит от executable, loader, ASLR, kernel и runtime. Не заучивай фиксированные addresses.

## Virtual != physical

CPU генерирует virtual addresses. Memory-management hardware + kernel-managed page tables переводят их к physical frames или сообщают, что mapping отсутствует/нужна обработка.

```text
virtual address
  ↓ translation
physical frame + offset
```

## Mapping

Mapping связывает virtual page range с:

- anonymous memory;
- file-backed pages;
- special kernel/device semantics.

Anonymous memory удобно для arena allocator.

## `mmap`

На Linux/POSIX-like systems `mmap` создаёт mapping.

Core anonymous private idea:

```c
void *p = mmap(NULL, length,
               PROT_READ | PROT_WRITE,
               MAP_PRIVATE | MAP_ANONYMOUS,
               -1, 0);
```

Linux `MAP_ANONYMOUS` — platform feature; course canonical environment Linux. Failure обозначается `MAP_FAILED`, а не `NULL`.

После использования mapping освобождается `munmap`.

## Reservation vs committed/touched memory

Большая anonymous mapping часто не приводит к немедленному physical backing каждого page. Physical pages могут появляться по demand при first touch.

Отсюда возможно:

```text
large virtual size
small resident set initially
```

Но overcommit/policy/platform details сложнее, поэтому не обещай, что любой huge mapping всегда безопасен.

## Page size

OS управляет memory страницами. Узнать базовый page size можно через `sysconf(_SC_PAGESIZE)`/соответствующий API.

Allocator позже должен понимать alignment, но ему не обязательно выдавать user blocks ровно page-sized.

## `/proc/self/maps`

На Linux файл показывает current process mappings. Он удобен как observational tool:

```bash
cat /proc/self/maps
```

Сделай mapping и посмотри, как layout изменился.

## File-backed mapping

`mmap` может отображать file region в address space. Это не означает «файл целиком мгновенно прочитан в RAM»; pages загружаются/кэшируются по demand согласно OS.

## Causal questions

1. Почему virtual address нельзя считать physical RAM address?
2. Почему mapping 1 GiB не обязательно сразу увеличивает resident RAM ровно на 1 GiB?
3. Почему `MAP_FAILED` нужно проверять отдельно от `NULL`?
4. Что является owner `mmap` region и каким API заканчивается lifetime?

## Lab

Напиши `map_probe.c`:

- узнай page size;
- создай anonymous mapping нескольких pages;
- напечатай returned address;
- прочитай `/proc/self/maps` до/после;
- запиши bytes в разные pages;
- `munmap`;
- проверь errors.

Разбор: [`01-virtual-address-space-mmap.solution.md`](01-virtual-address-space-mmap.solution.md).

## Exit check

Объясни разницу `virtual size`, `mapped range`, `physical backing` и `resident pages` на рабочем уровне.
