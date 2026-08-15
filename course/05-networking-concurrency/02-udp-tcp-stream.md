# 5.2 — UDP и TCP: datagram vs byte stream

**Теория:** ~80 мин  
**Exercise:** ~45 мин  
**С телефона:** да

← [`01-link-ip-routing.md`](01-link-ip-routing.md) · → [`03-socket-api-getaddrinfo.md`](03-socket-api-getaddrinfo.md)

## Цель

Перестать воспринимать TCP как «надёжные сообщения» и понять, почему application framing — ответственность протокола приложения.

## UDP

UDP предоставляет datagram service:

```text
send datagram
→ network may deliver, drop, duplicate/reorder depending conditions
→ receiver gets datagram boundary when delivered
```

UDP не гарантирует reliability/ordering/retransmission сам по себе.

Это не делает UDP «плохим TCP»: real-time/media/DNS/custom protocols могут предпочитать его semantics.

## TCP

TCP connection предоставляет ordered reliable **byte stream**.

Ключевое слово — stream.

Если sender сделал:

```text
send 100 bytes
send 50 bytes
```

receiver не обязан увидеть:

```text
recv -> 100
recv -> 50
```

Возможны chunks:

```text
30, 120
150
80, 70
...
```

в рамках ordered stream semantics.

POSIX `recv` возвращает столько bytes, сколько реально доступно/получено в рамках API contract; orderly peer shutdown даёт `0`. citeturn932665search0

## Reliability intuition

TCP использует sequence numbers, acknowledgements, retransmission, flow control и congestion control.

Application видит ordered bytes, а не packet retransmission details.

## Flow control vs congestion control

Flow control защищает receiver buffer capacity.

Congestion control адаптирует sending rate к network path congestion.

Не смешивай их в одно «TCP сам регулирует скорость».

## Connection establishment

Classic conceptual handshake:

```text
SYN
SYN-ACK
ACK
```

Но application code обычно работает через `connect/accept`, а kernel реализует protocol state machine.

## Close

TCP двунаправленный. `shutdown` может закрывать только send/receive half; `close` освобождает descriptor reference. Peer `recv == 0` означает orderly shutdown receive side stream after buffered data drained.

## Head-of-line blocking

TCP сохраняет byte order. Потерянный segment может задерживать delivery последующих bytes application even if они физически arrived.

Это один trade-off stream reliability.

## Exercise

Дан application protocol, где message = JSON line 1–100 KiB.

Объясни, почему код:

```text
recv(fd, buf, 65536)
parse buf as one JSON message
```

неверен.

Предложи два framing designs:

- delimiter-based;
- length-prefixed.

Для каждого назови edge cases.

Разбор: [`02-udp-tcp-stream.solution.md`](02-udp-tcp-stream.solution.md).

## Exit check

Одной фразой: что TCP гарантирует application, а чего он **не** гарантирует про boundaries?
