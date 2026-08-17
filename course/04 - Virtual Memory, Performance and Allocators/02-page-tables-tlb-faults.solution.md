# Разбор 4.2

При 4096-byte pages:

```text
0    -> page 0 offset 0
4095 -> page 0 offset 4095
4096 -> page 1 offset 0
8193 -> page 2 offset 1
```

TLB miss означает отсутствие cached translation; page-table walk может успешно найти present mapping без kernel-visible fault.

COW: до write два virtual mappings могут ссылаться на один physical frame; write fault приводит к private copy для writer и обновлению mapping.
