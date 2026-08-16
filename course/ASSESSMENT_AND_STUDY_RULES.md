# Правила обучения и проверки

Курс рассчитан на устойчивые ~6–8 часов/неделю. Скорость не является gate: understanding/project evidence важнее календаря.

## Learning cycle

```text
concept
→ explain
→ focused exercise
→ project application when relevant
→ debug/test
→ transfer scenario
```

Не нужно «закончить всю теорию» до проектов.

## Один большой milestone одновременно

- **Core milestone** — обязателен;
- **Guided lab** — только заданный scope;
- **Stretch** — optional.

## Lesson readiness

Prerequisite gap ремонтируется локально: короткое повторение + одно упражнение, затем возвращаемся. Не перепроходим модуль целиком.

## Lesson exit

- Explain model своими словами;
- Apply в exercise;
- project slice, если lesson project-oriented;
- ответить на новый scenario/edge case.

## Module gate: пять доказательств

**Explain** — модели без копирования определения.  
**Build** — milestone/lab required scope работает.  
**Transfer** — новая feature/scenario.  
**Debug** — реальный bug: symptom → hypothesis → evidence → root cause → fix → regression.  
**Review** — representation, ownership/state, complexity/resources, failures, tests, security assumptions, 10× trade-offs.

## Knowledge states

`Seen → Explain → Apply → Transfer`.

## Test model

### Public scenario

`project/TESTS.md`: known behavior/edge cases, часть specification.

### Executable public infrastructure

Course может дать black-box harness, fixture, controlled target, protocol client/load generator. Она не должна содержать solution проверяемого компонента.

### Student tests

Обязательны всегда. Для API-flexible C structures именно student suite реализует `make test` по public scenarios/invariants.

### Review/unseen

Дополнительные cases проверяют generalization. Они не изменяют SPEC задним числом; только комбинируют/напрягают уже заданный contract.

## AI policy

AI — teacher/reviewer/debugger, не implementation engine:

```text
symptom/question
→ hypothesis/diagnostic
→ hint
→ pseudocode
→ stronger local hint
→ full solution only after learning value is exhausted
```

Milestone code пишет ученик.

## Python infrastructure

Допустим для test harness, fixtures, load generation/analysis, failure-injection on disposable local artifacts. Если tooling itself — learning target, его пишет ученик.

## Consolidation

После milestone или ~4–6 недель можно выделить session/week на refactor, tests, review или отдых без «учебного долга».

## Artifact after milestone

- student source/build files;
- tests;
- learner README;
- transfer feature;
- debugging story;
- engineering review;
- meaningful Git history.
