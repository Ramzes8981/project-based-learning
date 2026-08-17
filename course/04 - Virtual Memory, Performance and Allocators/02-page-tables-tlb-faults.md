# 4.2 — Как машина переводит адрес небольшими блоками и что происходит при первом обращении

**Теория:** ~90 мин · **Лаб:** ~75 мин · **С телефона:** theory — да

← [`01-virtual-address-space-mmap.md`](01-virtual-address-space-mmap.md) · → [`03-cache-locality-working-set.md`](03-cache-locality-working-set.md)

## Проблема

Mapping every possible byte address individually would require absurd metadata. Need group addresses into fixed-size chunks and map/protect them together.

## Page

A fixed-size chunk used by virtual-memory mapping is a **страница (page)**. Common Linux x86-64 base page is often 4096 bytes, but code should query system where needed instead of universalizing 4 KiB.

Virtual address splits conceptually:

```text
virtual page number | offset inside page
```

Offset remains same during translation; mapping chooses physical frame/backing for virtual page.

## Page table

Data structures used by hardware/OS to translate virtual pages and store permissions/presence are **таблицы страниц (page tables)**.

Real x86-64 uses multi-level tables because flat table for enormous address space is wasteful. Core needs causal idea, not memorization of all level names.

## TLB

Walking page tables for every memory access would be expensive. CPU caches recent address translations in **Translation Lookaside Buffer (TLB)**.

This is the first time term TLB is needed: translation itself created repeated lookup cost.

TLB is not ordinary data cache; it caches address-translation information.

## Page fault

If translation cannot proceed normally — mapping not present yet, permission violation, file-backed data absent, copy-on-write event etc. — CPU transfers control to OS fault handler. This is **page fault**.

Not every page fault means program crash. OS may satisfy valid demand mapping and resume instruction. Invalid/unpermitted access may result in signal such as `SIGSEGV`.

## Demand allocation intuition

`mmap`/allocation can reserve virtual range before every physical backing frame is actually touched. First write may trigger minor fault and materialization. Thus “reserved virtual bytes” ≠ “resident physical memory right now”.

## Observe

Use `getrusage`, `/usr/bin/time -v`, or `/proc` counters available in environment to compare page-fault behavior when touching a newly mapped region page by page.

Do not infer exact physical allocation policy from one counter; state what it measures.

## Практика

1. Query page size with `sysconf(_SC_PAGESIZE)`.
2. `mmap` a moderate anonymous region.
3. Record fault/RSS-like evidence before touch and after touching one byte per page.
4. Protect one region `PROT_NONE` only in controlled child fixture if exploring fault signal; mark broken/intentional.

Разбор: [`02-page-tables-tlb-faults.solution.md`](02-page-tables-tlb-faults.solution.md).

## Causal questions

1. Why map chunks/pages instead of each byte independently?
2. Why does repeated page-table lookup motivate TLB?
3. Why is page fault not synonym for segmentation fault?

## Exit check

Draw virtual address → page/offset → page-table translation → possible TLB hit/miss → physical backing or fault.