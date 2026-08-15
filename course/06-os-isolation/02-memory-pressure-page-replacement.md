# 6.2 — Memory pressure, page replacement и COW deeper

**Теория:** ~70 мин  
**Lab:** ~60 мин  
**С телефона:** да

← [`01-scheduling-process-states.md`](01-scheduling-process-states.md) · → [`03-deadlocks-semaphores-condvars.md`](03-deadlocks-semaphores-condvars.md)

## Цель

Понять, что virtual memory — не только address translation: OS управляет limited physical memory и выбирает, какие pages сохранять resident.

## Resident set

Process может иметь большой virtual address space, но лишь часть pages resident в physical RAM.

При pressure kernel может:

- drop clean file-backed pages и перечитать позже;
- write dirty data согласно subsystem policy;
- reclaim anonymous pages через swap, если configured;
- kill processes при severe out-of-memory conditions depending system policy.

Не предполагай, что swap всегда включён или одинаков на всех systems.

## Page replacement intuition

Ideal replacement знал бы future accesses и удалял page, которая понадобится позже всех. Реальная OS будущего не знает.

Учебные policies:

- FIFO;
- LRU concept;
- CLOCK/approximation intuition.

## Locality

Temporal/spatial locality делает LRU-like heuristics полезными: recently used pages вероятнее понадобятся снова — но это heuristic, не закон.

## Thrashing

Если active working sets превышают available physical memory, system может тратить много времени на page movement/fault handling вместо useful work.

Symptoms:

- high fault/reclaim activity;
- storage/swap I/O;
- low useful throughput;
- latency spikes.

## COW deeper

`fork` может share pages до write. Когда parent/child пишут, protection fault позволяет kernel создать private copy.

COW trade-off:

- cheap fork for exec-heavy patterns;
- large child writes can materialize many copied pages.

## Shared memory mapping

`MAP_SHARED`/shared-memory mechanisms позволяют processes intentionally map shared pages. Тогда synchronization/protocol нужен, иначе logical/data races возможны между processes.

## Lab

Напиши program с configurable memory region:

- map large region;
- touch every page;
- touch sparse pages;
- read `/proc/self/status`/available metrics;
- сравни virtual/resident observations.

Не пытайся intentionally exhaust host RAM.

## Exercise

Для 3 physical frames и reference string:

```text
1 2 3 1 4 1 2 5
```

проведи FIFO page replacement manually. Затем сравни qualitatively с LRU.

Разбор: [`02-memory-pressure-page-replacement.solution.md`](02-memory-pressure-page-replacement.solution.md).

## Exit check

Почему page fault rate может быть performance symptom, но один page fault сам по себе не ошибка?
