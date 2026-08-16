# Стандарт написания уроков

## 1. Язык

Русский, с английским original term при первом важном появлении. API/type/register/protocol names не переводятся искусственно.

## 2. Self-contained

Lesson содержит достаточно theory/API semantics, чтобы выполнить обязательное упражнение/project slice без внешней статьи/видео. Official docs/book могут быть optional reference.

## 3. Mobile-first

- один learning cycle = один `.md`;
- короткие секции/абзацы;
- избегать wide tables;
- code lines желательно ≤100 chars;
- diagrams преимущественно vertical;
- lesson header указывает theory/practice/project estimate и пригодность телефона.

## 4. Lesson types

### Project lesson — обязательные блоки

1. цель;
2. prerequisite check/context, если prerequisite неочевиден;
3. engineering problem;
4. self-contained theory;
5. minimal examples;
6. causal/situational questions;
7. focused exercise + self-check;
8. project slice;
9. edge cases/debugging;
10. exit check.

### Theory / consolidation lesson

Не требует искусственного project slice. Обязательно:

1. цель;
2. self-contained model;
3. examples/diagrams;
4. causal/situational questions;
5. exercise/transfer;
6. edge cases/limits;
7. exit check.

## 5. Code quality

- no unexplained UB/data races/ownership ambiguity;
- examples define input/domain preconditions;
- allocation/I/O/error paths are not silently ignored;
- arithmetic on sizes/offsets has overflow/bounds reasoning;
- C examples compile warning-clean under course flags when complete;
- Rust examples prefer safe code; every `unsafe` has explicit checkable invariant;
- examples never reveal current milestone implementation.

## 6. Project folder

Every directory containing `SPEC.md` also contains:

```text
README.md
SPEC.md
ACCEPTANCE.md
TESTS.md
HINTS.md
```

`README.md` is learner-owned. Course infrastructure may add fixtures/targets/Python clients/load generators, but no core solution/starter TODO implementation.

## 7. Hints

Progressive:

```text
diagnostic question
→ direction
→ pseudocode/structure
→ concrete local hint
```

No complete milestone code as final hint.

## 8. Assessment questions

Prefer «что сломается, если…», invariant/ownership/failure reasoning over definition recall.

## 9. External references

Strong books/docs belong in `OPTIONAL_READING.md`/reference docs. Required lesson should not contain a URL as substitute for theory.

## 10. Repository QA

Learner materials must not contain internal assistant citation markers, unresolved TODO/TBD/FIXME placeholders, broken relative links or missing project contract docs. CI runs `scripts/course_audit.py`.
