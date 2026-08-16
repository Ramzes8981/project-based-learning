# Module 1C — Checkpoint

**Время:** ~90 мин + доработка tests  
**С телефона:** conceptual part — да

← [`04-negative-testing-fuzzing.md`](04-negative-testing-fuzzing.md) · ↑ [`README`](README.md)

## Explain

1. unit vs integration vs system vs acceptance;
2. test oracle;
3. invariant vs example;
4. property vs regression;
5. fake/stub/mock/spy на уровне назначения;
6. dependency injection без framework;
7. negative testing;
8. fault injection;
9. fuzzing и его границы.

## Artifact gate

В одном уже завершённом проекте должно быть:

- классифицированные tests;
- минимум один invariant checker/property;
- минимум один regression test;
- минимум один negative/error path;
- README объясняет `make test`/`cargo test` и что именно эти tests не доказывают.

## Scenario

Server parser проходит 10 000 random inputs без crash. Можно ли объявить protocol implementation correct? Нет: нужны semantic oracles, state/resource checks и coverage meaningful valid/invalid structure.

## Gate

После модуля каждый новый bug должен по возможности оставлять после себя regression test, а каждый milestone — иметь test strategy раньше финального review.
