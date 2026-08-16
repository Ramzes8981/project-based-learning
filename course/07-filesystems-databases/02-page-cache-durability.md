# 7.2 — Page cache, dirty data, `fsync` и durability

**Теория:** ~90 мин  
**Lab:** ~60 мин  
**С телефона:** да

← [`01-filesystem-names-inodes.md`](01-filesystem-names-inodes.md) · → [`03-fuse-userspace-filesystem.md`](03-fuse-userspace-filesystem.md)

## Цель

Отличать «write syscall принял bytes» от «выбранный failure model гарантирует сохранность данных».

## Data path

Упрощённо:

```text
application buffer
↓
libc stdio buffer (если используется)
↓
write/pwrite syscall
↓
kernel page cache: dirty pages
↓
filesystem/block layer
↓
device cache/controller/media
```

Успешный `write` означает, что операция выполнилась согласно syscall contract для переданных bytes. Это не универсальная гарантия пережить внезапную потерю питания.

## Page cache

Regular-file reads/writes обычно проходят через kernel cache, если не выбран специальный direct-I/O режим.

Read hit может не требовать device I/O. Write часто изменяет cached page и делает её dirty; writeback происходит позже.

Следствие:

```text
logical visibility != durable persistence
```

## `fsync`

`fsync(fd)` — explicit synchronization boundary для file data и metadata, необходимой для последующего retrieval, согласно OS/filesystem/device contract.

Он не превращает произвольную multi-file update sequence в transaction. Если обновление включает file content **и directory namespace**, reasoning должен включать оба объекта.

## `fdatasync`

Идея похожа, но цель — синхронизировать file data и только metadata, необходимую для retrieval. Не используй различие как микрооптимизацию до появления измеримой необходимости.

## Rename: visibility vs persistence

Rename/replacement в одной filesystem даёт сильную namespace atomicity для имени: observer не должен видеть «половину старого имени + половину нового файла». Но atomic namespace switch и сохранность этого switch после power loss — разные свойства.

## Snapshot replacement pattern

На Linux/Unix-подобной системе типичная схема для durable replacement:

```text
create temp in same directory/filesystem
write complete contents with robust short-write handling
fsync(temp) when durability required
rename(temp, target)
fsync(parent directory) when directory-entry durability required
```

Это **failure-model pattern**, не вечная формула для любой storage stack. Production code сверяет exact platform/filesystem guarantees.

## Failure models

### Application/process crash

Kernel остаётся жив, page cache сохраняется. `kill -9` не моделирует power loss.

### OS crash / power loss

Volatile kernel/device state может исчезнуть.

### Torn/partial application operation

Даже без power loss process может завершиться между несколькими page writes.

Database recovery нужен именно потому, что logical operation часто состоит из нескольких physical updates.

## Partial I/O

`pwrite/read` не освобождают от проверки return value. Pager должен либо loop до полного page transfer, либо иметь explicit policy/error, не считать short operation успехом.

## Lab

Сделай snapshot writer: temporary file → complete write → file sync → rename → optional directory sync. Составь failure matrix:

```text
before temp sync
after temp sync before rename
after rename before directory sync
after all requested sync points
```

Не симулируй power loss основной машины.

## Exit check

Для фразы «данные записаны» уточняй level: userspace buffer, kernel cache, namespace visibility или durable state относительно конкретного failure model.
