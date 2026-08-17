# 1.2 — Почему массив и указатель связаны, но не являются одним и тем же

**Теория:** ~65 мин  
**Практика:** ~60 мин  
**С телефона:** теория — да; практика — ПК

← [`01-addresses-pointers.md`](01-addresses-pointers.md) · → [`03-const-types-bits.md`](03-const-types-bits.md)

## Проблема

Мы уже проходили массив:

```c
int values[4] = {10, 20, 30, 40};
```

Теперь нужно понять, почему функция обычно получает массив вместе с отдельной длиной и почему выражения с array names часто выглядят как pointer operations.

## Элементы лежат подряд

Для массива элементы одного типа расположены последовательно.

```text
values[0]  values[1]  values[2]  values[3]
```

Адрес первого элемента:

```c
&values[0]
```

Во многих выражениях имя массива автоматически преобразуется в pointer на первый элемент. Это называют **array-to-pointer conversion**; не «массив становится pointer навсегда».

```c
int *p = values;
```

## Почему `p + 1` не значит «прибавить один byte»

Pointer arithmetic масштабируется размером типа, на который pointer указывает:

```c
p + 1
```

означает pointer к следующему `int` того же массива.

Поэтому:

```c
values[i]
```

и

```c
*(values + i)
```

описывают доступ к одному элементу при допустимом `i`.

## Граница и one-past pointer

Для массива из `N` элементов допустимо вычислить pointer **ровно за последним элементом** — one-past pointer:

```c
int *end = values + 4;
```

Он полезен как граница цикла, но разыменовывать `end` нельзя.

```text
[0] [1] [2] [3] | end
 ^               ^
 first           one-past
```

Pointer arithmetic имеет определённые правила внутри одного array object и его one-past boundary. Это не универсальная арифметика по всей памяти работающей программы.

## Почему функция теряет размер массива

Параметр вида:

```c
void print_all(int values[])
```

в function parameter context фактически описывает pointer parameter. Функция не получает встроенное число элементов. Поэтому честный API выглядит так:

```c
void print_all(const int *values, size_t count);
```

## BROKEN EXAMPLE — только для диагностики compiler warning

Следующий эксперимент намеренно показывает плохую mental model и **не является корректным образцом**:

```c
void bad_sizeof(int values[])
{
    printf("%zu\n", sizeof values);
}
```

С warning flags compiler обычно сообщает, что `sizeof` применяется к adjusted pointer parameter. После эксперимента удали этот код. Correct API передаёт `count` отдельно.

## Практика

Напиши:

```c
int sum_ints(const int *values, size_t count, int *out_sum);
```

Contract:

- `out_sum == NULL` → failure;
- `values == NULL` допустим только при `count == 0`;
- не читать ни одного элемента за `count`;
- пока считать, что сумма помещается в `int` — overflow разберём в следующем уроке.

Разбор: [`02-arrays-pointer-arithmetic.solution.md`](02-arrays-pointer-arithmetic.solution.md).

## Causal questions

1. Почему `values + 1` двигается к следующему `int`, а не к следующему byte?
2. Для чего можно вычислять one-past pointer, если его нельзя dereference?
3. Почему `sizeof` внутри array parameter не восстанавливает caller array length?

## Exit check

Ты не говоришь «array — это pointer». Ты можешь точно объяснить, **в каких выражениях** происходит conversion и что теряется на function boundary.