# Hash Table in C — SPEC

Эта версия эволюционирует из MiniKV Module 0.

## Representation

Core implementation использует **open addressing + linear probing**.

Bucket должен различать минимум states:

- EMPTY;
- OCCUPIED;
- TOMBSTONE.

Table владеет dynamic bucket storage. Ownership keys/values должен быть явно задокументирован; для core рекомендуется, чтобы table владел собственными копиями.

## Required operations

- create/init;
- destroy;
- set/insert/update;
- get;
- delete;
- automatic growth;
- rehash;
- instrumentation.

## Required properties

- collisions корректны;
- delete не разрывает probe chains;
- probe loop всегда имеет termination condition;
- high load triggers growth before pathological full state;
- allocation failure does not silently destroy old valid table;
- string length/size arithmetic validated;
- no known leaks/UAF/OOB.

## Metrics

Минимум:

- size;
- capacity;
- tombstones;
- resize count;
- total probes или эквивалентная probe metric.

## Transfer

Одна самостоятельная feature: alternate probing, iterator, configurable threshold, shrink policy, probe histogram и т.п.
