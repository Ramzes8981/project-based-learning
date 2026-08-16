# 1.17 — Trie / Prefix Tree

**Теория:** ~75 мин  
**Lab:** ~90 мин  
**С телефона:** теория — да

← [`16-string-searching.md`](16-string-searching.md) · → [`18-probability-for-hashing.md`](18-probability-for-hashing.md)

## Цель

Понять структуру, где path кодирует prefix key, и увидеть trade-off между быстрым prefix traversal и расходом памяти.

## Идея

Keys `car`, `cat`, `dog` разделяют prefix `ca`:

```text
root
├─ c
│  └─ a
│     ├─ r*
│     └─ t*
└─ d
   └─ o
      └─ g*
```

`*` означает terminal key.

Search cost зависит от длины key `L`, а не числа всех stored keys напрямую: порядка `O(L)` при constant-time child lookup.

## Child representation

Варианты:

- fixed array из 26/256 pointers — быстрый index, дорого по памяти;
- sorted dynamic list/vector — компактнее, child lookup дороже;
- hash map — дополнительная complexity/overhead.

Для учебного C lab можно ограничить alphabet `a..z`, чтобы сфокусироваться на ownership.

## Ownership

Tree владеет всеми nodes. Destroy рекурсивно/итеративно освобождает children перед parent. Keys могут не храниться целиком: path уже кодирует символы.

## Prefix queries

После traversal prefix node можно перечислить descendants и получить autocomplete-like behavior.

## Lab

Спроектируй небольшой Trie API и реализуй:

- insert lowercase word;
- contains exact word;
- starts_with;
- destroy;
- tests + sanitizer run.

Не копируй готовую implementation из интернета. Сначала выбери child representation и запиши memory estimate для одной node.

Разбор: [`17-trie.solution.md`](17-trie.solution.md).

## Causal questions

1. Почему Trie может тратить намного больше памяти, чем хранит символов?
2. Чем terminal marker отличается от leaf?
3. Почему `car` может быть key и одновременно prefix `cart`?
4. Как representation children меняет constants и memory?

## Exit check

Сравни Trie, Hash Table и BST для exact lookup, ordered iteration и prefix query.
