# 5.5 — Threads, races, mutexes и condition variables

**Теория:** ~95 мин  
**Lab:** ~90 мин  
**С телефона:** теория — да

← [`04-framing-protocol-design.md`](04-framing-protocol-design.md) · → [`06-thread-pool-backpressure.md`](06-thread-pool-backpressure.md)

## Цель

Понять shared-memory concurrency и построить bounded producer/consumer queue foundation.

## Process vs thread

Threads одного process разделяют address space и многие process resources, но имеют собственные execution stacks/register context.

Shared memory уменьшает copying, но создаёт synchronization obligations.

## C data race

Если два threads обращаются к одному ordinary object concurrently, минимум один access write и нет требуемой synchronization/happens-before relation, C program имеет data race и undefined behavior.

`counter++` концептуально:

```text
load
add
store
```

и не становится atomic только потому, что source line одна.

## Mutex

Mutex сериализует critical section и создаёт synchronization around shared invariant:

```text
lock
check/change shared state
unlock
```

Для POSIX mutex normal rule: thread, который успешно владеет mutex, освобождает его согласно выбранному mutex type/contract. Не проектируй code, где arbitrary thread «на всякий случай unlock чужой mutex».

## Lock scope

Начинай с coarse lock, если так correctness очевиднее, затем измеряй. Fine-grained locks могут повысить parallelism, но добавляют lock-order/deadlock/state complexity.

Не держи store mutex вокруг slow network read/write без необходимости: один client способен задержать всех workers.

## Deadlock

```text
A holds L1 -> waits L2
B holds L2 -> waits L1
```

Практические техники:

- global lock ordering;
- minimal nested locks;
- не вызывать unknown callbacks под lock без contract;
- не делать blocking I/O под shared-state lock без причины.

## Condition variable = wait for predicate

Правильная форма:

```text
lock mutex
while predicate false:
    cond_wait(cond, mutex)
use/update state
unlock
```

`cond_wait` conceptually atomically releases associated mutex while sleeping and reacquires it before return. Проверка — `while`, не `if`: wakeup не является доказательством, что predicate всё ещё true; возможны spurious wakeups/competition.

## Bounded queue predicates

```text
not_empty: size > 0
not_full:  size < capacity
```

Producer waits `not_full`, pushes under lock, signals/broadcasts `not_empty`. Consumer зеркально.

## Shutdown state

Queue обычно требует дополнительный state `stopping/closed`. Иначе workers могут навсегда ждать empty queue во время server shutdown.

## Lab

1. Counter race experiment — наблюдение, не «доказательство отсутствия race», если value случайно правильный.
2. Исправить mutex.
3. Bounded queue + two condvars + shutdown flag.
4. Если ThreadSanitizer совместим с environment, использовать как diagnostic; clean run не proof.

## Exit check

Нарисуй queue state machine и точно напиши predicates, которые проверяются в `while`.
