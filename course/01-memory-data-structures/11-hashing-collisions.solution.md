# Разбор 1.11

При capacity 8:

```text
A start 3 -> slot 3
B start 3 -> 3 busy -> slot 4
C start 4 -> 4 busy -> slot 5
D start 3 -> 3,4,5 busy -> slot 6
```

Если A удалить как `EMPTY`, lookup B, начав с slot 3, может остановиться слишком рано и сказать «B нет».

Если slot 3 — `TOMBSTONE`, lookup понимает, что probe chain мог продолжаться, и идёт дальше.

Safe stop обычно возможен на действительно `EMPTY` bucket, который никогда не был частью продолжающейся chain в текущей table state.
