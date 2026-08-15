# Разбор упражнения 0.2

Пример:

```c
#include <limits.h>
#include <stdio.h>

int main(void)
{
    int x = 42;

    printf("char      %zu\n", sizeof(char));
    printf("short     %zu\n", sizeof(short));
    printf("int       %zu\n", sizeof(int));
    printf("long      %zu\n", sizeof(long));
    printf("long long %zu\n", sizeof(long long));
    printf("x         %zu\n", sizeof(x));

    printf("INT_MIN  %d\n", INT_MIN);
    printf("INT_MAX  %d\n", INT_MAX);
    printf("UINT_MAX %u\n", UINT_MAX);

    unsigned int u = UINT_MAX;
    u += 1U;
    printf("wrapped  %u\n", u);

    return 0;
}
```

На обычном x86-64 Linux часто увидишь `int` 4 bytes и `long` 8 bytes, но смысл упражнения — не запомнить эти числа как закон C.

Unsigned переход из `UINT_MAX` в `0` определён языком. Не переноси этот вывод на signed overflow.
