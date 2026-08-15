# 6.1 — Process states, context switch и scheduling

**Теория:** ~70 мин  
**Упражнения:** ~60 мин  
**С телефона:** да

← [`README`](README.md) · → [`02-memory-pressure-page-replacement.md`](02-memory-pressure-page-replacement.md)

## Цель

Понять, почему scheduler оптимизирует конфликтующие цели и как CPU virtualization создаёт иллюзию одновременного выполнения множества runnable tasks.

## Process/thread state

Упрощённая модель:

```text
NEW
 ↓
RUNNABLE/READY ↔ RUNNING
      ↑            ↓
      └─ BLOCKED/WAITING

RUNNING -> TERMINATED
```

Точные kernel state names сложнее. Для reasoning важно различать:

- runnable — готов использовать CPU;
- running — сейчас выполняется;
- blocked/sleeping — ждёт event/I/O/timer/synchronization.

## Context switch

Чтобы сменить running task, OS сохраняет/восстанавливает execution state:

- registers;
- instruction pointer;
- stack pointer;
- scheduler/accounting state;
- address-space context where relevant.

Context switch имеет cost: kernel work, cache/TLB disruption и потеря locality.

Это не означает «threads всегда медленные» — cost зависит от workload и scheduler behavior.

## Preemption

Timer interrupts/other scheduling events позволяют kernel забрать CPU у running task и выбрать другой.

Без preemption CPU-bound process мог бы monopolize processor, если сам не yield/block.

## Scheduling goals

Конфликтующие metrics:

```text
turnaround = completion - arrival
response   = first_run - arrival
waiting    = time runnable but not running
throughput = completed jobs / time
```

Interactive workload хочет низкий response time. Batch workload может ценить throughput. Fairness и cache locality тоже конкурируют.

## FIFO

First-Come First-Served прост, но long job впереди создаёт convoy effect для коротких jobs.

## Shortest Job First intuition

Если duration известна, short jobs first уменьшает average turnaround в idealized model. В реальности точное future runtime неизвестно и starvation long jobs unacceptable.

## Round Robin

Runnable tasks получают time quantum по кругу.

Слишком маленький quantum → много context switches.

Слишком большой → interactive response приближается к FIFO behavior.

Modern general-purpose schedulers сложнее, но эти модели раскрывают trade-offs.

## Multi-core

Scheduler решает не только «кто следующий», но и placement/migration между CPUs. Migration может терять cache affinity.

## Exercise

Даны jobs:

```text
A arrival=0 burst=8
B arrival=1 burst=2
C arrival=2 burst=1
```

Нарисуй FCFS и idealized non-preemptive SJF schedule. Вычисли turnaround/response для каждого и averages.

Затем обсуди, почему SJF невозможно идеально реализовать без знания future bursts.

Разбор: [`01-scheduling-process-states.solution.md`](01-scheduling-process-states.solution.md).

## Exit check

Почему нельзя одновременно гарантировать минимум response time каждому task и отсутствие scheduling overhead/нечестности?
