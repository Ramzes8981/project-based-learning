# 3.3 — State, registers, clock и memory

**Теория:** ~60 мин  
**Упражнения:** ~45 мин  
**С телефона:** да

← [`02-boolean-logic-alu.md`](02-boolean-logic-alu.md) · → [`04-isa-machine-code.md`](04-isa-machine-code.md)

## Цель

Понять, почему computer требует state и как registers/RAM отличаются от pure combinational logic.

## Почему state нужен

Combinational circuit не помнит прошлое. Если inputs исчезли, output меняется.

Program execution требует хранить:

- current data;
- instruction position;
- intermediate results;
- stack/variables.

## Clocked state

Упрощённая synchronous model:

```text
между clock edges combinational logic вычисляет next state
на edge storage elements фиксируют новое state
```

Реальные CPUs сложнее (pipelines, multiple clocks/domains, out-of-order), но эта модель достаточна для Tiny16.

## Register

Register — небольшой быстрый storage element внутри CPU/datapath.

Tiny16 будет иметь несколько general-purpose registers + program counter.

## Program counter

PC содержит address/index следующей instruction.

Обычный шаг:

```text
fetch instruction at PC
execute
PC = PC + 1
```

Branch/jump может заменить next PC другим value.

## RAM abstraction

Memory можно моделировать как indexed array words/bytes:

```text
address -> stored value
```

CPU load читает memory в register, store пишет register/value в memory.

## Registers vs RAM

Registers:

- очень мало;
- directly encoded/selected by instructions;
- fastest tier datapath.

RAM:

- намного больше;
- addressable;
- access дороже.

Cache hierarchy добавим позже.

## Exercise

Нарисуй state Tiny machine:

```text
R0,R1,R2,R3
PC
RAM[0..255]
```

Проведи вручную три шага hypothetical:

```text
LOADI R0, 5
LOADI R1, 7
ADD   R0, R1
```

После каждого шага запиши registers и PC.

Разбор: [`03-state-registers-memory.solution.md`](03-state-registers-memory.solution.md).

## Exit check

Что сломается, если ALU существует, но нет ни одного state element?
