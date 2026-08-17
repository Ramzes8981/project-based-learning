# Optional 1B — Как искать подстроку быстрее повторного полного сравнения

**Статус:** optional; не блокирует core.  
**Теория:** ~65 мин · **Практика:** ~60 мин · **С телефона:** да

← [`22-dynamic-programming.md`](22-dynamic-programming.md) · optional next → [`24-trie.md`](24-trie.md)

После core Hash Table идея hash уже знакома, поэтому Rabin–Karp теперь не требует знания из будущего.

## Проблема

Naive substring search для каждой допустимой start position сравнивает pattern и в некоторых inputs много раз повторяет одну и ту же работу.

KMP использует information о собственных prefix/suffix pattern, чтобы не откатывать input index бессмысленно.

Rabin–Karp сначала сравнивает rolling hash windows. Совпадение hash означает только candidate: из-за collisions точный поиск обязан подтвердить actual bytes.

## Systems takeaway

- проверять `pattern_len > text_len` **до** выражений вроде `text_len - pattern_len` с `size_t`;
- hash ускоряет candidate filtering, но collision не исчезает;
- algorithm choice зависит от pattern count/input model.

Практика/разбор: [`23-string-searching.solution.md`](23-string-searching.solution.md).