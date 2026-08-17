# Разбор 0.1

Минимальный корректный пример:

```c
#include <stdio.h>

int main(void)
{
    puts("hello");
    return 0;
}
```

Сборка:

```bash
cc -std=c17 -Wall -Wextra -Wpedantic hello.c -o hello
```

Ключевая проверка понимания: после изменения `hello.c` старый executable остаётся старым, пока ты не запустишь compiler снова.

Syntax error мешает получить новый executable; логическая ошибка может успешно скомпилироваться и проявиться только в поведении.