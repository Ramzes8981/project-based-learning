# Module 8 — Binaries, Debugging, and the Security Bridge

**Status:** CORE  
**Estimated effort:** 40–55 hours (~6–8 weeks)  
**Core milestone:** minimal Linux debugger in C

## Why this module changed

The original roadmap pointed directly to Sy Brand's *Writing a Linux Debugger* series. It is an excellent explanation, but its implementation is C++ and later depends on `libelfin`; C++ was never taught in this course.

That was a hidden prerequisite.

The audited course therefore uses a **course-owned C debugger scope** as core, while the original series becomes a conceptual/reference source. Full source-level DWARF support is Stretch.

## Prerequisites

- x86-64/register/stack/ABI basics from Module 3;
- processes/signals/waiting from Module 2;
- Linux process inspection from Module 6;
- binary/file-layout and memory skills from prior modules.

## Sources

- **PRIMARY:** Linux man pages for `ptrace`, `waitpid`, signals, `/proc`.
- **BINARY REFERENCE:** ELF specification/tool docs + `readelf`, `objdump`, `nm`.
- **CONCEPT REFERENCE:** Sy Brand, *Writing a Linux Debugger*.
- **ARCHITECTURE REFERENCE:** Dive into Systems / x86-64 material as needed.

The Sy Brand code is not copied into the core C project.

---

# Outcomes

The learner can:

- inspect an ELF executable and distinguish sections/symbols/debug info;
- understand PIE/ASLR at a practical level;
- inspect process mappings and registers;
- explain how x86 software breakpoints use `int3` / byte `0xCC`;
- use `ptrace` to launch/control a tracee;
- read/write tracee memory/register state;
- implement address breakpoints and single stepping in a limited debugger;
- explain common executable hardening mechanisms and how memory corruption interacts with them;
- transition into legal local reverse-engineering/binary-exploitation labs without a conceptual cliff.

---

# Unit 8.1 — Executable files and ELF

### Learn

- executable vs object/shared object;
- ELF header;
- sections vs program segments at a working level;
- `.text`, `.rodata`, `.data`, `.bss`;
- symbol table;
- dynamic-linking idea;
- debug information concept.

### Tools

Use:

```text
file
readelf
objdump
nm
ldd   # with normal caution around untrusted binaries
```

### Lab

Compile one tiny C program with/without debug symbols and compare:

- file size;
- symbols;
- disassembly;
- sections.

### Situational question

Why can stripping symbols make human debugging harder without removing the machine instructions needed to run the program?

---

# Unit 8.2 — Process memory, PIE, and ASLR

### Learn

- virtual mappings;
- code/data/stack/heap/shared-library mappings;
- position-independent executable concept;
- ASLR;
- load address vs symbol-relative address.

### Lab

Inspect `/proc/<pid>/maps` across several runs of a test program and relate mappings to ELF/tool output.

### Common mistake

Assuming a source-level or link-time address always equals the runtime virtual address when PIE/ASLR is enabled.

---

# Unit 8.3 — `ptrace` and debugger lifecycle

### Learn

- tracer/tracee relationship;
- `PTRACE_TRACEME` / attach concept;
- `waitpid` state changes;
- stop/continue;
- signals as debugger events;
- error checking.

### Project slice — `minidbg-c` v0

Implement:

1. launch a test program;
2. trace it;
3. wait for stop;
4. continue;
5. report normal/signal termination.

### Rubric

The debugger must not confuse "child exited" with "child stopped".

---

# Unit 8.4 — Registers and memory

### Learn

- general-purpose register set at a practical level;
- instruction pointer;
- stack pointer;
- `ptrace` register/memory access interfaces;
- machine word / byte replacement issue.

### Project slice

Add commands to:

- dump important registers;
- read one memory word/address;
- show current instruction pointer.

### Scenario

If memory read returns a value that could also be `-1`, how do you distinguish data from a `ptrace` error? Check `errno` according to API semantics rather than guessing.

---

# Unit 8.5 — Software breakpoints

### Learn

On x86-64, a software breakpoint can replace the first byte of an instruction with `0xCC` (`int3`). When it executes, the tracee stops with `SIGTRAP`.

Core reasoning:

1. save original byte/word;
2. insert breakpoint byte;
3. continue;
4. receive stop;
5. adjust instruction pointer as required;
6. restore original instruction;
7. single-step original instruction;
8. reinsert breakpoint if it remains enabled.

### Project slice

Implement address breakpoints for the controlled x86-64 Linux environment.

### Required test

Set a breakpoint on a known non-PIE test binary first; then repeat with PIE using resolved runtime address logic.

---

# Unit 8.6 — Single-step and simple backtrace reasoning

### Learn

- `PTRACE_SINGLESTEP`;
- stop event;
- frame-pointer-based stack walk as a limited teaching model;
- why optimized code may omit/change simple frame assumptions;
- unwind metadata exists because real unwinding is harder.

### Project slice

Core requirement: instruction single-step.

A basic frame-pointer backtrace can be Guided/Stretch depending compiler settings.

---

# Unit 8.7 — DWARF and source-level debugging (concept + Stretch)

### Learn conceptually

- source line ↔ address mapping;
- DIEs / debug information at a high level;
- why a debugger needs a DWARF parser/library for robust source/variable support.

### Core scope

Use existing tools (`readelf --debug-dump`, GDB) to inspect debug info and explain the relationship.

### Stretch

Follow selected later parts of Sy Brand's series or another current library to add source-line breakpoints/variables.

Do not make C++/libelfin a surprise prerequisite for core completion.

---

# Unit 8.8 — Memory corruption and hardening bridge

### Learn

- stack/heap corruption recap;
- out-of-bounds write;
- use-after-free;
- code vs data permissions;
- NX/DEP concept;
- stack canary;
- PIE + ASLR;
- RELRO concept;
- compiler hardening flags as implementation-dependent tooling.

### Local lab only

Compile a deliberately vulnerable toy program in a controlled local environment and observe how memory corruption appears in GDB/minidbg. The core goal is diagnosis and mitigation understanding, not weaponization against real systems.

### Situational questions

- Why does ASLR not repair a buffer overflow?
- Why can a stack canary detect some overwrites but not make C memory-safe?
- Why is disabling mitigations useful only as a teaching simplification, not a production recommendation?

---

# Core milestone rubric — Minimal Linux Debugger in C

### Required features

- launch tracee;
- continue;
- report stop/exit state;
- read registers;
- read memory;
- set/remove address breakpoint;
- handle stepping over own breakpoint;
- instruction single-step.

### Tests

Use small deterministic test programs compiled with known flags. Include PIE and non-PIE behavior in the test plan, even if full symbol resolution is limited.

### Transfer task

Choose one:

- write register command;
- memory write command;
- breakpoint list/enable-disable;
- simple runtime-symbol lookup;
- frame-pointer backtrace under defined compiler flags.

### Engineering review

Document:

- architecture assumptions (Linux + x86-64);
- unsupported features;
- tracer/tracee state machine;
- signal handling;
- breakpoint lifecycle;
- security implications of process-debug privileges.

---

# Exit gate

The learner can explain how a source program becomes an ELF process and how a debugger observes/modifies that process at runtime, without depending on C++ concepts the course never taught.