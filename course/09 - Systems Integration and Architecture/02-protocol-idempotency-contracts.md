# 9.2 — Что означает timeout и можно ли просто повторить запрос

**Теория:** ~70 мин · **Design/project:** ~2 часа · **С телефона:** да

← [`01-requirements-boundaries-state.md`](01-requirements-boundaries-state.md) · → [`03-queueing-latency-capacity.md`](03-queueing-latency-capacity.md)

## Проблема

Клиент отправил `SET`, затем получил timeout.

Что произошло?

```text
request не дошёл
request дошёл, но server ещё не выполнил его
server выполнил mutation, response потерялся
response просто пришёл слишком поздно
server умер посередине операции
```

**Timeout сообщает только то, что клиент не дождался результата вовремя.** Он не доказывает, что операция не была выполнена.

## Почему retry опасен

Если повторить mutation вслепую, side effect может выполниться дважды.

Здесь возникает понятие **идемпотентности (idempotency)**: повторное применение операции с тем же смысловым input после первого успеха не меняет конечное состояние повторно.

`SET key=value` часто можно сделать идемпотентным относительно final value. `INCREMENT` — обычно нет.

Но даже у `SET` дополнительные side effects — version counter, audit event, billing — могут изменить полную семантику.

## Request identity

Уникальный request ID полезен только вместе с contract:

```text
сколько сервер хранит ID?
переживает ли dedup restart?
что происходит после expiry?
какой scope уникальности?
```

«Добавим UUID» само по себе ambiguity не устраняет.

## Project slice

Обнови `PROTOCOL.md`:

- какие операции можно retry;
- что означает timeout;
- какие duplicate effects допустимы;
- есть ли request ID/dedup;
- что меняется после restart.

Durable dedup **не обязателен** для core. Честный explicit limitation лучше фиктивной гарантии.

## Типичная неправильная модель

> Если клиент не получил `OK`, значит server ничего не сделал.

Распределённое по сети наблюдение так не работает даже при одном server process.

## Exit check

Для любого retry можешь объяснить, мог ли первый attempt уже изменить state и как контракт учитывает повтор?