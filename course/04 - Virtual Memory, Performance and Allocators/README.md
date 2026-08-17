# Module 4 — Почему адрес программы не равен ячейке RAM и откуда берётся стоимость памяти

**Оценка:** ~30–45 часов.  
**Prerequisite:** C memory model, process model, CPU/ISA basics. **Знание cache hierarchy не предполагается** — оно появляется внутри этого модуля.

## Уроки

1. [`01-virtual-address-space-mmap.md`](01-virtual-address-space-mmap.md) — **Почему два процесса могут использовать одинаковый адрес и не видеть одну память**.
2. [`02-page-tables-tlb-faults.md`](02-page-tables-tlb-faults.md) — **Как машина переводит адрес небольшими блоками и что происходит при первом обращении**.
3. [`03-cache-locality-working-set.md`](03-cache-locality-working-set.md) — **Почему одинаковое число C-операций может стоить очень по-разному**.
4. [`04-measurement-profiling.md`](04-measurement-profiling.md) — **Как отличить реальный bottleneck от красивой догадки**.
5. [`05-allocator-design.md`](05-allocator-design.md) — **Как выдавать выровненные блоки из собственного region**.
6. [`05b-free-lists-coalescing.md`](05b-free-lists-coalescing.md) — **Как вернуть свободный блок и снова использовать его без потери соседнего места**.
7. [`06-module-checkpoint.md`](06-module-checkpoint.md) — checkpoint.

## Проект

[`project/README.md`](project/README.md) — Arena Allocator. Final requirements staged: сначала alignment/bump, затем free-list/reuse/coalescing/metrics.

## Что изменено относительно старой структуры

- page tables больше не используются в 4.1 до их объяснения;
- cache больше не hidden prerequisite;
- прежний один перегруженный allocator lesson разделён на два learning cycles;
- performance claims требуют measurement protocol.