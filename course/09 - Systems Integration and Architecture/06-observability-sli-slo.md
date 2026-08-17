# 9.6 — Как понять, что происходит внутри сервиса, не читая весь код

**Теория:** ~75 мин · **Project:** ~3–5 часов · **С телефона:** да

← [`05-persistence-shutdown-recovery.md`](05-persistence-shutdown-recovery.md) · → [`07-architecture-decisions-security.md`](07-architecture-decisions-security.md)

## Проблема

Пользователь говорит: «сервис тормозит».

Без наблюдений неизвестно, это queue, storage, lock, network, malformed traffic или overload.

**Наблюдаемость (observability)** в scope курса — способность получить из runtime signals достаточно evidence для диагностики состояния системы.

## Logs и metrics решают разные задачи

**Logs** — отдельные события с контекстом.

**Metrics** — агрегируемые числа во времени: counters, gauges, histograms/samples.

Логировать каждый request body «на всякий случай» плохо: I/O cost, noise и утечка sensitive data.

## Минимальные signals capstone

- requests по operation/outcome;
- errors по категории;
- latency distribution;
- queue depth/rejects;
- active connections;
- storage operations/errors;
- startup/shutdown/recovery events.

## SLI и SLO

**Показатель уровня сервиса (Service Level Indicator, SLI)** — измеряемая величина, отражающая полезное поведение.

Например: success ratio или p95 latency для определённой группы requests.

**Цель уровня сервиса (Service Level Objective, SLO)** — target для SLI в определённом workload/window.

Учебный пример структуры:

```text
при workload X
valid GET/SET success ratio >= target
и p95 latency <= target
```

Значения не являются production рекомендацией.

## Denominator matters

Если malformed client request считать «server failure», availability metric будет отвечать не на тот вопрос. Metric definition должна явно задавать population.

## Cardinality

Нельзя бездумно использовать `request_id`, key или user ID как metric label: число уникальных time series может взорваться. В local capstone достаточно простых bounded dimensions.

## Project slice

Создай `METRICS.md`: для каждой metric запиши definition, units, labels/categories и operational question.

## Exit check

Для каждой metric можешь закончить фразу: **«Я смотрю на неё, чтобы отличить X от Y»**?