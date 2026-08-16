# 3.1 — Как одни и те же bits становятся числами и bytes в памяти

**Теория:** ~70 мин · **Практика:** ~65 мин · **С телефона:** теория — да

← [`README`](README.md) · → [`01b-floating-point-ieee754.md`](01b-floating-point-ieee754.md)

## Проблема

Hardware хранит/передаёт finite bit patterns. Но source code говорит `42`, `-1`, `uint32_t`, characters. Нужен договор интерпретации.

## Bit pattern не несёт смысл сам

```text
11111111
```

может быть:

- unsigned 255;
- часть signed integer representation;
- byte UTF-8/binary file;
- opcode fragment;
- flags.

Meaning приходит из type/format/ISA contract.

## Unsigned binary

For N bits unsigned range:

```text
0 .. 2^N - 1
```

Bits have positional weights powers of two.

## Signed target representation

На canonical x86-64/Linux target signed integers представляются two's complement. Например 8-bit pattern `11111111` represents `-1` in that hardware interpretation.

Но курс отделяет **C language rules** от hardware representation: C17 signed overflow всё равно UB even on two's-complement CPU. Hardware wrap instruction behavior не лицензирует source-level overflow.

## Bytes and endianness

Multi-byte integer must choose memory byte order.

Example value `0x12345678`:

```text
big-endian byte order:    12 34 56 78
little-endian byte order: 78 56 34 12
```

**Endianness** describes byte order of multi-byte representation. It does not reverse bits inside each byte.

## Observe safely in C

Character types may inspect object representation. For target experiment:

```c
#include <stdint.h>
#include <stdio.h>

int main(void)
{
    uint32_t x = UINT32_C(0x12345678);
    const unsigned char *p = (const unsigned char *)&x;

    for (size_t i = 0; i < sizeof x; ++i) {
        printf("%02x\n", p[i]);
    }
}
```

This observes host representation; it does not define a portable file/network format.

## Serialization rule

External format must choose byte order explicitly and encode/decode fields. Never dump raw C struct and assume stable cross-machine format: padding, alignment, endianness and type sizes can differ.

## Практика

1. Convert several small unsigned values between decimal/hex/binary manually.
2. Inspect host bytes of `uint32_t`.
3. Write tiny explicit big-endian encode/decode for 32-bit unsigned value using shifts/masks with checked valid shift counts.

Разбор: [`01-bits-integers-endianness.solution.md`](01-bits-integers-endianness.solution.md).

## Exit check

Why does knowing host is little-endian not justify writing raw `struct` as a stable file format?