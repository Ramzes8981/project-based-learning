# 1C.4 — Negative testing, fault injection и fuzzing intuition

**Теория:** ~75 мин  
**Упражнение:** ~60 мин  
**С телефона:** теория — да

← [`03-testability-dependencies-doubles.md`](03-testability-dependencies-doubles.md) · → [`05-module-checkpoint.md`](05-module-checkpoint.md)

## Цель

Проверять систему в состояниях, которые happy-path developer предпочёл бы не видеть.

## Negative tests

Проверяют invalid/malformed/forbidden input:

- overlong key;
- truncated frame;
- invalid enum/opcode;
- impossible length combination;
- duplicate insertion по запрещённому contract;
- empty file/header.

Главный oracle часто не «вернул красивый error», а ещё и:

```text
state не повреждён
resource не утёк
process не crash
subsequent valid operation всё ещё работает
```

## Fault injection

Искусственно создаём failure dependency:

- allocation failure;
- short read/write;
- interrupted syscall;
- disk write error;
- worker rejects task;
- peer disconnect mid-frame.

Для C allocation failure удобно тестировать через wrapper/dependency boundary, а не ждать реального OOM.

## Fuzzing

Fuzzer генерирует/мутирует много inputs и ищет crashes, sanitizer findings, hangs или violated properties.

Fuzzing особенно силён для parser boundaries. Он не заменяет spec-based tests: если программа стабильно возвращает неправильный ответ без crash и oracle не проверяет semantics, fuzzer может быть доволен.

## Fuzz target

Хорошая цель:

```text
arbitrary bytes -> parser
```

с properties:

- no UB/crash;
- execution bounded;
- accepted result satisfies structural invariants;
- rejected input leaves no leaked state.

## Seed corpus

Начни с маленьких meaningful examples: empty, minimum valid, maximum valid, each opcode, truncated cases. Mutation от них эффективнее случайных bytes без структуры.

## Sanitizers + fuzzing

ASan/UBSan превращают многие скрытые memory errors в observable failures. Но отсутствие crash за миллион inputs не доказывает correctness.

## Упражнение

Для MiniKV/Hash Table составь 12 negative/fault cases. Реализуй минимум 3: over-limit input, operation on boundary/full state, и simulated failure path, если архитектура уже позволяет.

Для pure parser можешь написать простой loop-mutator на Python: менять byte в fixture и запускать parser test harness. Это инфраструктура, не основной C/Rust skill.

Разбор: [`04-negative-testing-fuzzing.solution.md`](04-negative-testing-fuzzing.solution.md).

## Exit check

После failure можешь ли ты проверить не только error code, но и сохранность invariants/resources?
