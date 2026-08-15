# Разбор 1.2

Ключевой эксперимент:

```c
#include <stdio.h>
#include <stddef.h>

static void inspect(int values[], size_t count)
{
    printf("parameter sizeof = %zu\n", sizeof(values));
    for (size_t i = 0; i < count; ++i) {
        printf("%d\n", *(values + i));
    }
}

int main(void)
{
    int values[6] = {1, 2, 3, 4, 5, 6};
    printf("array sizeof = %zu\n", sizeof(values));
    inspect(values, 6);
    return 0;
}
```

Современный compiler обычно предупредит про `sizeof` на array function parameter — и это полезная диагностика.

`sizeof(values)` в `main` относится к настоящему `int[6]`. В `inspect` parameter уже имеет pointer semantics.
