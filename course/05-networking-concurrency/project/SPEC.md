# Concurrent KV Server — SPEC

## Storage

Используй собственную C Hash Table Module 1 или адаптированную course-owned implementation ученика.

## Protocol

Length-prefixed binary protocol из Lesson 5.4.

Обязательно:

- version;
- opcode;
- bounded frame length;
- explicit key/value lengths;
- network byte order;
- success/error responses.

## Operations

- GET;
- SET;
- optional DELETE transfer/base depending chosen scope.

## Networking

- address-independent socket setup;
- robust partial I/O;
- peer shutdown/malformed frames;
- no raw struct serialization.

## Concurrency core

```text
acceptor -> bounded queue -> fixed worker pool -> shared store
```

- mutex-protected shared store baseline;
- queue condvars;
- explicit full-queue policy;
- graceful shutdown plan.

## Metrics

- accepted/completed/errors/rejected;
- latency samples/percentiles via harness;
- active connections;
- queue depth.

## Non-goals

- TLS;
- production authentication;
- distributed replication;
- lock-free structures.
