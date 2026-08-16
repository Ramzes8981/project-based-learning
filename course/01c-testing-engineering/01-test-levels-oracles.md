# 1C.1 — Test levels и test oracle

**Теория:** ~60 мин  
**Упражнение:** ~45 мин  
**С телефона:** да

← [`README`](README.md) · → [`02-invariants-properties-regressions.md`](02-invariants-properties-regressions.md)

## Цель

Выбирать уровень теста по риску и понимать, **кто решает, что результат правильный**.

## Test oracle

Test oracle — правило/наблюдение, по которому тест отличает корректный результат от некорректного.

```text
input + execution + oracle -> pass/fail evidence
```

`program did not crash` — слабый oracle. Для `SET k=v; GET k` oracle может быть exact returned value + unchanged unrelated entries + valid counters.

## Unit test

Проверяет маленький компонент/функцию в изоляции настолько, насколько это полезно.

Подходит для hash function determinism, parser helper, heap sift operation. Unit test быстрый и локализует defect, но не доказывает integration.

## Integration test

Проверяет несколько реальных компонентов вместе: parser + storage, allocator + user, file format + pager.

Главный вопрос — interfaces согласованы ли в реальной композиции.

## System / black-box test

Запускает систему через внешний contract: process CLI, socket protocol, file format. Не обязан знать внутренние structs.

Shell и KV Server особенно хорошо проверяются так.

## Acceptance test

Проверяет пользовательское/проектное требование из SPEC. Acceptance может быть system test, но понятия не тождественны: acceptance говорит **зачем**, system — **на каком уровне**.

## Test pyramid не закон природы

Много быстрых narrow tests полезно, но systems software часто требует серьёзных integration/system checks. Не оптимизируй число тестов под красивую геометрию.

## Determinism

Тест должен по возможности контролировать time/randomness/environment. Flaky test уничтожает доверие: случайный green больше не является evidence.

## Упражнение

Возьми 12 tests своего Hash Table/Vector/MiniKV и классифицируй:

```text
unit / integration / system / acceptance
oracle
what bug class it detects
what it cannot prove
```

Добавь один test на public behavior, который не зависит от internal representation.

Разбор: [`01-test-levels-oracles.solution.md`](01-test-levels-oracles.solution.md).

## Exit check

Если test падает, можешь ли ты объяснить, какой contract был oracle и какой уровень системы реально проверялся?
