# Разбор 4.1

Ключевой skeleton lab:

```text
page = sysconf(_SC_PAGESIZE)
length = page * N
p = mmap(...)
if p == MAP_FAILED -> error
write to selected offsets < length
inspect /proc/self/maps
munmap(p, length)
```

Не хардкодь page size 4096 как закон. На многих x86-64 Linux это typical base page, но API должен сообщать реальное значение среды.
