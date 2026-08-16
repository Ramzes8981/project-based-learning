# Systems Engineering Progress

Небольшой evidence tracker. Детальные чек-листы находятся в уроках и project acceptance files; этот файл не должен дублировать syllabus.

## Current status

- **Current module:** Module 0 — C Fast Start
- **Current lesson:** 0.1 — Source → build → run
- **Current project:** MiniKV v0
- **Weekly capacity:** 6–8 hours
- **Canonical environment:** WSL2/Ubuntu for systems labs

## Core module status

| Module | Status | Core artifact |
|---|---|---|
| 0 — C Fast Start | ⬜ Not started | MiniKV v0 |
| 1 — Memory / Algorithms / Data Structures | ⬜ | Vector + Hash Table |
| 1B — Rust Systems Bridge | ⬜ | Rust MiniKV |
| 1C — Testing Engineering | ⬜ | Test strategy upgrade |
| 2 — Unix & Shell | ⬜ | Unix Shell |
| 3 — Computer Architecture | ⬜ | Tiny16 assembler/emulator |
| 4 — VM & Performance | ⬜ | Arena Allocator |
| 5 — Networking & Concurrency | ⬜ | Concurrent KV Server |
| 6 — OS & Isolation | ⬜ | Isolation Lab |
| 7 — Filesystems & Databases | ⬜ | SimpleDB |
| 8 — Binaries & Debugging | ⬜ | minidbg-c |
| 9 — Integration & Architecture | ⬜ | Persistent KV Service |

Legend: `⬜` not started · `🟨` in progress · `✅` passed · `🔁` revisit.

## Evidence for current learning cycle

Fill only current/just-completed lesson.

```text
Date:
Module / lesson:
Status: Seen / Explain / Apply / Transfer

Theory:
- what model I can explain now

Exercise:
- file/result
- failed edge cases and fixes

Project slice:
- what changed
- commit/reference

Debug story:
- symptom
- hypothesis
- evidence/tool
- root cause
- regression test

Open gaps:
- ...

Next:
- ...
```

## Milestone gate template

```text
Milestone:
Date passed:

Explain:
Build:
Transfer feature:
Debug evidence:
Tests/metrics:
Engineering review:
Known limitations:
```

## Cumulative checkpoints

After approximately every two large modules record one short cross-layer exercise, for example:

- explain old project without source;
- modify an earlier feature;
- diagnose a seeded bug;
- connect current layer to earlier memory/OS model.

## Roadmap change log

| Date | Change | Reason |
|---|---|---|
| 2026-08-15 | Initial systems roadmap | Create finite low-level/CS path |
| 2026-08-15 | Project-first redesign | Interleave theory, exercises and milestone slices |
| 2026-08-15 | Professional prerequisite audit | Remove hidden prerequisites/outdated project assumptions |
| 2026-08-16 | Self-contained course v3 | Move required theory into repo; add Rust Bridge and course-owned project specs |
| 2026-08-16 | Course v3.1 quality pass | Deepen CS core, add Testing Engineering, executable fixtures/tools, internal FUSE/FFI references and CI validation |
