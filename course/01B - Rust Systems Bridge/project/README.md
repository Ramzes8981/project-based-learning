# Rust MiniKV — ownership bridge

Проект начинается после 1B.6. Его цель — доказать, что ты понимаешь, как C contracts меняются в safe Rust.

## Behavior

Store supports:

```text
set key value
get key
delete key
len
```

Duplicate `set` replaces value. Missing lookup/delete returns explicit absence/status.

## Constraints unlocked by lessons

- after ownership/borrowing: no clone-as-bandage design;
- after `Option/Result`: absence/failure typed explicitly;
- after collections: owned `String` storage + borrowed `&str` lookup;
- `unsafe`/FFI **not required** for core project.

See [`SPEC.md`](SPEC.md), [`ACCEPTANCE.md`](ACCEPTANCE.md), [`TESTS.md`](TESTS.md), [`HINTS.md`](HINTS.md).