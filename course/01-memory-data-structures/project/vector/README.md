# Vector — рабочий README

Этот файл заполняешь по мере реализации.

## Status

## API

Запиши выбранные signatures и error semantics.

## Representation

```text
data pointer:
size:
capacity:
element type:
```

## Ownership

Кто владеет backing allocation? Что invalidates element pointers? Что происходит после destroy?

## Growth policy

Начальная capacity, factor, overflow/failure behavior.

## Build / tests

```text
make
make test
make clean
```

Запиши sanitizer command/target.

## Invariants

Минимум: `size <= capacity`, valid allocation/capacity relation, no out-of-bounds initialized elements.

## Debugging story

Symptom → hypothesis → evidence → root cause → fix → regression test.

## Known limitations / transfer

Опиши выбранное расширение и memory/performance trade-off.
