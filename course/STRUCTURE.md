# Структура курса

Репозиторий — единое учебное пространство: теория, упражнения, решения маленьких упражнений, project contracts и student project code живут рядом.

## Learning cycle

```text
concept/problem
↓
self-contained theory
↓
questions/scenario
↓
exercise
↓
project slice (если concept уже нужен milestone)
↓
debug/test/review
```

Не каждый теоретический CS lesson обязан искусственно менять текущий project. Consolidation lesson может завершаться transfer exercise/exit check, если project slice неестественен.

## Два типа lesson

### Project lesson

Новая concept напрямую нужна активному milestone. Обычно содержит theory → exercise → project slice → debugging → exit check.

### Theory / consolidation lesson

Фундаментальная тема (например P/NP, probability, часть algorithms), которой нужно собственное закрепление. Обязательны цель, самостоятельная теория, causal/situational questions, exercise/transfer и exit check; project slice добавляется только если органичен.

## Файловая модель

```text
course/<module>/
├── README.md
├── 01-topic.md
├── 01-topic.solution.md      # разбор небольшого exercise, если нужен
├── ...
└── project/
    ├── README.md             # learner-owned design/build/debug log
    ├── SPEC.md
    ├── ACCEPTANCE.md
    ├── TESTS.md              # known scenarios, not necessarily executable
    ├── HINTS.md
    ├── tests/                # executable public fixtures/harness when useful
    └── tools/                # infrastructure, not milestone solution
```

Если в модуле несколько проектов, каждый имеет собственный directory с этим contract.

## Где писать решения

Small lesson solution можно хранить рядом:

```text
03-topic.my.c
03-topic.my.rs
```

Reference `.solution.md` открывается после самостоятельной попытки.

Milestone implementation создаётся **в его project-folder**, без отдельного глобального `work/`.

## Три слоя проверки

### 1. `TESTS.md` — public scenarios

Человек заранее знает requirements/edge cases. Это часть specification.

### 2. Executable public tests/tools

Присутствуют, когда внешний contract стабилен и harness не навязывает внутренний design: Shell CLI, Tiny16 files, network protocol, DB format, debugger target fixtures.

Для Vector/Hash Table/Allocator signatures выбирает ученик, поэтому он сам строит unit suite по public scenarios.

### 3. Review/unseen tests

Дополнительные edge cases/operation sequences проверяют transfer и не дают свести project к hardcode public suite.

## Внешние материалы

Required path не ломается без internet. External URL допустим в optional/reference documents, но обязательный lesson должен объяснять concept и достаточный API contract локально.
