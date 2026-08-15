# 7.2 — Page cache, dirty data, `fsync` и durability

**Теория:** ~85 мин  
**Lab:** ~60 мин  
**С телефона:** да

← [`01-filesystem-names-inodes.md`](01-filesystem-names-inodes.md) · → [`03-fuse-userspace-filesystem.md`](03-fuse-userspace-filesystem.md)

## Цель

Отличать «write syscall успешно принял bytes» от «данные переживут crash/power loss».

## Несколько слоёв buffering

Упрощённый data path:

```text
application buffer
  ↓
libc buffering (если stdio)
  ↓
syscall
  ↓
OS page cache / dirty pages
  ↓
filesystem / block layer
  ↓
storage device caches/media
```

`write()` success обычно означает, что kernel принял data according to API contract; это не универсальная гарантия physical durability.

## Page cache

Regular file data часто кэшируется pages в RAM.

Read:

- cache hit → storage I/O может не понадобиться;
- miss → kernel загружает data.

Write:

- page изменяется/становится dirty;
- kernel может flush later.

Это повышает throughput и coalescing, но разделяет logical write completion и durable persistence.

## `fsync`

`fsync(fd)` запрашивает synchronized completion file data + metadata, необходимой для retrieval, в рамках filesystem/device contract.

Но durable update **нескольких** filesystem objects всё равно требует продуманной sequence. Например запись нового file + rename может потребовать sync file и directory depending desired crash guarantee/filesystem semantics.

Не превращай одну последовательность в «вечный универсальный рецепт» без platform guarantees.

## `fdatasync`

Схож с fsync, но может не ждать metadata, не нужную для subsequent data retrieval. Точные guarantees зависят от standard/platform.

## Rename

Rename в одной filesystem namespace обеспечивает strong namespace atomicity properties для имени: не должно быть промежуточного состояния, где target replacement наполовину виден как два смешанных path contents. Но atomic visibility ≠ crash durability на storage.

POSIX описывает `rename()` как операцию изменения имени, а synchronized persistence — отдельные interfaces. citeturn259580search0turn259580search2

## Safe replacement pattern intuition

Для config/file snapshot:

```text
create temp in same directory/filesystem
write full content
validate
fsync(temp) if durability required
rename(temp, target)
fsync(directory) if target-name durability is required by chosen platform/filesystem contract
```

Это conceptual Linux/Unix pattern; production implementation должна сверяться с конкретной filesystem semantics.

## Crash vs process crash

Process crash и machine power loss — разные failure models.

- process crash: kernel/page cache живы;
- OS/power loss: volatile kernel state исчезает.

Тест «kill -9 process и file сохранился» не доказывает power-loss durability.

## Partial writes

Regular file write тоже может fail/partial. Database pager использует robust positional I/O loops или чётко проверяет complete page transfer.

## Lab

Напиши маленький snapshot writer:

- temp file;
- write content;
- `fsync` temp;
- rename;
- inspect final content.

Затем составь failure matrix: crash before sync, after sync before rename, after rename before directory sync.

Не симулируй power loss реальной машины.

## Causal questions

1. Почему `close()` и `write()` success не равны durability guarantee?
2. Почему process kill и power loss — разные experiments?
3. Что даёт rename и чего не даёт?
4. Почему DB recovery design не может состоять только из `fsync` после каждого произвольного write?

## Exit check

Для фразы «данные записаны» уточни: в application buffer, kernel cache, filesystem namespace или durable media?
