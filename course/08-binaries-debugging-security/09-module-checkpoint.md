# Module 8 — Checkpoint

## Explain

- ELF sections vs segments;
- symbols/relocations;
- loader/shared libraries;
- PIE/ASLR/load base;
- ptrace tracer/tracee stop lifecycle;
- wait status;
- register/memory inspection;
- x86 software breakpoint state machine;
- single-step;
- frame-pointer unwind limitations;
- DWARF role;
- NX/canary/ASLR/RELRO defense layers.

## Core milestone

Проверь [`project/ACCEPTANCE.md`](project/ACCEPTANCE.md).

## Required fixtures

- non-PIE deterministic target;
- PIE target;
- loop/function-call target;
- signal-terminating target.

## Transfer

Одна:

- breakpoint enable/disable list;
- memory write;
- symbol-to-runtime address helper;
- limited frame-pointer `bt`;
- signal forwarding policy.

## Exit gate

Ты можешь пройти chain:

```text
ELF file
→ loader mappings
→ running registers/memory
→ ptrace stop
→ breakpoint patch
→ observe/modify/continue
```

и объяснить, где начинаются platform/security assumptions.
