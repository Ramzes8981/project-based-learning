# 1.6 — Почему некоторые ошибки C нельзя понимать как обычный runtime exception

**Теория:** ~75 мин  
**Лаб:** ~80 мин  
**С телефона:** теория — да; diagnostics — ПК

← [`05-heap-allocation.md`](05-heap-allocation.md) · → [`07-dynamic-array.md`](07-dynamic-array.md)

## Проблема

Новичок часто ожидает Python mental model:

```text
ошибка → runtime замечает → понятное исключение
```

C не обещает это для многих нарушений language contract. Код может упасть, «работать», испортить соседние данные или вести себя иначе после optimization.

## Undefined behavior

Если стандарт C не накладывает требований на поведение программы после определённого нарушения, это называют **неопределённым поведением (undefined behavior, UB)**.

Примеры, которые уже можно понять из предыдущих уроков:

- dereference dangling pointer;
- access за bounds массива;
- use after `free`;
- double `free`;
- signed integer overflow;
- некоторые invalid shifts и другие rule violations.

UB не означает «случайный exception». Compiler имеет право оптимизировать исходя из предположения, что корректная программа не выполняет UB.

## BROKEN EXAMPLE — out-of-bounds

```c
int a[2] = {1, 2};
printf("%d\n", a[2]);
```

`a + 2` можно вычислить как one-past pointer, но `a[2]` его разыменовывает. Это broken diagnostic fixture, не образец.

## BROKEN EXAMPLE — use after free

```c
int *p = malloc(sizeof *p);
if (p != NULL) {
    *p = 42;
    free(p);
    printf("%d\n", *p);
}
```

После `free` allocation lifetime закончился. То, что старые bytes иногда ещё видны, не возвращает validity.

## Sanitizers

Для controlled course fixtures используем инструменты compiler-а:

```bash
cc -std=c17 -Wall -Wextra -Wpedantic \
  -fsanitize=address,undefined -fno-omit-frame-pointer \
  broken.c -o broken
```

AddressSanitizer помогает ловить многие invalid memory accesses; UndefinedBehaviorSanitizer — некоторые UB categories. Они не являются доказательством отсутствия всех bugs.

## Valgrind — optional second lens

На поддерживаемой Linux-среде Valgrind может быть полезен для leaks/invalid accesses, но course gate не требует два одинаковых инструмента на каждое упражнение.

## Debugging workflow

```text
1. минимизировать reproduction
2. сформулировать hypothesis
3. включить подходящий diagnostic tool
4. получить evidence
5. исправить root cause
6. добавить regression test
7. снова запустить diagnostics
```

## Практика

Создай **отдельный каталог `broken-fixtures/`**, не смешивая его с correct project code. По одному воспроизведи:

- out-of-bounds;
- use-after-free;
- signed overflow.

Каждый файл начинается комментарием `BROKEN EXAMPLE`. Затем исправь каждый bug в отдельной correct версии и объясни нарушенный contract.

Разбор: [`06-undefined-behavior-debugging.solution.md`](06-undefined-behavior-debugging.solution.md).

## Exit check

Почему «у меня не упало» не является evidence, что UB отсутствует?