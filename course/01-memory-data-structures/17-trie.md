# Optional 1C — Когда общий префикс стоит хранить как структуру

**Статус:** optional; не блокирует core.  
**С телефона:** да

← [`16-string-searching.md`](16-string-searching.md) · optional next → [`18-probability-for-hashing.md`](18-probability-for-hashing.md)

**Trie** полезен, когда workload естественно спрашивает по prefixes: autocomplete, routing-prefix-like structures, dictionaries.

Node represents prefix state; edge represents next symbol/unit. Cost зависит от key length rather than number of stored keys, но memory overhead может быть большим из-за child structures.

В реальных Unicode systems сначала нужно решить, что такое «symbol» для trie: raw UTF-8 byte, Unicode code point или другая normalized unit. Нельзя автоматически считать `char` = character.

Практика/разбор: [`17-trie.solution.md`](17-trie.solution.md).