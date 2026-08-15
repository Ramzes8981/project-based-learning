# Разбор 1B.8

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0_i64));
    let mut handles = Vec::new();

    for _ in 0..4 {
        let counter = Arc::clone(&counter);
        handles.push(thread::spawn(move || {
            let mut guard = counter.lock().expect("mutex poisoned");
            *guard += 1;
        }));
    }

    for h in handles {
        h.join().expect("worker panicked");
    }

    assert_eq!(*counter.lock().unwrap(), 4);
}
```

Каждый thread owns свой `Arc` clone. Underlying allocation освобождается, когда последний strong `Arc` dropped. Mutex сериализует access к inner counter, но не предотвращает логические deadlocks при более сложном locking design.
