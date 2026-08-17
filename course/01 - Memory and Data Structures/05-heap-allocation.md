# 1.5 — Как программе попросить больше памяти и не потерять её

**Теория:** ~80 мин  
**Практика:** ~75 мин  
**С телефона:** теория — да; практика — ПК

← [`04-lifetime-ownership.md`](04-lifetime-ownership.md) · → [`06-undefined-behavior-debugging.md`](06-undefined-behavior-debugging.md)

## Проблема

MiniKV v0 упирался в фиксированное число records. Мы хотим размер, который выбирается во время выполнения и может изменяться.

Local fixed array этого не решает. Нужен механизм запросить storage у runtime и вернуть его позже.

## Dynamic allocation

В C стандартная библиотека предоставляет **динамическое выделение памяти (dynamic allocation)**:

- `malloc` — выделить block указанного размера;
- `calloc` — выделить место для элементов и zero-initialize bytes;
- `realloc` — изменить размер существующего allocation;
- `free` — закончить lifetime allocation.

Разговорно такую область storage часто называют **heap**, но стандарт C не требует конкретной heap implementation. Важно поведение API, а не картинка «stack сверху, heap снизу».

## `malloc`

```c
size_t count = 10;
if (count > SIZE_MAX / sizeof(int)) {
    /* reject */
}

int *items = malloc(count * sizeof *items);
if (items == NULL) {
    /* allocation failed */
}
```

Почему сначала checked arithmetic: маленький wrapped byte count опаснее честного failure.

## Кто освобождает

После успешного allocation должен существовать один понятный owner, ответственный за `free`.

```text
allocate
→ owner stores pointer
→ borrowers may use while live
→ owner free exactly once
→ no later access
```

Ошибки:

- забыть `free` → leak;
- `free` дважды → invalid;
- use after `free` → dangling access;
- потерять единственный owner pointer → allocation больше нельзя освободить.

## `realloc`: failure-safe pattern

`realloc` может:

- оставить block на месте;
- перенести data в новый block;
- вернуть `NULL` при failure, при этом исходный allocation остаётся owned caller-ом для non-zero requested size.

Поэтому не затирай единственный pointer сразу:

```c
void *tmp = realloc(items, new_bytes);
if (tmp == NULL) {
    /* items still owns the old allocation */
} else {
    items = tmp;
}
```

### Zero-size policy

Поведение `realloc(ptr, 0)` historically/platform-version-sensitive для teaching portability и легко создаёт двусмысленный ownership contract. В core мы **не используем его**. Если новый logical size равен zero, отдельной веткой вызывай `free` и устанавливай owner pointer в `NULL`.

## Pointer invalidation после успешного move

Если `realloc` перенёс block, pointers на старые elements больше нельзя использовать. Даже если числовой адрес «выглядит правдоподобно».

Это причина, почему внутренний pointer на `vector.items[3]` нельзя бездумно хранить через операцию роста.

## Cleanup on failure

Функция с несколькими allocations должна иметь понятный cleanup path. Часто в C полезен один cleanup label, если он уменьшает дублирование и делает ownership видимым.

## Практика

Реализуй helper, который создаёт dynamic array `int` заданного `count`, zero-initializes логические elements и возвращает success/failure через out-parameter. Требования:

- checked multiplication;
- `count == 0` имеет явный documented result;
- allocation failure не оставляет caller с мусорным pointer;
- owner освобождает resource ровно один раз.

Разбор: [`05-heap-allocation.solution.md`](05-heap-allocation.solution.md).

## Exit check

Объясни, почему `items = realloc(items, ...)` может потерять allocation при failure и почему pointers на elements могут стать invalid после success.