# 5.3 — Socket API и address-independent client/server

**Теория:** ~90 мин  
**Lab:** ~2–3 часа  
**С телефона:** теория — да

← [`02-udp-tcp-stream.md`](02-udp-tcp-stream.md) · → [`04-framing-protocol-design.md`](04-framing-protocol-design.md)

## Цель

Собрать TCP echo client/server через `getaddrinfo`, `socket`, `bind`, `listen`, `accept`, `connect`, `send/recv` без IPv4-only hardcoding.

## Socket descriptor

В Unix socket представлен file descriptor и участвует в `close`/readiness model, но underlying kernel object имеет network state/options.

## Server lifecycle

```text
getaddrinfo(local/service)
↓
for candidate addresses: socket -> bind
↓
listen
↓
accept loop
↓
one connected descriptor per accepted connection
```

Listening descriptor **не становится клиентским**. Успешный `accept` возвращает новый connected descriptor; listening socket остаётся доступен для следующих connections.

Ownership rule: каждый успешно созданный descriptor должен иметь ясного owner и ровно один eventual close path.

## Client lifecycle

```text
getaddrinfo(server/service)
↓
for candidate:
    socket
    connect
    success -> keep fd, stop
    failure -> close fd, try next
↓
freeaddrinfo
```

`getaddrinfo` даёт list candidates с family/type/protocol/address. Это убирает hard-coded assumption «address всегда IPv4 text».

## Address storage

Socket APIs принимают generic address pointer + explicit length. Для peer/local address buffers используют family-appropriate struct; `sockaddr_storage` предназначен как sufficiently large/aligned storage для socket address families поддерживаемого API.

Главная мысль: не cast arbitrary short object к `sockaddr *`; storage/length должны соответствовать реальному address object.

## `bind`, `listen`, backlog

`bind` назначает local endpoint. `SO_REUSEADDR` — конкретная socket option с platform/protocol semantics, не магическое лечение любой bind error.

`listen` делает stream socket passive. `backlog` связан с pending connection handling и не равен простому universal «максимум одновременных клиентов».

## Partial I/O

Connected stream socket сохраняет правила Lesson 5.2:

- `send` может обработать меньше bytes, чем просили;
- `recv` может вернуть любой positive chunk;
- `recv == 0` — EOF/orderly shutdown;
- `EINTR` требует retry/policy;
- nonblocking later добавит `EAGAIN/EWOULDBLOCK`.

## `SIGPIPE` / broken peer

Write to connection, где peer больше не читает, может приводить к `EPIPE` и signal behavior в зависимости от API/options/platform. Server обязан иметь process-wide policy, чтобы один disconnect не завершал весь service неожиданно.

## Lab — echo

Сделай address-independent client/server:

1. sequential accept;
2. one client handler at a time;
3. helper loops для write-all/read-until-EOF or chosen echo behavior;
4. every error path closes only resources it owns;
5. IPv4 localhost и IPv6 localhost, если IPv6 доступен в environment.

## Causal questions

1. Почему `accept` возвращает новый fd?
2. Почему failed connect candidate надо close перед следующим?
3. Кто владеет `addrinfo` list?
4. Почему `recv == 0` не означает «получен пустой message»?

Разбор: [`03-socket-api-getaddrinfo.solution.md`](03-socket-api-getaddrinfo.solution.md).

## Exit check

Нарисуй ownership: addrinfo list → listening fd → accepted fd → buffers → cleanup.
