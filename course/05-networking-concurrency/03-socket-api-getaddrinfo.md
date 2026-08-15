# 5.3 — Socket API и address-independent client/server

**Теория:** ~85 мин  
**Lab:** ~2–3 часа  
**С телефона:** теория — да

← [`02-udp-tcp-stream.md`](02-udp-tcp-stream.md) · → [`04-framing-protocol-design.md`](04-framing-protocol-design.md)

## Цель

Собрать TCP echo client/server через `getaddrinfo`, `socket`, `bind`, `listen`, `accept`, `connect`, `send/recv` без IPv4-only hardcoding.

## Socket как FD

POSIX socket represented file descriptor и участвует в close/poll/read/write model. Но socket имеет network-specific state/options.

## Server lifecycle

```text
getaddrinfo(local addr/service)
↓
socket
↓
bind
↓
listen
↓
accept loop
↓
connected client sockets
```

Listening socket и accepted connection socket — **разные descriptors/resources**. `accept` создаёт новый connected socket descriptor для конкретного connection. citeturn932665search4

## Client lifecycle

```text
getaddrinfo(server)
↓
for candidate addresses:
    socket
    connect
    if success -> use
    else close and try next
```

## `getaddrinfo`

Не строй address parsing вручную вокруг `inet_addr` и IPv4-only assumptions.

`getaddrinfo` возвращает linked list candidate socket addresses согласно hints.

Pattern:

```text
resolve
for each result:
   create socket matching family/type/protocol
   attempt operation
   on failure close
freeaddrinfo
```

## `sockaddr`

Socket API использует generic `struct sockaddr*`, а concrete IPv4/IPv6 structures имеют family-specific layouts. `sockaddr_storage` достаточно велик/aligned для supported address structures according to POSIX header contract. citeturn932665search1

## `bind` и address reuse

`bind` назначает local address. Server restart может столкнуться с address state/TIME_WAIT-like effects; `SO_REUSEADDR` имеет protocol/platform semantics и должен использоваться осознанно, а не как magic fix всех bind errors.

## `listen` backlog

`listen` переводит socket в passive/listening state. Backlog связан с pending connection queue semantics; не интерпретируй число как exact universal «максимум клиентов одновременно».

## Partial I/O снова

Connected socket использует тот же robustness mindset:

- send may be partial/error;
- recv may return any positive chunk up to buffer size;
- `0` = orderly peer shutdown;
- nonblocking later adds EAGAIN/EWOULDBLOCK.

## SIGPIPE

Writing to closed stream может trigger `SIGPIPE`/`EPIPE` depending API/options. Server должен иметь explicit policy, а не неожиданно погибать целиком из-за одного client.

## Lab — echo

Сделай:

- address-independent server;
- sequential accept loop;
- one connection at a time initially;
- client;
- full/partial I/O helpers;
- clean close/error paths.

Test IPv4 и, если environment configured, IPv6 localhost.

## Causal questions

1. Почему listening fd нельзя использовать как «fd конкретного клиента»?
2. Почему resolve возвращает список candidates?
3. Что ownership policy для accepted fd?
4. Почему `recv == 0` не error?

## Разбор

[`03-socket-api-getaddrinfo.solution.md`](03-socket-api-getaddrinfo.solution.md) содержит lifecycle checklist, не готовый server code.

## Exit check

Нарисуй resource ownership server: addrinfo list → listening socket → accepted socket → buffers → close.
