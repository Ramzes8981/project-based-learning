# Разбор упражнения 1C.4

Pattern failure test:

```text
snapshot logical state
inject failure / invalid input
assert explicit failure
assert logical state == snapshot
run one normal operation
assert invariants
```

Последний normal operation важен: структура может выглядеть неизменённой, но скрытая corruption проявится только позже.
