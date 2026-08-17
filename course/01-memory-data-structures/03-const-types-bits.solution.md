# Разбор 1.3

```c
#include <stddef.h>
#include <stdint.h>

int checked_array_bytes(size_t count, size_t elem_size, size_t *out)
{
    if (out == NULL) {
        return 0;
    }
    if (elem_size != 0 && count > SIZE_MAX / elem_size) {
        return 0;
    }

    *out = count * elem_size;
    return 1;
}
```

Важно: выражение `count * elem_size` отсутствует на failure path. Проверка после multiplication была бы слишком поздней.