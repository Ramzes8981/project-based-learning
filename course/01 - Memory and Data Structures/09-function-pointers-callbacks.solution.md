# Разбор упражнения 1.9

Один безопасный вариант интерфейса:

```c
#include <stdbool.h>
#include <stddef.h>

typedef bool (*Predicate)(int value, void *ctx);

size_t count_if(const int *values, size_t n, Predicate pred, void *ctx)
{
    size_t count = 0;
    for (size_t i = 0; i < n; ++i) {
        if (pred(values[i], ctx)) {
            ++count;
        }
    }
    return count;
}

static bool above_threshold(int value, void *ctx)
{
    const int *threshold = ctx;
    return value > *threshold;
}
```

Ключевой contract: `count_if` вызывает callback синхронно и не сохраняет `ctx`; caller обязан держать threshold живым до return. В production API также стоило бы определить поведение при `pred == NULL`.
