# Разбор 1B.3

Типичный conflict:

```rust
let mut v = vec![1, 2, 3];
let first = &v[0];
// v.push(4);      // нельзя, если first ещё будет использоваться
println!("{first}");
```

Почему: `push` может reallocate buffer, и старый reference на element стал бы dangling. Rust не обязан доказывать, произойдёт ли resize именно сейчас — API mutation потенциально invalidates borrow.

Перестройка:

```rust
let mut v = vec![1, 2, 3];
let first = &v[0];
println!("{first}");
v.push(4);
```

После последнего использования `first` borrow может закончиться.
