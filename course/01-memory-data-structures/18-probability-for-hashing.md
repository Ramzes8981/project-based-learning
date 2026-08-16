# Optional 1D — Почему случайные совпадения становятся вероятнее с ростом набора

**Статус:** optional deeper math. Минимум, нужный core Hash Table, есть в 1.16.  
**С телефона:** да

← [`17-trie.md`](17-trie.md) · ↑ [`README`](README.md)

Этот урок углубляет probability intuition вокруг collisions/birthday effect, но не является prerequisite для [`19-hashing-collisions.md`](19-hashing-collisions.md).

Main ideas:

- probability — модель неопределённости, а не гарантия конкретного run;
- expected value описывает средний результат по повторениям/распределению;
- collision probability растёт быстрее, чем интуитивное «занято x% buckets»;
- good hash distribution важна, но hash table correctness **не может** зависеть от отсутствия collisions.

Практика/разбор: [`18-probability-for-hashing.solution.md`](18-probability-for-hashing.solution.md).