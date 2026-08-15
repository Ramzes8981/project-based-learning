# Module 4 — Checkpoint

## Explain

- virtual vs physical address;
- mapping/page;
- page table/TLB;
- page fault vs TLB miss;
- COW;
- cache line/locality;
- working set;
- latency/throughput/p95/p99;
- benchmark evidence;
- alignment;
- metadata/free list;
- internal/external fragmentation;
- split/coalesce.

## Core milestone

Проверь [`project/ACCEPTANCE.md`](project/ACCEPTANCE.md).

## Required experiment

Сравни две placement policies на одинаковом deterministic workload. Не заявляй winner вне измеренного scope.

## Debug story

Найди seeded corruption:

- overlapping blocks;
- wrong coalescing;
- size arithmetic overflow;
- misalignment;
- double free.

## Exit gate

Ты можешь связать allocator layout с virtual mapping и cache/locality, а performance claim — с reproducible measurement.
