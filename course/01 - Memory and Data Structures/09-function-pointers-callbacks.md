# 1.9 — Как передать программе само действие

**Теория:** ~55 мин  
**Практика:** ~55 мин  
**С телефона:** теория — да; практика — ПК

← [`08-linked-structures.md`](08-linked-structures.md) · → [`10-complexity-invariants-binary-search.md`](10-complexity-invariants-binary-search.md)

## Проблема

Мы хотим одну reusable operation, но поведение для каждого элемента должно задаваться caller-ом:

```text
walk all values
→ for each value do caller-selected action
```

Копировать весь loop для print/sum/validation неудобно.

## Function pointer

У функции есть тип callable contract. C позволяет хранить pointer на функцию и вызывать её через этот pointer.

```c
typedef void (*IntVisitor)(int value, void *ctx);
```

`IntVisitor` — function pointer type: получает `int`, opaque context pointer и ничего не возвращает.

```c
void visit_all(const int *items, size_t count,
               IntVisitor visitor, void *ctx)
{
    if (visitor == NULL) {
        return;
    }
    for (size_t i = 0; i < count; ++i) {
        visitor(items[i], ctx);
    }
}
```

Функцию, переданную для последующего вызова, часто называют **callback**.

## Зачем `void *ctx`

Callback нередко нужен state. Глобальная variable создаёт скрытую зависимость. `ctx` позволяет caller передать context явно.

Типовая схема:

```text
caller owns context object
visit_all borrows pointer during call
callback casts it back according to agreed contract
```

Lifetime context должен покрывать все callback calls.

## Неправильная mental model

> «Function pointer — pointer на обычные data bytes функции, которые можно безопасно трактовать как `void *`».

Не делай такой вывод. C различает function pointers и object pointers; portability rules не позволяют бездумно смешивать их.

## Практика

Используя `visit_all`, реализуй callback, который считает количество values больше threshold, где threshold и counter лежат в context struct.

Разбор: [`09-function-pointers-callbacks.solution.md`](09-function-pointers-callbacks.solution.md).

## Exit check

Какой lifetime contract нужен между `ctx` и callback, и почему global state здесь хуже явного context?