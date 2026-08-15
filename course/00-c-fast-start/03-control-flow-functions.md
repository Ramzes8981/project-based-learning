# 0.3 — Управление, функции и границы ответственности

**Теория:** ~30 мин  
**Упражнение:** ~25 мин  
**Project slice:** ~20 мин  
**С телефона:** теория — да

← [`02-types-values.md`](02-types-values.md) · → [`04-arrays-strings.md`](04-arrays-strings.md)

## Цель

Быстро перенести уже знакомые programming concepts в C и заметить C-specific детали: truthiness, short-circuit, declaration/definition, pass-by-value и явные return codes.

## Prerequisite check

1. Чем функция отличается от вызова функции?
2. Что такое локальная область видимости?
3. Зачем функция может возвращать status вместо полезного значения?

## Инженерный контекст

Ты уже умеешь `if`, loops и functions в Python. Повторять основы программирования нет смысла. Но C заставляет яснее определять типы, границы функций и способы сообщения об ошибках.

## Условия

```c
if (x > 10) {
    /* ... */
} else {
    /* ... */
}
```

В C условие интерпретируется как integer-like truth value: `0` — false, ненулевое — true.

Для явных boolean values позже удобно использовать `bool` из `<stdbool.h>`.

## Short-circuit

Операторы `&&` и `||` вычисляются слева направо с short-circuit.

```c
if (denominator != 0 && numerator / denominator > 3) {
    /* ... */
}
```

Вторая часть не вычисляется, если первая уже делает всё выражение false. Это позволяет безопасно проверять precondition до опасной операции.

## Циклы

```c
for (int i = 0; i < 10; ++i) {
    /* ... */
}
```

```c
while (condition) {
    /* ... */
}
```

На этом этапе важнее не синтаксис, а invariants: что должно оставаться истинным на каждой итерации и почему цикл заканчивается.

## `switch`

```c
switch (command) {
case 1:
    /* ... */
    break;
case 2:
    /* ... */
    break;
default:
    /* ... */
    break;
}
```

Если `break` отсутствует, управление может перейти в следующий `case` (fallthrough). Иногда это намеренно, но случайный fallthrough — частый bug.

## Functions

```c
int max_int(int a, int b)
{
    return a > b ? a : b;
}
```

Здесь:

- `int` перед именем — return type;
- `a`, `b` — parameters;
- аргументы передаются **by value**.

Изменение `a` внутри функции не изменит исходную integer-переменную вызывающего кода.

Когда понадобится менять caller-owned state, в Module 1 введём pointer parameters.

## Declaration vs definition

Declaration сообщает компилятору, что сущность существует и каков её тип/интерфейс.

```c
int max_int(int a, int b);
```

Definition содержит реализацию:

```c
int max_int(int a, int b)
{
    return a > b ? a : b;
}
```

Эта разница станет важной при `.h/.c` разделении.

## Ошибки и return codes

В C нет единственного обязательного механизма ошибок вроде Python exceptions.

Для простой операции удобно вернуть status:

```c
enum Status {
    STATUS_OK = 0,
    STATUS_INVALID_INPUT = 1
};
```

Пока достаточно понять идею: API должен явно договориться, что означает return value.

## Causal questions

1. Почему `&&` полезен не только как логический оператор, но и как способ защитить вторую операцию precondition?
2. Почему функция, изменившая локальный параметр `int x`, не меняет integer у caller?
3. Чем случайный fallthrough в `switch` опаснее обычной опечатки?
4. Почему значение `-1` не является универсальным «кодом любой ошибки» для всех C API?

## Упражнение

Напиши функцию:

```text
classify_temperature(t)
```

которая возвращает один из нескольких integer status/categories по выбранным тобой диапазонам.

Требования:

- минимум 3 категории;
- диапазоны не должны пересекаться логически;
- main вызывает функцию на boundary values;
- никакого ввода от пользователя не нужно;
- добавь минимум 5 `assert` проверок.

Цель — потренировать function boundary и условия, а не сделать «приложение погоды».

### Self-check

- проверки покрывают границы диапазонов;
- функция детерминирована;
- нет global state;
- нет warnings.

Разбор: [`03-control-flow-functions.solution.md`](03-control-flow-functions.solution.md).

## Project slice

В MiniKV продумай операции как **поведение**, пока без окончательного API:

```text
insert/update
lookup
missing key
full store
```

Для каждой операции запиши:

- вход;
- успешный результат;
- возможную ошибку.

Это будущий API contract.

## Exit check

Объясни:

> Что именно в C передаётся by value и почему pointers позже меняют способ работы с caller-owned state?

Глубоко pointers знать ещё не нужно — важно увидеть проблему заранее.
