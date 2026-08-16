# SimpleDB v1 — Recovery & durability limitations

Этот файл заполняется учеником к checkpoint. Базовые non-claims уже зафиксированы, чтобы проект случайно не назывался transactional.

## Implemented persistence policy

Запиши фактическое поведение:

```text
when dirty pages are written:
what close does:
whether fsync/fdatasync is used:
what header/root update order is:
```

## Core non-guarantees

SimpleDB v1 **не гарантирует**:

- atomic multi-page transaction;
- WAL-based recovery;
- consistency после process/power failure в любой точке split;
- concurrent writers/readers correctness;
- checksum detection всех corruptions;
- durability beyond explicitly implemented sync policy.

## Failure matrix

Разбери минимум:

```text
crash before leaf page write
crash after new leaf write before parent update
crash after parent update before header/root update
short/error page write
truncated database file
```

Для каждого: какие состояния возможны, может ли open validator обнаружить проблему, теряются ли данные/структура.

## How WAL would change design

После Lesson 7.8 опиши conceptual sequence write-ahead rule и recovery idea, но **не заявляй WAL implemented**, если его нет.

## Evidence

Ссылки на tests/corruption fixtures и observed behavior.
