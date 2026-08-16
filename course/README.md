# Systems Engineering Course

Самодостаточный project-first курс по Computer Science и systems engineering для программиста с Python-бэкграундом.

**Основной язык:** русский.  
**Темп:** 6–8 часов в неделю.  
**Формат:** mobile-first теория + PC-first разработка.  
**Обязательная теория:** внутри этого репозитория.

## Начать отсюда

1. [`STRUCTURE.md`](STRUCTURE.md) — как устроены уроки и проекты.
2. [`AUTHORING_STANDARD.md`](AUTHORING_STANDARD.md) — стандарт качества материалов.
3. [`ASSESSMENT_AND_STUDY_RULES.md`](ASSESSMENT_AND_STUDY_RULES.md) — как проходить упражнения и milestone.
4. [`ENVIRONMENT.md`](ENVIRONMENT.md) — рабочая Linux-среда.
5. [`00-c-fast-start/README.md`](00-c-fast-start/README.md) — первый модуль.

## Модель обучения

```text
self-contained theory
↓
causal/situational questions
↓
small focused exercise
↓
active project slice when concept is ready
↓
tests / debugging / engineering review
↓
next cycle
```

Внешняя книга/курс никогда не являются prerequisite следующего обязательного шага. Они перечисляются как optional deep dive/reference.

## Core path

```text
0.  C Fast Start
    ↓
1.  Memory, Pointers, Algorithms & Data Structures
    ↓
1B. Rust Systems Bridge
    ↓
1C. Testing Engineering
    ↓
2.  Unix, Processes & Shell
    ↓
3.  Computer Architecture & Machine Code
    ↓
4.  Virtual Memory, Performance & Allocators
    ↓
5.  Networking & Concurrency
    ↓
6.  Operating Systems & Isolation
    ↓
7.  Filesystems & Database Internals
    ↓
8.  Binaries, Debugging & Security
    ↓
9.  Systems Integration & Architecture
```

## Milestones

```text
MiniKV v0
→ Vector + Hash Table C
→ Rust MiniKV
→ Unix Shell
→ Tiny16 Assembler/Emulator
→ Arena Allocator
→ Concurrent KV Server
→ Linux Isolation Lab
→ SimpleDB
→ minidbg-c
→ Persistent KV Service capstone
```

Код milestone пишет ученик. Курс предоставляет SPEC/acceptance/scenarios/hints и инфраструктуру (fixtures, controlled targets, client/load/test tools), только когда она не раскрывает проверяемую project logic.

## Self-contained policy

- обязательная теория — в lesson `.md`;
- official documentation — reference для platform/version detail, а не teaching dependency;
- external books/courses — [`OPTIONAL_READING.md`](OPTIONAL_READING.md);
- learner path валидируется `scripts/course_audit.py` в CI.
