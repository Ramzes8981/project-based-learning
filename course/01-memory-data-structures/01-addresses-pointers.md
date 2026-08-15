# 1.1 — Адреса и указатели

**Теория:** ~45 мин  
**Упражнение:** ~30 мин  
**Project slice:** ~45 мин  
**С телефона:** теория — да

← [`README`](README.md) · → [`02-arrays-pointer-arithmetic.md`](02-arrays-pointer-arithmetic.md)

## Цель

Понять pointer как отдельное значение, которое хранит адрес объекта, и научиться безопасно передавать caller-owned state в функцию.

## Prerequisite check

1. Почему обычный parameter `int x` не меняет integer у caller?
2. Что такое C object на уровне Module 0?
3. Почему MiniKV сейчас неудобно изменять через чистый pass-by-value?

## Инженерный контекст

Реальная systems-программа постоянно передаёт ссылки на buffers, structs, device state, sockets metadata и другие объекты. В C этот механизм выражается pointers.

Pointer не является «магической ссылкой». Это значение определённого pointer type, которое должно указывать на объект, допустимый для соответствующей операции.

## Object, address, pointer

```c
int x = 42;
int *p = &x;
```

Модель:

```text
x: int object
address(x): некоторое место в памяти
p: int* object/value, содержащий адрес x
```

`&x` — address-of: получить адрес `x`.

`*p` в expression — dereference: обратиться к объекту, на который указывает `p`.

```c
*p = 100;
```

меняет `x`, если `p == &x` и lifetime `x` ещё продолжается.

## Pointer type важен

`int *` и `double *` — разные pointer types. Тип говорит компилятору, объект какого типа ожидается за адресом и как интерпретировать операции вроде dereference/pointer arithmetic.

## Pointer тоже передаётся by value

Это важный mental model.

```c
void set_zero(int *p)
{
    *p = 0;
}
```

При вызове:

```c
int x = 5;
set_zero(&x);
```

функция получает **копию pointer value**. Но обе копии адресуют тот же `x`, поэтому `*p = 0` меняет caller-owned object.

C не имеет отдельной скрытой pass-by-reference семантики здесь: pointer value всё ещё передан by value.

## `NULL`

`NULL` используется как null pointer constant/convention: pointer намеренно не указывает на объект.

```c
int *p = NULL;
```

Dereference `NULL` недопустим. На типичной ОС это часто приводит к crash, но язык C не обещает тебе «красивый exception».

Проверка:

```c
if (p != NULL) {
    printf("%d\n", *p);
}
```

имеет смысл только если весь остальной контракт pointer тоже корректен: non-NULL ещё не гарантирует, что pointer указывает на живой object нужного типа.

## Pointer parameters и mutation

```c
typedef struct {
    int count;
} Counter;

void increment(Counter *counter)
{
    counter->count += 1;
}
```

`counter->count` — удобная форма `(*counter).count`.

Именно такой стиль позволит MiniKV API изменять один Store object, а не копировать его целиком.

## Causal questions

1. Если pointer передаётся by value, почему функция всё равно может менять caller object?
2. Почему `p != NULL` недостаточно, чтобы dereference был гарантированно безопасен?
3. Чем `p` отличается от `*p`?
4. Почему pointer type важен, если адрес на машине выглядит просто числом?

## Упражнение — swap

Напиши:

```c
void swap_int(int *a, int *b);
```

Требования:

- меняет значения двух caller variables;
- работает, если `a` и `b` указывают на разные integers;
- отдельно проверь случай `swap_int(&x, &x)` и объясни результат;
- не dereference null pointers: контракт функции должен быть явно записан.

### Self-check

После:

```c
int x = 10;
int y = 20;
swap_int(&x, &y);
```

получается `x == 20`, `y == 10`.

Разбор: [`01-addresses-pointers.solution.md`](01-addresses-pointers.solution.md).

## Project slice — MiniKV API становится pointer-based

Возьми Module 0 MiniKV и выбери функции, которые меняют `Store`.

Перепроектируй их так, чтобы они принимали address одного Store object, а не требовали копировать всю структуру.

Для каждого pointer parameter запиши:

```text
что он адресует?
может ли быть NULL?
функция только читает или меняет объект?
кто отвечает за lifetime объекта?
```

Пока Store всё ещё fixed-capacity и живёт без heap allocation.

## Типовые ошибки

- `int *p; *p = 3;` без назначения валидного адреса;
- перепутать `p` и `*p`;
- передать address локального объекта куда-то, где он переживёт lifetime;
- предположить, что любой non-NULL pointer валиден.

## Exit check

Нарисуй `x`, `p = &x` и вызов `set_zero(p)` как три уровня: object → address → pointer copy. Если можешь объяснить mutation без слова «магия», урок закрыт.
