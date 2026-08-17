# Разбор 2.1

Главная функция, которую стоит выделить самостоятельно, — `write_all(fd, buf, len)`.

Псевдокод:

```text
written = 0
while written < len:
    n = write(...)
    if n > 0 -> written += n
    if n == -1 && EINTR -> continue
    otherwise -> error
```

Для copy loop:

```text
while true:
    n = read(src, buffer)
    n > 0 -> write_all(dst, first n bytes)
    n == 0 -> EOF/success
    n < 0 && EINTR -> retry read
    otherwise -> error
```

Ключевой review — cleanup всех уже открытых descriptors на каждом failure path.
