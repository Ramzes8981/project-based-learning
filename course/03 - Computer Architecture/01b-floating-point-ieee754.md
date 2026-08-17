# 3.2 — Почему `0.1 + 0.2` не обязано быть ровно `0.3`

**Теория:** ~70 мин · **Практика:** ~60 мин · **С телефона:** теория — да

← [`01-bits-integers-endianness.md`](01-bits-integers-endianness.md) · → [`02-boolean-logic-alu.md`](02-boolean-logic-alu.md)

## Проблема

Integer bits represent discrete values. Real-world measurements need fractions and huge/small magnitudes. Finite bits cannot represent every real number exactly.

## Scientific-notation intuition

Decimal:

```text
6.02 × 10^23
```

Binary floating point uses same idea with base 2:

```text
sign × significand × 2^exponent
```

A common standard is **IEEE 754**. Canonical x86-64 course environment uses IEEE-754-like binary32/binary64 behavior for `float`/`double`, but portable C code should not assume details without target contract.

## Why 0.1 is hard in binary

Some decimal fractions have infinite repeating binary expansion, like `1/3` repeats in decimal. Finite significand stores nearest representable value.

So sequence:

```text
decimal literal
→ nearest representable binary floating value
→ arithmetic rounded to representable result
```

explains many equality surprises.

## Special values

IEEE 754 supports:

- signed zero;
- infinities;
- NaN values;
- subnormal numbers near zero.

NaN has unusual comparisons: it is not equal to itself under normal equality semantics. Use library predicates like `isnan` rather than magic bit assumptions for normal code.

## Precision vs range

More exponent bits extend magnitude range; more significand precision distinguishes nearby values. Relative precision means spacing between representable numbers grows with magnitude.

## Compare with tolerance only when problem permits it

There is no universal `epsilon` for all floating comparisons. Appropriate absolute/relative tolerance depends on scale and algorithm/domain.

For money/counts requiring exact decimal semantics, binary float may be wrong representation entirely.

## Safe bit observation

Do not violate strict aliasing by casting `float *` to `uint32_t *` and dereferencing. To inspect object representation, copy bytes with `memcpy` into suitable unsigned integer only when sizes/target assumptions are checked.

## Практика

1. Print `0.1 + 0.2` with high precision.
2. Compare naive equality with a scale-aware tolerance for a controlled example.
3. Observe `INFINITY`, `NAN`, `isnan`.
4. Explain why exact integer counts should generally remain integers.

Разбор: [`01b-floating-point-ieee754.solution.md`](01b-floating-point-ieee754.solution.md).

## Exit check

Explain floating error as finite representation/rounding, not as “CPU calculates badly”.