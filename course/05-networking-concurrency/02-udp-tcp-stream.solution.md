# Разбор 5.2

Delimiter framing требует:

- delimiter не может появиться unescaped в payload либо нужен escaping;
- parser должен хранить partial message между recv calls;
- нужен maximum message size, иначе peer может заставить buffer расти без bound.

Length prefix требует:

- fixed/endian-defined length field;
- validation `length <= MAX_FRAME` до allocation;
- обработку partial prefix и partial payload;
- integer-overflow checks.

Оба работают поверх TCP stream; выбор зависит от protocol goals.
