# 1.7 — Как сделать массив, который умеет расти

**Теория:** ~65 мин  
**Практика/project:** ~4–6 часов  
**С телефона:** теория — да; project — ПК

← [`06-undefined-behavior-debugging.md`](06-undefined-behavior-debugging.md) · → [`08-linked-structures.md`](08-linked-structures.md)

## Проблема

Теперь мы умеем выделить `N` элементов, но заранее не знаем, сколько элементов понадобится. Делать `realloc` на каждый `push` можно, но это заставит слишком часто копировать/move storage.

Нужно различать:

```text
len      — сколько элементов реально есть
capacity — сколько элементов помещается в текущем allocation без нового роста
```

Термин **ёмкость (capacity)** появляется здесь впервые, потому что теперь у нас действительно есть растущий allocation.

## Модель Vector

```c
typedef struct {
    int *data;
    size_t len;
    size_t capacity;
} IntVector;
```

Invariants:

```text
len <= capacity
capacity == 0 => data may be NULL
valid elements are data[0..len)
owner of data is the vector
```

## Grow before write

`push` сначала гарантирует место, только затем пишет:

```text
if len == capacity:
    choose new capacity
    checked bytes calculation
    realloc through temporary pointer
write data[len]
len += 1
```

Если grow failed, прежний vector должен остаться валидным и логически неизменённым.

## Почему обычно растут геометрически

Если увеличивать allocation на один element каждый раз, последовательность `N` pushes может многократно копировать почти весь старый массив.

Рост примерно в 2 раза делает дорогие moves редкими. Это приводит к **амортизированной стоимости (amortized cost)**: отдельный `push` иногда дорогой, но средняя стоимость длинной последовательности остаётся близкой к constant.

Формальный complexity framework будет в 1.10; здесь нужна только интуиция.

## Pointer invalidation

После grow старый `data` мог переместиться. Любой ранее сохранённый pointer на element нужно считать invalid, если API не гарантирует обратное.

Это должно быть написано в public contract Vector.

## Project

Выполни [`project/vector/SPEC.md`](project/vector/SPEC.md), затем acceptance/tests. Не копируй full implementation из hints: student owns milestone code.

## Causal questions

1. Почему `len` и `capacity` нельзя объединить в одно поле?
2. Почему `push` должен менять `len` только после успешного grow/write?
3. Почему pointer на `data[0]` может стать dangling после successful `realloc`?
4. Почему geometric growth уменьшает число full-array moves?

## Exit check

Ты можешь нарисовать state transition `len == capacity` → grow success/failure и назвать invariants до и после.