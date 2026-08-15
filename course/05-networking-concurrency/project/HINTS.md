# Concurrent KV Server — Hints

## Hint 1

Сначала sequential framed server. Concurrency поверх broken framing только усложнит debug.

## Hint 2

Выдели helpers/state для `read_exact/write_all` в blocking version.

## Hint 3

Worker должен стать owner client fd после dequeue. До этого ownership у acceptor/queue path.

## Hint 4

Не держи store mutex во время socket I/O.

## Hint 5

Если overload «лечится» увеличением queue без bounds, ты переносишь проблему в latency/memory.
