# 1.4 — Почему правильный адрес позже может стать недействительным

**Теория:** ~70 мин  
**Практика:** ~55 мин  
**С телефона:** теория — да; практика — ПК

← [`03b-text-bytes-utf8.md`](03b-text-bytes-utf8.md) · → [`05-heap-allocation.md`](05-heap-allocation.md)

## Проблема

Non-null pointer недостаточно. Он мог когда-то указывать на допустимый object, но object уже перестал существовать.

Значит, pointer safety зависит не только от адреса, но и от **времени существования объекта**.

## Время жизни объекта

Интервал выполнения программы, в котором объект существует и к нему допустимо обращаться, будем называть **временем жизни (lifetime)**.

Пример:

```c
int *bad(void)
{
    int local = 42;
    return &local;
}
```

`local` существует только во время выполнения этого вызова функции. После return его lifetime закончился. Возвращённый pointer сохраняет старое числовое значение, но это уже не делает объект живым.

## Call stack — ментальная модель, не магическая зона безопасности

Типичные local variables автоматического storage duration связаны со **стеком вызовов (call stack)**: каждый активный function call имеет frame с частью локального состояния; при возврате этот frame больше не принадлежит вызову.

Для курса достаточно модели:

```text
call function
→ frame exists
→ locals live
→ return
→ those locals' lifetime ends
```

Не выводи из неё точный физический layout: compiler optimizations могут хранить конкретное значение в register или вообще убрать объект. Language lifetime contract важнее красивой картинки стека.

## Dangling pointer

Pointer, который больше не указывает на живой object, называют **висячим указателем (dangling pointer)**.

```text
pointer value still exists
object lifetime ended
→ dereference is invalid
```

## Ownership как инженерный договор в C

Как только API создаёт ресурс, чья жизнь не совпадает автоматически с одним коротким function call, появляется вопрос: **кто отвечает за окончание его lifetime?**

Такой договор ответственности будем называть **владением (ownership)**:

- кто создаёт resource;
- кто обязан закончить его lifetime;
- кто только временно пользуется им;
- может ли reference пережить owner.

Это ещё не Rust ownership type system. В C ownership — convention/API contract.

## Borrowed pointer

Если функция получает pointer только на время вызова и не забирает ответственность за resource, будем говорить, что она **заимствует (borrows)** доступ.

```c
void print_entry(const Entry *entry);
```

`const` здесь помогает выразить «эта функция не должна менять `Entry` через этот pointer»; это не продлевает lifetime.

## Сценарии для аудита

Для каждого pointer задавай два независимых вопроса:

```text
1. На какой object он должен указывать?
2. Жив ли этот object во всех местах использования pointer?
```

Только потом спрашивай bounds/mutability.

## Практика

Классифицируй A–E и объясни **причину**, не только verdict:

A. Pointer на caller variable используется только пока caller variable ещё жив.  
B. Функция возвращает address local automatic variable.  
C. Pointer на элемент массива сохраняется, массив продолжает существовать и не меняет storage.  
D. Pointer передан read-only helper только на время helper call.  
E. Pointer сохранён в global/static variable, а исходный local object уже вышел из lifetime.

Разбор: [`04-lifetime-ownership.solution.md`](04-lifetime-ownership.solution.md).

## Exit check

Почему `p != NULL` ничего не говорит о том, закончился ли lifetime target object?