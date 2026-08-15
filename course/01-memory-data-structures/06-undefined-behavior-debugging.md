# 1.6 — Undefined behavior и debugging memory bugs

**Теория:** ~55 мин  
**Lab:** ~60 мин  
**Project slice:** ~30–45 мин  
**С телефона:** теория — да; lab — ПК

← [`05-heap-allocation.md`](05-heap-allocation.md) · → [`07-dynamic-array.md`](07-dynamic-array.md)

## Цель

Перестать интерпретировать memory bug как «программа иногда странно падает» и научиться классифицировать UB через compiler warnings, sanitizers и debugger.

## Что такое undefined behavior

Для некоторых нарушений стандарт C не задаёт допустимый результат вообще.

Это не означает «результат случайный, но обычно понятный». Компилятор имеет право оптимизировать исходя из предположения, что UB не происходит.

Примеры:

- out-of-bounds access;
- dereference dangling/invalid pointer;
- use-after-free;
- double free через library contract;
- signed integer overflow;
- некоторые invalid shifts;
- чтение некоторых uninitialized values.

## Почему «у меня работает» ничего не доказывает

UB может:

- не проявляться в debug build;
- ломаться только с `-O2`;
- зависеть от input/layout;
- повреждать соседнее state и падать намного позже.

Поэтому correctness нельзя проверять одним happy-path запуском.

## Compiler warnings

Базовые flags курса:

```bash
-Wall -Wextra -Wpedantic
```

Warnings — первая линия, но они не находят все runtime memory bugs.

## AddressSanitizer

```bash
cc -std=c17 -Wall -Wextra -Wpedantic -g \
  -fsanitize=address,undefined -fno-omit-frame-pointer \
  bug.c -o bug
```

ASan хорошо ловит многие:

- heap/stack out-of-bounds;
- use-after-free;
- some lifetime errors;
- leaks в поддерживаемых конфигурациях.

UBSan диагностирует ряд undefined operations.

Sanitizer — diagnostic tool, не proof отсутствия bugs.

## GDB минимальный workflow

```bash
gdb ./program
```

Полезные commands:

```text
run
break function_name
next
step
print variable
backtrace
continue
```

Главная цель пока — научиться отвечать «где именно observable failure?» и «какое состояние привело сюда?».

## Seeded bug

```c
#include <stdlib.h>

int main(void)
{
    int *p = malloc(sizeof(*p));
    if (p == NULL) {
        return 1;
    }

    *p = 10;
    free(p);
    return *p;
}
```

Bug — use-after-free. Даже если process однажды вернул `10`, behavior не становится допустимым.

## Debugging ladder

```text
1. воспроизвести
2. минимизировать
3. прочитать warning/sanitizer report
4. сформулировать hypothesis
5. проверить state/stack
6. исправить root cause
7. добавить regression test
```

## Causal questions

1. Почему UB не равно «runtime exception»?
2. Почему optimizer может сделать UB более заметным?
3. Почему sanitizer-clean run не является доказательством полной safety?
4. Зачем после bugfix нужен regression test?

## Lab

Создай три маленьких намеренно сломанных программы:

- out-of-bounds heap write;
- use-after-free;
- signed overflow.

Для каждой:

1. предскажи defect class;
2. запусти normal build;
3. запусти sanitizer build;
4. запиши, какое evidence указывает на root cause;
5. исправь;
6. повтори тест.

Не нужно делать опасный exploit; цель — диагностика controlled local code.

Разбор классов ошибок: [`06-undefined-behavior-debugging.solution.md`](06-undefined-behavior-debugging.solution.md).

## Project slice

Запусти текущий dynamic MiniKV/Hash Table scaffold под ASan+UBSan.

Исправь все известные reports до следующего урока. Если reports нет, специально создай отдельную учебную ветку/маленький bug и проверь, что toolchain действительно ловит проблему.

## Exit check

Ты должен уметь написать debugging story: symptom → evidence → hypothesis → root cause → regression test.
