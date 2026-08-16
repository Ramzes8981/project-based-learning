# Источники и их роль

Начиная с self-contained версии курса, **ни один внешний источник не является обязательным teaching dependency**.

## Приоритет

1. `course/<module>/<lesson>.md` — обязательная теория.
2. `project/SPEC.md` + local references (`FORMAT.md`, `PROTOCOL.md`, `ISA.md`, mini references) — точный project/API contract.
3. Official system documentation — optional reference для version/platform detail.
4. Books/courses — optional deep dive.

## Почему документация остаётся полезной

Systems engineer должен уметь читать standards/man pages/API docs, но упражнение не должно быть невозможно без них. Поэтому курс объясняет working model и минимальный contract локально; documentation используется для углубления и проверки версии.

## External projects

Nand2Tetris/другие сильные бесплатные projects могут быть **optional parallel practice**. Core gate всегда имеет course-owned theory/spec/tests и не требует чужой tutorial.

Полезные книги/курсы находятся в [`OPTIONAL_READING.md`](OPTIONAL_READING.md).
