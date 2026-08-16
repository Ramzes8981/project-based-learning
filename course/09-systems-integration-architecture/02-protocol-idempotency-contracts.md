# 9.2 — Protocol contracts, request IDs и idempotency

**Теория:** ~75 мин  
**Design/project:** ~2–3 часа  
**С телефона:** да

← [`01b-computational-limits-p-np.md`](01b-computational-limits-p-np.md) · → [`03-queueing-latency-capacity.md`](03-queueing-latency-capacity.md)

## Цель

Спроектировать network API так, чтобы timeout/retry semantics были явными.

## Failure ambiguity

Client отправил SET и получил timeout. Возможны:

```text
request не дошёл
server выполнил, response потерян
server умер во время operation
response задержался дольше client deadline
```

Timeout не доказывает, что operation не выполнена.

## Idempotency

Operation idempotent, если повторное применение с тем же semantic input оставляет state таким же после первого успешного применения.

`GET` обычно idempotent. `SET key=value` может быть idempotent относительно конечного value, но side effects/metrics/version increments способны сделать full semantics неидемпотентными. `increment` не idempotent.

## Request identity

Если protocol поддерживает dedup/retry-safe mutations, request ID должен иметь scope/lifetime/storage policy. «Добавим UUID» без server memory/recovery contract не решает ambiguous retry.

## Capstone decision

Ты можешь **не реализовывать** durable dedup в core. Но `PROTOCOL.md` обязан явно написать:

- какие operations client может retry;
- что означает timeout;
- есть ли request ID;
- какие duplicate effects возможны после restart.

## Project slice

Начни `PROTOCOL.md` как evolution Module 5 protocol и добавь response/error/deadline/retry semantics. Не добавляй distributed consensus ради one-node service.

## Exit check

Для каждого client retry ответь: может ли first attempt уже изменить state и как duplicate detect/semantics это учитывают?
