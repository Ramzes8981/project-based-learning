# 8.5 — Software breakpoints на x86-64

**Теория:** ~100 мин  
**Project slice:** ~8–12 часов  
**С телефона:** теория — да

← [`04-registers-memory.md`](04-registers-memory.md) · → [`06-single-step-stack-unwinding.md`](06-single-step-stack-unwinding.md)

## Цель

Реализовать address breakpoint как reversible patch + debugger state transition, а не просто «записать 0xCC».

## Software breakpoint idea

Debugger меняет first byte instruction at target address на x86 breakpoint/trap instruction (`INT3`, one-byte encoding `0xCC`).

GDB documentation описывает software breakpoints как replacement instruction at address на target-specific breakpoint/trap instruction. citeturn547994search9

## Breakpoint record

Для каждого breakpoint нужно хранить:

```text
address
original byte
enabled state
```

Если patch делается word-sized ptrace write, сохраняй original containing word/byte carefully.

## Insert

```text
read word at address
save original low/target byte
replace byte with 0xCC
write patched word
```

На x86 little-endian target byte mask position depends exact aligned/address word approach. Не предполагай `address` word-aligned; simplest course implementation can PEEK at exact address because ptrace handles word access semantics, then replace low byte corresponding to that address.

## Hit

Когда CPU executes INT3, tracee stops with SIGTRAP. На x86 instruction pointer is advanced past the one-byte trap instruction, so debugger identifies breakpoint at:

```text
hit_address = RIP - 1
```

Core verifies enabled breakpoint exists there before treating every SIGTRAP as breakpoint hit.

## Step over own breakpoint

Если просто restore original byte and `continue` without RIP correction, original instruction can be skipped or trap repeated depending state.

Correct conceptual lifecycle:

```text
1. detect breakpoint hit at RIP-1
2. set RIP back to breakpoint address
3. restore original instruction byte
4. single-step exactly one original instruction
5. wait for single-step stop
6. reinsert 0xCC if breakpoint remains enabled
7. continue/user command
```

This state machine is the core project concept.

## Duplicate breakpoints

Setting breakpoint twice at same address must not save `0xCC` as «original byte». Detect duplicate and reuse existing record.

## Remove

Disable/remove restores original byte **only if** tracee stopped and breakpoint currently enabled. Project must avoid restoring wrong stale word after code self-modification; self-modifying code is non-goal.

## PIE

Start with non-PIE target where address from `nm/objdump` corresponds simply to runtime executable mapping.

Then add helper/logic to combine PIE relative symbol value with runtime load base from `/proc/<pid>/maps`.

Full dynamic symbol resolver is Stretch.

## Project slice

Commands:

```text
break 0xADDRESS
breaks
delete/disable ID
continue
step
```

Implement breakpoint hit handling + step-over.

## Causal questions

1. Почему every SIGTRAP не обязательно твой breakpoint?
2. Почему нужно сохранить original byte?
3. Почему RIP корректируется назад на x86 INT3?
4. Почему duplicate breakpoint может corrupt original-byte bookkeeping?

## Exit check

Без кода перечисли breakpoint state transitions от insert до second hit.
