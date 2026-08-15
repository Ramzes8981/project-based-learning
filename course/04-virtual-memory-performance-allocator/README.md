# Module 4 — Virtual Memory, Performance, and Allocators

**Status:** CORE  
**Estimated effort:** 35–50 hours (~5–7 weeks)  
**Core milestone:** arena allocator over a controlled memory region

## Why this module is here

The previous course placed the allocator before enough virtual-memory context. That creates a hidden conceptual jump: the learner can manipulate blocks without understanding where process memory comes from.

This module first establishes virtual-memory and cache models, then implements an allocator **inside a region obtained with a modern interface**.

## Prerequisites

- Module 1 manual memory and data structures;
- Module 3 machine/architecture model;
- basic Unix APIs from Module 2.

## Sources

- **PRIMARY:** Dive into Systems — memory hierarchy/performance sections.
- **PRIMARY COMPANION:** selected OSTEP virtual-memory chapters.
- **CURRENT API:** POSIX/Linux `mmap`, `munmap`, `sysconf` documentation.
- **HISTORICAL REFERENCE ONLY:** *Memory Allocators 101* from the repository.

The historical tutorial uses `sbrk()`. `sbrk()` was removed from POSIX and must not be the course's recommended allocator backend. Read the tutorial for allocator structure, not for modern API choice.

---

# Outcomes

The learner can:

- distinguish virtual addresses from physical memory;
- explain pages, page faults and TLB at a working level;
- reason about cache locality and working-set behavior;
- benchmark code without confusing one noisy timing with evidence;
- explain allocator metadata, alignment and fragmentation;
- implement allocation/free within a controlled arena;
- compare allocation policies with measurements.

---

# Unit 4.1 — Process address space and virtual memory

### Learn

- virtual address;
- pages and page size;
- mappings;
- page fault intuition;
- page tables and TLB at a conceptual level;
- anonymous vs file-backed mapping;
- `mmap` / `munmap`;
- `/proc/<pid>/maps` on Linux.

### Lab

Create several mappings, inspect `/proc/self/maps`, touch pages and observe behavior with tools where practical.

### Situational question

Why can a program reserve a large virtual region without immediately consuming the same amount of physical RAM?

---

# Unit 4.2 — Memory hierarchy and locality

### Learn

- registers, caches, RAM, storage latency hierarchy;
- cache line;
- spatial/temporal locality;
- contiguous vs pointer-heavy layout;
- working set;
- cache miss intuition.

### Lab

Compare traversal patterns over the same amount of data:

- sequential;
- large stride;
- pointer-chasing.

Record runtime over repeated runs and explain likely causes.

### Bridge to NumPy

Connect contiguous arrays, vectorized kernels and memory access patterns to existing high-level numerical code.

---

# Unit 4.3 — Measurement discipline

### Learn

- latency vs throughput;
- warm-up/noise;
- multiple samples;
- median and percentile intuition;
- optimization requires a measured bottleneck;
- profiler vs timer.

### Practice rubric

A performance claim must state:

1. workload;
2. input size;
3. measurement method;
4. repeated results;
5. environment assumptions;
6. hypothesis explaining the result.

"It felt faster" does not count.

---

# Unit 4.4 — Allocator model

### Learn

- arena/heap region;
- block header metadata;
- alignment;
- internal/external fragmentation;
- free list;
- first-fit / best-fit intuition;
- splitting;
- coalescing.

### Useful formula

For power-of-two alignment `a`, reason about an align-up operation conceptually as rounding `n` to the next multiple of `a`. Do not copy bit tricks before proving their preconditions.

### Common novice errors

- returning misaligned addresses;
- overlapping blocks;
- forgetting metadata size;
- integer overflow when computing requested size + metadata;
- coalescing non-adjacent blocks;
- double-free corruption.

---

# Core milestone — Arena Allocator

Obtain one large region using `mmap()` (or an explicitly course-approved backing buffer for portability) and manage allocations **inside that region**.

## Required progression

1. bump allocator;
2. aligned blocks;
3. block metadata;
4. free list;
5. block reuse;
6. splitting;
7. adjacent-block coalescing;
8. statistics.

## Required metrics

Expose at least:

- arena bytes;
- allocated/requested bytes;
- free bytes;
- number of free blocks;
- largest free block;
- allocation count.

Use these to discuss fragmentation.

## Transfer task

Compare two placement policies (for example first-fit vs best-fit) on the same deterministic workload.

Do not claim one is globally better from one benchmark.

## Debugging

Seed or encounter at least one allocator corruption bug and diagnose it with:

- invariants/assertions;
- memory pattern inspection;
- GDB/sanitizers where applicable.

---

# Industry case

A long-running service has plenty of total free memory but cannot satisfy a large request inside its custom arena. Distinguish:

- exhaustion;
- internal fragmentation;
- external fragmentation;
- leak.

Propose measurements that distinguish the cases before changing the allocator.

---

# Exit gate

The learner can draw the allocator's block layout, explain a split/coalesce operation, measure fragmentation, and connect allocator behavior to virtual memory and cache locality.