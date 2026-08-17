# Optional 1C — Когда общий префикс стоит хранить как структуру

**Статус:** optional; не блокирует core.  
**Теория:** ~45 мин · **Практика:** ~60 мин · **С телефона:** да

← [`23-string-searching.md`](23-string-searching.md) · optional next → [`25-probability-for-hashing.md`](25-probability-for-hashing.md)

## Проблема

Если workload постоянно спрашивает «какие ключи начинаются с этого prefix?», обычный exact-key lookup отвечает не на тот вопрос.

**Trie** хранит prefix state как путь: node представляет уже прочитанный prefix, edge — следующую unit.

Такой trade-off полезен для autocomplete, dictionaries и routing-prefix-like задач. Cost lookup зависит главным образом от key length, но memory overhead child structures может быть большим.

В Unicode systems сначала нужно решить, что такое unit: raw UTF-8 byte, Unicode code point или другая normalized representation. Нельзя автоматически считать `char` = character.

Практика/разбор: [`24-trie.solution.md`](24-trie.solution.md).