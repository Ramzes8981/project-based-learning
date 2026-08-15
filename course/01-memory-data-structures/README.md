# Module 1 — Memory, Pointers, and Data Structures

**Status:** CORE  
**Estimated effort:** 55–70 hours (~8–10 weeks)  
**Core milestone:** `MiniKV → Hash Table in C`  
**Mini-milestone:** Dynamic Array / Vector in C

## Prerequisites

From Module 0:

- basic C syntax is usable without constant translation from Python;
- arrays, C strings and structs are familiar;
- `MiniKV v0` works with fixed-capacity linear lookup;
- simple tests exist.

No prior pointer or manual-memory knowledge is assumed.

## Sources

- **PRIMARY:** Dive into Systems — selected C/memory/debugging chapters: https://diveintosystems.org/
- **COMPANION:** current CS50 Memory and Data Structures material.
- **EXERCISES:** selected Stepik C + CSC/Stepik Algorithms & Data Structures.
- **PROJECT REFERENCE:** James Routley, *Write a hash table in C*: https://github.com/jamesroutley/write-a-hash-table

The project reference is not copied line-by-line. The course starts with a simpler design and uses the tutorial later for comparison.

## Outcomes

By the end of the module the learner can:

- trace pointer relationships and object lifetimes;
- distinguish stack and heap storage;
- define ownership rules in C;
- allocate/reallocate/free memory safely;
- use `const`, `size_t`, `<stdint.h>`, `bool`, enums and bit operations where appropriate;
- diagnose memory errors with warnings, sanitizers and GDB;
- implement dynamic arrays and basic linked structures;
- reason about common operation costs with Big-O/Θ;
- implement a hash table with collision handling and resizing.

---

# Unit 1.1 — Addresses and pointers

### Learn

- address and pointer intuition;
- pointer types;
- `&`, `*`, dereference;
- pointer parameters;
- `NULL`;
- practical `const`.

### Exercise

Draw several value/address/pointer diagrams, predict outcomes, then verify them in C.

### Project slice

Make MiniKV operations work through an explicit store pointer. For each pointer answer: what does it point to, who created that object, and how long does it live?

### What can go wrong?

- dereferencing `NULL`;
- retaining a pointer to an object that no longer exists;
- confusing the pointer value with the pointed value.

---

# Unit 1.2 — Representation, arrays and pointers

### Learn

- relationship **and difference** between arrays and pointers;
- pointer arithmetic;
- pointer-to-struct syntax;
- strings through pointers;
- `size_t`;
- fixed-width integers from `<stdint.h>`;
- `bool`;
- basic bitwise operations and masks.

Bitwise operations are deliberately taught here because terminal flags, binary formats, networking and architecture use them later.

### Exercises

- traverse one array by index and by pointer;
- inspect bytes of an integer;
- manipulate a few bit flags;
- explain when pointer arithmetic is valid.

### Project slice

Refine MiniKV representation and public API; use explicit lengths where raw arrays require them.

---

# Unit 1.3 — Lifetime and ownership

### Learn

- automatic/local lifetime;
- conceptual stack frames;
- returning pointers safely vs unsafely;
- dangling pointers;
- owned vs borrowed pointer as a **course convention**.

### Exercise

Given several snippets, identify owner, lifetime, invalid-access point and required cleanup.

### Project slice

Write an ownership contract for table, entry storage, keys, values and lookup results **before** adding heap allocation.

---

# Unit 1.4 — Dynamic memory

### Learn

- `malloc`, `calloc`, `realloc`, `free`;
- allocation failure;
- safe `realloc` patterns;
- cleanup paths;
- `errno` only where APIs actually define it.

### Exercise

Allocate/free arrays and structs, grow one allocation and deliberately create/fix a leak.

### Tooling

Introduce AddressSanitizer, UBSan and GDB basics.

### Project slice

Move MiniKV storage to heap-owned memory and implement deterministic cleanup.

---

# Unit 1.5 — Memory failures and undefined behavior

### Learn

- leak;
- uninitialized memory;
- out-of-bounds access;
- use-after-free;
- double free;
- buffer overflow;
- undefined behavior as a model, not a memorization list.

### Practice

Diagnose seeded bugs using compiler warnings → sanitizer output → debugger.

### Rubric

The learner must be able to identify the defect class and the evidence that led to the diagnosis, not merely paste a fix.

---

# Mini-milestone — Dynamic Array / Vector

Build:

- create/destroy;
- get/set;
- push;
- capacity growth.

### CS concepts

- contiguous layout;
- `size` vs `capacity`;
- geometric growth;
- amortized cost.

### Required explanation

Why repeated doubling does not make every `push` expensive.

### Self-check

- no unexplained warnings;
- no sanitizer errors;
- boundary tests for empty/full/growth states;
- one transfer feature, e.g. `pop`, reserve-capacity or shrink policy.

---

# Unit 1.6 — Linked structures

### Learn

- singly linked list;
- node ownership;
- stack ADT;
- queue ADT;
- contiguous vs linked layout.

### Exercises

Implement small linked-list, stack and queue exercises. These are **not** three new portfolio projects.

### Industry case

Compare an array-backed queue and linked queue for throughput, memory overhead and locality; explain why asymptotic complexity alone does not decide the winner.

---

# Unit 1.7 — Algorithms foundation

This block is mandatory; algorithms are not left to "as needed".

### Learn

- operation-count intuition;
- `O`, `Ω`, `Θ`;
- linear/binary search;
- insertion/selection sort for reasoning;
- recursion basics;
- BST concept;
- heap/priority-queue concept;
- dynamic-programming idea: overlapping subproblems + memoization/tabulation (small checkpoint only).

### Math just in time

- growth functions;
- logarithms;
- simple sums;
- invariants;
- induction intuition.

### Situational questions

- Why can an `O(n)` loop beat an `O(log n)` operation for tiny inputs?
- What breaks binary search if the invariant is wrong?
- What information is lost if complexity is discussed without memory cost?

---

# Unit 1.8 — Hashing

### Learn

- hash function purpose;
- hash value vs bucket index;
- modulo;
- collisions;
- load factor;
- open addressing vs chaining;
- linear probing first;
- deletion/tombstone issue;
- expected vs worst-case lookup.

### Math just in time

- modular arithmetic basics;
- probability intuition for distribution/collisions.

### Project slice

Convert MiniKV into a real hash table:

1. hash key;
2. map to bucket;
3. resolve collisions with linear probing;
4. implement insert/update/get/delete;
5. track load factor.

Then read the Routley tutorial's double-hashing design and compare it with the course design.

---

# Unit 1.9 — Resize and rehash

### Learn

- resize threshold;
- why entries must be rehashed;
- amortized resize cost;
- growth/shrink trade-offs.

### Project slice

Add automatic growth, rehashing, resize-boundary tests and collision/probe statistics.

---

# Core milestone rubric — Hash Table in C

A pass requires:

### Correctness

- create/destroy;
- insert/update;
- lookup;
- delete;
- collisions;
- resize;
- boundary tests.

### Memory

- documented ownership;
- zero known sanitizer errors;
- cleanup works on normal and error paths.

### Algorithms

Explain expected/worst-case lookup, load factor, probe behavior and resize cost.

### Transfer

Implement one feature not copied from the reference, e.g. iterator, alternate probing strategy, configurable load factor or instrumentation.

### Engineering review

Explain API boundaries, state ownership, failure paths, memory overhead, performance bottlenecks and what changes at 10×/100× data size.

---

# Exit gate

Module 1 is complete only when:

- the hash table passes its agreed tests;
- the learner can debug a seeded memory bug;
- the learner can explain the data layout without opening the source;
- core concepts reach at least **Apply**, and hashing/ownership reach **Transfer**.