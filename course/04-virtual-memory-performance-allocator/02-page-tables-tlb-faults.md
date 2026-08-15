# 4.2 — Page tables, TLB и page faults

**Теория:** ~70 мин  
**Упражнения:** ~45 мин  
**С телефона:** да

← [`01-virtual-address-space-mmap.md`](01-virtual-address-space-mmap.md) · → [`03-cache-locality-working-set.md`](03-cache-locality-working-set.md)

## Цель

Понять translation path virtual address → page → physical frame и почему TLB/page faults влияют на performance.

## Разбиение адреса

При page size `P = 2^k` virtual address можно conceptually разделить:

```text
virtual page number | page offset(k bits)
```

Offset внутри page не меняется при translation; меняется mapping virtual page → physical frame.

## Page table

Page table хранит translation metadata и permissions:

```text
VPN -> PPN/frame + present/read/write/execute/... metadata
```

Современные 64-bit systems используют multi-level page tables, чтобы не выделять гигантскую плоскую таблицу для всего address space.

Точные x86-64 level details будут optional; важно понять tree-like walk.

## TLB

Translation Lookaside Buffer — cache недавних virtual→physical translations.

Если translation в TLB — CPU избегает полного page-table walk.

TLB miss ≠ page fault. При TLB miss translation может быть валидна в page tables и просто потребовать walk.

## Page fault

Page fault возникает, когда memory access требует kernel handling.

Причины разные:

- valid mapping, page ещё не backed/loaded → minor/major-style handling;
- copy-on-write;
- protection violation;
- unmapped invalid access.

Не каждый page fault = segfault. Kernel может обслужить legitimate fault и продолжить instruction.

## Demand paging

File/anonymous page может появиться физически только при first access. Это позволяет lazy allocation/loading.

## Copy-on-write и `fork`

После `fork` parent/child могут первоначально share physical pages read-only-like under COW. При write kernel создаёт private copy для изменяющего process.

Это объясняет, как `fork` может быть эффективнее полного eager copy address space.

## Working set

Working set — pages/data, активно используемые workload в данном интервале. Если working set не помещается в fast memory/cache/physical RAM, возрастает churn/misses/faults.

## Exercise

Для page size 4096:

1. разложи addresses `0`, `4095`, `4096`, `8193` на page number + offset;
2. нарисуй две virtual pages разных processes, mapped на один shared frame;
3. затем COW write одного process → новый frame;
4. объясни TLB miss vs page fault.

Разбор: [`02-page-tables-tlb-faults.solution.md`](02-page-tables-tlb-faults.solution.md).

## Exit check

Если performance counter показывает много TLB misses, почему это ещё не доказывает swap/page-fault problem?
