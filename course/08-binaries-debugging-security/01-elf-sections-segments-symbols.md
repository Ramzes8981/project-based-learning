# 8.1 — Как executable хранит то, что нужно loader-у и debugger-у

**Теория:** ~95 мин · **Лаб:** ~90 мин · **С телефона:** theory — да

← [`README`](README.md) · → [`02-loader-pie-aslr.md`](02-loader-pie-aslr.md)

## Проблема

Compiler/linker produced executable bytes. OS loader must know which bytes map into memory, with what permissions and entry point. Debugger may additionally want symbol/debug information.

A flat byte blob is insufficient; executable needs structured format.

## ELF

Linux commonly uses **ELF (Executable and Linkable Format)** for executables, shared objects, object files and core dumps.

Core mental model separates two views:

```text
program headers / segments → runtime loader view
section headers / sections → link/debug/tooling organization view
```

## Segments: runtime mapping contract

Program headers describe loadable **segments** with file offset, virtual address intent, file/memory size and permissions. Loader primarily follows these for executable mappings.

`PT_LOAD` segments often explain why `/proc/<pid>/maps` shows read-only, executable and writable regions.

Do not say “`.text` is mapped because loader reads section `.text`” as universal ELF runtime mechanism. Sections can contribute bytes to segments; program headers drive loading.

## Sections

Sections such as `.text`, `.rodata`, `.data`, `.bss`, symbol/string/debug sections organize link-time/tool information. A stripped runtime executable can function with much section/symbol information removed if loadable program metadata remains sufficient.

## Symbols

Symbol table maps names to values/metadata in file/linking coordinate system. Dynamic symbols are subset needed for dynamic linking/export; full `.symtab` can be stripped.

Debugger cannot assume every function name exists in stripped binary.

## `.bss` puzzle

Uninitialized data can occupy memory size larger than bytes stored in file. Loadable segment expresses file size vs memory size; loader zero-fills required tail. This is why file need not contain megabytes of literal zero bytes.

## Observe

Use `readelf -h -l -S -s` and `objdump` on a tiny fixture. Before commands predict which view explains runtime executable permission region.

## Exit check

Why can an ELF execute after many section headers/debug symbols are stripped, and why are segments more directly relevant to loader?