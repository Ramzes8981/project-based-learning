# Разбор 1.5

Один ясный contract: zero count возвращает success и `*out = NULL`.

```c
#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>

int make_zeroed_ints(size_t count, int **out)
{
    if (out == NULL) {
        return 0;
    }
    *out = NULL;

    if (count == 0) {
        return 1;
    }
    if (count > SIZE_MAX / sizeof(int)) {
        return 0;
    }

    int *items = calloc(count, sizeof *items);
    if (items == NULL) {
        return 0;
    }

    *out = items;
    return 1;
}
```

Caller, получив non-null `*out`, становится owner и обязан вызвать `free` ровно один раз. Zero-size policy здесь задана самим API и не зависит от спорных corner cases `realloc(ptr, 0)`.