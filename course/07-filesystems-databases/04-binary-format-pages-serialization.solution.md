# Разбор 7.4

Хороший answer задаёт explicit layout, например:

```text
offset  size  field
0       4     magic
4       2     version LE
6       2     flags LE
8       4     record_count LE
12      4     payload_size LE
16      16    reserved zeros
```

Главное — decoder не зависит от padding C struct и reject unknown magic/version before interpreting later bytes.
