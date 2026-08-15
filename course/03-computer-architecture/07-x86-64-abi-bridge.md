# 3.7 — Bridge: C → x86-64 → ABI

**Теория:** ~80 мин  
**Lab:** ~90 мин  
**С телефона:** теория — частично

← [`06-assembler.md`](06-assembler.md) · → [`08-module-checkpoint.md`](08-module-checkpoint.md)

## Цель

Связать учебный Tiny16 с реальным Linux/x86-64: registers, stack, call/return и System V-style calling convention basics.

## Architectural registers

x86-64 имеет general-purpose registers вроде:

```text
RAX RBX RCX RDX
RSI RDI RBP RSP
R8..R15
RIP
```

`RIP` — instruction pointer, `RSP` — stack pointer.

Subregister names (`EAX`, `AX`, `AL`) адресуют части register с особыми semantics записи, которые будем углублять в debugger/security module.

## Stack

Stack memory используется для:

- return addresses;
- spilled temporaries;
- locals, не помещённых/не оставленных в registers;
- saved registers;
- alignment/call convention needs.

Но compiler не обязан создавать классический frame для каждой C-функции.

## `call` / `ret`

Упрощённо `call` сохраняет return address и передаёт control target function. `ret` восстанавливает next instruction address со stack согласно architecture semantics.

## ABI

ABI — бинарный contract между compiled components:

- где аргументы;
- где return value;
- какие registers caller/callee должны сохранять;
- stack alignment;
- object/binary conventions.

Для обычного Linux x86-64 первые integer/pointer arguments в System V ABI идут через register sequence типа `RDI, RSI, RDX, RCX, R8, R9`; return часто через `RAX`.

Это рабочая model; exact edge cases (aggregates, vector args, variadic functions) остаются outside core.

## Caller-saved vs callee-saved

Если caller хочет сохранить значение в caller-saved register через call — он должен сохранить его сам.

Callee-saved register, если callee использует/меняет его, должен быть восстановлен перед return согласно ABI.

## Optimizer

С `-O0` assembly проще для обучения, но не считай её «истинной формой C». С `-O2` compiler может inline, eliminate, reorder, vectorize.

Architectural semantics остаются, source-to-assembly mapping становится сложнее.

## Lab

Создай C:

```c
long add3(long a, long b, long c) {
    return a + b + c;
}
```

Собери assembly output (`-S`) и executable с debug symbols.

Найди:

- function label;
- argument registers;
- arithmetic;
- return register;
- `ret`.

Затем функция с >6 integer args покажет stack involvement.

В GDB:

- breakpoint function;
- inspect registers;
- `disassemble`;
- step instructions.

## Causal questions

1. Почему ABI не является ISA?
2. Почему compiled C components должны договориться о register preservation?
3. Почему `-O0` stack frame нельзя считать обязательным языковым свойством C?
4. Чем Tiny16 calling convention отличается от того, что он вообще не обязан иметь call stack, если ISA этого не задаёт?

## Exit check

Объясни vertical chain:

```text
C call
→ compiler follows ABI
→ machine instructions
→ registers/stack
→ call/ret state changes
```
