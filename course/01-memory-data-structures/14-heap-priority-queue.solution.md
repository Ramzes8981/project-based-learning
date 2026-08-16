# Разбор упражнения 1.14

Для min-heap unit tests особенно полезна отдельная функция `heap_is_valid`: для каждого существующего child проверять `parent <= child`.

`parent(i)` вызывай только при `i > 0`; цикл sift-up естественно выглядит как «пока i > 0, вычислить parent и сравнить». Это предотвращает unsigned underflow на root.
