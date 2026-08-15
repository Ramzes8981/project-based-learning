# 2.3 — `fork`, `exec`, `waitpid`: модель процессов

**Теория:** ~75 мин  
**Упражнение:** ~75 мин  
**Project slice:** ~45 мин  
**С телефона:** теория — да

← [`02-terminal-termios.md`](02-terminal-termios.md) · → [`04-shell-repl-parser.md`](04-shell-repl-parser.md)

## Цель

Понять классическую Unix-композицию: process создаётся через `fork`, затем child может заменить свой process image через `exec`, а parent наблюдает termination через `waitpid`.

## Program vs process

Program/executable — код/данные в файле.

Process — выполняющийся экземпляр с PID, address space, registers, descriptor table и другими kernel-managed attributes.

## `fork`

```c
pid_t pid = fork();
```

После success **оба процесса продолжают выполнение с точки после `fork`**, но return value различается:

```text
parent: pid > 0  (child PID)
child:  pid == 0
failure: pid == -1 (только caller, child не создан)
```

Child получает отдельный process identity и логически отдельное address space. Modern kernels обычно используют copy-on-write оптимизацию: memory pages физически не обязаны копироваться немедленно.

## File descriptors после `fork`

Child получает свои descriptor entries, которые относятся к тем же underlying open file descriptions для inherited FDs. Поэтому file offset/state sharing может удивить.

Это особенно важно для pipes/redirection.

## Multithreaded `fork` nuance

Позже после concurrency module важно помнить: child многопоточного процесса содержит только вызывавший thread, но унаследованное memory state может включать locks в сложном состоянии. Поэтому между `fork` и `exec` в таком child разрешён очень ограниченный набор async-signal-safe операций.

Наш shell сейчас single-threaded, поэтому не усложняем implementation, но фиксируем границу применимости.

## `exec`

`exec*` family **не создаёт новый process**. Она заменяет текущий process image новым executable image.

```text
child PID остаётся тем же
старый program image заменяется новым
успешный exec не возвращается
```

Если `exec` вернулся — произошла ошибка.

Для shell удобно `execvp`, потому что он делает PATH search. Но помни: environment/PATH являются частью execution context и security model.

## `argv`

Program получает argument vector:

```text
argv[0] program-like name/path convention
argv[1..] arguments
argv[argc] == NULL
```

`exec` functions требуют корректно сформированный null-terminated argv pointer array.

## `waitpid`

Parent должен reap child state:

```c
waitpid(child_pid, &status, 0);
```

Status не является просто exit code. Используют macros:

```text
WIFEXITED
WEXITSTATUS
WIFSIGNALED
WTERMSIG
```

## Zombie

После termination kernel сохраняет минимальную process status information до `wait`/`waitpid`. Не reaped child становится zombie entry.

Zombie почти не «ест RAM приложения», но расходует process table/kernel bookkeeping и показывает неправильный lifecycle.

## Exercise — process launcher

Напиши программу:

```text
launcher /bin/echo hello
```

которая:

1. fork;
2. child exec выбранной команды;
3. при exec failure child печатает error и завершает через `_exit`;
4. parent waitpid;
5. parent различает normal exit/signal termination.

Почему `_exit` после failed exec в child предпочтительнее обычного buffered library `exit` в forked context — зафиксируй как API nuance.

Разбор: [`03-fork-exec-wait.solution.md`](03-fork-exec-wait.solution.md).

## Project slice

Создай первый shell execution path: hard-coded argv → fork → execvp → waitpid. Parser/prompt добавим следующим уроком.

## Exit check

Нарисуй process tree до `fork`, сразу после `fork`, после successful child `exec` и после `waitpid`.
