# Module 1C — Testing Engineering

**Статус:** CORE BRIDGE  
**Оценка:** ~12–18 часов  
**Цель:** превратить тестирование из набора `assert` в инженерную систему доказательств и регрессий для последующих systems-проектов.

## Уроки

1. [`01-test-levels-oracles.md`](01-test-levels-oracles.md) — unit/integration/system/acceptance и test oracle.
2. [`02-invariants-properties-regressions.md`](02-invariants-properties-regressions.md) — invariants, properties, regression tests.
3. [`03-testability-dependencies-doubles.md`](03-testability-dependencies-doubles.md) — boundaries, dependency injection, fakes/stubs/mocks.
4. [`04-negative-testing-fuzzing.md`](04-negative-testing-fuzzing.md) — malformed input, fault injection, fuzzing intuition.
5. [`05-module-checkpoint.md`](05-module-checkpoint.md) — gate перед Unix/Shell.

## Почему отдельный bridge

Дальше каждый milestone должен иметь не только happy-path output, но и воспроизводимую проверку failure paths, invariants, resource cleanup и regression bugs. Этот модуль даёт общий язык один раз, чтобы не переобъяснять его в каждом проекте.

## Артефакт

Выбери Vector, Hash Table или Rust MiniKV и доработай **только test strategy**, не business logic: классифицируй существующие tests, добавь минимум один regression и один negative/error-path case.
