# 4.1 — Почему два процесса могут использовать одинаковый адрес и не видеть одну память

**Теория:** ~70 мин · **Лаб:** ~60 мин · **С телефона:** теория — да

← [`README`](README.md) · → [`02-page-tables-tlb-faults.md`](02-page-tables-tlb-faults.md)

## Проблема

Pointer prints a numeric address. Beginner mental model often becomes:

> «Это номер физической ячейки RAM».

Но два processes can show the same numeric address while referring to different data. ASLR can also move program mappings between runs.

So process pointer value is not a raw physical RAM coordinate.

## Virtual address space

Each process operates in its own **виртуальном адресном пространстве (virtual address space)** — range of addresses whose meanings are controlled by hardware + OS mappings for that process.

```text
process A: 0x... → A's mapped storage
process B: 0x... → B's mapped storage
```

Same virtual number can map differently or be unmapped.

We intentionally do **not** name the internal translation data structure yet. Next lesson asks: “how can mapping be represented efficiently?”

## Regions, permissions, mappings

A process address range can be mapped readable/writable/executable with OS/hardware-enforced permissions. Some regions back executable/library/file contents; others anonymous memory.

`/proc/<pid>/maps` on Linux lets us observe ranges and permissions. Observation first; detailed page mechanism next.

## `mmap` as mapping request

Linux/POSIX-style `mmap` asks kernel to create mapping in process virtual address space. It can be anonymous or file-backed.

Core lab uses anonymous read/write mapping only after checking `MAP_FAILED`, and releases it with `munmap`.

Do not teach `mmap` as “malloc but lower-level”. It has different granularity/contracts, mapping/file semantics and failure modes.

## ASLR preview without name dependency

You may observe addresses differ across runs. The security mechanism name ASLR is introduced formally in Module 8; here call it address-layout randomization observation only.

## Практика

1. Print addresses of code/local/dynamic object and compare across runs/processes.
2. Inspect `/proc/self/maps` and locate broad regions without memorizing labels.
3. Create small anonymous mapping, write/read within it, unmap.
4. Explain why numeric virtual address alone does not reveal physical RAM location.

Разбор: [`01-virtual-address-space-mmap.solution.md`](01-virtual-address-space-mmap.solution.md).

## Exit check

Why can two processes safely have the same virtual address value with different contents?