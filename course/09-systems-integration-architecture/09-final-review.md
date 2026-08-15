# 9.9 — Final Systems Engineering Review

**Время:** ~3–5 часов  
**С телефона:** часть review — да

← [`08-scaling-second-node.md`](08-scaling-second-node.md) · ↑ [`README`](README.md)

Финал проверяет не количество написанного C, а способность рассуждать вертикально через system layers.

## Capstone acceptance

Проверь [`project/ACCEPTANCE.md`](project/ACCEPTANCE.md).

## Vertical walkthrough

Выбери один `SET` request и проведи:

```text
client bytes
→ TCP stream/framing
→ socket fd
→ worker queue
→ synchronization
→ service logic
→ index/data structure
→ serialization/page/file
→ page cache/storage
→ response
```

На каждом layer ответь:

- state;
- ownership;
- failure;
- metric;
- resource cost.

## Incident scenarios

### 1. p99 вырос, CPU 30%

Предложи investigation plan через queue, storage, locks, network, faults.

### 2. Memory slowly grows

Отдели leak, queue growth, cache growth, connection leak, fragmentation.

### 3. Data missing after kill

Сверь durability acknowledgement contract, flush/recovery logs, storage format.

### 4. Server hangs under overload

Check deadlock vs blocked I/O vs full queue/backpressure vs storage stall.

### 5. Malformed request crashes server

Trace validation → integer/buffer handling → memory safety/tool evidence.

## Architecture defense

За 15–30 минут представить:

1. requirements;
2. architecture diagram;
3. state ownership;
4. protocol;
5. concurrency/backpressure;
6. persistence guarantee;
7. measured capacity;
8. failure tests;
9. observability;
10. top trade-offs;
11. next scaling step.

## Core completion gate

Курс core завершён, если ученик может сказать:

> Вот requirement. Вот implementation boundary. Вот evidence. Вот known failure/limitation. Вот alternative и почему сейчас я его не выбрал.

После этого advanced branches становятся осмысленными:

- Distributed Systems;
- Reverse Engineering/Binary Security;
- Kernel/OS;
- Rust systems deeper;
- Compilers;
- Embedded;
- Performance Engineering.
