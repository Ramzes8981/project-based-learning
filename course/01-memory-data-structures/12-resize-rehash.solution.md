# Разбор 1.12

Главная идея resize:

```text
old table remains owner/valid
        ↓
allocate fresh table
        ↓
reinsert OCCUPIED entries using new capacity
        ↓
only after success switch owner metadata
        ↓
free old storage
```

Порядок важен для failure safety. Если сначала разрушить old table, а затем allocation fail, данные потеряны.

`hash % capacity` объясняет rehash: тот же hash при другой capacity может дать другой starting bucket.
