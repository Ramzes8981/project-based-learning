# Course Environment

This file defines the **canonical technical environment** for the Systems Engineering Course.

The point is not to study tooling for weeks. The point is to make later labs reproducible and avoid changing environments in the middle of the course.

## Canonical desktop environment

For this course, use:

- **Windows + WSL2 + Ubuntu** as the primary desktop environment;
- VS Code with the WSL extension, or another editor that works inside the Linux filesystem;
- a normal Linux shell inside WSL;
- Git inside WSL;
- GCC or Clang;
- `make`;
- GDB;
- Python 3 for test harnesses and small support scripts.

Official WSL setup documentation:

- https://learn.microsoft.com/windows/wsl/install
- https://learn.microsoft.com/windows/wsl/setup/environment

A typical fresh Windows setup starts with:

```powershell
wsl --install
```

After Ubuntu is available, install the basic development tools inside Linux:

```bash
sudo apt update
sudo apt install build-essential clang gdb git make python3 python3-pip
```

Do not turn environment setup into a separate course. Once a small C program compiles and runs, start Module 0.

## Where to store course code

Prefer the Linux filesystem inside WSL, for example:

```text
~/systems-course/
```

rather than placing Linux projects under `/mnt/c/...`.

This keeps Linux tooling, permissions, paths, symlinks, and filesystem behavior closer to the environment used by later modules.

## Android / metro environment

Android is a **secondary learning environment**, not the canonical project runtime.

Use Termux for:

- tiny C experiments;
- shell practice;
- Git reading / small edits;
- compiling short examples;
- reviewing commands.

Use the phone mainly for:

- video lectures;
- Stepik exercises;
- mobile HTML books;
- quizzes and recall;
- notes.

Do **not** depend on Termux for Linux kernel labs, FUSE, container namespaces, debugger internals, or other platform-sensitive milestones.

## macOS

macOS is fine for most early C, algorithms, architecture, networking, and general programming work.

From Module 2 onward, POSIX details may differ from Linux. Modules involving Linux-specific interfaces (`ptrace`, Linux namespaces, some `/proc` behavior, libfuse/Linux integration) must be run in the canonical Linux environment.

If WSL does not expose a required kernel feature for a specific lab, use an Ubuntu virtual machine or native Linux for that lab. The course should never require replacing the host operating system.

---

# Compiler profiles

Do not begin with a complicated build system. Start with a simple compiler command and introduce Make only when repetition becomes annoying.

## Baseline C build

Use C17 for course-owned C code unless a tutorial has a justified compatibility requirement:

```bash
cc -std=c17 -Wall -Wextra -Wpedantic -g main.c -o main
```

Early goal: **zero unexplained compiler warnings**.

## Memory/debug build

From Module 1 onward, regularly use sanitizers for course-owned code:

```bash
cc -std=c17 -Wall -Wextra -Wpedantic -g \
  -fsanitize=address,undefined -fno-omit-frame-pointer \
  main.c -o main
```

A project is not considered healthy merely because it produces correct output once. Memory errors matter.

## POSIX code

When a module needs POSIX interfaces, introduce feature-test macros deliberately rather than silently switching the entire course to GNU extensions.

For example:

```bash
-D_POSIX_C_SOURCE=200809L
```

Some historical tutorials use GNU extensions or old APIs. The course should adapt the tutorial to the current module rather than copy its compiler flags blindly.

---

# Tools introduced just in time

| Tool | Introduced when |
|---|---|
| compiler / shell | Module 0 |
| Git basics | Module 0 |
| `make` | when the first build command becomes repetitive |
| GDB | first meaningful crash / Module 1 |
| AddressSanitizer / UBSan | Module 1 memory work |
| `strace` | Module 2 system-call work |
| `readelf`, `objdump`, `nm` | Module 3/8 |
| Wireshark | Module 5 |
| profiling tools | Module 4 |
| libfuse 3 | Module 7 |

Do not front-load tools that have no immediate use.

---

# Project hygiene

Every active project should have at least:

```text
project/
├── README.md
├── src/
├── include/        # when headers become useful
├── tests/
└── Makefile        # once justified
```

Exact structure may differ for small projects.

Rules:

1. Keep warnings enabled.
2. Commit after meaningful project slices.
3. Do not commit generated binaries.
4. Keep a short project README explaining current behavior and known limitations.
5. Prefer small, reversible commits over one giant final commit.
6. When a tutorial uses an outdated API, record the adaptation in the project README.

---

# Platform-sensitive milestone policy

Some upstream project tutorials are historically valuable but no longer suitable as exact modern instructions.

The course therefore distinguishes:

- **concept reference** — useful explanation, but code/API may be old;
- **current implementation source** — current official docs/examples;
- **course project spec** — what the learner actually builds.

This matters especially for:

- Linux containers;
- FUSE;
- debugger libraries/tooling;
- old compiler/build instructions.

The course project spec wins when an old tutorial conflicts with modern documentation.