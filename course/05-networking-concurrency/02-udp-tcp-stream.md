# 5.2 — UDP и TCP: datagram vs byte stream

**Теория:** ~80 мин  
**Exercise:** ~45 мин  
**С телефона:** да

← [`01-link-ip-routing.md`](01-link-ip-routing.md) · → [`03-socket-api-getaddrinfo.md`](03-socket-api-getaddrinfo.md)

## Цель

Перестать воспринимать TCP как «надёжные сообщения» и понять, почему application framing — ответственность application protocol.

## UDP

UDP предоставляет datagrams: одна отправка создаёт datagram boundary, которую receiver получает как datagram, если она доставлена. Сам UDP не обещает delivery, ordering или retransmission.

Это не «плохой TCP»: DNS, real-time media и custom protocols могут выбирать datagram semantics сознательно.

## TCP

TCP connection предоставляет ordered reliable **byte stream**.

Если sender сделал:

```text
send 100 bytes
send 50 bytes
```

receiver не имеет contract получить именно `100`, затем `50` bytes одним-в-один. `recv` может вернуть любой положительный chunk доступного stream вплоть до requested buffer size.

```text
30 + 120
150
80 + 70
...
```

Order bytes сохраняется, boundaries `send` — нет.

`recv == 0` после чтения уже buffered data означает orderly peer shutdown на stream side. Negative result означает error; для nonblocking режима отдельными нормальными состояниями станут `EAGAIN/EWOULDBLOCK`.

## Reliability mechanisms intuition

TCP internally использует sequence numbers, acknowledgements, retransmission, flow control и congestion control. Application получает stream abstraction, а не обязана самостоятельно собирать lost packets.

### Flow control

Не даёт sender переполнить advertised receive capacity peer.

### Congestion control

Адаптирует sending behavior к network path congestion.

Это разные feedback problems.

## Connection lifecycle

Application обычно видит `connect/accept`, а kernel ведёт TCP state machine. Classic three-way handshake — полезная модель establishment, но не повод вручную реализовывать TCP в socket application.

## Half-close

TCP full-duplex. `shutdown` может запретить дальнейшую send/receive direction отдельно; `close` освобождает descriptor reference. Это важно для protocols, где одна сторона сообщает EOF, но ещё читает response.

## Head-of-line blocking

TCP обязан выдавать application bytes по порядку. Если segment потерян, более поздние bytes не могут быть delivered application раньше gap, даже если физически уже пришли.

## Exercise

Protocol: JSON message 1–100 KiB.

Объясни, почему неверно:

```text
recv(fd, buf, 65536)
parse buffer as exactly one JSON message
```

Спроектируй delimiter framing и length-prefix framing. Для каждого перечисли partial read, multiple messages per recv, overlong message, EOF mid-message.

Разбор: [`02-udp-tcp-stream.solution.md`](02-udp-tcp-stream.solution.md).

## Exit check

TCP гарантирует ordered stream bytes; application message boundaries создаёт наш protocol/parser.
