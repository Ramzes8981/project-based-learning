# Authoring standard — self-contained systems course

Этот файл — нормативный стандарт курса. Технически верный текст считается дефектным, если новичок не может понять его из уже пройденного материала.

## 1. Главный порядок

Каждый новый concept проходит один и тот же путь:

```text
ПРОБЛЕМА
→ ИНТУИЦИЯ
→ ПРОСТАЯ МЕНТАЛЬНАЯ МОДЕЛЬ
→ ОФИЦИАЛЬНЫЙ ТЕРМИН
→ МЕХАНИКА
→ МАЛЕНЬКИЙ ПРИМЕР
→ ПРАКТИКА
→ CAUSAL CHECK
→ PROJECT APPLICATION, если естественно
```

Запрещено начинать урок со словаря терминов, который только позже получит смысл.

## 2. Progressive disclosure

Перед первым содержательным употреблением важного термина автор обязан проверить:

1. Уже возникла проблема, которую этот термин помогает описать?
2. Все слова в объяснении уже известны?
3. Есть ли concrete example?
4. Может ли ученик объяснить **почему**, а не повторить определение?

Если нет — термин переносится или предложение переписывается обычным языком.

Ключевые dependencies фиксируются в [`CONCEPT_DEPENDENCIES.json`](CONCEPT_DEPENDENCIES.json). Manifest не заменяет человеческий review.

## 3. Формат одного mobile-first lesson

Рекомендуемый шаблон:

```markdown
# 2.3 — Почему запущенной программе нужна ОС

**Теория:** ~35 мин
**Практика:** ~30 мин
**С телефона:** да; практика — ПК

← ... · → ...

## Что мы пытаемся понять
...

## Проблема
...

## Интуиция
...

## Ментальная модель
...

## Теперь назовём механизм
...

## Как это работает
...

## Маленький пример
...

## Неправильная mental model
...

## Causal questions
...

## Практика
...

## Project slice
... только если нужен

## Exit check
...
```

Не все заголовки обязательны буквально; обязательна **логика**.

## 4. Размер learning cycle

Один `.md` должен помещать одну центральную причинную идею. Признаки перегруза:

- больше 3–4 действительно новых механизмов;
- практика требует терминов из второй половины того же длинного урока;
- заголовок содержит 4–5 независимых существительных;
- exit check фактически является экзаменом по отдельному мини-модулю.

В таком случае lesson split предпочтительнее более длинного текста.

## 5. Названия

Заголовок должен отвечать «что я пойму/смогу сделать?»:

Хорошо:
- «Почему TCP не передаёт сообщения»;
- «Как программе попросить больше памяти»;
- «Почему указатель может стать недействительным».

Плохо без предварительного контекста:
- `TCP Framing`;
- `Heap Allocation`;
- `Memory Model Internals`.

Файл может сохранить стабильный технический slug, если переименование создаёт больше churn, чем педагогической пользы. Learner-facing heading и README обязаны быть человеческими.

## 6. Язык

Основной язык — русский. На первом важном употреблении:

> время жизни объекта (lifetime)

API, команды, identifiers и code остаются английскими. Не превращать текст в русско-английский суржик, если английское слово не нужно для документации/инструмента.

## 7. Практика

Практика должна требовать самостоятельного решения, но быть мала по scope.

Нельзя:
- давать огромный TODO skeleton;
- превращать курс в набор LeetCode;
- показывать финальный milestone implementation;
- просить скопировать код и назвать это практикой.

Можно:
- дать сигнатуру API;
- дать тест/fixture;
- дать псевдокод;
- показать мини-пример другого механизма;
- дать solution к маленькому упражнению после самостоятельной попытки.

## 8. Causal questions

Приоритет вопросов:

- «что изменится, если…?»;
- «почему этот порядок важен?»;
- «какой invariant сломался?»;
- «какое наблюдение отличит две гипотезы?»;
- «почему простой вариант перестал работать?».

Definition-only quiz не считается достаточным exit check.

## 9. Broken examples

Код с UB, race, leak, warning, deadlock или другим намеренным дефектом должен иметь явный маркер **`BROKEN EXAMPLE — не образец корректного кода`** до блока и объяснение, что именно наблюдаем.

После диагностического эксперимента должен существовать warning-clean/correct вариант или явная инструкция удалить broken fixture.

## 10. C correctness baseline

Correct examples и course fixtures проверяются с разумными warning flags. Обязательно думать о:

- signed overflow и conversions;
- `size_t` arithmetic overflow/underflow;
- bounds и null termination;
- pointer lifetime/one-past;
- ownership, leaks, double/use-after-free;
- `realloc` failure/zero-size policy;
- invalid shifts/aliasing;
- short I/O, `EINTR`, cleanup/descriptors;
- network length arithmetic/serialization/endian;
- pthread races/deadlocks/shutdown.

## 11. Rust correctness baseline

Особенно проверяются:

- ownership/borrow explanations;
- lifetime ≠ «время на часах»;
- unnecessary cloning;
- `unsafe` invariants;
- FFI ABI (`c_int`, `repr(C)`, platform contract);
- raw-pointer validity;
- ownership across FFI;
- panic across FFI boundary;
- `Send`/`Sync` только в контексте реальной concurrency-проблемы.

## 12. Project standard

Каждый core project имеет:

- `README.md`;
- `SPEC.md`;
- `ACCEPTANCE.md`;
- `TESTS.md`;
- `HINTS.md`.

SPEC начинается с behavior. Technical constraints привязаны к prerequisite lessons.

Для milestone должны быть понятны:

```text
prerequisites
observable behavior
technical constraints unlocked so far
acceptance criteria
tests
hints
README evidence
error/resource policy
transfer task
debugging story
```

Полного project solution в репозитории быть не должно.

## 13. Self-contained rule

Mandatory learner file не зависит от внешнего tutorial. Если lab требует небольшой API subset, добавляется local mini-reference. External URL разрешён в optional/reference files, но не как обязательный teaching dependency.

## 14. Mobile-first rule

- короткие секции;
- вертикальные ASCII-схемы;
- широкие таблицы только когда иначе хуже;
- длинные команды разбивать;
- время + `С телефона` в начале;
- prev/next navigation у mandatory lessons;
- код на ПК, теория по возможности читается на телефоне.

## 15. Финальный author review

Перед merge прочитать изменённый путь как ученик, который знает только предыдущие уроки. Для каждого незнакомого слова спросить: «почему я уже должен это знать?» Если ответа нет — это blocker.