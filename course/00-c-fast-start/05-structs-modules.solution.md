# Разбор упражнения 0.5

В этом упражнении корректность функции опирается на заранее объявленный диапазон:

```text
-10000 <= x <= 10000
-10000 <= y <= 10000
```

Это часть API contract, а не необязательный комментарий.

`point.h`:

```c
#ifndef POINT_H
#define POINT_H

typedef struct {
    int x;
    int y;
} Point;

/* Precondition: both coordinates are in [-10000, 10000]. */
int point_manhattan(Point p);

#endif
```

`point.c`:

```c
#include "point.h"

static int abs_int_in_domain(int x)
{
    return x < 0 ? -x : x;
}

int point_manhattan(Point p)
{
    return abs_int_in_domain(p.x) + abs_int_in_domain(p.y);
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
    assert(point_manhattan((Point){-10000, 10000}) == 20000);
    return 0;
}
```

Почему мы явно ограничили domain: без такого контракта выражение `-x` имеет проблемный случай `x == INT_MIN`, потому что положительное значение той же величины может не помещаться в `int`. Signed overflow в C — undefined behavior.

На раннем этапе курса мы не скрываем эту проблему кастом или случайным «более большим» типом. Сначала учимся задавать корректный контракт. Checked arithmetic и более общие способы обработки переполнения появятся позже.

`abs_int_in_domain` объявлена `static` на file scope, поэтому является implementation detail `point.c`, а не частью public API.
