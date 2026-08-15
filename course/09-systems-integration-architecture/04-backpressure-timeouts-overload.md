# 9.4 — Backpressure, load shedding и timeout budgets

**Теория:** ~80 мин  
**Failure experiment:** ~2–4 часа  
**С телефона:** да

← [`03-queueing-latency-capacity.md`](03-queueing-latency-capacity.md) · → [`05-persistence-shutdown-recovery.md`](05-persistence-shutdown-recovery.md)

## Цель

Сделать overload controlled failure mode, а не бесконечный рост queue/latency/memory.

## Overload

Если incoming work устойчиво больше service capacity:

```text
arrival > completion
→ backlog grows
```

Unbounded queue лишь откладывает момент failure:

- latency grows;
- memory grows;
- requests expire while waiting;
- recovery after load drop slow.

## Backpressure choices

Когда capacity exhausted:

- block upstream;
- stop reading/accepting temporarily;
- reject quickly;
- shed lower-priority work;
- enforce concurrency limits.

Policy зависит service contract.

## Load shedding

Fail fast может быть лучше, чем «успешно принять» request и ответить через минуту после client timeout.

Reject metric должен отличаться от internal error.

## Timeout budget

Timeout должен учитывать whole path:

```text
connect + queue + service + storage + response
```

Если downstream timeout 5s, upstream retry every 1s может создавать request amplification.

## Retry storm

Failure → clients retry → load increases → failure worse.

Mitigations:

- bounded retries;
- exponential backoff;
- jitter;
- idempotency/dedup;
- circuit-breaking/load shedding concepts.

Capstone не требует full circuit breaker library, но review должен увидеть feedback loop.

## Queue capacity

Capacity выбирается evidence-based. Слишком маленькая → unnecessary rejects burst; слишком большая → tail latency/memory.

Bound может быть связан с acceptable queue delay + throughput:

```text
rough queue length ≈ rate * allowed queue time
```

это intuition, не точная guarantee.

## Failure experiment

Нагрузить service выше sustainable throughput.

Снять:

- queue depth over time;
- latency percentiles;
- rejects;
- memory;
- throughput.

Измени одну policy:

- queue size;
- worker count;
- reject policy.

Сравни.

## Causal questions

1. Почему unbounded queue скрывает overload, но не решает его?
2. Как retry может worsen incident?
3. Почему fast reject иногда улучшает user experience?
4. Как timeout взаимодействует с queueing?

## Exit check

У service должен быть explicit answer: что происходит с новым request, когда capacity exhausted?
