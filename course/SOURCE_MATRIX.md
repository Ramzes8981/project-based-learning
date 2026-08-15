# Course Source Matrix

This file answers one question:

> **Which source should I use now, and why?**

The course does not expect the learner to consume every listed source.

## Roles

- **PRIMARY** — main teaching source for the block.
- **CURRENT REFERENCE** — current API/standard/tool authority used to verify details.
- **COMPANION** — alternate explanation, often Russian-language or more visual.
- **EXERCISES** — selected drills only.
- **PROJECT REFERENCE** — useful implementation walkthrough; course spec/rubric still wins.
- **GUIDED LAB** — only assigned subset is required.
- **HISTORICAL REFERENCE** — valuable ideas, but old APIs/environment must not be copied blindly.

Authority/freshness scale used here:

- **A** — official standard/docs or strong university-origin material appropriate for the role.
- **B** — strong, widely used community/educational source with a clear limited role.
- **H** — historical source: pedagogically useful, technically needs adaptation.

---

# Module 0 — C Fast Start

| Source | Role | Rating | Use |
|---|---|---:|---|
| CS50 Russian translation (Vert Dider / JavaRush) | PRIMARY explanation | B | Russian video explanation for basic C; old edition, so not API authority |
| CS50x current Week 1–2 | CURRENT REFERENCE | A | current structure/terminology/examples |
| Stepik C exercises | EXERCISES | B | assigned syntax/array/string drills only |

**Rule:** watch/read only the exact assigned section. Do not complete both CS50 versions end-to-end.

---

# Module 1 — Memory & Data Structures

| Source | Role | Rating | Use |
|---|---|---:|---|
| Dive into Systems | PRIMARY | A | pointers, memory model, debugging, systems connection |
| CS50 Memory / Data Structures | COMPANION | A | alternate visual explanation |
| CSC/Stepik Algorithms & Data Structures | COMPANION / EXERCISES | A/B | selected Russian algorithm/DS blocks |
| James Routley — Write a Hash Table in C | PROJECT REFERENCE | B | compare hash-table design after simpler course implementation is understood |

**Rule:** Dive teaches the model; the project teaches integration; CSC/Stepik fills targeted algorithm practice.

---

# Module 2 — Unix & Shell

| Source | Role | Rating | Use |
|---|---|---:|---|
| POSIX.1-2024 + current Linux man-pages | CURRENT REFERENCE | A | exact API semantics (`fork`, `exec`, `pipe`, `dup2`, `waitpid`, etc.) |
| Dive into Systems / selected OSTEP process material | PRIMARY theory | A | process/system-call mental model |
| Missing Semester current + Russian translation | COMPANION | A/B | shell/tooling fluency, not shell implementation spec |
| Kilo | GUIDED LAB | B | raw terminal/input subset only |
| Brennan — Write a Shell in C | PROJECT REFERENCE | H/B | minimal shell walkthrough; course extends/clarifies parser, pipes, redirection |

**Rule:** when tutorial code and current man/POSIX behavior differ, current API docs win.

---

# Module 3 — Computer Architecture

| Source | Role | Rating | Use |
|---|---|---:|---|
| Nand2Tetris Part I | PRIMARY | A | gates → ALU → memory → CPU → machine language → assembler |
| Dive into Systems architecture/assembly chapters | REFERENCE | A | bridge from teaching machine to real C/x86-64 systems |
| LC-3 / CHIP-8 tutorial selected by instructor | PROJECT REFERENCE | B | VM/emulator integration project |

**Rule:** Nand2Tetris is project-backed theory; do not replace it with passive architecture videos.

---

# Module 4 — Virtual Memory & Performance

| Source | Role | Rating | Use |
|---|---|---:|---|
| Dive into Systems memory hierarchy/performance | PRIMARY | A | cache/locality/performance model |
| OSTEP selected VM chapters | PRIMARY COMPANION | A | paging, address translation, TLB, VM model |
| POSIX/Linux `mmap`/`munmap` docs | CURRENT REFERENCE | A | actual mapping API |
| Memory Allocators 101 | HISTORICAL REFERENCE | H | allocator metadata/free-list ideas; **not** `sbrk()` as modern backend |

---

# Module 5 — Networking & Concurrency

| Source | Role | Rating | Use |
|---|---|---:|---|
| Stepik — Основы компьютерных сетей | PRIMARY theory | B/A for teaching role | Russian network theory + labs |
| Beej's Guide to Network Programming | PRIMARY programming | A/B | socket code and API-oriented explanation |
| current man/POSIX socket docs | CURRENT REFERENCE | A | exact API/error behavior |
| Dive into Systems / OSTEP concurrency | PRIMARY concurrency | A | threads, races, mutexes, condition variables |
| Wireshark | GUIDED LAB tool | A | inspect actual network traffic |

**Rule:** Stepik explains packets/routing/TCP; Beej is opened when writing socket code.

---

# Module 6 — OS & Isolation

| Source | Role | Rating | Use |
|---|---|---:|---|
| OSTEP | PRIMARY | A | scheduling, VM, concurrency, IPC concepts |
| Linux kernel docs + current man-pages | CURRENT REFERENCE | A | namespaces, `/proc`, cgroup v2, capabilities/API details |
| Stepik Operating Systems | COMPANION | B/H | Russian explanations for stable concepts; older course |
| Linux Container in 500 Lines of Code | HISTORICAL REFERENCE | H | conceptual inspiration only; old kernel/cgroup assumptions |

---

# Module 7 — Filesystems & Database Internals

| Source | Role | Rating | Use |
|---|---|---:|---|
| OSTEP Persistence/filesystem chapters | PRIMARY FS theory | A | filesystem/persistence mental model |
| official libfuse 3 docs/examples | CURRENT REFERENCE + GUIDED LAB | A | modern FUSE API (`hello`, `passthrough`) |
| cstack — Let's Build a Simple Database | PRIMARY PROJECT REFERENCE | B | REPL → pages → B-tree implementation sequence |
| SQLite official architecture/docs | CURRENT REFERENCE | A | deeper reality check / terminology |
| Russian DB course | COMPANION | B/H | production/database-engineering context, not low-level DB replacement |

**Rule:** cstack teaches page/B-tree implementation. It does not magically cover complete WAL/transaction recovery; those are separate conceptual outcomes.

---

# Module 8 — Binaries / Debugging / Security

| Source | Role | Rating | Use |
|---|---|---:|---|
| Linux man-pages (`ptrace`, `waitpid`, signals, `/proc`) | PRIMARY API | A | debugger process-control semantics |
| `readelf`/`objdump`/ELF docs | CURRENT REFERENCE | A | binary structure/tool behavior |
| Sy Brand — Writing a Linux Debugger | CONCEPT / HISTORICAL PROJECT REFERENCE | H/B | excellent debugger explanation; core course does **not** copy its C++/libelfin implementation |
| Dive into Systems/x86-64 material | REFERENCE | A | architecture refresh |

---

# Module 9 — Systems Integration / Architecture

| Source | Role | Rating | Use |
|---|---|---:|---|
| course capstone spec | PRIMARY | — | requirements, implementation, review |
| Google SRE book/workbook selected chapters | PRIMARY COMPANION | A | latency/traffic/errors/saturation, SLI/SLO/operability reasoning |
| AWS Well-Architected selected questions | REVIEW CHECKLIST | A | architecture trade-off prompts; **not** an AWS product course |

**Rule:** architecture is judged against measured requirements/failures, not diagram complexity.

---

# Mobile-first priority

When only a phone is available, prefer in this order:

1. assigned Russian/translated video or Stepik block;
2. exact HTML section from Dive/Beej/current docs;
3. short recall/scenario questions;
4. tiny Termux experiment only when it genuinely helps.

Do not try to implement major milestones on the phone.

---

# Offline policy

Prefer downloadable video/subtitles or downloadable/single-page HTML where available.

Before a commute-heavy week, the instructor should identify the exact sections to cache/download. "Download the whole course" is not required.

---

# Source replacement rule

Replace a source when:

- the assigned section is inaccessible;
- API/tooling is outdated for the course environment;
- mobile usability is poor and an equivalent source exists;
- the source adds cognitive load without improving the target outcome.

Record meaningful replacements in `SYSTEMS_ENGINEERING_PROGRESS.md`.