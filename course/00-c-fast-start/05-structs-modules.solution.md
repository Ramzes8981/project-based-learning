# Разбор упражнения 0.5

`point.h`:

```c
#ifndef POINT_H
#define POINT_H

typedef struct {
    int x;
    int y;
} Point;

int point_manhattan(Point p);

#endif
```

`point.c`:

```c
#include "point.h"

static int abs_int(int x)
{
    return x < 0 ? -x : x;
}

int point_manhattan(Point p)
{
    return abs_int(p.x) + abs_int(p.y);
}
```

`main.c`:

```c
#include <assert.h>
#include "point.h"

int main(void)
{
    assert(point_manhattan((Point){0, 0}) == 0);
    assert(point_manhattan((Point){3, 4}) == 7);
    assert(point_manhattan((Point){-3, 4}) == 7);
    return 0;
}
```

Здесь `abs_int` объявлена `static` на file scope, поэтому является implementation detail `point.c`, а не частью public API.

Это уже первая маленькая демонстрация interface boundary.
