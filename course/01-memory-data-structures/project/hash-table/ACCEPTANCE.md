# Hash Table — Acceptance

## Correctness

- insert new key;
- update existing key;
- get existing/missing;
- delete existing/missing;
- multiple deliberate collisions;
- lookup past tombstones;
- insert can reuse tombstone according to documented policy;
- resize preserves all active data;
- repeated resizes;
- destroy cleans all owned memory.

## Safety

- canonical warning flags clean;
- ASan/UBSan public scenarios clean;
- allocation size arithmetic checked;
- failure paths documented.

## Algorithms

README explains expected/worst lookup, load factor, probe clustering and rehash cost.

## Transfer

One non-copied feature + tests.

## Engineering review

Explain API, ownership, invalidation rules, memory overhead, failure behavior and 10×/100× dataset implications.
