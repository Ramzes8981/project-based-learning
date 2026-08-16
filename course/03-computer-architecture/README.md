# Module 3 — Как процессор превращает биты в выполнение инструкций

**Оценка:** ~35–50 часов.  
**Prerequisite:** C memory model + Unix process basics.

Вместо списка hardware terms модуль идёт от вопроса: **какую минимальную машину надо построить, чтобы последовательность bytes стала программой?**

## Уроки

1. [`01-bits-integers-endianness.md`](01-bits-integers-endianness.md) — **Как одно и то же множество bits получает смысл числа и порядок bytes**.
2. [`01b-floating-point-ieee754.md`](01b-floating-point-ieee754.md) — **Почему `0.1 + 0.2` не обязано быть ровно `0.3`**.
3. [`02-boolean-logic-alu.md`](02-boolean-logic-alu.md) — **Как из простых логических операций получается arithmetic decision circuit**.
4. [`03-state-registers-memory.md`](03-state-registers-memory.md) — **Почему combinational logic недостаточно: машине нужно состояние**.
5. [`04-isa-machine-code.md`](04-isa-machine-code.md) — **Как договориться, что конкретные bits означают конкретную инструкцию**.
6. [`05-fetch-decode-execute.md`](05-fetch-decode-execute.md) — **Как CPU шаг за шагом исполняет machine code**.
7. [`06-assembler.md`](06-assembler.md) — **Зачем человеку assembler, если CPU понимает только bits**.
8. [`07-x86-64-abi-bridge.md`](07-x86-64-abi-bridge.md) — **Как отдельно скомпилированные функции договариваются о registers, stack и calls**.
9. [`08-module-checkpoint.md`](08-module-checkpoint.md) — checkpoint.

## Проект

[`project/README.md`](project/README.md) — Tiny16 assembler + emulator. Это course-owned toy ISA: достаточно маленькая, чтобы проследить каждый bit, но достаточно настоящая, чтобы увидеть decode/state/control flow.

## Boundary

Мы не строим транзисторный CPU, pipeline/branch predictor или cache hierarchy здесь. Cache появляется в Module 4, когда возникнет performance problem памяти.