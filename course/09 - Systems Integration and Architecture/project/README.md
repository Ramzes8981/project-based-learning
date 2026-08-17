# Persistent KV Service — рабочий README

Этот файл заполняется по мере проекта. Не копируй сюда SPEC целиком — фиксируй **своё реализованное решение и evidence**.

## Build / Run

Exact commands, platform assumptions, compiler flags.

## Requirements / workload

Ссылки на `WORKLOAD.md` и список guarantees/non-goals.

## Architecture

Ссылка на `ARCHITECTURE.md` и кратко:

```text
boundaries
state owners
threading/synchronization
resource bounds
```

## Protocol

Ссылка на `PROTOCOL.md`: framing, limits, errors, timeout/retry semantics.

## Persistence / recovery

Ссылка на `RECOVERY.md`: acknowledgement guarantee и known failure limits.

## Observability

Ссылка на `METRICS.md`: definitions и способ получить measurements.

## Tests

Unit/property/integration/system/load/failure-injection strategy и exact commands.

## Benchmark evidence

Запиши hardware/OS/build, workload, duration/sample count, throughput, p50/p95/p99, queue/service latency и saturation observations.

## Debugging story

Минимум один реальный случай:

```text
symptom
hypotheses
evidence/tool
root cause
fix
regression test
```

## ADR / security limitations

Ссылки на решения, alternatives и trust/resource boundaries.

## 10× / second-node conclusion

Что ломается первым по измерениям? Можно ли исправить local design? Какие новые state/failure problems добавит второй узел?