# Разбор 4.4

Хороший claim выглядит примерно так:

> На массиве N элементов, build `-O2`, одном и том же host, 30 runs после warm-up, sequential traversal имел median X и p95 Y, а shuffled traversal — median A/p95 B. Hypothesis: shuffled pattern ухудшает locality/cache reuse.

Это всё ещё не universal truth для любого hardware/input, но вывод проверяем и привязан к evidence.
