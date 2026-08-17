# 8.2 — Почему адрес функции в файле и во время запуска может отличаться

**Теория:** ~90 мин · **Лаб:** ~85 мин · **С телефона:** theory — да

← [`01-elf-sections-segments-symbols.md`](01-elf-sections-segments-symbols.md) · → [`03-ptrace-debugger-lifecycle.md`](03-ptrace-debugger-lifecycle.md)

## Проблема

Symbol tool reports a value for function, but process `/proc/<pid>/maps` shows executable loaded at address that changes across runs. Debugger needs **runtime virtual address**.

## Loader

OS/kernel + dynamic loader map executable/shared objects, apply required relocations, resolve dynamic dependencies according to ELF/ABI rules and transfer control to entry point.

Exact responsibility split varies by executable type; core needs mapping relationship.

## PIE

**Position-Independent Executable (PIE)** is built so main executable can be loaded at varying virtual base. Modern Linux toolchains often enable PIE by default, but course build flags make fixture mode explicit.

## ASLR

**Address Space Layout Randomization (ASLR)** randomizes placement of selected mappings across runs. PIE lets main executable participate more fully; shared libraries/stack/etc. can also be randomized independently.

ASLR is mitigation, not secret key and not proof exploit impossible.

## Load bias

For a given ELF mapping, runtime address can often be related to ELF virtual-address coordinate via **load bias**:

```text
runtime_addr = ELF_virtual_value + load_bias
```

But compute bias from program headers + actual mappings, not by blindly subtracting first line of `/proc/maps` from symbol value. File offsets/alignment/multiple segments matter.

Course debugger can restrict accepted fixture layout and document algorithm; unsupported ELF layout must fail explicitly rather than set breakpoint at guessed address.

## Non-PIE comparison

Build fixture explicitly with/without PIE when toolchain supports flags, inspect ELF type/maps/symbol values. Explain difference empirically.

## Exit check

Why does a symbol value alone not always equal the runtime address a debugger must use?