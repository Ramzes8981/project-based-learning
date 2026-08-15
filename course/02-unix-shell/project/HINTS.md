# Shell — Hints

## Hint 1

Раздели layers:

```text
read line
parse tokens/plan
execute builtin OR external plan
```

## Hint 2

Для redirection нарисуй target descriptor table **до кода**.

## Hint 3

Pipeline hang почти всегда сначала проверяй через «кто ещё держит write end открытым?».

## Hint 4

Не `wait` producer до запуска consumer.

## Hint 5

Child setup order:

```text
configure descriptors/signals
close unused fds
exec
```

Parent cleanup order проектируй отдельно.
