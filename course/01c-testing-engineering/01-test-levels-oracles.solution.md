# Разбор упражнения 1C.1

Пример для Hash Table:

```text
SET alpha=one; GET alpha -> one
```

Это acceptance/public-behavior test. Он не должен проверять, в каком bucket лежит `alpha`, иначе станет brittle implementation test.

Отдельный unit test probe helper может проверять bucket sequence — там internal representation как раз является предметом теста.
