# 1B.8 — `Send`, `Sync` и preview concurrency safety

**Теория:** ~55 мин  
**Упражнение:** ~40 мин  
**С телефона:** да

← [`07-unsafe-raw-pointers-ffi.md`](07-unsafe-raw-pointers-ffi.md) · → [`09-module-checkpoint.md`](09-module-checkpoint.md)

## Цель

Увидеть, как ownership model распространяется на threads, не проходя весь concurrency module раньше времени.

## Data race

Data race conceptually требует concurrent accesses к одному memory location, минимум один write и отсутствие корректной synchronization.

C/Pthreads позволяет написать такую программу; behavior становится ошибочным/undefined по memory model.

Safe Rust старается не позволить отправить/shared type между threads, если compiler не может подтвердить соответствующие marker-trait properties.

## `Send`

Type `T: Send` означает, что ownership value этого типа можно безопасно передавать между threads согласно unsafe trait contract.

## `Sync`

`T: Sync` означает, что shared reference `&T` можно безопасно использовать из нескольких threads.

Упрощённая связь:

```text
T is Sync roughly means &T is Send
```

Но не превращай marker traits в магические runtime locks. Они описывают type-level thread-safety properties, а synchronization behaviour всё равно задают конкретные types.

## `Rc` vs `Arc`

`Rc<T>` — reference counting для single-threaded ownership sharing и не `Send/Sync` для cross-thread use.

`Arc<T>` — atomic reference counting, пригодный для cross-thread shared ownership при соответствующих свойствах `T`.

Но `Arc<T>` сам по себе не делает mutable `T` thread-safe.

Для mutation обычно нужна внутренняя synchronization:

```text
Arc<Mutex<T>>
```

Это composition ownership + locking.

## `MutexGuard` и RAII

Rust `Mutex::lock()` возвращает guard. Пока guard жив — lock held; при Drop guard lock освобождается.

Это тот же RAII/Drop принцип, теперь применён к synchronization resource.

## Scope threads

`std::thread::spawn` обычно требует `'static` captured data, потому что thread потенциально переживёт текущую function. Scoped threads могут безопасно borrow stack data, если scope гарантирует join до выхода.

Это хороший пример, как lifetime и concurrency связаны.

## Causal questions

1. Почему `Arc<T>` не эквивалентен `Arc<Mutex<T>>`?
2. Что `Send/Sync` гарантируют, а чего не гарантируют?
3. Почему ordinary reference на local data нельзя бездумно передать в arbitrary long-lived thread?
4. Как Drop помогает mutex unlock?

## Упражнение

Создай shared counter через `Arc<Mutex<i64>>`, запусти несколько threads, increment и join.

Затем ответь письменно:

- кто owns `Arc` clones?
- кто owns underlying counter?
- когда counter освобождается?
- что именно защищает `Mutex`?

Разбор: [`08-send-sync-concurrency-preview.solution.md`](08-send-sync-concurrency-preview.solution.md).

## Exit check

Сможешь ли ты объяснить, почему Rust предотвращает часть data races compile-time, но всё ещё позволяет deadlocks и плохую lock granularity?
