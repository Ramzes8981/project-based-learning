# 8.8 — Что mitigations делают с memory-corruption bug и чего они не исправляют

**Теория:** ~100 мин · **Лаб:** ~90 мин · **С телефона:** theory — да

← [`07-dwarf-source-debugging.md`](07-dwarf-source-debugging.md) · → [`09-module-checkpoint.md`](09-module-checkpoint.md)

## Проблема

C out-of-bounds/UAF may corrupt control/data. Modern systems add layers that make exploitation harder. Important distinction:

> mitigation changes exploitability/detectability; it does not make original invalid access correct.

## NX / executable permissions

Non-executable data mappings reduce straightforward execution of injected bytes. Return-oriented/code-reuse attacks show why NX is not complete defense.

## Stack canary

Compiler can place guard value near sensitive stack control data and verify before return. Some overwrites are detected, but not every memory corruption touches canary or is stopped before harmful data change.

## PIE + ASLR

Randomized runtime addresses make reliable code/data location harder. Information leaks or weak entropy/reuse can reduce benefit. ASLR does not enforce memory bounds.

## RELRO

ELF/linker hardening can make relocation-related regions read-only after relocation. Full/partial modes differ. It protects specific writable metadata surfaces, not arbitrary heap/stack data.

## Fortify / checked libc opportunities

Toolchain may add compile/runtime checks for operations when object sizes are known. Coverage depends on optimization/compiler/operation and is not substitute for explicit bounds.

## Sanitizers are developer diagnostics, not deploy mitigation

ASan/UBSan/TSan instrument programs to find bugs during testing. They change memory/performance and are not normally production exploit mitigation equivalent.

## Lab

Compile own intentionally vulnerable fixture **marked BROKEN EXAMPLE** with combinations of PIE/non-PIE, stack protector, RELRO/NX observations. Use `readelf`/maps/debugger to explain changed properties; do not build exploit chain.

Then fix bounds bug in source and show mitigations remain defense-in-depth.

## Exit check

For each mitigation name one attack surface it raises cost for and one class of bug it does not prevent.