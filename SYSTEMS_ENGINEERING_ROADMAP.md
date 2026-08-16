# Systems Engineering Roadmap

Краткая карта. **Исполняемый курс находится в [`course/README.md`](course/README.md).**

## Цель

Вырастить не «человека, знающего синтаксис C», а инженера, который способен связать:

```text
source
→ data/memory
→ algorithms/invariants
→ ownership
→ process/OS
→ CPU/ABI
→ virtual memory/cache
→ network/concurrency
→ storage/database
→ binary/debugger/security
→ measurable architecture decisions
```

Темп: **6–8 часов в неделю**.

## Core path

1. C foundations — из текста в программу, значения, функции, arrays/text, records, separate build.
2. C memory + core DS&A — addresses/pointers/lifetime/allocation/UB, Vector, complexity/invariants, trees/heaps/hashing.
3. Rust bridge — compiler-checked ownership/borrowing and explicit unsafe/FFI boundary.
4. Testing engineering — oracles, invariants, negative/property/fuzzing intuition.
5. Unix process model + shell.
6. Computer architecture + Tiny16.
7. Virtual memory, cache locality, performance, allocator.
8. Networking + concurrency + backpressure.
9. OS scheduling/resources/isolation.
10. Filesystems, durability, database storage/indexes.
11. ELF/debugging/security mitigations.
12. Single-node systems integration/capstone.

## Core projects

- behavior-first fixed-size record store;
- Vector in C;
- Hash Table in C;
- Rust MiniKV bridge;
- Unix Shell;
- Tiny16 assembler + emulator;
- Arena Allocator;
- Concurrent KV Server;
- Modern Linux Isolation Lab;
- SimpleDB;
- `minidbg-c`;
- Persistent KV Service capstone.

## Optional, not gates

Курс сознательно не задерживает systems path отдельными большими блоками DP, KMP/Rabin–Karp, Trie, P/NP, FUSE implementation или distributed consensus. Они остаются полезными optional/advanced темами и изучаются, когда появляется соответствующая задача.

## Advanced branches after core

- Security / Reverse Engineering / Binary Exploitation labs;
- Distributed Systems;
- Kernel / OS internals;
- Rust systems deeper;
- Compilers / runtimes;
- Performance Engineering;
- Embedded / Hardware.

## Source policy

Mandatory theory self-contained. External docs/books/tutorials — reference/deep dive, not prerequisites.

## Progress

[`SYSTEMS_ENGINEERING_PROGRESS.md`](SYSTEMS_ENGINEERING_PROGRESS.md)