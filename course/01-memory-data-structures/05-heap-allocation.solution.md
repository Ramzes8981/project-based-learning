# Разбор 1.5

Фрагмент безопасного size check:

```c
#include <stdint.h>
#include <stdlib.h>

if (n != 0 && sizeof(int) > SIZE_MAX / n) {
    /* size overflow */
}

int *values = malloc(n * sizeof(*values));
if (values == NULL && n != 0) {
    /* allocation failure */
}
```

Safe `realloc`:

```c
int *tmp = realloc(values, new_n * sizeof(*values));
if (tmp == NULL && new_n != 0) {
    free(values);
    return 1;
}
values = tmp;
```

В реальном коде перед `realloc` нужно так же проверить multiplication overflow для `new_n`.

Цель solution — показать ownership/failure structure, а не дать Vector implementation.
