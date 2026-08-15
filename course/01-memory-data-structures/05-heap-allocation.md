# 1.5 — Heap allocation: `malloc`, `calloc`, `realloc`, `free`

**Теория:** ~60 мин  
**Упражнение:** ~45 мин  
**Project slice:** ~60–90 мин  
**С телефона:** теория — да

← [`04-lifetime-ownership.md`](04-lifetime-ownership.md) · → [`06-undefined-behavior-debugging.md`](06-undefined-behavior-debugging.md)

## Цель

Уметь выделять dynamic storage, обрабатывать allocation failure и освобождать memory ровно один раз согласно ownership contract.

## Зачем heap

Fixed array Module 0 имеет lifetime/size, заданные программой заранее.

Dynamic allocation позволяет во время выполнения запросить storage нужного размера и самостоятельно решить, когда его освобождать.

В стандартной C library основные функции объявлены в `<stdlib.h>`.

## `malloc`

```c
int *values = malloc(count * sizeof(*values));
```

Если allocation успешна, возвращается pointer на storage, достаточно выровненный для подходящих object types.

Если неуспешна — `NULL`.

`malloc` **не инициализирует bytes нулями**.

Правило style:

```c
sizeof(*values)
```

обычно устойчивее к изменению типа, чем дублировать `sizeof(int)`.

## Проверка overflow размера

Выражение:

```c
count * sizeof(*values)
```

само может overflow `size_t`, прежде чем `malloc` увидит размер.

Перед allocation больших/внешне контролируемых counts нужен guard:

```text
count <= SIZE_MAX / element_size
```

Позже это станет security-critical в network parsing.

## `calloc`

```c
int *values = calloc(count, sizeof(*values));
```

выделяет storage для массива и zero-initializes bytes.

Не считай «all zero bytes» универсальным способом получить любое возможное semantic zero для любой экзотической структуры/representation; для наших обычных integer arrays это предсказуемо полезно.

## `free`

```c
free(values);
values = NULL;
```

`free` завершает lifetime allocated storage. Любые другие pointers на ту же allocation становятся dangling.

Присвоить **одну локальную копию** pointer в `NULL` полезно против случайного повторного использования именно этой переменной, но не чинит aliases.

## `realloc`

```c
void *realloc(void *ptr, size_t new_size);
```

может:

- расширить allocation на месте;
- переместить её;
- вернуть новый pointer;
- вернуть `NULL` при failure, оставив старую allocation валидной для ненулевого `new_size` по обычному контракту.

Поэтому опасно:

```c
values = realloc(values, new_size);
```

Если failure → потерян единственный pointer на old allocation.

Безопаснее:

```c
int *tmp = realloc(values, new_count * sizeof(*values));
if (tmp == NULL) {
    /* old values still owned here */
} else {
    values = tmp;
}
```

Отдельные corner cases `new_size == 0` не используем как часть core API: проще иметь явный `free` path.

## Allocation ownership

После успешного `malloc` должен существовать один понятный owner responsibility:

```text
allocate
  ↓
own resource
  ↓
use / transfer ownership
  ↓
free exactly once
```

«Где-то потом free» — плохой контракт.

## Cleanup on error

Если function успела выделить несколько resources, а затем шаг 4 падает, error path должен освободить уже приобретённые ресурсы.

В C часто используется single cleanup section:

```text
acquire A
acquire B
acquire C
if failure -> cleanup acquired resources in reverse/known order
```

Конкретный `goto cleanup` в C может быть вполне разумным инструментом, если уменьшает duplicated cleanup paths. Мы не вводим запрет «goto всегда зло».

## Causal questions

1. Почему `free(p); p = NULL;` не делает безопасными другие aliases?
2. Почему прямое `p = realloc(p, ...)` может создать leak?
3. Почему allocation size overflow — отдельный bug от `malloc == NULL`?
4. Где должен быть описан owner каждой allocation?

## Упражнение

Напиши программу, которая:

1. получает фиксированный `size_t n` из constant/test;
2. проверяет multiplication overflow;
3. выделяет `n` integers;
4. заполняет значениями;
5. увеличивает capacity через safe `realloc` pattern;
6. проверяет старые значения;
7. освобождает storage.

Разбор: [`05-heap-allocation.solution.md`](05-heap-allocation.solution.md).

## Project slice — Hash Table storage становится dynamic

Открой [`project/hash-table/SPEC.md`](project/hash-table/SPEC.md).

Перенеси table storage с fixed array на heap allocation, **но пока не добавляй hashing**. Сохрани линейный lookup.

Обязательные вопросы:

- кто owner entries allocation?
- что делает constructor/init при allocation failure?
- что делает destroy?
- какие fields нужно сбросить после destroy, чтобы object state был понятен?

## Exit check

Нарисуй success и failure paths для `create -> use -> destroy`, включая `malloc == NULL`.
