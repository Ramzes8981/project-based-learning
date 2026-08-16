# 1B.9 — `Send`, `Sync` и preview concurrency safety

**Теория:** ~60 мин  
**Упражнение:** ~45 мин  
**С телефона:** да

← [`08-unsafe-raw-pointers-ffi.md`](08-unsafe-raw-pointers-ffi.md) · → [`10-module-checkpoint.md`](10-module-checkpoint.md)

## Цель

Связать ownership/lifetimes с threads, не подменяя будущий concurrency module.

## Data race

Conceptually: concurrent accesses к одной memory location, минимум один write, без требуемой synchronization. В C ordinary data race приводит к undefined behavior. Safe Rust не позволяет многие такие sharing patterns выразить через safe references/types.

## `Send`

`T: Send` означает, что ownership `T` можно безопасно передавать между threads согласно trait contract.

## `Sync`

`T: Sync` означает, что shared `&T` можно безопасно использовать между threads. Упрощённо `T: Sync` связано с тем, что `&T: Send`.

Это не runtime locks.

## `Rc` / `Arc`

`Rc<T>` — single-thread reference counting. `Arc<T>` — atomic shared ownership для cross-thread use, когда свойства `T` это допускают.

`Arc<T>` не делает mutation безопасной автоматически. Частый composition:

```text
Arc<Mutex<T>>
```

`Arc` отвечает за shared ownership; `Mutex` — за synchronized mutable access.

## Guard и RAII

`Mutex::lock()` возвращает guard; Drop guard освобождает lock. Но panic/poisoning/error handling всё равно требуют осознанной policy.

## Threads и lifetime

Long-lived spawned thread не может без гарантии удерживать borrow local stack data. Scoped threads позволяют borrow, потому что scope гарантирует join до окончания borrowed data.

## Упражнение

Shared counter через `Arc<Mutex<i64>>`: несколько threads, increments, join, итоговая проверка.

Письменно объясни ownership Arc clones, counter lifetime и роль mutex.

Разбор: [`09-send-sync-concurrency-preview.solution.md`](09-send-sync-concurrency-preview.solution.md).

## Exit check

Почему Rust может предотвращать data races compile-time, но не гарантирует отсутствие deadlock или плохой lock granularity?
