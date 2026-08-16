# 8.1 — ELF: headers, sections, segments и symbols

**Теория:** ~95 мин  
**Lab:** ~90 мин  
**С телефона:** теория — да

← [`README`](README.md) · → [`02-loader-pie-aslr.md`](02-loader-pie-aslr.md)

## Цель

Понимать ELF одновременно как link/tool representation и как input loader'у, не смешивая sections с runtime segments.

## ELF roles

На Linux ELF используется для relocatable objects, executables, shared objects и ряда других object-file forms.

ELF header задаёт class (32/64), byte order, object type, machine architecture и offsets/counts основных tables. Любой parser сначала проверяет magic/class/endianness/table bounds до чтения variable structures.

## Sections: link/tool view

Типичные sections:

```text
.text      instructions
.rodata    read-only constants
.data      initialized writable data
.bss       zero-initialized storage (SHT_NOBITS-style concept)
.symtab    full/static symbol table when present
.dynsym    dynamic symbols when needed
.strtab    associated strings
.debug_*   debug information when emitted
```

Section header table описывает file ranges/metadata. Не каждая section обязана быть mapped в process.

## Segments: loader/runtime view

Executable/shared-object **program header table** описывает segments, которые loader использует для создания process image. `PT_LOAD` segment задаёт file offset, virtual address, file/memory sizes, permissions и alignment.

```text
sections -> удобно linker/debug/tools
segments -> удобно loader/runtime mappings
```

Один loadable segment может содержать несколько sections с совместимыми permissions/layout.

## `p_filesz` vs `p_memsz`

Loadable segment может требовать больше bytes в memory, чем занимает в file. Область `p_memsz > p_filesz` инициализируется согласно ELF loading rules; это одна из причин большого `.bss` не обязан раздувать executable file тем же объёмом.

## Symbols

Symbol table entry связывает name с value/address-like data, size, binding/type и section relation.

Undefined symbol в `.o` — нормально до link, если definition придёт из другого object/library. Stripping обычной `.symtab` не удаляет machine instructions; dynamic linking data может оставаться отдельно.

## Relocations

Relocation описывает место, которое должно быть скорректировано после выбора final addresses/symbol values. Это bridge `separately compiled objects -> final layout` и основа части PIC/dynamic-link logic.

## Lab tools

Для **собственного/доверенного** binary:

```text
file
readelf -h
readelf -S
readelf -l
readelf -s
objdump -d
nm
```

Сопоставь sections с `PT_LOAD` ranges и permissions. Не запускай untrusted binary ради анализа; static tools тоже следует использовать в изолированной среде для truly hostile samples.

## Lab

Собери C fixture с initialized global, zero array, const string и function call; сравни normal `-g -O0` и stripped copy. Покажи `.text/.data/.bss`, program headers, symbols, disassembly.

## Exit check

Если спрашивают «где `.text` в памяти», ты должен сначала перейти от section view к loadable segment/mapping, а не считать section header прямой runtime page-table инструкцией.
