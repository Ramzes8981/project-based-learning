# Разбор упражнения 0.6

Сначала dependency graph:

```text
point.h ─┬─> point.o ─┐
         │             ├─> app
         └─> main.o  ─┘
point.c ───> point.o
main.c  ───> main.o
```

Один корректный учебный вариант:

```make
CC = cc
CFLAGS = -std=c17 -Wall -Wextra -Wpedantic -g

app: main.o point.o
	$(CC) main.o point.o -o $@

main.o: main.c point.h
	$(CC) $(CFLAGS) -c main.c -o $@

point.o: point.c point.h
	$(CC) $(CFLAGS) -c point.c -o $@

test: app
	./app

clean:
	rm -f main.o point.o app

.PHONY: test clean
```

Проверка incremental behavior:

1. первый `make` создаёт оба `.o` и executable;
2. второй `make` без изменений ничего не компилирует;
3. изменение `point.c` требует `point.o` + relink;
4. изменение `point.h` делает устаревшими `point.o` и `main.o`, потому что оба source-файла зависят от header;
5. `make clean` удаляет только generated artifacts.

Если твой Makefile устроен иначе, это нормально: оценивается корректность dependency graph и воспроизводимые команды, а не совпадение строк с этим примером.

Для MiniKV готовый Makefile здесь намеренно не приведён: состав targets зависит от твоей структуры проекта и является частью milestone.
