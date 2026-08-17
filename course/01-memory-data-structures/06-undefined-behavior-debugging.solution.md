# Разбор 1.6

Ожидаемые root causes:

- OOB: разыменован one-past/outside-array location; correct version ограничивает index `< count`.
- UAF: allocation lifetime закончился на `free`; correct version не использует borrowed pointers после owner release.
- signed overflow: математический результат не представим типом; correct version проверяет range **до** operation или меняет contract/type.

Не сравнивай только «crashed / did not crash». Sanitizer diagnostic и violated language/API contract — более сильное evidence.

Broken fixtures должны оставаться явно маркированными и не компилироваться как часть normal project target.