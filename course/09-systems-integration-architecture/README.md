# Module 9 — Systems Integration & Architecture

**Цель:** собрать предыдущие low-level знания в один измеримый single-node service и научиться принимать architecture decisions через requirements, failure modes и evidence.

**Оценка:** ~40–55 часов.  
**Core capstone:** Persistent KV Service.

## Уроки

1. [`01-requirements-boundaries-state.md`](01-requirements-boundaries-state.md)
2. [`02-protocol-idempotency-contracts.md`](02-protocol-idempotency-contracts.md)
3. [`03-queueing-latency-capacity.md`](03-queueing-latency-capacity.md)
4. [`04-backpressure-timeouts-overload.md`](04-backpressure-timeouts-overload.md)
5. [`05-persistence-shutdown-recovery.md`](05-persistence-shutdown-recovery.md)
6. [`06-observability-sli-slo.md`](06-observability-sli-slo.md)
7. [`07-architecture-decisions-security.md`](07-architecture-decisions-security.md)
8. [`08-scaling-second-node.md`](08-scaling-second-node.md)
9. [`09-final-review.md`](09-final-review.md)

## Проект

[`project/SPEC.md`](project/SPEC.md)

Capstone не требует microservices/replication. Сначала нужно доказать качество и bottleneck одного узла.
