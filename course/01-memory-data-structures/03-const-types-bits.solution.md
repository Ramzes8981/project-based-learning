# Разбор 1.3

Пример operations:

```c
#include <stdbool.h>
#include <stdint.h>

static uint32_t enable(uint32_t flags, uint32_t mask)
{
    return flags | mask;
}

static uint32_t disable(uint32_t flags, uint32_t mask)
{
    return flags & ~mask;
}

static bool has(uint32_t flags, uint32_t mask)
{
    return (flags & mask) != 0;
}
```

Здесь state передаётся by value и возвращается как новое значение — подход удобен для маленького integer bitset.

Для mutable struct позже разумнее pointer-based API.
