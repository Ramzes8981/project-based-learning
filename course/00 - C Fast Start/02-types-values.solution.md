# Разбор 0.2

Один из корректных вариантов:

```c
#include <stdio.h>

int main(void)
{
    int done = 3;
    int total = 4;
    double fraction = (double)done / total;

    printf("done=%d total=%d fraction=%.2f\n", done, total, fraction);
    return 0;
}
```

Если написать `double fraction = done / total;`, сначала выполнится integer division: результат `0`, который затем преобразуется в `0.0`. Cast одного operand меняет тип самой операции деления.