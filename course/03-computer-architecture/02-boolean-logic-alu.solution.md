# Разбор 3.2

Half-adder:

```text
sum = XOR(a,b)
carry = AND(a,b)
```

Для `1111 + 0001` 4-bit adder даёт low result `0000` и carry-out `1`.

Сам факт carry-out ещё не определяет signed overflow: signed overflow связан с interpretation operands/sign bits, а unsigned carry — другая семантика.
