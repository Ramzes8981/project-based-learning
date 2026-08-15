# 4.4 — Measurement discipline и profiling

**Теория:** ~55 мин  
**Lab:** ~60 мин  
**С телефона:** да

← [`03-cache-locality-working-set.md`](03-cache-locality-working-set.md) · → [`05-allocator-design.md`](05-allocator-design.md)

## Цель

Научиться формулировать performance claim так, чтобы его можно было воспроизвести и опровергнуть.

## Latency vs throughput

Latency — время одной operation/request.

Throughput — количество completed operations за время.

Система может увеличить throughput параллелизмом и одновременно ухудшить tail latency.

## Distribution

Average скрывает хвост.

Используем:

```text
p50 median-like
p95
p99
```

`p99 = X` означает: примерно 99% observations ≤ X при конкретной выборке/методе percentile.

Не превращай percentile в абсолютную гарантию.

## Benchmark checklist

Любой claim содержит:

1. workload;
2. input size/distribution;
3. build flags;
4. hardware/environment;
5. warm-up/setup;
6. number of runs/samples;
7. statistic;
8. before/after only one relevant change if possible.

## Compiler optimization

Debug `-O0` и optimized `-O2/-O3` могут иметь совершенно разный generated code. Benchmark release-like code, если измеряешь production-ish performance.

Но debugging UB под optimization может быть сложнее — сначала correctness/sanitizers.

## Timer pitfalls

- clock resolution;
- system noise;
- CPU frequency scheduling;
- cold cache;
- measuring I/O accidentally;
- optimizer eliminating unused calculation.

## Profiler vs timer

Timer отвечает «сколько». Profiler помогает «где/почему».

Используй profiler/perf tools там, где available, но курс не зависит от конкретного GUI.

## Exercise

Возьми два traversal variants из прошлого lab.

Составь benchmark protocol до запуска. Затем собери 20+ samples, сравни median/p95 и сформулируй осторожный вывод.

Разбор: [`04-measurement-profiling.solution.md`](04-measurement-profiling.solution.md).

## Exit check

Фраза «после optimization стало на 30% быстрее» неполна. Назови минимум пять вещей, которые должны сопровождать claim.
