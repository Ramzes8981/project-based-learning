# 2.6 — Как две программы соединяются bytes и почему лишний open end мешает EOF

**Теория:** ~90 мин · **Практика/project:** ~4–6 часов · **С телефона:** теория — да

← [`05-redirection-dup2.md`](05-redirection-dup2.md) · → [`07-signals-process-groups.md`](07-signals-process-groups.md)

## Проблема

For:

```bash
producer | consumer
```

producer stdout must become consumer stdin. Need kernel byte channel between processes.

## Pipe

`pipe(fds)` creates two descriptors:

```text
fds[0] read end
fds[1] write end
```

Bytes written to write end can be read from read end.

A pipe is a byte stream; it does not preserve arbitrary application “message” boundaries. This will later rhyme with TCP.

## Descriptor topology

For one pipeline:

```text
producer child:
  stdout (1) → pipe write end

consumer child:
  stdin  (0) ← pipe read end

parent shell:
  closes both pipe ends after forks
```

Every process must close every pipe end it does not need.

## EOF depends on all writers

Reader sees EOF only after **all** file descriptors referring to write end are closed.

Classic bug:

```text
producer exits
but parent accidentally keeps write end open
→ consumer read waits for more bytes
→ pipeline appears hung
```

This is why fd ownership/topology is correctness, not cleanup cosmetics.

## Avoid parent wait deadlock

Do not fork producer, wait for it to finish, then fork consumer when pipe can fill. Producer may block on full pipe because no consumer drains it while parent waits.

Correct rough order:

```text
create pipe
fork producer
fork consumer
parent closes pipe fds
parent waits/reaps children
```

## `SIGPIPE` preview

Writing when no reader exists may generate `SIGPIPE`/`EPIPE`. Detailed signal policy next lesson. For now recognize closed peer as normal pipeline failure mode.

## Практика

Implement exactly one pipe `cmd1 | cmd2` first. Test with enough output to exceed tiny assumptions and with commands that consume until EOF.

Разбор: [`06-pipes-fd-topology.solution.md`](06-pipes-fd-topology.solution.md).

## Causal questions

1. Why does parent retaining write end prevent EOF?
2. Why can waiting producer before starting consumer deadlock?
3. Why is pipe ownership naturally drawn as topology rather than only list of close calls?

## Exit check

Draw every fd after each fork and mark which process must close it.