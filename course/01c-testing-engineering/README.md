# Module 1C — Как проверять программы так, чтобы тесты ловили реальные поломки

**Оценка:** ~12–18 часов.  
**Prerequisite:** Modules 0–1; Rust examples optional.

До этого тесты были локальной привычкой проекта. Теперь строим инженерную модель: **что именно считается доказательством корректности и какой класс failure способен поймать конкретный test**.

## Уроки

1. [`01-test-levels-oracles.md`](01-test-levels-oracles.md) — **Откуда тест знает правильный ответ**.
2. [`02-invariants-properties-regressions.md`](02-invariants-properties-regressions.md) — **Как проверять правило для целого класса входов**.
3. [`03-testability-dependencies-doubles.md`](03-testability-dependencies-doubles.md) — **Как отделить логику от зависимости, которая мешает воспроизводимому тесту**.
4. [`04-negative-testing-fuzzing.md`](04-negative-testing-fuzzing.md) — **Почему неправильный input нужно генерировать намеренно**.
5. [`05-module-checkpoint.md`](05-module-checkpoint.md) — checkpoint.

## Важная граница

Здесь не используются как известные `fd`, socket, syscall, short I/O или `EINTR`. Такие examples появятся после Unix/network lessons. Сейчас testability объясняется на уже знакомых pure/data/allocator boundaries.