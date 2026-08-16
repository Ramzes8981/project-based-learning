# 8.5 — Software breakpoints на x86-64

**Теория:** ~105 мин  
**Project slice:** ~8–12 часов  
**С телефона:** теория — да

← [`04-registers-memory.md`](04-registers-memory.md) · → [`06-single-step-stack-unwinding.md`](06-single-step-stack-unwinding.md)

## Цель

Реализовать address breakpoint как reversible machine-code patch + debugger state transition.

## x86 `INT3`

Core x86-64 software breakpoint заменяет first instruction byte на one-byte trap opcode `0xCC` (`INT3`). После исполнения trap tracee останавливается с `SIGTRAP`; x86 RIP указывает **после** one-byte trap, поэтому candidate breakpoint address = `RIP - 1`.

Не классифицируй любой `SIGTRAP` как breakpoint: `exec`, single-step и другие tracing events тоже могут давать trap stops.

## Breakpoint record

```text
address
original_byte
enabled
(optional hit count/id)
```

Duplicate insert must be detected before reading «original» byte again; иначе можно сохранить уже вставленный `0xCC` и потерять настоящий code byte.

## Patch operation

При word-sized ptrace memory API:

```text
peek word at breakpoint address
save low byte
patched = (word & ~0xff) | 0xcc
poke word
```

Это конкретно для принятой x86 little-endian exact-address strategy. Если implementation выравнивает word address, byte shift рассчитывается по `address - aligned_address`.

Используй unsigned masks/types, чтобы bit operations не зависели от signed shifts.

## Hit/step-over lifecycle

```text
wait -> SIGTRAP stop
read RIP
candidate = RIP - 1
verify enabled breakpoint(candidate)
set RIP = candidate
restore original byte
PTRACE_SINGLESTEP
wait for step stop
reinsert 0xCC if breakpoint still enabled
return to debugger prompt / continue policy
```

Ключевой invariant: original instruction исполняется ровно один раз, а persistent breakpoint после этого снова armed.

## Delete/disable

Restore original byte only while tracee stopped and if breakpoint is currently armed. Self-modifying code/thread races are explicit non-goals, поэтому saved byte remains valid under course assumptions.

## PIE

Сначала non-PIE fixtures с stable link/runtime addresses. Затем выбери symbol offset/value и вычисли runtime address из actual executable mapping base `/proc/<pid>/maps`. Не hardcode ASLR base.

## Tests

- breakpoint at known function hit twice in loop;
- duplicate `break` не corrupt saved byte;
- delete before hit restores code;
- continue after hit executes original instruction;
- unrelated SIGTRAP not mislabeled where distinguishable by current state;
- target exits while breakpoint armed without debugger corruption.

## Exit check

Опиши breakpoint не словом «0xCC», а full state machine restore → RIP fix → step → reinsert.
