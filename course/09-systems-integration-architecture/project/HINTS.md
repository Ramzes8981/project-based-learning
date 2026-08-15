# Capstone — Hints

## Hint 1

Не начинай код. Сначала requirements + state ownership.

## Hint 2

Reuse component **interfaces/ideas**, а не paste старые `main()` files together.

## Hint 3

Если persistence сложно, уменьшай guarantee/scope честно. Лучше простой correct append log with clear limitation, чем fake transactional DB.

## Hint 4

Когда p99 плохой, измерь queue wait отдельно от service work.

## Hint 5

Если хочется сразу second node, сначала покажи measured bottleneck one node и опиши state-consistency problem, который появится.
