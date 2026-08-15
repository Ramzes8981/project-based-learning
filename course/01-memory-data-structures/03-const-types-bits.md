# 1.3 — `const`, `size_t`, fixed-width integers, `bool` и bit masks

**Теория:** ~45 мин  
**Упражнение:** ~35 мин  
**Project slice:** ~30 мин  
**С телефона:** да

← [`02-arrays-pointer-arithmetic.md`](02-arrays-pointer-arithmetic.md) · → [`04-lifetime-ownership.md`](04-lifetime-ownership.md)

## Цель

Научиться выражать намерение API типами и освоить битовые операции до Unix flags, binary formats и networking.

## `const`

```c
void print_value(const int *p);
```

означает: через `p` функция не должна изменять pointed `int`.

Это читается как pointer to const int.

```c
int *const p = &x;
```

— const pointer: сам pointer value нельзя переназначить, но pointed object можно менять.

```c
const int *const p = &x;
```

— оба ограничения.

Для public API особенно важен первый вариант: read-only borrowed data обозначается `const T *`, когда функция только наблюдает.

`const` — compile-time contract aid, а не security boundary.

## `size_t`

`size_t` — unsigned integer type, предназначенный для размеров объектов и результатов `sizeof`.

Используй его для array lengths/capacities, когда значения по смыслу неотрицательны и совместимы с memory sizes.

Но помни unsigned pitfalls: выражение `size_t i = 0; --i;` не становится `-1`, а wraps к большому unsigned value.

## `<stdint.h>`

Когда нужен integer **конкретной ширины**, полезны типы:

```c
uint8_t
uint16_t
uint32_t
uint64_t
int32_t
```

Они существуют на реализациях, где соответствующая exact-width type поддерживается.

Для network/file formats ширина часто является частью protocol contract, поэтому `uint32_t` уместнее неопределённого по ширине `unsigned long`.

## `bool`

В C17:

```c
#include <stdbool.h>

bool ready = true;
```

Это делает intent понятнее, чем использовать случайный `int` для логического state.

## Bits

Основные операции:

```text
&   bitwise AND
|   bitwise OR
^   bitwise XOR
~   bitwise NOT
<<  left shift
>>  right shift
```

Не путай `&` как address-of в unary context и `&` как bitwise AND в binary expression: значение зависит от синтаксического контекста.

## Masks

Допустим, у нас четыре flags:

```c
#define FLAG_READ   (1u << 0)
#define FLAG_WRITE  (1u << 1)
#define FLAG_ADMIN  (1u << 2)
```

Включить:

```c
flags |= FLAG_WRITE;
```

Проверить:

```c
if ((flags & FLAG_WRITE) != 0) {
    /* enabled */
}
```

Выключить:

```c
flags &= ~FLAG_WRITE;
```

Это позже встретится в `termios`, permissions, binary headers и protocol flags.

## Shift edge cases

Shift может иметь undefined/implementation-sensitive corner cases, особенно с signed values, отрицательными operands и shift count вне ширины type.

Учебное правило: для masks используй подходящий unsigned type и проверяй диапазон shift count.

## Causal questions

1. Что обещает `const int *p`, а чего не обещает?
2. Почему `size_t` удобен для length, но обратный цикл `for (size_t i = n - 1; i >= 0; --i)` опасен?
3. Почему protocol field лучше описать `uint32_t`, если спецификация требует ровно 32 bits?
4. Чем logical `&&` отличается от bitwise `&`?

## Упражнение

Смоделируй permissions тремя bits.

Напиши маленькие функции:

- enable flag;
- disable flag;
- check flag.

Проверь combinations через `assert`.

### Self-check

- используются unsigned masks;
- функции не меняют read-only input без причины;
- каждая операция объяснима на уровне bits.

Разбор: [`03-const-types-bits.solution.md`](03-const-types-bits.solution.md).

## Project slice

Пересмотри MiniKV API:

- read-only operations должны по возможности принимать `const Store *`;
- sizes/capacities — `size_t`;
- status/state — `enum`/`bool` вместо magic integers, где это улучшает контракт.

Не переписывай код ради «модных типов»: каждое изменение должно иметь объяснимую семантику.

## Exit check

Сможешь ли ты по declaration функции понять, собирается ли она менять Store и какого типа length она ожидает?
