# 1.14 — Как быстро получать самый приоритетный элемент

**Теория:** ~65 мин  
**Практика:** ~75 мин  
**С телефона:** теория — да; практика — ПК

← [`13-bst-traversals-balanced-trees.md`](13-bst-traversals-balanced-trees.md) · → [`19-hashing-collisions.md`](19-hashing-collisions.md)

## Проблема

Scheduler/task queue часто не просит «найди key X» или «держи всё полностью sorted». Ему нужно другое:

```text
быстро добавить item
быстро получить item с минимальным/максимальным priority
```

Полностью сортировать после каждого insert избыточно.

## Priority queue

ADT с операциями вроде:

```text
push(item, priority)
peek_best()
pop_best()
```

Одна распространённая implementation — **binary heap**.

Не путай binary heap data structure с разговорным словом `heap` для dynamically allocated memory. Это два разных concepts.

## Array representation

Для zero-based array:

```text
left(i)  = 2*i + 1
right(i) = 2*i + 2
parent(i)= (i-1)/2, только если i > 0
```

Min-heap invariant:

```text
parent <= each child
```

Отсюда minimum всегда в index 0, но остальная array **не полностью sorted**.

## Push / pop

`push` добавляет element в конец и поднимает его, пока heap invariant не восстановлен.

`pop_min` заменяет root последним element и опускает его вниз.

Высота complete binary tree `O(log n)`, поэтому push/pop typically `O(log n)`, peek `O(1)`.

## Arithmetic safety

Не вычисляй child index, если multiplication/addition может выйти за `size_t`. На практике compare against `len` and derive only when parent can have a child; для course heap with realistic allocated lengths bounds already ограничивают индексы, но reasoning должно быть явным.

Никогда не вычисляй `(i - 1)` при `i == 0` для unsigned `size_t`.

## Практика

Реализуй min-heap поверх Vector-like storage и проверь heap invariant после каждого mutation в tests.

Разбор: [`14-heap-priority-queue.solution.md`](14-heap-priority-queue.solution.md).

## Exit check

Почему heap позволяет быстро получить minimum, хотя весь array не отсортирован?