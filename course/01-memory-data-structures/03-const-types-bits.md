# 1.3 — Как безопасно считать размеры до работы с памятью

**Теория:** ~60 мин  
**Практика:** ~55 мин  
**С телефона:** теория — да; практика — ПК

← [`02-arrays-pointer-arithmetic.md`](02-arrays-pointer-arithmetic.md) · → [`03b-text-bytes-utf8.md`](03b-text-bytes-utf8.md)

## Проблема

Скоро мы попросим runtime выделить место для `count` элементов:

```text
нужно bytes = count × bytes_per_element
```

Если само вычисление размера переполнится, следующая проверка границы уже будет опираться на неверное число.

## `size_t`: тип для размеров объектов

`sizeof` возвращает `size_t`. Это unsigned integer type, способный представлять размер любого отдельного объекта, который поддерживает implementation.

Он удобен для:

- числа элементов;
- byte sizes;
- индексов, когда отрицательное значение не имеет смысла.

Но unsigned не означает «не может переполниться».

## Unsigned arithmetic wraps modulo

Для unsigned integer operations результат вычисляется modulo `2^N` для ширины типа. Поэтому слишком большое произведение может стать маленьким числом.

Нельзя сначала вычислить опасное произведение, а потом спрашивать «не слишком ли оно большое?».

## Проверка до умножения

Для `count * elem_size`:

```c
if (elem_size != 0 && count > SIZE_MAX / elem_size) {
    /* multiplication would not fit in size_t */
}
```

Только после этой проверки можно вычислять:

```c
size_t bytes = count * elem_size;
```

`SIZE_MAX` объявлен через стандартные headers (`<stdint.h>` предоставляет его на типичных C implementations; также доступны limits/macros через standard headers в зависимости от нужного типа).

## Signed integer overflow

Для обычных signed integer types арифметика **не** имеет общего правила «тихо wrap как unsigned». Выход результата за представимый диапазон для signed addition/subtraction/multiplication относится к некорректным операциям языка; формальный термин **undefined behavior** будет введён в 1.6.

До 1.6 правило простое: если диапазон данных способен переполнить signed result, проверяй границы до операции или выбирай другой representation/contract.

## Fixed-width integers — только когда важна ширина

`uint32_t`/`int32_t` из `<stdint.h>` нужны, когда binary format/protocol требует конкретную ширину. Не заменяй ими автоматически каждый `int`.

Сейчас достаточно понимать причину: «32 bits» должно быть частью внешнего contract, а не случайной особенностью host `int`.

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

Глубже bit representation вернётся в architecture module; сейчас не нужен длинный detour.

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

Почему overflow check должен происходить **до** multiplication?