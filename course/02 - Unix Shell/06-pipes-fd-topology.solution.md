# Разбор 2.6

После setup:

```text
Child A:
  stdout -> pipe write
  close original pipe read
  close original pipe write after dup2

Child B:
  stdin -> pipe read
  close original pipe write
  close original pipe read after dup2

Parent:
  close pipe read
  close pipe write
  wait both children
```

Точные descriptor numbers временных pipe ends не важны; важна topology и отсутствие лишнего writer reference.
