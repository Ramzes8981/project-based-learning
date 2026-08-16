# Разбор 0.5

`math_ops.h`:

```c
#ifndef MATH_OPS_H
#define MATH_OPS_H

int add(int a, int b);

#endif
```

`math_ops.c`:

```c
#include "math_ops.h"

int add(int a, int b)
{
    return a + b;
}
```

`main.c`:

```c
#include <stdio.h>
#include "math_ops.h"

int main(void)
{
    printf("%d\n", add(20, 22));
    return 0;
}
```

Сборка по стадиям:

```bash
cc -std=c17 -Wall -Wextra -Wpedantic -c main.c -o main.o
cc -std=c17 -Wall -Wextra -Wpedantic -c math_ops.c -o math_ops.o
cc main.o math_ops.o -o app
```

Если последняя команда получает только `main.o`, declaration функции всё ещё известна, но её definition не найдена среди входов linker-а.