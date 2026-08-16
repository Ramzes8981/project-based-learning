# Module 0 — Checkpoint

**Время:** ~90–150 мин вместе с MiniKV review  
**С телефона:** вопросы — да; build/review — ПК

← [`06-make-build-test.md`](06-make-build-test.md) · ↑ [`README`](README.md)

Module 0 не закрывается по факту прочтения файлов. Нужно показать, что базовый C-синтаксис, многофайловая сборка и простое тестирование больше не блокируют разработку.

## Часть A — объяснение

Ответь без поиска:

1. Чем source file отличается от object file, executable и process?
2. Зачем нужен linker?
3. Почему `sizeof(int)` нельзя считать универсально равным 4?
4. В чём принципиальная разница signed и unsigned overflow?
5. Почему C array требует отдельного знания о length?
6. Зачем C string нужен `\0`?
7. Почему strings нельзя сравнивать по содержимому через обычный `==`?
8. Что означает `O(n)` для MiniKV lookup на текущем уровне понимания?
9. Чем declaration отличается от definition?
10. Зачем проекту header?
11. Что описывает dependency graph Make?
12. Почему изменение header может потребовать пересборки нескольких object files?
13. Зачем `make test` должен завершаться ненулевым status при провале теста?

## Часть B — сценарии

### Сценарий 1 — linker

Программа успешно скомпилировала два `.c` в `.o`, но linker пишет:

```text
undefined reference to store_get
```

Какие классы причин ты проверишь?

### Сценарий 2 — broken C string

`strlen(key)` иногда возвращает огромное число и программа затем падает.

Какой invariant C string, вероятно, нарушен?

### Сценарий 3 — границы массива

MiniKV имеет capacity 16. Цикл идёт от `i = 0` до `i <= 16`.

Что не так независимо от того, «работало ли это вчера»?

### Сценарий 4 — рост стоимости

Lookup занимает 2 микросекунды на 10 записях и становится заметно медленнее на очень большом наборе.

Как текущая структура данных объясняет рост хотя бы качественно?

Не делай вывод о точном коэффициенте производительности только из Big-O: сейчас важно объяснить направление роста.

### Сценарий 5 — stale object file

Ты изменил declaration в `minikv.h`, но `make` пересобрал только executable из старых `.o` и получил странный результат/ошибку.

Какое dependency rule, вероятно, описано неверно или отсутствует?

### Сценарий 6 — ложнозелёный тест

Тестовый executable завершился с exit code `1`, но твой shell script/Make target всё равно сообщает успех.

Почему это плохой build/test contract и как должен распространяться failure status?

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
- no unexplained warnings;
- learner README соответствует реальной реализации;
- `make`, `make test`, `make clean` работают согласно documented contract.

## Transfer task

Выбери одно небольшое расширение, которого нет в базовом минимуме:

- `delete` с понятной семантикой;
- `count`/statistics;
- перечисление всех occupied entries;
- отдельный status `VALUE_TOO_LONG`/`KEY_TOO_LONG`.

Добавь для transfer feature минимум два теста: happy path и boundary/error case.

## Debug story

Найди и исправь хотя бы один реальный или специально внесённый bug. В [`project/README.md`](project/README.md) запиши:

```text
Symptom
Hypothesis
Diagnostic step / evidence
Root cause
Fix
Regression test
```

Не достаточно написать «опечатался — исправил». История должна показывать, как evidence привело к root cause.

## Build review

Покажи dependency graph текущего MiniKV:

```text
headers/source
    ↓
object files
    ↓
executables/tests
```

Затем ответь:

- какой файл пересоберётся после изменения одного implementation `.c`;
- что изменится после правки public header;
- какие generated artifacts удаляет `make clean`;
- почему source/docs не должны удаляться.

## Gate

Переходи к Module 1, если:

- basic C syntax не требует постоянного перевода с Python;
- MiniKV v0 проходит собственные проверки;
- можешь объяснить data representation на уровне arrays/strings/structs;
- умеешь собрать проект воспроизводимо через Make;
- можешь отличить compiler error, linker error, failing test и runtime bug;
- понимаешь, **почему следующий шаг потребует pointers и dynamic memory**.

Если последняя часть неочевидна, сформулируй проблему: фиксированный Store нельзя удобно увеличивать, а функции пока не имеют хорошей модели изменения caller-owned complex state. Module 1 начнётся именно отсюда.
