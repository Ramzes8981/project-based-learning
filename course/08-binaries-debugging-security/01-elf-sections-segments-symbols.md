# 8.1 — ELF: headers, sections, segments и symbols

**Теория:** ~90 мин  
**Lab:** ~90 мин  
**С телефона:** теория — да

← [`README`](README.md) · → [`02-loader-pie-aslr.md`](02-loader-pie-aslr.md)

## Цель

Понимать ELF одновременно как link-time object structure и как input loader'у, не смешивая sections и runtime segments.

## ELF family

Linux commonly uses ELF for:

- relocatable object `.o`;
- executable;
- shared object `.so`;
- core-like files.

ELF header identifies class (32/64-bit), byte order, type, machine architecture and offsets/counts tables.

## Sections

Sections в основном организуют information для linker/debug/tools:

```text
.text      machine code
.rodata    read-only constants
.data      initialized writable data
.bss       zero-initialized storage description
.symtab    symbols (when present)
.strtab    strings for symbol names
.debug_*   debug information (when emitted)
```

Sections имеют names/metadata through section header table.

## Segments / program headers

Loader использует **program header table** executable/shared object, чтобы создать runtime mappings. Один loadable segment может включать несколько sections с compatible permissions/layout.

```text
ELF file
sections: link/tool view
segments: load/runtime view
```

ELF gABI определяет program headers как descriptions segments, нужных для подготовки program к execution. citeturn857293search2

## `.bss`

Large zero-initialized global array не обязан занимать столько же bytes в file: format может описать memory size > file bytes, loader supplies zero-filled memory.

Это distinction file size vs memory size.

## Symbols

Symbol associates name with value/address-like information, size/binding/type/section.

- local/global;
- defined/undefined;
- function/object.

Linker resolves undefined references against definitions/libraries.

Stripped executable может не иметь rich normal symbol table, но machine code остаётся executable. Dynamic symbols needed for dynamic linking may still exist depending binary.

## Relocations

Relocation говорит linker/loader: поле machine code/data должно быть adjusted once final address known.

Это bridge между separately compiled objects и position-independent code.

Core не требует вручную писать relocation processor.

## Tools

```text
file
readelf -h/-S/-l/-s
objdump -d
nm
ldd   # только trusted binaries; не как security analyzer untrusted files
```

## Lab

Собери маленький C program:

- global initialized variable;
- global zero array;
- const string;
- function call.

Сравни:

```text
cc -g -O0
cc -s/-strip equivalent copy
```

Найди `.text/.data/.bss`, program headers, symbols, disassembly. Нарисуй, какие sections входят в loadable segments.

## Causal questions

1. Почему sections и segments не являются синонимами?
2. Почему `.bss` может занимать много runtime memory при маленьком file footprint?
3. Почему stripping symbols не удаляет instructions?
4. Где relocation появляется в source→object→link chain?

## Exit check

Объясни, какие ELF structures нужны linker/tools, а какие loader для mappings.
