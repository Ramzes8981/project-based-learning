# 0.5 — Struct, enum, headers и linker

**Теория:** ~45 мин  
**Упражнение:** ~35 мин  
**Project slice:** ~60–90 мин  
**С телефона:** теория — да; project slice — ПК

← [`04-arrays-strings.md`](04-arrays-strings.md) · → [`06-module-checkpoint.md`](06-module-checkpoint.md)

## Цель

Научиться группировать связанные данные в `struct`, описывать состояния через `enum` и разделять маленькую программу на interface/implementation без магии вокруг headers и linker.

## Prerequisite check

1. Чем declaration отличается от definition?
2. Почему MiniKV должен знать capacity каждого string buffer?
3. Что такое executable и какую роль выполняет linker?

## Инженерный контекст

Пока program состоит из 30 строк, всё можно держать в одном файле. Но реальный проект быстро разваливается, если representation, public API, tests и executable entrypoint не имеют границ.

C не даёт classes/modules в Python-смысле, зато позволяет явно разделять interface и implementation через headers/translation units.

## `struct`

```c
struct Point {
    int x;
    int y;
};
```

Использование:

```c
struct Point p = { .x = 10, .y = 20 };
printf("%d\n", p.x);
```

`struct` описывает агрегат из полей. В памяти поля принадлежат одному объекту, но между ними позже может оказаться padding для alignment.

Пока padding не нужен для MiniKV; подробно разберём его перед binary/storage work.

## `typedef`

Можно создать удобное имя типа:

```c
typedef struct Point {
    int x;
    int y;
} Point;
```

Это не создаёт новый runtime object и не делает C «объектно-ориентированным». `typedef` даёт alias/имя типа.

## `enum`

```c
typedef enum {
    RESULT_OK,
    RESULT_NOT_FOUND,
    RESULT_FULL
} Result;
```

`enum` удобен, когда у состояния есть ограниченный именованный набор вариантов.

Именованный `RESULT_NOT_FOUND` обычно лучше «магического `-7`», смысл которого приходится помнить.

## Headers

`point.h`:

```c
#ifndef POINT_H
#define POINT_H

struct Point {
    int x;
    int y;
};

int point_manhattan(struct Point p);

#endif
```

`point.c`:

```c
#include "point.h"

int point_manhattan(struct Point p)
{
    int x = p.x < 0 ? -p.x : p.x;
    int y = p.y < 0 ? -p.y : p.y;
    return x + y;
}
```

`main.c` включает header и вызывает функцию.

### Зачем include guard

Если один header косвенно включится несколько раз, guard не даст его содержимому повторно объявиться там, где это запрещено/мешает.

## Translation unit

После preprocessing каждый `.c` превращается в отдельную **translation unit** и компилируется отдельно.

Например:

```bash
cc -std=c17 -Wall -Wextra -Wpedantic -g -c point.c -o point.o
cc -std=c17 -Wall -Wextra -Wpedantic -g -c main.c -o main.o
cc point.o main.o -o app
```

Первые две команды создают object files. Последняя вызывает linking.

Можно и короче:

```bash
cc -std=c17 -Wall -Wextra -Wpedantic -g point.c main.c -o app
```

Но длинная форма лучше показывает модель.

## Почему declaration в `.h`, definition в `.c`

Header — контракт, который должны видеть другие translation units.

Implementation details по возможности остаются в `.c`.

Это уменьшает accidental coupling и делает интерфейс проекта явным.

## Linker errors

Если header обещает:

```c
int point_manhattan(struct Point p);
```

но ни один object file не содержит definition, compilation отдельных файлов может пройти, а linker затем сообщит, что символ не найден.

Теперь `undefined reference` должен быть логически понятен.

## Causal questions

1. Почему `struct` лучше параллельных несвязанных массивов для сущности `Entry`?
2. Почему public header не должен без необходимости раскрывать каждый implementation detail?
3. Почему программа может успешно скомпилировать `.c` файлы и всё равно провалиться на linking?
4. Чем named enum status лучше случайных integer codes?

## Упражнение

Сделай маленький модуль `point` из трёх файлов:

```text
point.h
point.c
main.c
```

Требования:

- `Point` содержит `x/y`;
- одна функция вычисляет Manhattan distance до начала координат;
- declaration находится в header;
- definition — в `.c`;
- main создаёт несколько points и проверяет функцию через `assert`.

Сначала собери object files отдельно, затем link.

### Self-check

- нет warnings;
- умеешь показать object files;
- если временно удалить definition, понимаешь linker error;
- header имеет include guard.

Разбор: [`05-structs-modules.solution.md`](05-structs-modules.solution.md).

## Project slice — MiniKV v0

Теперь собери первую законченную версию MiniKV по [`project/SPEC.md`](project/SPEC.md).

Предлагаемая conceptual representation:

```text
Entry
  key buffer
  value buffer
  occupied/state

Store
  fixed array<Entry>
  current count / state
```

Ты самостоятельно выбираешь точные поля и API в рамках SPEC.

Обязательно добавь собственные `assert` tests из [`project/TESTS.md`](project/TESTS.md).

Пока не используй heap allocation.

## Exit check

Можешь ли ты объяснить путь:

```text
minikv.c -> minikv.o
main.c   -> main.o
          ↓
        linker
          ↓
       executable
```

и указать, какая часть является public contract?
