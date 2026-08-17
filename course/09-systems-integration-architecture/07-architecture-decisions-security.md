# 9.7 — Как защищать архитектурное решение, а не любимую технологию

**Теория:** ~80 мин · **Review:** ~2–3 часа · **С телефона:** да

← [`06-observability-sli-slo.md`](06-observability-sli-slo.md) · → [`08-scaling-second-node.md`](08-scaling-second-node.md)

## Проблема

Фраза «thread pool проще» не объясняет, почему это хороший выбор **для этого workload и этих constraints**.

Нужен след рассуждения, который можно пересмотреть после новых измерений.

## ADR

**Architecture Decision Record (ADR)** — короткая запись решения:

```text
Context
Decision
Alternatives
Consequences
Evidence / revisit condition
```

ADR не доказывает, что решение вечно правильное. Он сохраняет **почему оно было разумным при текущих данных**.

## Пример структуры trade-off

```text
context: handlers иногда блокируются на storage; concurrency bounded
choice: fixed thread pool
benefit: простая synchronous control flow
cost: thread stacks/context scheduling
risk: lock contention
measure: queue wait + worker utilization
revisit when: evidence показывает другой bottleneck/workload
```

## Security review начинается с boundaries

Сначала перечисли assets:

- persistent values;
- availability;
- host resources;
- config/logs/metrics.

Затем trust boundaries:

- network bytes — недоверенные;
- persistent file после corruption — недоверенный input;
- config/path inputs требуют validation.

## Resource exhaustion тоже security/reliability проблема

Проверь bounds для:

- connections;
- frame length;
- queue;
- threads;
- memory per request;
- disk/log growth.

## Least privilege

Обычному KV service не нужны root privileges только потому, что прошлые isolation/debugger labs использовали специальные capabilities.

Core не требует TLS/auth. Поэтому ограничение должно быть написано честно: **это учебный сервис, не предназначенный для публичной hostile network**.

## Практика

Сделай минимум 3 ADR и top failure/security review:

```text
failure
cause
observable signal
impact
mitigation/recovery
```

## Exit check

Можешь ли ты назвать alternative, объяснить почему его не выбрал сейчас и какое новое evidence заставит решение пересмотреть?