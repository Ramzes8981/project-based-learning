# Разбор упражнения 1C.2

Хороший Hash Table regression после bug с tombstone:

```text
insert A and colliding B
remove A
assert get(B) succeeds
```

Он сохраняет конкретный исторический failure. Более общее property дополняет его: после произвольной последовательности successful inserts/removes каждый active key из reference model должен находиться с тем же value.
