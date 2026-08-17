# 9.3 — Почему запрос может быть медленным, даже когда сама работа быстрая

**Теория:** ~80 мин · **Упражнение:** ~60 мин · **Project:** ~90 мин · **С телефона:** да

← [`02-protocol-idempotency-contracts.md`](02-protocol-idempotency-contracts.md) · → [`04-backpressure-timeouts-overload.md`](04-backpressure-timeouts-overload.md)

## Проблема

Storage operation занимает 2 ms, но клиент видит p99 = 150 ms. Значит, большая часть времени живёт **не там, где выполняется storage code**.

## Разложи latency

```text
input/network wait
+ queue wait
+ lock/service/storage work
+ output wait
= observed request latency
```

До оптимизации спроси: **где находится время?**

## Очередь появляется из разницы скоростей

Если work приходит быстрее, чем resource обслуживает его в конкретный момент, requests ждут.

Для упрощённого одного bottleneck resource:

```text
utilization ≈ arrival_rate / service_capacity
```

При приближении к saturation queueing delay обычно резко растёт. Точная форма зависит от workload distributions и architecture.

Нет универсального правила вроде «80% CPU всегда предел».

## Little's Law

Для стабильной системы в steady state:

```text
L = λ × W
```

где:

- `L` — среднее число элементов в системе;
- `λ` — средняя пропускная способность потока;
- `W` — среднее время элемента в системе.

Пример:

```text
500 req/s × 0.040 s ≈ 20 requests in flight average
```

Это consistency relation для подходящих steady-state measurements, не магическая capacity formula.

## Concurrency не равна throughput

Больше workers помогают, если есть параллельный CPU/I/O capacity. Они могут и ухудшить систему через:

- lock contention;
- context switching;
- cache locality loss;
- serialized storage;
- competition за общую очередь.

## Tail latency

p95/p99 показывают хвост distribution. Редкие fsync, page fault, lock convoy, scheduler delay или slow client могут почти не менять median, но сильно менять p99.

## Практика

Инструментируй как минимум:

```text
enqueue timestamp
service start timestamp
service finish timestamp
```

Сравни queue latency и service latency на low/medium/near-saturation load.

Разбор toy checks: [`03-queueing-latency-capacity.solution.md`](03-queueing-latency-capacity.solution.md).

## Exit check

При высоком p99 какой первый вопрос полезнее: «сколько ещё threads добавить?» или «в каком участке пути находится время?» Почему?