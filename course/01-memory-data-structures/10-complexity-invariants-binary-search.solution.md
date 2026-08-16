# Разбор упражнения 1.10

Вариант с sentinel `n`:

```c
#include <stddef.h>

size_t binary_search(const int *a, size_t n, int target)
{
    size_t lo = 0;
    size_t hi = n;

    while (lo < hi) {
        size_t mid = lo + (hi - lo) / 2;
        if (a[mid] == target) {
            return mid;
        }
        if (a[mid] < target) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return n;
}
```

`n` безопасен как sentinel, потому что valid indices принадлежат `[0, n)`. При `n == 0` loop не выполняется.
