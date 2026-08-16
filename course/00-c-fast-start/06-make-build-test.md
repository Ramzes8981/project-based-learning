# 0.6 — Make: воспроизводимая сборка и тестовый target

**Теория:** ~45 мин  
**Упражнение:** ~40–60 мин  
**Project slice:** ~45–75 мин  
**С телефона:** теория — да; практика — ПК

← [`05-structs-modules.md`](05-structs-modules.md) · → [`07-module-checkpoint.md`](07-module-checkpoint.md)

## Цель

Перестать собирать многофайловый C-проект длинными командами вручную и научиться описывать **dependency graph сборки** через простой `Makefile`.

После урока ты должен понимать:

```text
source/header changed
        ↓
какие object files стали устаревшими?
        ↓
что нужно пересобрать?
        ↓
что можно оставить как есть?
```

## Prerequisite check

1. Чем `.c` отличается от `.o`?
2. Что делает linker?
3. Если изменился `point.h`, какие translation units, включающие его, потенциально надо пересобрать?
4. Почему ручная команда сборки становится источником ошибок, когда файлов становится больше?

## Инженерный контекст

Для программы из одного файла достаточно:

```bash
cc hello.c -o hello
```

Но MiniKV уже естественно разделяется на несколько частей:

```text
main.c
minikv.c
minikv.h
tests.c
```

Если каждый раз вручную вспоминать правильные compiler flags и порядок команд, быстро возникают проблемы:

- забыли warning flag;
- забыли пересобрать один object file;
- тесты собираются иначе, чем main program;
- команда у другого человека отличается;
- после изменения header используется старый `.o`.

Build system нужен не ради «магии автоматизации», а ради **воспроизводимого описания зависимостей**.

## Главная модель Make

Правило Make имеет форму:

```make
TARGET: PREREQUISITES
	RECIPE
```

Читаем так:

> Чтобы получить `TARGET`, нужны `PREREQUISITES`. Если target отсутствует или устарел относительно prerequisite, выполни recipe.

Важно: перед recipe традиционно нужен **TAB**, а не набор пробелов.

## Маленький пример

Продолжим проект `point` из прошлого урока.

Файлы:

```text
main.c
point.c
point.h
```

Dependency graph:

```text
point.h ─┬─> point.o ─┐
         │             ├─> app
         └─> main.o  ─┘
point.c ───> point.o
main.c  ───> main.o
```

Один простой `Makefile`:

```make
CC = cc
CFLAGS = -std=c17 -Wall -Wextra -Wpedantic -g

app: main.o point.o
	$(CC) main.o point.o -o app

main.o: main.c point.h
	$(CC) $(CFLAGS) -c main.c -o main.o

point.o: point.c point.h
	$(CC) $(CFLAGS) -c point.c -o point.o

clean:
	rm -f main.o point.o app

.PHONY: clean
```

Это не «идеальный production Makefile». Он намеренно явный, чтобы сначала увидеть dependency graph.

## Что происходит при `make`

Make обычно выбирает первый target как default goal. Здесь это `app`.

Он проверяет prerequisites:

```text
app needs main.o + point.o
```

Если object files отсутствуют, Make ищет правила, которые умеют их построить.

Получается:

```text
compile main.c -> main.o
compile point.c -> point.o
link main.o + point.o -> app
```

Если сразу выполнить `make` ещё раз без изменений, корректно описанная сборка не должна без причины компилировать всё заново.

## Почему header — prerequisite object file

`main.c` может включать:

```c
#include "point.h"
```

После preprocessing содержимое header влияет на translation unit `main.c`.

Следовательно, изменение `point.h` потенциально делает `main.o` устаревшим.

Поэтому:

```make
main.o: main.c point.h
```

— не косметика, а dependency statement.

## Variables

Вместо повторения compiler command можно использовать переменные:

```make
CC = cc
CFLAGS = -std=c17 -Wall -Wextra -Wpedantic -g
```

Использование:

```make
$(CC) $(CFLAGS) ...
```

На этом этапе не нужны сложные Make functions или generated dependency files.

## Automatic variable `$@`

В recipe `$@` означает имя текущего target.

Например:

```make
point.o: point.c point.h
	$(CC) $(CFLAGS) -c point.c -o $@
```

Здесь `$@` превращается в `point.o`.

Это уже полезно, но не надо превращать первый Makefile в code golf.

## `.PHONY`

Targets вроде:

```text
clean
test
```

часто не являются реальными файлами.

Если случайно появится файл с именем `clean`, Make может решить, что target уже существует. Поэтому такие команды объявляют:

```make
.PHONY: clean test
```

## `test` target

Пусть учебный executable сам выполняет `assert` checks.

Можно добавить:

```make
test: app
	./app

.PHONY: test clean
```

Тогда интерфейс проекта становится простым:

```bash
make
make test
make clean
```

Позже test target сможет собирать отдельный test executable. Сейчас важна стабильная команда, а не конкретная test framework.

## Exit status и Make

Recipe command с ненулевым exit status обычно делает target failed.

Это полезно для тестов:

```text
assert failed / test process returns non-zero
        ↓
make test fails
```

Автоматизация должна сохранять информацию о неуспехе, а не печатать «ошибка была, но target зелёный».

## Incremental rebuild experiment

Собери `point`:

```bash
make
```

Затем снова:

```bash
make
```

Без изменений compile commands не должны повторяться.

Теперь измени только `point.c` и снова запусти `make`.

Ожидаемая зависимость:

```text
point.c changed
↓
point.o rebuild
↓
app relink
```

`main.o` не обязан пересобираться.

После изменения `point.h` обычно устареют **оба** object files, если оба translation units включают этот header.

## Causal questions

1. Почему Makefile — это в первую очередь dependency graph, а не список shell commands?
2. Почему `point.h` должен быть prerequisite для object files, которые его включают?
3. Зачем `test` должен возвращать ненулевой status при провале?
4. Чем `make clean && make` отличается от нормальной incremental build и почему не стоит постоянно использовать clean build как костыль?
5. Почему `.PHONY` относится к semantics target, а не к стилю оформления?

## Упражнение — Makefile для `point`

Для проекта прошлого урока создай Makefile самостоятельно.

Требования:

- default target собирает executable;
- `.c` компилируются в отдельные `.o`;
- зависимости от `point.h` описаны явно;
- используются canonical warning flags курса;
- есть `test`;
- есть `clean`;
- `test` и `clean` объявлены `.PHONY`;
- повторный `make` без изменений не пересобирает всё;
- изменение `point.c` пересобирает только нужный object + relink;
- изменение `point.h` пересобирает все зависящие object files.

Не копируй пример механически: сначала нарисуй dependency graph своего набора файлов.

Разбор: [`06-make-build-test.solution.md`](06-make-build-test.solution.md).

## Project slice — MiniKV build contract

Теперь создай **собственный** `Makefile` в [`project/`](project/).

К концу Module 0 должны работать:

```bash
make
make test
make clean
```

Минимальные требования:

- `make` собирает основную/учебную программу MiniKV;
- `make test` запускает твои проверки из `TESTS.md`;
- `make clean` удаляет generated build artifacts, но не source/spec/docs;
- warnings включены через единый набор flags;
- dependency graph не требует полного rebuild после изменения одного `.c`, если остальные translation units от него не зависят.

Курс **не даёт готовый MiniKV Makefile**, потому что выбор файлов и public API — часть твоего проектирования.

В [`project/README.md`](project/README.md) зафиксируй реальные build/test commands.

## Типовые ошибки

### `missing separator`

Частая причина — recipe начинается spaces вместо TAB.

### Make всегда пересобирает всё

Проверь, что targets действительно являются файлами, а dependencies описаны корректно. Не добавляй `.PHONY` обычным object/executable targets.

### Header изменился, но object не пересобрался

Скорее всего header не указан prerequisite соответствующего object target.

### `make test` всегда успешен

Проверь exit status test executable/script. Test runner не должен скрывать failure.

## Exit check

Нарисуй dependency graph MiniKV и объясни:

> Если изменить только implementation `.c`, что должно пересобраться и почему?

Если ответ выводится из зависимостей, а не из запоминания команд — можно идти к checkpoint.
