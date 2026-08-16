# Структура курса и dependency chain

Этот документ отвечает на один вопрос: **почему следующая тема появляется именно сейчас?**

## Входные знания

Нужно только:

- уметь написать небольшой Python-скрипт;
- понимать переменную, `if`, цикл и функцию на бытовом уровне;
- уметь запустить команду в терминале после инструкции;
- базовый SQL полезен, но не является prerequisite ранних модулей.

Не предполагаются: C/Rust, pointers, memory model, compiler internals, OS, networking, assembly или algorithms course.

## Главная цепочка

```text
C source cannot run by itself
→ compiler
→ values/control/functions
→ contiguous data + bounds
→ C text representation
→ records + multiple files
→ separate compilation creates unresolved names
→ linker

we need to refer to existing data
→ address
→ pointer
→ bounds and one-past
→ lifetime
→ dynamic allocation
→ ownership convention
→ UB/debugging
→ growing collection

operations get expensive as data grows
→ cost model / Big-O
→ invariant
→ search/sort/tree/heap
→ key lookup problem
→ hashing/collision/rehash

manual ownership contracts are hard to maintain
→ Rust ownership/borrowing/lifetimes
→ safe collections/errors
→ unsafe/FFI boundary

correct code can still regress
→ oracle/invariant/property/negative tests

program needs OS-managed resources
→ process + syscall mental model
→ file descriptor
→ reliable I/O
→ terminal
→ fork/exec/wait
→ redirection/pipes/signals

what executes those instructions?
→ bits/integers/floats
→ logic
→ CPU state/registers/memory
→ ISA/machine code
→ fetch/decode/execute
→ ABI

same pointer value does not mean same physical RAM
→ virtual address space
→ pages
→ page tables/TLB/faults
→ locality/cache
→ measurement
→ allocator

bytes must reach another program
→ link/IP/routing
→ UDP/TCP guarantees
→ socket
→ TCP is a byte stream
→ framing

one handler is not enough for many clients
→ thread
→ shared mutable state
→ race
→ mutex
→ waiting condition
→ bounded queue
→ backpressure
→ event loop/poll

many runnable programs compete for finite machine resources
→ scheduling/memory pressure
→ IPC
→ process inspection
→ namespaces/cgroups/capabilities

write() returned, but will bytes survive a crash?
→ filesystem object/inode
→ page cache
→ durability/fsync/rename
→ stable binary format
→ pager/records
→ disk index/B-tree
→ buffering/query cost
→ transactions/WAL/recovery concepts

source is gone but executable remains
→ ELF
→ loader
→ PIE/ASLR
→ ptrace
→ registers/memory
→ breakpoints
→ stepping/unwinding
→ mitigations

all mechanisms now interact in one service
→ measurable requirements
→ protocol retry semantics
→ queueing/capacity
→ overload
→ durability/recovery
→ observability/SLI/SLO
→ ADR/security review
→ evidence-based scaling question
```

## Core vs optional

Optional — это не «плохая» тема. Это тема, отсутствие которой **не ломает dependency chain следующего core project**.

### Core algorithms

- complexity intuition;
- invariants;
- binary search;
- sorting trade-offs;
- recursion as a control/data-structure tool;
- trees/traversal intuition;
- binary heap/priority queue;
- hashing/collisions/rehash;
- graphs/BFS/DFS/Dijkstra intuition when routing/dependency problems need it.

### Optional algorithms

- standalone dynamic programming block;
- KMP/Rabin–Karp implementation detail;
- Trie implementation;
- standalone probability derivations for hashing.

### Optional systems depth

- FUSE implementation lab;
- DWARF parser internals;
- P/NP theory;
- distributed consensus/replication implementation.

## Project rule

A project specification may be visible early, but it must be layered:

1. **Behavior now** — only observable behavior in vocabulary already known.
2. **Constraints unlocked later** — technical requirements grouped by prerequisite lesson.
3. **Final acceptance** — full contract after all required lessons.

Never require `capacity`, `ownership`, `hashing`, `fd`, `framing`, `backpressure`, `WAL` or another implementation term before its lesson created the need for it.

## Cumulative checkpoints

After each large boundary ask for a vertical explanation, not a definition dump:

- after C memory: “why can a pointer become invalid?”;
- after Unix: “what exactly survives `fork`, and what does `exec` replace?”;
- after architecture/VM: “what chain turns a load instruction into data?”;
- after networking/concurrency: “where can one request wait?”;
- after storage: “what does success mean under a crash?”;
- at capstone: requirement → mechanism → failure → evidence → trade-off.