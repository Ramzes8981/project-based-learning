# Systems Engineering Progress Tracker

> Progress companion to [`course/README.md`](course/README.md).
>
> The module READMEs define what to learn. This file tracks **where we are**, what evidence exists, and why the course changed. It intentionally does not duplicate every lesson checkbox.

## Current status

- **Weekly capacity:** 6–8 hours
- **Primary programming background:** Python / data stack
- **Mobile:** Android; theory/mobile exercises in metro, project work PC-first
- **Canonical desktop environment:** Windows + WSL2/Ubuntu
- **Current module:** Module 0 — C Fast Start
- **Current unit:** 0.1 — Source → executable
- **Current active project:** MiniKV v0 — not started
- **Core completion:** 0 / 10 modules

---

# Course progress

| Module | Status | Core evidence |
|---|---|---|
| [0 — C Fast Start](course/00-c-fast-start/README.md) | ⬜ Not started | MiniKV v0 + exit gate |
| [1 — Memory & Data Structures](course/01-memory-data-structures/README.md) | ⬜ Not started | Hash Table + Vector + exit gate |
| [2 — Unix & Shell](course/02-unix-shell/README.md) | ⬜ Not started | Unix Shell + exit gate |
| [3 — Computer Architecture](course/03-computer-architecture/README.md) | ⬜ Not started | Nand2Tetris 1–6 + VM/Emulator |
| [4 — Virtual Memory & Performance](course/04-virtual-memory-performance-allocator/README.md) | ⬜ Not started | Arena Allocator + measurements |
| [5 — Networking & Concurrency](course/05-networking-concurrency/README.md) | ⬜ Not started | Concurrent KV Server |
| [6 — OS & Isolation](course/06-os-isolation/README.md) | ⬜ Not started | Modern isolation lab |
| [7 — Filesystems & Databases](course/07-filesystems-databases/README.md) | ⬜ Not started | Simple Database + FUSE guided lab |
| [8 — Binaries / Debugging / Security](course/08-binaries-debugging-security/README.md) | ⬜ Not started | Minimal Debugger in C |
| [9 — Systems Integration / Architecture](course/09-systems-integration-architecture/README.md) | ⬜ Not started | Persistent KV service capstone |

Status values:

- ⬜ Not started
- 🟨 In progress
- 🟦 Consolidating / review
- ✅ Passed exit gate

---

# Current-module working record

Use this only for the active module.

## Module 0 — C Fast Start

### Current unit

**0.1 — Source → executable**

### Assigned source

_To be filled when the first lesson starts._

### Understanding state

Use:

- `Seen`
- `Explain`
- `Apply`
- `Transfer`

| Concept | State | Notes |
|---|---|---|
| source / compiler / executable | — | |
| `main` / exit status | — | |
| compiler diagnostics | — | |

### Exercise evidence

- [ ] compile/run a tiny C program
- [ ] modify/rebuild it
- [ ] explain one compiler diagnostic

### MiniKV slice

- [ ] project directory/README
- [ ] plain-language contract

### Current blockers

_None._

---

# Milestone evidence index

Each completed core milestone should link to evidence rather than just get a checkmark.

| Milestone | Repository/path | Tests | Transfer feature | Engineering review | Status |
|---|---|---|---|---|---|
| MiniKV / Hash Table | — | — | — | — | ⬜ |
| Unix Shell | — | — | — | — | ⬜ |
| VM / Emulator | — | — | — | — | ⬜ |
| Arena Allocator | — | — | — | — | ⬜ |
| Concurrent KV Server | — | — | — | — | ⬜ |
| Isolation Lab | — | — | — | — | ⬜ |
| Simple Database | — | — | — | — | ⬜ |
| Minimal Debugger | — | — | — | — | ⬜ |
| Architecture Capstone | — | — | — | — | ⬜ |

---

# Cumulative CS checkpoints

This list exists to ensure important CS fundamentals are not silently skipped. Detailed teaching belongs in module READMEs.

## Algorithms / Data Structures

- [ ] complexity: O / Ω / Θ
- [ ] linear + binary search
- [ ] elementary sorting
- [ ] dynamic array
- [ ] linked list / stack / queue
- [ ] hashing
- [ ] BST / heap concepts
- [ ] recursion / invariants
- [ ] DP fundamentals
- [ ] graphs / BFS / DFS
- [ ] Dijkstra / priority queue

## Computer Architecture

- [ ] binary / hex / signed representation
- [ ] gates / ALU
- [ ] registers / RAM
- [ ] CPU / fetch-decode-execute
- [ ] machine code / assembly
- [ ] stack / ABI basics
- [ ] cache / locality

## Operating Systems

- [ ] processes / FDs / syscalls
- [ ] scheduling
- [ ] virtual memory / pages / TLB
- [ ] threads / synchronization / deadlocks
- [ ] IPC
- [ ] filesystems
- [ ] namespaces / cgroup v2

## Networking / Storage / Architecture

- [ ] IP / routing / TCP / UDP
- [ ] socket framing / partial I/O
- [ ] concurrency / backpressure
- [ ] pages / B-tree / indexes
- [ ] durability / WAL / isolation concepts
- [ ] latency / throughput / percentiles
- [ ] observability / SLI-SLO basics
- [ ] capacity / scaling reasoning

---

# Learning log

Record only meaningful events: passed gates, major blockers, source replacements, course-order changes, or discoveries that change the plan.

| Date | Event / finding | Evidence / reason | Course adjustment |
|---|---|---|---|
| 2026-08-15 | Initial systems roadmap created | Needed durable path around project-based-learning milestones | Added first roadmap + progress tracker |
| 2026-08-15 | Project-first rule adopted | Exercises alone do not create development experience | Interleaved theory → exercise → project slice |
| 2026-08-15 | Russian resource layer added | Mobile/metro study should not be English-only | Added Russian companions/primaries where quality is sufficient |
| 2026-08-15 | Roadmap converted to course | Previous roadmap was too complex to execute | Added canonical `course/README.md` |
| 2026-08-16 | Professional pedagogical/technical audit | Hidden prerequisites, outdated APIs, module overload, weak rubrics found | Rebuilt course into 10 audited modules; see `course/AUDIT_2026-08.md` |

---

# Instructor update rule

After a meaningful lesson or project slice:

1. update the current unit/state here;
2. add evidence when a milestone changes;
3. do **not** create checklist bureaucracy for every five-minute exercise;
4. update the course syllabus only when the pedagogy/order/source actually changes.

The progress file should remain fast to read on a phone.