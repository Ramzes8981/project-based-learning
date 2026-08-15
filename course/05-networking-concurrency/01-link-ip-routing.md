# 5.1 — Ethernet, ARP, IP, subnet и routing

**Теория:** ~75 мин  
**Lab:** ~45–60 мин  
**С телефона:** теория — да

← [`README`](README.md) · → [`02-udp-tcp-stream.md`](02-udp-tcp-stream.md)

## Цель

Понять путь данных от local link frame до routed IP packet и уметь объяснить решение host: destination local или нужен gateway.

## Layering без зубрёжки OSI

Практическая цепочка:

```text
application data
↓ transport (TCP/UDP)
↓ IP packet
↓ link frame (например Ethernet/Wi-Fi-like link)
↓ physical/network medium
```

Layers имеют разные addressing/contract scopes.

## Ethernet frame

На Ethernet-like local network frame содержит source/destination MAC addresses и payload type/data.

MAC address используется в пределах link/local segment; router не маршрутизирует Internet «по MAC адресам от source до destination».

## IP address

IPv4 address — 32-bit logical network address. Prefix length определяет network/subnet часть.

Например:

```text
192.168.1.23/24
```

`/24` означает 24 high-order bits network prefix.

## Local-subnet decision

Host сравнивает destination prefix со своим connected route/prefix.

Если destination считается on-link:

```text
host должен узнать link-layer address destination
```

Если off-link:

```text
host отправляет frame к next-hop/default gateway MAC,
но IP destination остаётся конечным remote host
```

Это ключевой conceptual distinction.

## ARP

Для IPv4 Ethernet ARP сопоставляет local IPv4 address → MAC address.

Conceptually:

```text
Who has 192.168.1.50?
→ owner replies with MAC
→ sender caches mapping temporarily
```

ARP не работает как global Internet directory.

## Routing table

Routing decision выбирает route с наиболее специфичным подходящим prefix (longest-prefix match concept).

Route может задавать:

- destination prefix;
- next hop;
- interface;
- metric.

## TTL

IPv4 TTL уменьшается routers; при исчерпании packet удаляется. Это предотвращает вечную циркуляцию routing loops.

## ICMP

ICMP передаёт control/error information: echo request/reply, destination-related errors, time exceeded и др.

`ping` использует ICMP echo, но «ping не проходит» не означает автоматически «TCP service недоступен»: firewalls/policies могут отличаться.

## NAT preview

NAT меняет address/port mappings на network boundary. Он важен practically, но не является свойством базовой end-to-end IP model. Detailed NAT/firewall work позже в security/sysadmin tracks.

## Lab

На Linux:

```text
ip addr
ip route
ip neigh
```

Выбери один destination в local subnet и один remote. До любого packet capture ответь:

- какой route будет выбран;
- кому нужен ARP/neighbor resolution;
- какой MAC будет destination первого Ethernet frame;
- какой IP останется final destination.

При возможности проверь packet capture.

## Causal questions

1. Почему frame к default gateway всё ещё содержит IP remote server?
2. Зачем TTL?
3. Почему ARP не нужен для поиска MAC remote Internet server?
4. Что изменится, если prefix mask настроен неправильно?

## Exit check

Нарисуй local host → router → remote host и подпиши link-layer vs IP destination на каждом hop.
