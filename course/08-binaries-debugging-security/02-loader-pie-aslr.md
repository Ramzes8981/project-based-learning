# 8.2 — Loader, shared libraries, PIE и ASLR

**Теория:** ~80 мин  
**Lab:** ~90 мин  
**С телефона:** да

← [`01-elf-sections-segments-symbols.md`](01-elf-sections-segments-symbols.md) · → [`03-ptrace-debugger-lifecycle.md`](03-ptrace-debugger-lifecycle.md)

## Цель

Отличать link-time address/offset от runtime virtual address и вычислять runtime location в PIE process.

## Loader path

После `execve` kernel/loader setup создаёт process image:

```text
map executable segments
setup stack/argv/env/auxiliary data
load/interact with dynamic linker for dynamic executable
map shared libraries
apply relocations/lazy/eager binding according to format/runtime policy
transfer control to entry/startup code
```

C `main` не является самой первой machine instruction процесса; runtime startup eventually calls it.

## Static vs dynamic linking

Static link включает needed library code в executable at link time (with caveats/licensing/platform).

Dynamic executable references shared libraries loaded/mapped runtime.

Advantages dynamic libraries: sharing/updating/smaller binaries; costs: loader complexity, ABI/version dependency, relocation/binding.

## PIE

Position Independent Executable не требует fixed runtime base. Internal code/data references compiled in relocation-friendly relative forms.

Runtime address:

```text
load_base + object-relative virtual offset
```

для соответствующей mapping/model.

## ASLR

Address Space Layout Randomization меняет placement mappings across executions: executable base for PIE, shared libraries, stack, heap/mmap regions etc. Exact entropy/policy platform-dependent.

ASLR не исправляет memory-corruption bug; оно затрудняет predictability addresses.

## `/proc/<pid>/maps`

Показывает actual runtime ranges/permissions/backing. Сопоставь ELF program headers с mappings.

## Permissions

Typical code mapping `r-x`, read-only data `r--`, writable data `rw-`. W^X/NX policy стремится разделять writable и executable, но exact mappings/hardening depend build/system.

## Lab

Собери один test program:

1. default distro/compiler PIE settings;
2. explicit non-PIE variant (`-no-pie` where toolchain supports).

Запусти несколько раз, print address function/global и сравни `/proc/.../maps`.

Найди symbol/object-relative address через `nm/readelf` и runtime base.

## Causal questions

1. Почему hard-coded symbol address ломается в PIE+ASLR?
2. Почему non-PIE удобен как первый debugger breakpoint test, но не production recommendation?
3. Что ASLR защищает, а чего не защищает?
4. Почему `main` не обязана совпадать ELF entry point?

## Exit check

Для PIE symbol объясни formula runtime address = mapping base + relative value with correct ELF load assumptions.
