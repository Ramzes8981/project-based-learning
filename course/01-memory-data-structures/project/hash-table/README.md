# Hash Table — рабочий README

Этот файл принадлежит твоей реализации. SPEC задаёт поведение, но representation/API решения документируешь здесь.

## Status

## API

Какие операции и status/error values?

## Representation

- bucket state representation;
- capacity/active/tombstones;
- hash/probe policy.

## Ownership & lifetime

```text
table storage owner:
key owner:
value owner:
GET result lifetime:
what invalidates returned pointers:
destroy contract:
```

## Complexity assumptions

Expected/worst-case и assumptions distribution/load factor.

## Growth policy

Threshold, new capacity calculation, failure-safe rehash.

## Metrics

Probes, resize count, max/histogram и что они показывают.

## Build / tests

```text
make
make test
```

Запиши sanitizer run и boundary scenarios.

## Transfer feature

## Debugging story

Symptom → hypothesis → diagnostic evidence → root cause → fix → regression test.

## Known limitations

