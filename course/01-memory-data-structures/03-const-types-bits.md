# 1.3 — Как безопасно считать размеры до работы с памятью

**Теория:** ~65 мин  
**Практика:** ~55 мин  
**С телефона:** теория — да; практика — ПК

← [`02-arrays-pointer-arithmetic.md`](02-arrays-pointer-arithmetic.md) · → [`03b-text-bytes-utf8.md`](03b-text-bytes-utf8.md)

## Проблема

Скоро программе понадобится место для `count` элементов:

```text
нужно bytes = count × bytes_per_element
```

Если само вычисление размера переполнится, следующая проверка границы уже будет опираться на неверное число.

## `size_t`: тип для размеров объектов

`sizeof` возвращает `size_t`. Это unsigned integer type, способный представлять размер любого отдельного объекта, который поддерживает implementation.

Он удобен для числа элементов и byte sizes. Но unsigned не означает «не может переполниться».

## Unsigned arithmetic wraps modulo

Для unsigned integer operations результат вычисляется modulo `2^N` для ширины типа. Поэтому слишком большое произведение может стать маленьким числом.

Нельзя сначала вычислить опасное произведение, а потом спрашивать «не слишком ли оно большое?».

## Проверка до умножения

```c
if (elem_size != 0 && count > SIZE_MAX / elem_size) {
    /* multiplication would not fit in size_t */
}

size_t bytes = count * elem_size;
```

`SIZE_MAX` доступен через стандартный `<stdint.h>` на C99+ implementations, предоставляющих этот macro.

## Signed overflow создаёт другую проблему

Для signed integer arithmetic нет общего правила «wrap как у unsigned».

Если результат signed addition/subtraction/multiplication выходит за представимый диапазон, стандарт C **не задаёт требуемого поведения программы**. Такая категория называется **неопределённым поведением (undefined behavior, UB)**.

Это важнее обычного «получится неправильное число»: compiler вправе оптимизировать, исходя из предположения, что корректная программа не выполняет UB.

Пока нужен один практический вывод:

```text
если signed result способен не поместиться
→ проверь границы ДО операции
```

В 1.6 мы расширим модель UB на invalid memory access, lifetime violations и debugging tools.

## Fixed-width integers — только когда ширина является контрактом

`uint32_t`/`int32_t` из `<stdint.h>` нужны, когда внешний формат данных действительно требует конкретную ширину. Не заменяй ими автоматически каждый `int`.

## Bit flags — короткий bridge

Иногда несколько независимых yes/no states удобно хранить в bits одного unsigned value:

```c
enum {
    FLAG_READ  = 1u << 0,
    FLAG_WRITE = 1u << 1
};
```

Проверка:

```c
if ((flags & FLAG_WRITE) != 0) {
    /* enabled */
}
```

Глубже bit representation вернётся тогда, когда мы начнём строить модель процессора.

## Практика

Напиши helper:

```c
int checked_array_bytes(size_t count, size_t elem_size, size_t *out);
```

Contract:

- `out == NULL` → failure;
- если product не помещается в `size_t` → failure, `*out` не менять;
- иначе записать product и вернуть success;
- `count == 0` или `elem_size == 0` корректно дают `0`.

Разбор: [`03-const-types-bits.solution.md`](03-const-types-bits.solution.md).

## Exit check

Почему overflow check должен происходить **до** multiplication и почему нельзя переносить unsigned-wrap mental model на signed arithmetic?