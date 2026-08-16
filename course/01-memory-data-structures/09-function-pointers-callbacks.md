# 1.9 — Function pointers, callbacks и context pointers

**Теория:** ~60 мин  
**Упражнение:** ~45 мин  
**С телефона:** теория — да

← [`08-linked-structures.md`](08-linked-structures.md) · → [`10-complexity-invariants-binary-search.md`](10-complexity-invariants-binary-search.md)

## Цель

Понять function pointer как значение, которое обозначает функцию с конкретной сигнатурой, и безопасно использовать callback без скрытого ownership/lifetime контракта.

## Зачем это systems-программисту

Callbacks появляются в signal/event APIs, сортировке, FUSE, parsers, generic libraries и plugin-like interfaces. Если впервые увидеть callback table уже внутри filesystem API, сложность будет искусственной.

## Базовый синтаксис

```c
int compare_int(int a, int b)
{
    return (a > b) - (a < b);
}

int (*cmp)(int, int) = compare_int;
int r = cmp(10, 20);
```

Читаем декларацию изнутри: `cmp` — pointer на function, которая принимает два `int` и возвращает `int`.

Через `typedef` API читается лучше:

```c
typedef int (*IntCompare)(int, int);
```

## Signature — часть контракта

Нельзя безопасно подставить function с несовместимой сигнатурой и надеяться, что ABI «как-нибудь совпадёт». Типы параметров и return type должны соответствовать ожидаемому callback type.

## Callback

Callback — функция, переданная другому коду для вызова позже/внутри алгоритма.

```c
size_t count_if(const int *values, size_t n,
                int (*predicate)(int));
```

Алгоритм знает **когда вызвать**, caller предоставляет **что именно проверить**.

## Context pointer

Одного callback иногда недостаточно: ему нужны настройки/state.

Распространённая C-модель:

```c
typedef bool (*Predicate)(int value, void *ctx);
```

`void *ctx` — untyped pointer. Он не делает runtime type-checking. Обе стороны обязаны договориться, какой объект там лежит и сколько он живёт.

Пример contract:

```text
count_if borrows ctx only for duration of call
callback must not store ctx after return
```

Это связь function pointers с предыдущим lifetime уроком.

## Callback table

Системные API часто группируют callbacks:

```c
typedef struct {
    int (*open)(const char *path, void *ctx);
    int (*read)(const char *path, void *buf, size_t n, void *ctx);
} Operations;
```

Такой struct — таблица поведения. Позже именно эта mental model поможет понять FUSE operations.

## Не путать с code generation

Function pointer — адрес/идентификатор существующей функции в текущем executable/process model. Мы не создаём машинный код на лету.

## Error/safety checklist

- callback signature совпадает;
- `ctx` указывает на живой объект;
- mutability `ctx` соответствует contract;
- callback не сохраняется дольше, чем живут function/module/context;
- callback не вызывается после destroy/teardown;
- функция документирует, вызывает callback синхронно или может сохранить его на будущее.

## Упражнение

Реализуй маленький `count_if` для массива `int`.

1. callback без context: `is_positive`;
2. затем version с `void *ctx`, где context задаёт threshold;
3. tests: пустой массив, все подходят, никто не подходит, boundary threshold.

Не используй глобальную переменную для threshold: смысл упражнения — увидеть, зачем context передаётся явно.

Разбор: [`09-function-pointers-callbacks.solution.md`](09-function-pointers-callbacks.solution.md).

## Causal questions

1. Почему `void *` не означает «тип не важен»?
2. Что изменится, если API сохранит callback и `ctx` для вызова через минуту?
3. Почему callback-table — удобный интерфейс для ОС/FS framework?
4. Какие lifetime вопросы возникают у context pointer?

## Exit check

Ты должен уметь прочитать `int (*fn)(const char *, void *)` и сформулировать lifetime contract для второго аргумента.
