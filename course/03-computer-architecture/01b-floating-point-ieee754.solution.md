# Разбор упражнения 3.1B

Примеры зависят от compiler/platform, но типичные наблюдения:

```c
printf("%.17g\n", 0.1 + 0.2);
```

показывает approximation, не математический exact `0.3`.

Для `NaN`:

```c
#include <math.h>

double x = NAN;
assert(x != x);
assert(isnan(x));
```

Non-associativity удобно искать с очень разными magnitudes, например когда маленькое слагаемое теряется рядом с большим. Цель — объяснить rounding sequence, а не заучить конкретные числа.
