# 3.4 — ISA и machine code

**Теория:** ~70 мин  
**Упражнение:** ~60 мин  
**Project slice:** ~2–3 часа  
**С телефона:** да

← [`03-state-registers-memory.md`](03-state-registers-memory.md) · → [`05-fetch-decode-execute.md`](05-fetch-decode-execute.md)

## Цель

Понять Instruction Set Architecture как контракт между software и machine implementation.

## ISA

ISA определяет programmer-visible machine model:

- registers;
- instruction encodings;
- operations;
- memory/addressing semantics;
- branch behavior;
- sometimes privilege/system state.

Microarchitecture определяет, **как** конкретный CPU реализует ISA internally.

Два CPUs могут исполнять одну ISA разными pipelines/caches.

## Instruction encoding

Tiny16 instruction — 16-bit word. Курс задаёт exact format в [`project/ISA.md`](project/ISA.md).

Например conceptually:

```text
[ opcode | dst | src | immediate/unused ]
```

Bits — просто representation. Meaning появляется из ISA spec.

## Opcode

Opcode выбирает operation. Остальные fields могут выбирать registers/immediate/address.

## Immediate

Immediate — literal value encoded прямо в instruction, например `LOADI R0, 7`.

Ширина field ограничивает range. Если immediate 8 bits — нельзя просто представить произвольный 16-bit value без другого instruction/design.

## Load/store

Tiny16 использует простую load/store model:

```text
LOAD  Rd, [address/register]
STORE Rs, [address/register]
```

ALU primarily operates registers.

## Branch

Branch меняет PC при condition.

Не обязательно иметь complex flags: course ISA может использовать compare/zero semantics, главное — specification deterministic.

## Machine code vs assembly

Machine code:

```text
binary/hex words
```

Assembly:

```text
LOADI R0, 5
ADD R0, R1
```

Assembler переводит symbolic representation в words.

## Exercise

Прочитай [`project/ISA.md`](project/ISA.md) и вручную encode/decode минимум 8 instructions.

Проверь:

- register fields;
- immediate range;
- invalid opcode;
- branch target representation.

## Project slice

Создай parser/data structures будущего assembler, но **не пиши весь assembler сразу**. Сначала функция/модуль, который умеет encode одну уже распарсенную instruction structure.

## Exit check

Объясни разницу ISA vs assembly syntax vs emulator implementation.
