# Optional 1D — Почему случайные совпадения становятся вероятнее с ростом набора

**Статус:** optional deeper math; не prerequisite для core Hash Table.  
**Теория:** ~55 мин · **Практика:** ~45 мин · **С телефона:** да

← [`24-trie.md`](24-trie.md) · ↑ [`README`](README.md)

Hash Table уже изучена, поэтому теперь можно углубить probability intuition вокруг collisions/birthday effect без hidden prerequisite.

## Main ideas

- probability — модель неопределённости, а не гарантия конкретного run;
- expected value описывает средний результат по повторениям/распределению;
- collision probability растёт быстрее, чем интуитивное «занято x% buckets»;
- good hash distribution важна для cost, но correctness Hash Table **не может** зависеть от отсутствия collisions.

## Практика

Сравни несколько toy distributions при одинаковом load factor и объясни, почему один только `size/capacity` не говорит, сколько probes увидит конкретная таблица.

Разбор: [`25-probability-for-hashing.solution.md`](25-probability-for-hashing.solution.md).