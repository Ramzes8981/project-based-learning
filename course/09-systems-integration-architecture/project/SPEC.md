# Persistent KV Service — Capstone SPEC

## Goal

Собрать single-node service из изученных mechanisms, но не copy-paste giant monolith.

## Functional

- GET;
- SET;
- DELETE;
- multiple concurrent clients;
- persistent state across clean restart;
- graceful shutdown;
- status/metrics inspection.

## Protocol

Reuse/evolve Module 5 framed protocol. `PROTOCOL.md` обязателен.

## Concurrency

Reuse thread pool or justified event-loop design.

- bounded work;
- explicit overload behavior;
- synchronized state;
- shutdown coordination.

## Storage

Выбери и обоснуй один:

1. reuse/adapt SimpleDB;
2. append-only KV log + recovery;
3. snapshot + in-memory index for smaller scope.

Choice должен иметь explicit durability/recovery contract.

## Observability

Minimum:

- request outcomes;
- p50/p95/p99;
- queue/service latency separation;
- queue depth/rejects;
- active connections;
- storage errors/operations;
- lifecycle events.

## Failure experiments

At least:

- overload;
- malformed/oversized input;
- graceful shutdown;
- forced process kill;
- corrupted/truncated storage copy;
- injected storage error.

## Architecture artifacts

- `ARCHITECTURE.md`;
- `PROTOCOL.md`;
- `METRICS.md`;
- `RECOVERY.md`;
- at least 3 ADR files/section;
- `SECURITY_LIMITATIONS.md`;
- load-test report;
- 10×/second-node analysis.

## Non-goals

- TLS/auth production security;
- multi-node replication;
- consensus;
- Kubernetes/microservices;
- production deployment.
