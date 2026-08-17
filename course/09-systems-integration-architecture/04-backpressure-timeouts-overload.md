# 9.4 — Что делать, когда система физически не успевает

**Теория:** ~75 мин · **Failure experiment:** ~2–4 часа · **С телефона:** да

← [`03-queueing-latency-capacity.md`](03-queueing-latency-capacity.md) · → [`05-persistence-shutdown-recovery.md`](05-persistence-shutdown-recovery.md)

## Проблема

Если входящий поток устойчиво больше service capacity:

```text
arrival > completion
→ backlog grows
```

Неограниченная очередь не создаёт capacity. Она превращает overload в растущие latency и memory usage.

## Контролируемый отказ

Система должна решить, что делать при исчерпании capacity:

- временно перестать принимать новую работу;
- блокировать upstream;
- быстро отклонять часть запросов;
- ограничивать concurrency;
- сбрасывать менее важную работу.

Механизм, который не даёт downstream бесконечно поглощать excess work, называется **обратным давлением (backpressure)**.

Быстрое контролируемое `BUSY` иногда полезнее, чем «принять» запрос и ответить уже после client deadline.

## Timeout budget

Timeout относится ко всему пути:

```text
connect + queue + service + storage + response
```

Если request уже почти исчерпал deadline в queue, выполнение дорогой работы может быть бессмысленным — зависит от protocol semantics.

## Retry feedback loop

```text
service slows
→ clients timeout
→ clients retry
→ offered load grows
→ service slows more
```

Поэтому retries должны иметь bounds/backoff/jitter и учитывать idempotency.

## Queue bound

Слишком большая queue повышает worst-case waiting time и memory. Слишком маленькая может зря отвергать короткие bursts.

Bound выбирают под workload/latency target и затем проверяют экспериментом.

## Failure experiment

Нагрузить service выше sustainable capacity и записать:

- offered/completed rate;
- queue depth;
- p50/p95/p99;
- rejects;
- memory;
- CPU/storage observations.

Измени **одну** policy и сравни результаты.

## Exit check

Что происходит с новым request в момент, когда все workers заняты и bounded queue заполнена? Ответ должен быть частью service contract.