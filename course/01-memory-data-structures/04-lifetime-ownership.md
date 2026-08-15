# 1.4 — Lifetime и ownership в C

**Теория:** ~55 мин  
**Упражнение:** ~40 мин  
**Project slice:** ~40 мин  
**С телефона:** да

← [`03-const-types-bits.md`](03-const-types-bits.md) · → [`05-heap-allocation.md`](05-heap-allocation.md)

## Цель

Научиться задавать два вопроса для каждого pointer:

1. Жив ли объект, на который он указывает?
2. Кто отвечает за освобождение/завершение владения ресурсом?

## Storage duration и lifetime

Рассмотрим:

```c
int *bad(void)
{
    int x = 42;
    return &x;
}
```

`x` имеет automatic storage duration. Его lifetime заканчивается при выходе из block/function invocation.

Возвращённый pointer value может физически содержать старый адрес, но pointed object уже не существует. Dereference такого dangling pointer — invalid behavior/undefined behavior.

## Stack как рабочая модель

Обычно automatic locals находятся в stack frame, но язык C формально описывает lifetime/storage duration, а не обещает конкретное физическое размещение каждой переменной.

Для нашей Linux/x86-64 практики stack-frame модель очень полезна, но не путай её с полной спецификацией C.

```text
call function
   ↓
создаётся execution context/frame
   ↓
automatic locals живут во время вызова
   ↓
return
   ↓
их lifetime заканчивается
```

Оптимизатор может хранить некоторые locals только в registers или вообще устранить их. Семантика lifetime от этого не меняется.

## Ownership — convention, а не встроенный механизм C

C не имеет borrow checker. Поэтому команда должна сама определить правила.

Полезные слова курса:

- **owner** — компонент, отвечающий за lifetime и cleanup ресурса;
- **borrowed pointer** — временный доступ к объекту без передачи ownership;
- **transfer ownership** — ответственность за cleanup переходит другому компоненту.

Это не ключевые слова C. Это инженерный контракт.

## Borrowed pointer

```c
size_t count_positive(const int *values, size_t count);
```

Функция получает borrowed read-only access. Caller остаётся owner массива и должен гарантировать его lifetime на время вызова.

## Escaping pointer

Если function сохраняет pointer куда-то глобально/в long-lived struct, простой «borrow на время вызова» уже недостаточен. Нужно договориться, что pointed object проживёт достаточно долго или ownership будет передан/скопирован.

## String ownership

Особенно часто ошибки возникают со strings:

```c
const char *name = ...;
```

Нужно знать:

- string literal?
- pointer в caller buffer?
- heap allocation?
- static storage?
- можно ли менять bytes?
- кто освобождает?

Тип `char *` сам по себе не отвечает на эти вопросы.

## Causal questions

1. Почему адрес может выглядеть «нормальным», хотя pointer уже dangling?
2. Почему stack/heap — полезная, но недостаточная классификация ownership?
3. Что должен обещать caller, передавая borrowed pointer?
4. Почему сохранение borrowed pointer в глобальную переменную меняет требования к lifetime?

## Упражнение — lifetime audit

Для каждого scenario определи owner, lifetime и bug:

A. функция возвращает address local int;
B. caller передаёт address своего local struct в функцию, которая только читает его до return;
C. функция сохраняет pointer на caller string в global state, а caller затем заканчивает scope;
D. pointer на string literal передан как `char *` и код пытается изменить символ.

Напиши ответы текстом, затем создай два маленьких C-примера: один safe borrow и один намеренно dangling scenario, который **не нужно dereference**, а только объяснить.

Разбор: [`04-lifetime-ownership.solution.md`](04-lifetime-ownership.solution.md).

## Project slice — ownership contract MiniKV

До heap allocation создай в Hash Table project README секцию:

```text
Ownership v1
- кто владеет Store?
- Store копирует key/value или хранит borrowed pointers?
- что возвращает GET: copy или borrowed pointer?
- как долго валиден результат GET?
```

Выбери один контракт и обоснуй. Для учебного hash table обычно проще, если table владеет собственными копиями keys/values, но решение и детали должны быть осознанными.

## Exit check

Если видишь pointer field в struct, первым вопросом должно стать не «как его dereference», а «кто владеет pointed object и сколько он живёт?».
