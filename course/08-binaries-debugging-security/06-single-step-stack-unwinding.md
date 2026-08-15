# 8.6 — Single-step и limits stack unwinding

**Теория:** ~75 мин  
**Project slice:** ~4–6 часов  
**С телефона:** да

← [`05-software-breakpoints.md`](05-software-breakpoints.md) · → [`07-dwarf-source-debugging.md`](07-dwarf-source-debugging.md)

## Цель

Использовать instruction single-step и понять, почему «идти по RBP chain» — учебный частный случай, а не универсальный production unwinder.

## Single-step

`PTRACE_SINGLESTEP` resumes stopped tracee так, чтобы он снова остановился после одной instruction (плюс возможные signal events). Linux ptrace docs define this restart mode. citeturn857293search1

Debugger still waits and decodes stop event; request call itself не «возвращает после execution instruction».

## Why single-step useful

- stepping over restored breakpoint;
- inspecting state mutation;
- instruction-level debug;
- learning ABI.

## Stack frame model

With frame pointers and simple unoptimized functions:

```text
RBP -> saved previous RBP
       return address
       locals/spills...
```

Chain walk can follow previous RBP and read return addresses.

But compiler may:

- omit frame pointer;
- inline functions;
- tail-call;
- use complex prologue/epilogue;
- optimize variables away.

Therefore naive RBP backtrace is only valid under defined compile flags/ABI assumptions.

## Real unwinding

Robust debuggers use unwind metadata (DWARF CFI etc.) + architecture rules, not blind `RBP` chain.

## Project slice

Core:

- `step` instruction;
- print RIP before/after;
- `x/i` can remain Stretch (disassembler library not required).

Guided stretch:

- compile fixture with `-fno-omit-frame-pointer -O0`;
- implement limited `bt` following RBP chain;
- validate address ranges/alignment and maximum frames;
- clearly label assumptions.

## Causal questions

1. Почему ptrace SINGLESTEP всё равно требует `waitpid`?
2. Почему RBP backtrace может break under `-O2`?
3. Почему max-frame bound нужен даже в debugger tool?
4. Что unwind metadata solves?

## Exit check

Никогда не описывай frame-pointer walk как «как stack всегда устроен в C».
