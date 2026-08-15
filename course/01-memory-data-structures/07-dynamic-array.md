# 1.7 — Dynamic Array / Vector

**Теория:** ~50 мин  
**Exercise:** ~30 мин  
**Mini-milestone:** ~4–8 часов суммарно  
**С телефона:** теория — да; milestone — ПК

← [`06-undefined-behavior-debugging.md`](06-undefined-behavior-debugging.md) · → [`08-linked-structures.md`](08-linked-structures.md)

## Цель

Понять `size`, `capacity`, geometric growth и amortized cost через собственный маленький Vector implementation.

## Fixed vs dynamic

Fixed array:

```text
capacity известна заранее
memory contiguous
resize отсутствует
```

Dynamic array добавляет metadata:

```text
data pointer
size      — сколько элементов логически хранится
capacity  — сколько элементов помещается в allocation
```

Invariant:

```text
0 <= size <= capacity
```

## Push

Если `size < capacity`, новый element записывается в `data[size]`, затем size увеличивается.

Если `size == capacity`, сначала нужна большая allocation.

## Почему capacity обычно растёт геометрически

Плохая стратегия:

```text
capacity += 1 при каждом переполнении
```

Тогда при последовательных pushes придётся постоянно копировать всё больше элементов; суммарная работа растёт квадратично по числу push.

Геометрическая стратегия:

```text
1 -> 2 -> 4 -> 8 -> 16 -> ...
```

делает resize редким. Отдельный resize дорогой `O(n)`, но средняя стоимость последовательного `push` в amortized sense остаётся `O(1)`.

Интуиция суммы копирований до capacity `2^k`:

```text
1 + 2 + 4 + ... + 2^(k-1) < 2^k
```

То есть общий объём копирования того же порядка, что итоговое число элементов, а не `n^2`.

## Overflow и growth

Перед doubling нужно проверить:

- `capacity * 2` не overflow;
- `new_capacity * sizeof(element)` не overflow;
- allocation failure обработан.

## `realloc` и invalidated pointers

После successful `realloc` old address может стать invalid, потому что data могла переместиться.

Следовательно, external pointers на elements vector могут стать dangling после push/resize. Это важная API-семантика.

## Causal questions

1. Чем `size` отличается от `capacity`?
2. Почему `push` иногда `O(n)`, но amortized считается `O(1)`?
3. Какие pointers могут стать invalid после resize?
4. Почему growth factor 2 — policy, а не закон природы?

## Exercise — growth trace

Без кода составь таблицу для pushes 1..20 при initial capacity 1 и doubling policy:

```text
push index | size before | capacity before | resize? | capacity after
```

Посчитай суммарное число элементов, которые пришлось бы копировать на resizes.

Затем сравни со стратегией `capacity += 1` качественно и формулой суммы `1 + 2 + ... + (n-1)`.

Разбор: [`07-dynamic-array.solution.md`](07-dynamic-array.solution.md).

## Mini-milestone

Теперь выполни [`project/vector/SPEC.md`](project/vector/SPEC.md).

Не открывай готовые implementations `std::vector`/чужих tutorial'ов для копирования. Standard library можно использовать только как reference поведения/идей после своего design.

## Exit check

Нарисуй Vector до и после resize, включая old/new data address и какие aliases стали недействительными.
