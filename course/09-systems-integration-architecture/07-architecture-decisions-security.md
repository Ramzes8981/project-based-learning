# 9.7 — ADR, trade-offs и security review

**Теория:** ~85 мин  
**Review:** ~2–3 часа  
**С телефона:** да

← [`06-observability-sli-slo.md`](06-observability-sli-slo.md) · → [`08-scaling-second-node.md`](08-scaling-second-node.md)

## Цель

Фиксировать architecture как решения под constraints, а не как набор technologies.

## ADR

Architecture Decision Record минимум:

```text
Context
Decision
Alternatives considered
Consequences
Status/date
```

Хороший ADR отвечает «почему так» и сохраняет rejected alternatives.

## Candidate decisions

Capstone минимум 3 ADR:

- thread pool vs event loop;
- persistence snapshot vs append log/SimpleDB reuse;
- queue capacity/backpressure policy;
- protocol framing/versioning;
- in-memory cache/index policy.

## Trade-off structure

Не пиши:

> thread pool проще.

Пиши:

```text
workload: <= N concurrent connections, handlers block on storage briefly
benefit: simple synchronous code
cost: per-thread stack/context scheduling
risk: lock contention
measurement: worker saturation/queue metrics
revisit when: connection count/idle ratio exceeds X evidence
```

## Security review: assets/boundaries/input

Минимум:

### Assets

- persistent values;
- service availability;
- host resources;
- configuration/metrics/logs.

### Trust boundaries

Network input is untrusted even in local lab mental model.

Persistent file can become corrupt/untrusted after crash/manual mutation.

### Input validation

- frame lengths;
- key/value limits;
- numeric overflow;
- protocol version;
- filesystem paths/config.

### Resource exhaustion

- connections;
- queue;
- frame memory;
- disk growth;
- threads;
- logs.

### Least privilege

Service не должен запускаться root без feature requirement. Debug/isolation labs earlier needed special capabilities, but capstone ordinary KV should use ordinary user permissions.

## Secrets

Core has no authentication/TLS. Therefore document:

> service must not be exposed to hostile/public network as production system.

Do not bolt fake crypto/auth to tick a box.

## Failure modes

Use simple FMEA-like list:

```text
failure
cause
observable signal
impact
mitigation/recovery
```

## Exercise

Создай 3 ADR + top 10 failure/security review items.

## Exit check

Architecture quality оценивается соответствием constraints/evidence, а не количеством boxes.
