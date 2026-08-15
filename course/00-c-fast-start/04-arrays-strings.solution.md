# Разбор упражнения 0.4

Один вариант integer search:

```c
#include <stddef.h>

int linear_search(const int values[], size_t count, int target)
{
    for (size_t i = 0; i < count; ++i) {
        if (values[i] == target) {
            return (int)i;
        }
    }

    return -1;
}
```

Для маленького учебного массива `int` достаточно для индекса. В production API при очень больших collections контракт индекса/status стоило бы проектировать осторожнее.

Для strings идея та же, но сравнение:

```c
strcmp(values[i], target) == 0
```

Ключевой invariant цикла:

> перед началом итерации `i` элементы `0..i-1` уже проверены и не содержат более раннего совпадения.

`count == 0` естественно приводит к нулю итераций.
