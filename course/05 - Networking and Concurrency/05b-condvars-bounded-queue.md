# 5.6 — Как ждать работу без busy loop и зачем очереди нужен предел

**Теория:** ~90 мин · **Практика:** ~90 мин · **С телефона:** теория — да

← [`05-threads-races-sync.md`](05-threads-races-sync.md) · → [`06-thread-pool-backpressure.md`](06-thread-pool-backpressure.md)

## Проблема 1: mutex не умеет ждать condition эффективно

Worker должен спать, пока queue пустая. Плохой вариант:

```text
loop:
  lock
  check queue
  unlock
  repeat immediately
```

Это **активное ожидание (busy waiting)** тратит CPU и постоянно конкурирует за lock.

## Condition variable

**Условная переменная (condition variable)** позволяет thread уснуть, пока другой thread не сообщит, что связанное состояние могло измениться.

Критическая mental model:

```text
predicate/state защищён mutex
condition variable только сообщает «проверь predicate снова»
```

Поэтому predicate проверяется в цикле:

```c
pthread_mutex_lock(&q->mu);
while (q->count == 0 && !q->stopping) {
    pthread_cond_wait(&q->not_empty, &q->mu);
}
/* predicate determines action */
pthread_mutex_unlock(&q->mu);
```

Почему `while`, не `if`: wake может быть spurious, либо другой worker изменит state раньше, чем этот thread снова получит mutex.

## Проблема 2: бесконечная очередь не создаёт производительность

Если producers кладут work быстрее, чем workers забирают, queue растёт вместе с memory usage и waiting time.

**Ограниченная очередь (bounded queue)** имеет максимальный размер. Когда она заполнена, нужно выбрать наблюдаемую policy:

```text
producer waits/slows
или new work rejected
или upstream temporarily stops sending more work
```

Когда downstream заставляет upstream замедлить поступление новой работы вместо бесконечного накопления, это называют **обратным давлением (backpressure)**.

Следующий урок сравнит конкретные overload policies; здесь важно понять, почему bound создаёт необходимость такой policy.

## Queue invariants

Для ring buffer:

```text
0 <= count <= capacity
head/tail inside [0, capacity)
каждый queued item owned exactly once
stop state eventually wakes all waiters
```

## Shutdown — часть concurrency design

Workers, спящие на empty queue, должны проснуться при shutdown. `stopping` flag защищается тем же mutex, после перехода выполняется signal/broadcast.

Для queued connection descriptor ownership transfer должен быть однозначным: после успешного enqueue ответственность переходит queue/worker; при failure остаётся у producer. Иначе возможны descriptor leak или double close.

## Практика

Сначала build bounded queue с одним producer/consumer, затем несколькими workers. Проверь empty wait, full behavior, shutdown while workers sleep и ownership на enqueue failure.

## Exit check

Почему condition variable требует отдельного predicate под mutex и почему bounded capacity неизбежно превращает overload в explicit policy decision?