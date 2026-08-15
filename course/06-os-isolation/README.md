# Module 6 — Operating Systems and Isolation

**Status:** CORE  
**Estimated effort:** 40–55 hours (~6–8 weeks)  
**Core milestone:** modern Linux isolation lab / mini-container

## Prerequisites

- processes, signals and file descriptors from Module 2;
- virtual-memory model from Module 4;
- threads/synchronization from Module 5;
- basic x86-64/CPU model from Module 3.

## Sources

- **PRIMARY:** OSTEP selected chapters on virtualization, scheduling, concurrency and I/O.
- **CURRENT LINUX REFERENCE:** Linux man-pages + kernel documentation for namespaces/cgroup v2.
- **RUSSIAN COMPANION:** selected Stepik Operating Systems sections.
- **HISTORICAL REFERENCE ONLY:** the repository's *Linux Container in 500 Lines of Code*.

The historical container tutorial is not the course implementation spec. Modern Linux systems commonly use cgroup v2 and current namespace behavior; old kernel-version checks/cgroup-v1 instructions must not be copied blindly.

---

# Outcomes

The learner can:

- explain process/thread scheduling at a working level;
- explain virtual-memory isolation and page faults;
- reason about synchronization and deadlock;
- describe common IPC mechanisms and their trade-offs;
- inspect process/kernel state through `/proc` and tools;
- explain what Linux namespaces isolate and what they do **not** isolate;
- explain cgroup resource control conceptually and inspect cgroup v2;
- build a limited process-isolation lab without confusing it with a production container runtime.

---

# Unit 6.1 — CPU virtualization and scheduling

### Learn

- process abstraction;
- runnable/running/blocked states;
- context switch;
- timer/preemption intuition;
- scheduling policy goals;
- turnaround time vs response time;
- fairness vs throughput trade-off.

### Metrics

For simple scheduling exercises, use:

- turnaround = completion time − arrival time;
- response time = first scheduled time − arrival time;
- waiting time intuition.

### Situational task

Compare an interactive workload and a long CPU-bound batch job. Explain why one scheduling policy cannot optimize every metric simultaneously.

---

# Unit 6.2 — Virtual memory deeper

### Learn

- per-process virtual address space;
- page table;
- TLB;
- page fault;
- demand paging;
- copy-on-write connection to `fork()`;
- anonymous/file mappings;
- swapping concept, without assuming every modern system uses it identically.

### Lab

Use `/proc/<pid>/maps`, `pmap` where available, and a small mapping program to connect abstractions with a live process.

### What goes wrong if…?

- a process accesses an unmapped page?
- writable memory is shared across processes without synchronization/protocol?
- page working set exceeds available physical memory?

---

# Unit 6.3 — Synchronization deeper

### Learn

- mutex;
- condition variable;
- semaphore;
- atomicity intuition;
- lock ordering;
- deadlock conditions;
- starvation;
- producer/consumer;
- spurious wake-up concept: wait in a predicate loop.

### Lab

Implement a bounded producer/consumer queue with mutex + condition variables.

### Required debugging scenario

Seed one lock-order deadlock and diagnose it from thread states/backtraces.

---

# Unit 6.4 — IPC

### Learn

Compare:

- pipe;
- socket/socketpair;
- shared memory;
- signal;
- file-backed coordination at a conceptual level.

### Industry case

Two components exchange large payloads at high frequency. Explain why "IPC" is not one performance class: copying, serialization, synchronization and failure isolation all matter.

---

# Unit 6.5 — Linux process inspection

### Learn / use

- `/proc/<pid>/status`;
- `/proc/<pid>/fd`;
- `/proc/<pid>/maps`;
- `/proc/<pid>/ns`;
- `ps`;
- `strace`;
- `top`/`htop` if available.

The goal is to answer concrete questions about a running process, not memorize `/proc` files.

---

# Unit 6.6 — Namespaces

### Learn

Linux namespaces isolate views of global resources.

Study at least:

- UTS;
- PID;
- mount;
- network conceptually;
- user namespace;
- cgroup namespace conceptually.

Use current `namespaces(7)` / specific namespace man pages.

### Guided lab

Start with `unshare`/`nsenter` commands before writing C:

- create a new UTS namespace;
- change hostname inside it;
- inspect `/proc/.../ns` handles;
- explore PID/mount namespace behavior where the environment permits.

### Security nuance

Namespace isolation is not a complete security boundary by itself. Capabilities, filesystem setup, syscall surface, cgroups, LSMs/seccomp and kernel security still matter.

---

# Unit 6.7 — cgroup v2

### Learn

- process hierarchy;
- controllers;
- resource limits/accounting;
- cgroup v2 unified hierarchy concept;
- delegation/privilege caveats.

### Lab

At minimum inspect the active cgroup v2 hierarchy and current process membership.

Creating/modifying cgroups is environment-dependent; failure due to missing delegation is not a learning failure.

### Important course rule

Do not teach cgroup v1 mechanics as the normal modern design merely because an old tutorial uses them.

---

# Core milestone — Mini-container / isolation lab

This is deliberately **not** "build Docker".

## Required scope

Create a small launcher/lab that demonstrates several isolation mechanisms with current Linux APIs/tools.

Required evidence should include:

1. child process launch;
2. at least UTS + PID or mount namespace isolation where environment allows;
3. controlled root/filesystem view as an optional or environment-dependent step;
4. inspection of namespace IDs from `/proc`;
5. cgroup v2 observation and, if safely delegated, one resource limit experiment;
6. cleanup and limitations documented.

A course-owned C wrapper using `clone()`/`unshare()` may be built after command-line experiments make the model clear.

## Not required for core

- secure image distribution;
- overlay filesystem stack;
- full networking stack;
- production-grade seccomp profile;
- OCI compatibility;
- daemon/runtime management.

These are Stretch/advanced topics.

---

# Rubric

### Understanding

Explain the difference between:

- namespace isolation;
- cgroup resource control;
- filesystem root/view;
- privilege/capability control.

### Correctness

The lab can demonstrate its promised isolation properties and restore/clean resources it creates.

### Safety/limitations

README explicitly states that the result is an educational isolation tool, **not a secure production container runtime**.

### Transfer

Add one extra observable isolation feature or inspection command not copied from the base walkthrough.

### Debugging

Diagnose one permission/capability/environment failure without randomly running everything as root.

---

# Exit gate

Given a claim like "the process is in a container, so it cannot affect the host", the learner can challenge the statement by asking exactly **which resources are isolated, which capabilities remain, and which kernel boundary is still shared**.