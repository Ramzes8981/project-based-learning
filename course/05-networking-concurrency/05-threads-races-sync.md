# 5.5 — Threads, races, mutexes и condition variables

**Теория:** ~90 мин  
**Lab:** ~90 мин  
**С телефона:** теория — да

← [`04-framing-protocol-design.md`](04-framing-protocol-design.md) · → [`06-thread-pool-backpressure.md`](06-thread-pool-backpressure.md)

## Цель

Понять shared-memory concurrency и построить bounded producer/consumer queue foundation.

## Process vs thread

Threads одного process разделяют address space/resources, но имеют independent execution contexts/stacks/register state.

Shared memory делает communication дешёвой, но создаёт races.

## Data race

Conceptually:

- два threads concurrently access same memory location;
- минимум один access write;
- нет required synchronization ordering.

В C data race на ordinary non-atomic objects приводит к undefined behavior.

## `counter++` не atomic

Source expression может стать:

```text
load counter
add 1
store counter
```

Interleaving двух threads теряет update.

## Mutex

Mutex обеспечивает mutual exclusion critical section.

```text
lock
read/modify shared invariant
unlock
```

POSIX model делает locking thread owner mutex до unlock; это synchronization primitive для shared address space. citeturn932665search2turn932665search5

## Lock granularity

Один global mutex проще, но может serialize throughput.

Много fine-grained locks повышают potential concurrency, но увеличивают complexity/deadlock risk.

Начинай с simple correct design, потом measure.

## Deadlock

Классический cycle:

```text
Thread A holds L1, waits L2
Thread B holds L2, waits L1
```

Practical prevention: global lock ordering, минимизация nested locks, bounded lock scope.

## Condition variable

Condition variable позволяет thread спать до изменения predicate/state.

Правильная mental model:

```text
lock mutex
while !predicate:
    cond_wait(cond, mutex)
// predicate true under lock
use state
unlock
```

`while`, не `if`: wakeups могут быть spurious, а другой thread может забрать resource до reacquire.

`cond_wait` atomically releases mutex while waiting и reacquires before return according to pthread semantics.

## Lab — counter/race

1. Несколько threads increment shared counter без lock → наблюдай problem (не полагайся, что проявится каждый run).
2. Исправь mutex.
3. Собери bounded queue с mutex+condition variables.

Если ThreadSanitizer доступен/совместим, используй как diagnostic tool; отсутствие report не proof.

## Causal questions

1. Почему `counter++` может race?
2. Почему держать mutex вокруг blocking network I/O плохо?
3. Почему `cond_wait` в `while`?
4. Как lock order предотвращает cycle?

## Exit check

Нарисуй producer/consumer queue state и predicates `not_empty`, `not_full`.
