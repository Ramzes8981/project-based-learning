# 9.9 — Финальная инженерная защита

**Время:** ~3–5 часов · **С телефона:** подготовка — частично

← [`08-scaling-second-node.md`](08-scaling-second-node.md) · ↑ [`README`](README.md)

Финал проверяет не количество C-кода, а способность объяснить систему причинно.

## 1. Acceptance

Пройди [`project/ACCEPTANCE.md`](project/ACCEPTANCE.md) и приложи воспроизводимые evidence.

## 2. Один request через все слои

Возьми один `SET` и проведи его:

```text
client bytes
→ TCP stream
→ framing/parser
→ bounded queue / worker
→ synchronization
→ KV state/index
→ serialization/storage
→ page cache/durability boundary
→ response
```

На каждом шаге назови:

- state;
- owner;
- resource bound;
- possible failure;
- observable signal.

## 3. Incident walkthroughs

Разбери без запуска кода сначала как hypothesis tree:

- p99 вырос, CPU невысок;
- memory постепенно растёт;
- acknowledged data пропали после kill;
- server «завис» под overload;
- malformed frame приводит к crash.

Затем скажи, какие measurements/tools отличат гипотезы.

## 4. Architecture defense

За 15–30 минут объясни:

1. requirements/workload;
2. boundaries/state ownership;
3. protocol/retry semantics;
4. concurrency/backpressure;
5. persistence guarantee;
6. measurements;
7. failure tests;
8. observability;
9. top trade-offs/ADRs;
10. security limitations;
11. next scaling decision.

## Completion gate

Ты должен уметь сказать:

> Вот требование. Вот механизм. Вот evidence. Вот failure/limitation. Вот alternative и причина, почему сейчас выбран не он.

После этого advanced branches — Distributed Systems, deeper RE/binary security, kernel, embedded, compilers, deeper Rust/performance — становятся естественным продолжением.