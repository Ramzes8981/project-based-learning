# Module 8 — Как запущенная программа выглядит изнутри debugger-а

**Оценка:** ~40–60 часов.  
**Target:** Linux x86-64 for debugger labs.  
**Prerequisite:** process/signals, virtual memory, x86-64 ABI, C memory safety.

К этому моменту source-level mental model уже недостаточна: debugger получает executable file, runtime mappings, registers, signals and bytes. Модуль строится в том же порядке, в котором эти слои становятся нужны.

## Уроки

1. [`01-elf-sections-segments-symbols.md`](01-elf-sections-segments-symbols.md) — **Как executable хранит то, что нужно loader-у и debugger-у**.
2. [`02-loader-pie-aslr.md`](02-loader-pie-aslr.md) — **Почему адрес функции в файле и во время запуска может отличаться**.
3. [`03-ptrace-debugger-lifecycle.md`](03-ptrace-debugger-lifecycle.md) — **Как debugger останавливает tracee и получает право его наблюдать**.
4. [`04-registers-memory.md`](04-registers-memory.md) — **Как прочитать registers/memory, не путая `-1` с ptrace error**.
5. [`05-software-breakpoints.md`](05-software-breakpoints.md) — **Как один byte `INT3` превращается в breakpoint и почему RIP надо откатить**.
6. [`06-single-step-stack-unwinding.md`](06-single-step-stack-unwinding.md) — **Как выполнить ровно одну инструкцию и восстановить call chain в ограниченной модели**.
7. [`07-dwarf-source-debugging.md`](07-dwarf-source-debugging.md) — **Откуда debugger узнаёт source line и variable names, которых нет в ISA**.
8. [`08-memory-corruption-mitigations.md`](08-memory-corruption-mitigations.md) — **Что mitigations делают с memory-corruption bug и чего они не исправляют**.
9. [`09-module-checkpoint.md`](09-module-checkpoint.md) — checkpoint.

## Проект

[`project/README.md`](project/README.md) — `minidbg-c`: attach/launch, registers, memory, software breakpoints, single-step and limited stack trace on controlled fixtures.

## Security boundary

Лабы выполняются только на собственных course fixtures/processes в разрешённой среде. Здесь изучается debugger mechanism и defensive understanding memory corruption, а не скрытое управление чужими процессами.