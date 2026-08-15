# Разбор 2.3

Control flow:

```text
pid = fork()
├─ -1: parent/caller handles failure
├─  0: child
│      execvp(...)
│      if returned -> perror -> _exit(127-like chosen status)
└─ >0: parent
       waitpid(pid, &status, 0)
       inspect WIFEXITED/WIFSIGNALED
```

Ключевая ошибка новичка — написать code после `fork` без разветвления и случайно выполнить его в обоих processes.

Successful `exec` не возвращает управление старому child code.
