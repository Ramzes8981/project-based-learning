# Module 0 — C Fast Start

**Status:** CORE  
**Estimated effort:** 10–15 hours (~2 weeks at the target pace)  
**Active project:** `MiniKV v0` — fixed-capacity key/value store that will later evolve into the Hash Table milestone

## Why this module exists

The learner already knows general programming through Python. This is **not** a beginner-programming semester.

The goal is to become syntactically functional in C fast enough to start a real project, while noticing the places where C differs fundamentally from Python.

---

# Prerequisites

Required:

- variables / conditions / loops / functions in any language;
- basic ability to run a program.

Not required:

- C;
- pointers;
- algorithms coursework;
- Linux internals.

Environment prerequisite:

- complete the minimum setup from [`../ENVIRONMENT.md`](../ENVIRONMENT.md);
- be able to open a Linux shell and run a compiler.

---

# Sources

## PRIMARY — Russian CS50 explanation layer

Use the Russian CS50 translation selectively for the C introduction.

Role: `PRIMARY` for explanation/video.

Do **not** complete old CS50 as a standalone course.

## CURRENT REFERENCE — CS50x 2026

Use current CS50 Week 1 and selected Week 2 notes/shorts to verify terminology and modern course details:

- https://cs50.harvard.edu/x/weeks/1/
- https://cs50.harvard.edu/x/weeks/2/

Role: `REFERENCE`.

## EXERCISES — Stepik C

Use only assigned tasks from:

- https://stepik.org/course/3078/

Role: `EXERCISES`.

Do not chase course-completion percentage.

---

# Outcomes

By the end of the module, the learner can:

- compile and run C from the terminal;
- read basic compiler diagnostics;
- use primitive types deliberately;
- write functions and control flow without translating Python line-by-line;
- use fixed arrays and basic C strings;
- define and use a `struct`;
- split a tiny program into source/header files when useful;
- use Git for small incremental commits;
- explain at a basic level why C values/arrays/strings are represented differently from Python objects.

---

# Learning sequence

## Unit 0.1 — Source → executable

### Learn

- source code;
- compiler;
- executable;
- `main`;
- exit status;
- `printf`;
- compiler warnings.

### Exercise

Create, compile, run, modify, and recompile a tiny C program.

Trigger one harmless compiler diagnostic and explain it.

### Project slice

Create the `MiniKV` project directory and README.

Write the project contract in plain language:

- store key/value pairs;
- retrieve a value by key;
- fixed maximum capacity for now;
- no hashing yet;
- no dynamic memory yet.

No implementation complexity is required yet.

---

## Unit 0.2 — Types and values

### Learn

- `char`, integer types, floating-point types;
- `sizeof`;
- signed vs unsigned intuition;
- integer overflow as a concept;
- variable scope.

Do not memorize every platform-specific type size.

### Exercise

Inspect type sizes and predict several simple expressions before running them.

Compare the behavior conceptually with Python integers.

### Project slice

Choose simple fixed-size types for the first `MiniKV` representation and document why.

---

## Unit 0.3 — Control flow and functions (fast pass)

### Learn

- `if` / `switch`;
- loops;
- functions;
- declarations vs definitions at a basic level;
- return codes for simple errors.

Because these programming ideas are already known, spend time on **C syntax and behavior**, not introductory programming exercises.

### Exercise

Write 2–3 small functions with explicit input validation / return behavior.

### Project slice

Create operations conceptually equivalent to:

- initialize store;
- add/update entry;
- find entry.

Implementation can still be incomplete.

---

## Unit 0.4 — Arrays and strings

### Learn

- fixed arrays;
- array length is not stored automatically with a raw C array;
- `char` arrays;
- null-terminated strings;
- bounds responsibility;
- basic functions from `<string.h>` as reference, not magic.

### CS checkpoint — linear search

Learn:

- linear search;
- operation-count intuition;
- first informal `O(n)` idea.

No formal asymptotic-analysis lecture yet.

### Exercises

- search a fixed integer array;
- search a fixed array of records;
- perform one small string manipulation safely.

### Project slice — MiniKV v0

Implement a deliberately simple version:

```text
fixed array of entries
        ↓
linear scan by key
        ↓
return matching value / not found
```

This is **not yet a hash table**.

The slowness of linear lookup is intentional; it creates the problem that Module 1 will solve.

---

## Unit 0.5 — Structs and simple modules

### Learn

- `struct`;
- `enum`;
- fields;
- `.c` / `.h` at a basic level;
- include guards;
- compile/link concept only as far as needed for two files.

### Exercise

Represent one real record using a struct and split a tiny example into interface/implementation.

### Project slice

Replace temporary MiniKV representation with explicit concepts such as:

```text
Entry
Store
```

Separate public API from implementation if the code is large enough to justify it.

Add simple `assert`-based tests for:

- empty store;
- insert/get;
- missing key;
- full capacity.

---

# What is intentionally NOT taught yet

Do not front-load:

- pointers in depth;
- `malloc` / `free`;
- advanced Makefiles;
- GDB internals;
- complex algorithms;
- formal discrete mathematics;
- assembly.

Those appear when the project needs them.

---

# Exit gate

Before Module 1, the learner must be able to:

## Explain

- source vs executable;
- primitive C value vs Python object at a high level;
- why a C array needs explicit bounds knowledge;
- why a C string needs a terminator;
- why MiniKV lookup is linear.

## Build

`MiniKV v0` supports fixed-capacity key/value storage and linear lookup.

## Debug

Fix at least one compiler warning or simple logic bug independently.

## Transfer

Add one tiny feature not shown in the source material, for example:

- update an existing key;
- delete by shifting entries;
- return explicit status codes.

Do not move on if basic C syntax still consumes most of the learner's attention.