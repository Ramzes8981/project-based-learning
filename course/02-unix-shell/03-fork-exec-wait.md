# 2.3 — Как shell создаёт новый process и запускает в нём другую программу

**Теория:** ~90 мин · **Практика:** ~100 мин · **С телефона:** теория — да

← [`02-terminal-termios.md`](02-terminal-termios.md) · → [`04-shell-repl-parser.md`](04-shell-repl-parser.md)

## Проблема

Shell должен остаться жив после команды `ls`. Если он просто заменит себя `ls`, prompt исчезнет. Значит, нужен отдельный process for command and a way for parent shell to wait/observe result.

## `fork`: один process становится двумя execution flows

On POSIX systems `fork()` creates child process based on caller state.

Return distinguishes paths:

```text
< 0  failure, no child
= 0  child path
> 0  parent path; value is child PID
```

After fork both processes continue from following instruction, but they are separate processes. Memory is logically separate even if OS internally uses copy-on-write optimization.

## File descriptors across fork

Child inherits copies of parent's descriptor table entries referring to same underlying open-file descriptions/resources. Therefore open pipe/file descriptors before fork can establish later topology.

Important: separate fd numbers can refer to shared kernel open-file state; and closing an fd in one process does not automatically close corresponding inherited fd in another.

## `exec`: replace current process program image

`exec*` family does **not** create new process. On success it replaces current process's program image while preserving process identity and selected OS state such as open fds without close-on-exec.

Typical shell:

```text
parent shell
  ↓ fork
child
  ↓ setup redirection
  ↓ exec program
new program in child PID
```

If `exec` succeeds, code after it is not executed.

## Failure in child

If `exec` fails, child should report error and terminate without accidentally continuing parent-shell logic. In post-fork child, `_exit(status)` is often preferable to `exit` when avoiding duplicated stdio cleanup/buffers inherited from parent.

## `waitpid`: reap and observe

Parent uses `waitpid` to collect child termination state. Otherwise terminated child can remain as zombie entry until reaped.

Do not compare raw status directly with expected exit code. Use macros:

```c
if (WIFEXITED(status)) {
    int code = WEXITSTATUS(status);
}
if (WIFSIGNALED(status)) {
    int sig = WTERMSIG(status);
}
```

Retry `waitpid` on `EINTR` when appropriate.

## Error ownership

After successful fork:

- parent owns responsibility to reap child;
- child must either exec or terminate;
- both sides must close descriptors they no longer need.

## Практика

Write launcher for fixed command path/argv:

1. fork;
2. child `execvp`/chosen exec variant;
3. child reports exec error + `_exit(127)`;
4. parent loops `waitpid` with `EINTR` handling;
5. prints decoded exit/signal result.

Разбор: [`03-fork-exec-wait.solution.md`](03-fork-exec-wait.solution.md).

## Causal questions

1. Why does shell need fork before exec for ordinary foreground command?
2. What exactly does exec replace, and what does it not create?
3. Why must parent reap child?
4. Why can inherited fds matter to later pipe EOF?

## Exit check

Draw parent/child timeline for `shell → fork → child exec → parent wait → prompt`.