# Разбор 2.5

После fork до redirection child наследует:

```text
0 -> terminal input
1 -> terminal output
2 -> terminal error
```

Shell child открывает `in.txt` как `in_fd`, `out.txt` как `out_fd`, затем:

```text
dup2(in_fd, 0)
dup2(out_fd, 1)
close(in_fd)
close(out_fd)
exec(...)
```

Parent descriptors не меняются.

Если `in_fd` случайно уже равен 0, корректный code должен учитывать semantics `dup2(fd, fd)` и cleanup без двойного close логической цели.
