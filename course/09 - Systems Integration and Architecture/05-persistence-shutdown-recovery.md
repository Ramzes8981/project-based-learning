# 9.5 — Когда можно честно сказать «запись сохранена»

**Теория:** ~80 мин · **Project/failure lab:** ~3–5 часов · **С телефона:** да

← [`04-backpressure-timeouts-overload.md`](04-backpressure-timeouts-overload.md) · → [`06-observability-sli-slo.md`](06-observability-sli-slo.md)

## Проблема

Server ответил `OK` на `SET`. Через секунду питание пропало.

Должно ли значение сохраниться?

Без заранее определённого durability contract правильного ответа нет.

## Разные уровни обещания

`OK` может означать, например:

```text
изменено только in-memory state
bytes переданы kernel/page cache
fsync-complete согласно выбранному protocol
```

Эти гарантии различаются по latency и поведению при failure.

## Graceful shutdown

Нормальное завершение — тоже protocol:

```text
1. отметить shutting down
2. перестать принимать новую работу
3. drain/reject queued work по policy
4. дождаться workers
5. выполнить storage flush/sync по contract
6. закрыть resources
7. exit
```

Если закрыть storage раньше workers, получится race/use-after-close логического ресурса.

## Forced termination

`SIGKILL`, crash или power loss обходят cleanup code. Recovery зависит от persistent format/protocol, а не от надежды на destructor/`close()`.

SimpleDB из предыдущего модуля не превращается автоматически в transactional engine.

## Допустимые core strategies

### Snapshot

```text
state → temp file → sync → replace old snapshot
```

Плюсы: простая recovery модель. Минусы: стоимость O(data size), потеря изменений после последнего snapshot в зависимости от policy.

### Append-only mutation log

```text
append record → replay on startup → periodic compaction/snapshot
```

Плюсы: incremental writes. Минусы: growth, partial tail, checksums/versioning/replay policy.

Можно также аккуратно переиспользовать ограниченный SimpleDB contract.

## Corrupt input

Persistent bytes после crash/manual damage нельзя считать доверенными. Startup parser обязан проверять magic/version/lengths/offset arithmetic до доступа к данным.

## Failure lab

Испытай на **копиях** данных:

- clean restart;
- graceful SIGTERM;
- forced kill;
- truncated file;
- bit flip/corruption;
- injected write/sync failure.

## Exit check

Сформулируй одной фразой: **после какого acknowledgement и при каких failures какие writes гарантированно сохраняются?**