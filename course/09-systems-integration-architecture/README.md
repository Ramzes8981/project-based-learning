# Module 9 — Собираем систему и доказываем инженерные решения

**Цель:** собрать предыдущие механизмы в один измеримый single-node KV service и научиться принимать архитектурные решения от требований, ограничений и наблюдений, а не от списка технологий.

**Оценка:** ~45–65 часов.  
**Core capstone:** Persistent KV Service.

## Что уже должно быть знакомо

Перед модулем ты уже работал с TCP/framing, bounded work и threads, файлами и durability, индексами/страницами, debugging и memory safety.

Здесь почти нет новых low-level primitives. Новая задача — **связать знакомые механизмы в систему и уметь доказать, почему она устроена именно так**.

## Обязательный путь

1. [`01-requirements-boundaries-state.md`](01-requirements-boundaries-state.md) — как превратить «быстрый сервис» в проверяемые требования.
2. [`02-protocol-idempotency-contracts.md`](02-protocol-idempotency-contracts.md) — что означает timeout и когда retry безопасен.
3. [`03-queueing-latency-capacity.md`](03-queueing-latency-capacity.md) — где на самом деле живёт latency.
4. [`04-backpressure-timeouts-overload.md`](04-backpressure-timeouts-overload.md) — что делать, когда работы приходит больше, чем система успевает выполнить.
5. [`05-persistence-shutdown-recovery.md`](05-persistence-shutdown-recovery.md) — что именно означает «данные сохранены».
6. [`06-observability-sli-slo.md`](06-observability-sli-slo.md) — как сделать сервис диагностируемым.
7. [`07-architecture-decisions-security.md`](07-architecture-decisions-security.md) — как фиксировать trade-offs и проверять границы доверия.
8. [`08-scaling-second-node.md`](08-scaling-second-node.md) — почему второй узел создаёт новые проблемы со state.
9. [`09-final-review.md`](09-final-review.md) — защита capstone и cross-layer walkthrough.

## Optional

[`01b-computational-limits-p-np.md`](01b-computational-limits-p-np.md) — компактная интуиция P/NP/NP-complete. Это полезный CS-фундамент, но он **не является prerequisite для capstone**.

## Проект

Начни с [`project/SPEC.md`](project/SPEC.md), но читай его **по этапам**. Технические ограничения становятся обязательными только после соответствующего урока.

Архитектура начинается с [`project/WORKLOAD.md`](project/WORKLOAD.md), а не с диаграммы компонентов.

## Gate модуля

Модуль пройден, если для ключевого решения ты умеешь показать цепочку:

```text
requirement
→ constraint
→ design choice
→ measurement/failure evidence
→ known limitation
→ alternative
```

Не требуется строить production-ready distributed database.