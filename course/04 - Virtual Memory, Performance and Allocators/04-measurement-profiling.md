# 4.4 — Как отличить реальный bottleneck от красивой догадки

**Теория:** ~70 мин · **Лаб:** ~100 мин · **С телефона:** theory — да

← [`03-cache-locality-working-set.md`](03-cache-locality-working-set.md) · → [`05-allocator-design.md`](05-allocator-design.md)

## Проблема

Once you know cache/TLB/page faults, almost any slowdown can be “explained” with a plausible story. Without measurement this becomes cargo-cult optimization.

## Measurement protocol

Before benchmark write:

```text
question/hypothesis
input/workload
build flags
machine/environment
metric
warmup policy
run count
what result would falsify hypothesis
```

Then measure.

## Wall time vs CPU time

Wall-clock includes waiting/scheduling/I/O. CPU time counts time process consumed CPU. Difference can be evidence of waiting but not automatic diagnosis.

## Microbenchmark traps

- compiler removes unused computation;
- input too small → timer overhead dominates;
- one run captures noise;
- debug vs optimized builds compared accidentally;
- cache warm/cold state changes;
- background load;
- benchmark changes code layout itself.

## Profiling

A **profiler** attributes sampled/measured cost to code/events. `perf` on Linux may expose cycles, instructions, faults, cache-related counters depending on permissions/hardware.

Counter name is not proof of cause. Correlate with code path/workload and controlled comparison.

## Statistics minimum

For repeated runtime samples, record distribution summary: median + range/quantiles; do not report 7 decimal places from noisy laptop run.

Latency percentiles as service SLI concept come later; here they are just distribution summaries if used.

## Практика

Take one Module 4 locality experiment:

1. state hypothesis;
2. run reproducible script/command several times;
3. collect wall time and at least one OS/hardware signal available;
4. change one variable;
5. decide whether evidence supports hypothesis.

Разбор: [`04-measurement-profiling.solution.md`](04-measurement-profiling.solution.md).

## Exit check

What evidence would make you abandon your favorite cache explanation?