# 1.2 — Arrays, pointers и pointer arithmetic

**Теория:** ~50 мин  
**Упражнение:** ~35 мин  
**Project slice:** ~30–45 мин  
**С телефона:** теория — да

← [`01-addresses-pointers.md`](01-addresses-pointers.md) · → [`03-const-types-bits.md`](03-const-types-bits.md)

## Цель

Понять связь массивов и pointers без ложного правила «array = pointer».

## Prerequisite check

1. Что хранит `int *p`?
2. Что делает `*p`?
3. Что было особенного с длиной array в Module 0?

## Array — не pointer

```c
int a[4] = {10, 20, 30, 40};
```

`a` — **array object** из четырёх `int`.

В большинстве expressions имя массива преобразуется (decays) в pointer на первый element:

```c
int *p = a;
```

эквивалентно по адресу первого элемента:

```c
int *p = &a[0];
```

Но сам array object не превращается в pointer как сущность.

Доказательство на уровне поведения:

```c
sizeof(a)
```

в scope настоящего массива даёт размер всего массива, а:

```c
sizeof(p)
```

даёт размер pointer object.

## Array parameter trap

```c
void f(int values[10])
```

в parameter list не передаёт в функцию «полный array object из 10 ints». Для большинства практических целей parameter adjusted to pointer type.

Поэтому функция должна получать length отдельно:

```c
void f(int values[], size_t count);
```

или эквивалентно:

```c
void f(int *values, size_t count);
```

Это объясняет, почему `sizeof(values)` внутри функции не даёт исходную array length.

## Pointer arithmetic

Если `p` указывает на element массива, `p + 1` указывает на следующий element, а не «на адрес + 1 byte».

```c
int *p = a;
printf("%d\n", *(p + 2));  // 30
```

Компилятор масштабирует шаг согласно типу pointed object.

Для valid array object разрешено формировать pointer на **one past the last element**, но dereference такого pointer недопустим.

```text
&a[0] ... &a[3]  -> valid elements
&a[4]            -> one-past pointer: можно сравнивать/использовать как boundary,
                    нельзя *dereference
```

## `a[i]` и pointer notation

На концептуальном уровне:

```c
a[i]
```

эквивалентно:

```c
*(a + i)
```

Это помогает понять array indexing, но не означает, что pointer notation всегда лучше читается.

## Pointer subtraction

Разность двух pointers в пределах одного array object может описывать расстояние в элементах. Результат имеет специальный signed type `ptrdiff_t`.

Не вычитай произвольные адреса unrelated objects и не строй логику на их «числовой близости».

## Strings снова

C string часто передаётся как `const char *`, то есть pointer на первый character sequence. Функции вроде `strlen` идут вперёд до terminator.

Отсюда два обязательных контракта:

- pointer должен адресовать доступную последовательность;
- в пределах доступной последовательности должен существовать `\0`.

## Causal questions

1. Почему фраза «array — это pointer» вводит в заблуждение?
2. Почему `sizeof` помогает увидеть разницу?
3. Зачем разрешён one-past pointer, если его нельзя dereference?
4. Почему `p + 1` для `int *` не означает «следующий byte»?

## Упражнение

Создай array из 6 integers.

1. Выведи элементы через indexing.
2. Выведи те же элементы через pointer traversal.
3. Вычисли address first element и one-past boundary.
4. Не dereference boundary.
5. Передай array в функцию вместе с explicit count и внутри сравни `sizeof(parameter)` с `sizeof(array)` у caller.

### Self-check

Ты должен суметь объяснить различие результатов `sizeof` без фразы «компилятор странный».

Разбор: [`02-arrays-pointer-arithmetic.solution.md`](02-arrays-pointer-arithmetic.solution.md).

## Project slice

В MiniKV убедись, что каждый API, работающий с external array/buffer, получает достаточную информацию о capacity/length. Не пытайся «восстановить» length через `sizeof(parameter)`.

## Exit check

Ответь: когда expression `a` превращается в pointer и почему это всё равно не делает type `int[4]` тем же самым, что `int *`?
