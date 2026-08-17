# 6.3 — Как ожидание нескольких ресурсов превращается в deadlock и как это диагностировать

**Теория:** ~80 мин · **Практика:** ~70 мин · **С телефона:** теория — да

← [`02-memory-pressure-page-replacement.md`](02-memory-pressure-page-replacement.md) · → [`04-ipc-models.md`](04-ipc-models.md)

## Что уже известно

Module 5 уже ввёл mutex, condition variable, bounded queue and lock-order preview. Здесь не повторяем syntax. Новый вопрос: **как увидеть deadlock как структуру ожиданий ресурсов**.

## Deadlock

A **deadlock** exists when a set of execution flows cannot progress because each waits for condition/resource that can only be released by another waiting member.

Classic wait-for graph:

```text
T1 → lock B → owned by T2
T2 → lock A → owned by T1
```

Cycle in a wait-for graph is key diagnostic signal for single-instance lock resources.

## Coffman conditions as diagnostic checklist

Textbook conditions commonly associated with resource deadlock:

- mutual exclusion;
- hold and wait;
- no forced preemption of held resource;
- circular wait.

Do not memorize names as theorem decoration. Prevention works by structurally breaking at least one relevant condition: global lock order attacks circular wait; acquire-all-or-release can attack hold-and-wait, etc.

## Semaphore

A **semaphore** represents a count of permits/resources. Unlike mutex, it need not encode “one owner”. Use it when invariant is “at most N concurrent users/units”.

Binary semaphore and mutex can look similar at count=1 but ownership/error semantics differ; do not substitute by name alone.

## Condition variable is not a resource counter

Condvar notifies that predicate may have changed. It does not remember arbitrary event count like a queue/semaphore. Predicate remains source of truth under mutex.

## Diagnosis

When service hangs:

```text
which threads are blocked?
on what syscall/futex/lock?
who owns needed resource?
what lock acquisition order led here?
```

Tools may include debugger thread backtraces, `strace`, `/proc`, sanitizer/deadlock tooling where supported. Evidence should reconstruct wait graph.

## Практика

Create controlled two-lock deadlock fixture marked **BROKEN EXAMPLE**, run only with timeout guard, capture thread stacks, draw wait-for cycle. Then fix using one global lock order and add regression that stresses both operation orders without relying only on timeout.

## Exit check

Why does “add a timeout to lock” avoid infinite waiting but not prove resource-order design correct?