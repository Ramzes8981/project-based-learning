# Разбор 1.2

Correct solution не должен содержать intentional warning из диагностического эксперимента:

```c
#include <stddef.h>

int sum_ints(const int *values, size_t count, int *out_sum)
{
    if (out_sum == NULL) {
        return 0;
    }
    if (values == NULL && count != 0) {
        return 0;
    }

    int sum = 0;
    for (size_t i = 0; i < count; ++i) {
        sum += values[i];
    }
    *out_sum = sum;
    return 1;
}
```

Условие упражнения пока явно предполагает отсутствие `int` overflow. В production-style API такое предположение должно быть либо доказано bounds, либо заменено checked arithmetic.