# Module 0 — C Fast Start

**Цель:** быстро стать функциональным в C и начать первый реальный проект без отдельного «семестра синтаксиса».

**Оценка:** 12–18 часов.  
**Активный проект:** `MiniKV v0` — fixed-capacity key/value store с линейным поиском.

## Уроки

1. [`01-source-build-run.md`](01-source-build-run.md) — от исходника до процесса.
2. [`02-types-values.md`](02-types-values.md) — типы, размеры и представление значений.
3. [`03-control-flow-functions.md`](03-control-flow-functions.md) — C-синтаксис управления и функции.
4. [`04-arrays-strings.md`](04-arrays-strings.md) — массивы, строки, границы, линейный поиск.
5. [`05-structs-modules.md`](05-structs-modules.md) — `struct`, `enum`, `.h/.c`, linker и API preconditions.
6. [`06-make-build-test.md`](06-make-build-test.md) — dependency graph, Make, `make test`, incremental build.
7. [`07-module-checkpoint.md`](07-module-checkpoint.md) — проверка Module 0.

## Проект

Перед первым project slice прочитай [`project/SPEC.md`](project/SPEC.md), затем веди собственный [`project/README.md`](project/README.md). По мере уроков возвращайся к проекту и расширяй реализацию **в этой же папке**.

Проектный каталог содержит:

```text
project/
├── README.md       # твои design/build/debugging notes
├── SPEC.md         # обязательное поведение
├── ACCEPTANCE.md   # gate проекта
├── TESTS.md        # известные заранее test scenarios
└── HINTS.md        # подсказки по уровням
```

Исходный C-код, headers, Makefile и тестовые executable/files создаёшь ты по мере прохождения уроков.

Курс **не** даёт готовый MiniKV-код или готовый MiniKV Makefile.

## Что пока сознательно не изучаем

- pointers в глубину;
- `malloc/free`;
- data structures beyond fixed arrays;
- sanitizers/GDB в глубину;
- assembly;
- formal discrete math.

Они появятся тогда, когда следующий проектный шаг создаст необходимость.

## Gate модуля в одной фразе

К Module 1 ты должен уметь самостоятельно собрать маленький многофайловый C-проект, проверить его через `make test`, объяснить representation MiniKV и увидеть, почему fixed storage начинает мешать дальнейшему развитию.
