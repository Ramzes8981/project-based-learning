# Module 9 — Systems Integration and Architecture Capstone

**Status:** CORE CAPSTONE  
**Estimated effort:** 40–55 hours (~6–8 weeks)  
**Capstone:** observable persistent KV service built from prior-course ideas

## Why this module exists

The course should not end with isolated low-level projects.

An engineer/architect must be able to recombine knowledge about data structures, processes, networking, concurrency, storage, performance, observability and failure into one system and explain the trade-offs.

This capstone is intentionally smaller than a production distributed system. Deep replication/consensus remains an advanced branch.

## Prerequisites

Core Modules 0–8 completed or equivalent exit gates passed.

## Sources

- **PRIMARY COURSE-LED:** this capstone specification and review process.
- **OPERABILITY REFERENCE:** selected free Google SRE book/workbook chapters, especially monitoring and SLO thinking: https://sre.google/
- **ARCHITECTURE CHECKLIST REFERENCE:** selected AWS Well-Architected questions/pillars, used as a review framework rather than an AWS product course.

No new giant architecture textbook is required.

---

# Outcomes

The learner can:

- turn functional requirements into component boundaries;
- define an explicit service protocol and storage contract;
- identify state ownership and concurrency boundaries;
- measure latency, throughput, errors and saturation;
- design bounded queues/backpressure;
- reason about graceful shutdown and persistence;
- distinguish retry-safe from non-idempotent operations;
- run failure experiments and observe results;
- create an architecture diagram and ADR-style decision notes;
- identify the bottleneck before proposing scaling mechanisms.

---

# Capstone scenario

Build a single-node persistent key/value service for an internal application.

The service must support at least:

- `GET`;
- `SET`;
- delete or equivalent mutation;
- persistence across restart;
- multiple concurrent clients;
- bounded resource usage for incoming work;
- observable health/metrics.

Use prior components or ideas rather than blindly combining old repositories. Reuse is allowed when interfaces are understood.

---

# Unit 9.1 — Requirements and architecture boundary

### Define functional requirements

Example:

- key/value operations;
- maximum key/value size;
- persistence requirement;
- expected concurrency;
- error semantics.

### Define non-functional targets

Choose modest measurable targets for the local environment, for example:

- target requests/s under a defined workload;
- p95/p99 latency target;
- maximum queue depth;
- memory bound;
- restart/recovery expectation.

Targets are hypotheses/constraints, not bragging numbers.

### Artifact

Create an architecture diagram:

```text
clients
  ↓
protocol/parser
  ↓
concurrency / bounded queue
  ↓
service logic
  ↓
storage
  ↓
filesystem / OS
```

Document component ownership/state boundaries.

---

# Unit 9.2 — Interface and protocol design

### Learn/apply

- versioned protocol field or explicit contract;
- request IDs where useful;
- maximum frame size;
- stable error responses;
- idempotency distinction;
- malformed-input behavior.

### Situational question

A client times out after sending `SET`, then retries because it never received the response. Could the operation have succeeded twice or partially? Define what the protocol can and cannot guarantee.

---

# Unit 9.3 — Latency, throughput, utilization, queueing

### Metrics

Track at minimum:

- throughput (requests/s);
- p50/p95/p99 latency;
- error rate;
- active connections;
- queue depth/rejections;
- CPU/memory signal where practical.

Google SRE's four-golden-signals framing is useful here: latency, traffic, errors and saturation.

### Queueing intuition

Introduce Little's Law for a stable system:

```text
L = λW
```

where:

- `L` = average number of items in the system;
- `λ` = average arrival/throughput rate;
- `W` = average time in the system.

Use it as a reasoning tool, not a guarantee for arbitrary unstable workloads.

### Exercise

Given two measured quantities, estimate the third and compare with observed queue/concurrency behavior.

---

# Unit 9.4 — Backpressure and overload

### Learn

- bounded queues;
- overload vs failure;
- rejection/load shedding;
- timeout budget;
- why adding more threads can worsen overload;
- saturation signals.

### Failure experiment

Drive the service above sustainable throughput.

Record:

- latency curve;
- queue depth;
- errors/rejections;
- CPU/memory behavior.

Then change one backpressure policy and compare.

---

# Unit 9.5 — Persistence and shutdown

### Learn/apply

- clean shutdown sequence;
- stop accepting new work;
- drain/reject queued work according to policy;
- flush/close storage;
- durability assumptions;
- restart behavior.

### Failure scenarios

Test at least:

- normal graceful shutdown;
- forced process termination;
- malformed storage/input where safe to simulate;
- unavailable/full-like storage condition simulated in a controlled way.

Document what can be recovered and what cannot.

---

# Unit 9.6 — Observability

### Required signals

Expose or log:

- request count;
- error count/type;
- latency distribution or buckets/samples;
- queue depth/rejections;
- startup/shutdown/recovery events.

### Logging rules

- logs describe events/context, not every loop iteration;
- do not log sensitive payloads by default;
- errors should identify operation/context sufficiently for debugging.

### SLI/SLO introduction

Define one simple service-level indicator and one learning SLO, e.g. successful request ratio or p95 latency under a stated test load.

Do not turn this into a full SRE curriculum.

---

# Unit 9.7 — Architecture decisions

Create at least three short ADR-style notes:

```text
Context
Decision
Alternatives considered
Consequences / trade-offs
```

Good topics:

- thread pool vs event loop;
- in-memory index vs scan;
- framing choice;
- persistence strategy;
- queue/backpressure policy.

### Anti-pattern

Architecture diagrams without decisions, constraints or failure behavior do not count as architecture reasoning.

---

# Unit 9.8 — Capacity and scaling thought experiment

Do **not** immediately invent microservices/sharding.

Given measured bottlenecks, answer:

1. What resource saturates first?
2. Can vertical improvement solve it?
3. Which state prevents horizontal replication?
4. What consistency question appears if storage is replicated?
5. What new failure modes are introduced by a second node?

This becomes the entrance test for the advanced Distributed Systems branch.

---

# Core capstone rubric

## Functional

- documented protocol;
- core KV operations;
- concurrent clients;
- persistence/restart;
- bounded input/work behavior.

## Quality

- tests for normal/boundary/malformed requests;
- no unexplained compiler warnings;
- appropriate memory/concurrency checks;
- README with run/test instructions.

## Performance

- reproducible load-test method;
- throughput + latency percentiles;
- saturation/backpressure observation;
- no performance claim without workload definition.

## Reliability

- graceful shutdown;
- at least three controlled failure scenarios;
- limitations documented.

## Architecture artifacts

- component/data-flow diagram;
- state/ownership map;
- three ADRs;
- metrics/SLO note;
- 10× scaling analysis.

## Transfer

One substantial change must be designed from first principles rather than copied from an earlier tutorial.

---

# Exit gate

The learner can answer an architecture review starting from evidence:

> Here are the requirements, here is where state lives, here are the measured bottlenecks/failures, here are the trade-offs, and here is what I would change next.

Passing this module completes the finite Systems Engineering Core. Distributed systems, kernel engineering, reverse engineering/exploitation, Rust, compilers and embedded work become specialized branches.