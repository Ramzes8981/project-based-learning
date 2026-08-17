# 8.7 — Откуда debugger узнаёт source line и variable names, которых нет в ISA

**Теория:** ~85 мин · **Практика:** ~60 мин · **С телефона:** theory — да

← [`06-single-step-stack-unwinding.md`](06-single-step-stack-unwinding.md) · → [`08-memory-corruption-mitigations.md`](08-memory-corruption-mitigations.md)

## Проблема

CPU has addresses/registers. Source debugger prints `main.c:42`, local variable names/types and can unwind optimized frames. This information is not part of ISA machine code semantics.

## Debug information

Compilers can emit metadata, commonly **DWARF** on Linux/ELF, describing mappings such as:

```text
machine address ranges ↔ source files/lines
variables ↔ locations/expressions over time
call-frame unwinding rules
source-level types/scopes
```

Debug info can live in ELF sections or separate debug files and may be stripped from deployed executable.

## Line table is not one address per source line

Optimizations reorder/combine/remove code. One source line can map to multiple instruction ranges; some lines map to none; one instruction range can correspond to surprising source location.

## Variable location can change

A local can reside in register, stack slot, optimized away or described by expression depending on PC. “Variable address” is not stable universal concept.

## Scope boundary

Core project does **not** implement full DWARF parser. Use `readelf --debug-dump`, `addr2line`/tooling on own fixture to connect raw addresses with metadata. Optional extension can parse a narrow line-table subset via library.

## Exit check

Why can debugger show `<optimized out>` even though source code declares variable?