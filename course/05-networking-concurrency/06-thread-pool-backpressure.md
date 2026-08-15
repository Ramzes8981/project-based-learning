# 5.6 — Thread pool, bounded queue и backpressure

**Теория:** ~70 мин  
**Project slice:** ~6–10 часов  
**С телефона:** теория — да

← [`05-threads-races-sync.md`](05-threads-races-sync.md) · → [`07-poll-event-loop.md`](07-poll-event-loop.md)

## Цель

Сделать concurrency **bounded** и определить поведение overload вместо бесконтрольного создания threads/requests.

## Thread-per-connection

Просто:

```text
accept -> create thread -> handle client
```

Но при большом числе connections:

- много stacks/thread metadata;
- scheduling overhead;
- unbounded resource creation;
- attacker/overload может исчерпать resources.

## Thread pool

```text
acceptor
  ↓
bounded queue<client_fd/job>
  ↓
N worker threads
  ↓
process protocol/storage
```

Workers fixed/configured → resource concurrency bounded.

## Queue bound

Unbounded queue «решает» overload накоплением latency + memory.

Когда arrival rate > sustainable service rate долгое время, backlog растёт без конца.

Bounded queue заставляет выбрать policy:

- block acceptor/producer;
- reject connection/request;
- shed/drop work;
- apply timeout.

Нет бесплатного варианта; policy является service contract.

## Backpressure

Backpressure означает, что downstream saturation влияет на upstream behavior вместо бесконечного buffering.

## Shared KV store

Простой core design: один mutex вокруг hash table operations. Это correctness-first baseline.

Не держи store mutex во время network recv/send. Critical section должен защищать только shared state.

Позже можно измерить read/write lock/sharding experiment как transfer.

## Connection ownership

После `accept` fd owner переходит queue/worker согласно design. Нужно исключить:

- double close;
- fd leak при queue reject;
- worker exit without close.

## Graceful shutdown preview

Нужно определить:

```text
stop accepting
signal queue shutdown
workers finish/drain or abort by policy
join workers
cleanup store
```

## Project slice

Реализуй thread pool + bounded queue + synchronized Hash Table.

Public metrics:

- active/accepted connections;
- queue depth;
- rejected work;
- completed requests.

## Causal questions

1. Почему больше threads может ухудшить overload?
2. Почему bounded queue делает failure более явным?
3. Где должен close client fd при reject?
4. Почему global store mutex — разумный первый вариант, хотя не самый масштабируемый?

## Exit check

Если queue full, твой server обязан иметь **явное** поведение, а не «надеяться, что такого не будет».
