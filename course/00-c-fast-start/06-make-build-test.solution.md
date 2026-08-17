# Разбор 0.6

Минимальный pattern:

```make
CC ?= cc
CFLAGS := -std=c17 -Wall -Wextra -Wpedantic

app: main.o store.o
	$(CC) main.o store.o -o app

main.o: main.c store.h
	$(CC) $(CFLAGS) -c main.c -o main.o

store.o: store.c store.h
	$(CC) $(CFLAGS) -c store.c -o store.o

.PHONY: test clean

test: app
	./app --self-test

clean:
	rm -f app main.o store.o
```

Точные target names проекта могут отличаться. Существенный invariant: изменение `store.h` должно заставить пересобрать object files, которые включают этот header.