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

## Deadlock preview

If code acquires multiple locks in inconsistent order:

```text
T1 owns A, waits B
T2 owns B, waits A
```

neither progresses. Full resource-wait analysis returns in OS module; core prevention here: minimize lock count and define global lock order when multiple locks are unavoidable.

## Atomics — only for the right invariant

Atomic integer can make one read-modify-write indivisible, but does not automatically protect multi-field Hash Table invariants. Use atomics for clearly independent atomic state/counters; use higher-level synchronization for compound structures.

Memory ordering details beyond simple counters are optional advanced concurrency.

## Rust bridge: `Send` and `Sync` now have a reason

Only now, after real threads exist:

- `Send` means ownership of a value may be transferred to another thread when the type's contract allows it;
- `Sync` means shared references to the type may be used across threads safely according to its contract.

They are marker traits expressing type-level concurrency safety properties. `Sync` does **not** mean “contains a mutex”, and compiler approval does not prove your business invariant or absence of deadlock.

## Практика

1. Build controlled counter race fixture **marked BROKEN EXAMPLE** and observe with ThreadSanitizer where supported.
2. Fix with mutex and explain guarded invariant.
3. For KV store list which fields need same lock to preserve one logical operation.

## Exit check

Why can `atomic<int> size` coexist with a broken non-atomic Hash Table state, and why does one mutex around entire request hurt concurrency even if correct?