# Russian-language resources for the Systems Engineering Roadmap

> Companion to [`SYSTEMS_ENGINEERING_ROADMAP.md`](SYSTEMS_ENGINEERING_ROADMAP.md).
>
> Purpose: provide strong Russian-language alternatives for mobile study without weakening the technical depth of the roadmap.
>
> **Rule:** prefer the best source, not Russian at any cost. A Russian resource may replace an English primary source only when it covers the required concepts at comparable depth. Otherwise it is a companion/explanation layer and the English source remains authoritative for current APIs, terminology, exercises, and advanced details.

---

# How to choose between Russian and English

Use this order:

1. **Russian primary** — when the Russian course is strong, free, and covers the required block well.
2. **Russian companion + English primary** — when the Russian material is excellent for explanation but older or less complete.
3. **English primary with subtitles + Russian discussion** — when no equivalent Russian resource exists.
4. **English documentation/man pages/RFCs** — always acceptable and often unavoidable in systems work.

Recommended study pattern in the metro:

```text
Russian lecture / translated lecture
        ↓
short notes / quiz
        ↓
English reference when terminology or details matter
        ↓
PC project slice
        ↓
review and explanation in Russian
```

---

# Phase 0 — Tooling / shell / Git / debugging

## Primary English

- MIT Missing Semester (latest 2026): https://missing.csail.mit.edu/2026/

## Russian alternative

### Missing Semester — Russian community translation

The official MIT course page lists a **Russian** community translation in its Translations section:

- https://missing.csail.mit.edu/

Use the translation for the lecture notes where convenient, but prefer the current 2026 English materials for newer topics because translations can lag behind the latest edition.

### Recommended role

**Russian companion, English current primary.**

Good mobile flow:

- Russian translated notes for shell concepts
- 2026 lecture/video with subtitles for current tooling
- commands practiced in Termux/PC

---

# Phases 1–2 — C fundamentals, pointers, memory, data structures

## Russian course 1 — Harvard CS50 translated by Vert Dider / JavaRush

- https://javarush.com/quests/lectures/questharvardcs50.level00.lecture00
- landing page: https://landing.javarush.com/ru/cs50/

This is a full Russian localization of **CS50 2015–2016**, made by Vert Dider with JavaRush. It includes translated video lectures, text material, and practical-task explanations.

### Strengths

- high-quality Russian voice translation
- very phone-friendly lecture format
- covers compilation, C, debugging, memory, pointers, linked structures, hash tables, algorithms, and security concepts
- free to access

### Important limitation

It is an **old CS50 edition (2015–2016)**. The fundamental C/CS material remains useful, but:

- current CS50 structure and exercises have changed;
- tooling/library details can differ;
- use modern CS50 pages or current documentation when details conflict.

### Recommended role

**Russian primary for explanation/video + modern CS50 as current reference.**

Do not blindly complete the entire old CS50 course. Select lectures that map to our roadmap cycles.

---

## Russian course 2 — Stepik: Основы программирования на C. Задачи

- https://stepik.org/course/3078/

Free Russian practical C course with hundreds of exercises and automatic checking.

### Best use in our roadmap

**Exercise bank**, not the main systems curriculum.

Use selected tasks for:

- types and operators
- control flow
- functions
- arrays / strings
- basic algorithmic thinking
- compiler/run practice

Do not spend weeks completing every beginner exercise just for completion percentage. We already know general programming from Python.

### Recommended role

**Russian exercise source / mobile practice.**

---

## English material still retained

### Dive into Systems

- https://diveintosystems.org/

No Russian replacement currently promoted to primary status in this roadmap. Its main value is the vertical connection:

```text
C -> memory -> assembly -> architecture -> cache -> OS -> parallelism
```

Use it as the deeper systems source, with explanations/discussion in Russian.

### Beej's Guide to C

- https://beej.us/guide/bgc/

Keep as reference/alternate explanation, especially for precise C details.

---

# Algorithms and Data Structures CS thread

## Russian primary — Stepik / Computer Science Center

### Алгоритмы: теория и практика. Структуры данных

- https://stepik.org/course/1547/

Free course from Computer Science Center. Covers core data-structure reasoning and assumes basic programming plus logarithms/induction.

### Recommended role

**Strong Russian primary/companion** for the data-structures thread.

Use selected modules just-in-time alongside the C project:

- arrays / dynamic structures
- queues / stacks
- hashing
- trees/heaps where relevant

Do not detach it into a separate semester-long course.

## Deeper algorithms

The Stepik/CSC ecosystem also contains the Russian **Algorithms: Theory and Practice** series. Use it as a Russian companion before or alongside selected MIT 6.006 topics.

MIT 6.006 remains useful later for deeper analysis and university-level treatment:

- https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/

---

# Discrete Mathematics / Mathematical Reasoning

## Main source retained

MIT Mathematics for Computer Science:

- https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/

No single Russian replacement is made mandatory.

### Learning policy

Discrete math remains **just-in-time**:

- Big-O -> functions, logarithms, sums
- hashing -> modulo arithmetic, probability intuition
- correctness -> logic, invariants, induction
- graphs -> sets, relations, graph definitions

For Russian study, prefer targeted Russian explanations/courses for the exact needed concept rather than completing an unrelated full discrete-math syllabus.

---

# Computer Architecture

## English core retained

- Dive into Systems
- Nand2Tetris: https://www.nand2tetris.org/

These remain core because the project progression from gates to CPU/assembler is unusually strong.

## Russian companion strategy

Use Russian lecture material for difficult concepts when needed, but keep the Nand2Tetris projects themselves as the practical backbone.

Do not replace the project sequence with theory-only videos.

### Required architecture topics

- binary / hex
- integer representation
- logic gates
- ALU
- registers
- RAM
- CPU
- machine language
- assembly
- ABI/calling conventions
- cache hierarchy

---

# Operating Systems

## Russian course — Stepik: Операционные системы

- https://stepik.org/course/1780/

Free Russian course focused on OS kernel internals. It expects C/C++, pointers/address arithmetic, data structures, Git, and basic English documentation reading.

### Strengths

- memory management
- kernel-level concepts
- systems-oriented rather than user-level OS overview
- exercises and video

### Limitation

The course is older (last update listed as 2020), so use it for **stable concepts**, not as an authority for modern Linux-specific details.

### Recommended role

**Russian companion / selected primary for OS fundamentals**, paired with OSTEP.

## English deeper reference

OSTEP:

- https://pages.cs.wisc.edu/~remzi/OSTEP/

Use for coherent treatment of virtualization, concurrency, and persistence.

---

# Networking

## Russian primary — Stepik: Основы компьютерных сетей

- https://stepik.org/course/208904/

Free Russian course covering TCP/IP and practical networking concepts. Includes topics such as Ethernet, IP, TCP/IP, DHCP, VLAN, NAT, VPN and practical tasks in the Miminet web emulator.

### Recommended role

**Russian primary for networking theory** before/during the socket-programming phase.

It is particularly useful for mobile study because much of the conceptual work and quizzes can be done in a browser.

## English programming companion

Beej's Guide to Network Programming:

- https://beej.us/guide/bgnet/

Keep it because our roadmap requires **writing socket code in C**, not just understanding network administration.

## Practice

Always pair theory with:

- Wireshark
- socket client/server code
- simple protocol implementation
- concurrent server milestone

---

# Storage / Database Internals

## Russian companion — Stepik: Свободное погружение в СУБД

- https://stepik.org/course/70710/

Free Russian course for programmers who already know SQL and applications using relational databases. Covers schema quality, production failure cases, complex SQL, concurrent access, and relational/non-relational features.

### Recommended role

**Architecture/database companion**, especially for practical database engineering and concurrency thinking.

### Important limitation

It does **not replace** our low-level database-internals milestone. Our roadmap still needs explicit work with:

- pages
- records
- serialization
- B-trees
- buffer/cache behavior
- persistence
- WAL/recovery concepts

The project [Let's Build a Simple Database](https://cstack.github.io/db_tutorial/) remains the main hands-on internals milestone.

---

# Distributed Systems / Architecture — Advanced

## Russian option — Stepik: Сетевые и распределённые системы: немного о сложном и важном

- https://stepik.org/course/181658

Free Russian course about networks and distributed systems, with theory, experiments, tests, and over 16 hours of video listed.

### Recommended role

**Candidate Russian companion** when the advanced distributed-systems branch starts.

Do not promote it to primary until we inspect its syllabus against our required topics:

- replication
- consistency
- partitioning
- consensus
- failure detection
- retries/idempotency
- queues/streams
- distributed storage
- reliability/observability

---

# Security / Reverse Engineering

No Russian course is promoted as a core replacement yet.

Reason: this section will eventually depend heavily on current tools and primary documentation:

- GDB
- ELF/DWARF
- Ghidra
- Linux internals
- exploit mitigations
- architecture-specific behavior

Russian explanation material can be added topic-by-topic, but current English documentation remains important.

---

# Current recommended Russian/English balance

For the first half of the roadmap, a realistic study mix can now be approximately:

```text
Russian explanations / translated lectures / Stepik: 50–65%
English books / current docs / project tutorials:       35–50%
```

This ratio is not a target quota. It is a convenience outcome.

As the roadmap becomes more low-level and specialized, the English share will naturally rise because primary documentation, man pages, standards, GitHub projects, debugger/tool docs, and many systems tutorials are English-first.

---

# Mobile-first shortlist

If studying only from the phone in the metro, prefer:

1. **CS50 Russian (Vert Dider / JavaRush)** — video explanations
2. **Stepik C exercises** — interactive practice
3. **Stepik Algorithms / Data Structures** — video + interactive tasks
4. **Missing Semester Russian notes / current video with subtitles**
5. **Stepik Computer Networks** — browser-friendly theory/practice
6. **Beej HTML guides** — offline/single-page reference when English reading is comfortable

The PC session should then convert the learned material into the active milestone project.

---

# Maintenance rule

When a Russian resource is added to the roadmap, record:

- language
- role: `primary`, `companion`, `exercise bank`, or `reference`
- whether it is free
- how current it is
- mobile/offline suitability
- which exact roadmap cycles it supports

Do not add a Russian resource merely because it exists. It must reduce friction without reducing depth.