# 9.1 — Requirements, boundaries и state ownership

**Теория:** ~65 мин  
**Design exercise:** ~90 мин  
**Project slice:** ~60 мин  
**С телефона:** да

← [`README`](README.md) · → [`02-protocol-idempotency-contracts.md`](02-protocol-idempotency-contracts.md)

## Цель

Перевести расплывчатое «сделать быстрый KV-сервис» в проверяемые functional/non-functional requirements и component boundaries.

## Functional requirements

Функция описывает **что** service делает:

- `GET key`;
- `SET key value`;
- `DELETE key`;
- persistence across restart;
- multiple clients.

Но этого недостаточно для architecture.

## Non-functional requirements

Нужно определить ограничения/targets:

- maximum key/value/frame size;
- expected concurrent connections;
- target request rate workload;
- latency objective;
- memory bound;
- durability expectation;
- graceful shutdown behavior;
- operating environment.

Target — не bragging number. Он должен иметь workload и test method.

## Component boundaries

Capstone можно разложить:

```text
network listener
  ↓
protocol decode/encode
  ↓
work scheduling / queue
  ↓
KV service logic
  ↓
storage/index
  ↓
pager/filesystem
```

Boundary полезна, если имеет contract и ownership, а не просто box on diagram.

## State inventory

Для каждого state:

```text
state
owner
mutable by whom
lifetime
persistence
synchronization
failure impact
```

Примеры:

- listening fd;
- client connection;
- work queue;
- in-memory index;
- persistent file;
- metrics counters;
- shutdown flag.

## Single source of truth

Если одна logical сущность хранится в двух местах, нужно определить synchronization/recovery contract.

Например in-memory index + disk log/pages: кто authoritative после restart?

## Architecture diagram

Диаграмма должна показывать:

- components;
- data/control flow;
- state placement;
- concurrency boundaries.

Не рисуй future Kafka/Redis/Kubernetes, которых нет в requirements.

## Exercise

Перед code напиши `ARCHITECTURE.md` v0:

1. 5–10 functional requirements;
2. 5–10 non-functional constraints;
3. component diagram;
4. state ownership table/list;
5. three known non-goals.

## Causal questions

1. Почему `fast` не requirement без workload/metric?
2. Почему component boundary без contract мало полезна?
3. Чем in-memory state отличается от durable source of truth?
4. Почему early microservices могут добавить failure modes без solving bottleneck?

## Exit check

Каждый box диаграммы должен отвечать: что входит, что выходит, какое state owns и как ломается.
