# Разбор упражнения 0.4

Один вариант integer search:

```c
#include <stddef.h>

size_t linear_search(const int values[], size_t count, int target)
{
    for (size_t i = 0; i < count; ++i) {
        if (values[i] == target) {
            return i;
        }
    }

    return count;
}
```

Контракт:

```text
result < count  -> элемент найден по этому индексу
result == count -> not found
```

Такой вариант не требует сужать `size_t` index до `int`. Sentinel `count` безопасен, потому что валидные индексы массива длины `count` находятся только в диапазоне `0..count-1`.

Для strings идея та же, но сравнение содержимого:

```c
strcmp(values[i], target) == 0
```

При этом `values[i]` и `target` обязаны быть валидными null-terminated C strings. `strcmp` не получает отдельную длину и не может сам исправить broken string contract.

Ключевой invariant цикла:

> перед началом итерации `i` элементы `0..i-1` уже проверены и не содержат более раннего совпадения.

`count == 0` естественно приводит к нулю итераций и возврату `0`; для пустого массива это одновременно значение `count`, то есть корректный `not found` sentinel.
