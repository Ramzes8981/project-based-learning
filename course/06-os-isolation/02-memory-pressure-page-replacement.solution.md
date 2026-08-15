# Разбор 6.2

FIFO с тремя frames можно вести queue order. Важно считать fault только когда requested page не resident.

Урок не требует memorization конкретного total faults — главное вручную поддерживать invariant:

```text
frames contain at most 3 resident pages
FIFO victim = oldest loaded among resident pages under this toy policy
```

LRU иногда принимает другое решение, потому что учитывает recent use, а не arrival time.
