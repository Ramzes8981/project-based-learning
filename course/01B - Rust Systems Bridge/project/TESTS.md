# Rust MiniKV — Public scenarios

1. new Store is empty;
2. insert/get;
3. multiple entries;
4. update existing key;
5. missing key;
6. key/value at limit;
7. input over limit -> expected error variant;
8. delete/transfer feature;
9. borrowed lookup used read-only;
10. repeated tests under `cargo test`.

Дополнительный review проверяет API/ownership, а не только outputs.
