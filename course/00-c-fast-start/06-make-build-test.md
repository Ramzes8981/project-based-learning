# 0.6 — Как перестать вручную повторять команды сборки и проверки

**Теория:** ~40 мин  
**Практика/project:** ~75 мин  
**С телефона:** теория — да; практика — ПК

← [`05-structs-modules.md`](05-structs-modules.md) · → [`07-module-checkpoint.md`](07-module-checkpoint.md)

## Проблема

У многофайловой программы уже несколько команд:

```text
compile main.c
compile store.c
link results
run tests
```

Ручное повторение ненадёжно: легко забыть warning flags или проверить старый executable.

## Интуиция

Нужен файл с воспроизводимыми правилами «что из чего строится». В этом курсе используем `make` и `Makefile`.

## Минимальная mental model

```text
target: prerequisites
<TAB> command
```

Пример:

```make
CC ?= cc
CFLAGS := -std=c17 -Wall -Wextra -Wpedantic

app: main.o math_ops.o
	$(CC) main.o math_ops.o -o app

main.o: main.c math_ops.h
	$(CC) $(CFLAGS) -c main.c -o main.o

math_ops.o: math_ops.c math_ops.h
	$(CC) $(CFLAGS) -c math_ops.c -o math_ops.o

clean:
	rm -f app main.o math_ops.o
```

`make` сравнивает prerequisites и targets и выполняет нужные recipes.

## Тест как наблюдаемый контракт

На этом этапе не строим testing framework. Достаточно сделать команду, которая:

1. собирает актуальную программу;
2. запускает небольшой deterministic test;
3. возвращает non-zero status при несоответствии.

Например отдельный `test_store.c` может вызывать функции store напрямую.

## Почему это инженерная тема

Воспроизводимая команда важнее IDE-кнопки:

```text
make clean
make
make test
```

Её одинаково понимают человек, CI и будущий ты.

## Неправильная mental model

> «Make нужен только большим проектам».

Наоборот, маленький проект — безопасное место научиться build dependency до того, как ручная сборка станет сложной.

## Практика

1. Добавь Makefile в Module 0 project.
2. `make` должен собирать executable без warning.
3. `make test` должен запускать project tests.
4. `make clean` удаляет generated build artifacts.
5. Измени header и посмотри, какие `.o` пересобираются.

Разбор: [`06-make-build-test.solution.md`](06-make-build-test.solution.md).

## Project slice

Теперь доведи MiniKV до поведения из [`project/ACCEPTANCE.md`](project/ACCEPTANCE.md). Не добавляй dynamic memory, hashing или другие механизмы из будущего.

## Exit check

Почему build rule должен зависеть от header, если сам `.c` не менялся?