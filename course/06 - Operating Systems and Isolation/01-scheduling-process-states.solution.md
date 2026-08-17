# Разбор 6.1

FCFS:

```text
A 0..8
B 8..10
C 10..11
```

Response:

```text
A 0
B 7
C 8
```

Turnaround:

```text
A 8
B 9
C 9
```

При non-preemptive SJF с arrival constraints A уже стартовал в t=0 и не прерывается, поэтому до t=8 картина та же; затем C перед B:

```text
A 0..8
C 8..9
B 9..11
```

Это хороший reminder: scheduling policy + preemption assumptions меняют answer. Нельзя говорить «SJF» без модели.
