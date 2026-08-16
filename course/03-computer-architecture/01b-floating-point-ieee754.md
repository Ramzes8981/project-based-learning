# 3.1B — Floating point и IEEE 754

**Теория:** ~95 мин  
**Упражнения:** ~70 мин  
**С телефона:** теория — да

← [`01-bits-integers-endianness.md`](01-bits-integers-endianness.md) · → [`02-boolean-logic-alu.md`](02-boolean-logic-alu.md)

## Цель

Понять, почему `float/double` — конечные binary approximations, что означают sign/exponent/fraction, и какие инженерные ошибки возникают из rounding/non-associativity.

## Почему fixed-point intuition не хватает

Integer N bits кодирует конечный набор целых. Для огромного диапазона real-like values floating point хранит примерно:

```text
sign × significand × base^exponent
```

Это trade-off: большой dynamic range, но precision распределена неравномерно.

## IEEE 754 binary32

Обычный `float` на нашей target platform соответствует binary32:

```text
1 sign bit
8 exponent bits
23 fraction bits
```

Для normal finite value концептуально:

```text
(-1)^sign × (1.fraction) × 2^(exponent-bias)
```

bias для binary32 = 127.

`double` обычно binary64:

```text
1 + 11 + 52 bits
bias = 1023
```

Курс не полагается на это как универсальный закон любого C implementation; в нашей Linux/x86-64 практике проверяй `sizeof`/platform assumptions, а binary format при сериализации задавай явно.

## Почему 0.1 не exact

Десятичная `0.1` имеет бесконечное двоичное дробное представление. Finite significand вынужден округлить.

Поэтому:

```text
0.1 + 0.2 == 0.3
```

не является надёжным general-purpose equality test для вычисленных floating values.

## Rounding

Arithmetic operation часто вычисляет exact mathematical result концептуально, затем округляет к ближайшему representable floating value согласно rounding mode. Ошибка может накапливаться.

## ULP intuition

Spacing между representable values растёт с magnitude. Рядом с большим числом следующий representable value дальше, чем рядом с маленьким.

Это объясняет, почему добавление очень маленького `delta` к огромному value иногда ничего не меняет.

## Special values

### Signed zero

`+0` и `-0` сравниваются равными, но знак может влиять на некоторые операции, например reciprocal sign.

### Infinity

Возникает как специальное значение для overflow/division-like semantics в floating environment; это не обычное максимальное finite число.

### NaN

`NaN` обозначает «not a number» для undefined/invalid floating results. Важный факт:

```text
NaN != NaN
```

по обычному equality comparison. Для проверки используют соответствующий API (`isnan`/`is_nan`).

### Subnormal

Очень малые ненулевые значения около zero используют другой encoding без implicit leading 1, позволяя gradual underflow ценой меньшей precision.

## Non-associativity

В real arithmetic:

```text
(a + b) + c = a + (b + c)
```

В floating arithmetic rounding может сделать результаты разными.

Следствие: compiler optimization/reduction order, parallel aggregation и data order способны влиять на low bits результата.

## Catastrophic cancellation intuition

Вычитание двух почти равных больших approximations может уничтожить значащие digits и сильно увеличить relative error результата.

## Money и counters

Не выбирай `double` автоматически для денег только потому, что есть decimal point. Часто нужен integer minor units или decimal arithmetic с чёткими rounding rules.

## Serialization

Нельзя записывать raw struct и надеяться на universal format. Если protocol/file format использует IEEE binary32/64, он должен явно определить width и byte order, а код — encode/decode согласно contract.

## C experiment

Используй `<float.h>` и `<math.h>`:

- `FLT_DIG`, `DBL_DIG`;
- `isnan`, `isinf`;
- выведи `0.1 + 0.2` с высокой precision;
- сравни `(a+b)+c` и `a+(b+c)` для подобранных magnitudes.

Не делай type-punning через incompatible pointer cast для чтения bits. Для controlled representation experiment копируй bytes через `memcpy` в integer object совместимого размера только после compile-time/runtime проверки размера.

## Упражнение

1. Объясни поля binary32 на бумаге.
2. Найди на практике decimal case, где equality неожиданна.
3. Найди non-associativity case.
4. Покажи `NaN` comparison.
5. Запиши, какие units/rounding contract выбрал бы для цены и почему.

Разбор: [`01b-floating-point-ieee754.solution.md`](01b-floating-point-ieee754.solution.md).

## Exit check

Почему floating error — не «рандомная неточность CPU», а следствие конечного representable set и rounding?
