# 5.1 — Как packet выбирает следующий шаг к другой машине

**Теория:** ~75 мин · **Практика:** ~70 мин · **С телефона:** теория — да

← [`README`](README.md) · → [`02-udp-tcp-stream.md`](02-udp-tcp-stream.md)

## Проблема

Process on one host has bytes for another host. A cable/Wi-Fi link only reaches a local network segment; the destination may be many networks away.

Need answer two different questions:

```text
who is the next local receiver?
where should an IP packet go next toward its final destination?
```

## Link layer first

A local network technology such as Ethernet moves frames between interfaces on the same link. It has its own local addressing/format. Core does not implement Ethernet; we only need boundary: local delivery is not global routing.

## IP address identifies network-layer destination

Internet Protocol (IP) gives packets source/destination addresses and allows routers to forward them across networks.

An **IP packet** is a network-layer unit. It is not a TCP message and not an application record.

## Prefix and route

A route says roughly:

```text
for destination prefix P
→ send via interface / next hop
```

Routers choose the most specific matching prefix (longest-prefix match) among available routes.

Example mental model:

```text
app bytes
↓
transport later
↓
IP packet: destination 203.0.113.7
↓ route lookup
next hop / interface
↓ local link delivery
```

## Default route

If no more-specific route matches, a default route may select gateway/next hop. It is not “the Internet address”; it is fallback routing policy.

## TTL / hop limit

Packets need a bound against routing loops. IPv4 TTL / IPv6 Hop Limit is decremented by routers; reaching zero prevents infinite forwarding.

## Graph connection

Routing topology can be modeled as graph. BFS/Dijkstra intuition was introduced in Module 1; networking now supplies a real use case. Real routing protocols have policy/state details beyond simple shortest-path exercise.

## Observe, do not memorize commands

On Linux use tools available in environment such as:

```bash
ip addr
ip route
```

Before reading output, predict which interface/default route should exist. Commands are observation tools, not the lesson itself.

## Практика

1. Pick one destination from your test environment.
2. Read `ip route` and identify matching route/default.
3. Draw host → next hop → hypothetical later routers.
4. Explain why local MAC/link address and final IP address answer different questions.

## Exit check

Why can a host know final IP destination while still sending the next frame only to a local router?