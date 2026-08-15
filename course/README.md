# Systems Engineering Course

Самодостаточный project-first курс по Computer Science и systems engineering для программиста с Python-бэкграундом.

**Основной язык:** русский.  
**Темп:** 6–8 часов в неделю.  
**Формат:** mobile-first теория + PC-first разработка.  
**Обязательная теория:** внутри этого репозитория.

## Начать отсюда

1. [`STRUCTURE.md`](STRUCTURE.md) — как устроены уроки и проекты.
2. [`AUTHORING_STANDARD.md`](AUTHORING_STANDARD.md) — стандарт качества материалов.
3. [`ASSESSMENT_AND_STUDY_RULES.md`](ASSESSMENT_AND_STUDY_RULES.md) — как проходить упражнения и milestone.
4. [`ENVIRONMENT.md`](ENVIRONMENT.md) — рабочая Linux-среда.
5. [`00-c-fast-start/README.md`](00-c-fast-start/README.md) — первый модуль.

## Модель обучения

```text
теория внутри урока
    ↓
causal questions
    ↓
небольшое упражнение
    ↓
кусок реального проекта
    ↓
debug/review
    ↓
следующий урок
```

Внешняя книга или курс никогда не должны быть обязательны для выполнения следующего шага. Они перечисляются отдельно как optional deep dive.

## Core path

```text
0. C Fast Start
   ↓
1. Memory, Pointers & Data Structures
   ↓
1B. Rust Systems Bridge
   ↓
2. Unix, Processes & Shell
   ↓
3. Computer Architecture & Machine Code
   ↓
4. Virtual Memory, Performance & Allocators
   ↓
5. Networking & Concurrency
   ↓
6. Operating Systems & Isolation
   ↓
7. Filesystems & Database Internals
   ↓
8. Binaries, Debugging & Security
   ↓
9. Systems Integration & Architecture
```

Rust bridge обязателен, но не удваивает курс. Основные low-level milestone остаются C-first, а Rust используется для понимания ownership/borrowing/safety и для сравнительных labs.

## Проекты

Код каждого проекта создаётся учеником в `project/` соответствующего модуля. Курс предоставляет спецификацию, acceptance criteria, public tests и hints, но не готовую milestone implementation.

## Внешние материалы

Полезные книги и курсы не запрещены. Они находятся в [`OPTIONAL_READING.md`](OPTIONAL_READING.md) и используются только для углубления.
