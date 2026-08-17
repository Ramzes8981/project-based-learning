# 9.8 — Почему «добавим второй сервер» меняет саму задачу

**Теория:** ~85 мин · **Design:** ~90 мин · **С телефона:** да

← [`07-architecture-decisions-security.md`](07-architecture-decisions-security.md) · → [`09-final-review.md`](09-final-review.md)

## Проблема

Single-node benchmark не достигает target. Кажется естественным добавить второй узел.

Но сначала нужно доказать, **что именно является bottleneck**.

## Сначала evidence

Проверь:

- CPU saturation;
- network bandwidth;
- storage latency/throughput;
- global lock;
- queue/worker capacity;
- memory/working set.

Если bottleneck — неудачный O(n) scan или global mutex, второй host может лишь дороже скрыть локальную проблему.

## Stateless и stateful — разные случаи

Stateless frontend часто можно реплицировать сравнительно просто.

KV service хранит authoritative mutable state. Два узла сразу создают вопрос:

> кто владеет каким состоянием и что видит клиент при partial failure?

## Partitioning

Разделяем keys между owners.

Новые вопросы: routing, rebalance, hot keys, node failure, cross-partition operations.

## Replication

Несколько nodes имеют копии state.

Новые вопросы:

- кто принимает writes;
- когда write acknowledged;
- stale reads;
- ordering/conflicts;
- failover authority;
- replication lag.

## Timeout снова становится ambiguity

Node failure и network partition нельзя надёжно различить по одному timeout. Автоматический failover без coordination может породить split brain.

Consensus/quorum/fencing — реальные следующие темы, но **не core capstone**.

## Практика

На основе измеренного bottleneck ответь:

1. поможет ли second instance;
2. что произойдёт со state;
3. нужен partitioning или replication;
4. какие guarantees изменятся;
5. какие минимум 5 failure modes появятся.

Не реализуй distributed version только ради галочки.

## Exit check

Почему второй узел для stateful service — это не просто «в два раза больше throughput»?