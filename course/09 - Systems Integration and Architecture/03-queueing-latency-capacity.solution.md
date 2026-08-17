# Разбор 9.3

Пример:

```text
lambda = 500 req/s
W = 40 ms = 0.04 s
L = 500 * 0.04 = 20 in-flight requests average
```

Если система утверждает steady throughput 10k req/s, average latency 1 s и при этом «в системе никогда больше 20 requests», measurements/definitions inconsistent: Little's Law ожидает около 10k average items under those definitions.

Проверяй, что latency population и throughput population относятся к одному workload/window.
