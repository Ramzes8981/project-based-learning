# Course Shell — рабочий README

## Status

## Build

```text
make
make test
make clean
```

Запиши имя executable и canonical run command.

## Grammar

Скопируй **своими словами** реально поддержанную grammar и non-goals. Не обещай quotes/job-control, если их нет.

## Parser design

Token representation, validation phases, ownership of token buffers.

## Process model

Для external command/pipeline опиши:

```text
parent responsibilities
child responsibilities
exec failure path
descriptor close policy
wait/reap policy
```

## Redirection / FD topology

Запиши, какие descriptors существуют до/после `fork`, `dup2`, close.

## Signals

Chosen SIGINT/process-group model и limitations.

## Tests

- unit parser tests;
- black-box cases из `TESTS.md`;
- `project/tests/run_cases.py` как optional external-behavior harness;
- sanitizer/debugger checks, где применимо.

## Known limitations

## Transfer feature

## Debugging story

Symptom → hypothesis → diagnostic command/evidence → root cause → fix → regression.
