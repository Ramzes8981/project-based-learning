# 3.2 — Boolean logic, adders и ALU

**Теория:** ~65 мин  
**Упражнения:** ~60 мин  
**С телефона:** да

← [`01-bits-integers-endianness.md`](01-bits-integers-endianness.md) · → [`03-state-registers-memory.md`](03-state-registers-memory.md)

## Цель

Понять, как простые Boolean functions складываются в arithmetic datapath.

## Boolean gates

Для bits `a,b`:

```text
NOT a
AND(a,b)
OR(a,b)
XOR(a,b)
```

NAND универсален: из него можно построить остальные Boolean gates.

## Truth table как спецификация

XOR:

```text
a b | out
0 0 | 0
0 1 | 1
1 0 | 1
1 1 | 0
```

Hardware block можно воспринимать как функцию bit inputs → outputs, пока внутри нет state.

## Combinational vs sequential

Combinational logic output зависит от **текущих inputs**.

Sequential logic позже добавит state, зависящий от прошлого.

## Half adder

Складывает два bits:

```text
sum   = a XOR b
carry = a AND b
```

Full adder учитывает `carry_in` и выдаёт `sum + carry_out`.

Соединяя full adders, можно построить N-bit adder.

## Overflow hardware vs language

Hardware adder выдаёт фиксированные low N bits и flags/extra carry depending design. Язык C поверх этого устанавливает свои semantic rules.

CPU может физически wrap signed addition, но compiler вправе считать signed C overflow невозможным в valid program.

## ALU

Arithmetic Logic Unit выбирает операцию над operands:

```text
ADD
SUB
AND
OR
XOR
SHIFT
COMPARE-like flag generation
```

ALU сама не «знает программу». Control logic/decoded instruction выбирает operation.

## Multiplexer

MUX выбирает один из inputs по selector bits. В CPU multiplexers управляют, откуда взять operand/result/path.

## Exercise

1. Построй truth tables NAND, XOR, half-adder.
2. Объясни full-adder через два half-adders или equations.
3. Нарисуй 4-bit ripple-carry adder.
4. Для `1111 + 0001` укажи low 4 bits и carry-out.

Разбор: [`02-boolean-logic-alu.solution.md`](02-boolean-logic-alu.solution.md).

## Optional deep dive

Если нравится hardware path, Nand2Tetris Projects 1–2 — отличный дополнительный hands-on, но обязательная теория уже здесь.

## Exit check

Объясни разницу между «ALU умеет ADD» и «CPU выполняет instruction ADD».
