# 5.5 — Почему два threads ломают общий mutable state

**Теория:** ~95 мин · **Практика:** ~90 мин · **С телефона:** теория — да

← [`04-framing-protocol-design.md`](04-framing-protocol-design.md) · → [`05b-condvars-bounded-queue.md`](05b-condvars-bounded-queue.md)

## Проблема

Single-client server can block while one connection waits. A direct idea: run handlers concurrently in multiple execution flows inside one process.

A **поток (thread)** is an execution flow sharing process address space/resources with other threads while having its own execution state such as stack/register context.

Shared address space makes communication cheap—and creates correctness hazards.

## Read-modify-write is not one indivisible event

```c
counter += 1;
```

conceptually can be:

```text
read counter
compute +1
write counter
```

Two threads may interleave and lose update.

## Data race in C

When threads access same memory concurrently, at least one access is a write, and accesses are not properly synchronized according to C memory model, program can have **data race**; data race causes undefined behavior in C.

This is stronger than “sometimes wrong final number”. Compiler/hardware are not required to preserve naive interleaving model for racy program.

## Mutex

A **мьютекс (mutex)** provides mutual exclusion around critical section/shared invariant.

```text
lock
→ read/modify shared state
→ restore invariant
→ unlock
```

Mutex protects an invariant/resource, not arbitrary lines because they “look dangerous”. Document what lock guards.

## Lock scope

Too narrow → invariant may still race. Too broad → unrelated work serializes, increasing queue/wait time. Never hold application lock across slow blocking I/O unless design explicitly requires it.

## Deadlock

If code acquires multiple locks in inconsistent order:

```text
T1 owns A, waits B
T2 owns B, waits A
```

neither progresses. Это **взаимная блокировка (deadlock)**. Более системный анализ wait-for dependencies вернётся в OS-модуле; базовая профилактика здесь — минимизировать lock count и задавать единый lock order, если locks несколько.

## Atomics — только для простого отдельного state

C11/C17 предоставляет **атомарные объекты (atomic objects)** через `<stdatomic.h>`. Например, отдельный counter можно хранить как `atomic_int` и обновлять atomic operation.

Это не превращает несколько полей Hash Table в одну атомарную транзакцию. Atomics подходят для invariants, которые действительно выражаются отдельным atomic state; compound structures обычно требуют более высокого уровня synchronization.

Детали memory ordering beyond простых counters — optional advanced concurrency.

## Rust bridge: `Send` и `Sync` теперь имеют причину

Только теперь, после появления реальных threads, полезно раскрыть два Rust contracts:

- `Send` — ownership значения разрешено переносить между threads;
- `Sync` — shared references к типу разрешено использовать между threads согласно его safety contract.

Это marker traits. `Sync` не означает «внутри есть mutex» и не доказывает отсутствие deadlock/business-logic race.

## Практика

1. Собери controlled counter race fixture, явно помеченный **BROKEN EXAMPLE**, и проверь ThreadSanitizer там, где он поддерживается.
2. Исправь вариант mutex-ом и объясни guarded invariant.
3. Отдельно сделай простой atomic counter и объясни, почему этот приём нельзя механически перенести на всю Hash Table.

## Exit check

Почему atomic counter может быть полностью корректен рядом с логически сломанным shared Hash Table state, и почему один mutex вокруг всего request может быть корректным, но плохо масштабироваться?