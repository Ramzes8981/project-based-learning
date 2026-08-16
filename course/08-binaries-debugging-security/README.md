# Module 8 — Binaries, Debugging & Security Bridge

**Цель:** связать ELF file, runtime mappings, registers/signals и debugger state machine; научиться диагностировать memory-corruption mechanisms и mitigations на контролируемых локальных targets.

**Оценка:** ~45–62 часа.  
**Core milestone:** `minidbg-c` — минимальный Linux/x86-64 debugger на C.

## Platform boundary

Core намеренно **Linux + x86-64 + single-threaded tracee**. `ptrace`, register layout и `INT3` semantics не выдаются за portable C.

## Уроки

1. [`01-elf-sections-segments-symbols.md`](01-elf-sections-segments-symbols.md)
2. [`02-loader-pie-aslr.md`](02-loader-pie-aslr.md)
3. [`03-ptrace-debugger-lifecycle.md`](03-ptrace-debugger-lifecycle.md)
4. [`04-registers-memory.md`](04-registers-memory.md)
5. [`05-software-breakpoints.md`](05-software-breakpoints.md)
6. [`06-single-step-stack-unwinding.md`](06-single-step-stack-unwinding.md)
7. [`07-dwarf-source-debugging.md`](07-dwarf-source-debugging.md)
8. [`08-memory-corruption-mitigations.md`](08-memory-corruption-mitigations.md)
9. [`09-module-checkpoint.md`](09-module-checkpoint.md)

## Проект

[`project/SPEC.md`](project/SPEC.md) · [`project/README.md`](project/README.md)

`project/tests/targets/` содержит только **контролируемые учебные tracees**, которые можно собирать non-PIE/PIE с известными symbols. Debugger implementation курс не предоставляет.

Core не требует C++ и не реализует полноценный DWARF parser. Source-level debugging — Stretch после machine-level core.
