# Persistent KV Service — staged SPEC

Ты реализуешь код сам. Этот документ описывает поведение и постепенно добавляет технические ограничения только после соответствующих уроков.

## Stage 0 — Поведение и workload

**После 9.1.**

Сервис хранит записи `key → value`.

Поведение:

- `SET` создаёт или заменяет value;
- `GET` возвращает value или `NOT_FOUND`;
- `DELETE` удаляет существующую запись и корректно сообщает отсутствие;
- несколько клиентов могут пользоваться сервисом;
- есть определённый contract clean restart/shutdown;
- можно получить диагностические metrics/status.

До кода заполни `WORKLOAD.md`, functional requirements, targets и non-goals.

## Stage 1 — Protocol contract

**После 9.2.**

Переиспользуй или эволюционируй framed protocol Module 5.

`PROTOCOL.md` обязан описывать:

- wire format/version;
- maximum frame/key/value sizes;
- status/error responses;
- timeout/retry semantics;
- idempotency/duplicate limitations.

Все length arithmetic и parsing paths должны быть bounds/overflow checked до allocation/access.

## Stage 2 — Concurrency и bounded resources

**После 9.3–9.4.**

Выбери thread pool или другой уже изученный model и обоснуй его.

Обязательно:

- explicit owner mutable KV state;
- synchronization rules;
- bounded connections/work/frame memory;
- явная overload policy;
- defined shutdown wake/drain behavior.

## Stage 3 — Persistence

**После 9.5.**

Выбери **один** понятный storage contract:

1. адаптированный SimpleDB;
2. append-only mutation log + replay;
3. snapshot + in-memory index.

`RECOVERY.md` должен точно сказать, что означает successful write acknowledgement и какие failure cases могут потерять/corrupt data.

Не заявляй WAL/transaction guarantees, которых implementation не имеет.

## Stage 4 — Observability

**После 9.6.**

Минимум:

- request outcomes;
- latency distribution;
- queue vs service latency;
- queue depth/rejects;
- active connections;
- storage errors/operations;
- lifecycle/recovery events.

Definitions находятся в `METRICS.md`.

## Stage 5 — Failure/architecture evidence

**После 9.7–9.9.**

Нужны:

- `ARCHITECTURE.md`;
- минимум 3 ADR;
- `SECURITY_LIMITATIONS.md`;
- reproducible load report;
- overload experiment;
- malformed/oversized input tests;
- graceful and forced termination experiments;
- corrupted/truncated **copy** recovery test;
- injected storage error;
- 10× / second-node analysis.

## Non-goals

Core не требует:

- TLS/auth production security;
- replication/consensus;
- Kubernetes/microservices;
- public deployment;
- production-grade transactional database.

Уменьшить guarantee честно лучше, чем реализовать непроверяемую «production-like» архитектуру.