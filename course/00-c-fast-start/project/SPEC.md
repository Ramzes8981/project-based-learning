# MiniKV v0 — Specification

Это первый сквозной проект курса. В Module 0 он намеренно примитивный, а позже эволюционирует в Hash Table и сетевой KV service.

## Цель версии v0

Реализовать key/value store с:

- фиксированным maximum capacity;
- фиксированными maximum lengths key/value;
- linear lookup;
- массивом `Entry`/эквивалентным representation;
- без heap allocation;
- без hashing.

## Обязательное поведение

### SET

Для пары `(key, value)`:

- если key уже существует — value обновляется;
- если key новый и есть свободное место — создаётся запись;
- если store заполнен — возвращается явный status;
- слишком длинные key/value не должны переписывать память за буфером.

### GET

- существующий key возвращает связанное value/успешный status;
- отсутствующий key даёт явный `not found` результат.

## Ограничения

Выбери и задокументируй конкретные небольшие лимиты, например capacity порядка 8–32 entries и короткие строки.

Числа — часть твоего design decision. Тесты должны использовать выбранный контракт последовательно.

Если API использует C strings, каждый accepted key/value обязан иметь корректный null terminator в пределах обещанной buffer capacity.

## Что запрещено в v0

- `malloc/calloc/realloc/free`;
- hash function;
- resize;
- linked list;
- импорт готовой реализации hash table;
- скрывать failure за переполнением fixed buffer или молчаливой порчей данных.

## Файлы к завершению Module 0

Точная структура исходников не навязывается. К завершению Module 0 в этой project-папке должны появиться созданные тобой:

- исходный C-код;
- header, если public API уже выделен;
- тестовый executable/files или эквивалентные автоматические `assert`-проверки;
- `Makefile`;
- заполненный [`README.md`](README.md) с контрактом, build/test commands и известными ограничениями.

Уже предоставленные курсом файлы:

```text
README.md       learner-owned documentation template
SPEC.md         этот контракт
ACCEPTANCE.md   gate
TESTS.md        public test scenarios
HINTS.md        progressive hints
```

`TESTS.md` не является готовым harness: тестовый код для MiniKV — часть твоей реализации.

## Build contract

После урока 0.6 проект должен поддерживать документированный интерфейс сборки:

```bash
make
make test
make clean
```

Exact targets/files внутри Makefile проектируешь сам в рамках этого поведения.

## Design questions

До кода ответь:

1. Что означает «пустой slot»?
2. Как отличить existing key от нового?
3. Что происходит при update existing key?
4. Как гарантировать, что key/value помещаются в buffers и сохраняют string terminator contract?
5. Где хранится количество активных записей и обязательно ли оно вообще?
6. Какие failures возвращаются caller явно, а какие состояния считаются невозможными по contract?

SPEC описывает поведение, но не отвечает за тебя на эти вопросы.
