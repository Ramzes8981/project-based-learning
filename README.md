# Systems Engineering Course

Личный self-contained курс по Computer Science и systems engineering: C, Rust, алгоритмы/структуры данных, тестирование, Unix, архитектура CPU, виртуальная память, сети, concurrency, ОС, storage/database internals, binaries/debugging/security и system architecture.

> **Главная точка входа:** [`course/README.md`](course/README.md)

## Что изменено относительно исходного fork

Исходный `project-based-learning` — большой каталог внешних project tutorials. Он сохранён в [`PROJECT_CATALOG.md`](PROJECT_CATALOG.md) как источник дополнительных идей.

Основная часть fork теперь — собственный курс, где обязательные знания находятся внутри репозитория:

```text
самодостаточная теория в Markdown
    ↓
вопросы на понимание
    ↓
небольшое упражнение
    ↓
project slice, когда тема уже нужна milestone
    ↓
tests / debugging / review
    ↓
следующий learning cycle
```

Внешние книги, курсы, стандарты и документация используются как **optional/reference**, а не как обязательная замена уроков.

## Core path

```text
0.  C Fast Start
1.  Memory and Data Structures
1B. Rust Systems Bridge
1C. Testing Engineering
2.  Unix Shell
3.  Computer Architecture
4.  Virtual Memory, Performance and Allocators
5.  Networking and Concurrency
6.  Operating Systems and Isolation
7.  Filesystems and Databases
8.  Binaries, Debugging and Security
9.  Systems Integration and Architecture
```

## Как начать

1. [`course/STRUCTURE.md`](course/STRUCTURE.md)
2. [`course/ASSESSMENT_AND_STUDY_RULES.md`](course/ASSESSMENT_AND_STUDY_RULES.md)
3. [`course/ENVIRONMENT.md`](course/ENVIRONMENT.md)
4. [`Module 0 — C Fast Start`](<course/00 - C Fast Start/README.md>)
5. Текущий прогресс: [`SYSTEMS_ENGINEERING_PROGRESS.md`](SYSTEMS_ENGINEERING_PROGRESS.md)

## Проекты

Milestone-код пишет ученик с нуля. В `project/` каталогах лежат:

- `README.md` — learner-owned design/build/debug log;
- `SPEC.md` — ТЗ/контракт;
- `ACCEPTANCE.md` — критерии сдачи;
- `TESTS.md` — public test scenarios;
- `HINTS.md` — ступенчатые подсказки;
- дополнительные fixtures/tooling только там, где их написание не является целью задания.

Готовых reference implementations основных milestone в learner path нет.

## Mobile-first

Уроки разбиты на небольшие `.md` learning cycles и рассчитаны на чтение с телефона. Большая практическая разработка выполняется в Linux-среде на ПК.

## Quality gates

`scripts/course_audit.py` и GitHub Actions проверяют learner path на broken relative links, служебные assistant markers, незакрытые placeholders и отсутствие обязательных project docs.

## Дополнительные материалы

- [`course/OPTIONAL_READING.md`](course/OPTIONAL_READING.md) — хорошие книги/курсы для углубления;
- [`SYSTEMS_ENGINEERING_RUSSIAN_RESOURCES.md`](SYSTEMS_ENGINEERING_RUSSIAN_RESOURCES.md) — необязательные русскоязычные companion-ресурсы;
- [`PROJECT_CATALOG.md`](PROJECT_CATALOG.md) — исходный каталог project-based-learning.

## License

Исходные материалы upstream сохраняют свою лицензию и историю. Новые course materials находятся в этом fork рядом с исходным проектом; при дальнейшем публичном распространении лицензирование добавленного контента следует оформить отдельно и явно.
