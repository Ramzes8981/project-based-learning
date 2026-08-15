# Разбор упражнения 0.3

Один вариант:

```c
#include <assert.h>

enum TemperatureClass {
    TEMP_COLD,
    TEMP_NORMAL,
    TEMP_HOT
};

int classify_temperature(int t)
{
    if (t < 10) {
        return TEMP_COLD;
    }

    if (t < 25) {
        return TEMP_NORMAL;
    }

    return TEMP_HOT;
}

int main(void)
{
    assert(classify_temperature(9) == TEMP_COLD);
    assert(classify_temperature(10) == TEMP_NORMAL);
    assert(classify_temperature(24) == TEMP_NORMAL);
    assert(classify_temperature(25) == TEMP_HOT);
    assert(classify_temperature(100) == TEMP_HOT);
    return 0;
}
```

Ключевой вопрос — boundary values `9/10` и `24/25`. Если тестировать только очевидные середины диапазонов, можно пропустить off-by-one ошибку.
