# 2.6 — Pipes и descriptor topology

**Теория:** ~75 мин  
**Project slice:** ~4–7 часов  
**С телефона:** теория — да

← [`05-redirection-dup2.md`](05-redirection-dup2.md) · → [`07-signals-process-groups.md`](07-signals-process-groups.md)

## Цель

Научиться строить pipeline через `pipe`, `fork`, `dup2`, `close` и понимать EOF как свойство открытых write ends.

## `pipe`

```c
int fds[2];
pipe(fds);
```

Conceptually:

```text
fds[0] -> read end
fds[1] -> write end
```

Bytes, записанные в write end, читаются из read end FIFO-like stream.

Pipe — byte stream: message boundaries не гарантируются автоматически.

## `A | B`

Нужно:

```text
A stdout -> pipe write
B stdin  -> pipe read
```

Process topology:

```text
A process --fd1--> [pipe] --fd0--> B process
```

Parent shell создаёт pipe до fork children, чтобы они унаследовали необходимые descriptors.

## Критическое правило close unused ends

После fork каждый process наследует copies fd entries.

Если parent или B process оставит **лишний write end pipe открытым**, reader B может не получить EOF даже после termination A: kernel всё ещё видит хотя бы одного open writer reference.

Это классический shell deadlock/hang.

## Почему wait order важен

Плохая идея для pipeline:

```text
fork A
wait A
fork B
```

Если A пишет больше pipe capacity и B ещё не читает, A блокируется, parent ждёт A, B никогда не запускается → deadlock.

Оба pipeline processes должны работать concurrently, затем shell waits.

## N-stage pipeline

Для `A | B | C` нужны два pipes.

У process i:

- stdin от previous pipe, если есть;
- stdout в next pipe, если есть;
- все unrelated pipe FDs закрыты.

Полезно проектировать topology сначала как graph/table, а потом писать loop.

## Pipe errors

Writing когда readers отсутствуют может привести к `SIGPIPE`/`EPIPE` в зависимости signal handling. Это позже обсуждаем вместе с signals.

## Project slice

Core минимум:

```text
A | B
```

После стабильной версии — transfer/N-stage pipeline.

Обязательно:

- create pipe;
- fork both children;
- correct `dup2`;
- close unused FDs в parent/children;
- wait both;
- no hanging due to leaked pipe ends.

## Causal questions

1. Почему extra writer fd удерживает EOF?
2. Почему нельзя ждать A до запуска B?
3. Почему child должен закрывать unrelated ends даже если «не использует их в коде»?
4. Чем pipe похож на TCP byte stream концептуально?

## Exercise

Нарисуй таблицу FDs для:

```text
printf data | wc -c
```

Rows: parent, child A, child B. Columns: stdin/stdout/pipe read/pipe write. Отметь, что закрывается в каждом процессе.

Разбор: [`06-pipes-fd-topology.solution.md`](06-pipes-fd-topology.solution.md).

## Exit check

Если pipeline зависает, первое диагностическое действие — нарисовать/inspect все живые pipe endpoints, а не добавлять random sleeps.
