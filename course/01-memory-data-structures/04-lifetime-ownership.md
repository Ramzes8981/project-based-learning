# 1.4 — Lifetime и ownership в C

**Теория:** ~60 мин  
**Упражнение:** ~40 мин  
**Project slice:** ~40 мин  
**С телефона:** да

← [`03-const-types-bits.md`](03-const-types-bits.md) · → [`05-heap-allocation.md`](05-heap-allocation.md)

## Цель

Для каждого pointer уметь отвечать:

1. Какой объект он обозначает?
2. Жив ли этот объект сейчас?
3. Кто отвечает за cleanup?
4. Разрешено ли через этот pointer менять объект?
5. Может ли pointer пережить текущий вызов/область видимости?

## Lifetime важнее числового адреса

```c
int *bad(void)
{
    int x = 42;
    return &x;
}
```

`x` имеет automatic storage duration. При выходе из вызова функции lifetime объекта заканчивается.

Критическая модель курса:

> После окончания lifetime объекта pointer на него больше не является пригодной ссылкой на этот объект. Нельзя строить корректность на том, что его числовые биты «всё ещё похожи на старый адрес».

Dereference такого dangling pointer — undefined behavior. Но проблема начинается раньше dereference: сам contract уже потерян, потому что pointed object больше не существует.

## Почему «stack address ещё там» — плохая mental model

Физические bytes могут временно не измениться, stack area может быть переиспользована следующим вызовом, optimizations могут вообще изменить размещение. C описывает lifetime объектов, а не обещает сохранность старого содержимого stack slot.

Полезная рабочая схема:

```text
call
↓
automatic object begins lifetime
↓
borrowed pointers могут ссылаться на него
↓
return/end of block
↓
lifetime ends
↓
старые pointers больше не дают валидный доступ к объекту
```

## Ownership — инженерный контракт

C не имеет встроенного borrow checker. Поэтому мы вводим явные термины:

- **owner** — компонент, отвечающий за lifetime и cleanup ресурса;
- **borrow** — временный доступ без передачи ownership;
- **ownership transfer** — ответственность за cleanup переходит другой стороне;
- **shared read-only borrow** — несколько наблюдателей без mutation;
- **mutable access** — изменение объекта, требующее более строгого reasoning об aliasing.

Это не ключевые слова C, но без такого словаря сложные проекты быстро становятся неразбираемыми.

## Borrowed pointer

```c
size_t count_positive(const int *values, size_t count);
```

Функция не становится owner массива. Caller гарантирует, что область `values[0..count)` доступна всё время вызова. `const` дополнительно обещает, что эта функция не будет менять элементы через данный pointer.

## Escaping pointer

Если функция сохраняет pointer в global/static state или в long-lived struct, borrow больше не ограничен временем вызова. Значит, нужен новый контракт:

- object проживёт дольше сохранённого pointer;
- либо данные копируются;
- либо ownership передаётся;
- либо хранение pointer запрещено.

## Heap не равен ownership

`malloc` создаёт объект с allocated storage duration, но сам факт «лежит в heap» не говорит, кто обязан вызвать `free`.

```text
storage location != ownership policy
```

Один модуль может выделить память и передать ownership другому. Или owner может временно дать borrowed pointer десятку функций.

## String ownership

Для `const char *name` всегда выясняй:

- literal со static storage?
- caller-owned buffer?
- heap allocation?
- часть более крупного объекта?
- null-terminated ли последовательность?
- как долго валиден pointer?

Один тип `const char *` не кодирует всё это.

## Типичные bugs

### Return local address

Lifetime заканчивается раньше пользователя pointer.

### Store borrowed pointer too long

Container сохранил pointer на caller buffer, caller завершил scope/reallocated buffer — container держит dangling pointer.

### Double ownership

Два компонента считают себя владельцами и оба вызывают `free`.

### Lost ownership

Последний owner pointer перезаписан до `free` → leak.

## Упражнение — lifetime audit

Для сценариев A–E запиши: object, owner, borrower, момент окончания lifetime, bug/fix.

A. функция возвращает address local `int`;
B. caller передаёт address local struct функции, которая только читает его до return;
C. функция сохраняет pointer на caller string глобально, caller завершает scope;
D. heap buffer передан функции с контрактом ownership transfer;
E. два struct fields указывают на один heap buffer, но destructor каждого пытается `free` его.

Затем создай **safe** пример borrow. Намеренно dangling pointer можно продемонстрировать только текстом/через sanitizer-friendly отдельный experiment; не превращай UB в «проверку, что иногда работает».

Разбор: [`04-lifetime-ownership.solution.md`](04-lifetime-ownership.solution.md).

## Project slice — ownership contract Hash Table

В [`project/hash-table/README.md`](project/hash-table/README.md) запиши:

```text
who owns table storage?
who owns key/value bytes?
does insert copy or borrow?
what does get return?
how long is returned pointer/reference valid?
what invalidates it (update/resize/destroy)?
```

Для первого milestone рекомендуется table-owned copy keys/values: это проще для lifetime reasoning, но exact API выбираешь сам.

## Exit check

Если видишь pointer field, ты должен сначала спросить «какой объект, чей lifetime и чей cleanup?», а уже потом думать о `*` и `->`.
