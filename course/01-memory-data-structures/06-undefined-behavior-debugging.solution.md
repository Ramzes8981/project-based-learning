# Разбор 1.6

Ожидаемые классы:

- запись `p[n]` в allocation на `n` элементов — heap-buffer-overflow;
- чтение/запись после `free(p)` — heap-use-after-free;
- `INT_MAX + 1` в signed `int` — signed integer overflow / UB.

Sanitizer message нужно читать сверху вниз до первого места **вашего** кода, которое объясняет invalid access, а не просто копировать последнюю строку stack trace.

После исправления добавь regression test, который воспроизводил старый input/path и теперь проходит.
