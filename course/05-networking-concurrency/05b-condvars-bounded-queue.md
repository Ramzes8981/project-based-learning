# 5.6 — Как ждать работу без busy loop и зачем очереди нужен предел

**Теория:** ~90 мин · **Практика:** ~90 мин · **С телефона:** теория — да

← [`05-threads-races-sync.md`](05-threads-races-sync.md) · → [`06-thread-pool-backpressure.md`](06-thread-pool-backpressure.md)

## Проблема 1: mutex не умеет ждать condition эффективно

Worker needs sleep until queue non-empty. Bad solution:

```text
loop:
  lock
  check queue
  unlock
  repeat immediately
```

This **busy waiting** burns CPU and repeatedly contends for lock.

## Condition variable

A **условная переменная (condition variable)** lets thread sleep until another thread signals that shared-state condition may have changed.

Critical rule:

```text
condition is state protected by mutex
condition variable is notification mechanism
```

Always re-check predicate in loop:

```c
pthread_mutex_lock(&q->mu);
while (q->count == 0 && !q->stopping) {
    pthread_cond_wait(&q->not_empty, &q->mu);
}
/* predicate now determines action */
pthread_mutex_unlock(&q->mu);
```

Why `while`, not `if`: wake can be spurious or another thread can consume state before this thread reacquires lock.

## Problem 2: unbounded queue converts overload into memory growth

If producers enqueue faster than workers drain, queue depth grows without bound.

A **bounded queue** has explicit maximum. Full queue forces policy:

```text
wait producer
reject work
shed/close connection
apply upstream backpressure
```

No policy removes overload; it decides where overload becomes visible.

## Queue invariants

For ring buffer example:

```text
0 <= count <= capacity
head/tail always inside [0, capacity)
items [logical queue] owned exactly once
stop state eventually wakes all waiters
```

## Shutdown is part of concurrency design

Workers waiting forever on empty queue must wake on shutdown. A `stopping` flag is protected by same mutex, then broadcast/signal after transition.

Design ownership of queued connection fd: once enqueue succeeds, queue/worker owns it; on enqueue failure, producer retains responsibility to close/reject. Ambiguous transfer creates descriptor leaks/double close.

## Практика

Build bounded queue with one producer/one consumer first, then multiple workers. Tests cover empty wait, full behavior, shutdown while workers sleep, ownership on enqueue failure.

## Exit check

Why does condition variable require a separate predicate protected by mutex, and how does bounded capacity turn “slow server” into explicit policy decision?