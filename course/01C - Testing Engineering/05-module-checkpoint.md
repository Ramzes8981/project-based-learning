# 1C.5 — Checkpoint: какой failure способен поймать твой тест

**Время:** ~90–150 мин · **С телефона:** review — да

← [`04-negative-testing-fuzzing.md`](04-negative-testing-fuzzing.md) · ↑ [`README`](README.md)

## Explain

Для каждого собственного test-а выбери один и ответь:

```text
boundary?
oracle?
какой failure class ловит?
какой не ловит?
какая hidden dependency может сделать flaky?
```

## Required transfer

Возьми bug из Vector/Hash Table/Rust MiniKV и преврати его debugging story в permanent regression:

```text
minimal reproducer
→ root cause
→ regression oracle/property
→ clean rerun
```

## Gate

Ты готов к Unix module, если не используешь слова unit/integration/fuzzing как badges, а можешь объяснить, какое конкретное evidence каждый test даёт.