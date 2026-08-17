# Hash Table in C — рабочий milestone

Проект начинается после 1.16 и получает resize после 1.17.

## Поведение

Хранит `key → int value`:

- put new;
- update existing;
- get;
- delete;
- collisions не меняют correctness;
- table растёт по documented policy;
- allocation failure не теряет old state.

Не требуется cryptographic hash, concurrent access или disk persistence.

## Документы

[`SPEC.md`](SPEC.md) · [`ACCEPTANCE.md`](ACCEPTANCE.md) · [`TESTS.md`](TESTS.md) · [`HINTS.md`](HINTS.md)

Student owns implementation; full solution отсутствует.