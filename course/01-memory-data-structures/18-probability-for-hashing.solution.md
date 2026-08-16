# Разбор упражнения 1.18

При capacity 8 и 6 active entries load factor `6/8 = 0.75` независимо от distribution. Но contiguous/probe-cluster или одинаковые start buckets могут дать намного больше probes, чем хорошо распределённые starts.

Именно поэтому instrumentation Hash Table позже считает probes, а не только `size/capacity`.
