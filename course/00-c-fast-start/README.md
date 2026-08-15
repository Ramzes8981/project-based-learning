# Module 0 — C Fast Start

**Цель:** быстро стать функциональным в C и начать первый реальный проект без отдельного «семестра синтаксиса».

**Оценка:** 10–15 часов.  
**Активный проект:** `MiniKV v0` — fixed-capacity key/value store с линейным поиском.

## Уроки

1. [`01-source-build-run.md`](01-source-build-run.md) — от исходника до процесса.
2. [`02-types-values.md`](02-types-values.md) — типы, размеры и представление значений.
3. [`03-control-flow-functions.md`](03-control-flow-functions.md) — C-синтаксис управления и функции.
4. [`04-arrays-strings.md`](04-arrays-strings.md) — массивы, строки, границы, линейный поиск.
5. [`05-structs-modules.md`](05-structs-modules.md) — `struct`, `enum`, `.h/.c`, linker.
6. [`06-module-checkpoint.md`](06-module-checkpoint.md) — проверка Module 0.

## Проект

Перед первым project slice прочитай [`project/SPEC.md`](project/SPEC.md). По мере уроков возвращайся к нему и расширяй собственную реализацию в этой же папке.

Курс **не** даёт готовый MiniKV-код.

## Что пока сознательно не изучаем

- pointers в глубину;
- `malloc/free`;
- data structures beyond fixed arrays;
- GDB в глубину;
- assembly;
- formal discrete math.

Они появятся тогда, когда следующий проектный шаг создаст необходимость.
