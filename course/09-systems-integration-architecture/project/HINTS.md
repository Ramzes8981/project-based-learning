# Persistent KV Service — Hints

Открывай следующий hint только после собственной попытки.

## Hint 1

До `main.c` ответь: какой workload и guarantee ты проверяешь? Если ответа нет — рано выбирать architecture.

## Hint 2

Reuse старых проектов означает reuse **контрактов/небольших компонентов после review**, а не склейку нескольких `main()`.

## Hint 3

Если concurrency ломает state, сначала нарисуй owner и все пути mutation. Mutex — инструмент после модели, не замена модели.

## Hint 4

Если p99 плохой, измерь queue wait отдельно от service work прежде чем увеличивать worker count.

## Hint 5

Если persistence слишком сложен, сузь guarantee. Простой проверяемый snapshot/log лучше «почти WAL» без корректного recovery protocol.

## Hint 6

Любой length из network/storage сначала validation/overflow arithmetic, только потом allocation/copy/indexing.

## Hint 7

Если хочется второй node, сначала покажи график/measurement bottleneck одного node и сформулируй, кто станет owner state после масштабирования.