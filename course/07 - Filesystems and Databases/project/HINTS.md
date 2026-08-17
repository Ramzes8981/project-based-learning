# SimpleDB — Hints

## Hint 1

Не начинай с B-tree. Сначала pager + one leaf page + persistence.

## Hint 2

Нарисуй exact byte offsets `FORMAT.md` и напиши маленькие encode/decode helpers before tree code.

## Hint 3

Для split удобно сначала собрать sorted logical records old+new, затем распределить по two leaves. Оптимизировать in-place позже.

## Hint 4

При descent сохраняй path/parent info или parent_page — нужно будет propagate separator.

## Hint 5

Если tree ломается только после reopen, сравни logical in-memory state с hex bytes на disk: bug вероятно serialization/layout, а не search algorithm.
