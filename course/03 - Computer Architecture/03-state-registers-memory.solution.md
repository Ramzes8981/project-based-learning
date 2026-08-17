# Разбор 3.3

Один trace:

```text
initial: R0=0 R1=0 PC=0
LOADI R0,5 -> R0=5 PC=1
LOADI R1,7 -> R1=7 PC=2
ADD R0,R1 -> R0=12 R1=7 PC=3
```

Это intentionally simple sequential machine. Реальный CPU может fetch/execute overlap, но architectural state должен выглядеть так, будто instructions соблюдают ISA semantics.
