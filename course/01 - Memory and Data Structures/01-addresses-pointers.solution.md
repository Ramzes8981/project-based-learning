# Разбор 1.1

```c
#include <stddef.h>

int swap_ints(int *a, int *b)
{
    if (a == NULL || b == NULL) {
        return 0;
    }

    int tmp = *a;
    *a = *b;
    *b = tmp;
    return 1;
}
```

Если `a == b`, функция остаётся корректной: она несколько раз обращается к одному `int`, и итоговое значение не меняется.

`NULL` check — только одна часть pointer validity. Pointer может быть non-null, но уже не относиться к живому объекту; это тема 1.4.