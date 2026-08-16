# Module 9 — Systems Integration & Architecture

**Цель:** собрать предыдущие low-level знания в один измеримый single-node service и принимать architecture decisions через requirements, quantitative constraints, failure modes и evidence.

**Оценка:** ~50–70 часов.  
**Core capstone:** Persistent KV Service.

## Уроки

1. [`01-requirements-boundaries-state.md`](01-requirements-boundaries-state.md) — requirements + workload/capacity assumptions.
2. [`01b-computational-limits-p-np.md`](01b-computational-limits-p-np.md) — границы алгоритмической решаемости/масштабирования.
3. [`02-protocol-idempotency-contracts.md`](02-protocol-idempotency-contracts.md)
4. [`03-queueing-latency-capacity.md`](03-queueing-latency-capacity.md)
5. [`04-backpressure-timeouts-overload.md`](04-backpressure-timeouts-overload.md)
6. [`05-persistence-shutdown-recovery.md`](05-persistence-shutdown-recovery.md)
7. [`06-observability-sli-slo.md`](06-observability-sli-slo.md)
8. [`07-architecture-decisions-security.md`](07-architecture-decisions-security.md)
9. [`08-scaling-second-node.md`](08-scaling-second-node.md)
10. [`09-final-review.md`](09-final-review.md)

## Проект

[`project/SPEC.md`](project/SPEC.md) · [`project/README.md`](project/README.md)

Архитектура начинается не с boxes, а с [`project/WORKLOAD.md`](project/WORKLOAD.md): traffic, data size, concurrency, latency/resource targets и measurement method. Только после этого выбираются queue/storage/concurrency policies.

Capstone не требует microservices/replication. Сначала нужно измерить single-node bottleneck и доказать, что второй узел решает реальную проблему.
