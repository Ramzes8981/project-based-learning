# Разбор упражнения Optional 1B

Для naive length-based search безопасный внешний цикл возможен только если `pattern_len <= text_len`; иначе выражение вроде `text_len - pattern_len` на `size_t` underflow.

После этой проверки start positions принадлежат `[0, text_len - pattern_len]`. Внутреннее сравнение должно оставаться внутри обоих explicit lengths.

Для Rabin–Karp равенство hash — только candidate. Collision является нормальной частью модели, поэтому подтверждение actual bytes обязательно для точного поиска.
