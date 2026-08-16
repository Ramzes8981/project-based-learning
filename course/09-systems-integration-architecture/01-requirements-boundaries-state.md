# 9.1 — Requirements, workload, boundaries и state ownership

**Теория:** ~90 мин  
**Design exercise:** ~2 часа  
**Project slice:** ~90 мин  
**С телефона:** да

← [`README`](README.md) · → [`01b-computational-limits-p-np.md`](01b-computational-limits-p-np.md)

## Цель

Перевести «сделать быстрый KV-сервис» в измеримый workload/constraints contract до выбора architecture.

## Functional requirements

Минимум capstone:

```text
GET / SET / DELETE
multiple clients
persistent state after clean restart
graceful shutdown
metrics/status
```

Functional список говорит **что**, но почти не отвечает **сколько/как хорошо**.

## Quantitative workload model

До architecture задай baseline **гипотезы**, не «истину рынка»:

```text
steady RPS:
burst RPS + duration:
read/write/delete ratio:
concurrent connections:
key size distribution:
value size distribution:
working-set size:
total records / storage growth:
restart/recovery time target:
```

Для учебного локального сервиса числа могут быть скромными. Главное — один и тот же workload использовать при сравнении designs.

## Service targets

Пример структуры, а не готовые числа:

```text
p95 latency <= target at baseline load
p99 <= target at burst load or explicit overload begins
resident memory <= budget
queue capacity <= bound
storage file growth <= explained model
shutdown <= target when queue has N items
```

Каждый target содержит **metric + workload + observation window/tool**. `fast`, `scalable`, `low memory` без этого — не requirements.

## Rough capacity arithmetic

До benchmark полезны sanity estimates:

```text
memory ≈ records × (key + value + index/allocator overhead)
network ingress ≈ RPS × average request bytes
storage growth/day ≈ successful writes/day × average durable bytes/write
```

Это order-of-magnitude model. Затем измерение уточняет assumptions.

## Component boundaries

```text
listener/connection lifecycle
↓
protocol codec
↓
bounded scheduler/queue
↓
KV semantics
↓
storage/index
↓
pager/filesystem
```

Boundary обязан иметь:

```text
input/output contract
state owner
threading/synchronization rule
failure behavior
resource limit
observability
```

## State inventory

Для listening fd, connections, tasks, index, persistent file, metrics, shutdown state запиши:

```text
owner
lifetime
mutable by whom
persistent/ephemeral
synchronization
recovery source of truth
failure impact
```

## Architecture exercise

Создай/обнови:

- [`project/WORKLOAD.md`](project/WORKLOAD.md);
- `ARCHITECTURE.md` с components/data flow/state ownership;
- 5–10 functional requirements;
- quantitative non-functional targets;
- минимум 5 non-goals.

Сделай две оценки: baseline и hypothetical 10×. Не добавляй второй узел — только покажи, какой resource первым может стать bottleneck.

## Exit check

Любое число в architecture review должно отвечать: откуда hypothesis, чем измерим и какое решение оно способно изменить?
