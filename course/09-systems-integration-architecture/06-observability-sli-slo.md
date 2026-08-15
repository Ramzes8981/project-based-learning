# 9.6 — Observability, logging, metrics, SLI и SLO basics

**Теория:** ~80 мин  
**Project slice:** ~3–5 часов  
**С телефона:** да

← [`05-persistence-shutdown-recovery.md`](05-persistence-shutdown-recovery.md) · → [`07-architecture-decisions-security.md`](07-architecture-decisions-security.md)

## Цель

Сделать service diagnosable: отличать traffic, latency, errors и saturation без чтения каждого source line во время incident.

## Logs vs metrics

Logs — discrete contextual events.

Metrics — aggregatable numeric time-series/counters/gauges/histograms.

Не логируй каждый request body просто чтобы «было observable»: это I/O cost, noise и privacy/security risk.

## Minimum signals

Capstone exposes/logs at least:

- requests total by operation/outcome;
- errors by category;
- latency histogram/samples;
- active connections;
- queue depth/rejects;
- storage read/write/error counts;
- startup/shutdown/recovery events.

## Cardinality

Metric label `user_id/key/request_id` with unbounded unique values creates high-cardinality explosion in real metrics systems.

Core local metrics may be simple counters, but architecture review must understand cardinality.

## SLI

Service Level Indicator — measured quantity representing user/service behavior.

Examples:

```text
successful request ratio
p95 latency under defined request population
```

## SLO

Service Level Objective — target for SLI over window/workload.

Example learning SLO:

```text
>= 99.5% valid GET/SET requests succeed
under benchmark workload X,
p95 < 20 ms on local reference host
```

Numbers are course hypotheses, not universal production requirements.

## Availability denominator

Define which requests count. Malformed client input usually shouldn't count as server availability failure; internal storage error should.

Metric definition matters more than pretty percentage.

## Health

`process alive` != service healthy. Health concept may include ability to accept/process/storage ready.

But overly aggressive health check can worsen load/restart loops.

## Correlation IDs

Request ID useful to trace a single operation across log events, but do not expose sensitive data or use unbounded ID as metric label.

## Project slice

Implement simple local observability:

- structured log lines or clear key=value format;
- counters;
- latency histogram/buckets or samples analyzed by Python;
- metrics dump endpoint/command/file acceptable.

Document definitions in `METRICS.md`.

## Exercise

Define numerator/denominator for:

- success rate;
- overload reject rate;
- malformed request rate.

Explain which indicates service failure.

## Exit check

Каждая metric должна отвечать конкретному operational question.
