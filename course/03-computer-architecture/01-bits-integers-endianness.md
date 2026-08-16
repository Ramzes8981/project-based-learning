# 3.1 — Bits, integers и endianness

**Теория:** ~55 мин  
**Упражнения:** ~45 мин  
**С телефона:** да

← [`README`](README.md) · → [`01b-floating-point-ieee754.md`](01b-floating-point-ieee754.md)

## Цель

Уметь переводить значения между binary/hex, объяснять two's complement и отличать numeric value от byte order в памяти.

## Bits и hex

Один hex digit кодирует 4 bits:

```text
0x0 = 0000
0xF = 1111
0x2A = 0010 1010
```

Hex удобен для addresses, masks, opcodes и raw bytes, потому что компактно сохраняет bit boundaries.

## Unsigned N-bit integer

Для N bits диапазон:

```text
0 .. 2^N - 1
```

Binary value:

```text
b_(N-1)*2^(N-1) + ... + b_1*2 + b_0
```

## Two's complement

Для signed N-bit representation старший bit имеет weight `-2^(N-1)`, остальные обычные положительные weights.

Диапазон:

```text
-2^(N-1) .. 2^(N-1)-1
```

Например 8-bit:

```text
11111111 = -1
10000000 = -128
01111111 = 127
```

Two's complement объясняет hardware representation, но **не меняет правило C**, что signed integer overflow — UB.

## Shifts

Unsigned left/right shifts удобны для masks/field extraction. Не переносим автоматически те же assumptions на signed negative values.

## Endianness

Endianness описывает **порядок bytes multi-byte value в памяти**, а не порядок bits внутри byte.

Для `uint32_t x = 0x12345678`:

```text
little-endian memory addresses increasing:
78 56 34 12

big-endian:
12 34 56 78
```

Numeric value всё равно `0x12345678`.

## Network byte order preview

Network protocols часто задают multi-byte integers в big-endian/network order. Host representation может отличаться, поэтому serialization должна быть explicit.

## Object bytes

В C можно исследовать bytes объекта через `unsigned char *`. Character types имеют специальную роль для наблюдения object representation; не делай из этого общего разрешения alias arbitrary objects через любой pointer type.

## Exercise

1. Переведи `0xA7`, `0x1234` в binary.
2. Представь `-1`, `-2`, `127`, `-128` в 8-bit two's complement.
3. Напиши C-программу, которая выводит bytes `uint32_t 0x12345678` через `const unsigned char *`.
4. Объясни observed endianness.

Разбор: [`01-bits-integers-endianness.solution.md`](01-bits-integers-endianness.solution.md).

## Exit check

Объясни, почему `0x12345678` как value и byte sequence `78 56 34 12` не противоречат друг другу.
