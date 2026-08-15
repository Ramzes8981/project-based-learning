# Module 0 — Checkpoint

**Время:** ~60–120 мин вместе с MiniKV review  
**С телефона:** вопросы — да; build/review — ПК

← [`05-structs-modules.md`](05-structs-modules.md) · ↑ [`README`](README.md)

Module 0 не закрывается по факту прочтения пяти файлов. Нужно показать, что C-синтаксис больше не блокирует простую разработку.

## Часть A — объяснение

Ответь без поиска:

1. Чем source file отличается от executable и process?
2. Зачем нужен linker?
3. Почему `sizeof(int)` нельзя считать универсально равным 4?
4. В чём принципиальная разница signed и unsigned overflow?
5. Почему C array требует отдельного знания о length?
6. Зачем C string нужен `\0`?
7. Почему strings нельзя сравнивать по содержимому через обычный `==`?
8. Что означает `O(n)` для MiniKV lookup на текущем уровне понимания?
9. Чем declaration отличается от definition?
10. Зачем проекту header?

## Часть B — сценарии

### Сценарий 1

Программа успешно скомпилировала два `.c` в `.o`, но linker пишет `undefined reference to store_get`.

Какие классы причин ты проверишь?

### Сценарий 2

`strlen(key)` иногда возвращает огромное число и программа затем падает.

Какой invariant C string, вероятно, нарушен?

### Сценарий 3

MiniKV имеет capacity 16. Цикл идёт от `i = 0` до `i <= 16`.

Что не так независимо от того, «работало ли это вчера»?

### Сценарий 4

Lookup занимает 2 микросекунды на 10 записей и 150 миллисекунд на очень большой набор.

Как текущая структура данных объясняет рост хотя бы качественно?

## Часть C — MiniKV v0

Проверь проект по [`project/ACCEPTANCE.md`](project/ACCEPTANCE.md).

Обязательно:

- fixed capacity;
- no heap allocation;
- set/update;
- get;
- missing key;
- full-store behavior;
- key/value length validation;
- tests;
- no unexplained warnings.

## Transfer task

Выбери одно небольшое расширение, которого нет в базовом минимуме:

- `delete` с понятной семантикой;
- `count`/statistics;
- перечисление всех occupied entries;
- отдельный status `VALUE_TOO_LONG`/`KEY_TOO_LONG`.

## Debug story

Найди и исправь хотя бы один реальный или специально внесённый bug. В README проекта запиши четыре пункта:

```text
симптом
гипотеза
как проверил
корневая причина
```

## Gate

Переходи к Module 1, если:

- basic C syntax не требует постоянного перевода с Python;
- MiniKV v0 проходит собственные проверки;
- можешь объяснить data representation на уровне arrays/strings/structs;
- понимаешь, **почему следующий шаг потребует pointers и dynamic memory**.

Если последняя часть неочевидна, сформулируй проблему: фиксированный Store нельзя удобно увеличивать, а функции пока не имеют хорошей модели изменения caller-owned complex state. Module 1 начнётся именно отсюда.
