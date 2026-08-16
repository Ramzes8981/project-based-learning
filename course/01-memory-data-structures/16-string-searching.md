# Optional 1B — Как искать подстроку быстрее повторного полного сравнения

**Статус:** optional; не блокирует core.  
**С телефона:** да

← [`15-dynamic-programming.md`](15-dynamic-programming.md) · optional next → [`17-trie.md`](17-trie.md)

Сначала naive substring search: для каждой допустимой start position сравнить pattern. Worst-case может повторять одну и ту же работу.

KMP использует information о собственных prefix/suffix pattern, чтобы не откатывать input index бессмысленно. Rabin–Karp сначала сравнивает rolling hash windows, но hash match требует verification из-за collisions.

Ключевой systems takeaway:

- проверять `pattern_len > text_len` **до** выражений вроде `text_len - pattern_len` с `size_t`;
- hashing ускоряет candidate filtering, но collision означает необходимость final byte comparison;
- algorithm choice зависит от pattern count/input model.

Практика/разбор остаются в [`16-string-searching.solution.md`](16-string-searching.solution.md).