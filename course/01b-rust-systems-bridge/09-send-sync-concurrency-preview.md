# Optional 1B.X — Почему некоторые Rust types нельзя бездумно переносить между threads

**Статус:** optional preview. Core `Send`/`Sync` будет введён в Module 5 после появления thread/race problem.  
**С телефона:** да

↑ [`README`](README.md)

Короткая идея для любопытства:

- `Send` roughly expresses that ownership of a value may be transferred between threads safely;
- `Sync` roughly expresses that shared references to a type may be used from multiple threads safely.

Это **не** значит «`Sync` = mutex» и не значит, что любой type с mutex automatically solves higher-level invariants.

Не учи/запоминай детали marker traits до Module 5. Здесь достаточно увидеть, что Rust продолжает кодировать concurrency contracts в type system.