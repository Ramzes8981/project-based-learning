# 9.1 — Как понять, что именно должна выдерживать система

**Теория:** ~75 мин · **Design:** ~2–3 часа · **С телефона:** да

← [`README`](README.md) · → [`02-protocol-idempotency-contracts.md`](02-protocol-idempotency-contracts.md)

## Проблема

Фраза «сделать быстрый надёжный KV-сервис» почти ничего не говорит инженеру.

Нельзя выбрать очередь, число workers или durability policy, пока неизвестно:

- сколько запросов приходит;
- какого они размера;
- сколько клиентов одновременно;
- что считается приемлемой задержкой;
- сколько памяти/диска можно потратить;
- какие данные обязаны пережить restart.

## Ментальная модель

Сначала описываем **наблюдаемое поведение и ограничения**, затем строим систему.

```text
workload + guarantees + resource limits
                 ↓
           design choices
                 ↓
             evidence
```

## Требования

**Функциональные требования (functional requirements)** отвечают «что система делает»:

```text
GET / SET / DELETE
несколько клиентов
состояние переживает оговорённый restart
есть graceful shutdown
можно посмотреть health/metrics
```

**Нефункциональные требования (non-functional requirements)** отвечают «при каких условиях и насколько хорошо».

Плохое требование:

> сервис должен быть быстрым.

Проверяемое:

```text
при workload X p95 latency <= target
очередь ограничена N элементами
RSS <= memory budget
shutdown <= target при очереди размера M
```

Числа в учебном проекте — гипотезы для эксперимента, а не универсальные production нормы.

## Workload

Заполни [`project/WORKLOAD.md`](project/WORKLOAD.md):

```text
request rate / concurrency
GET:SET:DELETE ratio
key/value sizes
record count / working set
burst shape
storage growth
```

Важно использовать **один и тот же workload**, когда сравниваешь два designs.

## Где находится state

Для каждого изменяемого объекта задай:

```text
кто владеет?
кто может менять?
как долго живёт?
нужна ли синхронизация?
переживает ли restart?
что является source of truth после crash?
```

Это **инвентаризация состояния (state inventory)**.

## Границы компонентов

Разделяй систему не по красивым boxes, а по контрактам:

```text
connection / protocol
        ↓
bounded execution
        ↓
KV semantics
        ↓
storage/index
```

Для boundary должны быть понятны input/output, owner state, failure behavior и resource bound.

## Типичная неправильная модель

> Сначала выберу thread pool, cache и B-tree, потом подгоню требования.

Так design невозможно проверить: любое измерение можно объявить «достаточно хорошим» задним числом.

## Практика

До написания нового кода создай:

- `WORKLOAD.md`;
- 5–10 functional requirements;
- несколько измеримых targets;
- минимум 5 non-goals;
- первый `ARCHITECTURE.md` только с boundaries/state ownership.

## Exit check

Для каждого числа и каждого компонента можешь ответить: **какое требование заставило его появиться и чем мы проверим решение?**