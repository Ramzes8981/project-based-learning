# Systems Engineering — учебный путь

Этот каталог — основной self-contained курс. Он рассчитан на человека, который уже писал небольшие Python-скрипты и знает базовый SQL, но ещё не изучал Computer Science и systems programming системно.

Темп: **6–8 часов в неделю**. Обязательная теория находится в репозитории; внешние ссылки — только дополнительное чтение или справка.

## Как устроено обучение

Каждый новый механизм появляется только после проблемы, которая делает его необходимым:

```text
проблема
↓
интуиция
↓
простая mental model
↓
официальный термин
↓
механика
↓
маленький пример
↓
самостоятельная практика
↓
causal questions
↓
применение в проекте, если оно естественно
```

Если термин нужен только в следующем модуле, текущий урок не должен требовать его знания.

## Как проходить один урок

1. С телефона прочитай теорию и ответь на causal questions без подсказок.
2. На ПК выполни маленькое упражнение.
3. Сначала предскажи результат, затем запускай код/инструмент.
4. Если есть solution-файл, открывай его **после** своей попытки.
5. Project slice делай только тогда, когда урок явно говорит, что для него уже есть prerequisites.
6. Перед переходом дальше пройди `Exit check`.

Статусы понимания: `Seen → Explain → Apply → Transfer`.

## Core path

### 0. [Как из текста на C получить работающую программу](<00 - C Fast Start/README.md>)

Плавный вход в C: значения, ветвления, функции, несколько значений подряд, текст в C, структуры и многофайловая программа. Линковщик появляется только тогда, когда возникает отдельная сборка нескольких файлов.

**Итог:** маленькая программа «имя → значение» с фиксированным числом записей, описанная сначала через поведение, а не через структуры данных.

### 1. [Как программа находит данные в памяти и безопасно управляет их временем жизни](<01 - Memory and Data Structures/README.md>)

Первая половина модуля — модель памяти C: адреса, указатели, границы, время жизни, динамическая память, ownership-by-convention, UB и диагностика. Затем — структуры данных и алгоритмические trade-offs, которые реально нужны systems engineer.

**Core проекты:** растущий Vector и Hash Table.  
**Optional advanced algorithms:** DP, KMP/Rabin–Karp, Trie и формальная probability-лекция вынесены из обязательного gate.

### 1B. [Как Rust заставляет явно описывать владение ресурсами](<01B - Rust Systems Bridge/README.md>)

Rust не повторяет C с новым синтаксисом. Он показывает, какие уже знакомые C-контракты компилятор способен проверять: ownership, borrowing, lifetime, typed errors и `unsafe` boundary.

### 1C. [Как проверять программы так, чтобы тесты ловили реальные поломки](<01C - Testing Engineering/README.md>)

Oracles, invariants, regression tests, negative tests, fuzzing intuition и testability. Unix-specific I/O testing появляется позже, после Unix API.

### 2. [Как ОС запускает программы и соединяет их в shell](<02 - Unix Shell/README.md>)

Сначала появляется модель запущенной программы и обращения к ОС; затем file descriptors, terminal, `fork/exec/wait`, redirection, pipes и signals.

**Проект:** Unix Shell.

### 3. [Как процессор превращает биты в выполнение инструкций](<03 - Computer Architecture/README.md>)

Представление чисел, Boolean logic, state, ISA, machine code, fetch/decode/execute, assembler и мост к x86-64 ABI.

**Проект:** Tiny16 assembler + emulator.

### 4. [Почему адрес программы не равен ячейке RAM и откуда берётся стоимость памяти](<04 - Virtual Memory, Performance and Allocators/README.md>)

Virtual address space, pages, page tables, TLB, faults, cache locality, measurement и allocator design. Allocator изучается двумя циклами: сначала выдача выровненных блоков, затем возврат/повторное использование.

**Проект:** Arena Allocator.

### 5. [Как байты доходят до другой программы и что ломается при параллельной обработке](<05 - Networking and Concurrency/README.md>)

IP/routing, UDP/TCP, socket API, главное свойство TCP stream, framing, threads, races, synchronization, bounded queues, backpressure и `poll`.

**Проект:** Concurrent KV Server.

### 6. [Как ОС делит процессор, память и ресурсы между программами](<06 - Operating Systems and Isolation/README.md>)

Scheduling, memory pressure, IPC, `/proc`, namespaces, cgroup v2 и capabilities. Базовые mutex/condvar не преподаются второй раз: здесь они используются для анализа системных последствий.

**Проект:** Modern Linux Isolation Lab.

### 7. [Как данные получают имя на диске, переживают сбой и превращаются в базу данных](<07 - Filesystems and Databases/README.md>)

Names/inodes, page cache, durability, binary formats, pager, records, B-tree family, buffering/query cost и transaction/WAL concepts.

**Проект:** SimpleDB.  
**Optional lab:** FUSE — после базовой модели файловой системы, а не как prerequisite для БД.

### 8. [Как запущенная программа выглядит изнутри debugger-а](<08 - Binaries, Debugging and Security/README.md>)

ELF, loader, PIE/ASLR, `ptrace`, registers/memory, software breakpoints, stepping, stack unwinding, DWARF boundary и memory-corruption mitigations.

**Проект:** `minidbg-c`.

### 9. [Как собрать один измеримый сервис и аргументировать архитектурные решения](<09 - Systems Integration and Architecture/README.md>)

Requirements, workload, retry/idempotency contracts, queueing, overload, durability, observability, SLI/SLO, ADR/security review и вопрос второго узла.

**Capstone:** Persistent KV Service.

## Что не является обязательным core

Темы остаются в репозитории, но не блокируют движение к systems/security engineering:

- dynamic programming как отдельный большой блок;
- KMP/Rabin–Karp и Trie;
- отдельная теория P/NP/NP-completeness;
- FUSE implementation lab;
- глубокий DWARF parser;
- distributed consensus/replication;
- production TLS/auth;
- kernel development, compilers и embedded — это следующие ветки.

## Навигация и качество

- [`STRUCTURE.md`](STRUCTURE.md) — dependency chain и curriculum boundaries.
- [`AUTHORING_STANDARD.md`](AUTHORING_STANDARD.md) — правила написания уроков.
- [`ASSESSMENT_AND_STUDY_RULES.md`](ASSESSMENT_AND_STUDY_RULES.md) — assessment/gates.
- [`ENVIRONMENT.md`](ENVIRONMENT.md) — среда.
- [`CONCEPT_DEPENDENCIES.json`](CONCEPT_DEPENDENCIES.json) — машинно проверяемая карта ключевых понятий.
- [`SOURCE_MATRIX.md`](SOURCE_MATRIX.md) — политика источников.
- [`OPTIONAL_READING.md`](OPTIONAL_READING.md) — необязательное чтение.

CI запускает `scripts/course_audit.py`: broken links, orphan solutions, duplicate lesson prefixes, project-doc completeness, placeholders/internal markers, navigation integrity и consistency concept manifest.
