# Module 7 — Filesystems and Database Internals

**Status:** CORE  
**Estimated effort:** 60–80 hours (~9–12 weeks)  
**Core milestone:** Simple Database in C  
**Guided lab:** current libfuse 3 filesystem examples

## Prerequisites

- file descriptors, robust I/O and processes from Module 2;
- memory/data structures from Module 1;
- virtual memory and measurement from Module 4;
- OS concepts from Module 6;
- binary representation from Module 3.

## Sources

- **PRIMARY FS THEORY:** selected OSTEP Persistence/filesystem chapters.
- **CURRENT FUSE API:** official libfuse 3 documentation/examples: https://libfuse.github.io/doxygen/
- **DATABASE PROJECT PRIMARY:** *Let's Build a Simple Database*: https://cstack.github.io/db_tutorial/
- **REFERENCE:** current SQLite architecture/file-format documentation where deeper clarification is needed.
- **RUSSIAN COMPANION:** selected database-engineering material from the Russian resources file.

The old repository FUSE tutorial is a historical/concept companion if useful. Course code targets **libfuse 3**, not FUSE 2.x APIs.

---

# Outcomes

The learner can:

- explain pathname → directory entry → inode/file metadata at a useful level;
- distinguish application buffering, OS page cache and persistent storage;
- reason about `fsync`/durability without assuming `close()` means durable storage;
- implement/modify a simple FUSE 3 filesystem callback layer;
- define a stable binary page/record layout;
- explain B/B+ tree motivation and page-oriented indexes;
- implement the cstack-style single-file database through multi-level B-tree scope;
- distinguish what the project implements from transactions/WAL/isolation concepts it only studies.

---

# Unit 7.1 — Filesystem data model

### Learn

- file vs pathname;
- directory entry;
- inode/metadata concept;
- hard link vs symbolic link;
- permissions at a working level;
- pathname resolution;
- file offset;
- descriptor vs open-file state intuition.

### Lab

Use `stat`, `ls -li`, hard links and symlinks to answer concrete questions about identity vs names.

### Situational question

Two pathnames have different text but the same inode number. What does that imply, and what happens when one pathname is unlinked?

---

# Unit 7.2 — Buffering, cache, and durability

### Learn

Distinguish:

```text
application buffer
    ↓
libc / syscall boundary
    ↓
OS page cache
    ↓
storage device
```

Study:

- buffered vs direct-looking application I/O concept;
- page cache;
- dirty pages;
- `fsync`/`fdatasync` concept;
- crash vs orderly close;
- atomicity is not the same as durability.

### Industry case

An application writes a configuration/database file, receives success, then power is lost. Explain why "write returned successfully" is not sufficient evidence of durable storage.

### Practice

Design a safe-ish replace-file sequence using a temporary file + sync/rename concepts and document the durability assumptions. The exact filesystem guarantees must be checked rather than invented.

---

# Unit 7.3 — FUSE 3 guided lab

### Learn

- FUSE kernel/userspace boundary;
- high-level callback model;
- path-based operations;
- `getattr`, `readdir`, `open`, `read` at a basic level;
- errors as negative `errno` values in the API.

### Current implementation source

Start from official libfuse 3 `hello.c`, then inspect `passthrough.c`.

### Guided lab scope

1. build/run official `hello` example;
2. add one additional read-only file;
3. add a simple generated virtual file (for example process/course statistics);
4. inspect callbacks triggered by common shell operations.

### Stretch

A larger writable filesystem can be attempted later, but the full historical FUSE tutorial is not required for core completion.

---

# Unit 7.4 — Storage pages and serialization

### Learn

- page as fixed-size storage unit;
- record layout;
- offsets;
- serialization/deserialization;
- alignment/padding concerns;
- portable file format vs dumping a raw C struct;
- version/magic-number concept.

### Common novice error

Writing a C struct directly to disk and assuming its padding, endianness and type sizes define a portable durable format.

### Practice

Define a small page header/record format explicitly and inspect the bytes with `hexdump`/`xxd`.

---

# Unit 7.5 — Simple database: REPL → rows → pages

Follow/adapt cstack Parts 1–6.

### Project slices

- REPL / commands;
- statement preparation;
- fixed schema;
- row serialization;
- in-memory table;
- tests;
- pager/persistence;
- cursor abstraction.

### Course adaptations

- use course compiler warnings/sanitizers;
- tests may be written in Python rather than copying the original Ruby harness;
- error handling should be explicit;
- project README records deviations from the tutorial.

---

# Unit 7.6 — B-trees and indexes

### Learn

- why sorted page trees beat full scans for key lookup;
- B-tree/B+ tree family concept;
- node/page fan-out;
- leaf vs internal node;
- binary search within node;
- split propagation;
- tree height / logarithmic search intuition.

### Formula intuition

If an internal node has fan-out roughly `b`, a balanced tree storing `N` keys has height on the order of:

```text
log_b(N)
```

High fan-out is important for page-oriented storage because it reduces I/O levels.

### Project slices

Adapt cstack Parts 7–14:

- leaf-node format;
- binary search/duplicate keys;
- leaf split;
- recursive search;
- internal nodes;
- parent updates;
- internal-node split.

---

# Unit 7.7 — Buffer/cache and query-path reasoning

### Learn

- logical operation vs physical page access;
- page cache/buffer-pool concept;
- sequential scan vs index lookup;
- index read amplification;
- extra indexes improve reads but cost storage/writes.

### Instrumentation task

Count or log page accesses for:

- full scan;
- key lookup;
- inserts causing splits.

Use evidence to explain the trade-off.

---

# Unit 7.8 — Transactions, WAL, and isolation: conceptual foundation

The cstack milestone **does not implement a real transactional WAL system**. The course must not mark these concepts as learned merely because the database persists.

### Learn conceptually

- transaction / atomic commit;
- write-ahead logging idea;
- crash recovery idea;
- durability;
- isolation anomalies at a high level;
- locking/MVCC concept comparison;
- ACID as properties, not a marketing checklist.

### Scenario questions

- What if the process crashes halfway through a page split?
- What if two writers modify related pages concurrently?
- Why does "data is in a file" not imply transaction durability/correct recovery?

### Required artifact

Write a one-page failure/recovery design note explaining **what the course database cannot guarantee** and what components a production design would need.

No fake WAL implementation is required just to tick a checkbox.

---

# Core milestone rubric — Simple Database

### Required implementation

- command/REPL layer;
- row serialization;
- persistent pager;
- cursor abstraction;
- multi-level B-tree key lookup/insertion through agreed tutorial scope;
- duplicate-key behavior;
- automated tests.

### Storage correctness

- explicit page format documented;
- no reliance on undocumented struct dumps for persistent format;
- boundary/page-split tests;
- project reopens persisted data correctly within supported assumptions.

### Performance reasoning

Show page-access measurements for at least scan vs indexed key lookup.

### Transfer task

Choose one:

- page-access instrumentation;
- `.btree` visualization improvement;
- delete/read operation extension;
- secondary-index design prototype (implementation optional depending scope);
- file-format version/magic header.

### Engineering review

Explain data path:

```text
command -> parser/statement -> cursor/index -> page -> OS cache -> storage
```

and list unsupported transactional/recovery guarantees explicitly.

---

# Exit gate

Given a database performance or corruption scenario, the learner can separate query/index behavior, page layout, caching, persistence and transaction/recovery concerns instead of treating "the database" as one black box.