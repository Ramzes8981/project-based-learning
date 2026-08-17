# Разбор 0.4

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    int values[5] = {10, 20, 30};
    size_t used = 3;
    size_t max_items = sizeof values / sizeof values[0];

    for (size_t i = 0; i < used; ++i) {
        printf("%d\n", values[i]);
    }

    char word[8];
    const char *src = "cat";
    size_t len = strlen(src);
    if (len + 1 <= sizeof word) {
        memcpy(word, src, len + 1);
        printf("%s\n", word);
    }

    printf("used=%zu max=%zu\n", used, max_items);
    return 0;
}
```

`used` — логическое число занятых элементов. `max_items` — сколько элементов помещается в фиксированном массиве. Для `word` конечный `\0` копируется вместе с текстом.