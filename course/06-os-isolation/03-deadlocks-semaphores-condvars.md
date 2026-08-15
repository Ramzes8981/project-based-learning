# 6.3 — Deadlock, semaphore и synchronization design

**Теория:** ~80 мин  
**Lab:** ~90 мин  
**С телефона:** да

← [`02-memory-pressure-page-replacement.md`](02-memory-pressure-page-replacement.md) · → [`04-ipc-models.md`](04-ipc-models.md)

## Цель

Углубить concurrency: deadlock conditions, semaphore semantics, condition predicates и debugging blocked threads.

## Deadlock conditions

Классическая модель Coffman conditions:

1. mutual exclusion;
2. hold and wait;
3. no preemption of resource;
4. circular wait.

Все четыре вместе позволяют deadlock. Разрушение хотя бы одного condition может предотвратить этот класс cycle.

## Lock ordering

Если все code paths приобретают locks по global order:

```text
L1 before L2 before L3
```

circular wait между ними невозможен.

Ordering требует discipline/API design; comments без enforcement могут деградировать.

## Semaphore

Counting semaphore хранит conceptual count available units.

`wait/P/down` уменьшает или blocks when unavailable.

`post/V/up` увеличивает/wakes.

Binary semaphore может выглядеть как mutex, но ownership semantics отличаются: mutex обычно имеет owning thread/unlock contract, semaphore — count/signal primitive.

## Condition variable revisited

Condition variable не хранит «event happened forever». Это coordination around shared predicate protected by mutex.

Correct pattern:

```text
lock
while predicate false:
    wait(cond, mutex)
use/update state
unlock
```

Signal without state/predicate reasoning приводит к lost assumptions.

## Spurious wakeup

Wait может вернуться даже без desired predicate true; кроме того, другой awakened thread может изменить state до reacquisition.

Поэтому `while`, не `if`.

## Starvation

Program может не deadlock, но один thread бесконечно не получает resource/scheduling progress из-за unfair policy/contention.

Deadlock = никто в cycle не может продвинуться. Starvation = отдельный participant может не продвигаться.

## Priority inversion preview

Low-priority thread держит lock, high-priority ждёт, medium-priority постоянно выполняется → effective priority inversion. OS/RT systems могут иметь inheritance protocols.

Core только понимает phenomenon.

## Lab — deadlock diagnosis

Создай controlled two-lock deadlock в отдельной test program.

1. воспроизведи;
2. attach GDB;
3. inspect all thread backtraces;
4. найди lock cycle;
5. исправь global ordering;
6. добавь documentation/test strategy.

## Causal questions

1. Почему semaphore не всегда заменяет mutex?
2. Почему condition variable должна быть связана с predicate?
3. Чем starvation отличается от deadlock?
4. Как thread backtraces показывают wait cycle?

## Exit check

При hang concurrent program первым делом классифицируй: deadlock, blocked I/O, condition predicate bug или просто slow work.
