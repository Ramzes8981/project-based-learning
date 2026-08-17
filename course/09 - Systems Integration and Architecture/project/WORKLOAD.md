# Capstone workload & targets

Заполни до выбора финальной architecture.

## Environment

```text
CPU:
RAM:
OS/kernel:
storage:
compiler/build flags:
```

## Data model

```text
key size distribution:
value size distribution:
record count / working set:
initial file size:
growth assumption:
```

## Traffic

```text
steady RPS target:
burst RPS target + duration:
GET/SET/DELETE ratio:
concurrent connections:
connection reuse policy:
```

## Service objectives for experiment

```text
p50:
p95:
p99:
throughput:
max queue depth:
reject policy:
RSS/memory budget:
shutdown target:
recovery target:
```

Targets are course hypotheses. After measurements update them only with an ADR/explanation; do not move goalposts to make benchmark green.

## 10× scenario

Multiply one relevant dimension at a time and estimate first bottleneck before building anything distributed.
