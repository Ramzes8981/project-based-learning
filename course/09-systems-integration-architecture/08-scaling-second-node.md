# 9.8 — Capacity planning и вопрос «добавить второй узел»

**Теория:** ~90 мин  
**Design exercise:** ~90 мин  
**С телефона:** да

← [`07-architecture-decisions-security.md`](07-architecture-decisions-security.md) · → [`09-final-review.md`](09-final-review.md)

## Цель

Понять, почему horizontal scaling stateful service создаёт distributed-systems problems, а не просто удваивает throughput.

## Сначала bottleneck

Перед second node ответь measured evidence:

- CPU saturated?
- network bandwidth?
- storage IOPS/latency?
- global lock?
- queue/worker capacity?
- memory/cache?

Если bottleneck single global mutex, второй process/node may help only if state partition/coordination redesigned.

## Vertical improvement

Иногда дешевле:

- better algorithm/index;
- batching;
- larger cache;
- faster storage;
- reduce copies/locks;
- more cores/RAM.

Distributed system adds operational/failure complexity.

## Stateless frontends

Stateless service легко replicate behind load balancing because requests don't require local authoritative mutable state.

KV storage is stateful: two nodes need decide how data is distributed/replicated.

## Partitioning

Key space divided:

```text
node A owns subset
node B owns subset
```

Questions:

- routing;
- rebalancing;
- hot keys;
- node failure;
- cross-partition operations.

## Replication

Same data on multiple nodes:

Questions:

- which node accepts writes?;
- when is write acknowledged?;
- what if follower is down?;
- stale reads?;
- ordering/conflicts?;
- failover authority?

## Consistency

Once replicas exist, concurrent/failure timing creates observations impossible in single process.

Linearizable/strong/eventual models belong advanced Distributed Systems branch. Core only identifies need for explicit model.

## Network partitions

Node failure vs network partition cannot be perfectly distinguished just from timeout. Automatic failover can risk split-brain if multiple leaders believe they own writes.

Consensus/quorum/fencing become real topics.

## New failure modes from node 2

- partial failure;
- network partition;
- clock skew;
- replication lag;
- duplicate/reordered requests;
- leader election;
- split brain;
- rebalancing;
- cross-node observability.

## Exercise

На основе **твоего measured bottleneck** capstone ответь:

1. поможет ли second instance?
2. что делать with state?
3. partition or replication?
4. какие guarantees потеряются/нужны?
5. какие 5 new failure modes появятся?

Не реализуй distributed version в core.

## Exit check

«Добавить сервер» для stateful system должно автоматически вызывать вопросы consistency/ownership/failure, а не только load balancer diagram.
